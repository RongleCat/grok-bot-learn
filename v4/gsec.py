import subprocess, sys, os, re, concurrent.futures as cf
SK = "/home/box/agent-data/workflows/lieflat-less-ai-tone/SKILL.md"
RULE = open(SK).read()
P = sys.argv[1]; slug = P.split("/")[1]
a = open(os.environ.get("SRC","../site/docs/{P}.md").format(P=P)).read()
a = "\n".join(l for l in a.split("\n") if not l.startswith("![") or "/info/" not in l)
def hsplit(t, mk):
    out, cur, fence = [], [], False
    for l in t.split("\n"):
        if l.startswith("```"): fence = not fence
        if not fence and l.startswith(mk) and cur:
            out.append("\n".join(cur) + "\n"); cur = []
        cur.append(l)
    out.append("\n".join(cur))
    return out
parts0 = hsplit(a, "## ")
parts = []
for p in parts0:
    if len(p) > 2500 and "\n### " in p: parts += hsplit(p, "### ")
    else: parts.append(p)
D = os.environ.get("D","gsec") + f"/{slug}"; os.makedirs(D, exist_ok=True)
def job(i):
    s = parts[i]; out = f"{D}/{i:02d}.md"
    if "## 延伸阅读" in s or len(s) < 200:
        open(out, "w").write(s.strip() + "\n"); return i, len(s), len(s)
    if os.path.exists(out): return i, len(s), len(open(out).read())
    codes = re.findall(r"(?s:```.*?```)|(?:^> (?:来源|作者)：.*(?:\n|$))+|^!\[[^\]]*\]\(/cases-img/[^)]*\)", s, flags=re.M)
    ph = s
    for n, c in enumerate(codes): ph = ph.replace(c.rstrip("\n"), f"[[CODE{n}]]", 1)
    codes = [c.rstrip("\n") for c in codes]
    T = int(len(re.sub(r"\[\[CODE\d+\]\]", "", ph)) * float(os.environ.get("R","0.4")))
    q = f"""以下是去 AI 腔写作规则：
{RULE}

按上面规则写出没有 AI 腔的中文，不要调用任何工具，直接输出。把下面这段网页教程大幅精简：正文控制在 {T} 字以内。语气平实口语，像老用户给朋友讲。
1. 去掉重复、铺垫、空泛总结和过渡句，把事讲清楚。
2. 必须保留：操作步骤、命令、具体数字与限制、坑点、验收标准、链接、图片行。
3. 形如 [[CODE0]] 的占位符各自单独占一行原样保留，不得改动或删除。
4. 二级标题原样保留；三级标题可合并或删减。
5. 每段 1 到 3 句，多用列表、编号步骤、表格。
6. 关键句用 **加粗**，每个小节 1 到 3 处，不滥用。
7. 不加 emoji、HTML 注释、装饰标签，不写开场白和结束语。只输出 Markdown，不要代码围栏包住全文。

{ph}"""
    for t in range(3):
        try:
            r = subprocess.run(["agy", "--model", "gemini-3.8-flash-high", "--print-timeout", "480s", "-p", q], capture_output=True, text=True, stdin=subprocess.DEVNULL, timeout=540)
        except Exception: continue
        b = r.stdout.strip()
        if b.startswith("```"): b = b.split("\n", 1)[1].rsplit("```", 1)[0]
        mk = s.split(" ")[0] + " "
        k = b.find("\n" + mk) + 1 if not b.startswith(mk) else 0
        if not i: k = b.find("# ")
        if k == 0 and not b.startswith(mk) and i: k = -1
        if k < 0: continue
        b = b[k:].strip() + "\n"
        if not all(f"[[CODE{n}]]" in b for n in range(len(codes))): continue
        for n, c in enumerate(codes): b = b.replace(f"[[CODE{n}]]", c, 1)
        if s.split("\n")[0].strip() in b and len(b) > len(s) * 0.15:
            open(out, "w").write(b); return i, len(s), len(b)
    return i, len(s), -1
with cf.ThreadPoolExecutor(3) as ex:
    for r in ex.map(job, range(len(parts))): print(slug, *r, flush=True)
import glob
t = "".join(open(f).read().rstrip() + "\n\n" for f in sorted(glob.glob(f"{D}/*.md")))
if len(glob.glob(f"{D}/*.md")) != len(parts): print("INCOMPLETE", slug); sys.exit(1)
out, lines, i = [], t.split("\n"), 0
while i < len(lines):
    l = lines[i]
    if l.startswith("```"):
        j = i + 1
        while j < len(lines) and not lines[j].startswith("```"): j += 1
        blk = lines[i:j + 1]
        if len(blk) > 8:
            h = next((x.lstrip("#").strip() for x in reversed(out) if x.startswith("#")), "提示词")
            out += [f"::: details {re.sub(r'^\\d+\\.\\s*', '', h)}", *blk, ":::"]
        else: out += blk
        i = j + 1; continue
    out.append(l); i += 1
t = re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip() + "\n"
os.makedirs(os.path.dirname(f"out5/{P}.md"), exist_ok=True)
open(f"out5/{P}.md", "w").write(t)
print("DONE", slug, len(a), len(t), "bold", t.count("**") // 2, "details", t.count("::: details"), flush=True)
