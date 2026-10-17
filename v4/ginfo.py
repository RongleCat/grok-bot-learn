import subprocess, os, sys, concurrent.futures as cf
P = sys.argv[1]; slug = P.split("/")[1]
SEC = [(s.split("|")[0], s.split("|")[1], s.split("|")[2]) for s in sys.argv[2:]]
def job(x):
    key, sec, bot = x
    out = f"info/{slug}-{key}.html"
    if os.path.exists(out): return out, "skip"
    p = f"""Read the section titled "{sec}" in /workspace/grok-bot-learn/v4/out5/{P}.md (Chinese tutorial). Create ONE infographic that makes that section's core idea easy to grasp (flow, structure, comparison or checklist).
Write a single self-contained HTML file /workspace/grok-bot-learn/v4/{out}.
Rules: canvas exactly 1200x760 px, body margin 0, html/body overflow hidden; light warm background, near-black text, rounded cards (radius 20px+), thin borders, generous whitespace, fonts "PingFang SC","Noto Sans CJK SC",sans-serif, at most 2 accent colors. Include bots/{bot} once (90-130px) near the title, undistorted. Simplified Chinese text taken strictly from that section, no invented facts. Max ~40 short text items, min font 15px. Everything must fit with >=36px margin at the bottom; nothing overflowing, overlapping or clipped; no awkward breaks splitting short words. Short title only; no eyebrow, kicker or small label line above or below the title, no subtitle like 信息图, no footer, source, watermark, emoji or decorative tags. No comments of any kind, no scripts, no external resources.
Verify by rendering: node -e "const {{chromium}}=require('/workspace/grok-bot-learn/site/node_modules/playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:1200,height:760}}}});await p.goto('file:///workspace/grok-bot-learn/v4/{out}');await p.screenshot({{path:'/tmp/{slug}-{key}.png'}});await b.close()}})()" then view /tmp/{slug}-{key}.png and fix any layout problem. Reply DONE."""
    try:
        r = subprocess.run(["codex", "exec", "--skip-git-repo-check", "--dangerously-bypass-approvals-and-sandbox", "-C", "/workspace/grok-bot-learn/v4", p], capture_output=True, text=True, stdin=subprocess.DEVNULL, timeout=2400)
    except Exception:
        return out, "timeout"
    return out, os.path.exists(out)
with cf.ThreadPoolExecutor(1) as ex:
    for r in ex.map(job, SEC):
        print(*r, flush=True)
