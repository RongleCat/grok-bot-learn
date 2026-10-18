<script setup lang="ts">
import { withBase } from 'vitepress'
import GrokOrb from './GrokOrb.vue'
import copy from './ecosystem.json'

const c = copy.index
const pages = ['/ecosystem/grok-bot-clipper']
const covers = ['/ecosystem/clipper-banner.webp']
const trio = [
  { shape: 'nuage', color: 'orange', size: 72 },
  { shape: 'cercle', color: 'encre', size: 104 },
  { shape: 'squircle', color: 'bleu', size: 72 }
]
</script>

<template>
  <div class="eco">
    <section class="eco-hero">
      <div class="eco-trio">
        <GrokOrb v-for="(o, i) in trio" :key="i" :size="o.size" :shape="o.shape" :color="o.color" :playful="i === 1" />
      </div>
      <h1>{{ c.title }}</h1>
      <p>{{ c.lead }}</p>
    </section>
    <div class="eco-grid">
      <a v-for="(it, i) in c.items" :key="it.name" class="eco-card" :href="withBase(pages[i])">
        <img :src="withBase(covers[i])" :alt="it.name" width="1983" height="793" decoding="async" />
        <div class="eco-body">
          <span class="eco-tag">{{ it.tag }}</span>
          <strong>{{ it.name }}</strong>
          <span class="eco-desc">{{ it.desc }}</span>
          <span class="eco-cta">{{ it.cta }} →</span>
        </div>
      </a>
    </div>
  </div>
</template>

<style scoped>
.eco {
  max-width: 1080px;
  margin: 0 auto;
  padding: 32px 24px 96px;
}
.eco-hero {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 32px 0 48px;
}
.eco-trio {
  display: flex;
  align-items: flex-end;
  gap: 4px;
}
.eco-hero h1 {
  margin: 24px 0 0;
  font-size: clamp(36px, 6vw, 56px);
  line-height: 1.1;
  font-weight: 700;
  letter-spacing: -0.03em;
}
.eco-hero p {
  margin: 16px 0 0;
  font-size: 17px;
  line-height: 1.7;
  color: var(--vp-c-text-2);
}
.eco-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
}
.eco-card {
  display: flex;
  flex-direction: column;
  border: 1px solid var(--vp-c-divider);
  border-radius: 24px;
  overflow: hidden;
  background: var(--vp-c-bg);
  transition: transform 0.2s, border-color 0.2s, box-shadow 0.2s;
}
.eco-card:hover {
  transform: translateY(-3px);
  border-color: #0a0a0c;
  box-shadow: 0 18px 40px -24px rgba(10, 10, 12, 0.35);
}
.eco-card img {
  width: 100%;
  height: auto;
  aspect-ratio: 1983 / 793;
  object-fit: cover;
  background: #fff;
  border-bottom: 1px solid var(--vp-c-divider);
}
.eco-body {
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 22px 24px 24px;
}
.eco-tag {
  align-self: flex-start;
  padding: 2px 10px;
  border-radius: 999px;
  background: #fef1e4;
  font-size: 12px;
  font-weight: 600;
  color: #b4560f;
}
.eco-body strong {
  font-size: 22px;
  letter-spacing: -0.01em;
}
.eco-desc {
  font-size: 15px;
  line-height: 1.65;
  color: var(--vp-c-text-2);
}
.eco-cta {
  margin-top: 6px;
  font-size: 14px;
  font-weight: 600;
}
@media (max-width: 720px) {
  .eco-grid {
    grid-template-columns: 1fr;
  }
}
</style>
