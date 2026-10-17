import subprocess, sys, os, re, concurrent.futures as cf
SK = "/home/box/agent-data/workflows/lieflat-less-ai-tone/SKILL.md"
RULE = open(SK).read()
a = open("out/part1/05-computer.md").read()
parts = re.split(r"(?m)^(?=## )", a)
os.makedirs("sec5", exist_ok=True)
def job(i):
    s = parts[i]; out = f"sec5/{i:02d}.md"
    if i == 0 or "## 延伸阅读" in s:
        open(out, "w").write(s.strip() + "\n"); return i, len(s), len(s)
    if os.path.exists(out): return i, len(s), len(open(out).read())
    T = int(len(re.sub(r"```.*?```","",s,flags=re.S)) * 0.3)
    q = f"""以下是去 AI 腔写作规则：
{RULE}

按上面规则写出没有 AI 腔的中文，不要调用任何工具，直接输出。把下面这段网页教程大幅精简：代码块以外的正文必须控制在 {T} 字以内（代码块原样保留，不计入）。语气平实口语，像老用户给朋友讲。
1. 去掉重复、铺垫、空泛总结和过渡句，把事讲清楚。
2. 必须保留：操作步骤、可复制的提示词代码块（原样保留）、命令、具体数字与限制、坑点、验收标准、链接。
3. 二级标题原样保留；三级标题可合并或删减。
4. 每段 1 到 3 句，多用列表、编号步骤、表格。
5. 关键句用 **加粗**，每个小节 1 到 3 处，不滥用。
6. 不加 emoji、HTML 注释、装饰标签，不写开场白和结束语。只输出 Markdown，不要代码围栏包住全文。

{s}"""
    for t in range(4):
        try:
            r = subprocess.run(["agy", "--model", "gemini-3.8-flash-high", "--print-timeout", "480s", "-p", q], capture_output=True, text=True, stdin=subprocess.DEVNULL, timeout=540)
        except Exception: continue
        b = r.stdout.strip()
        if b.startswith("```"): b = b.split("\n", 1)[1].rsplit("```", 1)[0]
        k = b.find("## ")
        if k < 0: continue
        b = b[k:].strip() + "\n"
        if s.split("\n")[0].strip() in b and len(b) > len(s) * 0.15 and "print timeout" not in r.stderr:
            open(out, "w").write(b); return i, len(s), len(b)
    return i, len(s), -1
with cf.ThreadPoolExecutor(4) as ex:
    for r in ex.map(job, range(len(parts))): print(*r, flush=True)
print("SECDONE")
