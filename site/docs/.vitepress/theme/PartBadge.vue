<script setup lang="ts">
import { computed } from 'vue'
import { useRoute } from 'vitepress'
import GrokOrb from './GrokOrb.vue'

const skins: Record<string, { shape: string; color: string; label: string }> = {
  part1: { shape: 'squircle', color: 'bleu', label: '第一篇 · 使用手册' },
  part2: { shape: 'nuage', color: 'orange', label: '第二篇 · 案例篇' },
  part3: { shape: 'hexagone', color: 'vert', label: '第三篇 · 进阶篇' },
  part4: { shape: 'triangle', color: 'violet', label: '第四篇 · 落地篇' },
  cases: { shape: 'galet', color: 'rose', label: '案例库' }
}
const route = useRoute()
const skin = computed(() => skins[route.path.split('/').filter(Boolean)[0] ?? ''])
</script>

<template>
  <div v-if="skin" :key="route.path" class="part-badge">
    <GrokOrb :size="34" :shape="skin.shape" :color="skin.color" />
    <span>{{ skin.label }}</span>
  </div>
</template>
