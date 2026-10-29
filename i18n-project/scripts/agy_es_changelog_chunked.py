#!/usr/bin/env python3
"""Translate changelog.json to es via meta + official chunks (ARG_MAX workaround)."""
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
OUT = THEME / "locales/es/changelog.json"
BACKUP = PROJ / "backups/es/locales/changelog.json"
WORKDIR = PROJ / "work/es"
GLOSSARY = PROJ / "glossary/DO_NOT_TRANSLATE.txt"
MODEL = os.environ.get("AGY_MODEL", "gemini-3.8-flash-high")
LOG = Path(os.environ.get("ES_LOG", str(PROJ / "logs/agy-es-full.log")))
CHUNK = 20
LOCALE = "es"
LANG = "Spanish"


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


def run_agy(prompt: str, out_path: Path) -> None:
    prompt_path = out_path.with_suffix(".prompt.txt")
    tmp_out = out_path.with_suffix(".tmp.txt")
    prompt_path.write_text(prompt, encoding="utf-8")
    env = os.environ.copy()
    env["GEMINI_FORCE_FILE_STORAGE"] = "true"
    # Avoid ARG_MAX: pass prompt via python reading file (same as agy_translate_one.sh)
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
    for attempt in range(1, 8):
        r = subprocess.run(
            ["python3", "-c", code, MODEL, str(prompt_path), str(tmp_out)],
            capture_output=True,
            text=True,
            env=env,
        )
        combined = (r.stderr or "") + "\n" + (r.stdout or "")
        if r.stderr:
            log(r.stderr.rstrip("\n"))
        if r.returncode == 0 and tmp_out.exists() and tmp_out.stat().st_size > 0:
            out_path.write_text(tmp_out.read_text(encoding="utf-8"), encoding="utf-8")
            return
        last_err = f"attempt {attempt} rc={r.returncode}"
        log(f"[RETRY-CHUNK] {out_path.name} {last_err}")
        m = re.search(r"Resets in (\d+)m(\d+)s", combined)
        if m or "RESOURCE_EXHAUSTED" in combined or "Individual quota reached" in combined:
            wait = (int(m.group(1)) * 60 + int(m.group(2)) + 30) if m else 90
            wait = min(max(wait, 60), 25 * 60)
            log(f"[QUOTA-WAIT] {out_path.name} sleeping {wait}s")
            time.sleep(wait)
        else:
            time.sleep(min(5 * attempt, 30))
    raise RuntimeError(f"agy failed for {out_path.name}: {last_err}")


def build_prompt(label: str, payload) -> str:
    gloss = GLOSSARY.read_text(encoding="utf-8")
    body = json.dumps(payload, ensure_ascii=False, indent=2)
    return (
        f"Translate JSON UI strings for Grok Bot learning site (bot.fmcat.top) into {LANG} ({LOCALE}).\n"
        "Rules: keep JSON keys unchanged; keep link/href/url/src/path/id/version/date/platform string values unchanged; "
        "translate only human-readable string values (title, points, full nested text, summary, lead, note, etc).\n"
        "Do NOT translate DO_NOT_TRANSLATE terms. Do NOT use tools, shell, or browse. Output ONLY valid JSON, no markdown fence.\n"
        f"=== DO_NOT_TRANSLATE ===\n{gloss}\n=== END ===\n"
        f"=== SOURCE JSON ===\n{body}\n=== END ===\n"
    )


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



def restore_identity(src_item: dict, dst_item: dict) -> dict:
    out = dict(dst_item)
    for k in ("id", "url", "date", "version", "platform"):
        if k in src_item:
            out[k] = src_item[k]
    return out


