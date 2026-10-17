cd /workspace/grok-bot-learn/v3
for i in 1 2 3; do
  rm -f out/cases/en2.md
  PAR=1 python3 run.py cases/en2
  if ! cmp -s out/cases/en2.md out/cases/en2.md.draft && [ -s out/cases/en2.md ]; then echo "TONE_OK try $i"; break; fi
  echo "TONE_FAIL try $i"; [ $i -lt 3 ] && sleep 240
done
cp out/cases/en2.md.draft /tmp/en2.draft.bak
if [ -s out/cases/en2.md ] && ! cmp -s out/cases/en2.md out/cases/en2.md.draft; then
  cd .. && python3 v3/assemble.py && bash deploy.sh > v3/deploy3.log 2>&1 && echo DEPLOY_OK
fi
echo ALLDONE
