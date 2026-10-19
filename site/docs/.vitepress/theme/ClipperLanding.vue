<script setup lang="ts">
import { withBase } from 'vitepress'
import GrokOrb from './GrokOrb.vue'
import copy from './ecosystem.json'
import links from './links.json'
import { rich, tidy } from './rich'
import { track } from './track'

const c = copy.clipper
const crew = [
  { shape: 'nuage', color: 'orange', size: 120 },
  { shape: 'goutte', color: 'violet', size: 112 },
  { shape: 'cercle', color: 'encre', size: 176 },
  { shape: 'hexagone', color: 'vert', size: 112 },
  { shape: 'squircle', color: 'bleu', size: 120 }
]
const skins = [
  { shape: 'squircle', color: 'bleu', tint: '#eaf3fe' },
  { shape: 'goutte', color: 'violet', tint: '#f1ebfe' },
  { shape: 'nuage', color: 'orange', tint: '#fef1e4' },
  { shape: 'hexagone', color: 'vert', tint: '#e6f8ef' },
  { shape: 'galet', color: 'rose', tint: '#fdeef3' },
  { shape: 'cercle', color: 'encre', tint: '#f4f4f5' }
]
const extraSkins = [
  { shape: 'capsule', color: 'bleu' },
  { shape: 'triangle', color: 'ambre' },
  { shape: 'squircle', color: 'turquoise' },
  { shape: 'hexagone', color: 'violet' }
]
const videos = [
  { src: '/ecosystem/clipper-demo-1.mp4', poster: '/ecosystem/clipper-demo-1.webp' },
  { src: '/ecosystem/clipper-demo-2.mp4', poster: '/ecosystem/clipper-demo-2.webp' }
]
const down = (from: string) => track('clipper-download', { from })
</script>

