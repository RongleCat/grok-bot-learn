<script setup lang="ts">
import { computed } from 'vue'
import { useRoute } from 'vitepress'
import GrokOrb from './GrokOrb.vue'
import uiRoot from './ui.json'
import { useLocaleJson, partKeyFromPath } from './i18n'

const skins: Record<string, { shape: string; color: string }> = {
  part1: { shape: 'squircle', color: 'bleu' },
  part2: { shape: 'nuage', color: 'orange' },
  part3: { shape: 'hexagone', color: 'vert' },
  part4: { shape: 'triangle', color: 'violet' },
  cases: { shape: 'galet', color: 'rose' }
}
const route = useRoute()
const ui = useLocaleJson(uiRoot as Record<string, unknown>, 'ui.json')
const skin = computed(() => {
  const key = partKeyFromPath(route.path)
  const meta = skins[key]
  if (!meta) return null
  const label = ((ui.value as any).parts?.[key] as string) || key
  return { ...meta, label }
})
</script>

<template>
  <div v-if="skin" :key="route.path" class="part-badge">
    <GrokOrb :size="34" :shape="skin.shape" :color="skin.color" />
    <span>{{ skin.label }}</span>
  </div>
</template>
