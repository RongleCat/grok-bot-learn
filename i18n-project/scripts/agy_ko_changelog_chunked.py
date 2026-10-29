#!/usr/bin/env python3
"""Translate changelog.json to ko via meta + official chunks (ARG_MAX workaround)."""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path("/workspace/grok-bot-learn")
PROJ = ROOT / "i18n-project"
THEME = ROOT / "site/docs/.vitepress/theme"
SRC = THEME / "changelog.json"
OUT = THEME / "locales/ko/changelog.json"
BACKUP = PROJ / "backups/ko/locales/changelog.json"
WORKDIR = PROJ / "work/ko"
GLOSSARY = PROJ / "glossary/DO_NOT_TRANSLATE.txt"
MODEL = os.environ.get("AGY_MODEL", "gemini-3.8-flash-high")
LOG = Path(os.environ.get("KO_LOG", str(PROJ / "logs/agy-ko-full.log")))
CHUNK = 20
LOCALE = "ko"
LANG = "Korean"


def log(msg: str) -> None:
    line = msg if msg.endswith("\n") else msg + "\n"
    sys.stdout.write(line)
    sys.stdout.flush()
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a", encoding="utf-8") as f:
        f.write(line)


def strip_fence(raw: str) -> str:
    raw = raw.strip()
    raw = re.sub(r"^```(?:json)?\s*", "", raw)
    raw = re.sub(r"\s*```$", "", raw)
    return raw.strip()


def sanitize_json_text(raw: str) -> str:
    """Escape bare control chars that models sometimes leave inside string values.

    Walks the text and, when inside a JSON string, replaces unescaped U+0000–U+001F
    with \\u00XX (except already-escaped sequences). Outside strings, whitespace
    newlines/tabs are left alone.
    """
    out: list[str] = []
    i = 0
    n = len(raw)
    in_str = False
    while i < n:
        ch = raw[i]
        if not in_str:
            out.append(ch)
            if ch == '"':
                in_str = True
            i += 1
            continue
        # in string
        if ch == "\\":
            # keep escape + next char as-is when present
            out.append(ch)
            i += 1
            if i < n:
                out.append(raw[i])
                i += 1
            continue
        if ch == '"':
            out.append(ch)
            in_str = False
            i += 1
            continue
        o = ord(ch)
        if o < 32:
            out.append(f"\\u{o:04x}")
            i += 1
            continue
        out.append(ch)
        i += 1
    return "".join(out)


def parse_json_out(path: Path):
    raw = strip_fence(path.read_text(encoding="utf-8"))
    try:
        return json.loads(raw, strict=False)
    except json.JSONDecodeError as e1:
        log(f"[WARN] json.loads strict=False failed on {path.name}: {e1}; sanitizing controls")
        cleaned = sanitize_json_text(raw)
        try:
            return json.loads(cleaned, strict=False)
        except json.JSONDecodeError as e2:
            # last resort: drop remaining bare controls outside sanitizer gaps
            cleaned2 = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", " ", cleaned)
            try:
                return json.loads(cleaned2, strict=False)
            except json.JSONDecodeError:
                raise e2 from e1


