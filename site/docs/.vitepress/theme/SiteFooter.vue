<script setup lang="ts">
import { withBase } from 'vitepress'
import { useSidebar } from 'vitepress/theme'
const { hasSidebar } = useSidebar()
</script>

<template>
  <footer class="tz-footer" :class="{ 'has-sidebar': hasSidebar }">
    <div class="tz-footer-inner">
      <div class="tz-footer-links">
        <span class="tz-item">公众号「铁柱AGI」</span>
        <a class="tz-item" href="https://x.com/cgnot996" target="_blank" rel="noopener">X @cgnot996</a>
        <a class="tz-item" :href="withBase('/group')">答疑群<span class="tz-sub">进群聊 AI Agent</span></a>
      </div>
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
    padding-left: calc((100% - (var(--vp-layout-max-width) - 64px)) / 2 + var(--vp-sidebar-width) - 32px + 32px);
  }
}
.tz-footer-inner {
  max-width: 960px;
  margin: 0 auto;
  text-align: center;
}
.tz-footer-links {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 10px 28px;
  font-size: 14px;
  color: var(--vp-c-text-1);
}
.tz-item {
  display: inline-flex;
  align-items: baseline;
  gap: 8px;
}
a.tz-item {
  color: #2563eb;
  font-weight: 600;
  text-decoration: none;
}
a.tz-item:hover {
  text-decoration: underline;
  text-underline-offset: 3px;
}
.dark a.tz-item {
  color: #60a5fa;
}
.tz-sub {
  font-weight: 400;
  font-size: 13px;
  color: var(--vp-c-text-2);
}
.tz-note {
  margin: 14px 0 0;
  font-size: 12px;
  color: var(--vp-c-text-3);
}
</style>
