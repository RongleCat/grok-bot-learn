<script setup lang="ts">
import { computed, ref } from 'vue'
import data from './changelog.json'
import { tidy } from './rich'

type Item = { kind: 'pc' | 'mobile' | 'ours'; id: string; date: string; platform: string; version: string; url: string; title: string; points: string[]; summary: string }

const ui = data.ui
const chip: Record<string, string> = { pc: 'PC', ios: 'iOS', android: 'Android' }
const tabs = [
  { k: 'all', t: '全部' },
  { k: 'pc', t: 'PC' },
  { k: 'mobile', t: '移动端' },
  { k: 'ours', t: '我们的解读' }
]
const items: Item[] = [
  ...data.official.map((e: any) => ({ kind: e.platform === 'pc' ? 'pc' : 'mobile', summary: '', ...e })),
  ...data.ours.map((t: any) => ({ kind: 'ours', version: '', points: [], ...t }))
].sort((a, b) => (a.date === b.date ? (a.kind === 'ours' ? -1 : b.kind === 'ours' ? 1 : 0) : a.date < b.date ? 1 : -1)) as Item[]
const counts = computed(() => ({ all: items.length, pc: items.filter((i) => i.kind === 'pc').length, mobile: items.filter((i) => i.kind === 'mobile').length, ours: items.filter((i) => i.kind === 'ours').length }))
const tab = ref('all')
const limit = ref(16)
const shown = computed(() => items.filter((i) => tab.value === 'all' || i.kind === tab.value))
const md = (d: string) => `${+d.slice(5, 7)}月${+d.slice(8, 10)}日`
const month = (d: string) => `${d.slice(0, 4)} 年 ${+d.slice(5, 7)} 月`
function pick(k: string) {
  tab.value = k
  limit.value = 16
}
</script>

<template>
  <div class="cl">
    <section class="cl-hero">
      <div class="cl-blobs" aria-hidden="true">
        <img src="/bots/cercle-bleu.svg" alt="" width="44" height="44" />
        <img class="c" src="/bots/goutte-rose.svg" alt="" width="64" height="64" />
        <img src="/bots/triangle-violet.svg" alt="" width="44" height="44" />
      </div>
      <h1>更新日志</h1>
      <p class="tz-tidy">{{ tidy(ui.lead) }}</p>
      <p class="cl-meta">{{ ui.synced }} {{ data.updated }} · {{ ui.note }}</p>
    </section>

    <div class="cl-tabs" role="tablist">
      <button v-for="t in tabs" :key="t.k" type="button" role="tab" :aria-selected="tab === t.k" :class="['cl-tab', t.k, { on: tab === t.k }]" @click="pick(t.k)">
        {{ t.t }}<span>{{ counts[t.k as keyof typeof counts] }}</span>
      </button>
    </div>

    <ol class="cl-line">
      <template v-for="(it, n) in shown" :key="it.kind + it.id">
        <li v-if="n === 0 || month(it.date) !== month(shown[n - 1].date)" v-show="n < limit" class="cl-month">{{ month(it.date) }}</li>
        <li v-show="n < limit" :class="['cl-item', it.kind]">
          <time :datetime="it.date">{{ md(it.date) }}</time>
          <article class="cl-card">
            <div class="cl-chips">
              <img v-if="it.kind === 'ours'" class="cl-face" src="/bots/goutte-rose.svg" alt="" width="22" height="22" />
              <span v-if="it.kind === 'ours'" class="cl-chip ours">我们的解读</span>
              <span v-else class="cl-chip" :class="it.platform">{{ chip[it.platform] }}</span>
              <span v-if="it.version" class="cl-ver">v{{ it.version }}</span>
            </div>
            <h2 class="tz-tidy">{{ tidy(it.title) }}</h2>
            <ul v-if="it.points.length">
              <li v-for="(p, k) in it.points" :key="k">{{ tidy(p.replace(/。$/, '')) }}</li>
            </ul>
            <p v-if="it.summary">{{ tidy(it.summary) }}</p>
            <a :href="it.url" target="_blank" rel="noopener" :data-umami-event="it.kind === 'ours' ? 'changelog-tweet' : 'changelog-official'">{{ it.kind === 'ours' ? ui.tweet : ui.official }} ↗</a>
          </article>
        </li>
      </template>
      <li v-if="!shown.length" class="cl-empty">{{ ui.empty }}</li>
    </ol>
    <div v-if="shown.length > limit" class="cl-more">
      <button type="button" @click="limit += 16">{{ ui.more }}</button>
    </div>
  </div>
</template>

