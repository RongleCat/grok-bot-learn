import { readFileSync, writeFileSync, mkdirSync, readdirSync, rmSync } from 'node:fs'
import { join, dirname } from 'node:path'
import { fileURLToPath } from 'node:url'
const root = join(dirname(fileURLToPath(import.meta.url)), '..')
const data = JSON.parse(readFileSync(join(root, 'site/docs/.vitepress/theme/tools.json'), 'utf8'))
const dir = join(root, 'site/docs/tools')
mkdirSync(dir, { recursive: true })
for (const f of readdirSync(dir)) if (f.endsWith('.md')) rmSync(join(dir, f))
const u = data.ui
writeFileSync(join(dir, 'index.md'), `---\nlayout: page\nsidebar: false\ntitle: ${u.title}\n---\n\n<ToolIndex />\n`)
for (const t of data.tools) {
  const L = ['---', `title: ${t.name}`, 'sidebar: false', 'prev: false', 'next: false', '---', '', `# ${t.name}`, '', `<ToolMeta id="${t.id}" />`, '', t.intro, '']
  L.push(`## ${u.promptTitle}`, '', u.promptHint, '', '<div class="tool-prompt">', '', '````text', t.prompt.trim(), '````', '', '</div>', '')
  if (t.todo.length) L.push(`## ${u.todoTitle}`, '', ...t.todo.map((x) => `- ${x}`), '')
  L.push(`## ${u.src}`, '', ...t.src.map((s) => `- [${s.t}](${s.u})`), '', `> ${u.note}`, '', `[← ${u.back}](/tools/)`, '')
  writeFileSync(join(dir, t.id + '.md'), L.join('\n'))
}
console.log(data.tools.length)
