import re, json, os, glob, sys
M = json.load(open("meta.json"))
J = json.load(open("../v3/jobs.json"))
U2F = {}
for k, (t, u) in J["urls"].items():
    U2F[u.rstrip("/")] = k
for k, v in M.items():
    if v["url"]:
        U2F[v["url"].rstrip("/")] = k
        U2F[v["url"].split("/status/")[0] + "/status/" + v["url"].split("/status/")[-1]] = k
CASEF = {k for k, v in M.items() if v["author"] and k not in ("fs07", "fs08", "fs16")}
SKIP = re.compile(r"容易踩的坑|做完怎么验收|延伸阅读|提示词库|对照|索引")
PICK = {"fs09": [1, 2], "fs15": [0, 2], "fs56": [], "fs30": []}
def imgs(k):
    a = sorted(glob.glob(f"img/{k}-*"))
    if k in PICK:
        return [p for p in a if int(os.path.basename(p).split("-")[1].split(".")[0]) in PICK[k]]
    return a[:2]
def fs_in(text):
    out = []
    for u in re.findall(r"\((https?://[^)\s]+)\)", text):
        k = U2F.get(u.rstrip("/"))
        if k in CASEF and k not in out:
            out.append(k)
    return out
def by_name(h, body, used):
    t = [k for k in sorted(CASEF) if M[k]["title"] and M[k]["title"][:24] in h and k not in used]
    if t:
        return t[0]
    a = [k for k in sorted(CASEF) if M[k]["author"] and len(M[k]["author"]) >= 3 and M[k]["author"] in h and k not in used]
    if not a:
        return None
    l = [k for k in fs_in(body) if k in a]
    return (l or a)[0]
def head(k):
    v = M[k]
    s = f"> 来源：[{v['title']}]({v['url']})  \n> 作者：[{v['author']} @{v['handle']}](https://x.com/{v['handle']})\n"
    for p in imgs(k):
        s += f"\n![{v['title']}](/cases-img/{os.path.basename(p)})\n"
    return s
def process(text):
    lines = text.split("\n")
    hs = [(i, len(m.group(1))) for i, l in enumerate(lines) if (m := re.match(r"^(#{2,3}) ", l))]
    used, ins = set(), {}
    for lvl in (3, 2):
        for n, (i, d) in enumerate(hs):
            if d != lvl or SKIP.search(lines[i]):
                continue
            j = next((x for x, dd in hs[n + 1:] if dd <= (3 if lvl == 3 else 2)), len(lines))
            if lvl == 2 and any(i < x < j for x in ins):
                continue
            body = "\n".join(lines[i:j])
            k = by_name(lines[i], body, used)
            if not k:
                c = [x for x in fs_in(body) if x not in used]
                k = c[0] if len(c) == 1 or (c and lvl == 3) else None
                if lvl == 2 and not re.search(r"案例", lines[i]):
                    k = None
            if k and k not in used:
                used.add(k); ins[i] = k
    for i in sorted(ins, reverse=True):
        lines.insert(i + 1, "\n" + head(ins[i]).rstrip())
    return "\n".join(lines), [ins[i] for i in sorted(ins)]
if __name__ == "__main__":
    for f in sys.argv[1:]:
        t, ks = process(open(f).read())
        print(f, ks)
