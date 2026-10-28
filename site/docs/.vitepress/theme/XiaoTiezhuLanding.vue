<script setup lang="ts">
import { withBase } from 'vitepress'
import GrokOrb from './GrokOrb.vue'
import copy from './ecosystem.json'
import links from './links.json'
import { rich, tidy } from './rich'
import { track } from './track'

const c = copy.xiaotiezhu
const shots: Record<string, { src: string; href: string; w: number; h: number }> = {
  'digest-page': { src: '/ecosystem/xiaotiezhu-digest-page.webp', href: '/ecosystem/xiaotiezhu-digest-page.webp', w: 780, h: 1800 },
  'vip-card': { src: '/ecosystem/xiaotiezhu-vip-preview.webp', href: '/ecosystem/xiaotiezhu-vip-card.webp', w: 750, h: 1200 },
  'xiaowan-card': { src: '/ecosystem/xiaotiezhu-xiaowan-preview.webp', href: '/ecosystem/xiaotiezhu-xiaowan-card.webp', w: 750, h: 1200 }
}
const extraSkins = [
  { shape: 'capsule', color: 'bleu' },
  { shape: 'triangle', color: 'ambre' },
  { shape: 'squircle', color: 'turquoise' },
  { shape: 'hexagone', color: 'violet' }
]
const go = (from: string) => track('xiaotiezhu-cta', { from })
</script>

<template>
  <div class="xt">
    <section class="xt-hero">
      <div class="xt-id">
        <img class="xt-avatar" :src="withBase('/ecosystem/xiaotiezhu-avatar.webp')" alt="小铁柱" width="1254" height="1254" decoding="async" />
        <GrokOrb :size="72" shape="goutte" color="violet" />
      </div>
      <span class="xt-meta">{{ c.meta }}</span>
      <h1>小铁柱</h1>
      <p class="xt-slogan tz-tidy">{{ tidy(c.slogan) }}</p>
      <p class="xt-lead tz-tidy">{{ tidy(c.lead) }}</p>
      <div class="xt-actions">
        <a class="xt-btn primary" :href="withBase(links.xiaotiezhuWechat)" data-from="xiaotiezhu" @click="go('hero')">{{ c.ctaPrimary }}</a>
        <a class="xt-btn" :href="links.xiaotiezhuSample" target="_blank" rel="noopener">{{ c.ctaSecondary }}</a>
      </div>
      <p class="xt-unofficial tz-tidy">{{ tidy(c.unofficial) }}</p>
    </section>

    <section class="xt-sec">
      <h2>{{ c.featuresTitle }}</h2>
      <div class="xt-features">
        <div v-for="(f, i) in c.features" :key="f.k" class="xt-feature" :class="{ flip: i % 2 === 1 }">
          <div class="xt-visual" :class="{ bare: !shots[f.shot] }" :data-i="i">
            <a v-if="shots[f.shot]" :href="withBase(shots[f.shot].href)" target="_blank" rel="noopener">
              <img :src="withBase(shots[f.shot].src)" :alt="f.k" :width="shots[f.shot].w" :height="shots[f.shot].h" loading="lazy" decoding="async" />
            </a>
            <GrokOrb v-else :size="128" shape="nuage" color="orange" playful />
          </div>
          <div class="xt-text">
            <h3>{{ f.k }}</h3>
            <p v-html="rich(f.v)"></p>
          </div>
        </div>
      </div>
    </section>

    <section class="xt-sec">
      <h2>{{ c.pricingTitle }}</h2>
      <p class="xt-sub tz-tidy">{{ tidy(c.pricingLead) }}</p>
      <div class="xt-plans">
        <article v-for="p in c.plans" :key="p.name" class="xt-plan">
          <h3>{{ p.name }}</h3>
          <p class="xt-price"><b>¥{{ p.price }}</b><span>{{ p.unit }}</span></p>
          <p>{{ p.note }}</p>
        </article>
      </div>
      <ul class="xt-addons">
        <li v-for="a in c.addons" :key="a.name">
          <strong>{{ a.name }}</strong>
          <b>{{ a.price }}</b>
          <span>{{ a.note }}</span>
        </li>
      </ul>
      <p class="xt-theme">{{ c.themeNote }}</p>
    </section>

    <section class="xt-sec">
      <h2>{{ c.extrasTitle }}</h2>
      <div class="xt-extras">
        <div v-for="(e, i) in c.extras" :key="e.k" class="xt-extra">
          <GrokOrb :size="56" :shape="extraSkins[i].shape" :color="extraSkins[i].color" />
          <strong>{{ e.k }}</strong>
          <span v-html="rich(e.v)"></span>
        </div>
      </div>
    </section>

    <section class="xt-sec">
      <h2>{{ c.stepsTitle }}</h2>
      <ol class="xt-steps">
        <li v-for="s in c.steps" :key="s.k">
          <strong>{{ s.k }}</strong>
          <span v-html="rich(s.v)"></span>
        </li>
      </ol>
    </section>

    <section class="xt-sec">
      <h2>{{ c.faqTitle }}</h2>
      <div class="xt-faq">
        <details v-for="(f, i) in c.faq" :key="f.q" :open="i === 0">
          <summary>{{ f.q }}</summary>
          <p v-html="rich(f.a)"></p>
        </details>
      </div>
    </section>

    <section class="xt-sec">
      <div class="xt-end">
        <img :src="withBase('/ecosystem/xiaotiezhu-avatar.webp')" alt="" width="1254" height="1254" decoding="async" />
        <h2>{{ c.endTitle }}</h2>
        <p>{{ c.endText }}</p>
        <a class="xt-btn light" :href="withBase(links.xiaotiezhuWechat)" data-from="xiaotiezhu" @click="go('end')">{{ c.endBtn }}</a>
      </div>
    </section>
  </div>
