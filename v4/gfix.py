import subprocess, sys, json
F = json.load(open("fix.json"))
for slug in sys.argv[1:]:
    p = f"""Fix the infographic /workspace/grok-bot-learn/v4/info/{slug}.html (1200x760 canvas). Problem: {F.get(slug,'layout overflow')} Make everything fit inside the canvas with >=36px bottom margin, no overlap or clipping, no awkward word breaks; you may shorten text or reduce sizes, keep content facts. No eyebrow or small label line above the title, no comments, no scripts. Verify by rendering with node + /workspace/grok-bot-learn/site/node_modules/playwright to /tmp/{slug}-fix.png, view it, iterate. Reply DONE."""
    r = subprocess.run(["codex", "exec", "--skip-git-repo-check", "--dangerously-bypass-approvals-and-sandbox", "-C", "/workspace/grok-bot-learn/v4", p], capture_output=True, text=True, stdin=subprocess.DEVNULL, timeout=2400)
    print(slug, "fixed", flush=True)
