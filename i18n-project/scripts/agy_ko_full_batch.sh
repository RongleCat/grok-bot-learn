#!/usr/bin/env bash
# Korean remaining/full batch — SKIP non-empty site files; retry 1x
set -uo pipefail
ROOT="/workspace/grok-bot-learn"
PROJ="$ROOT/i18n-project"
ONE="$PROJ/scripts/agy_translate_one.sh"
# durable private copy (survives project churn)
DUR=/workspace/ko-batch
mkdir -p "$DUR/bin" "$DUR/out" "$DUR/work" "$DUR/backups"
cp -f "$ONE" "$DUR/bin/agy_translate_one.sh" 2>/dev/null || true
chmod +x "$DUR/bin/agy_translate_one.sh" "$ONE"
ONE="$DUR/bin/agy_translate_one.sh"
LOG="$PROJ/logs/agy-ko-full.log"
STATUS="$PROJ/logs/translate-STATUS.md"
OUT_ROOT="$ROOT/site/docs/ko"
BACKUP="$PROJ/backups/ko"
LIST="${LIST_OVERRIDE:-/tmp/ko-remaining.txt}"
CONCURRENCY="${CONCURRENCY:-1}"
SUMMARY="$PROJ/logs/ko-full-summary.txt"
export WORKDIR_OVERRIDE="$DUR/work"
export BACKUP_OVERRIDE="$BACKUP"
export AGY_MODEL=gemini-3.8-flash-high
export GEMINI_FORCE_FILE_STORAGE=true
export GLOSSARY_OVERRIDE="$PROJ/glossary/DO_NOT_TRANSLATE.txt"

mkdir -p "$(dirname "$LOG")" "$BACKUP" "$OUT_ROOT" \
  "$ROOT/site/docs/.vitepress/theme/locales/ko"
echo "" >> "$LOG"
echo "=== ko full batch START $(date '+%Y-%m-%d %H:%M:%S %z') concurrency=$CONCURRENCY ===" | tee -a "$LOG"

ok=0
fail=0
skip=0
FAIL_LIST=()
HALF_MARKED=0

translate_one() {
  local rel="$1"
  local out="$OUT_ROOT/$rel"
  local bak="$BACKUP/$rel"
  local dur="$DUR/out/$rel"
  # restore from backup/durable if site empty
  if [[ (! -f "$out" || ! -s "$out") && -f "$bak" && -s "$bak" ]]; then
    mkdir -p "$(dirname "$out")"; cp "$bak" "$out"
    echo "[RESTORE] $rel from backup" | tee -a "$LOG"
  fi
  if [[ (! -f "$out" || ! -s "$out") && -f "$dur" && -s "$dur" ]]; then
    mkdir -p "$(dirname "$out")"; cp "$dur" "$out"
    echo "[RESTORE] $rel from durable" | tee -a "$LOG"
  fi
  if [[ -f "$out" && -s "$out" ]]; then
    mkdir -p "$(dirname "$bak")" "$(dirname "$dur")"
    cp "$out" "$bak"; cp "$out" "$dur"
    echo "[SKIP] $rel ($(wc -c <"$out" | tr -d ' ') bytes)" | tee -a "$LOG"
    return 2
  fi
  echo "[START] $rel $(date '+%H:%M:%S')" | tee -a "$LOG"
  # refresh ONE
  [[ -f "$PROJ/scripts/agy_translate_one.sh" ]] && cp -f "$PROJ/scripts/agy_translate_one.sh" "$ONE" && chmod +x "$ONE"
  if bash "$ONE" ko "$rel" >>"$LOG" 2>&1; then
    mkdir -p "$(dirname "$bak")" "$(dirname "$dur")"
    [[ -f "$out" ]] && cp "$out" "$bak" && cp "$out" "$dur"
    echo "[OK] $rel ($(wc -c <"$out" | tr -d ' ') bytes)" | tee -a "$LOG"
    return 0
  fi
  echo "[RETRY] $rel" | tee -a "$LOG"
  sleep 3
  if bash "$ONE" ko "$rel" >>"$LOG" 2>&1; then
    mkdir -p "$(dirname "$bak")" "$(dirname "$dur")"
    [[ -f "$out" ]] && cp "$out" "$bak" && cp "$out" "$dur"
    echo "[OK-RETRY] $rel ($(wc -c <"$out" | tr -d ' ') bytes)" | tee -a "$LOG"
    return 0
  fi
  echo "[FAIL] $rel" | tee -a "$LOG"
  return 1
}

