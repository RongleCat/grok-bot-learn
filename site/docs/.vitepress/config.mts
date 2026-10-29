import { defineConfig, type HeadConfig } from 'vitepress'
import { execFileSync } from 'node:child_process'
import { readFileSync, writeFileSync, mkdirSync, existsSync } from 'node:fs'
import { dirname, join, resolve } from 'node:path'
import bots from './theme/bots.json'
import eco from './theme/ecosystem.json'
import changelog from './theme/changelog.json'
import tools from './theme/tools.json'
import side from './sidebar.json'
import sideZhHant from './sidebar.zh-Hant.json'
import sideEn from './sidebar.en.json'
import sideJa from './sidebar.ja.json'
import sideKo from './sidebar.ko.json'
import sideEs from './sidebar.es.json'
import sidePtBR from './sidebar.pt-BR.json'
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

// 多语言路径前缀与 meta 映射
const I18N_KEYS = ['zh-CN', 'zh-Hant', 'en', 'ja', 'ko', 'es', 'pt-BR'] as const
const I18N_PREFIX: Record<string, string> = { 'zh-CN': '', 'zh-Hant': '/zh-Hant', en: '/en', ja: '/ja', ko: '/ko', es: '/es', 'pt-BR': '/pt-BR' }
const I18N_OG: Record<string, string> = { 'zh-CN': 'zh_CN', 'zh-Hant': 'zh_TW', en: 'en_US', ja: 'ja_JP', ko: 'ko_KR', es: 'es_ES', 'pt-BR': 'pt_BR' }
const I18N_HL: Record<string, string> = { 'zh-CN': 'zh-Hans', 'zh-Hant': 'zh-Hant', en: 'en', ja: 'ja', ko: 'ko', es: 'es', 'pt-BR': 'pt-BR' }
function pageLocale(rel: string) {
  const s = rel.split('/')[0]
  return ['zh-Hant', 'en', 'ja', 'ko', 'es', 'pt-BR'].includes(s) ? s : 'zh-CN'
}
function stripPrefix(rel: string) {
  const loc = pageLocale(rel)
  return loc === 'zh-CN' ? rel : rel.slice(loc.length + 1)
}

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

const namesZhHant: Record<string, string> = {
  part1: '第一篇 · 使用手冊',
  part2: '第二篇 · 案例篇',
  part3: '第三篇 · 進階篇',
  part4: '第四篇 · 落地篇'
}

const sidebarZhHant = [
  ...Object.entries(namesZhHant)
    .filter(([k]) => (sideZhHant as Record<string, string[][]>)[k])
    .map(([k, text]) => ({ text, collapsed: false, items: (sideZhHant as Record<string, string[][]>)[k].map(([t, link]) => ({ text: t, link })) })),
  { text: '案例庫', items: [{ text: '全部案例', link: '/zh-Hant/cases/' }, ...((sideZhHant as Record<string, string[][]>).cases || []).map(([t, link]) => ({ text: t, link }))] }
]


const namesEn: Record<string, string> = {
  part1: 'Part 1 · Manual',
  part2: 'Part 2 · Cases',
  part3: 'Part 3 · Advanced',
  part4: 'Part 4 · Team'
}
const sidebarEn = [
  ...Object.entries(namesEn)
    .filter(([k]) => (sideEn as Record<string, string[][]>)[k])
    .map(([k, text]) => ({ text, collapsed: false, items: (sideEn as Record<string, string[][]>)[k].map(([t, link]) => ({ text: t, link })) })),
  { text: 'Case Library', items: [{ text: 'All cases', link: '/en/cases/' }, ...((sideEn as Record<string, string[][]>).cases || []).map(([t, link]) => ({ text: t, link }))] }
]

const namesJa: Record<string, string> = {
  part1: '第1部 · マニュアル',
  part2: '第2部 · 事例',
  part3: '第3部 · 応用',
  part4: '第4部 · チーム'
}
const sidebarJa = [
  ...Object.entries(namesJa)
    .filter(([k]) => (sideJa as Record<string, string[][]>)[k])
    .map(([k, text]) => ({ text, collapsed: false, items: (sideJa as Record<string, string[][]>)[k].map(([t, link]) => ({ text: t, link })) })),
  { text: '事例ライブラリ', items: [{ text: 'すべての事例', link: '/ja/cases/' }, ...((sideJa as Record<string, string[][]>).cases || []).map(([t, link]) => ({ text: t, link }))] }
]

