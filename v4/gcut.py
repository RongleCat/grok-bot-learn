import subprocess, sys, os, re, shutil
PR = r"(?s:```.*?```)|(?:^> (?:来源|作者)：.*(?:\n|$))+|^!\[[^\]]*\]\(/cases-img/[^)]*\)"
RULE = open("/home/box/agent-data/workflows/lieflat-less-ai-tone/SKILL.md").read()
P = sys.argv[1]; slug = P.split("/")[1]
orig = {int(l.split()[1]): int(l.split()[2]) for l in open(sys.argv[2]) if l.startswith(slug + " ")}
S, D = f"gsec/{slug}", f"gsec3/{slug}"
ORIG_NC = {}
if "--nc" in sys.argv:
    _a = "\n".join(l for l in open(f"../site/docs/{P}.md").read().split("\n") if not (l.startswith("![") and "/info/" in l))
    for _i, _p in enumerate(re.split(r"(?m)^(?=## )", _a)): ORIG_NC[_i] = len(re.sub(PR, "", _p, flags=re.M))
os.makedirs(D, exist_ok=True)
nc = lambda x: len(re.sub(PR, "", x, flags=re.M))
for f in sorted(os.listdir(S)):
    i = int(f[:2]); s = open(f"{S}/{f}").read(); out = f"{D}/{f}"
    if os.path.exists(out): continue
    T = int(orig.get(i, len(s)) * 0.5)
    if "--nc" in sys.argv: T = int(ORIG_NC[i] * 0.5)
    if "## 延伸阅读" in s or nc(s) <= T * 1.1:
        shutil.copy(f"{S}/{f}", out); print(slug, i, "keep", nc(s), T, flush=True); continue
    codes = [c.rstrip("\n") for c in re.findall(PR, s, flags=re.M)]; ph = s
    for n, c in enumerate(codes): ph = ph.replace(c, f"[[CODE{n}]]", 1)
    Tc = T - (nc(s) - len(re.sub(r"\[\[CODE\d+\]\]", "", ph)))
    q = f"""以下是去 AI 腔写作规则：
{RULE}

按上面规则写出没有 AI 腔的中文，不要调用任何工具，直接输出。下面这段教程现在约 {len(ph)} 字，请删到 {T} 字以内（硬性要求，超出即失败）。
可以删：背景铺垫、重复上文的话、举例里的第二第三个例子、作者自述的旁枝细节、“未核”类说明以外的修饰语、过渡句、总结句、表格里次要的列。
不能删：操作步骤和菜单路径、命令、具体价格数字与限制、坑点、验收标准、链接、图片行，以及形如 [[CODE0]] 的占位符（各自单独一行原样保留）。
二级标题原样保留，三级标题可合并。每段 1 到 3 句，关键句 **加粗**，每节 1 到 3 处。不加 emoji、注释、装饰标签，不写开场白和结束语，只输出 Markdown。

{ph}"""
    best = None
    for t in range(2):
        try:
            r = subprocess.run(["agy", "--model", "gemini-3.8-flash-high", "--print-timeout", "300s", "-p", q], capture_output=True, text=True, stdin=subprocess.DEVNULL, timeout=360)
        except Exception: continue
        b = r.stdout.strip()
        if b.startswith("```"): b = b.split("\n", 1)[1].rsplit("```", 1)[0]
        k = b.find("## ") if i else b.find("# ")
        if k < 0: continue
        b = b[k:].strip() + "\n"
        if not all(f"[[CODE{n}]]" in b for n in range(len(codes))) or s.split("\n")[0].strip() not in b: continue
        for n, c in enumerate(codes): b = b.replace(f"[[CODE{n}]]", c, 1)
        if nc(b) <= T * 1.1 and nc(b) > T * 0.4: best = b; break
    if best: open(out, "w").write(best); print(slug, i, "cut", nc(s), nc(best), T, flush=True)
    else: shutil.copy(f"{S}/{f}", out); print(slug, i, "miss", nc(s), T, flush=True)
print("CUTDONE", slug, flush=True)
