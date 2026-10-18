import { chromium } from 'playwright'
const S = '/workspace/grok-bot-learn/shots/'
const base = 'https://bot.fmcat.top'
const b = await chromium.launch()
const p = await b.newPage({ viewport: { width: 1440, height: 900 } })
await p.goto(base + '/', { waitUntil: 'networkidle' })
await p.waitForTimeout(3000)
await p.screenshot({ path: S + 'v3-home.png', fullPage: true })
const p2 = await b.newPage({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 3 })
await p2.goto(base + '/', { waitUntil: 'networkidle' })
await p2.waitForTimeout(3000)
const o = await p2.locator('.gh-orb').boundingBox()
await p2.screenshot({ path: S + 'v3-logo.png', clip: { x: o.x - 40, y: o.y - 30, width: o.width + 80, height: o.height + 60 } })
for (const [u, f] of [['/part1/04-handoff', 'v3-chapter-handoff.png'], ['/part3/21-backup', 'v3-chapter-backup.png'], ['/cases/', 'v3-cases.png'], ['/cases/tiezhu', 'v3-cases-tiezhu.png']]) {
  await p.goto(base + u, { waitUntil: 'networkidle' })
  await p.waitForTimeout(1500)
  await p.screenshot({ path: S + f })
}
await b.close()
