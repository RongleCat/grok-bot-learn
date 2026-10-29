<script setup lang="ts">
import { computed, ref } from 'vue'
import dataRoot from './changelog.json'
import { useLocaleJson } from './i18n'
const data = useLocaleJson(dataRoot as Record<string, unknown>, 'changelog.json')
import { tidy } from './rich'

type Item = { kind: 'pc' | 'mobile' | 'ours'; id: string; date: string; platform: string; version: string; url: string; title: string; points: string[]; summary: string; full?: [string, string[]][] }

const ui = computed(() => (data.value as any).ui)
const chip: Record<string, string> = { pc: 'PC', ios: 'iOS', android: 'Android' }
const tabs = [
  { k: 'all', t: '全部' },
  { k: 'pc', t: 'PC' },
  { k: 'mobile', t: '移动端' },
  { k: 'ours', t: '我们的解读' }
]
const items: Item[] = [
  ...(data.value as any).official.map((e: any) => ({ kind: e.platform === 'pc' ? 'pc' : 'mobile', summary: '', ...e })),
  ...(data.value as any).ours.map((t: any) => ({ kind: 'ours', version: '', points: [], ...t }))
].sort((a, b) => (a.date === b.date ? (a.kind === 'ours' ? -1 : b.kind === 'ours' ? 1 : 0) : a.date < b.date ? 1 : -1)) as Item[]
const counts = computed(() => ({ all: items.length, pc: items.filter((i) => i.kind === 'pc').length, mobile: items.filter((i) => i.kind === 'mobile').length, ours: items.filter((i) => i.kind === 'ours').length }))
const tab = ref('all')
const limit = ref(16)
const shown = computed(() => items.filter((i) => tab.value === 'all' || i.kind === tab.value))
const groups = computed(() => {
  const out: { m: string; start: number; items: Item[] }[] = []
  shown.value.forEach((it, n) => {
    const m = month(it.date)
    if (!out.length || out[out.length - 1].m !== m) out.push({ m, start: n, items: [] })
    out[out.length - 1].items.push(it)
  })
  return out
})
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
      <li v-for="g in groups" v-show="g.start < limit" :key="g.m" class="cl-month">
        <h3>{{ g.m }}</h3>
        <ol class="cl-group">
          <li v-for="(it, j) in g.items" v-show="g.start + j < limit" :key="it.kind + it.id" :class="['cl-item', it.kind]">
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
              <details v-if="it.full && it.full.length" class="cl-full">
                <summary>{{ ui.full }}</summary>
                <div v-for="(sec, k) in it.full" :key="k" class="cl-sec">
                  <h4 v-if="sec[0]">{{ sec[0] }}</h4>
                  <ul>
                    <li v-for="(x, q) in sec[1]" :key="q">{{ tidy(x) }}</li>
                  </ul>
                </div>
              </details>
              <a :href="it.url" target="_blank" rel="noopener" :data-umami-event="it.kind === 'ours' ? 'changelog-tweet' : 'changelog-official'">{{ it.kind === 'ours' ? ui.tweet : ui.official }} ↗</a>
            </article>
          </li>
        </ol>
      </li>
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
  border-color: var(--tz-c-hover-border);
}
.cl-tab.on {
  border-color: var(--tz-c-ink);
  background: var(--tz-c-ink);
  color: var(--tz-c-on-ink);
}
.cl-tab.on span {
  color: var(--tz-on-ink-muted);
}
.cl-line {
  list-style: none;
  margin: 0;
  padding: 0;
}
.cl-month {
  margin: 28px 0 0;
}
.cl-month h3 {
  margin: 0 0 14px;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 0.04em;
  line-height: 1.5;
  color: var(--vp-c-text-3);
}
.cl-group {
  --date: 72px;
  --rail: 32px;
  position: relative;
  list-style: none;
  margin: 0;
  padding: 0;
}
.cl-group::before {
  content: '';
  position: absolute;
  left: calc(var(--date) + var(--rail) / 2 - 1px);
  top: 28px;
  bottom: 0;
  width: 2px;
  border-radius: 2px;
  background: var(--vp-c-divider);
}
.cl-item {
  position: relative;
  display: grid;
  grid-template-columns: var(--date) var(--rail) minmax(0, 1fr);
  padding-bottom: 16px;
}
.cl-item:last-child {
  padding-bottom: 0;
}
.cl-item::before {
  content: '';
  position: absolute;
  left: calc(var(--date) + var(--rail) / 2 - 6px);
  top: 22px;
  width: 12px;
  height: 12px;
  box-sizing: border-box;
  border-radius: 50%;
  background: var(--dot, var(--pc));
  box-shadow: 0 0 0 4px var(--vp-c-bg);
}
.cl-item.mobile {
  --dot: var(--mo);
}
.cl-item.ours {
  --dot: var(--ours);
}
.cl-item time {
  grid-column: 1;
  padding-top: 17px;
  padding-right: 4px;
  font-size: 14px;
  font-weight: 600;
  line-height: 22px;
  text-align: right;
  white-space: nowrap;
  color: var(--vp-c-text-2);
  font-variant-numeric: tabular-nums;
}
.cl-card {
  grid-column: 3;
  min-width: 0;
  padding: 16px 20px 18px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 18px;
  background: var(--vp-c-bg);
}
.cl-item.ours .cl-card {
  border-color: color-mix(in srgb, var(--ours) 35%, transparent);
  background: linear-gradient(180deg, color-mix(in srgb, var(--ours) 7%, var(--vp-c-bg)), var(--vp-c-bg) 70%);
}
.cl-chips {
  display: flex;
  height: 22px;
  line-height: 22px;
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
  color: var(--tz-badge-ours);
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
  padding-left: 1.2em;
  list-style: disc;
}
.cl-card li::marker {
  color: var(--vp-c-text-3);
}
.cl-full {
  margin-top: 12px;
  border-top: 1px dashed var(--vp-c-divider);
  padding-top: 10px;
}
.cl-full summary {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 14px;
  font-weight: 600;
  line-height: 1.6;
  color: var(--tz-c-ink);
  cursor: pointer;
  list-style: none;
}
.cl-full summary::-webkit-details-marker {
  display: none;
}
.cl-full summary::after {
  content: '';
  width: 6px;
  height: 6px;
  border-right: 1.5px solid currentColor;
  border-bottom: 1.5px solid currentColor;
  transform: translateY(-2px) rotate(45deg);
  transition: transform 0.2s;
}
.cl-full[open] summary::after {
  transform: translateY(1px) rotate(-135deg);
}
.cl-full summary:focus-visible {
  outline: 2px solid var(--tz-c-ink);
  outline-offset: 3px;
  border-radius: 4px;
}
.cl-sec h4 {
  margin: 14px 0 0;
  font-size: 15px;
  font-weight: 700;
  line-height: 1.5;
}
.cl-sec ul {
  margin-top: 4px;
}
.cl-sec li {
  font-size: 15px;
  line-height: 1.75;
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
  color: var(--tz-c-ink);
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
  background: var(--tz-c-ink);
  color: var(--tz-c-on-ink);
  font-size: 15px;
  font-weight: 600;
}
.cl-more button:hover {
  background: var(--tz-c-ink-2);
}
@media (max-width: 640px) {
  .cl {
    padding: 16px 20px 72px;
  }
  .cl-tabs {
    margin: 0 -20px 4px;
    padding: 10px 20px;
  }
  .cl-group {
    --rail: 22px;
  }
  .cl-group::before {
    left: 10px;
    top: 11px;
    bottom: 0;
  }
  .cl-item {
    grid-template-columns: var(--rail) minmax(0, 1fr);
    row-gap: 8px;
  }
  .cl-item::before {
    left: 5px;
    top: 5px;
  }
  .cl-item time {
    grid-column: 2;
    padding: 0;
    text-align: left;
  }
  .cl-card {
    grid-column: 2;
    padding: 14px 16px 16px;
  }
  .cl-card h2 {
    font-size: 18px;
  }
}
</style>
