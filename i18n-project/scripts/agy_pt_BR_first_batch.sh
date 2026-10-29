#!/usr/bin/env bash
# pt-BR first batch: index + part1(12) + tools/agy + home.json + tools.json
set -uo pipefail
ROOT="/workspace/grok-bot-learn"
PROJ="$ROOT/i18n-project"
ONE="$PROJ/scripts/agy_translate_one.sh"
LOG="$PROJ/logs/agy-pt-BR-first-batch.log"
LOCALE="pt-BR"
export AGY_MODEL="${AGY_MODEL:-gemini-3.8-flash-high}"

ITEMS=(
  "index.md"
  "part1/01-what-is.md"
  "part1/02-plans.md"
  "part1/03-install.md"
  "part1/04-handoff.md"
  "part1/05-computer.md"
  "part1/06-memory.md"
  "part1/07-apps.md"
  "part1/08-skills-routines.md"
  "part1/09-group-team.md"
  "part1/10-usage.md"
  "part1/11-safety.md"
  "part1/grok-vs-grok-bot.md"
  "tools/agy.md"
  "--json home.json"
  "--json tools.json"
)

mkdir -p "$PROJ/logs" "$ROOT/site/docs/$LOCALE/part1" "$ROOT/site/docs/$LOCALE/tools" \
  "$ROOT/site/docs/.vitepress/theme/locales/$LOCALE"

{
  echo "=== pt-BR first batch start ==="
  date '+%Y-%m-%d %H:%M:%S %z'
  echo "model=$AGY_MODEL locale=$LOCALE"
} | tee "$LOG"

ok=0; fail=0; FAILED_LIST=""
for item in "${ITEMS[@]}"; do
  ts=$(date '+%H:%M:%S')
  echo "[TRY] $item $ts" | tee -a "$LOG"
  if [[ "$item" == --json* ]]; then
    # shellcheck disable=SC2086
    if "$ONE" "$LOCALE" $item >>"$LOG" 2>&1; then
      name="${item#--json }"
      out="$ROOT/site/docs/.vitepress/theme/locales/$LOCALE/$name"
      bytes=$(wc -c <"$out" | tr -d ' ')
      echo "[OK] $item ($bytes bytes)" | tee -a "$LOG"
      ok=$((ok+1))
    else
      echo "[ERR] $item — retry once" | tee -a "$LOG"
      if "$ONE" "$LOCALE" $item >>"$LOG" 2>&1; then
        name="${item#--json }"
        out="$ROOT/site/docs/.vitepress/theme/locales/$LOCALE/$name"
        bytes=$(wc -c <"$out" | tr -d ' ')
        echo "[OK] $item retry ($bytes bytes)" | tee -a "$LOG"
        ok=$((ok+1))
      else
        echo "[FAIL] $item after retry" | tee -a "$LOG"
        fail=$((fail+1))
        FAILED_LIST="$FAILED_LIST $item"
      fi
    fi
  else
    out="$ROOT/site/docs/$LOCALE/$item"
    if "$ONE" "$LOCALE" "$item" >>"$LOG" 2>&1; then
      bytes=$(wc -c <"$out" | tr -d ' ')
      echo "[OK] $item ($bytes bytes)" | tee -a "$LOG"
      ok=$((ok+1))
    else
      echo "[ERR] $item — retry once" | tee -a "$LOG"
      if "$ONE" "$LOCALE" "$item" >>"$LOG" 2>&1; then
        bytes=$(wc -c <"$out" | tr -d ' ')
        echo "[OK] $item retry ($bytes bytes)" | tee -a "$LOG"
        ok=$((ok+1))
      else
        echo "[FAIL] $item after retry" | tee -a "$LOG"
        fail=$((fail+1))
        FAILED_LIST="$FAILED_LIST $item"
      fi
    fi
  fi
done

{
  echo "=== BATCH DONE ok=$ok fail=$fail ==="
  echo "FAILED_LIST=$FAILED_LIST"
  date '+%Y-%m-%d %H:%M:%S %z'
} | tee -a "$LOG"
