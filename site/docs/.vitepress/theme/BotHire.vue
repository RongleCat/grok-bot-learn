<script setup lang="ts">
import { ref } from 'vue'
import data from './bots.json'

const bots = data.bots
const lead = bots.find((b) => 'primary' in b && b.primary) || bots[0]
const rest = bots.filter((b) => b !== lead)
const half = Math.ceil(rest.length / 2)
const crowd = [...rest.slice(0, half), lead, ...rest.slice(half)].map((b, i) => {
  const d = Math.abs(i - half)
  return { b, k: d ? Math.max(0.8, 1.3 - d * 0.1) : 1.5, c: !d }
})
const said = ref<Record<string, string>>({})
const open = ref('')
const hop = ref<Record<string, number>>({})
const last: Record<string, number> = {}

function speak(slug: string) {
  const b = bots.find((x) => x.slug === slug)
  if (!b) return
  let i = Math.floor(Math.random() * b.lines.length)
  if (b.lines.length > 1 && i === last[slug]) i = (i + 1 + Math.floor(Math.random() * (b.lines.length - 1))) % b.lines.length
  last[slug] = i
  said.value = { ...said.value, [slug]: b.lines[i] }
  hop.value = { ...hop.value, [slug]: (hop.value[slug] || 0) + 1 }
  open.value = slug
}

function hush(slug: string) {
  if (open.value === slug) open.value = ''
}

let touch = false

function enter(e: PointerEvent, slug: string) {
  touch = e.pointerType !== 'mouse'
  if (!touch) speak(slug)
}

function leave(e: PointerEvent, slug: string) {
  if (e.pointerType === 'mouse') hush(slug)
}

function press(slug: string) {
  if (touch) speak(slug)
}

function focus(slug: string) {
  if (!touch) speak(slug)
}
</script>

<template>
  <div class="hire">
    <section class="hire-hero">
      <div class="hire-crowd" aria-hidden="true">
        <svg v-for="m in crowd" :key="m.b.slug" :viewBox="m.b.vb" class="hire-mini" :class="{ c: m.c }" :style="{ '--k': m.k, '--t': m.b.color }">
          <path :d="m.b.head" :fill="m.b.color" />
          <path v-for="(e, k) in m.b.eyes" :key="k" :d="e" fill="#fff" />
        </svg>
      </div>
      <h1>{{ data.title }}</h1>
      <p>{{ data.lead }}</p>
    </section>
    <div class="hire-grid">
      <article v-for="b in bots" :key="b.slug" class="hire-card" :style="{ '--tint': b.color }">
        <div class="hire-stage">
          <span class="hire-bubble" :class="{ on: open === b.slug }" role="status" aria-live="polite">{{ said[b.slug] }}</span>
          <button
            type="button"
            class="hire-face"
            :aria-label="b.name"
            @pointerenter="enter($event, b.slug)"
            @pointerleave="leave($event, b.slug)"
            @focus="focus(b.slug)"
            @blur="hush(b.slug)"
            @click="press(b.slug)"
          >
            <svg :key="hop[b.slug] || 0" :viewBox="b.vb" :class="{ hop: hop[b.slug] }">
              <path :d="b.head" :fill="b.color" />
              <path v-for="(e, k) in b.eyes" :key="k" :d="e" fill="#fff" />
            </svg>
          </button>
        </div>
        <h2>{{ b.name }}</h2>
        <p>{{ b.desc }}</p>
        <div class="hire-acts">
          <a class="hire-use" :href="b.url" target="_blank" rel="noopener" :data-umami-event="'bot-import'" :data-umami-event-bot="b.slug">{{ data.use }}</a>
          <a class="hire-post" :href="b.post" target="_blank" rel="noopener" :data-umami-event="'bot-post'" :data-umami-event-bot="b.slug">{{ data.post }}</a>
        </div>
      </article>
    </div>
  </div>
</template>

