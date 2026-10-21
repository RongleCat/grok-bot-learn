<script setup lang="ts">
import { computed, onMounted, ref, watch } from 'vue'
import { withBase } from 'vitepress'
import data from './tools.json'
import { tidy } from './rich'

const ui = data.ui
const skin: Record<string, string> = {
  '编码 Agent': 'cercle-bleu',
  '模型/生成': 'goutte-rose',
  '通讯与发布': 'squircle-orange',
  '数据抓取': 'nuage-turquoise',
  '基础工具': 'hexagone-ambre'
}
const q = ref('')
const cat = ref('all')
const norm = (s: string) => s.toLowerCase().replace(/\s+/g, '')
const hay = data.tools.map((t) => norm([t.id, t.name, t.desc, t.what, t.cat, ...t.tags].join(' ')))
const hit = computed(() => {
  const k = norm(q.value)
  return data.tools.filter((t, i) => (!k || hay[i].includes(k)))
})
const shown = computed(() => hit.value.filter((t) => cat.value === 'all' || t.cat === cat.value))
const count = (c: string) => (c === 'all' ? hit.value.length : hit.value.filter((t) => t.cat === c).length)
const plain = (s: string) => s.replace(/\*\*|`/g, '')
onMounted(() => {
  const p = new URLSearchParams(location.search)
  if (p.get('q')) q.value = p.get('q') || ''
  if (p.get('cat') && data.cats.includes(p.get('cat') || '')) cat.value = p.get('cat') || 'all'
})
watch([q, cat], () => {
  const p = new URLSearchParams()
  if (q.value) p.set('q', q.value)
  if (cat.value !== 'all') p.set('cat', cat.value)
  const s = p.toString()
  history.replaceState(history.state, '', location.pathname + (s ? '?' + s : ''))
})
</script>

<template>
  <div class="tl">
    <section class="tl-hero">
      <div class="tl-blobs" aria-hidden="true">
        <img src="/bots/squircle-orange.svg" alt="" width="44" height="44" />
        <img class="c" src="/bots/galet-encre.svg" alt="" width="64" height="64" />
        <img src="/bots/nuage-turquoise.svg" alt="" width="44" height="44" />
      </div>
      <h1>{{ ui.title }}</h1>
      <p class="tz-tidy" v-html="tidy(ui.lead).replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')"></p>
    </section>

    <div class="tl-bar">
      <label class="tl-search">
        <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><circle cx="11" cy="11" r="7" fill="none" stroke="currentColor" stroke-width="2" /><path d="m20 20-3.5-3.5" stroke="currentColor" stroke-width="2" stroke-linecap="round" /></svg>
        <input v-model="q" type="search" :placeholder="ui.search" :aria-label="ui.search" />
      </label>
      <div class="tl-tabs" role="tablist">
        <button type="button" role="tab" :aria-selected="cat === 'all'" :class="['tl-tab', { on: cat === 'all' }]" @click="cat = 'all'">{{ ui.all }}<span>{{ count('all') }}</span></button>
        <button v-for="c in data.cats" :key="c" type="button" role="tab" :aria-selected="cat === c" :class="['tl-tab', { on: cat === c }]" @click="cat = c">
          <img :src="withBase(`/bots/${skin[c]}.svg`)" alt="" width="16" height="16" />{{ c }}<span>{{ count(c) }}</span>
        </button>
      </div>
    </div>

    <p class="tl-count">{{ ui.count.replace('{n}', String(shown.length)) }}</p>
    <div v-if="shown.length" class="tl-grid">
      <a v-for="t in shown" :id="t.id" :key="t.id" class="tl-card" :href="withBase(`/tools/${t.id}`)">
        <div class="tl-top">
          <img :src="withBase(`/bots/${skin[t.cat]}.svg`)" alt="" width="28" height="28" />
          <span class="tl-cat">{{ t.cat }}</span>
        </div>
        <strong>{{ t.name }}</strong>
        <span class="tl-desc">{{ plain(t.desc) }}</span>
        <span class="tl-cta">{{ ui.more }} →</span>
      </a>
    </div>
    <p v-else class="tl-empty">{{ ui.empty }}</p>
  </div>
</template>

<style scoped>
.tl {
  max-width: 1080px;
  margin: 0 auto;
  padding: 32px 24px 96px;
}
.tl-hero {
  text-align: center;
  padding: 32px 0 36px;
}
.tl-blobs {
  display: flex;
  justify-content: center;
  align-items: flex-end;
  gap: 10px;
}
.tl-blobs img.c {
  filter: drop-shadow(0 10px 14px rgba(10, 10, 12, 0.25));
}
.tl-hero h1 {
  margin: 20px 0 0;
  font-size: clamp(34px, 6vw, 52px);
  line-height: 1.1;
  font-weight: 700;
  letter-spacing: -0.03em;
}
.tl-hero p {
  margin: 14px auto 0;
  max-width: 34em;
  font-size: 17px;
  line-height: 1.8;
  color: var(--vp-c-text-2);
}
.tl-hero p :deep(strong) {
  color: var(--vp-c-text-1);
}
.tl-bar {
  position: sticky;
  top: var(--vp-nav-height, 64px);
  z-index: 5;
  padding: 10px 0;
  background: var(--vp-c-bg);
}
.tl-search {
  display: flex;
  align-items: center;
  gap: 10px;
  height: 48px;
  padding: 0 18px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 999px;
  color: var(--vp-c-text-3);
  transition: border-color 0.2s;
}
.tl-search:focus-within {
  border-color: #0a0a0c;
}
.tl-search input {
  flex: 1;
  min-width: 0;
  font-size: 17px;
  color: var(--vp-c-text-1);
  background: transparent;
  outline: none;
}
.tl-tabs {
  display: flex;
  gap: 6px;
  margin-top: 10px;
  overflow-x: auto;
  scrollbar-width: none;
}
.tl-tab {
  flex: none;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  height: 36px;
  padding: 0 14px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 999px;
  font-size: 15px;
  font-weight: 600;
  color: var(--vp-c-text-2);
  transition: border-color 0.2s, background 0.2s, color 0.2s;
}
.tl-tab span {
  font-size: 12px;
  font-weight: 500;
  color: var(--vp-c-text-3);
}
.tl-tab:hover {
  border-color: #0a0a0c;
}
.tl-tab.on {
  border-color: #0a0a0c;
  background: #0a0a0c;
  color: #fff;
}
.tl-tab.on span {
  color: rgba(255, 255, 255, 0.65);
}
.tl-count {
  margin: 12px 0 14px;
  font-size: 14px;
  color: var(--vp-c-text-3);
}
.tl-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}
.tl-card {
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 20px 22px 22px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 24px;
  background: var(--vp-c-bg);
  color: inherit;
  text-decoration: none;
  transition: transform 0.2s, border-color 0.2s, box-shadow 0.2s;
}
.tl-card:hover {
  transform: translateY(-3px);
  border-color: #0a0a0c;
  box-shadow: 0 18px 40px -24px rgba(10, 10, 12, 0.35);
}
.tl-top {
  display: flex;
  align-items: center;
  gap: 8px;
}
.tl-cat {
  font-size: 13px;
  font-weight: 600;
  color: var(--vp-c-text-3);
}
.tl-card strong {
  font-size: 20px;
  line-height: 1.35;
  letter-spacing: -0.01em;
}
.tl-desc {
  flex: 1;
  font-size: 15px;
  line-height: 1.7;
  color: var(--vp-c-text-2);
}
.tl-cta {
  margin-top: 4px;
  font-size: 14px;
  font-weight: 600;
}
.tl-empty {
  padding: 48px 0;
  text-align: center;
  font-size: 17px;
  color: var(--vp-c-text-3);
}
@media (max-width: 960px) {
  .tl-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
@media (max-width: 640px) {
  .tl {
    padding: 16px 20px 72px;
  }
  .tl-grid {
    grid-template-columns: 1fr;
  }
}
</style>
