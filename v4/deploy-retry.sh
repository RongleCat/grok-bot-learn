cd /workspace/grok-bot-learn
for i in 1 2 3; do
  NODE_OPTIONS=--max-old-space-size=4096 ./deploy.sh > v4/deploy4.log 2>&1 && grep -q "pages.dev 200" v4/deploy4.log && { echo "DEPLOY_OK $i $(date)" >> v4/PROGRESS.md; exit 0; }
  sleep 120
done
echo "DEPLOY_FAIL $(date)" >> v4/PROGRESS.md
