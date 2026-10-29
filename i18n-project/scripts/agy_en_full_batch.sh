#!/usr/bin/env bash
# English remaining batch — durable backup under i18n-project/backups/en
set -uo pipefail
ROOT="/workspace/grok-bot-learn"
PROJ="$ROOT/i18n-project"
ONE="$PROJ/scripts/agy_translate_one.sh"
LOG="$PROJ/logs/agy-en-full.log"
STATUS="$PROJ/logs/translate-STATUS.md"
OUT_ROOT="$ROOT/site/docs/en"
BACKUP="$PROJ/backups/en"
LIST="$PROJ/logs/en-remaining.txt"
CONCURRENCY="${CONCURRENCY:-3}"

mkdir -p "$(dirname "$LOG")" "$BACKUP"
echo "" >> "$LOG"
echo "=== en full batch RESTART $(date '+%Y-%m-%d %H:%M:%S %z') concurrency=$CONCURRENCY ===" | tee -a "$LOG"

ok=0
fail=0
skip=0
FAIL_LIST=()

translate_one() {
  local rel="$1"
  local out="$OUT_ROOT/$rel"
  local bak="$BACKUP/$rel"
  # Prefer restoring from durable backup if site missing
  if [[ (! -f "$out" || ! -s "$out") && -f "$bak" && -s "$bak" ]]; then
    mkdir -p "$(dirname "$out")"
    cp "$bak" "$out"
    echo "[RESTORE] $rel from backup" | tee -a "$LOG"
  fi
  if [[ -f "$out" && -s "$out" ]]; then
    # ensure backup exists
    mkdir -p "$(dirname "$bak")"
    cp "$out" "$bak"
    echo "[SKIP] $rel ($(wc -c <"$out" | tr -d ' ') bytes)" | tee -a "$LOG"
    return 2
  fi
  echo "[START] $rel $(date '+%H:%M:%S')" | tee -a "$LOG"
  if bash "$ONE" en "$rel" >>"$LOG" 2>&1; then
    echo "[OK] $rel ($(wc -c <"$out" | tr -d ' ') bytes)" | tee -a "$LOG"
    return 0
  fi
  echo "[RETRY] $rel" | tee -a "$LOG"
  sleep 3
  if bash "$ONE" en "$rel" >>"$LOG" 2>&1; then
    echo "[OK-RETRY] $rel ($(wc -c <"$out" | tr -d ' ') bytes)" | tee -a "$LOG"
    return 0
  fi
  echo "[FAIL] $rel" | tee -a "$LOG"
  return 1
}

translate_json() {
  local name="$1"
  local out="$ROOT/site/docs/.vitepress/theme/locales/en/$name"
  local bak="$BACKUP/locales/$name"
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
  if bash "$ONE" en --json "$name" >>"$LOG" 2>&1; then
    echo "[OK-JSON] $name ($(wc -c <"$out" | tr -d ' ') bytes)" | tee -a "$LOG"
    return 0
  fi
  echo "[RETRY-JSON] $name" | tee -a "$LOG"
  sleep 3
  if bash "$ONE" en --json "$name" >>"$LOG" 2>&1; then
    echo "[OK-RETRY-JSON] $name ($(wc -c <"$out" | tr -d ' ') bytes)" | tee -a "$LOG"
    return 0
  fi
  echo "[FAIL-JSON] $name" | tee -a "$LOG"
  return 1
}

update_status() {
  local note="$1"
  local now md_count ui_count
  now=$(date '+%Y-%m-%d %H:%M:%S')
  md_count=$(find "$OUT_ROOT" -name '*.md' -type f -size +0c 2>/dev/null | wc -l)
  ui_count=$(find "$ROOT/site/docs/.vitepress/theme/locales/en" -name '*.json' -type f -size +0c 2>/dev/null | wc -l)
  cat > "$STATUS" << ST
# 翻译进度

- 更新时间：${now} (Asia/Singapore)
- 状态：**translating**

| 语种 | 进度 | 备注 |
|---|---|---|
| zh-Hant | **61/61 + UI 6** | OpenCC 全量 |
| en | **${md_count}/61 MD + UI ${ui_count}** | ${note} |
| ja | 进行中 | agy |
| ko | 进行中 | agy |
| es / pt-BR | 排队/进行中 | agy |

本批日志：\`logs/agy-en-full.log\`（ok=${ok} fail=${fail} skip=${skip}）
ST
}

mapfile -t REMAINING < "$LIST"
echo "Remaining MD: ${#REMAINING[@]}" | tee -a "$LOG"
update_status "全量重启；剩余 ${#REMAINING[@]} 篇 + UI 4"

running=0
pids=()
rels=()

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
  md_count=$(find "$OUT_ROOT" -name '*.md' -type f -size +0c 2>/dev/null | wc -l)
  # halfway of full corpus ≈ 30+, or when new ok reaches ~17 of 34
  if [[ $ok -eq 17 ]]; then
    update_status "重启后过半（本批 ok=${ok}）；md=${md_count}/61"
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

md_count=$(find "$OUT_ROOT" -name '*.md' -type f -size +0c 2>/dev/null | wc -l)
ui_count=$(find "$ROOT/site/docs/.vitepress/theme/locales/en" -name '*.json' -type f -size +0c 2>/dev/null | wc -l)
now=$(date '+%Y-%m-%d %H:%M:%S')

{
  echo "=== SUMMARY $(date '+%Y-%m-%d %H:%M:%S %z') ==="
  echo "ok=$ok fail=$fail skip=$skip"
  echo "md_total=$md_count ui=$ui_count"
  echo "FAIL_LIST=${FAIL_LIST[*]:-none}"
} | tee -a "$LOG"

state="en 全量收尾"
[[ $fail -eq 0 && $md_count -ge 61 ]] && state="**en 全量完成**"

cat > "$STATUS" << ST
# 翻译进度

- 更新时间：${now} (Asia/Singapore)
- 状态：**translating**

| 语种 | 进度 | 备注 |
|---|---|---|
| zh-Hant | **61/61 + UI 6** | OpenCC 全量 |
| en | **${md_count}/61 MD + UI ${ui_count}** | ${state}；本批 ok=${ok} fail=${fail} skip=${skip} |
| ja | 进行中 | agy |
| ko | 进行中 | agy |
| es / pt-BR | 排队/进行中 | agy |

本批日志：\`logs/agy-en-full.log\`
失败列表：${FAIL_LIST[*]:-none}
ST

cat > "$PROJ/logs/en-full-summary.txt" << SUM
ok=$ok
fail=$fail
skip=$skip
md_count=$md_count
ui_count=$ui_count
fail_list=${FAIL_LIST[*]:-none}
SUM

echo "DONE" | tee -a "$LOG"
