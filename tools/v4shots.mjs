import { chromium } from 'playwright'
const b = await chromium.launch()
const p = await b.newPage({ viewport: { width: 1280, height: 1600 } })
const go = async (u, f, sel) => { await p.goto('https://bot.tiezhu.si' + u, { waitUntil: 'networkidle' }); if (sel) await p.locator(sel).first().scrollIntoViewIfNeeded(); await p.waitForTimeout(800); await p.screenshot({ path: '../shots/' + f }) }
await go('/cases/cn', 'v4-case-page.png', 'blockquote')
await go('/part1/05-computer', 'v4-infographic-page.png', 'img[src*="/info/"]')
await go('/part1/11-safety', 'v4-split-page.png', 'h2')
await b.close()
