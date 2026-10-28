<script setup lang="ts">
import { withBase } from 'vitepress'
import GrokOrb from './GrokOrb.vue'
import JoinCard from './JoinCard.vue'
import copy from './ecosystem.json'
import links from './links.json'
import { rich, tidy } from './rich'
import { track } from './track'

const c = copy.xiaotiezhu
const shots: Record<string, string> = {
  'digest-page': '/ecosystem/xiaotiezhu-digest-page.webp',
  'vip-card': '/ecosystem/xiaotiezhu-vip-preview.webp',
  'xiaowan-card': '/ecosystem/xiaotiezhu-xiaowan-preview.webp'
}
const fullShots: Record<string, string> = {
  'vip-card': '/ecosystem/xiaotiezhu-vip-card.webp',
  'xiaowan-card': '/ecosystem/xiaotiezhu-xiaowan-card.webp'
}
const skins = [
  { shape: 'squircle', color: 'bleu' },
  { shape: 'goutte', color: 'violet' },
  { shape: 'nuage', color: 'orange' },
  { shape: 'hexagone', color: 'vert' }
]
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
      <img class="xt-avatar" :src="withBase('/ecosystem/xiaotiezhu-avatar.webp')" alt="" width="120" height="120" decoding="async" />
      <span class="xt-meta">{{ c.meta }}</span>
      <h1>小铁柱</h1>
      <p class="xt-slogan tz-tidy">{{ tidy(c.slogan) }}</p>
      <p class="xt-lead tz-tidy">{{ tidy(c.lead) }}</p>
      <div class="xt-actions">
        <a class="xt-btn primary" :href="withBase(links.xiaotiezhuWechat)" @click="go('hero')">{{ c.ctaPrimary }}</a>
        <a class="xt-btn" :href="links.xiaotiezhuSample" target="_blank" rel="noopener">{{ c.ctaSecondary }}</a>
      </div>
      <p class="xt-unofficial tz-tidy">{{ tidy(c.unofficial) }}</p>
    </section>

    <section class="xt-sec">
      <h2>{{ c.featuresTitle }}</h2>
      <div class="xt-features">
        <div v-for="(f, i) in c.features" :key="f.k" class="xt-feature" :class="{ flip: i % 2 === 1 }">
          <div class="xt-visual" :data-i="i" aria-hidden="true">
            <a
              v-if="shots[f.shot]"
              class="xt-shot"
              :href="withBase(fullShots[f.shot] || shots[f.shot])"
              target="_blank"
              rel="noopener"
            >
              <img :src="withBase(shots[f.shot])" :alt="f.k" loading="lazy" decoding="async" />
            </a>
            <GrokOrb v-else class="xt-vorb" :size="120" :shape="skins[i].shape" :color="skins[i].color" playful />
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
        <div v-for="p in c.plans" :key="p.name" class="xt-plan">
          <span class="xt-plan-name">{{ p.name }}</span>
          <div class="xt-price">
            <span class="xt-yen">¥</span>
            <span class="xt-num">{{ p.price }}</span>
            <span class="xt-unit">{{ p.unit }}</span>
          </div>
          <p class="xt-plan-note">{{ p.note }}</p>
        </div>
      </div>
      <ul class="xt-addons">
        <li v-for="a in c.addons" :key="a.name">
          <strong>{{ a.name }}</strong>
          <span class="xt-addon-price">{{ a.price }}</span>
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
        <li v-for="(s, i) in c.steps" :key="s.k">
          <span class="n">{{ i + 1 }}</span>
          <strong>{{ s.k.replace(/^\d+\.\s*/, '') }}</strong>
          <span v-html="rich(s.v)"></span>
        </li>
      </ol>
    </section>

    <section class="xt-sec xt-faqsec">
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
        <h2>{{ c.endTitle }}</h2>
        <p>{{ c.endText }}</p>
        <a class="xt-btn light" :href="withBase(links.xiaotiezhuWechat)" @click="go('end')">{{ c.endBtn }}</a>
        <div class="xt-join">
          <JoinCard from="xiaotiezhu">
            <p class="xt-join-hint">扫码添加管家微信，开通小铁柱</p>
          </JoinCard>
        </div>
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
.xt-avatar {
  width: 96px;
  height: 96px;
  border-radius: 28px;
  object-fit: cover;
  border: 1px solid var(--vp-c-divider);
  box-shadow: 0 16px 40px -24px rgba(10, 10, 12, 0.45);
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
  font-size: clamp(44px, 8vw, 80px);
  line-height: 1;
  font-weight: 800;
  letter-spacing: -0.045em;
}
.xt-slogan {
  margin: 22px 0 0;
  max-width: 720px;
  font-size: clamp(20px, 3.2vw, 30px);
  font-weight: 700;
  letter-spacing: -0.02em;
  line-height: 1.35;
}
.xt-lead {
  max-width: 620px;
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
.xt-visual[data-i='0'] { background: var(--tz-tint-1); }
.xt-visual[data-i='1'] { background: var(--tz-tint-2); }
.xt-visual[data-i='2'] { background: var(--tz-tint-3); }
.xt-visual[data-i='3'] { background: var(--tz-tint-4); }
.xt-visual {
  position: relative;
  display: grid;
  place-items: center;
  min-height: 280px;
  border-radius: 28px;
  overflow: hidden;
  padding: 20px;
}
.xt-shot {
  display: block;
  width: 100%;
  max-width: 420px;
  border-radius: 16px;
  overflow: hidden;
  border: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg);
  box-shadow: 0 18px 40px -26px rgba(10, 10, 12, 0.45);
}
.xt-shot img {
  display: block;
  width: 100%;
  height: auto;
}
.xt-vorb {
  opacity: 0.95;
}
.xt-text h3 {
  margin: 0;
  font-size: 26px;
  font-weight: 700;
  letter-spacing: -0.02em;
}
.xt-text p {
  margin: 12px 0 0;
  font-size: 17px;
  line-height: 1.75;
  color: var(--vp-c-text-2);
}
.xt-text p :deep(strong),
.xt-extra :deep(strong),
.xt-steps :deep(strong),
.xt-faq p :deep(strong) {
  color: var(--vp-c-text-1);
}
.xt-plans {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  margin-top: 36px;
}
.xt-plan {
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding: 28px 26px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 24px;
  background: var(--vp-c-bg-soft);
}
.xt-plan-name {
  font-size: 15px;
  font-weight: 600;
  color: var(--vp-c-text-2);
}
.xt-price {
  display: flex;
  align-items: baseline;
  gap: 4px;
}
.xt-yen {
  font-size: 22px;
  font-weight: 700;
}
.xt-num {
  font-size: clamp(48px, 8vw, 64px);
  font-weight: 800;
  letter-spacing: -0.04em;
  line-height: 1;
}
.xt-unit {
  margin-left: 4px;
  font-size: 15px;
  color: var(--vp-c-text-2);
}
.xt-plan-note {
  margin: 4px 0 0;
  font-size: 14px;
  line-height: 1.6;
  color: var(--vp-c-text-2);
}
.xt-addons {
  list-style: none;
  margin: 20px 0 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.xt-addons li {
  display: grid;
  grid-template-columns: auto auto 1fr;
  gap: 12px 16px;
  align-items: baseline;
  padding: 18px 22px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 18px;
}
.xt-addon-price {
  font-size: 18px;
  font-weight: 700;
  color: var(--tz-c-ink);
}
.dark .xt-addon-price {
  color: var(--vp-c-text-1);
}
.xt-theme {
  margin: 16px 0 0;
  text-align: center;
  font-size: 14px;
  color: var(--vp-c-text-2);
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
  color: var(--vp-c-text-2);
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
.xt-steps .n {
  display: grid;
  place-items: center;
  width: 34px;
  height: 34px;
  margin-bottom: 6px;
  border-radius: 50%;
  background: var(--tz-c-ink);
  color: var(--tz-c-on-ink);
  font-weight: 700;
  font-size: 15px;
}
.xt-steps strong {
  font-size: 17px;
}
.xt-steps li > span:last-child {
  font-size: 14px;
  line-height: 1.65;
  color: var(--vp-c-text-2);
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
  color: var(--vp-c-text-2);
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
.xt-end h2 {
  color: var(--tz-c-on-ink);
}
.xt-end > p {
  margin: 12px 0 28px;
  max-width: 560px;
  color: var(--tz-end-muted);
}
.xt-join {
  width: min(720px, 100%);
  margin-top: 36px;
  text-align: left;
}
.xt-join :deep(.tz-join) {
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  border-radius: 20px;
  padding: 20px;
}
.xt-join-hint {
  margin: 0 0 12px;
  font-size: 15px;
  font-weight: 600;
}
@media (max-width: 900px) {
  .xt-extras {
    grid-template-columns: 1fr 1fr;
  }
  .xt-feature {
    gap: 32px;
  }
  .xt-steps {
    grid-template-columns: 1fr;
  }
}
@media (max-width: 720px) {
  .xt-feature,
  .xt-plans {
    grid-template-columns: 1fr;
  }
  .xt-feature {
    gap: 18px;
  }
  .xt-feature.flip .xt-visual {
    order: 0;
  }
  .xt-visual {
    min-height: 220px;
  }
  .xt-features {
    gap: 40px;
  }
  .xt-sec {
    margin-top: 80px;
  }
  .xt-addons li {
    grid-template-columns: 1fr auto;
  }
  .xt-addons li > span:last-child {
    grid-column: 1 / -1;
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
  .xt {
    padding-left: 20px;
    padding-right: 20px;
  }
  .xt-end {
    padding: 40px 20px 48px;
  }
}
</style>