translate_json() {
  local name="$1"
  local out="$ROOT/site/docs/.vitepress/theme/locales/ko/$name"
  local bak="$BACKUP/locales/$name"
  local dur="$DUR/out/ui/$name"
  if [[ (! -f "$out" || ! -s "$out") && -f "$bak" && -s "$bak" ]]; then
    mkdir -p "$(dirname "$out")"; cp "$bak" "$out"
    echo "[RESTORE-JSON] $name" | tee -a "$LOG"
  fi
  if [[ (! -f "$out" || ! -s "$out") && -f "$dur" && -s "$dur" ]]; then
    mkdir -p "$(dirname "$out")"; cp "$dur" "$out"
    echo "[RESTORE-JSON] $name from durable" | tee -a "$LOG"
  fi
  if [[ -f "$out" && -s "$out" ]]; then
    mkdir -p "$(dirname "$bak")" "$(dirname "$dur")"
    cp "$out" "$bak"; cp "$out" "$dur"
    echo "[SKIP-JSON] $name" | tee -a "$LOG"
    return 2
  fi
  echo "[START-JSON] $name $(date '+%H:%M:%S')" | tee -a "$LOG"
  [[ -f "$PROJ/scripts/agy_translate_one.sh" ]] && cp -f "$PROJ/scripts/agy_translate_one.sh" "$ONE" && chmod +x "$ONE"
  if bash "$ONE" ko --json "$name" >>"$LOG" 2>&1; then
    mkdir -p "$(dirname "$bak")" "$(dirname "$dur")"
    [[ -f "$out" ]] && cp "$out" "$bak" && cp "$out" "$dur"
    echo "[OK-JSON] $name ($(wc -c <"$out" | tr -d ' ') bytes)" | tee -a "$LOG"
    return 0
  fi
  echo "[RETRY-JSON] $name" | tee -a "$LOG"
  sleep 3
  if bash "$ONE" ko --json "$name" >>"$LOG" 2>&1; then
    mkdir -p "$(dirname "$bak")" "$(dirname "$dur")"
    [[ -f "$out" ]] && cp "$out" "$bak" && cp "$out" "$dur"
    echo "[OK-RETRY-JSON] $name ($(wc -c <"$out" | tr -d ' ') bytes)" | tee -a "$LOG"
    return 0
  fi
  echo "[FAIL-JSON] $name" | tee -a "$LOG"
  return 1
}

ko_md() { find "$OUT_ROOT" -name '*.md' -type f -size +0c 2>/dev/null | wc -l; }
ko_ui() { find "$ROOT/site/docs/.vitepress/theme/locales/ko" -name '*.json' -type f -size +0c 2>/dev/null | wc -l; }
en_md() { find "$ROOT/site/docs/en" -name '*.md' -type f -size +0c 2>/dev/null | wc -l; }
en_ui() { find "$ROOT/site/docs/.vitepress/theme/locales/en" -name '*.json' -type f -size +0c 2>/dev/null | wc -l; }
ja_md() { find "$ROOT/site/docs/ja" -name '*.md' -type f -size +0c 2>/dev/null | wc -l; }
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
| en | **$(en_md)/61 MD + UI $(en_ui)** | agy |
| ja | **$(ja_md)/61 MD + UI $(ja_ui)** | agy |
| ko | **$(ko_md)/61 MD + UI $(ko_ui)** | ${note} |
| es / pt-BR | 排队/进行中 | agy |

本批日志：\`logs/agy-ko-full.log\`（ok=${ok} fail=${fail} skip=${skip}）
ST
}

# Build work list: prefer LIST; ensure first-batch leftovers included; append remaining UI later
mapfile -t REMAINING < "$LIST"
echo "Remaining MD from list: ${#REMAINING[@]}" | tee -a "$LOG"
update_status "全量续跑启动；列表 ${#REMAINING[@]} 篇 + UI"

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
  md_count=$(ko_md)
  if [[ $HALF_MARKED -eq 0 && $md_count -ge 31 ]]; then
    HALF_MARKED=1
    update_status "过半 md=${md_count}/61；本批 ok=${ok} fail=${fail} skip=${skip}"
    echo "[HALFWAY] md=$md_count ok=$ok $(date '+%H:%M:%S')" | tee -a "$LOG"
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

for name in home.json tools.json bots.json ecosystem.json changelog.json funnel.json; do
  translate_json "$name"
  rc=$?
  if [[ $rc -eq 0 ]]; then ok=$((ok + 1))
  elif [[ $rc -eq 2 ]]; then skip=$((skip + 1))
  else fail=$((fail + 1)); FAIL_LIST+=("json:$name"); fi
done

md_count=$(ko_md)
ui_count=$(ko_ui)
now=$(date '+%Y-%m-%d %H:%M:%S')

{
  echo "=== SUMMARY $(date '+%Y-%m-%d %H:%M:%S %z') ==="
  echo "ok=$ok fail=$fail skip=$skip"
  echo "md_total=$md_count ui=$ui_count"
  echo "FAIL_LIST=${FAIL_LIST[*]:-none}"
} | tee -a "$LOG"

state="ko 全量收尾"
[[ $fail -eq 0 && $md_count -ge 61 ]] && state="**ko 全量完成**"

cat > "$STATUS" << ST
# 翻译进度

- 更新时间：${now} (Asia/Singapore)
- 状态：**translating**

| 语种 | 进度 | 备注 |
|---|---|---|
| zh-Hant | **61/61 + UI 6** | OpenCC 全量 |
| en | **$(en_md)/61 MD + UI $(en_ui)** | agy |
| ja | **$(ja_md)/61 MD + UI $(ja_ui)** | agy |
| ko | **${md_count}/61 MD + UI ${ui_count}** | ${state}；本批 ok=${ok} fail=${fail} skip=${skip} |
| es / pt-BR | 排队/进行中 | agy |

本批日志：\`logs/agy-ko-full.log\`
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
