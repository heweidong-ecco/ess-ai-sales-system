import re, sys, tempfile, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from tools import facts_tool as ft


def make_tree():
    tmp = Path(tempfile.mkdtemp())
    (tmp / "content/facts").mkdir(parents=True)
    return tmp


class TestParseFrontmatter(unittest.TestCase):
    def test_parse_scalars_and_lists(self):
        text = "---\nid: F-PRODUCT-001\nclass: product\ntitle: \"柜 100kW\"\nmarkets: [EN, DE]\n---\n## zh\n正文"
        fields, body = ft.parse_frontmatter(text)
        self.assertEqual(fields["id"], "F-PRODUCT-001")
        self.assertEqual(fields["class"], "product")
        self.assertEqual(fields["title"], "柜 100kW")
        self.assertEqual(fields["markets"], ["EN", "DE"])
        self.assertTrue(body.lstrip().startswith("## zh"))

    def test_missing_frontmatter_returns_none(self):
        fields, body = ft.parse_frontmatter("# 没有头\n\nhi")
        self.assertIsNone(fields)

    def test_value_can_contain_colon(self):
        fields, _ = ft.parse_frontmatter("---\nsource: spec page 3: Para 2\n---\nx")
        self.assertEqual(fields["source"], "spec page 3: Para 2")


class TestNextId(unittest.TestCase):
    def test_empty_returns_001(self):
        base = make_tree()
        self.assertEqual(ft.next_id(base, "product"), "F-PRODUCT-001")

    def test_increments_over_existing(self):
        base = make_tree()
        d = base / "content/facts/product"; d.mkdir()
        (d / "F-PRODUCT-002.md").write_text("---\nid: F-PRODUCT-002\n---\n", encoding="utf-8")
        self.assertEqual(ft.next_id(base, "product"), "F-PRODUCT-003")

    def test_next_id_raises_when_class_reaches_999(self):
        base = make_tree()
        d = base / "content/facts/product"; d.mkdir(parents=True)
        (d / "F-PRODUCT-999.md").write_text("---\nid: F-PRODUCT-999\n---\n", encoding="utf-8")
        with self.assertRaises(RuntimeError):
            ft.next_id(base, "product")

    def test_ignores_non_cards(self):
        base = make_tree()
        (base / "content/facts/_template.md").write_text("x", encoding="utf-8")
        self.assertEqual(ft.list_cards(base), [])


class TestListCards(unittest.TestCase):
    def test_lists_only_class_cards_sorted(self):
        base = make_tree()
        d = base / "content/facts/company"; d.mkdir()
        (d / "F-COMPANY-002.md").write_text("a", encoding="utf-8")
        (d / "F-COMPANY-001.md").write_text("a", encoding="utf-8")
        (base / "content/facts/_template.md").write_text("t", encoding="utf-8")
        names = [p.name for p in ft.list_cards(base)]
        self.assertEqual(names, ["F-COMPANY-001.md", "F-COMPANY-002.md"])


class TestCreateCard(unittest.TestCase):
    def test_create_writes_card_under_class_dir(self):
        base = make_tree()
        p = ft.create_card(base, "product")
        self.assertEqual(p.name, "F-PRODUCT-001.md")
        self.assertEqual(p.parent, base / "content/facts/product")
        text = p.read_text(encoding="utf-8")
        self.assertIn("id: F-PRODUCT-001", text)
        self.assertIn("class: product", text)

    def test_create_second_card_increments(self):
        base = make_tree()
        ft.create_card(base, "certification")
        p2 = ft.create_card(base, "certification")
        self.assertEqual(p2.name, "F-CERTIFICATION-002.md")

    def test_create_rejects_unknown_class(self):
        base = make_tree()
        with self.assertRaises(ValueError):
            ft.create_card(base, "nope")


def write_card(base, cls, name, body):
    d = base / "content/facts" / cls
    d.mkdir(parents=True, exist_ok=True)
    p = d / name
    p.write_text(body, encoding="utf-8")
    return p


VALID = """---
id: F-PRODUCT-001
class: product
title: 柜 100kW
status: approved
reviewer: 张
reviewed_at: 2026-09-01
markets: [EN, DE]
source: 手册 p5
---
## zh
额定功率 100kW。

## en
Rated 100 kW.
"""


