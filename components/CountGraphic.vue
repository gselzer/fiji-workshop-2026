<!--
  Five nuclei on a dark field — illustrates "how many?" counting.
  Usage: <CountGraphic /> or <CountGraphic :scale="0.7" segmented />
-->
<script setup lang="ts">
withDefaults(defineProps<{ scale?: number; segmented?: boolean }>(), { scale: 1, segmented: false })
</script>

<template>
  <div class="outer" :style="{ width: `${370 * scale}px`, height: `${180 * scale}px` }">
    <div :class="['inner', { segmented }]" :style="{ transform: `scale(${scale})` }">
      <div class="nucleus" style="left:25px;  top:16px;  width:56px; height:56px;"></div>
      <div class="nucleus" style="left:152px; top:30px;  width:48px; height:48px;"></div>
      <div class="nucleus" style="left:288px; top:14px;  width:52px; height:52px;"></div>
      <div class="nucleus" style="left:60px;  top:104px; width:50px; height:50px;"></div>
      <div class="nucleus" style="left:210px; top:108px; width:54px; height:54px;"></div>
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

.nucleus {
  position: absolute;
  border-radius: 50%;
  background: rgba(var(--dapi-rgb), 0.82);
  box-shadow: 0 0 12px rgba(var(--dapi-rgb), 0.5);
}
.segmented .nucleus { background: rgba(255,255,255,0.95); box-shadow: none; }
</style>
