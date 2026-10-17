import json, os, re, shutil
J = json.load(open("v3/jobs.json"))
side = {}
for path, title, *_ in J["jobs"]:
    src = f"v3/out/{path}.md"
    if not os.path.exists(src):
        continue
    dst = f"site/docs/{path}.md"
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy(src, dst)
    k = path.split("/")[0]
    m = re.match(r"第 (\d+) 章 (?:案例：)?([^：]+)", title)
    t = f"{m.group(1)}. {m.group(2)}" if m else title
    side.setdefault(k, []).append([t, "/" + path])
json.dump(side, open("site/docs/.vitepress/sidebar.json", "w"), ensure_ascii=False, indent=1)
cards = []
for t, link in side.get("cases", []):
    body = open(f"site/docs{link}.md").read().split("\n")
    lead = next((l for l in body[1:] if l.strip() and not l.startswith("#")), "")
    n = sum(1 for l in body if l.startswith("### "))
    cards.append(f"## [{t}]({link})\n\n{lead}\n\n收录 {n} 篇\n")
open("site/docs/cases/index.md", "w").write("# 案例库\n\n社区作者和官方团队用 Grok Bot 做成的真实项目，每篇写清谁、做了什么、怎么做、能借鉴什么，并附原文链接。\n\n" + "\n".join(cards))
print(side.keys(), len(cards))
