import { chromium } from 'playwright'
const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1440, height: 900 } })
p.on('console', m => console.log('console', m.type(), m.text()))
await p.goto('http://127.0.0.1:5173/', { waitUntil: 'networkidle' }); await p.waitForTimeout(1000)
console.log(await p.evaluate(() => { const s = document.querySelector('.gh-orb'); return s.outerHTML.slice(0, 700) }))
await b.close()
