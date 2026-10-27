<!--
  Animated cell trajectory over time — illustrates "does X move?" tracking.
  Uses useId() to keep SVG filter/path IDs unique across multiple instances.
  Usage: <MotionGraphic /> or <MotionGraphic :scale="0.7" segmented />
-->
<script setup lang="ts">
import { useId } from 'vue'
const props = withDefaults(defineProps<{ scale?: number; segmented?: boolean }>(), { scale: 1, segmented: false })
const uid = useId()
const glowId = `glow-${uid}`
const trajId = `traj-${uid}`
</script>

<template>
  <div class="outer" :style="{ width: `${370 * props.scale}px`, height: `${180 * props.scale}px` }">
    <div :class="['inner', { segmented: props.segmented }]" :style="{ transform: `scale(${props.scale})` }">
      <svg width="370" height="180" viewBox="0 0 370 180" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <filter :id="glowId" x="-50%" y="-50%" width="200%" height="200%">
            <feGaussianBlur stdDeviation="3.5" result="blur"/>
            <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
          </filter>
        </defs>
        <path :id="trajId" fill="none" stroke="none"
          d="M 27,91 C 62,82 62,71 97,71 C 135,71 135,87 173,87 C 211,87 211,61 249,61 C 288,61 288,80 328,80"/>
        <!-- Ghost dots fading in at each waypoint -->
        <circle class="ghost" cx="27"  cy="91" r="13" opacity="0">
          <animate attributeName="opacity" values="1;1;0"     keyTimes="0;0.90;1"               dur="4s" repeatCount="indefinite"/>
        </circle>
        <circle class="ghost" cx="97"  cy="71" r="13" opacity="0">
          <animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;0.1874;0.1875;0.90;1" dur="4s" repeatCount="indefinite"/>
        </circle>
        <circle class="ghost" cx="173" cy="87" r="13" opacity="0">
          <animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;0.3749;0.375;0.90;1"  dur="4s" repeatCount="indefinite"/>
        </circle>
        <circle class="ghost" cx="249" cy="61" r="13" opacity="0">
          <animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;0.5624;0.5625;0.90;1" dur="4s" repeatCount="indefinite"/>
        </circle>
        <circle class="ghost" cx="328" cy="80" r="13" opacity="0">
          <animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;0.7499;0.750;0.90;1"  dur="4s" repeatCount="indefinite"/>
        </circle>
        <!-- Frame counter -->
        <text class="frame-label" x="358" y="168" text-anchor="end" font-size="7" font-family="monospace" opacity="0">frame 0
          <animate attributeName="opacity" values="1;1;0;0"     keyTimes="0;0.1874;0.1875;1"               dur="4s" repeatCount="indefinite"/>
        </text>
        <text class="frame-label" x="358" y="168" text-anchor="end" font-size="7" font-family="monospace" opacity="0">frame 1
          <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.1874;0.1875;0.3749;0.375;1" dur="4s" repeatCount="indefinite"/>
        </text>
        <text class="frame-label" x="358" y="168" text-anchor="end" font-size="7" font-family="monospace" opacity="0">frame 2
          <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.3749;0.375;0.5624;0.5625;1" dur="4s" repeatCount="indefinite"/>
        </text>
        <text class="frame-label" x="358" y="168" text-anchor="end" font-size="7" font-family="monospace" opacity="0">frame 3
          <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.5624;0.5625;0.7499;0.750;1" dur="4s" repeatCount="indefinite"/>
        </text>
        <text class="frame-label" x="358" y="168" text-anchor="end" font-size="7" font-family="monospace" opacity="0">frame 4
          <animate attributeName="opacity" values="0;0;1;1;0"   keyTimes="0;0.7499;0.750;0.90;1"          dur="4s" repeatCount="indefinite"/>
        </text>
        <!-- Moving cell — glows in fluorescence mode, plain in segmented mode -->
        <circle class="moving" r="14" :filter="props.segmented ? undefined : `url(#${glowId})`">
          <animateMotion dur="4s" repeatCount="indefinite" calcMode="linear"
            keyTimes="0;0.75;1" keyPoints="0;1;1">
            <mpath :href="`#${trajId}`"/>
          </animateMotion>
        </circle>
      </svg>
    </div>
  </div>
</template>

<style scoped>
.outer { overflow: hidden; flex-shrink: 0; }
.inner {
  width: 370px; height: 180px;
  transform-origin: top left;
  background: #0f172a;
  border-radius: 8px;
  border: 1.5px solid #334155;
  overflow: hidden;
}
.inner.segmented { background: #0a0a0a; border-color: #333; }

.ghost  { fill: rgba(var(--dapi-rgb), 0.6); }
.moving { fill: rgba(var(--dapi-rgb), 0.95); }
.frame-label { fill: #475569; }

.segmented .ghost       { fill: rgba(255,255,255,0.6); }
.segmented .moving      { fill: rgba(255,255,255,0.95); }
.segmented .frame-label { fill: #666; }
</style>
