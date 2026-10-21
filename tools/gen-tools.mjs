import { readFileSync, writeFileSync, mkdirSync, readdirSync, rmSync } from 'node:fs'
import { join, dirname } from 'node:path'
import { fileURLToPath } from 'node:url'
const root = join(dirname(fileURLToPath(import.meta.url)), '..')
const data = JSON.parse(readFileSync(join(root, 'site/docs/.vitepress/theme/tools.json'), 'utf8'))
const dir = join(root, 'site/docs/tools')
mkdirSync(dir, { recursive: true })
for (const f of readdirSync(dir)) if (f.endsWith('.md')) rmSync(join(dir, f))
const u = data.ui
const code = (a) => (a.length ? ['```bash', ...a, '```', ''] : [])
writeFileSync(join(dir, 'index.md'), `---\nlayout: page\nsidebar: false\ntitle: ${u.title}\n---\n\n<ToolIndex />\n`)
for (const t of data.tools) {
  const L = ['---', `title: ${t.name}`, 'sidebar: false', 'prev: false', 'next: false', '---', '', `# ${t.name}`, '', `<ToolMeta id="${t.id}" />`, '', t.what, '']
  if (t.prereq.length) L.push(`## ${u.prereq}`, '', ...t.prereq.map((x) => `- ${x}`), '')
  if (t.install.length) L.push(`## ${u.install}`, '', ...code(t.install), ...code(t.installAlt))
  L.push(`## ${u.auth}`, '', t.auth, '', ...code(t.authCmd))
  if (t.steps.length) L.push(`## ${u.steps}`, '', ...t.steps.map((x, i) => `${i + 1}. ${x}`), '')
  if (t.verify.length) L.push(`## ${u.verify}`, '', ...code(t.verify))
  if (t.pitfalls.length) L.push(`## ${u.pitfalls}`, '', ...t.pitfalls.flatMap((p) => [`### ${p.q}`, '', p.a, '']))
  L.push(`## ${u.src}`, '', ...t.src.map((s) => `- [${s.t}](${s.u})`), '', `> ${u.note}`, '', `[← ${u.back}](/tools/)`, '')
  writeFileSync(join(dir, t.id + '.md'), L.join('\n'))
}
console.log(data.tools.length)
