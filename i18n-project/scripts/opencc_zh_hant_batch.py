#!/usr/bin/env python3
"""简体 Markdown/JSON → zh-Hant（OpenCC s2twp）。
产出：site/docs/zh-Hant/… 与 theme/locales/zh-Hant/…；不改简体真源。
用法：
  python3 opencc_zh_hant_batch.py
  python3 opencc_zh_hant_batch.py part1/01-what-is.md
  python3 opencc_zh_hant_batch.py --json home.json
"""
from __future__ import annotations
import json, re, sys
from pathlib import Path

try:
    from opencc import OpenCC
except ImportError:
    sys.exit("需要: pip install opencc-python-reimplemented")

ROOT = Path(__file__).resolve().parents[2]
PROJ = Path(__file__).resolve().parents[1]
SRC_ROOT = ROOT / "site" / "docs"
OUT_ROOT = SRC_ROOT / "zh-Hant"
THEME = SRC_ROOT / ".vitepress" / "theme"
THEME_LOC = THEME / "locales" / "zh-Hant"
TSV = PROJ / "SOURCE_PAGES.tsv"
GLOSSARY = PROJ / "glossary" / "DO_NOT_TRANSLATE.txt"
FENCE_RE = re.compile(r"(```[\s\S]*?```|`[^`]+`)")

def load_dnt() -> list[str]:
    if not GLOSSARY.exists():
        return []
    return [ln.strip() for ln in GLOSSARY.read_text(encoding="utf-8").splitlines() if ln.strip() and not ln.startswith("#")]

def protect(text: str, terms: list[str]) -> tuple[str, dict[str, str]]:
    mapping = {}
    for i, term in enumerate(sorted(terms, key=len, reverse=True)):
        if term and term in text:
            key = f"__DNT_{i}__"
            mapping[key] = term
            text = text.replace(term, key)
    return text, mapping

def convert_text(src: str, cc: OpenCC, terms: list[str]) -> str:
    parts = FENCE_RE.split(src)
    out = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            out.append(part)
            continue
        p, m = protect(part, terms)
        c = cc.convert(p)
        for k, v in m.items():
            c = c.replace(k, v)
        out.append(c)
    return "".join(out)

def convert_json_obj(obj, cc, terms):
    if isinstance(obj, str):
        return convert_text(obj, cc, terms)
    if isinstance(obj, list):
        return [convert_json_obj(x, cc, terms) for x in obj]
    if isinstance(obj, dict):
        # 键名不译；link 等以 / 开头的路径不译
        out = {}
        for k, v in obj.items():
            if k in ("link", "href", "url", "src", "path") and isinstance(v, str):
                out[k] = v
            else:
                out[k] = convert_json_obj(v, cc, terms)
        return out
    return obj

def rel_from_tsv(line: str) -> str | None:
    line = line.strip()
    if not line or line.startswith("#"):
        return None
    path = line.split("\t")[0].strip()
    return path[len("site/docs/"):] if path.startswith("site/docs/") else path

def main() -> None:
    cc = OpenCC("s2twp")
    terms = load_dnt()
    args = sys.argv[1:]
    if args and args[0] == "--json":
        names = args[1:] or ["home.json", "tools.json", "bots.json", "ecosystem.json", "changelog.json", "funnel.json"]
        ok = fail = 0
        for name in names:
            src = THEME / name
            if not src.is_file():
                print(f"SKIP {src}"); fail += 1; continue
            data = json.loads(src.read_text(encoding="utf-8"))
            out = convert_json_obj(data, cc, terms)
            dst = THEME_LOC / name
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
            print(f"OK json {name} → theme/locales/zh-Hant/{name}")
            ok += 1
        print(f"done json ok={ok} fail={fail}")
        return

    if args:
        targets = args
    else:
        targets = [r for line in TSV.read_text(encoding="utf-8").splitlines() if (r := rel_from_tsv(line))]

    ok = fail = 0
    for rel in targets:
        src = SRC_ROOT / rel
        dst = OUT_ROOT / rel
        if not src.is_file():
            print(f"SKIP missing {src}"); fail += 1; continue
        text = convert_text(src.read_text(encoding="utf-8"), cc, terms)
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(text, encoding="utf-8")
        print(f"OK {rel}"); ok += 1
    print(f"done md ok={ok} fail={fail} out={OUT_ROOT}")

if __name__ == "__main__":
    main()