<style scoped>
.cl {
  --pc: #3b82f6;
  --mo: #8b5cf6;
  --ours: #ff5eb1;
  max-width: 760px;
  margin: 0 auto;
  padding: 32px 24px 96px;
}
.cl-hero {
  text-align: center;
  padding: 32px 0 36px;
}
.cl-blobs {
  display: flex;
  justify-content: center;
  align-items: flex-end;
  gap: 10px;
}
.cl-blobs img.c {
  filter: drop-shadow(0 10px 14px rgba(255, 94, 177, 0.3));
}
.cl-hero h1 {
  margin: 20px 0 0;
  font-size: clamp(34px, 6vw, 52px);
  line-height: 1.1;
  font-weight: 700;
  letter-spacing: -0.03em;
}
.cl-hero p {
  margin: 14px auto 0;
  max-width: 34em;
  font-size: 17px;
  line-height: 1.8;
  color: var(--vp-c-text-2);
}
.cl-hero .cl-meta {
  margin-top: 6px;
  font-size: 14px;
  line-height: 1.6;
  color: var(--vp-c-text-3);
}
.cl-tabs {
  position: sticky;
  top: var(--vp-nav-height, 64px);
  z-index: 5;
  display: flex;
  gap: 6px;
  padding: 10px 0;
  margin-bottom: 8px;
  overflow-x: auto;
  scrollbar-width: none;
  background: var(--vp-c-bg);
}
.cl-tab {
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
.cl-tab span {
  font-size: 12px;
  font-weight: 500;
  color: var(--vp-c-text-3);
}
.cl-tab:hover {
  border-color: #0a0a0c;
}
.cl-tab.on {
  border-color: #0a0a0c;
  background: #0a0a0c;
  color: #fff;
}
.cl-tab.on span {
  color: rgba(255, 255, 255, 0.65);
}
.cl-line {
  list-style: none;
  margin: 0;
  padding: 0;
}
.cl-month {
  margin: 28px 0 12px;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 0.04em;
  color: var(--vp-c-text-3);
}
.cl-item {
  position: relative;
  display: grid;
  grid-template-columns: 76px 1fr;
  gap: 20px;
  padding-bottom: 16px;
}
.cl-item::before {
  content: '';
  position: absolute;
  left: 88px;
  top: 26px;
  bottom: -2px;
  width: 1px;
  background: var(--vp-c-divider);
}
.cl-item time {
  padding-top: 18px;
  font-size: 14px;
  font-weight: 600;
  text-align: right;
  color: var(--vp-c-text-2);
  font-variant-numeric: tabular-nums;
}
.cl-card {
  position: relative;
  margin-left: 12px;
  padding: 16px 20px 18px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 18px;
  background: var(--vp-c-bg);
}
.cl-card::before {
  content: '';
  position: absolute;
  left: -19px;
  top: 21px;
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: var(--dot, var(--pc));
  box-shadow: 0 0 0 4px var(--vp-c-bg);
}
.cl-item.mobile .cl-card::before {
  --dot: var(--mo);
}
.cl-item.ours .cl-card {
  border-color: color-mix(in srgb, var(--ours) 35%, transparent);
  background: linear-gradient(180deg, color-mix(in srgb, var(--ours) 7%, var(--vp-c-bg)), var(--vp-c-bg) 70%);
}
.cl-item.ours .cl-card::before {
  --dot: var(--ours);
}
.cl-chips {
  display: flex;
  align-items: center;
  gap: 8px;
}
.cl-face {
  width: 22px;
  height: 22px;
}
.cl-chip {
  display: inline-flex;
  align-items: center;
  height: 22px;
  padding: 0 9px;
  border-radius: 999px;
  font-size: 12px;
  font-weight: 600;
  color: var(--pc);
  background: color-mix(in srgb, var(--pc) 10%, transparent);
}
.cl-chip.ios,
.cl-chip.android {
  color: var(--mo);
  background: color-mix(in srgb, var(--mo) 10%, transparent);
}
.cl-chip.ours {
  color: #d62f86;
  background: color-mix(in srgb, var(--ours) 12%, transparent);
}
.cl-ver {
  font-size: 13px;
  color: var(--vp-c-text-3);
  font-variant-numeric: tabular-nums;
}
.cl-card h2 {
  margin: 10px 0 0;
  padding: 0;
  border: 0;
  font-size: 19px;
  line-height: 1.45;
  font-weight: 700;
  letter-spacing: -0.01em;
}
.cl-card ul {
  margin: 8px 0 0;
  padding-left: 1.1em;
}
.cl-card li,
.cl-card p {
  font-size: 16px;
  line-height: 1.8;
  color: var(--vp-c-text-1);
}
.cl-card p {
  margin: 8px 0 0;
}
.cl-card a {
  display: inline-block;
  margin-top: 10px;
  font-size: 14px;
  font-weight: 600;
  color: var(--vp-c-text-2);
  text-decoration: none;
}
.cl-card a:hover {
  color: #0a0a0c;
  text-decoration: underline;
}
.cl-empty {
  padding: 48px 0;
  text-align: center;
  color: var(--vp-c-text-3);
}
.cl-more {
  display: flex;
  justify-content: center;
  margin-top: 16px;
}
.cl-more button {
  height: 42px;
  padding: 0 22px;
  border-radius: 999px;
  background: #0a0a0c;
  color: #fff;
  font-size: 15px;
  font-weight: 600;
}
.cl-more button:hover {
  background: #2a2a2e;
}
@media (max-width: 640px) {
  .cl {
    padding: 16px 20px 72px;
  }
  .cl-tabs {
    top: var(--vp-nav-height, 64px);
    margin: 0 -20px 4px;
    padding: 10px 20px;
  }
  .cl-item {
    grid-template-columns: 1fr;
    gap: 6px;
    padding-left: 18px;
  }
  .cl-item::before {
    left: 4px;
    top: 8px;
  }
  .cl-item time {
    padding-top: 0;
    text-align: left;
  }
  .cl-card {
    margin-left: 0;
    padding: 14px 16px 16px;
  }
  .cl-card::before {
    left: -18px;
    top: -21px;
  }
  .cl-card h2 {
    font-size: 18px;
  }
}
</style>
