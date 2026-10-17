import subprocess
from PIL import Image, ImageDraw, ImageFont
K = ["s3", "s5", "s6", "s7"]
js = "const {chromium}=require('/workspace/grok-bot-learn/site/node_modules/playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1200,height:760},deviceScaleFactor:2});for(const k of %s){await p.goto('file:///workspace/grok-bot-learn/v4/info/05-computer-'+k+'.html');await p.waitForTimeout(300);await p.screenshot({path:'/tmp/r5-'+k+'.png'})}await b.close()})()" % K
subprocess.run(["node", "-e", js], check=True)
f = [x for x in subprocess.run(["fc-list", ":lang=zh:style=Bold", "file"], capture_output=True, text=True).stdout.split("\n") if "Sans" in x][0].split(":")[0]
font = ImageFont.truetype(f, 26)
for k in K:
    im = Image.open(f"/tmp/r5-{k}.png").convert("RGBA")
    o = Image.new("RGBA", im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(o)
    t = "铁柱AGI"; w, h = d.textbbox((0, 0), t, font=font)[2:]
    d.text((im.width - w - 36, im.height - h - 28), t, font=font, fill=(60, 60, 60, 120))
    Image.alpha_composite(im, o).convert("RGB").save(f"../site/docs/public/info/05-computer-{k}.png", optimize=True)
print("WMOK")
