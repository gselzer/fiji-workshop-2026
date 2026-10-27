<!--
  Dim vs bright cell pair — illustrates "how bright?" intensity measurement.
  In segmented mode the dim cell is ghosted (below threshold) and the bright
  cell becomes white — showing that binary segmentation discards intensity info.
  Usage: <IntensityGraphic /> or <IntensityGraphic :scale="0.7" segmented />
-->
<script setup lang="ts">
withDefaults(defineProps<{ scale?: number; segmented?: boolean }>(), { scale: 1, segmented: false })
</script>

<template>
  <div class="outer" :style="{ width: `${370 * scale}px`, height: `${180 * scale}px` }">
    <div :class="['inner', { segmented }]" :style="{ transform: `scale(${scale})` }">
      <div class="center-flex">
        <div style="display:flex; gap:60px; align-items:center">
          <div class="cell cell-dim"></div>
          <div class="cell cell-bright"></div>
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

.cell { width: 110px; height: 110px; border-radius: 50%; }
.cell-dim    { background: rgba(var(--dapi-rgb), 0.14); box-shadow: 0 0 0 1.5px rgba(var(--dapi-rgb), 0.35); }
.cell-bright { background: rgba(var(--dapi-rgb), 0.96); box-shadow: 0 0 20px rgba(var(--dapi-rgb), 0.55), 0 0 0 1.5px var(--dapi-border); }

/* Both cells look identical after binarization — intensity info is lost */
.segmented .cell-dim    { background: rgba(255,255,255,0.95); box-shadow: none; }
.segmented .cell-bright { background: rgba(255,255,255,0.95); box-shadow: none; }
</style>
