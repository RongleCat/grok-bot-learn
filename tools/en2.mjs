import { chromium } from 'playwright'
const b = await chromium.launch()
const p = await b.newPage({ viewport: { width: 1440, height: 900 } })
await p.goto('https://bot.tiezhu.si/cases/en2', { waitUntil: 'networkidle' })
await p.waitForTimeout(1500)
await p.screenshot({ path: '/workspace/grok-bot-learn/shots/v3-cases-en2.png' })
await b.close()
