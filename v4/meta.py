import re, glob, json, os
M = {}
for f in sorted(glob.glob("../sources/feishu/[0-9][0-9]_*.md")):
    n = os.path.basename(f)[:2]
    t = open(f, encoding="utf-8", errors="ignore").read()
    h = re.search(r'^> 原文：\[(.+?)\]\((https?://[^)]+)\)｜作者：([^｜]+?)\s+@([\\\w]+)', t, re.M)
    imgs = [(alt, tok) for alt, tok in re.findall(r'!\[([^\]]*)\]\(https://feishu\.cn/file/(\w+)\)', t) if "视频" not in alt]
    M["fs" + n] = dict(file=f, title=h.group(1).replace("\\", "") if h else None, url=h.group(2) if h else None, author=h.group(3).strip() if h else None, handle=h.group(4).replace("\\", "") if h else None, imgs=imgs)
json.dump(M, open("meta.json", "w"), ensure_ascii=False, indent=1)
for k, v in M.items():
    if v["imgs"] or v["url"]:
        print(k, v["author"], v["handle"], len(v["imgs"]))
