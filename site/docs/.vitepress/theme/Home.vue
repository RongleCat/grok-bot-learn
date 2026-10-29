<script setup lang="ts">
import GrokOrb from './GrokOrb.vue'
import copyRoot from './home.json'
import { useLocaleJson, useLocalePath } from './i18n'
const copy = useLocaleJson(copyRoot as Record<string, unknown>, 'home.json')
const localePath = useLocalePath()

const partSkins = [
  { shape: 'squircle', color: 'bleu' },
  { shape: 'nuage', color: 'orange' },
  { shape: 'hexagone', color: 'vert' },
  { shape: 'triangle', color: 'violet' }
]
const roleSkins = [
  { shape: 'galet', color: 'rouge' },
  { shape: 'capsule', color: 'bleu' },
  { shape: 'goutte', color: 'ambre' },
  { shape: 'squircle', color: 'turquoise' },
  { shape: 'nuage', color: 'rose' },
  { shape: 'hexagone', color: 'encre' }
]
const loopSkins = [
  { shape: 'cercle', color: 'encre' },
  { shape: 'galet', color: 'orange' },
  { shape: 'squircle', color: 'vert' },
  { shape: 'nuage', color: 'violet' }
]
const friends = [
  { shape: 'squircle', color: 'bleu', size: 54, x: -250, y: -40 },
  { shape: 'triangle', color: 'ambre', size: 44, x: -170, y: 70 },
  { shape: 'nuage', color: 'rose', size: 50, x: 190, y: -60 },
  { shape: 'hexagone', color: 'vert', size: 46, x: 250, y: 50 },
  { shape: 'goutte', color: 'orange', size: 38, x: -120, y: -95 },
  { shape: 'capsule', color: 'violet', size: 40, x: 130, y: 95 }
]
const segs = (s: string) => s.match(/[^，。；！？]+[，。；！？]*/g) || [s]
</script>

<template>
  <div class="gh">
    <section class="gh-hero">
      <div class="gh-stage">
        <GrokOrb v-for="(f, i) in friends" :key="i" class="gh-friend" :style="{ transform: `translate(${f.x}px, ${f.y}px)`, animationDelay: `${i * 0.6}s` }" :size="f.size" :shape="f.shape" :color="f.color" />
        <GrokOrb :size="168" playful class="gh-orb" />
      </div>
      <h1>{{ copy.title }}</h1>
      <p class="gh-lead"><span v-for="(t, i) in segs(copy.lead)" :key="i" class="gh-seg">{{ t }}</span></p>
      <div class="gh-actions">
        <a class="gh-btn primary" :href="localePath('/part1/01-what-is')">{{ copy.primary }}</a>
        <a class="gh-btn" :href="localePath('/cases/')">{{ copy.secondary }}</a>
      </div>
      <a class="gh-notice" :href="localePath('/part1/02-plans')">
        <span class="dot"></span>
        <span class="gh-notice-text"><span v-for="(t, i) in segs(copy.notice)" :key="i" class="gh-seg">{{ t }}</span></span>
        <span class="arrow">→</span>
      </a>
    </section>

    <section class="gh-sec">
      <h2>{{ copy.partsTitle }}</h2>
      <div class="gh-parts">
        <a v-for="(p, i) in copy.parts" :key="p.name" class="gh-part" :data-i="i" :href="localePath(p.link)">
          <GrokOrb :size="56" :shape="partSkins[i].shape" :color="partSkins[i].color" />
          <span class="tag">{{ p.tag }}</span>
          <strong>{{ p.name }}</strong>
          <span class="desc">{{ p.desc }}</span>
        </a>
      </div>
    </section>

    <section class="gh-sec">
      <h2>{{ copy.asksTitle }}</h2>
      <div class="gh-asks">
        <a v-for="a in copy.asks" :key="a.q" class="gh-ask" :href="localePath(a.link)">{{ a.q }}<span>→</span></a>
      </div>
    </section>

    <section class="gh-sec">
      <div class="gh-group" data-from="home">
        <div>
          <h2>{{ copy.groupTitle }}</h2>
          <p>{{ copy.groupText }}</p>
        </div>
        <a class="gh-btn primary" :href="localePath('/group')">{{ copy.groupBtn }}</a>
      </div>
    </section>

    <section class="gh-sec">
      <h2>{{ copy.loopTitle }}</h2>
      <ol class="gh-loop">
        <li v-for="(s, i) in copy.loop" :key="s.k">
          <GrokOrb :size="40" :shape="loopSkins[i].shape" :color="loopSkins[i].color" />
          <span class="n">0{{ i + 1 }}</span>
          <strong>{{ s.k }}</strong>
          <span class="desc">{{ s.v }}</span>
        </li>
      </ol>
    </section>

    <section class="gh-sec">
      <h2>{{ copy.rolesTitle }}</h2>
      <div class="gh-roles">
        <a v-for="(r, i) in copy.roles" :key="r.name" class="gh-role" :href="localePath(r.link)">
          <GrokOrb :size="44" :shape="roleSkins[i].shape" :color="roleSkins[i].color" />
          <strong>{{ r.name }}</strong>
          <span class="desc">{{ r.desc }}</span>
        </a>
      </div>
    </section>

    <section class="gh-sec">
      <div class="gh-head">
        <h2>{{ copy.casesTitle }}</h2>
        <a :href="localePath('/cases/')">{{ copy.casesMore }} →</a>
      </div>
      <ol class="gh-cases">
        <li v-for="(c, i) in copy.cases" :key="c.t">
          <a :href="localePath(c.link)">
            <span class="n">{{ String(i + 1).padStart(2, '0') }}</span>
            <span class="t">{{ c.t }}</span>
            <span class="a">{{ c.a }}</span>
          </a>
        </li>
      </ol>
    </section>
  </div>
</template>
