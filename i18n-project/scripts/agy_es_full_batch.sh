#!/usr/bin/env bash
# Spanish remaining batch — durable backup under i18n-project/backups/es
set -uo pipefail
ROOT="/workspace/grok-bot-learn"
PROJ="$ROOT/i18n-project"
ONE="$PROJ/scripts/agy_translate_one.sh"
LOG="$PROJ/logs/agy-es-full.log"
STATUS="$PROJ/logs/translate-STATUS.md"
OUT_ROOT="$ROOT/site/docs/es"
BACKUP="$PROJ/backups/es"
LIST="${LIST_OVERRIDE:-/tmp/es-remaining.txt}"
CONCURRENCY="${CONCURRENCY:-2}"
SUMMARY="$PROJ/logs/es-full-summary.txt"
CHUNKED="$PROJ/scripts/agy_es_changelog_chunked.py"

mkdir -p "$(dirname "$LOG")" "$BACKUP" "$OUT_ROOT" "$ROOT/site/docs/.vitepress/theme/locales/es"
echo "" >> "$LOG"
echo "=== es full batch START $(date '+%Y-%m-%d %H:%M:%S %z') concurrency=$CONCURRENCY ===" | tee -a "$LOG"

ok=0
fail=0
skip=0
FAIL_LIST=()

translate_one() {
  local rel="$1"
  local out="$OUT_ROOT/$rel"
  local bak="$BACKUP/$rel"
  if [[ (! -f "$out" || ! -s "$out") && -f "$bak" && -s "$bak" ]]; then
    mkdir -p "$(dirname "$out")"
    cp "$bak" "$out"
    echo "[RESTORE] $rel from backup" | tee -a "$LOG"
  fi
  if [[ -f "$out" && -s "$out" ]]; then
    mkdir -p "$(dirname "$bak")"
    cp "$out" "$bak"
    echo "[SKIP] $rel ($(wc -c <"$out" | tr -d ' ') bytes)" | tee -a "$LOG"
    return 2
  fi
  echo "[START] $rel $(date '+%H:%M:%S')" | tee -a "$LOG"
  if bash "$ONE" es "$rel" >>"$LOG" 2>&1; then
    echo "[OK] $rel ($(wc -c <"$out" | tr -d ' ') bytes)" | tee -a "$LOG"
    return 0
  fi
  echo "[RETRY] $rel" | tee -a "$LOG"
  sleep 3
  if bash "$ONE" es "$rel" >>"$LOG" 2>&1; then
    echo "[OK-RETRY] $rel ($(wc -c <"$out" | tr -d ' ') bytes)" | tee -a "$LOG"
    return 0
  fi
  echo "[FAIL] $rel" | tee -a "$LOG"
  return 1
}

translate_json() {
  local name="$1"
  local out="$ROOT/site/docs/.vitepress/theme/locales/es/$name"
  local bak="$BACKUP/locales/$name"
  if [[ "$name" == "changelog.json" ]]; then
    echo "[START-JSON] changelog.json → chunked $(date '+%H:%M:%S')" | tee -a "$LOG"
    if ES_LOG="$LOG" python3 "$CHUNKED" >>"$LOG" 2>&1; then
      echo "[OK-JSON] changelog.json ($(wc -c <"$out" | tr -d ' ') bytes)" | tee -a "$LOG"
      return 0
    fi
    echo "[FAIL-JSON] changelog.json" | tee -a "$LOG"
    return 1
  fi
  if [[ (! -f "$out" || ! -s "$out") && -f "$bak" && -s "$bak" ]]; then
    mkdir -p "$(dirname "$out")"
    cp "$bak" "$out"
    echo "[RESTORE-JSON] $name" | tee -a "$LOG"
  fi
  if [[ -f "$out" && -s "$out" ]]; then
    mkdir -p "$(dirname "$bak")"; cp "$out" "$bak"
    echo "[SKIP-JSON] $name" | tee -a "$LOG"
    return 2
  fi
  echo "[START-JSON] $name $(date '+%H:%M:%S')" | tee -a "$LOG"
  if bash "$ONE" es --json "$name" >>"$LOG" 2>&1; then
    echo "[OK-JSON] $name ($(wc -c <"$out" | tr -d ' ') bytes)" | tee -a "$LOG"
    return 0
  fi
  echo "[RETRY-JSON] $name" | tee -a "$LOG"
  sleep 3
  if bash "$ONE" es --json "$name" >>"$LOG" 2>&1; then
    echo "[OK-RETRY-JSON] $name ($(wc -c <"$out" | tr -d ' ') bytes)" | tee -a "$LOG"
    return 0
  fi
  echo "[FAIL-JSON] $name" | tee -a "$LOG"
  return 1
}

count_md() { find "$1" -name '*.md' -type f -size +0c 2>/dev/null | wc -l; }
count_ui() { find "$ROOT/site/docs/.vitepress/theme/locales/$1" -name '*.json' -type f -size +0c 2>/dev/null | wc -l; }

