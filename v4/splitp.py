import re, sys
END = re.compile(r'(?<=[。！？])(?![”」』）)\]】])|(?<=[。！？][”」』）])')
LINK = re.compile(r'!?\[[^\]\n]*\]\([^)\n]*\)|`[^`\n]+`')
def chunks(p, lim=110):
    keep = []
    def hide(m):
        keep.append(m.group(0))
        return f"\x00{len(keep) - 1}\x00"
    p = LINK.sub(hide, p)
    back = lambda x: re.sub(r"\x00(\d+)\x00", lambda m: keep[int(m.group(1))], x)
    s = [x for x in END.split(p) if x]
    out, cur = [], ""
    for x in s:
        if cur and len(back(cur)) + len(back(x)) > lim:
            out.append(cur); cur = x
        else:
            cur += x
    if cur:
        out.append(cur)
    if len(out) > 1 and len(back(out[-1])) < 25:
        x = out.pop(); out[-1] += x
    return [back(x) for x in out]
def split(text, lim=110):
    res, fence = [], False
    for block in re.split(r'\n{2,}', text):
        lines = block.split('\n')
        if block.count('```') % 2 == 1:
            fence = not fence
            res.append(block); continue
        if fence or len(lines) > 1 or re.match(r'\s*([#|>\-*+<]|\d+[.)]|```|!\[)', block) or len(block) <= 130:
            res.append(block); continue
        res.extend(chunks(block, lim))
    return '\n\n'.join(res).rstrip() + '\n'
def stats(text):
    fence, n, worst = False, 0, 0
    for b in re.split(r'\n{2,}', text):
        if b.count('```') % 2 == 1:
            fence = not fence; continue
        if fence or re.match(r'\s*([#|>\-*+<]|\d+[.)]|```|!\[)', b):
            continue
        n += 1; worst = max(worst, len(b))
    return n, worst
if __name__ == "__main__":
    for f in sys.argv[1:]:
        t = open(f).read(); print(f, stats(t), stats(split(t)))
def split_lines(text, lim=110):
    out, fence = [], False
    for ln in text.split("\n"):
        if ln.lstrip().startswith("```"):
            fence = not fence; out.append(ln); continue
        if fence or ln.startswith(("#", "|", "!")) or len(ln) <= 125:
            out.append(ln); continue
        m = re.match(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$", ln)
        q = re.match(r"^(\s*>\s?)(.*)$", ln)
        if m:
            ind = m.group(1) + " " * (len(m.group(2)) + 1)
            c = chunks(m.group(3), lim)
            out.append(f"{m.group(1)}{m.group(2)} {c[0]}")
            for x in c[1:]:
                out += ["", ind + x]
        elif q:
            c = chunks(q.group(2), lim)
            for k, x in enumerate(c):
                if k:
                    out.append(q.group(1).rstrip())
                out.append(q.group(1) + x)
        else:
            c = chunks(ln, lim)
            for k, x in enumerate(c):
                if k:
                    out.append("")
                out.append(x)
    return "\n".join(out)
