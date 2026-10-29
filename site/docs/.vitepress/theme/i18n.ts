// 多语言 JSON：theme/locales/<locale>/<filename>.json 整文件覆盖 root；缺译回退 zh-CN
import { computed, type ComputedRef } from 'vue'
import { useData } from 'vitepress'

const modules: Record<string, unknown> = import.meta.glob('./locales/*/*.json', { eager: true, import: 'default' })
const NON_ROOT = ['zh-Hant', 'en', 'ja', 'ko', 'es', 'pt-BR']

export function useLocaleJson<T extends Record<string, unknown>>(rootData: T, filename: string): ComputedRef<T> {
  const { page } = useData()
  return computed(() => {
    const seg = page.value.relativePath.split('/')[0]
    if (!NON_ROOT.includes(seg)) return rootData
    const m = modules[`./locales/${seg}/${filename}`] as T | undefined
    return m ?? rootData
  })
}

export function localeSeg(relativePath: string): string {
  const seg = relativePath.split('/')[0]
  return NON_ROOT.includes(seg) ? seg : 'zh-CN'
}