</template>

<style scoped>
.xt {
  max-width: 1120px;
  margin: 0 auto;
  padding: 24px 24px 96px;
}
.xt-hero {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 48px 0 8px;
}
.xt-id {
  display: flex;
  align-items: flex-end;
  gap: 8px;
}
.xt-avatar {
  width: 96px;
  height: 96px;
  border-radius: 28px;
  object-fit: cover;
  border: 1px solid var(--vp-c-divider);
  background: #fff;
}
.xt-meta {
  margin-top: 22px;
  padding: 6px 14px;
  border-radius: 999px;
  background: var(--vp-c-bg-soft);
  font-size: 13px;
  color: var(--vp-c-text-2);
}
.xt-hero h1 {
  margin: 18px 0 0;
  font-size: clamp(44px, 8vw, 88px);
  line-height: 1;
  font-weight: 800;
  letter-spacing: -0.045em;
}
.xt-slogan {
  margin: 22px 0 0;
  max-width: 720px;
  font-size: clamp(22px, 3.4vw, 32px);
  font-weight: 700;
  letter-spacing: -0.02em;
  line-height: 1.3;
}
.xt-lead {
  max-width: 640px;
  margin: 14px 0 0;
  font-size: 17px;
  line-height: 1.7;
  color: var(--vp-c-text-2);
}
.xt-actions {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 12px;
  margin-top: 32px;
}
.xt-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 13px 26px;
  border-radius: 999px;
  border: 1px solid var(--vp-c-divider);
  font-size: 16px;
  font-weight: 600;
  transition: transform 0.2s, background 0.2s;
}
.xt-btn:hover {
  transform: translateY(-1px);
  background: var(--vp-c-bg-soft);
}
.xt-btn.primary {
  background: var(--tz-c-ink);
  border-color: var(--tz-c-ink);
  color: var(--tz-c-on-ink);
  box-shadow: 0 12px 28px -14px rgba(10, 10, 12, 0.6);
}
.xt-btn.primary:hover {
  background: var(--tz-c-ink-2);
}
.xt-btn.light {
  background: var(--tz-c-on-ink);
  border-color: var(--tz-c-on-ink);
  color: var(--tz-c-ink);
}
.xt-btn.light:hover {
  background: var(--tz-c-on-ink);
}
.xt-unofficial {
  margin: 16px 0 0;
  font-size: 13px;
  color: var(--vp-c-text-3);
}
.xt-sec {
  margin-top: 104px;
}
.xt-sec h2 {
  margin: 0;
  text-align: center;
  font-size: clamp(26px, 3.6vw, 36px);
  font-weight: 700;
  letter-spacing: -0.025em;
}
.xt-sub {
  margin: 12px 0 0;
  text-align: center;
  color: var(--vp-c-text-2);
}
.xt-features {
  display: flex;
  flex-direction: column;
  gap: 28px;
  margin-top: 40px;
}
.xt-feature {
  display: grid;
  grid-template-columns: 1.1fr 1fr;
  align-items: center;
  gap: 56px;
}
.xt-feature.flip .xt-visual {
  order: 2;
}
.xt-visual {
  border-radius: 28px;
  overflow: hidden;
  border: 1px solid var(--vp-c-divider);
  background: #fff;
}
.xt-visual[data-i='0'] { background: var(--tz-tint-2); }
.xt-visual[data-i='1'] { background: var(--tz-tint-1); }
.xt-visual[data-i='2'] { background: var(--tz-tint-3); }
.xt-visual[data-i='3'] { background: var(--tz-tint-4); }
.xt-visual.bare {
  display: grid;
  place-items: center;
  height: 280px;
  background: var(--tz-tint-3);
}
.xt-visual a {
  display: block;
}
.xt-visual img {
  display: block;
  width: 100%;
  height: 420px;
  object-fit: cover;
  object-position: top;
  background: #fff;
}
.xt-text h3 {
  margin: 0;
  font-size: 26px;
  font-weight: 700;
  letter-spacing: -0.02em;
}
.xt-text p,
.xt-extra :deep(span),
.xt-steps :deep(span),
.xt-faq :deep(p) {
  color: var(--vp-c-text-2);
}
.xt-text p {
  margin: 12px 0 0;
  font-size: 17px;
  line-height: 1.75;
}
.xt-text :deep(strong),
.xt-extra :deep(strong),
.xt-steps :deep(strong),
.xt-faq :deep(strong) {
  color: var(--vp-c-text-1);
}
.xt-plans {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  margin-top: 36px;
}
.xt-plan {
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 28px 24px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 24px;
  background: var(--vp-c-bg);
}
.xt-plan h3 {
  margin: 0;
  font-size: 18px;
}
.xt-price {
  display: flex;
  align-items: baseline;
  gap: 8px;
  margin: 0;
}
.xt-price b {
  font-size: clamp(40px, 5vw, 56px);
  line-height: 1;
  letter-spacing: -0.04em;
}
.xt-price span,
.xt-plan > p:last-child,
.xt-addons span {
  font-size: 15px;
  line-height: 1.65;
  color: var(--vp-c-text-2);
}
.xt-plan > p:last-child {
  margin: 4px 0 0;
}
.xt-addons {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin: 16px 0 0;
  padding: 0;
}
.xt-addons li {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 10px 16px;
  padding: 18px 22px;
  border-radius: 18px;
  background: var(--vp-c-bg-soft);
}
.xt-addons b {
  font-size: 22px;
  letter-spacing: -0.03em;
}
.xt-theme {
  margin: 16px 0 0;
  padding: 14px 18px;
  border-radius: 14px;
  background: var(--tz-tint-2);
  font-size: 15px;
  line-height: 1.65;
}
.xt-extras {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  margin-top: 36px;
}
.xt-extra {
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding: 22px;
  border-radius: 22px;
  background: var(--vp-c-bg-soft);
}
.xt-extra strong {
  font-size: 17px;
}
.xt-extra span {
  font-size: 14px;
  line-height: 1.65;
}
.xt-steps {
  list-style: none;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  margin: 36px 0 0;
  padding: 0;
}
.xt-steps li {
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 24px 22px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 22px;
}
.xt-steps strong {
  font-size: 17px;
}
.xt-steps span {
  font-size: 14px;
  line-height: 1.65;
}
.xt-faq {
  max-width: 760px;
  margin: 32px auto 0;
  border-top: 1px solid var(--vp-c-divider);
}
.xt-faq details {
  border-bottom: 1px solid var(--vp-c-divider);
}
.xt-faq summary {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
  padding: 20px 4px;
  font-size: 17px;
  font-weight: 600;
  cursor: pointer;
  list-style: none;
}
.xt-faq summary::-webkit-details-marker {
  display: none;
}
.xt-faq summary::after {
  content: '+';
  flex: none;
  font-size: 22px;
  font-weight: 400;
  color: var(--vp-c-text-3);
  transition: transform 0.2s;
}
.xt-faq details[open] summary::after {
  transform: rotate(45deg);
}
.xt-faq p {
  margin: 0;
  padding: 0 4px 20px;
  font-size: 15px;
  line-height: 1.75;
}
.xt-end {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 48px 32px 56px;
  border-radius: 32px;
  background: var(--tz-c-ink);
  color: var(--tz-c-on-ink);
}
.xt-end img {
  width: 88px;
  height: 88px;
  border-radius: 24px;
  object-fit: cover;
  background: #fff;
}
.xt-end h2 {
  margin-top: 28px;
  max-width: 720px;
  color: var(--tz-c-on-ink);
}
.xt-end p {
  max-width: 640px;
  margin: 12px 0 28px;
  color: var(--tz-end-muted);
}
@media (max-width: 900px) {
  .xt-extras {
    grid-template-columns: 1fr 1fr;
  }
  .xt-feature {
    gap: 32px;
  }
}
@media (max-width: 720px) {
  .xt-feature,
  .xt-plans,
  .xt-steps,
  .xt-extras {
    grid-template-columns: 1fr;
  }
  .xt-feature {
    gap: 18px;
  }
  .xt-feature.flip .xt-visual {
    order: 0;
  }
  .xt-visual img,
  .xt-visual.bare {
    height: 280px;
  }
  .xt-features {
    gap: 40px;
  }
  .xt-sec {
    margin-top: 80px;
  }
  .xt {
    padding-left: 20px;
    padding-right: 20px;
  }
}
@media (max-width: 520px) {
  .xt-extras {
    grid-template-columns: 1fr;
  }
  .xt-btn {
    padding: 12px 22px;
    font-size: 15px;
  }
}
</style>
