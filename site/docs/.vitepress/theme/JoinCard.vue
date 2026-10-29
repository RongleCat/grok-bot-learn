<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { withBase } from 'vitepress'
import copyRoot from './funnel.json'
import { useLocaleJson } from './i18n'
const copy = useLocaleJson(copyRoot as Record<string, unknown>, 'funnel.json')
import { track, lastFrom } from './track'

const props = defineProps<{ from: string; xhs?: boolean }>()
const done = ref(false)
const qr = ref<HTMLElement | null>(null)
let io: IntersectionObserver | null = null
let timer: ReturnType<typeof setTimeout> | undefined

function fallback(text: string) {
  const t = document.createElement('textarea')
  t.value = text
  t.setAttribute('readonly', '')
  t.style.position = 'fixed'
  t.style.opacity = '0'
  document.body.appendChild(t)
  t.select()
  t.setSelectionRange(0, text.length)
  let ok = false
  try {
    ok = document.execCommand('copy')
  } catch {}
  document.body.removeChild(t)
  return ok
}

async function copyId() {
  let ok = false
  try {
    await navigator.clipboard.writeText('AI_Tiezhu')
    ok = true
  } catch {
    ok = fallback('AI_Tiezhu')
  }
  if (!ok) return
  done.value = true
  clearTimeout(timer)
  timer = setTimeout(() => (done.value = false), 2000)
  track('wechat-copy', { from: props.from, ref: lastFrom() })
}

onMounted(() => {
  if (!qr.value || !('IntersectionObserver' in window)) return
  io = new IntersectionObserver((list) => {
    if (list.some((x) => x.isIntersecting)) {
      track('wechat-qr-view', { from: props.from, ref: lastFrom() })
      io?.disconnect()
    }
  }, { threshold: 0.6 })
  io.observe(qr.value)
})
onBeforeUnmount(() => {
  io?.disconnect()
  clearTimeout(timer)
})
</script>

<template>
  <div class="tz-join" :class="{ card: xhs }">
    <div class="tz-join-text">
      <template v-if="xhs">
        <p class="tz-join-title">{{ copy.join_title }}</p>
        <p v-html="copy.join_text.replace(/`([^`]+)`/g, '<code>$1</code>')"></p>
        <p><strong>{{ copy.join_xhs }}</strong></p>
      </template>
      <slot v-else />
      <button type="button" class="tz-copy" :class="{ done }" @click="copyId">{{ done ? copy.copied : copy.copy_btn }}</button>
    </div>
    <div ref="qr" class="tz-join-side">
      <img class="tz-join-qr" :src="withBase('/qr-wechat.png')" width="168" height="168" alt="铁柱的个人微信二维码" />
      <p class="tz-qr-hint">{{ copy.qr_hint }}</p>
    </div>
  </div>
</template>
