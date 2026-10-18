import { defineConfig, type HeadConfig } from 'vitepress'
import side from './sidebar.json'
import seo from './seo.json'

const SITE = 'https://bot.tiezhu.si'
const NAME = 'Grok Bot 新手指南'
const HOME_TITLE = 'Grok Bot 新手指南：Grok Bot 中文教程与实战案例'
const OG_IMAGE = `${SITE}/og-share.png`
const AUTHOR = { '@type': 'Person', name: '铁柱AGI', url: 'https://x.com/cgnot996' }
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
    const graph: Record<string, unknown>[] = []
    if (isHome) {
      graph.push({
        '@type': 'WebSite',
        '@id': SITE + '/#website',
        url: SITE + '/',
        name: NAME,
        alternateName: ['Grok Bot 中文教程', 'Grok Bot 教程', 'Grok Bot 新手教程'],
        description: desc,
        inLanguage: 'zh-CN',
        publisher: AUTHOR
      })
    } else {
      const seg = rel.split('/')[0]
      const first = (side as Record<string, string[][]>)[seg]?.[0]?.[1]
      const part = names[seg] && first ? { name: names[seg], item: SITE + first } : seg === 'cases' && rel !== 'cases/index.md' ? { name: '案例库', item: SITE + '/cases/' } : null
      const crumbs = [{ name: NAME, item: SITE + '/' }, ...(part ? [part] : []), { name: pageData.title, item: url }]
      graph.push({
        '@type': 'BreadcrumbList',
        itemListElement: crumbs.map((c, i) => ({ '@type': 'ListItem', position: i + 1, name: c.name, item: c.item }))
      })
      if (seg !== 'group.md' && seg !== 'xhs.md') {
        graph.push({
          '@type': 'TechArticle',
          headline: pageData.title,
          description: desc,
          inLanguage: 'zh-CN',
          url,
          mainEntityOfPage: url,
          image: OG_IMAGE,
          author: AUTHOR,
          publisher: AUTHOR,
          isPartOf: { '@type': 'WebSite', '@id': SITE + '/#website', name: NAME, url: SITE + '/' },
          about: { '@type': 'SoftwareApplication', name: 'Grok Bot', applicationCategory: 'BusinessApplication' }
        })
      }
    }
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
      { text: '使用手册', link: '/part1/01-what-is' },
      { text: '案例篇', link: '/part2/12-content' },
      { text: '进阶篇', link: '/part3/19-orchestration' },
      { text: '落地篇', link: '/part4/23-enterprise' },
      { text: '案例库', link: '/cases/' },
      { text: '答疑群', link: '/group' }
    ],
    sidebar,
    search: { provider: 'local' },
    outline: { label: '本页', level: [2, 3] },
    docFooter: { prev: '上一章', next: '下一章' },
    returnToTopLabel: '回到顶部',
    sidebarMenuLabel: '目录'
  }
})
