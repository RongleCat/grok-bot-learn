import subprocess, os, sys, concurrent.futures as cf
CH = ["part1/01-what-is","part1/02-plans","part1/03-install","part1/04-handoff","part1/05-computer","part1/06-memory","part1/07-apps","part1/08-skills-routines","part1/09-group-team","part1/10-usage","part1/11-safety","part3/19-orchestration","part3/20-automation","part3/21-backup","part3/22-feishu-wechat","part4/23-enterprise","part4/24-roles","part4/25-faq"]
BOTS = sorted(f for f in os.listdir("info/bots") if f.endswith(".png"))
def job(i_p):
    i, p = i_p
    slug = p.split("/")[1]
    out = f"info/{slug}.html"
    if os.path.exists(out) and os.path.getsize(out) > 1500:
        return p, "skip"
    bot = BOTS[i % len(BOTS)]
    prompt = f"""Read /workspace/grok-bot-learn/v3/out/{p}.md (a Chinese tutorial chapter). Create ONE infographic that helps a beginner understand the chapter's core concept (a flow, structure diagram, comparison or checklist; pick the single most useful one).
Write it as a single self-contained HTML file at /workspace/grok-bot-learn/v4/{out}.
Rules:
- Canvas exactly 1200x760 px, body margin 0, white/very light warm gray background, near-black text, rounded cards (radius 20px+), thin borders, generous whitespace, system Chinese sans-serif fonts (PingFang SC, Noto Sans CJK SC, sans-serif). Use at most 2 accent colors.
- Include the decorative image bots/{bot} (relative path) once, about 90-130px, placed in a corner or beside the title. Do not distort it.
- All text in Simplified Chinese, taken strictly from the chapter: no invented facts, numbers, prices or features. Short labels, max ~60 visible text items; nothing overflowing or overlapping; minimum font size 15px.
- A short title at top. No subtitle like "信息图", no footer, no source line, no watermark, no decorative tags, no emoji.
- No HTML/CSS/JS comments anywhere. No external resources, no scripts.
Only write the file; reply DONE."""
    r = subprocess.run(["codex", "exec", "--skip-git-repo-check", "--dangerously-bypass-approvals-and-sandbox", "-C", "/workspace/grok-bot-learn/v4", prompt], capture_output=True, text=True, stdin=subprocess.DEVNULL, timeout=1500)
    open(f"log/info-{slug}.log", "w").write(r.stdout[-3000:] + r.stderr[-2000:])
    return p, os.path.exists(out)
sel = list(enumerate(CH)) if len(sys.argv) < 2 else [(i, p) for i, p in enumerate(CH) if p in sys.argv[1:]]
with cf.ThreadPoolExecutor(4) as ex:
    for r in ex.map(job, sel):
        print(*r, flush=True)