<style scoped>
.hire {
  max-width: 1120px;
  margin: 0 auto;
  padding: 32px 24px 96px;
}
.hire-hero {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 32px 0 48px;
}
.hire-crowd {
  --u: min(52px, 8vw);
  display: flex;
  justify-content: center;
  align-items: flex-end;
  gap: min(6px, 0.9vw);
  width: 100%;
}
.hire-mini {
  flex: none;
  width: calc(var(--u) * var(--k, 1));
  height: calc(var(--u) * var(--k, 1));
  overflow: visible;
}
.hire-mini.c {
  margin: 0 min(6px, 0.9vw);
  filter: drop-shadow(0 10px 14px color-mix(in srgb, var(--t) 30%, transparent));
}
.hire-hero h1 {
  margin: 24px 0 0;
  font-size: clamp(36px, 6vw, 56px);
  line-height: 1.1;
  font-weight: 700;
  letter-spacing: -0.03em;
}
.hire-hero p {
  margin: 16px 0 0;
  font-size: 17px;
  line-height: 1.7;
  color: var(--vp-c-text-2);
}
.hire-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}
.hire-card {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 0 24px 24px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 24px;
  background: var(--vp-c-bg);
  transition: transform 0.2s, border-color 0.2s, box-shadow 0.2s;
}
.hire-card:hover {
  transform: translateY(-3px);
  border-color: #0a0a0c;
  box-shadow: 0 18px 40px -24px rgba(10, 10, 12, 0.35);
}
.hire-stage {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: flex-end;
  width: calc(100% + 48px);
  height: 176px;
  margin: 0 -24px 18px;
  padding-bottom: 24px;
  border-radius: 23px 23px 0 0;
  background: radial-gradient(ellipse 120px 72px at 50% 68%, color-mix(in srgb, var(--tint) 24%, transparent) 0%, color-mix(in srgb, var(--tint) 8%, transparent) 55%, transparent 100%);
}
.hire-face {
  width: 92px;
  height: 92px;
  padding: 0;
  border: 0;
  background: none;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}
.hire-face svg {
  width: 100%;
  height: 100%;
  overflow: visible;
  transform-origin: 50% 100%;
}
.hire-face svg.hop {
  animation: hop 0.6s cubic-bezier(0.3, 1.6, 0.5, 1);
}
.hire-face:focus-visible {
  outline: 2px solid #0a0a0c;
  outline-offset: 6px;
  border-radius: 50%;
}
@keyframes hop {
  0% { transform: translateY(0) scale(1, 1); }
  25% { transform: translateY(2px) scale(1.08, 0.9); }
  55% { transform: translateY(-12px) scale(0.95, 1.06); }
  80% { transform: translateY(0) scale(1.03, 0.97); }
  100% { transform: translateY(0) scale(1, 1); }
}
.hire-bubble {
  position: absolute;
  left: 50%;
  top: 12px;
  z-index: 2;
  width: max-content;
  max-width: calc(100% - 32px);
  padding: 8px 14px;
  border: 1.5px solid #0a0a0c;
  border-radius: 16px;
  background: #fff;
  font-size: 14px;
  font-weight: 600;
  line-height: 1.45;
  color: #0a0a0c;
  box-shadow: 3px 3px 0 #0a0a0c;
  opacity: 0;
  pointer-events: none;
  transform: translate(-50%, 6px) scale(0.92);
  transform-origin: 50% 100%;
  transition: opacity 0.18s, transform 0.28s cubic-bezier(0.3, 1.5, 0.5, 1);
}
.hire-bubble::after {
  content: '';
  position: absolute;
  left: 50%;
  bottom: -7px;
  width: 12px;
  height: 12px;
  margin-left: -6px;
  border-right: 1.5px solid #0a0a0c;
  border-bottom: 1.5px solid #0a0a0c;
  background: #fff;
  transform: rotate(45deg);
}
.hire-bubble.on {
  opacity: 1;
  transform: translate(-50%, 0) scale(1);
}
.hire-card h2 {
  margin: 0;
  padding: 0;
  border: 0;
  font-size: 21px;
  font-weight: 700;
  letter-spacing: -0.01em;
  line-height: 1.3;
}
.hire-card p {
  flex: 1;
  margin: 10px 0 0;
  font-size: 15px;
  line-height: 1.65;
  color: var(--vp-c-text-2);
}
.hire-acts {
  display: flex;
  gap: 10px;
  margin-top: 20px;
}
.hire-acts a {
  display: inline-flex;
  align-items: center;
  height: 38px;
  padding: 0 18px;
  border-radius: 999px;
  font-size: 14px;
  font-weight: 600;
  text-decoration: none;
  transition: background 0.2s, border-color 0.2s;
}
.hire-use {
  background: #0a0a0c;
  color: #fff;
}
.hire-use:hover {
  background: #2a2a2e;
}
.hire-post {
  border: 1px solid var(--vp-c-divider);
  color: #0a0a0c;
}
.hire-post:hover {
  border-color: #0a0a0c;
}
@media (max-width: 960px) {
  .hire-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
@media (max-width: 640px) {
  .hire {
    padding: 16px 16px 72px;
  }
  .hire-grid {
    grid-template-columns: 1fr;
  }
}
@media (prefers-reduced-motion: reduce) {
  .hire-face svg.hop {
    animation: none;
  }
  .hire-bubble,
  .hire-card {
    transition: opacity 0.18s;
  }
  .hire-bubble,
  .hire-bubble.on,
  .hire-card:hover {
    transform: translate(-50%, 0);
  }
  .hire-card:hover {
    transform: none;
  }
}
</style>
