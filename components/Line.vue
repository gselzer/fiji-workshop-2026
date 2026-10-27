<!--
  A straight line, optionally with arrowheads, in px on the 980 x 551 canvas.

  Usage:
    <Line x1="100" y1="100" x2="300" y2="200" color="#91DAED" width="4" />
    <Line x1="100" y1="100" x2="300" y2="200" color="red" width="4" arrow="end" />

  arrow: "none" (default), "end" (head at x2,y2), "start", or "both"
  dashed: add the attribute to draw a dashed line
-->
<script setup lang="ts">
import { computed, useId } from 'vue'

const props = withDefaults(defineProps<{
  x1: number | string
  y1: number | string
  x2: number | string
  y2: number | string
  color?: string
  width?: number | string
  arrow?: 'none' | 'end' | 'start' | 'both'
  dashed?: boolean
}>(), {
  color: 'currentColor',
  width: 2,
  arrow: 'none',
  dashed: false,
})

const id = `line-head-${useId()}`
const hasEnd = computed(() => props.arrow === 'end' || props.arrow === 'both')
const hasStart = computed(() => props.arrow === 'start' || props.arrow === 'both')
</script>

<template>
  <svg
    class="absolute left-0 top-0 pointer-events-none"
    :width="Math.max(+x1, +x2) + 4 * +width"
    :height="Math.max(+y1, +y2) + 4 * +width"
    style="overflow: visible"
  >
    <defs v-if="arrow !== 'none'">
      <!-- head is 3x the line width, like PowerPoint's medium triangle -->
      <marker :id="id" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="3" markerHeight="3" orient="auto-start-reverse">
        <path d="M0,0 L10,5 L0,10 z" :fill="color" />
      </marker>
    </defs>
    <line
      :x1="x1" :y1="y1" :x2="x2" :y2="y2"
      :stroke="color"
      :stroke-width="width"
      :stroke-dasharray="dashed ? `${3 * +width} ${2 * +width}` : undefined"
      :marker-end="hasEnd ? `url(#${id})` : undefined"
      :marker-start="hasStart ? `url(#${id})` : undefined"
    />
  </svg>
</template>
