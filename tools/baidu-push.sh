#!/usr/bin/env bash
set -euo pipefail
SITE="https://bot.fmcat.top"
ENV="$HOME/.agents/secrets/baidu.env"
if [ ! -f "$ENV" ]; then
  echo "missing $ENV (needs BAIDU_PUSH_TOKEN from 百度搜索资源平台 > 普通收录 > API提交)" >&2
  exit 1
fi
set -a; source "$ENV"; set +a
: "${BAIDU_PUSH_TOKEN:?BAIDU_PUSH_TOKEN not set in $ENV}"
URLS=$(curl -fsS "$SITE/sitemap.xml" | grep -oE '<loc>[^<]+' | sed 's/<loc>//')
echo "$URLS" | curl -sS -H 'Content-Type: text/plain' --data-binary @- "http://data.zz.baidu.com/urls?site=$SITE&token=$BAIDU_PUSH_TOKEN"
echo
