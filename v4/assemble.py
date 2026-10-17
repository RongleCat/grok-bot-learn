import json, os, re, shutil, sys, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
STAGE = int(os.environ.get("STAGE", "4"))
J = json.load(open("../v3/jobs.json"))
if STAGE >= 2:
    from cases import process
for path, title, *_ in J["jobs"]:
    src = f"out5/{path}.md" if os.path.exists(f"out5/{path}.md") else f"out/{path}.md" if os.path.exists(f"out/{path}.md") else f"../v3/out/{path}.md"
    if not os.path.exists(src): continue
    t = open(src).read()
    slug = path.split("/")[1]
    if STAGE >= 2 and (path.startswith("part2") or path.startswith("cases")) and "> 来源：" not in t:
        t, _ = process(t)
    if STAGE >= 3 and os.path.exists(f"../site/docs/public/info/{slug}.png"):
        i = t.find("\n## ")
        if i > 0:
            t = t[:i] + f"\n\n![{re.sub(r'^第 \d+ 章 ', '', title)}](/info/{slug}.png)\n" + t[i:]
    SI = json.load(open("secinfo.json")).get(slug, {})
    for key, h in SI.items():
        if os.path.exists(f"../site/docs/public/info/{slug}-{key}.png") and h in t:
            t = t.replace(h + "\n", h + f"\n\n![{h[3:]}](/info/{slug}-{key}.png)\n", 1)
    from splitp import split_lines
    t = split_lines(t)
    open(f"../site/docs/{path}.md", "w").write(t)
print("ok", STAGE)
