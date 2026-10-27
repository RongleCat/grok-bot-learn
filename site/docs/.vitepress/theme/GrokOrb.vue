<script setup lang="ts">
import { computed, onBeforeUnmount, onMounted, ref, shallowRef, triggerRef, useId } from 'vue'
import { COLOR_BY_ID, SHAPE_BY_ID, mixHex } from './bot/skins'
import { EXPRESSION_BY_ID } from './bot/expressions'
import { BotEngine, type BotFrame } from './bot/engine'
import { clamp, easings } from './bot/math'
import { lookTarget, TURN_TIME } from './bot/gaze'
import { DEMI_VIEWBOX, RAYON } from './bot/repere'
import { STATE_BY_ID, type StateId } from './bot/states'
import { NOTIF_BLUE } from './bot/decor'

const props = withDefaults(defineProps<{ size?: number; playful?: boolean; shape?: string; color?: string; expression?: string }>(), { size: 32, playful: false, shape: 'cercle', color: 'encre', expression: '' })

const R = RAYON
const VB = DEMI_VIEWBOX
const ink = computed(() => COLOR_BY_ID.get(props.color)?.hex ?? '#0a0a0c')
const paper = computed(() => '#ffffff')
const uid = (useId() ?? 'o').replace(/[^a-zA-Z0-9-]/g, '')
const maskId = `orb-${uid}`
const engine = new BotEngine(R, 'idle', SHAPE_BY_ID.get(props.shape)?.radii ?? null, EXPRESSION_BY_ID.get(props.expression) ?? null)
const frame = shallowRef<BotFrame>(engine.sample(0))
const svg = ref<SVGSVGElement | null>(null)
const state = ref<StateId>('idle')

let raf = 0
let last = 0
let clock = 0
let pointer: { x: number; y: number } | null = null
let aiming = false
let turnSince = 0
let backAt = Infinity
let nextIdleFx = 6

const tricks: StateId[] = ['wink', 'orbit', 'swirl', 'burst', 'wide', 'thinking']
let trick = 0

function go(id: StateId, hold: number) {
  state.value = id
  engine.setState(id, clock)
  backAt = clock + hold
}

function onMove(e: PointerEvent) {
  if (e.pointerType === 'touch') return
  pointer = { x: e.clientX, y: e.clientY }
}

function onLeave() {
  pointer = null
}

function onClick() {
  go(tricks[trick % tricks.length], 2.2)
  trick++
}

function aim() {
  if (!STATE_BY_ID.get(state.value)?.baseFace) {
    if (aiming) engine.setLook(null, clock, TURN_TIME)
    aiming = false
    return
  }
  const box = svg.value?.getBoundingClientRect()
  if (!box || box.width === 0) return
  if (!aiming) turnSince = clock
  const hw = Math.max(1, window.innerWidth / 2)
  const hh = Math.max(1, window.innerHeight / 2)
  engine.setLook(
    lookTarget({
      nx: pointer ? clamp((pointer.x - (box.left + box.width / 2)) / hw, -1, 1) : 0,
      ny: pointer ? clamp((pointer.y - (box.top + box.height / 2)) / hh, -1, 1) : 0,
      tour: easings.easeOutQuint(clamp((clock - turnSince) / TURN_TIME)),
      pointer: pointer !== null
    }),
    clock
  )
  aiming = true
}

function tick(ms: number) {
  raf = requestAnimationFrame(tick)
  const dt = last ? Math.min((ms - last) / 1000, 0.064) : 0
  last = ms
  clock += dt
  if (clock >= backAt) {
    backAt = Infinity
    state.value = 'idle'
    engine.setState('idle', clock)
  }
  if (props.playful && state.value === 'idle' && clock >= nextIdleFx) {
    go('wink', 1.2)
    nextIdleFx = clock + 9 + Math.random() * 6
  }
  aim()
  frame.value = engine.sample(clock)
  triggerRef(frame)
}

