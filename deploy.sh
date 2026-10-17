#!/usr/bin/env bash
set -euo pipefail
set -a
source "$HOME/.agents/secrets/cloudflare.env"
set +a
PROJECT="${PROJECT:-tiezhu-grokbot}"
DOMAIN="${DOMAIN:-bot.tiezhu.si}"
cd "$(dirname "$0")/site"
npm run build
if ! npx -y wrangler@3 pages project list 2>/dev/null | grep -q "│ $PROJECT "; then
  npx -y wrangler@3 pages project create "$PROJECT" --production-branch main
fi
npx -y wrangler@3 pages deploy docs/.vitepress/dist --project-name "$PROJECT" --branch main --commit-dirty=true
API="https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/pages/projects/$PROJECT/domains"
if ! curl -fsS -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" "$API" | grep -q "\"name\":\"$DOMAIN\""; then
  curl -sS -X POST -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" -H "Content-Type: application/json" --data "{\"name\":\"$DOMAIN\"}" "$API"
  echo
fi
curl -sS -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" "$API/$DOMAIN"
echo
curl -s -o /dev/null -w "https://$PROJECT.pages.dev %{http_code}\n" "https://$PROJECT.pages.dev/"