def run_agy(prompt: str, out_path: Path) -> None:
    prompt_path = out_path.with_suffix(".prompt.txt")
    tmp_out = out_path.with_suffix(".tmp.txt")
    prompt_path.write_text(prompt, encoding="utf-8")
    env = os.environ.copy()
    env["GEMINI_FORCE_FILE_STORAGE"] = "true"
    code = r"""
import os, subprocess, sys
from pathlib import Path
model, prompt_path, tmp_out = sys.argv[1], sys.argv[2], sys.argv[3]
prompt = open(prompt_path, encoding='utf-8').read()
env = os.environ.copy()
env['GEMINI_FORCE_FILE_STORAGE'] = 'true'
r = subprocess.run(
    ['agy', '--model', model, '--output-format', 'text', '--dangerously-skip-permissions', f'-p={prompt}'],
    capture_output=True, text=True, env=env
)
sys.stderr.write(r.stderr or '')
if r.returncode != 0:
    sys.stderr.write(f'agy exit {r.returncode}\n')
ok = bool(r.returncode == 0 and r.stdout and r.stdout.strip())
body = ''
if r.stdout:
    body = r.stdout if r.stdout.endswith('\n') else r.stdout + '\n'
Path(tmp_out).write_text(body, encoding='utf-8')
sys.exit(0 if ok else 1)
"""
    last_err = None
    for attempt in range(1, 3):
        r = subprocess.run(
            ["python3", "-c", code, MODEL, str(prompt_path), str(tmp_out)],
            capture_output=True,
            text=True,
            env=env,
        )
        if r.stderr:
            log(r.stderr.rstrip("\n"))
        if r.returncode == 0 and tmp_out.exists() and tmp_out.stat().st_size > 0:
            out_path.write_text(tmp_out.read_text(encoding="utf-8"), encoding="utf-8")
            return
        last_err = f"attempt {attempt} rc={r.returncode}"
        log(f"[RETRY-CHUNK] {out_path.name} {last_err}")
        time.sleep(3)
    raise RuntimeError(f"agy failed for {out_path.name}: {last_err}")


def build_prompt(label: str, payload) -> str:
    gloss = GLOSSARY.read_text(encoding="utf-8")
    body = json.dumps(payload, ensure_ascii=False, indent=2)
    return (
        f"Translate JSON UI strings for Grok Bot learning site (bot.fmcat.top) into {LANG} ({LOCALE}).\n"
        "Rules: keep JSON keys unchanged; keep link/href/url/src/path/id/version/date/platform string values unchanged; "
        "translate only human-readable string values (title, points, full nested text, summary, lead, note, etc).\n"
        "Output ONLY valid JSON: no markdown fence; escape newlines inside strings as \\n; no raw control characters.\n"
        "Do NOT translate DO_NOT_TRANSLATE terms. Do NOT use tools, shell, or browse.\n"
        f"=== DO_NOT_TRANSLATE ===\n{gloss}\n=== END ===\n"
        f"=== SOURCE JSON ===\n{body}\n=== END ===\n"
    )


def restore_identity(src_item: dict, dst_item: dict) -> dict:
    out = dict(dst_item) if isinstance(dst_item, dict) else {}
    for k in ("id", "url", "date", "version", "platform"):
        if k in src_item:
            out[k] = src_item[k]
    return out


def load_or_translate(label: str, payload, outp: Path, expect_list: bool, expect_len: int | None):
    """Reuse existing chunk file if it parses; else agy (+1 retry on parse/len fail)."""
    prompt = build_prompt(label, payload)

    def try_parse():
        obj = parse_json_out(outp)
        if expect_list:
            if not isinstance(obj, list):
                raise ValueError(f"expected list got {type(obj)}")
            if expect_len is not None and len(obj) != expect_len:
                raise ValueError(f"len {len(obj)} != {expect_len}")
        return obj

    if outp.exists() and outp.stat().st_size > 0:
        try:
            obj = try_parse()
            log(f"[RESUME-CHUNK] {label} from {outp.name} ({outp.stat().st_size} bytes)")
            return obj
        except Exception as e:
            log(f"[WARN] resume parse failed for {label}: {e}; re-translating")

    log(f"[CHUNK] {label} prompt_bytes={len(prompt.encode())} starting {time.strftime('%H:%M:%S')}")
    run_agy(prompt, outp)
    try:
        obj = try_parse()
    except Exception as e:
        log(f"[WARN] {label} parse/len fail after agy: {e}; retry agy once")
        run_agy(prompt, outp)
        obj = try_parse()
    log(f"[OK-CHUNK] {label} out_bytes={outp.stat().st_size}")
    return obj


