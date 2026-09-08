"""facts_tool:事实卡录入/校验/索引工具(仅标准库)。见 sop/facts-record.md。"""
import re
from pathlib import Path

CARD_CLASSES = {"product", "advantage", "certification", "case", "company", "price"}
STATUSES = {"draft", "approved", "obsolete"}
REQUIRED = ["id", "class", "title", "status", "source"]
_ID_RE = re.compile(r"^F-([A-Z]+)-(\d{3})$")
_IGNORED = {"_template.md", "_index.md"}


def facts_dir_for(base: Path) -> Path:
    return base / "content" / "facts"


def parse_frontmatter(text):
    m = re.match(r"\A---\n(.*?)\n---\n?(.*)\Z", text, re.DOTALL)
    if not m:
        return None, text
    fm, body = m.groups()
    fields = {}
    for line in fm.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        k, v = line.split(":", 1)
        k, v = k.strip(), v.strip()
        if v.startswith("[") and v.endswith("]"):
            fields[k] = [i.strip().strip('"').strip("'") for i in v[1:-1].split(",") if i.strip()]
        else:
            fields[k] = v.strip('"').strip("'")
    return fields, body


def list_cards(base: Path):
    facts = facts_dir_for(base)
    if not facts.exists():
        return []
    return sorted(
        p for p in facts.rglob("*.md")
        if p.name not in _IGNORED and p.parent != facts
    )


def next_id(base: Path, cls: str) -> str:
    if cls not in CARD_CLASSES:
        raise ValueError(f"未知类别:{cls};可用 {sorted(CARD_CLASSES)}")
    cls_upper = cls.upper()
    hi = 0
    for p in list_cards(base):
        m = _ID_RE.match(p.stem)
        if m and m.group(1) == cls_upper:
            hi = max(hi, int(m.group(2)))
    return f"F-{cls_upper}-{hi + 1:03d}"


DEFAULT_TEMPLATE = """---
id: F-CLASS-000
class: class
title: ""
status: draft
reviewer: ""
reviewed_at: ""
markets: []
keywords: []
source: ""
glossary_terms: []
related_facts: []
---
## zh
(源语事实内容,默认中文,主源)

## en
(已核验英文译文)

## de
(按需;无则删除本小节)
"""


def create_card(base: Path, cls: str) -> Path:
    nid = next_id(base, cls)
    facts = facts_dir_for(base)
    tpl = facts / "_template.md"
    text = tpl.read_text(encoding="utf-8") if tpl.exists() else DEFAULT_TEMPLATE
    text = re.sub(r"^id: .*$", f"id: {nid}", text, count=1, flags=re.M)
    text = re.sub(r"^class: .*$", f"class: {cls}", text, count=1, flags=re.M)
    d = facts / cls
    d.mkdir(parents=True, exist_ok=True)
    p = d / f"{nid}.md"
    p.write_text(text, encoding="utf-8")
    return p


def validate_card(base: Path, card: Path) -> list[str]:
    errors = []
    text = card.read_text(encoding="utf-8")
    fields, body = parse_frontmatter(text)
    if fields is None:
        return ["无 YAML frontmatter(需 --- ... ---)"]
    fname = card.name
    for f in REQUIRED:
        v = fields.get(f, "")
        if isinstance(v, list) and not v:
            errors.append(f"必填字段缺值:{f}")
        elif isinstance(v, str) and not v.strip():
            errors.append(f"必填字段缺值:{f}")
    iid = fields.get("id", "") or ""
    m = _ID_RE.match(iid)
    if not m:
        errors.append(f"id 非法:{iid}(应为 F-<CLASS>-<nnn>)")
    else:
        cls_expected = m.group(1).lower()
        if fields.get("class") != cls_expected:
            errors.append(f"class 字段({fields.get('class')})与 id 前缀({m.group(1)})不一致")
    if not _ID_RE.match(card.stem):
        errors.append(f"文件名非编号格式:{fname}(应为 F-<CLASS>-<nnn>.md)")
    cls = fields.get("class")
    if cls and cls not in CARD_CLASSES:
        errors.append(f"class 非法:{cls}")
    st = fields.get("status")
    if st and st not in STATUSES:
        errors.append(f"status 非法:{st}(应为 {sorted(STATUSES)})")
    if st == "approved":
        if not (fields.get("reviewer") or "").strip():
            errors.append("approved 状态缺 reviewer(必填)")
        if not (fields.get("reviewed_at") or "").strip():
            errors.append("approved 状态缺 reviewed_at(必填)")
    if not re.search(r"^##\s+zh\s*$", body, re.M):
        errors.append("正文缺 `## zh` 节")
    return sorted(set(errors))


