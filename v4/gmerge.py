import sys, os, re
P = sys.argv[1]; slug = P.split("/")[1]
D = os.environ.get("D","gsec") + f"/{slug}"
a=""
import glob
t = "".join(open(f).read().rstrip() + "\n\n" for f in sorted(glob.glob(f"{D}/*.md")))
out, lines, i = [], t.split("\n"), 0
while i < len(lines):
    l = lines[i]
    if l.lstrip().startswith("```"):
        j = i + 1
        while j < len(lines) and not lines[j].lstrip().startswith("```"): j += 1
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
