import { chromium } from 'playwright'
const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1440, height: 900 } })
await p.goto('http://127.0.0.1:5173/', { waitUntil: 'networkidle' })
for (const [x, y] of [[20, 450], [1420, 450], [720, 20], [720, 880]]) {
  await p.mouse.move(x, y); await p.waitForTimeout(1800)
  console.log(x, y, await p.evaluate(() => [...document.querySelectorAll('.gh-orb mask path')].slice(1).map(e => e.getAttribute('transform')).join(' | ')))
}
await b.close()
