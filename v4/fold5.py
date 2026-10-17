import re, glob
t = "".join(open(f).read().rstrip() + "\n\n" for f in sorted(glob.glob("sec5/*.md")))
out, head, lines, i = [], "", t.split("\n"), 0
while i < len(lines):
    l = lines[i]
    m = re.match(r"#{2,4} (?:\d+\.\s*)?(.*)", l)
    if m: head = m.group(1).strip()
    if l.startswith("```"):
        j = i + 1
        while j < len(lines) and not lines[j].startswith("```"): j += 1
        blk = lines[i:j + 1]
        if len(blk) > 8:
            name = "部署与登记提示词" if "管家" in blk[1]+" ".join(blk[:6]) or "服务管家" in "\n".join(blk) and "恢复" not in blk[1] else "重置后的一键恢复提示词"
            out += [f"::: details {name}", *blk, ":::"]
        else:
            out += blk
        i = j + 1; continue
    out.append(l); i += 1
t = re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip() + "\n"
open("out5/part1/05-computer.md", "w").write(t)
nc = re.sub(r"```.*?```", "", t, flags=re.S)
print("total", len(t), "noncode", len(nc), "bold", t.count("**") // 2, "details", t.count("::: details"))