onMounted(() => {
  window.addEventListener('pointermove', onMove)
  document.addEventListener('pointerleave', onLeave)
  raf = requestAnimationFrame(tick)
})

onBeforeUnmount(() => {
  cancelAnimationFrame(raf)
  window.removeEventListener('pointermove', onMove)
  document.removeEventListener('pointerleave', onLeave)
})

function dotAttrs(dot: BotFrame['dots'][number]) {
  const fill = dot.color ?? (dot.depth === undefined ? ink.value : mixHex(paper.value, ink.value, dot.depth))
  const common = { fill, opacity: dot.opacity }
  return dot.d
    ? { ...common, d: dot.d, transform: `translate(${dot.x} ${dot.y}) rotate(${dot.rot ?? 0}) scale(${R})` }
    : { ...common, cx: dot.x, cy: dot.y, r: dot.r }
}
</script>

<template>
  <svg ref="svg" class="grok-orb" :data-ink="props.color" :width="props.size" :height="props.size" :viewBox="`${-VB} ${-VB} ${VB * 2} ${VB * 2}`" role="img" aria-label="Grok Bot" @click="onClick">
    <defs>
      <mask :id="maskId" maskUnits="userSpaceOnUse" :x="-VB" :y="-VB" :width="VB * 2" :height="VB * 2">
        <path :d="frame.bodyPath" fill="#fff" />
        <path v-for="(eye, i) in frame.eyes" :key="i" :d="eye.d" :transform="eye.matrix" :opacity="eye.alpha" fill="#000" />
        <circle v-if="frame.notch" :cx="frame.notch.x" :cy="frame.notch.y" :r="frame.notch.r" fill="#000" />
      </mask>
      <linearGradient v-for="arc in frame.arcs" :id="`${uid}-${arc.id}`" :key="arc.id" gradientUnits="userSpaceOnUse" :x1="arc.grad.x1" :y1="arc.grad.y1" :x2="arc.grad.x2" :y2="arc.grad.y2">
        <stop v-for="(c, i) in arc.grad.stops" :key="i" :offset="i / (arc.grad.stops.length - 1)" :stop-color="c" />
      </linearGradient>
    </defs>
    <g fill="none" stroke-linecap="round">
      <path v-for="arc in frame.arcs" :key="`b${arc.id}`" :d="arc.back" :stroke="`url(#${uid}-${arc.id})`" :stroke-width="arc.width" :opacity="arc.opacity" />
    </g>
    <g v-if="frame.dotsBehind">
      <component :is="dot.d ? 'path' : 'circle'" v-for="(dot, i) in frame.dots" :key="`pb${i}`" v-bind="dotAttrs(dot)" />
    </g>
    <g :opacity="frame.bodyAlpha">
      <path :d="frame.bodyPath" :fill="paper" />
      <g :mask="`url(#${maskId})`">
        <rect :x="-VB" :y="-VB" :width="VB * 2" :height="VB * 2" :fill="ink" />
      </g>
    </g>
    <g v-if="!frame.dotsBehind">
      <component :is="dot.d ? 'path' : 'circle'" v-for="(dot, i) in frame.dots" :key="`pf${i}`" v-bind="dotAttrs(dot)" />
    </g>
    <circle v-if="frame.notif" :cx="frame.notif.x" :cy="frame.notif.y" :r="frame.notif.r" :fill="NOTIF_BLUE" />
    <g fill="none" stroke-linecap="round">
      <path v-for="arc in frame.arcs" :key="`f${arc.id}`" :d="arc.front" :stroke="`url(#${uid}-${arc.id})`" :stroke-width="arc.width" :opacity="arc.opacity" />
    </g>
  </svg>
</template>

<style scoped>
.grok-orb {
  cursor: pointer;
  display: block;
  overflow: visible;
}
.dark .grok-orb[data-ink='encre'] {
  filter: invert(1);
}
</style>
