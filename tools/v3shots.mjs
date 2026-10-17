import { chromium } from 'playwright'
const S = '/workspace/grok-bot-learn/shots/'
const base = process.env.BASE || 'http://127.0.0.1:5173'
const b = await chromium.launch()
const p = await b.newPage({ viewport: { width: 1440, height: 900 } })
await p.goto(base + '/', { waitUntil: 'networkidle' })
await p.mouse.move(1300, 150)
await p.waitForTimeout(2500)
await p.screenshot({ path: S + 'v3-home.png', fullPage: true })
const p2 = await b.newPage({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 3 })
await p2.goto(base + '/', { waitUntil: 'networkidle' })
await p2.mouse.move(720, 450)
await p2.waitForTimeout(2500)
const o = await p2.locator('.gh-orb').boundingBox()
await p2.screenshot({ path: S + 'v3-logo.png', clip: { x: o.x - 40, y: o.y - 30, width: o.width + 80, height: o.height + 60 } })
for (const [u, f] of [['/part1/08-skills-routines.html', 'v3-chapter-routines.png'], [process.env.CH2 || '/part1/03-install.html', 'v3-chapter-2.png']]) {
  await p.goto(base + u, { waitUntil: 'networkidle' })
  await p.waitForTimeout(1000)
  await p.screenshot({ path: S + f })
}
await b.close()
