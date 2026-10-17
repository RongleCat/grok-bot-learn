import { defineConfig } from 'vitepress'
import side from './sidebar.json'

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
  title: 'Grok Bot 学习站',
  description: 'Grok Bot 从 0 到 1 中文教程',
  appearance: false,
  head: [
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/favicon-light.svg', media: '(prefers-color-scheme: light)' }],
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/favicon-dark.svg', media: '(prefers-color-scheme: dark)' }],
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/favicon.svg' }],
    ['link', { rel: 'apple-touch-icon', href: '/apple-touch-icon.png' }],
    ['meta', { property: 'og:image', content: '/og.png' }]
  ],
  themeConfig: {
    nav: [
      { text: '使用手册', link: '/part1/01-what-is' },
      { text: '案例篇', link: '/part2/12-content' },
      { text: '进阶篇', link: '/part3/19-orchestration' },
      { text: '落地篇', link: '/part4/23-enterprise' },
      { text: '案例库', link: '/cases/' }
    ],
    sidebar,
    search: { provider: 'local' },
    outline: { label: '本页', level: [2, 3] },
    docFooter: { prev: '上一章', next: '下一章' },
    returnToTopLabel: '回到顶部',
    sidebarMenuLabel: '目录'
  }
})
