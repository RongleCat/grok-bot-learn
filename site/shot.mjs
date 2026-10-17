import { chromium } from 'playwright'
const S = '/workspace/grok-bot-learn/shots/'
const b = await chromium.launch()
const p = await b.newPage({ viewport: { width: 1440, height: 900 } })
await p.goto('http://127.0.0.1:5173/', { waitUntil: 'networkidle' })
await p.mouse.move(1200, 150)
await p.waitForTimeout(1500)
await p.screenshot({ path: S + 'v2-home.png', fullPage: true })
const orb = await p.locator('.gh-orb').boundingBox()
await p.screenshot({ path: S + 'v2-logo-closeup.png', clip: { x: orb.x - 60, y: orb.y - 40, width: orb.width + 120, height: orb.height + 80 } })
const pts = [[200, 150], [1240, 150], [1240, 700], [200, 700], [720, 120], [720, 800], [200, 150]]
let n = 0
for (let k = 0; k < pts.length - 1; k++) {
  const [x0, y0] = pts[k], [x1, y1] = pts[k + 1]
  for (let s = 0; s <= 12; s++) {
    await p.mouse.move(x0 + (x1 - x0) * s / 12, y0 + (y1 - y0) * s / 12)
    await p.waitForTimeout(40)
    await p.screenshot({ path: `/tmp/gf/f${String(n++).padStart(3, '0')}.png`, clip: { x: orb.x - 260, y: orb.y - 30, width: orb.width + 520, height: orb.height + 60 } })
  }
}
await p.goto('http://127.0.0.1:5173/guide/09-routines.html', { waitUntil: 'networkidle' })
await p.waitForTimeout(800)
await p.screenshot({ path: S + 'v2-chapter.png', fullPage: true })
const m = await b.newPage({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true })
await m.goto('http://127.0.0.1:5173/', { waitUntil: 'networkidle' })
await m.waitForTimeout(800)
await m.screenshot({ path: S + 'v2-mobile-home.png', fullPage: true })
await b.close()