def main() -> int:
    WORKDIR.mkdir(parents=True, exist_ok=True)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    BACKUP.parent.mkdir(parents=True, exist_ok=True)

    if OUT.exists() and OUT.stat().st_size > 0:
        # verify quickly; if bad, wipe and continue
        try:
            existing = json.loads(OUT.read_text(encoding="utf-8"))
            if (
                isinstance(existing.get("official"), list)
                and len(existing["official"]) == 79
                and isinstance(existing.get("ours"), list)
                and len(existing["ours"]) == 6
            ):
                log(f"[SKIP-JSON] changelog.json already at {OUT} ({OUT.stat().st_size} bytes)")
                return 0
        except Exception:
            pass
        log(f"[WARN] existing {OUT} incomplete/invalid; rebuilding")

    src = json.loads(SRC.read_text(encoding="utf-8"))
    log(f"[START-JSON-CHUNKED] changelog.json {time.strftime('%Y-%m-%d %H:%M:%S %z')} CHUNK={CHUNK}")

    meta_payload = {
        "updated": src.get("updated"),
        "ui": src.get("ui", {}),
        "ours": src.get("ours", []),
    }
    meta_out = WORKDIR / "changelog-meta-out.txt"
    meta = load_or_translate("meta", meta_payload, meta_out, expect_list=False, expect_len=None)
    if not isinstance(meta, dict):
        raise RuntimeError("meta is not an object")

    src_ours = src.get("ours", [])
    if isinstance(meta.get("ours"), list) and len(meta["ours"]) == len(src_ours):
        meta["ours"] = [restore_identity(s, d) for s, d in zip(src_ours, meta["ours"])]
    else:
        log("[WARN] meta ours length mismatch; forcing re-translate meta")
        if meta_out.exists():
            meta_out.unlink()
        meta = load_or_translate("meta", meta_payload, meta_out, expect_list=False, expect_len=None)
        if not isinstance(meta.get("ours"), list) or len(meta["ours"]) != len(src_ours):
            raise RuntimeError("meta ours length mismatch after retry")
        meta["ours"] = [restore_identity(s, d) for s, d in zip(src_ours, meta["ours"])]

    official = src.get("official", [])
    translated_official = []
    for i in range(0, len(official), CHUNK):
        chunk = official[i : i + CHUNK]
        idx = i // CHUNK
        label = f"official-{idx:02d}"
        outp = WORKDIR / f"changelog-{label}-out.txt"
        part = load_or_translate(label, chunk, outp, expect_list=True, expect_len=len(chunk))
        part = [restore_identity(s, d) for s, d in zip(chunk, part)]
        translated_official.extend(part)

    result = {
        "updated": src.get("updated", meta.get("updated")),
        "ui": meta.get("ui", src.get("ui")),
        "official": translated_official,
        "ours": meta.get("ours", src.get("ours")),
    }

    # identity check
    bad = []
    for s, d in zip(official, translated_official):
        for k in ("id", "url"):
            if s.get(k) != d.get(k):
                bad.append((k, s.get(k), d.get(k)))
    for s, d in zip(src_ours, result["ours"]):
        for k in ("id", "url"):
            if s.get(k) != d.get(k):
                bad.append((k, s.get(k), d.get(k)))
    if bad:
        raise RuntimeError(f"id/url mismatch samples: {bad[:5]}")

    if len(translated_official) != len(official):
        raise RuntimeError(f"official count {len(translated_official)} != {len(official)}")
    if len(result["ours"]) != len(src_ours):
        raise RuntimeError(f"ours count {len(result['ours'])} != {len(src_ours)}")

    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    OUT.write_text(text, encoding="utf-8")
    BACKUP.write_text(text, encoding="utf-8")
    log(
        f"[OK-JSON] changelog.json wrote {OUT} ({OUT.stat().st_size} bytes) "
        f"official={len(translated_official)} ours={len(result['ours'])}"
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as e:
        log(f"[FAIL-JSON-CHUNKED] changelog.json {e}")
        raise