def validate_all(base: Path) -> list[tuple[Path, list[str]]]:
    cards = list_cards(base)
    seen = {}
    results = []
    for p in cards:
        errs = validate_card(base, p)
        m = _ID_RE.match(p.stem)
        if m:
            iid = p.stem
            if iid in seen:
                errs.append(f"id 重复:{iid}(与 {seen[iid].relative_to(base)} 冲突)")
            else:
                seen[iid] = p
        results.append((p, errs))
    return results


def _cmd_new(base, args):
    p = create_card(base, args.cls)
    print(f"已建:{p.relative_to(base)}")
    print("三步录入:1) 填 frontmatter 与正文(必填 id/class/title/source;approved 需 reviewer) "
          "2) 补 zh/en(+de) 3) 校验:`python3 tools/facts_tool.py validate <该文件>`")


def build_index(base: Path) -> str:
    rows = []
    for p in list_cards(base):
        fields, _ = parse_frontmatter(p.read_text(encoding="utf-8"))
        if fields is None:
            fields = {}
        def esc(x): return (str(x).replace("|", "\\|") if x is not None else "")
        markets = ", ".join(fields.get("markets", []) or [])
        rows.append((p.name,
                     "| {id} | {cls} | {title} | {st} | {mk} | {src} |".format(
                         id=p.name, cls=fields.get("class", ""), title=esc(fields.get("title", "")),
                         st=fields.get("status", ""), mk=esc(markets), src=esc(fields.get("source", "")))))
    rows.sort()
    lines = [
        "<!-- AUTO-GENERATED by facts_tool index;勿手改 -->",
        "# 事实卡索引(_index)",
        "",
        f"- 共 {len(rows)} 张 · 生成:{__import__('datetime').datetime.now():%Y-%m-%d}",
        "",
        "| id | class | title | status | markets | source |",
        "|---|---|---|---|---|---|",
    ] + [r for _n, r in rows]
    return "\n".join(lines) + "\n"


def search_cards(base: Path, term: str):
    q = term.lower()
    out = []
    for p in list_cards(base):
        fields, body = parse_frontmatter(p.read_text(encoding="utf-8"))
        if fields is None:
            fields, body = {}, ""
        kws = " ".join(fields.get("keywords", []) or [])
        hay = f"{fields.get('title','')} {kws} {body}".lower()
        if q in hay:
            zh = ""
            m = re.search(r"^##\s+zh\s*\n(.*?)(?=^##\s|\Z)", body, re.S | re.M)
            if m:
                zh = m.group(1).strip()
            out.append((str(p.relative_to(base)), zh[:60]))
    return out


def main(argv=None):
    import argparse
    import sys
    parser = argparse.ArgumentParser(prog="facts_tool", description="事实卡录入/校验/索引工具")
    sub = parser.add_subparsers(dest="cmd", required=True)
    p_new = sub.add_parser("new", help="按类别新建一张卡")
    p_new.add_argument("cls", choices=sorted(CARD_CLASSES))
    p_val = sub.add_parser("validate", help="校验卡片(默认全部)")
    p_val.add_argument("paths", nargs="*", help="可选:一个或多个卡片文件路径")
    sub.add_parser("index", help="重建 content/facts/_index.md")
    p_search = sub.add_parser("search", help="检索")
    p_search.add_argument("term")
    args = parser.parse_args(argv)
    base = Path(__file__).resolve().parent.parent
    if args.cmd == "new":
        _cmd_new(base, args)
    elif args.cmd == "validate":
        if args.paths:
            files = [Path(a) for a in args.paths]
            failed = [(p, validate_card(base, p)) for p in files]
            failed = [(p, errs) for p, errs in failed if errs]
        else:
            failed = [(p, errs) for p, errs in validate_all(base) if errs]
            ok = len(list_cards(base)) - len(failed)
        if failed:
            for p, errs in failed:
                print(f"[FAIL] {p}")
                for e in errs:
                    print(f"   - {e}")
            sys.exit(1)
        else:
            print(f"全部通过({ok} 张)" if not args.paths else f"通过:{len(files)} 张")
    elif args.cmd == "index":
        idx = build_index(base)
        out = facts_dir_for(base) / "_index.md"
        out.write_text(idx, encoding="utf-8")
        n = len(list_cards(base))
        print(f"已重建 {out.relative_to(base)}(索引 {n} 张)")
    elif args.cmd == "search":
        hits = search_cards(base, args.term)
        if not hits:
            print(f"无匹配:{args.term}")
        else:
            for rel, snippet in hits:
                print(f"{rel}: {snippet}")


if __name__ == "__main__":
    main()
