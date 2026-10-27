<!--
  Co-localizing DAPI/FITC pairs — illustrates "does X appear near Y?" colocalization.
  Uses useId() to keep SVG filter/path IDs unique across multiple instances.
  Usage: <ColocGraphic /> or <ColocGraphic :scale="0.7" segmented />
-->
<script setup lang="ts">
const props = withDefaults(defineProps<{ scale?: number; segmented?: boolean }>(), { scale: 1, segmented: false })
</script>

<template>
  <div class="outer" :style="{ width: `${370 * props.scale}px`, height: `${180 * props.scale}px` }">
    <div :class="['inner', { segmented: props.segmented }]" :style="{ transform: `scale(${props.scale})` }">
      <svg width="370" height="180" viewBox="0 0 370 180" xmlns="http://www.w3.org/2000/svg">
        <!-- Pair 1 -->
        <circle class="dapi-dot" cx="70"  cy="62"  r="14"/>
        <circle class="fitc-dot" cx="80"  cy="70"  r="14"/>
        <!-- Pair 2 -->
        <circle class="dapi-dot" cx="185" cy="100" r="14"/>
        <circle class="fitc-dot" cx="195" cy="91"  r="14"/>
        <!-- Pair 3 -->
        <circle class="dapi-dot" cx="288" cy="60"  r="14"/>
        <circle class="fitc-dot" cx="297" cy="68"  r="14"/>
        <!-- Legend -->
        <circle class="dapi-dot legend-dot" cx="305" cy="145" r="5"/>
        <text class="legend-label" x="315" y="152" font-size="6" font-family="monospace">DAPI</text>
        <circle class="fitc-dot legend-dot" cx="305" cy="165" r="5"/>
        <text class="legend-label" x="315" y="172" font-size="6" font-family="monospace">FITC</text>
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

.dapi-dot    { fill: rgba(var(--dapi-rgb), 0.65); }
.fitc-dot    { fill: rgba(var(--fitc-rgb), 0.6); }
.legend-dot  { opacity: 0.85; }
.legend-label { fill: #475569; }

.segmented .dapi-dot    { fill: rgba(255,255,255,0.85); }
.segmented .fitc-dot    { fill: rgba(255,255,255,0.65); }
.segmented .legend-label { fill: #666; }
</style>
