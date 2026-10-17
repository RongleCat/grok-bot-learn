import { chromium } from 'playwright'
import fs from 'fs'
const names = ['cercle-bleu','galet-rouge','squircle-orange','capsule-vert','triangle-violet','hexagone-ambre','nuage-turquoise','goutte-rose','squircle-brun','galet-encre']
const out = '/workspace/grok-bot-learn/site/docs/public/bots/'
const b = await chromium.launch()
const p = await b.newPage({ viewport: { width: 1400, height: 1000 } })
await p.goto('http://localhost:5199/zz-bots.html'); await p.waitForTimeout(2500); await p.addStyleTag({ content: '*{background:transparent !important}' })
const els = await p.$$('#bots svg')
for (let i = 0; i < els.length; i++) {
  let s = await els[i].evaluate(e => { const c = e.cloneNode(true); c.setAttribute('xmlns','http://www.w3.org/2000/svg'); c.removeAttribute('class'); c.removeAttribute('role'); c.removeAttribute('aria-label'); return c.outerHTML })
  s = s.replace(/<!--.*?-->/gs, '')
  fs.writeFileSync(out + names[i] + '.svg', s)
  await els[i].screenshot({ path: out + names[i] + '.png', omitBackground: true })
}
await p.setContent('<body style="margin:0;background:#fff;display:flex;flex-wrap:wrap;width:1300px;padding:20px;gap:20px;font:16px sans-serif">' + names.map(n => `<div style="text-align:center"><img src="http://localhost:5199/bots/${n}.png" width=220><div>${n}</div></div>`).join('') + '</body>')
await b.close()
console.log(els.length)
