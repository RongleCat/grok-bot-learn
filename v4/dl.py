import json, subprocess, os, glob
M = json.load(open("meta.json"))
for k, v in M.items():
    if k in ("fs07", "fs08", "fs16"):
        continue
    for i, (alt, tok) in enumerate(v["imgs"][:4]):
        base = f"img/{k}-{i}"
        if glob.glob(base + ".*"):
            continue
        r = subprocess.run(["lark-cli", "docs", "+media-download", "--token", tok, "--output", base], capture_output=True, text=True, stdin=subprocess.DEVNULL)
        print(k, i, glob.glob(base + ".*") or r.stderr[-200:], flush=True)
