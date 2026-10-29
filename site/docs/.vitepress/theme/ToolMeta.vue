<script setup lang="ts">
import { computed } from 'vue'
import { withBase } from 'vitepress'
import dataRoot from './tools.json'
import { useLocaleJson } from './i18n'
const data = useLocaleJson(dataRoot as Record<string, unknown>, 'tools.json')

const props = defineProps<{ id: string }>()
const skin: Record<string, string> = { '编码 Agent': 'cercle-bleu', '模型/生成': 'goutte-rose', '通讯与发布': 'squircle-orange', '数据抓取': 'nuage-turquoise', '基础工具': 'hexagone-ambre' }
const t = computed(() => (data.value as any).tools.find((x: any) => x.id === props.id))
</script>

<template>
  <a v-if="t" class="tm" :href="withBase(`/tools/?cat=${encodeURIComponent(t.cat)}`)">
    <img :src="withBase(`/bots/${skin[t.cat]}.svg`)" alt="" width="22" height="22" />{{ t.cat }}
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