const namesKo: Record<string, string> = {
  part1: '제1부 · 매뉴얼',
  part2: '제2부 · 사례',
  part3: '제3부 · 심화',
  part4: '제4부 · 팀'
}
const sidebarKo = [
  ...Object.entries(namesKo)
    .filter(([k]) => (sideKo as Record<string, string[][]>)[k])
    .map(([k, text]) => ({ text, collapsed: false, items: (sideKo as Record<string, string[][]>)[k].map(([t, link]) => ({ text: t, link })) })),
  { text: '사례 라이브러리', items: [{ text: '전체 사례', link: '/ko/cases/' }, ...((sideKo as Record<string, string[][]>).cases || []).map(([t, link]) => ({ text: t, link }))] }
]

const namesEs: Record<string, string> = {
  part1: 'Parte 1 · Manual',
  part2: 'Parte 2 · Casos',
  part3: 'Parte 3 · Avanzado',
  part4: 'Parte 4 · Equipo'
}
const sidebarEs = [
  ...Object.entries(namesEs)
    .filter(([k]) => (sideEs as Record<string, string[][]>)[k])
    .map(([k, text]) => ({ text, collapsed: false, items: (sideEs as Record<string, string[][]>)[k].map(([t, link]) => ({ text: t, link })) })),
  { text: 'Biblioteca de casos', items: [{ text: 'Todos los casos', link: '/es/cases/' }, ...((sideEs as Record<string, string[][]>).cases || []).map(([t, link]) => ({ text: t, link }))] }
]

const namesPtBR: Record<string, string> = {
  part1: 'Parte 1 · Manual',
  part2: 'Parte 2 · Casos',
  part3: 'Parte 3 · Avançado',
  part4: 'Parte 4 · Equipe'
}
const sidebarPtBR = [
  ...Object.entries(namesPtBR)
    .filter(([k]) => (sidePtBR as Record<string, string[][]>)[k])
    .map(([k, text]) => ({ text, collapsed: false, items: (sidePtBR as Record<string, string[][]>)[k].map(([t, link]) => ({ text: t, link })) })),
  { text: 'Biblioteca de Casos', items: [{ text: 'Todos os casos', link: '/pt-BR/cases/' }, ...((sidePtBR as Record<string, string[][]>).cases || []).map(([t, link]) => ({ text: t, link }))] }
]

