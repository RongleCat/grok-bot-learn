<script setup lang="ts">
import { computed } from 'vue'
import { withBase } from 'vitepress'
import dataRoot from './tools.json'
import { useLocaleJson, useLocalePath } from './i18n'

const data = useLocaleJson(dataRoot as Record<string, unknown>, 'tools.json')
const localePath = useLocalePath()

const props = defineProps<{ id: string }>()
const skin: Record<string, string> = {
  '编码 Agent': 'cercle-bleu',
  '模型/生成': 'goutte-rose',
  '通讯与发布': 'squircle-orange',
  '数据抓取': 'nuage-turquoise',
  '基础工具': 'hexagone-ambre',
  '編碼 Agent': 'cercle-bleu',
  '資料抓取': 'nuage-turquoise',
  '通訊與釋出': 'squircle-orange',
  '基礎工具': 'hexagone-ambre',
  'Coding Agents': 'cercle-bleu',
  'Models & Generation': 'goutte-rose',
  'Communication & Publishing': 'squircle-orange',
  'Data Scraping': 'nuage-turquoise',
  'Basic Tools': 'hexagone-ambre',
  'コーディング Agent': 'cercle-bleu',
  'モデル/生成': 'goutte-rose',
  '通信・配信': 'squircle-orange',
  'データ収集': 'nuage-turquoise',
  '基本ツール': 'hexagone-ambre',
  '코딩 Agent': 'cercle-bleu',
  '모델/생성': 'goutte-rose',
  '통신 및 배포': 'squircle-orange',
  '데이터 수집': 'nuage-turquoise',
  '기본 도구': 'hexagone-ambre',
  'Agentes de código': 'cercle-bleu',
  'Modelos/Generación': 'goutte-rose',
  'Comunicación y publicación': 'squircle-orange',
  'Extracción de datos': 'nuage-turquoise',
  'Herramientas básicas': 'hexagone-ambre',
  'Agentes de Código': 'cercle-bleu',
  'Modelos / Geração': 'goutte-rose',
  'Comunicação e Publicação': 'squircle-orange',
  'Coleta de Dados': 'nuage-turquoise',
  'Ferramentas Básicas': 'hexagone-ambre'
}
const rootCatById: Record<string, string> = Object.fromEntries((dataRoot as any).tools.map((t: any) => [t.id, t.cat as string]))
const t = computed(() => (data.value as any).tools.find((x: any) => x.id === props.id))
const skinOf = computed(() => {
  if (!t.value) return 'cercle-bleu'
  return skin[t.value.cat] || skin[rootCatById[t.value.id]] || 'cercle-bleu'
})
</script>

<template>
  <a v-if="t" class="tm" :href="localePath(`/tools/?cat=${encodeURIComponent(t.cat)}`)">
    <img :src="withBase(`/bots/${skinOf}.svg`)" alt="" width="22" height="22" />{{ t.cat }}
  </a>
</template>

<style scoped>
.tm {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  margin: 4px 0 8px;
  padding: 4px 12px 4px 6px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 999px;
  font-size: 14px;
  font-weight: 600;
  color: var(--vp-c-text-2) !important;
  text-decoration: none !important;
}
.tm:hover {
  border-color: var(--tz-c-hover-border);
}
</style>
