#!/usr/bin/env bash
BACKUP=/workspace/grok-bot-learn/i18n-project/backups/en
SITE=/workspace/grok-bot-learn/site/docs/en
LOCALE_SITE=/workspace/grok-bot-learn/site/docs/.vitepress/theme/locales/en
while true; do
  sleep 20
  python3 - <<'PY'
import shutil
from pathlib import Path
src=Path('/workspace/grok-bot-learn/i18n-project/backups/en')
dst=Path('/workspace/grok-bot-learn/site/docs/en')
if not src.exists():
    raise SystemExit
for f in src.rglob('*'):
    if not f.is_file() or 'locales' in f.parts: continue
    rel=f.relative_to(src)
    t=dst/rel
    if (not t.exists()) or t.stat().st_size < f.stat().st_size:
        t.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(f, t)
ldst=Path('/workspace/grok-bot-learn/site/docs/.vitepress/theme/locales/en')
ldst.mkdir(parents=True, exist_ok=True)
for f in (src/'locales').glob('*.json') if (src/'locales').exists() else []:
    t=ldst/f.name
    if (not t.exists()) or t.stat().st_size < f.stat().st_size:
        shutil.copyfile(f, t)
PY
done
