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
