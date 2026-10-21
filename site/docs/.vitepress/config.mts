import { defineConfig, type HeadConfig } from 'vitepress'
import { execFileSync } from 'node:child_process'
import { readFileSync, writeFileSync, mkdirSync, existsSync } from 'node:fs'
import { dirname, join, resolve } from 'node:path'
import bots from './theme/bots.json'
import eco from './theme/ecosystem.json'
import changelog from './theme/changelog.json'
import tools from './theme/tools.json'
import side from './sidebar.json'
import seo from './seo.json'

const SITE = 'https://bot.fmcat.top'
const NAME = 'Grok Bot 新手指南'
const HOME_TITLE = 'Grok Bot 新手指南：Grok Bot 中文教程与实战案例'
const OG_IMAGE = `${SITE}/og-share.png`
const AUTHOR_ID = SITE + '/#author'
const SITE_ID = SITE + '/#website'
const PERSON = { '@type': 'Person', '@id': AUTHOR_ID, name: '铁柱AGI', url: SITE + '/about', sameAs: ['https://x.com/cgnot996', 'https://github.com/RongleCat'], knowsAbout: ['Grok Bot', 'AI Agent'] }
const AUTHOR = { '@id': AUTHOR_ID }
const DOCS = resolve(__dirname, '..')
const LLMS_NOTE = '本文件是供 AI 助手与搜索引擎读取的站点索引。本站为社区非官方教程，作者铁柱AGI，与 xAI、Cursor 无隶属关系。'
const LLMS_MD = '各章节与案例页网址后加 .md 即为 Markdown 版本，全站正文合集在 /llms-full.txt。'
const LLMS_FULL = '本文件收录全站教程与案例的 Markdown 正文，每篇前标有原文网址，引用时请链接原文网址。'
const dateCache: Record<string, { published?: string; modified?: string }> = {}
function gitDates(file: string) {
  if (dateCache[file]) return dateCache[file]
  let out = ''
  try {
    out = execFileSync('git', ['log', '--follow', '--format=%cI', '--', file], { cwd: DOCS, encoding: 'utf8' }).trim()
  } catch {}
  const all = out.split('\n').filter(Boolean)
  return (dateCache[file] = { published: all[all.length - 1], modified: all[0] })
}
function isDoc(rel: string) {
  return /^part[1-4]\//.test(rel) || (/^cases\//.test(rel) && rel !== 'cases/index.md') || (/^tools\//.test(rel) && rel !== 'tools/index.md')
}
function mdTitle(rel: string) {
  const src = readFileSync(join(DOCS, rel), 'utf8')
  const fm = /^---\n[\s\S]*?\ntitle:\s*(.+)\n[\s\S]*?---/.exec(src)
  const h1 = /^#\s+(.+)$/m.exec(src.replace(/^---\n[\s\S]*?\n---\n/, ''))
  return (h1 ? h1[1] : fm ? fm[1] : rel).trim()
}
function mdBody(rel: string) {
  return readFileSync(join(DOCS, rel), 'utf8')
    .replace(/^---\n[\s\S]*?\n---\n/, '')
    .replace(/\]\((\/[^)\s]*)\)/g, (_, u) => `](${SITE}${u})`)
    .replace(/(src|href)="(\/[^"]*)"/g, (_, a, u) => `${a}="${SITE}${u}"`)
    .trim()
}
function xhotItems() {
  const src = readFileSync(join(DOCS, 'cases/x-hot.md'), 'utf8')
  const out: { name: string; url: string }[] = []
  const re = /^###\s+(.+)\n+>\s*原帖：\[[^\]]*\]\((https:\/\/x\.com\/[^)]+)\)/gm
  let m
  while ((m = re.exec(src))) out.push({ name: m[1].trim(), url: m[2] })
  return out
}
const verify: HeadConfig[] = [
  ...(process.env.GOOGLE_SITE_VERIFICATION ? [['meta', { name: 'google-site-verification', content: process.env.GOOGLE_SITE_VERIFICATION }] as HeadConfig] : []),
  ...(process.env.BAIDU_SITE_VERIFICATION ? [['meta', { name: 'baidu-site-verification', content: process.env.BAIDU_SITE_VERIFICATION }] as HeadConfig] : []),
  ...(process.env.BING_SITE_VERIFICATION ? [['meta', { name: 'msvalidate.01', content: process.env.BING_SITE_VERIFICATION }] as HeadConfig] : [])
]
const descs = seo as Record<string, string>

