<script setup lang="ts">
import { computed } from 'vue'
import { useRoute } from 'vitepress'
import copyRoot from './funnel.json'
import { useLocaleJson, useLocalePath, stripLocalePrefix } from './i18n'

const copy = useLocaleJson(copyRoot as Record<string, unknown>, 'funnel.json')
const localePath = useLocalePath()
const route = useRoute()
const path = computed(() => stripLocalePrefix(route.path))
const show = computed(() => /^\/(part[1-4]|cases)(\/|$)/.test(path.value))
const text = computed(() => ((copy.value as any).doc_end as Record<string, string>)[path.value] || (copy.value as any).doc_end_generic)
</script>

<template>
  <div v-if="show" :key="path" class="tz-docend" data-from="doc-end">
    <p>{{ text }}</p>
    <a :href="localePath('/group')">{{ copy.doc_end_btn }} →</a>
  </div>
</template>
