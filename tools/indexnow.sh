#!/usr/bin/env bash
set -euo pipefail
HOST="bot.tiezhu.si"
KEY="$(basename "$(ls "$(dirname "$0")"/../site/docs/public/*.txt | grep -E '/[0-9a-f]{32}\.txt$' | head -1)" .txt)"
URLS=$(curl -fsS "https://$HOST/sitemap.xml" | grep -oE '<loc>[^<]+' | sed 's/<loc>//' | python3 -c 'import sys,json;print(json.dumps([l.strip() for l in sys.stdin if l.strip()]))')
BODY="{\"host\":\"$HOST\",\"key\":\"$KEY\",\"keyLocation\":\"https://$HOST/$KEY.txt\",\"urlList\":$URLS}"
for EP in https://api.indexnow.org/indexnow https://www.bing.com/indexnow https://yandex.com/indexnow; do
  curl -sS -o /dev/null -w "$EP %{http_code}\n" -H 'Content-Type: application/json; charset=utf-8' --data "$BODY" "$EP"
done