export default defineConfig({
  lang: 'zh-CN',
  title: NAME,
  description: descs.home,
  appearance: true,
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
  locales: {
    root: { label: '简体中文', lang: 'zh-CN' },
    'zh-Hant': {
      label: '繁體中文', lang: 'zh-Hant', link: '/zh-Hant/',
      title: 'Grok Bot 新手指南',
      description: '由社區整理的非官方 Grok Bot 中文教程與實戰案例庫。',
      themeConfig: {
        nav: [
          {
            text: '教程',
            activeMatch: '^/zh-Hant/part[1-4]',
            items: [
              { text: '使用手冊', link: '/zh-Hant/part1/01-what-is', activeMatch: '^/zh-Hant/part1/' },
              { text: '案例篇', link: '/zh-Hant/part2/12-content', activeMatch: '^/zh-Hant/part2/' },
              { text: '進階篇', link: '/zh-Hant/part3/19-orchestration', activeMatch: '^/zh-Hant/part3/' },
              { text: '落地篇', link: '/zh-Hant/part4/23-enterprise', activeMatch: '^/zh-Hant/part4/' }
            ]
          },
          { text: '案例庫', link: '/zh-Hant/cases/' },
          { text: 'Bot 直聘', link: '/zh-Hant/bots/', activeMatch: '^/zh-Hant/bots/' },
          { text: '周邊生態', link: '/zh-Hant/ecosystem/', activeMatch: '^/zh-Hant/ecosystem/' },
          { text: '工具箱', link: '/zh-Hant/tools/', activeMatch: '^/zh-Hant/tools/' },
          { text: '更新日誌', link: '/zh-Hant/changelog/', activeMatch: '^/zh-Hant/changelog/' },
          { text: '付費答疑群', link: '/zh-Hant/group' }
        ],
        sidebar: sidebarZhHant,
        outline: { label: '本頁', level: [2, 3] },
        docFooter: { prev: '上一章', next: '下一章' },
        darkModeSwitchLabel: '外觀', lightModeSwitchTitle: '切換到淺色', darkModeSwitchTitle: '切換到深色',
        returnToTopLabel: '回到頂部', sidebarMenuLabel: '目錄',
        lastUpdated: { text: '最後更新' }
      }
    },
    en: {
      label: 'English', lang: 'en-US', link: '/en/',
      title: 'Grok Bot Beginner\'s Guide',
      description: 'An unofficial community-maintained Grok Bot tutorial and practical case library.',
      themeConfig: {
        nav: [
          {
            text: 'Guide',
            activeMatch: '^/en/part[1-4]',
            items: [
              { text: 'Manual', link: '/en/part1/01-what-is', activeMatch: '^/en/part1/' },
              { text: 'Cases', link: '/en/part2/12-content', activeMatch: '^/en/part2/' },
              { text: 'Advanced', link: '/en/part3/19-orchestration', activeMatch: '^/en/part3/' },
              { text: 'Team', link: '/en/part4/23-enterprise', activeMatch: '^/en/part4/' }
            ]
          },
          { text: 'Case Library', link: '/en/cases/' },
          { text: 'Bot Direct Hire', link: '/en/bots/', activeMatch: '^/en/bots/' },
          { text: 'Ecosystem', link: '/en/ecosystem/', activeMatch: '^/en/ecosystem/' },
          { text: 'Toolbox', link: '/en/tools/', activeMatch: '^/en/tools/' },
          { text: 'Changelog', link: '/en/changelog/', activeMatch: '^/en/changelog/' },
          { text: 'Paid Q&A Group', link: '/en/group' }
        ],
        sidebar: sidebarEn,
        outline: { label: 'On this page', level: [2, 3] },
        docFooter: { prev: 'Previous', next: 'Next' },
        darkModeSwitchLabel: 'Appearance', lightModeSwitchTitle: 'Switch to light theme', darkModeSwitchTitle: 'Switch to dark theme',
        returnToTopLabel: 'Back to top', sidebarMenuLabel: 'Menu',
        lastUpdated: { text: 'Last updated' }
      }
    },
    ja: {
      label: '日本語', lang: 'ja', link: '/ja/',
      title: 'Grok Bot 初心者ガイド',
      description: 'コミュニティが管理する非公式 Grok Bot チュートリアルと実践事例集。',
      themeConfig: {
        nav: [
          {
            text: 'ガイド',
            activeMatch: '^/ja/part[1-4]',
            items: [
              { text: 'マニュアル', link: '/ja/part1/01-what-is', activeMatch: '^/ja/part1/' },
              { text: '事例', link: '/ja/part2/12-content', activeMatch: '^/ja/part2/' },
              { text: '応用', link: '/ja/part3/19-orchestration', activeMatch: '^/ja/part3/' },
              { text: 'チーム', link: '/ja/part4/23-enterprise', activeMatch: '^/ja/part4/' }
            ]
          },
          { text: '事例ライブラリ', link: '/ja/cases/' },
          { text: 'Bot ダイレクト採用', link: '/ja/bots/', activeMatch: '^/ja/bots/' },
          { text: '周辺エコシステム', link: '/ja/ecosystem/', activeMatch: '^/ja/ecosystem/' },
          { text: 'Grok クラウドPCツールボックス', link: '/ja/tools/', activeMatch: '^/ja/tools/' },
          { text: '更新履歴', link: '/ja/changelog/', activeMatch: '^/ja/changelog/' },
          { text: '有料Q&Aグループ', link: '/ja/group' }
        ],
        sidebar: sidebarJa,
        outline: { label: 'このページ', level: [2, 3] },
        docFooter: { prev: '前章', next: '次章' },
        darkModeSwitchLabel: '外観', lightModeSwitchTitle: 'ライトモードに切替', darkModeSwitchTitle: 'ダークモードに切替',
        returnToTopLabel: 'トップに戻る', sidebarMenuLabel: 'メニュー',
        lastUpdated: { text: '最終更新' }
      }
    },
    ko: {
      label: '한국어', lang: 'ko', link: '/ko/',
      title: 'Grok Bot 초보자 가이드',
      description: '커뮤니티에서 관리하는 비공식 Grok Bot 튜토리얼 및 실전 사례 모음.',
      themeConfig: {
        nav: [
          {
            text: '가이드',
            activeMatch: '^/ko/part[1-4]',
            items: [
              { text: '매뉴얼', link: '/ko/part1/01-what-is', activeMatch: '^/ko/part1/' },
              { text: '사례', link: '/ko/part2/12-content', activeMatch: '^/ko/part2/' },
              { text: '심화', link: '/ko/part3/19-orchestration', activeMatch: '^/ko/part3/' },
              { text: '팀', link: '/ko/part4/23-enterprise', activeMatch: '^/ko/part4/' }
            ]
          },
          { text: '사례 라이브러리', link: '/ko/cases/' },
          { text: 'Bot 채용', link: '/ko/bots/', activeMatch: '^/ko/bots/' },
          { text: '주변 생태계', link: '/ko/ecosystem/', activeMatch: '^/ko/ecosystem/' },
          { text: 'Grok 클라우드 PC 툴박스', link: '/ko/tools/', activeMatch: '^/ko/tools/' },
          { text: '변경 내역', link: '/ko/changelog/', activeMatch: '^/ko/changelog/' },
          { text: '유료 Q&A 그룹', link: '/ko/group' }
        ],
        sidebar: sidebarKo,
        outline: { label: '이 페이지', level: [2, 3] },
        docFooter: { prev: '이전', next: '다음' },
        darkModeSwitchLabel: '테마', lightModeSwitchTitle: '라이트 모드로 전환', darkModeSwitchTitle: '다크 모드로 전환',
        returnToTopLabel: '맨 위로', sidebarMenuLabel: '메뉴',
        lastUpdated: { text: '마지막 업데이트' }
      }
    },
    es: {
      label: 'Español', lang: 'es', link: '/es/',
      title: 'Guía para principiantes de Grok Bot',
      description: 'Tutorial no oficial de Grok Bot mantenido por la comunidad, con casos prácticos.',
      themeConfig: {
        nav: [
          {
            text: 'Guía',
            activeMatch: '^/es/part[1-4]',
            items: [
              { text: 'Manual', link: '/es/part1/01-what-is', activeMatch: '^/es/part1/' },
              { text: 'Casos', link: '/es/part2/12-content', activeMatch: '^/es/part2/' },
              { text: 'Avanzado', link: '/es/part3/19-orchestration', activeMatch: '^/es/part3/' },
              { text: 'Equipo', link: '/es/part4/23-enterprise', activeMatch: '^/es/part4/' }
            ]
          },
          { text: 'Biblioteca de casos', link: '/es/cases/' },
          { text: 'Contratación directa de bots', link: '/es/bots/', activeMatch: '^/es/bots/' },
          { text: 'Ecosistema periférico', link: '/es/ecosystem/', activeMatch: '^/es/ecosystem/' },
          { text: 'Herramientas', link: '/es/tools/', activeMatch: '^/es/tools/' },
          { text: 'Registro de cambios', link: '/es/changelog/', activeMatch: '^/es/changelog/' },
          { text: 'Grupo de consultas de pago', link: '/es/group' }
        ],
        sidebar: sidebarEs,
        outline: { label: 'En esta página', level: [2, 3] },
        docFooter: { prev: 'Anterior', next: 'Siguiente' },
        darkModeSwitchLabel: 'Apariencia', lightModeSwitchTitle: 'Cambiar a modo claro', darkModeSwitchTitle: 'Cambiar a modo oscuro',
        returnToTopLabel: 'Volver arriba', sidebarMenuLabel: 'Menú',
        lastUpdated: { text: 'Última actualización' }
      }
    },
    'pt-BR': {
      label: 'Português (Brasil)', lang: 'pt-BR', link: '/pt-BR/',
      title: 'Guia para Iniciantes do Grok Bot',
      description: 'Tutorial não oficial do Grok Bot mantido pela comunidade, com casos práticos.',
      themeConfig: {
        nav: [
          {
            text: 'Guia',
            activeMatch: '^/pt-BR/part[1-4]',
            items: [
              { text: 'Manual', link: '/pt-BR/part1/01-what-is', activeMatch: '^/pt-BR/part1/' },
              { text: 'Casos', link: '/pt-BR/part2/12-content', activeMatch: '^/pt-BR/part2/' },
              { text: 'Avançado', link: '/pt-BR/part3/19-orchestration', activeMatch: '^/pt-BR/part3/' },
              { text: 'Equipe', link: '/pt-BR/part4/23-enterprise', activeMatch: '^/pt-BR/part4/' }
            ]
          },
          { text: 'Biblioteca de Casos', link: '/pt-BR/cases/' },
          { text: 'Contratação Direta de Bots', link: '/pt-BR/bots/', activeMatch: '^/pt-BR/bots/' },
          { text: 'Ecossistema ao redor', link: '/pt-BR/ecosystem/', activeMatch: '^/pt-BR/ecosystem/' },
          { text: 'Ferramentas', link: '/pt-BR/tools/', activeMatch: '^/pt-BR/tools/' },
          { text: 'Registro de Alterações', link: '/pt-BR/changelog/', activeMatch: '^/pt-BR/changelog/' },
          { text: 'Grupo Pago de Dúvidas', link: '/pt-BR/group' }
        ],
        sidebar: sidebarPtBR,
        outline: { label: 'Nesta página', level: [2, 3] },
        docFooter: { prev: 'Anterior', next: 'Próximo' },
        darkModeSwitchLabel: 'Aparência', lightModeSwitchTitle: 'Mudar para tema claro', darkModeSwitchTitle: 'Mudar para tema escuro',
        returnToTopLabel: 'Voltar ao topo', sidebarMenuLabel: 'Menu',
        lastUpdated: { text: 'Última atualização' }
      }
    }
  },
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
    L.push('## 周边生态', '', `- [周边生态](${SITE}/ecosystem/): ${descs['ecosystem/index.md'] || (eco as any).index.lead}`, `- [Grok Bot Clipper 浏览器插件](${SITE}/ecosystem/grok-bot-clipper): ${descs['ecosystem/grok-bot-clipper.md'] || (eco as any).clipper.lead}`, `- [小铁柱](${SITE}/ecosystem/xiaotiezhu): ${descs['ecosystem/xiaotiezhu.md'] || (eco as any).xiaotiezhu.lead}`, '')
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
    const locale = pageLocale(rel)
    const path = pathOf(rel)
    const url = SITE + path
    const isHome = rel === 'index.md'
    const title = isHome ? HOME_TITLE : `${pageData.title} | ${NAME}`
    const desc = pageData.description || descs.home
    const head: HeadConfig[] = [
      ['link', { rel: 'canonical', href: url }],
      ['meta', { property: 'og:type', content: isHome ? 'website' : 'article' }],
      ['meta', { property: 'og:site_name', content: NAME }],
      ['meta', { property: 'og:locale', content: I18N_OG[locale] }],
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
      } else if (rel === 'ecosystem/xiaotiezhu.md') {
        const x = (eco as any).xiaotiezhu
        graph.push(page('WebPage', { mainEntity: { '@id': url + '#service' } }))
        graph.push({
          '@type': 'Service',
          '@id': url + '#service',
          name: '小铁柱',
          description: desc,
          url,
          provider: AUTHOR,
          areaServed: 'CN',
          serviceType: '微信群运维助手',
          image: `${SITE}/ecosystem/xiaotiezhu-banner.webp`,
          offers: x.plans.map((p: { name: string; price: string; unit: string; note: string }) => ({
            '@type': 'Offer',
            name: p.name,
            description: p.note,
            price: p.price,
            priceCurrency: 'CNY',
            unitText: p.unit
          }))
        })
      } else if (rel === 'ecosystem/index.md') {
        graph.push(page('CollectionPage', {
          mainEntity: {
            '@type': 'ItemList',
            itemListElement: (eco as any).index.items.map((it: { name: string; desc: string }, i: number) => ({ '@type': 'ListItem', position: i + 1, name: it.name, description: it.desc, url: SITE + ((eco as any).index.pages?.[i] || '/ecosystem/grok-bot-clipper') }))
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
    // 多语言 hreflang 与 og:locale:alternate
    const rootRel = stripPrefix(rel)
    const rootPath = pathOf(rootRel)
    for (const loc of I18N_KEYS) {
      head.push(['link', { rel: 'alternate', hreflang: I18N_HL[loc], href: SITE + I18N_PREFIX[loc] + rootPath }])
      if (loc !== locale) head.push(['meta', { property: 'og:locale:alternate', content: I18N_OG[loc] }])
    }
    head.push(['link', { rel: 'alternate', hreflang: 'x-default', href: SITE + rootPath }])
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
    darkModeSwitchLabel: '外观',
    lightModeSwitchTitle: '切换到浅色',
    darkModeSwitchTitle: '切换到深色',
    search: { provider: 'local' },
    outline: { label: '本页', level: [2, 3] },
    docFooter: { prev: '上一章', next: '下一章' },
    returnToTopLabel: '回到顶部',
    lastUpdated: { text: '最后更新', formatOptions: { dateStyle: 'medium', forceLocale: true } },
    sidebarMenuLabel: '目录'
  }
})
