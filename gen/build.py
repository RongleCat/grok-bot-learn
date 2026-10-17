import json, os, re, shutil
R = "/workspace/grok-bot-learn"
D = R + "/site/docs"
O = R + "/v3/out"
J = json.load(open(R + "/v3/jobs.json"))["jobs"]
for d in ["guide", "appendix", "cases", "part1", "part2", "part3", "part4"]:
    shutil.rmtree(f"{D}/{d}", ignore_errors=True)
def fix(s):
    s = re.sub(r"\]\((https://cursor\.com/[^)\s]*?)\.md(#[^)\s]*)?\)", lambda m: f"]({m.group(1)}{m.group(2) or ''})", s)
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
    return s.strip() + "\n"
side = {}
for path, title, _, _ in J:
    if path.startswith("cases"):
        continue
    src = f"{O}/{path}.md"
    if not os.path.exists(src):
        continue
    os.makedirs(os.path.dirname(f"{D}/{path}.md"), exist_ok=True)
    open(f"{D}/{path}.md", "w").write(fix(open(src).read()))
    side.setdefault(path.split("/")[0], []).append([re.sub(r"^第 (\d+) 章 ", r"\1. ", title.split("：")[0]), "/" + path])
parts = []
for name in ["tiezhu", "cn", "en1", "en2"]:
    src = f"{O}/cases/{name}.md"
    if os.path.exists(src):
        parts.append(re.sub(r"^(#+) ", lambda m: "#" + m.group(1) + " ", fix(open(src).read()), flags=re.M))
os.makedirs(f"{D}/cases", exist_ok=True)
open(f"{D}/cases/index.md", "w").write("# 案例库\n\n" + "\n".join(parts))
json.dump(side, open(f"{D}/.vitepress/sidebar.json", "w"), ensure_ascii=False, indent=1)
print({k: len(v) for k, v in side.items()}, len(parts))