def main() -> int:
    WORKDIR.mkdir(parents=True, exist_ok=True)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    BACKUP.parent.mkdir(parents=True, exist_ok=True)

    if OUT.exists() and OUT.stat().st_size > 0:
        log(f"[SKIP-JSON] changelog.json already at {OUT} ({OUT.stat().st_size} bytes)")
        return 0

    src = json.loads(SRC.read_text(encoding="utf-8"))
    log(f"[START-JSON-CHUNKED] changelog.json {time.strftime('%Y-%m-%d %H:%M:%S %z')}")

    meta_payload = {
        "updated": src.get("updated"),
        "ui": src.get("ui", {}),
        "ours": src.get("ours", []),
    }
    meta_out = WORKDIR / "changelog-meta-out.txt"
    meta = None
    if meta_out.exists() and meta_out.stat().st_size > 0:
        try:
            meta = parse_json_out(meta_out)
            log(f"[RESUME] meta reuse {meta_out.stat().st_size} bytes")
        except Exception as e:
            log(f"[RESUME-MISS] meta {e}")
            meta = None
    if meta is None:
        log(f"[CHUNK] meta prompt_bytes={len(build_prompt('meta', meta_payload).encode())} starting {time.strftime('%H:%M:%S')}")
        run_agy(build_prompt("meta", meta_payload), meta_out)
        meta = parse_json_out(meta_out)
        log(f"[OK-CHUNK] meta out_bytes={meta_out.stat().st_size}")

    # restore ours id/url/date/platform
    src_ours = src.get("ours", [])
    if isinstance(meta.get("ours"), list) and len(meta["ours"]) == len(src_ours):
        meta["ours"] = [restore_identity(s, d) for s, d in zip(src_ours, meta["ours"])]
    else:
        # retry once if length mismatch
        log("[WARN] meta ours length mismatch; retrying meta")
        run_agy(build_prompt("meta", meta_payload), meta_out)
        meta = parse_json_out(meta_out)
        if isinstance(meta.get("ours"), list) and len(meta["ours"]) == len(src_ours):
            meta["ours"] = [restore_identity(s, d) for s, d in zip(src_ours, meta["ours"])]
        else:
            raise RuntimeError("meta ours length mismatch after retry")

    official = src.get("official", [])
    translated_official = []
    for i in range(0, len(official), CHUNK):
        chunk = official[i : i + CHUNK]
        idx = i // CHUNK
        label = f"official-{idx:02d}"
        outp = WORKDIR / f"changelog-{label}-out.txt"
        prompt = build_prompt(label, chunk)
        part = None
        if outp.exists() and outp.stat().st_size > 0:
            try:
                part = parse_json_out(outp)
                if isinstance(part, list) and len(part) == len(chunk):
                    log(f"[RESUME] {label} reuse {outp.stat().st_size} bytes")
                else:
                    part = None
            except Exception as e:
                log(f"[RESUME-MISS] {label} {e}")
                part = None
        if part is None:
            log(f"[CHUNK] {label} prompt_bytes={len(prompt.encode())} starting {time.strftime('%H:%M:%S')}")
            run_agy(prompt, outp)
            part = parse_json_out(outp)
            if not isinstance(part, list) or len(part) != len(chunk):
                log(f"[WARN] {label} length mismatch got={type(part)}/{len(part) if isinstance(part, list) else '?'} expected={len(chunk)}; retry")
                run_agy(prompt, outp)
                part = parse_json_out(outp)
            if not isinstance(part, list) or len(part) != len(chunk):
                raise RuntimeError(f"{label} length mismatch")
        part = [restore_identity(s, d) for s, d in zip(chunk, part)]
        translated_official.extend(part)
        log(f"[OK-CHUNK] {label} out_bytes={outp.stat().st_size}")

    result = {
        "updated": meta.get("updated", src.get("updated")),
        "ui": meta.get("ui", src.get("ui")),
        "official": translated_official,
        "ours": meta.get("ours", src.get("ours")),
    }
    # keep updated from source if present
    if "updated" in src:
        result["updated"] = src["updated"]

    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    OUT.write_text(text, encoding="utf-8")
    BACKUP.write_text(text, encoding="utf-8")
    log(
        f"[OK-JSON] changelog.json wrote {OUT} ({OUT.stat().st_size} bytes) official={len(translated_official)}"
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as e:
        log(f"[FAIL-JSON-CHUNKED] changelog.json {e}")
        raise
