import subprocess, sys, json, concurrent.futures as cf
FIX = json.load(open("fix.json"))
def job(item):
    slug, issue = item
    p = f"""The file /workspace/grok-bot-learn/v4/info/{slug}.html is an infographic rendered at a fixed 1200x760 viewport. Visual review found: {issue}
Fix it by editing that file. Every element must sit fully inside the 1200x760 canvas with at least 32px margin at the bottom; no text may overflow, overlap other boxes, or be clipped by its card; avoid awkward line breaks that split short Chinese words across lines (give labels enough width or shorten them using wording from the chapter /workspace/grok-bot-learn/v3/out/ files). Reduce the number of items if needed rather than shrinking fonts below 15px. Keep the same style, the bot image, and Simplified Chinese text taken from the chapter. No comments of any kind. You may verify by running: node -e "const {{chromium}}=require('/workspace/grok-bot-learn/site/node_modules/playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:1200,height:760}}}});await p.goto('file:///workspace/grok-bot-learn/v4/info/{slug}.html');await p.screenshot({{path:'/tmp/{slug}.png'}});await b.close()}})()" and looking at /tmp/{slug}.png. Reply DONE."""
    try:
        r = subprocess.run(["codex", "exec", "--skip-git-repo-check", "--dangerously-bypass-approvals-and-sandbox", "-C", "/workspace/grok-bot-learn/v4", p], capture_output=True, text=True, stdin=subprocess.DEVNULL, timeout=2400)
    except Exception as e:
        return slug, 'timeout'
    open(f"log/fix-{slug}.log", "w").write(r.stdout[-3000:] + r.stderr[-1500:])
    return slug, r.returncode
with cf.ThreadPoolExecutor(3) as ex:
    for r in ex.map(job, FIX.items()):
        print(*r, flush=True)
