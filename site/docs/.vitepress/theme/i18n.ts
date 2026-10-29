// 多语言 JSON：theme/locales/<locale>/<filename>.json 整文件覆盖 root；缺译回退 zh-CN
import { computed, type ComputedRef } from 'vue'
import { useData, withBase } from 'vitepress'

const modules: Record<string, unknown> = import.meta.glob('./locales/*/*.json', { eager: true, import: 'default' })
export const NON_ROOT = ['zh-Hant', 'en', 'ja', 'ko', 'es', 'pt-BR'] as const

const BCP47: Record<string, string> = {
  'zh-CN': 'zh-CN',
  'zh-Hant': 'zh-TW',
  en: 'en-US',
  ja: 'ja-JP',
  ko: 'ko-KR',
  es: 'es-ES',
  'pt-BR': 'pt-BR'
}

export function useLocaleJson<T extends Record<string, unknown>>(rootData: T, filename: string): ComputedRef<T> {
  const { page } = useData()
  return computed(() => {
    const seg = page.value.relativePath.split('/')[0]
    if (!NON_ROOT.includes(seg as (typeof NON_ROOT)[number])) return rootData
    const m = modules[`./locales/${seg}/${filename}`] as T | undefined
    return m ?? rootData
  })
}

export function localeSeg(relativePath: string): string {
  const seg = relativePath.split('/')[0]
  return (NON_ROOT as readonly string[]).includes(seg) ? seg : 'zh-CN'
}

/** 当前页语种（zh-CN / en / …） */
export function useLocaleSeg(): ComputedRef<string> {
  const { page } = useData()
  return computed(() => localeSeg(page.value.relativePath))
}

/**
 * 内部链接加语种前缀：zh-CN 根站无前缀；其他 → /en/group 等。
 * 返回的函数已包 withBase。
 */
export function useLocalePath(): (path: string) => string {
  const { page } = useData()
  return (path: string) => {
    const seg = page.value.relativePath.split('/')[0]
    const p = path.startsWith('/') ? path : `/${path}`
    if ((NON_ROOT as readonly string[]).includes(seg)) return withBase(`/${seg}${p}`)
    return withBase(p)
  }
}

/** 去掉路径上的语种前缀，便于查 root 路径 key（如 /en/part1/x → /part1/x） */
export function stripLocalePrefix(path: string): string {
  let p = path.replace(/\.html$/, '')
  if (p.length > 1 && p.endsWith('/')) p = p.slice(0, -1)
  const parts = p.split('/').filter(Boolean)
  if (parts.length && (NON_ROOT as readonly string[]).includes(parts[0])) {
    const rest = parts.slice(1).join('/')
    return rest ? `/${rest}` : '/'
  }
  return p || '/'
}

/** 篇章段：路由第一段或第二段（跳过 locale） */
export function partKeyFromPath(path: string): string {
  const parts = path.split('/').filter(Boolean)
  if (!parts.length) return ''
  if ((NON_ROOT as readonly string[]).includes(parts[0])) return parts[1] ?? ''
  return parts[0]
}

export function bcp47(seg: string): string {
  return BCP47[seg] || 'zh-CN'
}