function pathOf(rel: string) {
  const p = '/' + rel.replace(/\.md$/, '').replace(/(^|\/)index$/, '$1')
  return p
}

const names: Record<string, string> = {
  part1: '第一篇 · 使用手册',
  part2: '第二篇 · 案例篇',
  part3: '第三篇 · 进阶篇',
  part4: '第四篇 · 落地篇'
}

const sidebar = [
  ...Object.entries(names)
    .filter(([k]) => (side as Record<string, string[][]>)[k])
    .map(([k, text]) => ({ text, collapsed: false, items: (side as Record<string, string[][]>)[k].map(([t, link]) => ({ text: t, link })) })),
  { text: '案例库', items: [{ text: '全部案例', link: '/cases/' }, ...((side as Record<string, string[][]>).cases || []).map(([t, link]) => ({ text: t, link }))] }
]

export default defineConfig({
  lang: 'zh-CN',
  title: NAME,
  description: descs.home,
  appearance: false,
  cleanUrls: true,
  markdown: {
    config(md) {
      const image = md.renderer.rules.image!
      md.renderer.rules.image = (tokens, idx, options, env, self) => {
        const t = tokens[idx]
        const src = t.attrGet('src') || ''
        if (/^\/info\/[^/]+\.png$/.test(src)) {
          t.attrSet('src', src.replace(/\.png$/, '.webp'))
          t.attrSet('width', '1600')
          t.attrSet('height', '1013')
        }
        env.imgCount = (env.imgCount || 0) + 1
        if (env.imgCount > 1) t.attrSet('loading', 'lazy')
        t.attrSet('decoding', 'async')
        return image(tokens, idx, options, env, self)
      }
    }
  },
  srcExclude: ['admin/**', 'advanced/**', 'appendix/**', 'core/**', 'guide/**', 'resources/**', 'start/**', 'zz-bots.md', 'cases/outdated.md'],
  sitemap: {
    hostname: SITE,
    transformItems: (items) => items.filter((i) => !/404/.test(i.url) && !/(^|\/)xhs$/.test(i.url)).map((i) => ({ ...i, changefreq: 'weekly', priority: i.url === '' || i.url === SITE + '/' ? 1.0 : 0.8 }))
  },
  lastUpdated: true,
  buildEnd(cfg) {
    const out = cfg.outDir
    const pages = cfg.pages.filter((r) => r !== '404.md' && r !== 'xhs.md')
    const docs = pages.filter(isDoc).sort()
    for (const rel of docs) {
      const f = join(out, pathOf(rel) + '.md')
      mkdirSync(dirname(f), { recursive: true })
      writeFileSync(f, mdBody(rel) + '\n')
    }
    const line = (rel: string, d?: string) => `- [${mdTitle(rel)}](${SITE}${pathOf(rel)})${d || descs[rel] ? ': ' + (d || descs[rel]) : ''}`
    const L: string[] = [`# ${NAME}`, '', `> ${descs.home}`, '', LLMS_NOTE, '', LLMS_MD, '']
    for (const [k, t] of Object.entries(names)) {
      const items = ((side as Record<string, string[][]>)[k] || []).map(([, link]) => link.replace(/^\//, '') + '.md').filter((r) => pages.includes(r))
      if (!items.length) continue
      L.push(`## ${t}`, '', ...items.map((r) => line(r)), '')
    }
    const cases = pages.filter((r) => r.startsWith('cases/')).sort((a, b) => (a === 'cases/index.md' ? -1 : b === 'cases/index.md' ? 1 : a.localeCompare(b)))
    L.push('## 案例库', '', ...cases.map((r) => line(r)), '')
    L.push('## Bot 直聘', '', `- [Bot 直聘](${SITE}/bots/): ${descs['bots/index.md'] || (bots as any).lead}`, ...(bots as any).bots.map((b: any) => `- [${b.name}](${b.url}): ${b.desc}`), '')
    L.push('## 周边生态', '', `- [周边生态](${SITE}/ecosystem/): ${descs['ecosystem/index.md'] || (eco as any).index.lead}`, `- [Grok Bot Clipper 浏览器插件](${SITE}/ecosystem/grok-bot-clipper): ${descs['ecosystem/grok-bot-clipper.md'] || (eco as any).clipper.lead}`, '')
    {
      const cl = changelog as any
      const tag: Record<string, string> = { pc: 'PC', ios: 'iOS', android: 'Android' }
      L.push('## 更新日志', '', `- [更新日志](${SITE}/changelog/): ${descs['changelog/index.md'] || cl.ui.lead}`, ...cl.official.slice(0, 12).map((e: any) => `- ${e.date} ${tag[e.platform]}${e.version ? ' v' + e.version : ''} [${e.title}](${e.url}): ${e.points.map((p: string) => p.replace(/。$/, '')).join('；')}`), ...cl.ours.map((t: any) => `- ${t.date} [${t.title}](${t.url}): ${t.summary}`), '')
    }
    {
      const tl = tools as any
      L.push('## ' + tl.ui.title, '', `- [${tl.ui.title}](${SITE}/tools/): ${descs['tools/index.md'] || tl.ui.lead.replace(/\*\*/g, '')}`, ...tl.tools.map((t: any) => `- [${t.name}](${SITE}/tools/${t.id}): ${descs['tools/' + t.id + '.md'] || t.desc}`), '')
    }
    L.push('## Optional', '', `- [关于铁柱AGI](${SITE}/about): ${descs['about.md'] || ''}`, `- [付费答疑群](${SITE}/group): ${descs['group.md'] || ''}`, `- [GitHub 源码](https://github.com/RongleCat/grok-bot-learn)`, `- [铁柱AGI on X](https://x.com/cgnot996)`, '')
    writeFileSync(join(out, 'llms.txt'), L.join('\n'))
    const F: string[] = [`# ${NAME}`, '', `> ${descs.home}`, '', LLMS_FULL, '', LLMS_NOTE, '']
    for (const rel of docs) {
      const d = gitDates(rel)
      F.push('---', '', `URL: ${SITE}${pathOf(rel)}`, ...(d.modified ? [`更新: ${d.modified.slice(0, 10)}`] : []), '', mdBody(rel), '')
    }
    writeFileSync(join(out, 'llms-full.txt'), F.join('\n'))
  },
  transformPageData(pageData) {
    const rel = pageData.relativePath
    const fm = pageData.frontmatter
    const d = fm.description || (rel === 'index.md' ? descs.home : descs[rel])
    if (d) pageData.description = d
    if (rel === 'index.md') {
      pageData.title = HOME_TITLE
      fm.titleTemplate = false
      pageData.titleTemplate = false
    }
  },
  transformHead({ pageData }) {
    const rel = pageData.relativePath
    if (pageData.isNotFound || rel === '404.md') return [['meta', { name: 'robots', content: 'noindex' }]]
    const path = pathOf(rel)
    const url = SITE + path
    const isHome = rel === 'index.md'
    const title = isHome ? HOME_TITLE : `${pageData.title} | ${NAME}`
    const desc = pageData.description || descs.home
    const head: HeadConfig[] = [
      ['link', { rel: 'canonical', href: url }],
      ['meta', { property: 'og:type', content: isHome ? 'website' : 'article' }],
      ['meta', { property: 'og:site_name', content: NAME }],
      ['meta', { property: 'og:locale', content: 'zh_CN' }],
      ['meta', { property: 'og:title', content: title }],
      ['meta', { property: 'og:description', content: desc }],
      ['meta', { property: 'og:url', content: url }],
      ['meta', { property: 'og:image', content: OG_IMAGE }],
      ['meta', { property: 'og:image:width', content: '1200' }],
      ['meta', { property: 'og:image:height', content: '630' }],
      ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
      ['meta', { name: 'twitter:creator', content: '@cgnot996' }],
      ['meta', { name: 'twitter:title', content: title }],
      ['meta', { name: 'twitter:description', content: desc }],
      ['meta', { name: 'twitter:image', content: OG_IMAGE }]
    ]
    const graph: Record<string, unknown>[] = [
      {
        '@type': 'WebSite',
        '@id': SITE_ID,
        url: SITE + '/',
        name: NAME,
        alternateName: ['Grok Bot 中文教程', 'Grok Bot 教程', 'Grok Bot 新手教程'],
        description: descs.home,
        inLanguage: 'zh-CN',
        publisher: AUTHOR
      },
      PERSON
    ]
    const dates = gitDates(rel)
    const page = (type: string, extra: Record<string, unknown> = {}) => ({
      '@type': type,
      '@id': url + '#webpage',
      url,
      name: isHome ? HOME_TITLE : pageData.title,
      description: desc,
      inLanguage: 'zh-CN',
      isPartOf: { '@id': SITE_ID },
      ...(dates.published ? { datePublished: dates.published, dateModified: dates.modified } : {}),
      ...extra
    })
    if (isHome) {
      graph.push(page('WebPage', { about: { '@type': 'SoftwareApplication', name: 'Grok Bot', applicationCategory: 'BusinessApplication' } }))
    } else {
      const seg = rel.split('/')[0]
      const first = (side as Record<string, string[][]>)[seg]?.[0]?.[1]
      const part = names[seg] && first ? { name: names[seg], item: SITE + first } : seg === 'cases' && rel !== 'cases/index.md' ? { name: '案例库', item: SITE + '/cases/' } : seg === 'tools' && rel !== 'tools/index.md' ? { name: (tools as any).ui.title, item: SITE + '/tools/' } : seg === 'ecosystem' && rel !== 'ecosystem/index.md' ? { name: '周边生态', item: SITE + '/ecosystem/' } : null
      const crumbs = [{ name: NAME, item: SITE + '/' }, ...(part ? [part] : []), { name: pageData.title, item: url }]
      graph.push({
        '@type': 'BreadcrumbList',
        itemListElement: crumbs.map((c, i) => ({ '@type': 'ListItem', position: i + 1, name: c.name, item: c.item }))
      })
      if (rel === 'ecosystem/grok-bot-clipper.md') {
        const c = (eco as any).clipper
        const vids = c.videos.map((v: { title: string }, i: number) => {
          const d = gitDates(`public/ecosystem/clipper-demo-${i + 1}.mp4`)
          return {
            '@type': 'VideoObject',
            name: `Grok Bot Clipper ${v.title}`,
            description: c.videoLead,
            thumbnailUrl: `${SITE}/ecosystem/clipper-demo-${i + 1}.webp`,
            contentUrl: `${SITE}/ecosystem/clipper-demo-${i + 1}.mp4`,
            duration: ['PT3M5S', 'PT39S'][i],
            inLanguage: 'zh-CN',
            creator: AUTHOR,
            ...(d.published ? { uploadDate: d.published } : {})
          }
        })
        graph.push(page('WebPage', { mainEntity: { '@id': url + '#app' }, video: vids }))
        graph.push({
          '@type': 'SoftwareApplication',
          '@id': url + '#app',
          name: 'Grok Bot Clipper',
          description: desc,
          url,
          applicationCategory: 'BrowserApplication',
          operatingSystem: 'Chrome, Edge, Firefox',
          softwareVersion: '0.4.0',
          inLanguage: 'zh-CN',
          image: `${SITE}/ecosystem/clipper-banner.webp`,
          author: AUTHOR,
          publisher: AUTHOR,
          isAccessibleForFree: true,
          offers: { '@type': 'Offer', price: '0', priceCurrency: 'USD' },
          license: 'https://opensource.org/licenses/MIT',
          sameAs: 'https://github.com/RongleCat/grok-bot-clipper'
        })
      } else if (rel === 'ecosystem/index.md') {
        graph.push(page('CollectionPage', {
          mainEntity: {
            '@type': 'ItemList',
            itemListElement: (eco as any).index.items.map((it: { name: string; desc: string }, i: number) => ({ '@type': 'ListItem', position: i + 1, name: it.name, description: it.desc, url: SITE + '/ecosystem/grok-bot-clipper' }))
          }
        }))
      } else if (rel === 'bots/index.md') {
        graph.push(page('CollectionPage', {
          mainEntity: {
            '@type': 'ItemList',
            numberOfItems: (bots as any).bots.length,
            itemListElement: (bots as any).bots.map((b: { name: string; desc: string; url: string; post?: string }, i: number) => ({
              '@type': 'ListItem',
              position: i + 1,
              item: { '@type': 'CreativeWork', name: b.name, description: b.desc, url: b.url, author: AUTHOR, ...(b.post ? { sameAs: b.post } : {}) }
            }))
          }
        }))
      } else if (rel === 'changelog/index.md') {
        const cl = changelog as any
        const tag: Record<string, string> = { pc: 'PC', ios: 'iOS', android: 'Android' }
        const all = [
          ...cl.official.map((e: any) => ({ '@type': 'CreativeWork', name: `Grok Bot ${tag[e.platform]}${e.version ? ' ' + e.version : ''}：${e.title}`, description: e.points.map((p: string) => p.replace(/。$/, '')).join('；'), datePublished: e.date, url: e.url, inLanguage: 'zh-CN' })),
          ...cl.ours.map((t: any) => ({ '@type': 'SocialMediaPosting', headline: t.title, description: t.summary, datePublished: t.date, url: t.url, author: AUTHOR }))
        ].sort((a: any, b: any) => (a.datePublished < b.datePublished ? 1 : -1))
        graph.push(page('CollectionPage', { dateModified: cl.updated, about: { '@type': 'SoftwareApplication', name: 'Grok Bot', applicationCategory: 'BusinessApplication' }, mainEntity: { '@type': 'ItemList', numberOfItems: all.length, itemListOrder: 'https://schema.org/ItemListOrderDescending', itemListElement: all.map((item, i) => ({ '@type': 'ListItem', position: i + 1, item })) } }))
      } else if (rel === 'about.md') {
        graph.push(page('ProfilePage', { mainEntity: AUTHOR }))
      } else if (rel === 'cases/index.md') {
        graph.push(page('CollectionPage'))
      } else if (isDoc(rel)) {
        graph.push(page('WebPage', { mainEntity: { '@id': url + '#article' } }))
        const art: Record<string, unknown> = {
          '@type': 'TechArticle',
          '@id': url + '#article',
          headline: pageData.title,
          description: desc,
          inLanguage: 'zh-CN',
          url,
          mainEntityOfPage: { '@id': url + '#webpage' },
          image: OG_IMAGE,
          author: AUTHOR,
          publisher: AUTHOR,
          ...(dates.published ? { datePublished: dates.published, dateModified: dates.modified } : {}),
          isPartOf: { '@id': SITE_ID },
          about: { '@type': 'SoftwareApplication', name: 'Grok Bot', applicationCategory: 'BusinessApplication' }
        }
        if (rel === 'cases/x-hot.md') {
          art.mentions = xhotItems().map((x) => ({ '@type': 'SocialMediaPosting', headline: x.name, url: x.url }))
          graph.push(art)
          graph.push({ '@type': 'ItemList', name: pageData.title, itemListElement: xhotItems().map((x, i) => ({ '@type': 'ListItem', position: i + 1, name: x.name, url: x.url })) })
        } else graph.push(art)
        head.push(['link', { rel: 'alternate', type: 'text/markdown', href: url + '.md' }])
      } else {
        graph.push(page('WebPage'))
      }
    }
    head.push(['link', { rel: 'alternate', hreflang: 'zh-CN', href: url }])
    head.push(['link', { rel: 'alternate', hreflang: 'x-default', href: url }])
    if (rel === 'xhs.md') head.unshift(['meta', { name: 'robots', content: 'noindex, follow' }])
    head.push(['script', { type: 'application/ld+json' }, JSON.stringify({ '@context': 'https://schema.org', '@graph': graph })])
    return head
  },
  head: [
    ...verify,
    ['meta', { name: 'applicable-device', content: 'pc,mobile' }],
    ['meta', { name: 'author', content: '铁柱AGI' }],
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/favicon-light.svg', media: '(prefers-color-scheme: light)' }],
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/favicon-dark.svg', media: '(prefers-color-scheme: dark)' }],
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/favicon.svg' }],
    ['link', { rel: 'apple-touch-icon', href: '/apple-touch-icon.png' }],
    ['script', { defer: '', src: '/s/a.js', 'data-website-id': '6c2386ea-c82d-468a-bfa7-9651eea59ab9', 'data-host-url': '/s' }]
  ],
  themeConfig: {
    nav: [
      {
        text: '教程',
        activeMatch: '^/part[1-4]/',
        items: [
          { text: '使用手册', link: '/part1/01-what-is', activeMatch: '^/part1/' },
          { text: '案例篇', link: '/part2/12-content', activeMatch: '^/part2/' },
          { text: '进阶篇', link: '/part3/19-orchestration', activeMatch: '^/part3/' },
          { text: '落地篇', link: '/part4/23-enterprise', activeMatch: '^/part4/' }
        ]
      },
      { text: '案例库', link: '/cases/' },
      { text: 'Bot 直聘', link: '/bots/', activeMatch: '^/bots/' },
      { text: '周边生态', link: '/ecosystem/', activeMatch: '^/ecosystem/' },
      { text: '工具箱', link: '/tools/', activeMatch: '^/tools/' },
      { text: '更新日志', link: '/changelog/', activeMatch: '^/changelog/' },
      { text: '付费答疑群', link: '/group' }
    ],
    socialLinks: [{ icon: 'github', link: 'https://github.com/RongleCat/grok-bot-learn', ariaLabel: 'GitHub' }],
    sidebar,
    search: { provider: 'local' },
    outline: { label: '本页', level: [2, 3] },
    docFooter: { prev: '上一章', next: '下一章' },
    returnToTopLabel: '回到顶部',
    lastUpdated: { text: '最后更新', formatOptions: { dateStyle: 'medium', forceLocale: true } },
    sidebarMenuLabel: '目录'
  }
})
