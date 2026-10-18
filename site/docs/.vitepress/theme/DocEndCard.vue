<script setup lang="ts">
import { computed } from 'vue'
import { useRoute, withBase } from 'vitepress'
import copy from './funnel.json'

const route = useRoute()
const path = computed(() => route.path.replace(/\.html$/, '').replace(/\/$/, '') || '/')
const show = computed(() => /^\/(part[1-4]|cases)(\/|$)/.test(path.value))
const text = computed(() => (copy.doc_end as Record<string, string>)[path.value] || copy.doc_end_generic)
</script>

<template>
  <div v-if="show" :key="path" class="tz-docend" data-from="doc-end">
    <p>{{ text }}</p>
    <a :href="withBase('/group')">{{ copy.doc_end_btn }} →</a>
  </div>
</template>
