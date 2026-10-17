import subprocess, sys, os, re
SK = "/home/box/agent-data/workflows/lieflat-less-ai-tone/SKILL.md"
path = sys.argv[1]
a = open(os.environ.get("SRC", f"out/{path}.md")).read()
T = int(len(a) * 0.5)
q = f"""先阅读 {SK}，按其中规则写出没有 AI 腔的中文。然后把下面这篇网页教程精简到原来的一半左右篇幅：原文约 {len(a)} 字，输出必须控制在 {T} 字以内（代码块不计入也可）。语气像老用户给朋友讲解，平实口语，不要用「须」「禁止」「严禁」这类公文腔堆砌。
要求：
1. 去掉重复、铺垫、空泛的总结和过渡句，把事情讲清楚。
2. 必须保留：所有操作步骤、可复制的提示词代码块、命令、具体数字与限制、容易踩的坑、验收标准、链接和出处。
3. 保留一级标题和所有二级标题的文字与顺序；三级标题可合并。
4. 每段 2 到 4 句；多用列表、编号步骤和表格。
5. 每段只把一个最关键的句子或结论用 **加粗** 标出，不是每段都必须有，全文加粗不要滥用。
6. 不加 emoji、HTML 注释、装饰性标签，不写前言或结束语。只输出完整 Markdown，不要用代码围栏包住全文。

{a}"""
r = subprocess.run(["agy", "--model", "gemini-3.8-flash-high", "--dangerously-skip-permissions", "--add-dir", os.path.dirname(SK), "--print-timeout", "900s", "-p", q], capture_output=True, text=True, stdin=subprocess.DEVNULL, timeout=1000)
b = r.stdout.strip()
if b.startswith("```"):
    b = b.split("\n", 1)[1].rsplit("```", 1)[0]
b = b[b.find("# "):].strip() + "\n"
H = lambda x: re.findall(r"^## .*", x, re.M)
os.makedirs(os.path.dirname(f"out5/{path}.md"), exist_ok=True)
open(f"out5/{path}.md", "w").write(b)
print(path, len(a), len(b), H(a) == H(b), b.count("**") // 2, r.stderr[-300:])
