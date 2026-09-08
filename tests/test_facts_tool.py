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


if __name__ == "__main__":
    unittest.main()
