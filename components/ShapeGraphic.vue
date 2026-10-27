<!--
  Round vs elongated cells — illustrates "what shape/size?" measurement.
  Usage: <ShapeGraphic /> or <ShapeGraphic :scale="0.7" segmented />
-->
<script setup lang="ts">
withDefaults(defineProps<{ scale?: number; segmented?: boolean }>(), { scale: 1, segmented: false })
</script>

<template>
  <div class="outer" :style="{ width: `${370 * scale}px`, height: `${180 * scale}px` }">
    <div :class="['inner', { segmented }]" :style="{ transform: `scale(${scale})` }">
      <div class="center-flex">
        <div style="display:flex; gap:60px; align-items:center">
          <div class="shape" style="width:110px; height:110px;"></div>
          <div class="shape" style="width:170px; height:60px;"></div>
        </div>
      </div>
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
  position: relative;
}
.inner.segmented { background: #0a0a0a; border-color: #333; }
.center-flex { width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; }

.shape {
  border-radius: 50%;
  background: rgba(var(--dapi-rgb), 0.7);
  box-shadow: 0 0 10px rgba(var(--dapi-rgb), 0.4), 0 0 0 2px var(--dapi-border);
}
.segmented .shape { background: rgba(255,255,255,0.95); box-shadow: none; }
</style>