update_status() {
  local note="$1"
  local now
  now=$(date '+%Y-%m-%d %H:%M:%S')
  cat > "$STATUS" << ST
# 翻译进度

- 更新时间：${now} (Asia/Singapore)
- 状态：**translating**

| 语种 | 进度 | 备注 |
|---|---|---|
| zh-Hant | **61/61 + UI 6** | 完成 |
| en | **$(count_md "$ROOT/site/docs/en")/61 MD + UI $(count_ui en)** | 完成 |
| ja | **$(count_md "$ROOT/site/docs/ja")/61 MD + UI $(count_ui ja)** | agy |
| ko | **$(count_md "$ROOT/site/docs/ko")/61 MD + UI $(count_ui ko)** | agy |
| es | **$(count_md "$OUT_ROOT")/61 MD + UI $(count_ui es)** | ${note} |
| pt-BR | **$(count_md "$ROOT/site/docs/pt-BR")/61 MD + UI $(count_ui pt-BR)** | agy |

本批日志：\`logs/agy-es-full.log\`（ok=${ok} fail=${fail} skip=${skip}）
ST
}

mapfile -t REMAINING < "$LIST"
echo "Remaining MD: ${#REMAINING[@]}" | tee -a "$LOG"
update_status "扩全量启动；剩余 ${#REMAINING[@]} 篇 + UI 4（bots/ecosystem/changelog/funnel）"

running=0
pids=()
rels=()
halfway_marked=0

wait_one() {
  local pid="${pids[0]}"
  local rel="${rels[0]}"
  pids=("${pids[@]:1}")
  rels=("${rels[@]:1}")
  running=$((running - 1))
  local rc=0
  wait "$pid" || rc=$?
  if [[ $rc -eq 0 ]]; then
    ok=$((ok + 1))
  elif [[ $rc -eq 2 ]]; then
    skip=$((skip + 1))
  else
    fail=$((fail + 1))
    FAIL_LIST+=("$rel")
  fi
  local md_count
  md_count=$(count_md "$OUT_ROOT")
  # first batch 14 MD already done; halfway of full corpus ≈ 30+, or when md hits 30
  if [[ $halfway_marked -eq 0 && $md_count -ge 30 ]]; then
    halfway_marked=1
    update_status "过半（md=${md_count}/61；本批 ok=${ok} fail=${fail}）"
    echo "[HALFWAY] ok=$ok md=$md_count $(date '+%H:%M:%S')" | tee -a "$LOG"
  fi
}

for rel in "${REMAINING[@]}"; do
  [[ -z "$rel" ]] && continue
  while [[ $running -ge $CONCURRENCY ]]; do
    wait_one
  done
  ( translate_one "$rel"; exit $? ) &
  pids+=($!)
  rels+=("$rel")
  running=$((running + 1))
done

while [[ $running -gt 0 ]]; do
  wait_one
done

for name in bots.json ecosystem.json changelog.json funnel.json; do
  translate_json "$name"
  rc=$?
  if [[ $rc -eq 0 ]]; then ok=$((ok + 1))
  elif [[ $rc -eq 2 ]]; then skip=$((skip + 1))
  else fail=$((fail + 1)); FAIL_LIST+=("json:$name"); fi
done

md_count=$(count_md "$OUT_ROOT")
ui_count=$(count_ui es)
now=$(date '+%Y-%m-%d %H:%M:%S')

{
  echo "=== SUMMARY $(date '+%Y-%m-%d %H:%M:%S %z') ==="
  echo "ok=$ok fail=$fail skip=$skip"
  echo "md_total=$md_count ui=$ui_count"
  echo "FAIL_LIST=${FAIL_LIST[*]:-none}"
} | tee -a "$LOG"

state="es 全量收尾"
[[ $fail -eq 0 && $md_count -ge 61 && $ui_count -ge 6 ]] && state="**es 全量完成**"

cat > "$STATUS" << ST
# 翻译进度

- 更新时间：${now} (Asia/Singapore)
- 状态：**translating**

| 语种 | 进度 | 备注 |
|---|---|---|
| zh-Hant | **61/61 + UI 6** | 完成 |
| en | **$(count_md "$ROOT/site/docs/en")/61 MD + UI $(count_ui en)** | 完成 |
| ja | **$(count_md "$ROOT/site/docs/ja")/61 MD + UI $(count_ui ja)** | agy |
| ko | **$(count_md "$ROOT/site/docs/ko")/61 MD + UI $(count_ui ko)** | agy |
| es | **${md_count}/61 MD + UI ${ui_count}** | ${state}；本批 ok=${ok} fail=${fail} skip=${skip} |
| pt-BR | **$(count_md "$ROOT/site/docs/pt-BR")/61 MD + UI $(count_ui pt-BR)** | agy |

本批日志：\`logs/agy-es-full.log\`
失败列表：${FAIL_LIST[*]:-none}
ST

cat > "$SUMMARY" << SUM
ok=$ok
fail=$fail
skip=$skip
md_count=$md_count
ui_count=$ui_count
fail_list=${FAIL_LIST[*]:-none}
SUM

echo "DONE" | tee -a "$LOG"
