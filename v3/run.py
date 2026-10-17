import json, subprocess, sys, os, concurrent.futures as cf
J = json.load(open("jobs.json"))
U = J["urls"]
SRC = "/workspace/grok-bot-learn/v3/src"
SK = "/home/box/agent-data/workflows/lieflat-less-ai-tone/SKILL.md"
def agy(prompt, log):
    r = subprocess.run(["agy", "--model", "gemini-3.8-flash-high", "--dangerously-skip-permissions", "--add-dir", SRC, "--add-dir", os.path.dirname(SK), "--print-timeout", "900s", "-p", prompt], capture_output=True, text=True, cwd=SRC, stdin=subprocess.DEVNULL)
    open(log, "a").write(r.stdout + "\n----ERR\n" + r.stderr)
    return r.stdout.strip()
def clean(s):
    s = s.strip()
    if s.startswith("```"):
        s = s.split("\n", 1)[1]
        if s.rstrip().endswith("```"):
            s = s.rstrip()[:-3]
    i = s.find("# ")
    return s[i:].strip() + "\n" if i >= 0 else s
def gen(job):
    path, title, scope, files = job
    out = f"out/{path}.md"
    if os.path.exists(out) and os.path.getsize(out) > 3000:
        return path, "skip"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    links = "\n".join(f"- {f}: 《{U[f[:4]][0]}》 {U[f[:4]][1]}" for f in files if f.startswith("fs"))
    p = f"""你在为中文网站「Grok Bot 学习站」写一章正文。
先用读文件工具逐篇完整阅读以下素材（都在 {SRC}）：{', '.join(files)}

本章标题：{title}
本章要覆盖：{scope}

写作要求：
1. 只输出这一章的 Markdown 全文，第一行是「# {title}」，不要输出任何前言、说明或结束语，不要用代码围栏包住全文。
2. 页面层次参考一本实战蓝皮书：开头两三段直接点出读者在这件事上最常遇到的麻烦和这一章能帮他做成什么；然后是若干二级标题小节，按「是什么/怎么做/做到什么程度算好」推进；多用编号步骤、对照表格；给出可以直接复制发给 Bot 的提示词（用 ```text 代码块）；每章要有「容易踩的坑」小节和「做完怎么验收」小节；案例章要为每个案例写清楚谁、做了什么、怎么做、可以借鉴什么。
3. 内容必须来自素材，信息要具体实在（界面名称、按钮、数字、限制、命令、提示词原文），不要编造素材里没有的功能、价格或数字。社区作者自述的数字要写明是作者自述。
4. 方案与价格一律以 2026-10-12 起的 The X Subscription 统一订阅为准。素材中关于「绑定 X 领 $100 开发者积分」、旧资费、旧套餐的内容已经过期，一律不写，也不要提它们过期了。
5. 正文不少于 3000 个汉字，不能是提纲。
6. 文风：像一个用过很久的老用户写给朋友的教程，平实、具体、短句为主。不要用「不仅……而且」「值得注意的是」「总而言之」「赋能」「无缝」「至关重要」「让我们」这类套话，不要用破折号堆砌，不要每段都以总结句收尾，不要用 emoji。
7. 引用社区文章时，在相关段落末尾用 Markdown 链接标出处，可用链接如下：
{links}
官方文档链接格式：docs_grok-bot_xxx.md 对应 https://cursor.com/cn/docs/grok-bot/xxx ，help_grok-bot_xxx.md 对应 https://cursor.com/cn/help/grok-bot/xxx 。
8. 文末加「## 延伸阅读」列出用到的官方页面与社区原文链接。
9. 不要出现 HTML 注释。
"""
    if os.path.exists(out + ".draft") and os.path.getsize(out + ".draft") > 3000:
        a = open(out + ".draft").read()
    else:
        a = clean(agy(p, f"log/{path.replace('/', '_')}.gen.log"))
    if len(a) < (1200 if path.startswith("cases") else 2500):
        return path, f"short {len(a)}"
    open(out + ".draft", "w").write(a)
    q = f"""先阅读 {SK}，严格按照其中的规则，对下面这篇 Markdown 做去 AI 味改写。保持标题、小节顺序、列表、表格、代码块、链接和所有事实不变。只输出改写后的 Markdown 全文，不要任何说明，不要用代码围栏包住全文。

{a}"""
    b = clean(agy(q, f"log/{path.replace('/', '_')}.tone.log"))
    if len(b) < 0.7 * len(a):
        b = a
    open(out, "w").write(b)
    return path, len(b)
sel = J["jobs"] if len(sys.argv) < 2 else [j for j in J["jobs"] if j[0] in sys.argv[1:]]
with cf.ThreadPoolExecutor(int(os.environ.get("PAR", "6"))) as ex:
    for r in ex.map(gen, sel):
        print(*r, flush=True)
