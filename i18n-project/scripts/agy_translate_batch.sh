#!/usr/bin/env bash
# ./agy_translate_batch.sh en [limit] [prefix]
set -euo pipefail
LOCALE="${1:?}"; LIMIT="${2:-}"; PREFIX="${3:-}"
PROJ="$(cd "$(dirname "$0")/.." && pwd)"
TSV="$PROJ/SOURCE_PAGES.tsv"
ONE="$PROJ/scripts/agy_translate_one.sh"
LOG="$PROJ/logs/agy-batch-${LOCALE}-$(date +%Y%m%d-%H%M%S).log"
case "$LOCALE" in en|ja|ko|es|pt-BR) ;; *) exit 2;; esac
n=0; ok=0; fail=0
while IFS=$'\t' read -r path _ || [[ -n "${path:-}" ]]; do
  [[ -z "${path:-}" || "$path" =~ ^# ]] && continue
  rel="${path#site/docs/}"
  [[ -n "$PREFIX" && "$rel" != "$PREFIX"* ]] && continue
  out="$PROJ/../site/docs/$LOCALE/$rel"
  if [[ "${SKIP_EXISTING:-}" == "1" && -f "$out" ]]; then echo "skip $rel" | tee -a "$LOG"; continue; fi
  n=$((n+1))
  [[ -n "$LIMIT" && "$n" -gt "$LIMIT" ]] && break
  echo "[$n] $rel" | tee -a "$LOG"
  if AGY_DRY="${AGY_DRY:-}" "$ONE" "$LOCALE" "$rel" >>"$LOG" 2>&1; then ok=$((ok+1)); else fail=$((fail+1)); echo "FAIL $rel"|tee -a "$LOG"; fi
done < "$TSV"
echo "batch done locale=$LOCALE ok=$ok fail=$fail log=$LOG" | tee -a "$LOG"
