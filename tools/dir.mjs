import { chromium } from 'playwright'
const S = '/workspace/grok-bot-learn/shots/'
const b = await chromium.launch()
const p = await b.newPage({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2 })
await p.goto('https://bot.fmcat.top/', { waitUntil: 'networkidle' })
await p.waitForTimeout(3000)
const o = await p.locator('.gh-orb').boundingBox()
const c = { x: o.x - 20, y: o.y - 20, width: o.width + 40, height: o.height + 40 }
await p.screenshot({ path: S + 'v3-logo.png', clip: c })
await p.mouse.move(10, 450); await p.waitForTimeout(2000)
await p.screenshot({ path: '/tmp/l.png', clip: c })
await p.mouse.move(1430, 450); await p.waitForTimeout(2000)
await p.screenshot({ path: '/tmp/r.png', clip: c })
const n = await p.locator('.VPNavBarTitle').boundingBox()
await p.screenshot({ path: S + 'v3-logo-nav.png', clip: { x: n.x, y: n.y, width: 200, height: n.height } })
await b.close()
