import glob, os
from PIL import Image

root = os.path.join(os.path.dirname(__file__), '..', 'site', 'docs', 'public', 'info')
for f in sorted(glob.glob(os.path.join(root, '*.png'))):
    w = f[:-4] + '.webp'
    if os.path.exists(w) and os.path.getmtime(w) >= os.path.getmtime(f):
        continue
    im = Image.open(f).convert('RGB')
    if im.width > 1600:
        im = im.resize((1600, round(im.height * 1600 / im.width)), Image.LANCZOS)
    im.save(w, quality=82, method=6)
    print(os.path.basename(w), os.path.getsize(w) // 1024, 'KB')
