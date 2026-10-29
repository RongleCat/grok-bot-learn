#!/usr/bin/env bash
# Japanese remaining batch — durable backup under i18n-project/backups/ja
set -uo pipefail
ROOT="/workspace/grok-bot-learn"
PROJ="$ROOT/i18n-project"
ONE="$PROJ/scripts/agy_translate_one.sh"
LOG="$PROJ/logs/agy-ja-full.log"
STATUS="$PROJ/logs/translate-STATUS.md"
OUT_ROOT="$ROOT/site/docs/ja"
BACKUP="$PROJ/backups/ja"
LIST="${LIST_OVERRIDE:-/tmp/ja-remaining.txt}"
CONCURRENCY="${CONCURRENCY:-2}"
SUMMARY="$PROJ/logs/ja-full-summary.txt"

mkdir -p "$(dirname "$LOG")" "$BACKUP" "$OUT_ROOT"
echo "" >> "$LOG"
echo "=== ja full batch START $(date '+%Y-%m-%d %H:%M:%S %z') concurrency=$CONCURRENCY ===" | tee -a "$LOG"

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
  if bash "$ONE" ja "$rel" >>"$LOG" 2>&1; then
    echo "[OK] $rel ($(wc -c <"$out" | tr -d ' ') bytes)" | tee -a "$LOG"
    return 0
  fi
  echo "[RETRY] $rel" | tee -a "$LOG"
  sleep 3
  if bash "$ONE" ja "$rel" >>"$LOG" 2>&1; then
    echo "[OK-RETRY] $rel ($(wc -c <"$out" | tr -d ' ') bytes)" | tee -a "$LOG"
    return 0
  fi
  echo "[FAIL] $rel" | tee -a "$LOG"
  return 1
}

translate_json() {
  local name="$1"
  local out="$ROOT/site/docs/.vitepress/theme/locales/ja/$name"
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
  if bash "$ONE" ja --json "$name" >>"$LOG" 2>&1; then
    echo "[OK-JSON] $name ($(wc -c <"$out" | tr -d ' ') bytes)" | tee -a "$LOG"
    return 0
  fi
  echo "[RETRY-JSON] $name" | tee -a "$LOG"
  sleep 3
  if bash "$ONE" ja --json "$name" >>"$LOG" 2>&1; then
    echo "[OK-RETRY-JSON] $name ($(wc -c <"$out" | tr -d ' ') bytes)" | tee -a "$LOG"
    return 0
  fi
  echo "[FAIL-JSON] $name" | tee -a "$LOG"
  return 1
}

en_md() { find "$ROOT/site/docs/en" -name '*.md' -type f -size +0c 2>/dev/null | wc -l; }
en_ui() { find "$ROOT/site/docs/.vitepress/theme/locales/en" -name '*.json' -type f -size +0c 2>/dev/null | wc -l; }
ko_md() { find "$ROOT/site/docs/ko" -name '*.md' -type f -size +0c 2>/dev/null | wc -l; }
ja_md() { find "$OUT_ROOT" -name '*.md' -type f -size +0c 2>/dev/null | wc -l; }
ja_ui() { find "$ROOT/site/docs/.vitepress/theme/locales/ja" -name '*.json' -type f -size +0c 2>/dev/null | wc -l; }

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
| zh-Hant | **61/61 + UI 6** | OpenCC 全量 |
| en | **$(en_md)/61 MD + UI $(en_ui)** | agy 全量进行中/收尾 |
| ja | **$(ja_md)/61 MD + UI $(ja_ui)** | ${note} |
| ko | **$(ko_md)/61 MD** | agy |
| es / pt-BR | 排队/进行中 | agy |

本批日志：\`logs/agy-ja-full.log\`（ok=${ok} fail=${fail} skip=${skip}）
ST
}

mapfile -t REMAINING < "$LIST"
echo "Remaining MD: ${#REMAINING[@]}" | tee -a "$LOG"
update_status "全量启动；剩余 ${#REMAINING[@]} 篇 + UI 4"

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
  md_count=$(ja_md)
  if [[ $ok -eq 24 ]]; then
    update_status "过半（本批 ok=${ok}）；md=${md_count}/61"
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

md_count=$(ja_md)
ui_count=$(ja_ui)
now=$(date '+%Y-%m-%d %H:%M:%S')

{
  echo "=== SUMMARY $(date '+%Y-%m-%d %H:%M:%S %z') ==="
  echo "ok=$ok fail=$fail skip=$skip"
  echo "md_total=$md_count ui=$ui_count"
  echo "FAIL_LIST=${FAIL_LIST[*]:-none}"
} | tee -a "$LOG"

state="ja 全量收尾"
[[ $fail -eq 0 && $md_count -ge 61 ]] && state="**ja 全量完成**"

cat > "$STATUS" << ST
# 翻译进度

- 更新时间：${now} (Asia/Singapore)
- 状态：**translating**

| 语种 | 进度 | 备注 |
|---|---|---|
| zh-Hant | **61/61 + UI 6** | OpenCC 全量 |
| en | **$(en_md)/61 MD + UI $(en_ui)** | agy |
| ja | **${md_count}/61 MD + UI ${ui_count}** | ${state}；本批 ok=${ok} fail=${fail} skip=${skip} |
| ko | **$(ko_md)/61 MD** | agy |
| es / pt-BR | 排队/进行中 | agy |

本批日志：\`logs/agy-ja-full.log\`
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
