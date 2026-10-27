<!--
  A filled "block" arrow like PowerPoint's Right/Left/Up/Down Arrow shapes.

  Usage (all numbers are px on the 980 x 551 slide canvas):
    <BlockArrow dir="right" x="300" y="200" w="180" h="45" color="#FF0000" />

  adj1 = shaft thickness (% of the arrow's height/width), default 50
  adj2 = head length (% of the shorter side), default 50
-->
<script setup lang="ts">
import { computed } from 'vue'

const props = withDefaults(defineProps<{
  dir?: 'right' | 'left' | 'up' | 'down'
  x: number | string
  y: number | string
  w: number | string
  h: number | string
  color?: string
  adj1?: number | string
  adj2?: number | string
  rotate?: number | string
}>(), {
  dir: 'right',
  color: '#FF0000',
  adj1: 50,
  adj2: 50,
  rotate: 0,
})

const points = computed(() => {
  const w = +props.w
  const h = +props.h
  const horizontal = props.dir === 'right' || props.dir === 'left'
  // build a right-pointing arrow in a (len x thick) frame, then map it
  const len = horizontal ? w : h
  const thick = horizontal ? h : w
  const head = Math.min(len, Math.min(w, h) * (+props.adj2 / 100))
  const shaft = thick * (+props.adj1 / 100)
  const a = (thick - shaft) / 2
  const pts: [number, number][] = [
    [0, a], [len - head, a], [len - head, 0], [len, thick / 2],
    [len - head, thick], [len - head, thick - a], [0, thick - a],
  ]
  const map = ([l, t]: [number, number]): [number, number] => {
    switch (props.dir) {
      case 'left': return [len - l, t]
      case 'down': return [t, l]
      case 'up': return [t, len - l]
      default: return [l, t]
    }
  }
  return pts.map(map).map(p => p.join(',')).join(' ')
})
</script>

<template>
  <svg
    class="absolute pointer-events-none"
    :style="{ left: `${x}px`, top: `${y}px`, transform: +rotate ? `rotate(${rotate}deg)` : undefined }"
    :width="w"
    :height="h"
  >
    <polygon :points="points" :fill="color" />
  </svg>
</template>