<template>
  <div class="cl">
    <section class="cl-hero">
      <span class="cl-meta">{{ c.meta }}</span>
      <h1>Grok Bot Clipper</h1>
      <p class="cl-slogan tz-tidy">{{ tidy(c.slogan) }}</p>
      <p class="cl-lead tz-tidy">{{ tidy(c.lead) }}</p>
      <div class="cl-actions">
        <a class="cl-btn primary" :href="links.clipperDownload" target="_blank" rel="noopener" @click="down('hero')">
          <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path d="M12 3v12m0 0-5-5m5 5 5-5M4 19h16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" /></svg>
          {{ c.download }}
        </a>
        <a class="cl-btn" :href="links.clipperRepo" target="_blank" rel="noopener">{{ c.source }}</a>
      </div>
      <p class="cl-unofficial tz-tidy">{{ tidy(c.unofficial) }}</p>
      <div class="cl-crew">
        <GrokOrb v-for="(o, i) in crew" :key="i" class="cl-bob" :style="{ animationDelay: `${i * 0.5}s` }" :size="o.size" :shape="o.shape" :color="o.color" :playful="i === 2" />
      </div>
    </section>

    <section class="cl-sec">
      <h2>{{ c.videoTitle }}</h2>
      <p class="cl-sub tz-tidy">{{ tidy(c.videoLead) }}</p>
      <div class="cl-videos">
        <figure v-for="(v, i) in videos" :key="v.src" class="cl-video">
          <div class="cl-frame">
            <span class="cl-dots"><i></i><i></i><i></i></span>
            <video controls preload="none" playsinline :poster="withBase(v.poster)" width="1008" height="720">
              <source :src="withBase(v.src)" type="video/mp4" />
            </video>
          </div>
          <figcaption>{{ c.videos[i].title }}</figcaption>
        </figure>
      </div>
    </section>

    <section class="cl-sec">
      <h2>{{ c.featuresTitle }}</h2>
      <div class="cl-features">
        <div v-for="(f, i) in c.features" :key="f.k" class="cl-feature" :class="{ flip: i % 2 === 1 }">
          <div class="cl-visual" :style="{ background: skins[i].tint }" aria-hidden="true">
            <div v-if="i === 0" class="mk mk-page">
              <span class="ln w90"></span><span class="ln w70"></span>
              <span class="pick"><span class="ln w80"></span><span class="ln w60"></span></span>
              <span class="ln w85"></span><span class="ln w50"></span>
            </div>
            <div v-else-if="i === 1" class="mk mk-page">
              <span class="ln w90"></span><span class="ln w60"></span>
              <span class="crop"><span class="mosaic"></span><span class="pen"></span></span>
              <span class="ln w75"></span>
            </div>
            <div v-else-if="i === 2" class="mk mk-post">
              <span class="head"><span class="av"></span><span class="ln w40"></span></span>
              <span class="ln w90"></span><span class="ln w70"></span>
              <span class="img"></span>
              <span class="bar"><span></span><span></span><span></span><span class="on"></span></span>
            </div>
            <div v-else-if="i === 3" class="mk mk-basket">
              <span class="chip c1"></span><span class="chip c2"></span><span class="chip c3"></span>
              <span class="bin"></span>
            </div>
            <div v-else-if="i === 4" class="mk mk-page">
              <span class="ln w50 bold"></span><span class="ln w90"></span><span class="ln w80"></span>
              <span class="files"><span></span><span></span><span></span></span>
              <span class="ok"></span>
            </div>
            <div v-else class="mk mk-split">
              <span class="left"><span class="ln w90"></span><span class="ln w70"></span><span class="ln w85"></span><span class="ln w60"></span></span>
              <span class="right"><span class="bub me"></span><span class="bub"></span><span class="bub me s"></span></span>
            </div>
            <GrokOrb class="cl-vorb" :size="96" :shape="skins[i].shape" :color="skins[i].color" />
          </div>
          <div class="cl-text">
            <h3>{{ f.k }}</h3>
            <p v-html="rich(f.v)"></p>
          </div>
        </div>
      </div>
    </section>

    <section class="cl-sec">
      <h2>{{ c.extrasTitle }}</h2>
      <div class="cl-extras">
        <div v-for="(e, i) in c.extras" :key="e.k" class="cl-extra">
          <GrokOrb :size="56" :shape="extraSkins[i].shape" :color="extraSkins[i].color" />
          <strong>{{ e.k }}</strong>
          <span>{{ e.v }}</span>
        </div>
      </div>
    </section>

    <section class="cl-sec">
      <h2>{{ c.stepsTitle }}</h2>
      <ol class="cl-steps">
        <li v-for="(s, i) in c.steps" :key="s.k">
          <span class="n">{{ i + 1 }}</span>
          <strong>{{ s.k }}</strong>
          <span>{{ s.v }}</span>
        </li>
      </ol>
    </section>

    <section class="cl-sec cl-faqsec">
      <h2>{{ c.faqTitle }}</h2>
      <div class="cl-faq">
        <details v-for="(f, i) in c.faq" :key="f.q" :open="i === 0">
          <summary>{{ f.q }}</summary>
          <p v-html="rich(f.a)"></p>
        </details>
      </div>
    </section>

    <section class="cl-sec">
      <div class="cl-end">
        <img :src="withBase('/ecosystem/clipper-avatars.webp')" alt="" width="1200" height="227" decoding="async" />
        <h2>{{ c.endTitle }}</h2>
        <p>{{ c.endText }}</p>
        <a class="cl-btn light" :href="links.clipperDownload" target="_blank" rel="noopener" @click="down('end')">{{ c.endBtn }}</a>
      </div>
    </section>
  </div>
</template>

