import { chromium } from 'playwright'
const S = '/workspace/grok-bot-learn/shots/'
const b = await chromium.launch()
const p = await b.newPage({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 3 })
await p.goto('http://127.0.0.1:5180/', { waitUntil: 'networkidle' })
await p.waitForTimeout(3000)
const o = await p.locator('.gh-orb').boundingBox()
await p.screenshot({ path: S + 'v3-logo-rest.png', clip: { x: o.x - 40, y: o.y - 30, width: o.width + 80, height: o.height + 60 } })
await b.close()
