<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { withBase } from 'vitepress'
import { useSidebar } from 'vitepress/theme'

const { hasSidebar } = useSidebar()
const open = ref(false)
const root = ref<HTMLElement | null>(null)
let hover = false

const enter = () => { if (hover) open.value = true }
const leave = () => { if (hover) open.value = false }
const toggle = () => { open.value = !open.value }
const outside = (e: PointerEvent) => {
  if (open.value && root.value && !root.value.contains(e.target as Node)) open.value = false
}
const esc = (e: KeyboardEvent) => { if (e.key === 'Escape') open.value = false }

onMounted(() => {
  hover = window.matchMedia('(hover: hover) and (pointer: fine)').matches
  document.addEventListener('pointerdown', outside)
  document.addEventListener('keydown', esc)
})
onBeforeUnmount(() => {
  document.removeEventListener('pointerdown', outside)
  document.removeEventListener('keydown', esc)
})
</script>

<template>
  <footer class="tz-footer" :class="{ 'has-sidebar': hasSidebar }">
    <div class="tz-inner">
      <nav class="tz-links">
        <div ref="root" class="tz-mp" @mouseenter="enter" @mouseleave="leave">
          <button type="button" class="tz-link" :aria-expanded="open" aria-haspopup="true" @click="toggle">公众号「铁柱AGI」</button>
          <div v-show="open" class="tz-pop" role="dialog" aria-label="公众号「铁柱AGI」二维码">
            <img :src="withBase('/mp-search.png')" width="720" height="262" alt="微信搜一搜：铁柱AGI" />
          </div>
        </div>
        <span class="tz-sep" aria-hidden="true"></span>
        <a class="tz-link" href="https://x.com/cgnot996" target="_blank" rel="noopener">X @cgnot996</a>
        <span class="tz-sep" aria-hidden="true"></span>
        <a class="tz-link" :href="withBase('/group')">答疑群</a>
        <span class="tz-sep" aria-hidden="true"></span>
        <a class="tz-link" :href="withBase('/about')">关于作者</a>
      </nav>
      <p class="tz-note">本站是社区非官方学习站，非 xAI 官方。</p>
    </div>
  </footer>
</template>

<style scoped>
.tz-footer {
  border-top: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg);
  padding: 28px 24px 32px;
  position: relative;
  z-index: 1;
}
@media (min-width: 960px) {
  .tz-footer.has-sidebar {
    padding-left: calc(var(--vp-sidebar-width) + 32px);
  }
}
@media (min-width: 1440px) {
  .tz-footer.has-sidebar {
    padding-left: calc((100% - (var(--vp-layout-max-width) - 64px)) / 2 + var(--vp-sidebar-width));
  }
}
.tz-inner {
  max-width: 720px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
}
.tz-links {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  gap: 8px 20px;
}
.tz-link {
  font: inherit;
  font-size: 14px;
  line-height: 24px;
  font-weight: 500;
  color: var(--vp-c-text-1);
  background: none;
  border: 0;
  padding: 0;
  cursor: pointer;
  text-decoration: none;
  transition: color 0.2s;
}
.tz-link:hover,
.tz-link[aria-expanded='true'] {
  color: #2563eb;
}
.tz-sep {
  width: 1px;
  height: 12px;
  background: var(--vp-c-divider);
}
.tz-mp {
  position: relative;
  display: inline-flex;
}
.tz-pop {
  position: absolute;
  bottom: calc(100% + 12px);
  left: 50%;
  transform: translateX(-50%);
  width: max-content;
  padding: 10px;
  background: #fff;
  border: 1px solid var(--vp-c-divider);
  border-radius: 12px;
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.12);
  z-index: 20;
}
.tz-pop::after {
  content: '';
  position: absolute;
  top: 100%;
  left: 50%;
  width: 10px;
  height: 10px;
  background: #fff;
  border-right: 1px solid var(--vp-c-divider);
  border-bottom: 1px solid var(--vp-c-divider);
  transform: translate(-50%, -5px) rotate(45deg);
}
.tz-pop::before {
  content: '';
  position: absolute;
  left: 0;
  right: 0;
  top: 100%;
  height: 14px;
}
.tz-pop img {
  display: block;
  max-width: none;
  width: 300px;
  height: auto;
  border-radius: 6px;
}
.tz-note {
  margin: 0;
  font-size: 12px;
  line-height: 18px;
  color: var(--vp-c-text-3);
}
@media (max-width: 480px) {
  .tz-links {
    gap: 8px 14px;
  }
  .tz-link {
    font-size: 13px;
  }
  .tz-pop {
    left: 0;
    transform: none;
    padding: 8px;
  }
  .tz-pop::after {
    left: 48px;
  }
  .tz-pop img {
    width: min(260px, calc(100vw - 48px));
  }
}
</style>