<style scoped>
.cl {
  max-width: 1120px;
  margin: 0 auto;
  padding: 24px 24px 96px;
}
.cl-hero {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 48px 0 8px;
}
.cl-meta {
  padding: 6px 14px;
  border-radius: 999px;
  background: var(--vp-c-bg-soft);
  font-size: 13px;
  color: var(--vp-c-text-2);
}
.cl-hero h1 {
  margin: 22px 0 0;
  font-size: clamp(44px, 8vw, 88px);
  line-height: 1;
  font-weight: 800;
  letter-spacing: -0.045em;
}
.cl-slogan {
  margin: 22px 0 0;
  font-size: clamp(22px, 3.4vw, 32px);
  font-weight: 700;
  letter-spacing: -0.02em;
  line-height: 1.3;
}
.cl-lead {
  max-width: 560px;
  margin: 14px 0 0;
  font-size: 17px;
  line-height: 1.7;
  color: var(--vp-c-text-2);
}
.cl-actions {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 12px;
  margin-top: 32px;
}
.cl-btn {
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
.cl-btn:hover {
  transform: translateY(-1px);
  background: var(--vp-c-bg-soft);
}
.cl-btn.primary {
  background: #0a0a0c;
  border-color: #0a0a0c;
  color: #fff;
  box-shadow: 0 12px 28px -14px rgba(10, 10, 12, 0.6);
}
.cl-btn.primary:hover {
  background: #2a2a2e;
}
.cl-btn.light {
  background: #fff;
  border-color: #fff;
  color: #0a0a0c;
}
.cl-unofficial {
  margin: 16px 0 0;
  font-size: 13px;
  color: var(--vp-c-text-3);
}
.cl-crew {
  display: flex;
  align-items: flex-end;
  justify-content: center;
  gap: clamp(0px, 2vw, 28px);
  margin-top: 40px;
  min-height: 190px;
}
.cl-bob {
  animation: cl-bob 5s ease-in-out infinite;
}
@keyframes cl-bob {
  50% {
    transform: translateY(-12px);
  }
}
.cl-sec {
  margin-top: 104px;
}
.cl-sec h2 {
  margin: 0;
  text-align: center;
  font-size: clamp(26px, 3.6vw, 36px);
  font-weight: 700;
  letter-spacing: -0.025em;
}
.cl-sub {
  margin: 12px 0 0;
  text-align: center;
  color: var(--vp-c-text-2);
}
.cl-videos {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
  margin-top: 36px;
}
.cl-video {
  margin: 0;
}
.cl-frame {
  border: 1px solid var(--vp-c-divider);
  border-radius: 20px;
  overflow: hidden;
  background: #0a0a0c;
  box-shadow: 0 24px 60px -36px rgba(10, 10, 12, 0.5);
}
.cl-dots {
  display: flex;
  gap: 6px;
  padding: 10px 14px;
  background: #f4f4f5;
}
.cl-dots i {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #d9d9de;
}
.cl-frame video {
  display: block;
  width: 100%;
  height: auto;
  aspect-ratio: 1008 / 720;
  background: #0a0a0c;
}
.cl-video figcaption {
  margin-top: 12px;
  text-align: center;
  font-size: 15px;
  font-weight: 600;
}
.cl-features {
  display: flex;
  flex-direction: column;
  gap: 28px;
  margin-top: 40px;
}
.cl-feature {
  display: grid;
  grid-template-columns: 1.1fr 1fr;
  align-items: center;
  gap: 56px;
}
.cl-feature.flip .cl-visual {
  order: 2;
}
.cl-visual {
  position: relative;
  display: grid;
  place-items: center;
  height: 280px;
  border-radius: 28px;
  overflow: hidden;
}
.cl-vorb {
  position: absolute;
  right: 10px;
  bottom: 6px;
}
.cl-text h3 {
  margin: 0;
  font-size: 26px;
  font-weight: 700;
  letter-spacing: -0.02em;
}
.cl-text p {
  margin: 12px 0 0;
  font-size: 17px;
  line-height: 1.75;
  color: var(--vp-c-text-2);
}
.cl-text p :deep(strong) {
  color: var(--vp-c-text-1);
}
.mk {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 10px;
  width: 62%;
  padding: 22px;
  border-radius: 18px;
  background: #fff;
  box-shadow: 0 18px 40px -26px rgba(10, 10, 12, 0.45);
}
.ln {
  display: block;
  height: 9px;
  border-radius: 6px;
  background: #e7e7ea;
}
.ln.bold {
  height: 12px;
  background: #cfcfd4;
}
.w40 { width: 40%; }
.w50 { width: 50%; }
.w60 { width: 60%; }
.w70 { width: 70%; }
.w75 { width: 75%; }
.w80 { width: 80%; }
.w85 { width: 85%; }
.w90 { width: 90%; }
.pick {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin: 0 -8px;
  padding: 8px;
  border-radius: 8px;
  background: rgba(59, 147, 240, 0.16);
  outline: 2px solid #3b93f0;
}
.pick .ln {
  background: #9cc6f5;
}
.crop {
  position: relative;
  height: 66px;
  border: 2px dashed #8b5cf6;
  border-radius: 8px;
}
.mosaic {
  position: absolute;
  left: 12px;
  top: 12px;
  width: 44%;
  height: 38px;
  border-radius: 4px;
  background: repeating-conic-gradient(#c9b6f8 0 25%, #e6dcfd 0 50%) 0 0 / 12px 12px;
}
.pen {
  position: absolute;
  right: 14px;
  top: 18px;
  width: 30%;
  height: 26px;
  border: 3px solid #f2852b;
  border-radius: 50%;
}
.mk-post .head {
  display: flex;
  align-items: center;
  gap: 10px;
}
.mk-post .av {
  width: 26px;
  height: 26px;
  border-radius: 50%;
  background: #f2a25c;
}
.mk-post .head .ln {
  flex: 1;
  max-width: 40%;
}
.mk-post .img {
  height: 70px;
  border-radius: 10px;
  background: linear-gradient(135deg, #fde3c8, #fbc89a);
}
.mk-post .bar {
  display: flex;
  justify-content: space-between;
  padding-top: 4px;
}
.mk-post .bar span {
  width: 18px;
  height: 18px;
  border-radius: 6px;
  background: #e7e7ea;
}
.mk-post .bar .on {
  background: #0a0a0c;
}
.mk-basket {
  height: 190px;
  background: transparent;
  box-shadow: none;
  padding: 0;
}
.mk-basket .chip {
  position: absolute;
  width: 46%;
  height: 52px;
  border-radius: 12px;
  background: #fff;
  box-shadow: 0 12px 26px -18px rgba(10, 10, 12, 0.5);
}
.mk-basket .c1 { left: 6%; top: 0; transform: rotate(-8deg); }
.mk-basket .c2 { left: 30%; top: 14px; transform: rotate(4deg); border-top: 6px solid #3fcf8e; }
.mk-basket .c3 { left: 52%; top: 2px; transform: rotate(10deg); border-top: 6px solid #3b93f0; }
.mk-basket .bin {
  position: absolute;
  left: 10%;
  right: 10%;
  bottom: 0;
  height: 96px;
  border-radius: 14px 14px 28px 28px;
  background: #3fcf8e;
  box-shadow: inset 0 10px 0 rgba(255, 255, 255, 0.35);
}
.mk-page .files {
  display: flex;
  gap: 8px;
}
.mk-page .files span {
  width: 54px;
  height: 40px;
  border-radius: 8px;
  background: #fbd3e1;
}
.mk-page .ok {
  position: absolute;
  right: -14px;
  top: -14px;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: #16a34a;
}
.mk-page .ok::after {
  content: '';
  position: absolute;
  left: 12px;
  top: 8px;
  width: 9px;
  height: 15px;
  border: solid #fff;
  border-width: 0 3px 3px 0;
  transform: rotate(45deg);
}
.mk-split {
  flex-direction: row;
  gap: 14px;
  width: 70%;
}
.mk-split .left {
  display: flex;
  flex: 1;
  flex-direction: column;
  gap: 10px;
}
.mk-split .right {
  display: flex;
  flex-direction: column;
  gap: 8px;
  width: 40%;
  padding-left: 14px;
  border-left: 1px solid #ececee;
}
.bub {
  display: block;
  height: 24px;
  width: 90%;
  border-radius: 10px 10px 10px 2px;
  background: #ececee;
}
.bub.me {
  align-self: flex-end;
  width: 70%;
  border-radius: 10px 10px 2px 10px;
  background: #0a0a0c;
}
.bub.s {
  width: 46%;
}
.cl-extras {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  margin-top: 36px;
}
.cl-extra {
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding: 22px;
  border-radius: 22px;
  background: var(--vp-c-bg-soft);
}
.cl-extra strong {
  font-size: 17px;
}
.cl-extra span {
  font-size: 14px;
  line-height: 1.65;
  color: var(--vp-c-text-2);
}
.cl-steps {
  list-style: none;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  margin: 36px 0 0;
  padding: 0;
}
.cl-steps li {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 24px 22px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 22px;
}
.cl-steps .n {
  display: grid;
  place-items: center;
  width: 34px;
  height: 34px;
  margin-bottom: 6px;
  border-radius: 50%;
  background: #0a0a0c;
  color: #fff;
  font-weight: 700;
  font-size: 15px;
}
.cl-steps strong {
  font-size: 17px;
}
.cl-steps li > span:last-child {
  font-size: 14px;
  line-height: 1.65;
  color: var(--vp-c-text-2);
}
.cl-faq {
  max-width: 760px;
  margin: 32px auto 0;
  border-top: 1px solid var(--vp-c-divider);
}
.cl-faq details {
  border-bottom: 1px solid var(--vp-c-divider);
}
.cl-faq summary {
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
.cl-faq summary::-webkit-details-marker {
  display: none;
}
.cl-faq summary::after {
  content: '+';
  flex: none;
  font-size: 22px;
  font-weight: 400;
  color: var(--vp-c-text-3);
  transition: transform 0.2s;
}
.cl-faq details[open] summary::after {
  transform: rotate(45deg);
}
.cl-faq p {
  margin: 0;
  padding: 0 4px 20px;
  font-size: 15px;
  line-height: 1.75;
  color: var(--vp-c-text-2);
}
.cl-faq p :deep(strong) {
  color: var(--vp-c-text-1);
}
.cl-end {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 48px 32px 56px;
  border-radius: 32px;
  background: #0a0a0c;
  color: #fff;
}
.cl-end img {
  width: min(420px, 90%);
  height: auto;
  padding: 14px 20px;
  border-radius: 20px;
  background: #fff;
}
.cl-end h2 {
  margin-top: 28px;
  color: #fff;
}
.cl-end p {
  margin: 12px 0 28px;
  color: #b5b5bb;
}
@media (max-width: 900px) {
  .cl-extras,
  .cl-steps {
    grid-template-columns: 1fr 1fr;
  }
  .cl-feature {
    gap: 32px;
  }
}
@media (max-width: 720px) {
  .cl-videos,
  .cl-feature {
    grid-template-columns: 1fr;
  }
  .cl-feature {
    gap: 18px;
  }
  .cl-feature.flip .cl-visual {
    order: 0;
  }
  .cl-visual {
    height: 220px;
  }
  .cl-vorb {
    transform: scale(0.75);
    transform-origin: bottom right;
    right: 14px;
    bottom: 12px;
  }
  .cl-features {
    gap: 40px;
  }
  .cl-sec {
    margin-top: 80px;
  }
}
@media (max-width: 520px) {
  .cl-extras,
  .cl-steps {
    grid-template-columns: 1fr;
  }
  .cl-crew {
    zoom: 0.5;
    margin-top: 48px;
  }
  .mk {
    width: 74%;
    padding: 16px;
  }
  .mk-split {
    width: 82%;
  }
  .cl-btn {
    padding: 12px 22px;
    font-size: 15px;
  }
  .cl {
    padding-left: 20px;
    padding-right: 20px;
  }
}
@media (max-width: 360px) {
  .cl-crew {
    zoom: 0.44;
  }
}
</style>
