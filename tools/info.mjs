import { chromium } from 'playwright'
import fs from 'fs'
const d = '/workspace/grok-bot-learn/v4/info/'
fs.mkdirSync(d + 'png', { recursive: true })
const b = await chromium.launch()
const p = await b.newPage({ viewport: { width: 1200, height: 760 }, deviceScaleFactor: 2 })
for (const f of fs.readdirSync(d).filter(x => x.endsWith('.html') && (process.argv.length < 3 || process.argv.includes(x)))) {
  await p.goto('file://' + d + f); await p.waitForTimeout(400)
  const o = await p.evaluate(() => [document.documentElement.scrollWidth, document.documentElement.scrollHeight, [...document.querySelectorAll('body *')].filter(e => e.children.length === 0 && (e.scrollWidth > e.clientWidth + 2 || e.scrollHeight > e.clientHeight + 2) && getComputedStyle(e).overflow !== 'visible').length])
  await p.screenshot({ path: d + 'png/' + f.replace('.html', '.png') })
  console.log(f, o.join(' '))
}
await b.close()
