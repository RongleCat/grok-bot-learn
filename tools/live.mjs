import { chromium } from 'playwright'
const b = await chromium.launch()
const p = await b.newPage({ viewport: { width: 1440, height: 900 } })
await p.goto('https://tiezhu-grokbot.pages.dev/', { waitUntil: 'networkidle' })
await p.mouse.move(1200, 150)
await p.waitForTimeout(1500)
await p.screenshot({ path: '/workspace/grok-bot-learn/shots/live-pagesdev.png' })
await b.close()
