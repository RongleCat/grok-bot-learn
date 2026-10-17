import json, subprocess, sys, os, re, concurrent.futures as cf
from splitp import split, stats
SK = "/home/box/agent-data/workflows/lieflat-less-ai-tone/SKILL.md"
J = json.load(open("../v3/jobs.json"))
def agy(prompt, log):
    try:
        r = subprocess.run(["agy", "--model", "gemini-3.8-flash-high", "--dangerously-skip-permissions", "--add-dir", os.path.dirname(SK), "--print-timeout", "900s", "-p", prompt], capture_output=True, text=True, stdin=subprocess.DEVNULL, timeout=1000)
    except Exception as e:
        open(log, "w").write(str(e)); return ""
    open(log, "w").write(r.stdout + "\n----ERR\n" + r.stderr)
    return r.stdout.strip()
def clean(s):
    s = s.strip()
    if s.startswith("```"):
        s = s.split("\n", 1)[1]
        if s.rstrip().endswith("```"):
            s = s.rstrip()[:-3]
    i = s.find("# ")
    return s[i:].strip() + "\n" if i >= 0 else s
def urls(t): return set(re.findall(r'\]\((https?://[^)\s]+)\)', t))
def job(path):
    out = f"out/{path}.md"
    if os.path.exists(out):
        return path, "skip"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    a = open(f"../v3/out/{path}.md").read()
    tone = f"先阅读 {SK}，按其中规则顺带去掉 AI 腔。" if path == "cases/en2" else "措辞尽量保持原样，只在拆分和改成列表时做必要的衔接调整。"
    q = f"""把下面这篇中文网页教程重新排版成适合网页阅读的结构。{tone}
要求：
1. 每个正文段落 2 到 4 句，一般不超过 120 个汉字；长段落拆开。
2. 并列的要点改成列表，有先后顺序的操作改成编号步骤，多项对比改成表格；长小节下增加三级小标题。
3. 信息量不能缩水：所有事实、数字、命令、提示词、代码块、表格、链接、出处都要保留。
4. 保持一级标题和二级标题的顺序与文字不变。
5. 不要新增原文没有的事实，不要加 emoji、HTML 注释、「小结」「提示」之类装饰性标签，不要写前言或结束语。
6. 只输出完整的 Markdown，不要用代码围栏包住全文。

{a}"""
    lg = f"log/{path.replace('/', '_')}.log"
    prev = open(lg).read().split("\n----ERR\n")[0] if os.path.exists(lg) else ""
    b = clean(prev) if len(prev) > 0.85 * len(a) else clean(agy(q, lg))
    H = lambda x: re.findall(r'^## .*', x, re.M)
    ok = H(a) == H(b) and len(b) <= 1.35 * len(a) and len(b) >= 0.85 * len(a) and len(urls(b)) >= 0.9 * len(urls(a)) and b.startswith(a.split("\n")[0])
    src = "agy" if ok else "script"
    if not ok:
        b = a
    b = split(b)
    open(out, "w").write(b)
    return path, src, len(a), len(b), stats(b)
sel = [j[0] for j in J["jobs"]] if len(sys.argv) < 2 else sys.argv[1:]
with cf.ThreadPoolExecutor(int(os.environ.get("PAR", "6"))) as ex:
    for r in ex.map(job, sel):
        print(*r, flush=True)
