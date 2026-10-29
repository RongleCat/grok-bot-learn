#!/usr/bin/env bash
# 单篇 agy → site/docs/<locale>/<rel>
# 用法: ./agy_translate_one.sh en part1/01-what-is.md
#       ./agy_translate_one.sh en --json home.json
set -euo pipefail
LOCALE="${1:?locale}"; shift
MODEL="${AGY_MODEL:-gemini-3.8-flash-high}"
ROOT="/workspace/grok-bot-learn"
PROJ="$ROOT/i18n-project"
GLOSSARY="${GLOSSARY_OVERRIDE:-$PROJ/glossary/DO_NOT_TRANSLATE.txt}"
[[ -f "$GLOSSARY" ]] || GLOSSARY="$PROJ/glossary/DO_NOT_TRANSLATE.txt"
SRC_ROOT="$ROOT/site/docs"
THEME="$SRC_ROOT/.vitepress/theme"
WORKDIR="${WORKDIR_OVERRIDE:-$PROJ/work/$LOCALE}"
BACKUP="${BACKUP_OVERRIDE:-$PROJ/backups/$LOCALE}"
mkdir -p "$WORKDIR" "$BACKUP"

lang_name() { case "$1" in en) echo English;; ja) echo Japanese;; ko) echo Korean;; es) echo Spanish;; pt-BR) echo "Brazilian Portuguese";; *) echo "$1";; esac; }

case "$LOCALE" in en|ja|ko|es|pt-BR) ;; *) echo "use OpenCC for zh-Hant" >&2; exit 2;; esac

PROMPT_FILE="$WORKDIR/prompt-$$.txt"
TMP_OUT="$WORKDIR/out-$$.txt"

run_agy() {
  local out="$1"
  export GEMINI_FORCE_FILE_STORAGE=true
  python3 - "$MODEL" "$PROMPT_FILE" "$TMP_OUT" <<'PY'
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
PY
  local rc=$?
  if [[ $rc -ne 0 ]]; then
    return $rc
  fi
  mkdir -p "$(dirname "$out")"
  cp "$TMP_OUT" "$out"
  return 0
}

install_backup() {
  local rel_or_name="$1"
  local src="$2"
  mkdir -p "$(dirname "$BACKUP/$rel_or_name")"
  cp "$src" "$BACKUP/$rel_or_name"
}

if [[ "${1:-}" == "--json" ]]; then
  NAME="${2:?json name}"
  SRC="$THEME/$NAME"
  OUT="$THEME/locales/$LOCALE/$NAME"
  [[ -f "$SRC" ]] || { echo "missing $SRC" >&2; exit 1; }
  mkdir -p "$(dirname "$OUT")"
  {
    echo "Translate JSON UI strings for Grok Bot learning site (bot.fmcat.top) into $(lang_name "$LOCALE") ($LOCALE)."
    echo "Rules: keep JSON keys unchanged; keep link/href/url/src/path string values unchanged; translate only human-readable string values."
    echo "Do NOT translate DO_NOT_TRANSLATE terms. Do NOT use tools, shell, or browse. Output ONLY valid JSON, no markdown fence."
    echo "=== DO_NOT_TRANSLATE ==="; cat "$GLOSSARY"; echo "=== END ==="
    echo "=== SOURCE JSON ==="; cat "$SRC"; echo "=== END ==="
  } > "$PROMPT_FILE"
  if [[ "${AGY_DRY:-}" == "1" ]]; then echo "(dry) $OUT"; exit 0; fi
  echo "json $NAME → locales/$LOCALE/"
  run_agy "$OUT"
  python3 - "$OUT" <<'PY'
import sys,re,json
from pathlib import Path
p=Path(sys.argv[1])
raw=p.read_text(encoding='utf-8').strip()
raw=re.sub(r'^```(?:json)?\s*','',raw); raw=re.sub(r'\s*```$','',raw)
json.loads(raw)
p.write_text(raw if raw.endswith('\n') else raw+'\n', encoding='utf-8')
PY
  install_backup "locales/$NAME" "$OUT"
  rm -f "$PROMPT_FILE" "$TMP_OUT"
  echo "wrote $OUT"
  exit 0
fi

REL="${1:?rel path}"
SRC="$SRC_ROOT/$REL"
OUT="$SRC_ROOT/$LOCALE/$REL"
[[ -f "$SRC" ]] || { echo "missing $SRC" >&2; exit 1; }
mkdir -p "$(dirname "$OUT")"
{
  echo "You are translating Grok Bot learning-site docs (https://bot.fmcat.top) into $(lang_name "$LOCALE") ($LOCALE)."
  echo "Rules:"
  echo "- Keep Markdown structure, frontmatter KEY names unchanged; translate frontmatter string values (title/description)."
  echo "- Keep link paths as-is (engineering adds locale prefix)."
  echo "- Keep fenced code blocks and inline code EXACTLY unchanged."
  echo "- Do NOT translate DO_NOT_TRANSLATE terms (product names, people, URLs, commands)."
  echo "- Keep the meaning of the community disclaimer if present."
  echo "- Translate ALL human-readable Chinese text into the target language, INCLUDING chapter/section titles that appear as Markdown link text (e.g. further-reading / 延伸阅读 lists like [第 N 章 …](/part1/…)). Keep the URL/path inside the parentheses unchanged."
  echo "- Only keep Chinese when it is inside a fenced code block, inline code, or a DO_NOT_TRANSLATE term."
  echo "- Do NOT use tools, shell, or browse. Output ONLY the full translated Markdown, no preamble."
  echo "=== DO_NOT_TRANSLATE ==="; cat "$GLOSSARY"; echo "=== END ==="
  echo "=== SOURCE ==="; cat "$SRC"; echo "=== END ==="
} > "$PROMPT_FILE"
if [[ "${AGY_DRY:-}" == "1" ]]; then echo "(dry) $OUT"; wc -c "$PROMPT_FILE"; exit 0; fi
echo "translating $REL → $LOCALE ..."
run_agy "$OUT"
install_backup "$REL" "$OUT"
BYTES=$(wc -c <"$OUT" | tr -d ' ')
rm -f "$PROMPT_FILE" "$TMP_OUT"
echo "wrote $OUT ($BYTES bytes)"