class TestValidate(unittest.TestCase):
    def test_valid_approved_card_ok(self):
        base = make_tree()
        p = write_card(base, "product", "F-PRODUCT-001.md", VALID)
        self.assertEqual(ft.validate_card(base, p), [])

    def test_missing_required_source_fails(self):
        base = make_tree()
        body = VALID.replace("source: 手册 p5\n", "")
        p = write_card(base, "product", "F-PRODUCT-001.md", body)
        errs = ft.validate_card(base, p)
        self.assertTrue(any("source" in e for e in errs))

    def test_bad_id_format_fails(self):
        base = make_tree()
        p = write_card(base, "product", "F-PRODUCT-001.md", VALID.replace("F-PRODUCT-001", "bad-id"))
        self.assertTrue(any("id" in e for e in ft.validate_card(base, p)))

    def test_approved_requires_reviewer_and_date(self):
        base = make_tree()
        body = VALID.replace("reviewer: 张\nreviewed_at: 2026-09-01\n", "")
        p = write_card(base, "product", "F-PRODUCT-001.md", body)
        errs = ft.validate_card(base, p)
        self.assertTrue(any("approved" in e and "reviewer" in e for e in errs))

    def test_missing_zh_section_fails(self):
        base = make_tree()
        body = VALID.split("## zh")[0]
        p = write_card(base, "product", "F-PRODUCT-001.md", body)
        self.assertTrue(any("zh" in e for e in ft.validate_card(base, p)))

    def test_class_mismatch_with_id_fails(self):
        base = make_tree()
        body = VALID.replace("id: F-PRODUCT-001", "id: F-CERTIFICATION-001")
        p = write_card(base, "product", "F-PRODUCT-001.md", body)
        self.assertTrue(any("class" in e for e in ft.validate_card(base, p)))

    def test_duplicate_ids_detected_globally(self):
        base = make_tree()
        write_card(base, "product", "F-PRODUCT-001.md", VALID)
        dup = VALID.replace("class: product\ntitle: 柜 100kW", "class: company\ntitle: 公司资质")
        write_card(base, "company", "F-PRODUCT-001.md", dup)
        results = ft.validate_all(base)
        self.assertTrue(any("重复" in e for _p, errs in results for e in errs))

    def test_filename_mismatch_with_content_id_fails(self):
        base = make_tree()
        body = VALID.replace("id: F-PRODUCT-001", "id: F-PRODUCT-002")
        p = write_card(base, "product", "F-PRODUCT-001.md", body)
        errs = ft.validate_card(base, p)
        self.assertTrue(any("文件名" in e and "不一致" in e for e in errs))

    def test_directory_mismatch_with_class_fails(self):
        base = make_tree()
        body = VALID.replace("id: F-PRODUCT-001", "id: F-CERTIFICATION-001").replace(
            "class: product", "class: certification")
        p = write_card(base, "product", "F-CERTIFICATION-001.md", body)
        errs = ft.validate_card(base, p)
        self.assertTrue(any("目录" in e and "不一致" in e for e in errs))

    def test_same_content_id_across_filenames_flagged_duplicate(self):
        base = make_tree()
        write_card(base, "product", "F-PRODUCT-001.md", VALID)
        dup = VALID.replace("title: 柜 100kW", "title: 同 id 另一张")
        write_card(base, "product", "F-PRODUCT-002.md", dup)
        results = ft.validate_all(base)
        self.assertTrue(any("重复" in e for _p, errs in results for e in errs))


class TestIndexSearch(unittest.TestCase):
    def test_index_lists_cards_sorted_with_fields(self):
        base = make_tree()
        write_card(base, "product", "F-PRODUCT-001.md", VALID)
        idx = ft.build_index(base)
        self.assertIn("F-PRODUCT-001", idx)
        self.assertIn("product", idx)
        self.assertLess(idx.index("F-PRODUCT-001"), idx.index("| product |"))

    def test_index_id_column_uses_content_id_without_md(self):
        base = make_tree()
        write_card(base, "product", "F-PRODUCT-001.md", VALID)
        idx = ft.build_index(base)
        rows = [l for l in idx.splitlines() if l.startswith("| F-")]
        self.assertEqual(len(rows), 1)
        self.assertTrue(rows[0].startswith("| F-PRODUCT-001 |"))
        self.assertNotIn(".md", rows[0])

    def test_index_excludes_template(self):
        base = make_tree()
        (base / "content/facts/_template.md").write_text(ft.DEFAULT_TEMPLATE, encoding="utf-8")
        write_card(base, "product", "F-PRODUCT-001.md", VALID)
        idx = ft.build_index(base)
        self.assertNotIn("_template", idx)
        self.assertNotIn("F-CLASS-000", idx)

    def test_search_matches_title_and_body_ci(self):
        base = make_tree()
        write_card(base, "product", "F-PRODUCT-001.md", VALID)
        self.assertTrue(any("F-PRODUCT-001" in p for p, _ in ft.search_cards(base, "100KW")))
        self.assertTrue(any("F-PRODUCT-001" in p for p, _ in ft.search_cards(base, "柜")))

    def test_search_matches_zh_body_with_truncated_snippet(self):
        base = make_tree()
        write_card(base, "product", "F-PRODUCT-001.md", VALID)
        hits = ft.search_cards(base, "额定功率")
        matched = [(p, s) for p, s in hits if "F-PRODUCT-001" in p]
        self.assertTrue(matched, "正文命中 zh 段应有结果")
        for _p, snippet in matched:
            self.assertLessEqual(len(snippet), 60)
            self.assertTrue(snippet.startswith("额定功率"))
            self.assertEqual(snippet, "额定功率 100kW。")

    def test_search_no_match_empty(self):
        base = make_tree()
        write_card(base, "product", "F-PRODUCT-001.md", VALID)
        self.assertEqual(ft.search_cards(base, "qqqnotexist"), [])


class TestEndToEnd(unittest.TestCase):
    def test_three_steps_full(self):
        base = make_tree()
        p = ft.create_card(base, "product")           # step1 new:content/facts/product/F-PRODUCT-001.md
        p.write_text(VALID, encoding="utf-8")         # step2 填(zh/en/source/reviewer/status)
        self.assertEqual(ft.validate_card(base, p), [])   # step3a 校验通过
        idx = ft.build_index(base)
        self.assertIn(p.stem, idx)                        # step3b 入索引(按内容 id,不带 .md),可检索
        self.assertNotIn(p.name, idx)                     # 索引 id 列不再带 .md


if __name__ == "__main__":
    unittest.main()
