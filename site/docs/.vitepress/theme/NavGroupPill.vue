<script setup lang="ts">
import { computed } from 'vue'
import uiRoot from './ui.json'
import { useLocaleJson, useLocalePath } from './i18n'

const ui = useLocaleJson(uiRoot as Record<string, unknown>, 'ui.json')
const t = computed(() => ui.value as any)
const localePath = useLocalePath()
</script>

<template>
  <a class="tz-nav-pill" :href="localePath('/group')">{{ t.nav.groupPill }}</a>
</template>
