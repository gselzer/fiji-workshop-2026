<!--
  3×3 tiled acquisition grid — 9 separate rounded tiles with slide background
  showing in gaps and outer padding. Boundary circles are placed at exactly the
  tile edge (cx=T or cx=0) so removing the gap would make them seamless.
  Usage: <TiledAcquisitionGraphic /> or <TiledAcquisitionGraphic :scale="0.6" />
-->
<script setup lang="ts">
withDefaults(defineProps<{ scale?: number }>(), { scale: 1 })

const T = 110               // tile size in px
const G = 10                // gap between tiles + outer padding
const SIZE = 3 * T + 4 * G // 370 (10px outer pad on each side + 2 inner gaps)

type Circle = { cx: number; cy: number; r: number }

// Circles fully within each tile (well away from edges)
const inner: Record<string, Circle[]> = {
  '0,0': [{ cx: 40, cy: 40, r: 18 }, { cx: 80, cy: 75, r: 10 }],
  '1,0': [{ cx: 50, cy: 35, r: 16 }],
  '2,0': [{ cx: 55, cy: 65, r: 18 }],
  '0,1': [{ cx: 38, cy: 50, r: 15 }],
  '1,1': [{ cx: 55, cy: 60, r: 18 }, { cx: 95, cy: 28, r: 10 }],
  '2,1': [{ cx: 68, cy: 42, r: 15 }],
  '0,2': [{ cx: 50, cy: 50, r: 16 }],
  '1,2': [{ cx: 65, cy: 65, r: 18 }],
  '2,2': [{ cx: 48, cy: 55, r: 15 }, { cx: 90, cy: 20, r: 16 }],
}

// Horizontal boundaries [leftCol, row, cy, r]
// Left tile gets cx=T (right edge), right tile gets cx=0 (left edge) — symmetric halves.
// Removing the gap snaps them into one circle.
const hBounds: [number, number, number, number][] = [
  [0, 0, 65, 20],
  [1, 0, 50, 20],
  [0, 1, 50, 18],
  [1, 2, 60, 20],
]

// Vertical boundaries [col, topRow, cx, r]
// Top tile gets cy=T (bottom edge), bottom tile gets cy=0 (top edge).
const vBounds: [number, number, number, number][] = [
  [0, 0, 60, 20],
  [1, 0, 75, 18],
  [2, 0, 35, 20],
  [0, 1, 75, 20],
  [1, 1, 38, 18],
]

// Four-tile corners [leftCol, topRow, r]
// Each of the four tiles gets a quarter-circle at its respective corner.
const corners: [number, number, number][] = [
  [0, 0, 24],
  [1, 1, 22],
]

const tileBV = [0.030, 0.012, 0.025, 0.014, 0.020, 0.028, 0.022, 0.012, 0.018]

const tiles = Array.from({ length: 9 }, (_, i) => {
  const col = i % 3, row = Math.floor(i / 3)
  const circles: Circle[] = [...(inner[`${col},${row}`] ?? [])]

  for (const [lc, lr, cy, r] of hBounds) {
    if (lr === row) {
      if (col === lc)     circles.push({ cx: T, cy, r })
      if (col === lc + 1) circles.push({ cx: 0, cy, r })
    }
  }
  for (const [lc, lr, cx, r] of vBounds) {
    if (lc === col) {
      if (row === lr)     circles.push({ cx, cy: T, r })
      if (row === lr + 1) circles.push({ cx, cy: 0, r })
    }
  }
  for (const [lc, lr, r] of corners) {
    if (col === lc     && row === lr)     circles.push({ cx: T, cy: T, r })
    if (col === lc + 1 && row === lr)     circles.push({ cx: 0, cy: T, r })
    if (col === lc     && row === lr + 1) circles.push({ cx: T, cy: 0, r })
    if (col === lc + 1 && row === lr + 1) circles.push({ cx: 0, cy: 0, r })
  }

  return { i, bv: tileBV[i], circles }
})
</script>

<template>
  <div class="outer" :style="{ width: `${SIZE * scale}px`, height: `${SIZE * scale}px` }">
    <div class="inner" :style="{ transform: `scale(${scale})` }">
      <div class="tile-grid">
        <div v-for="t in tiles" :key="t.i" class="tile-wrap">
          <svg :width="T" :height="T">
            <rect class="tile-bg" x="0" y="0" :width="T" :height="T"/>
            <rect x="0" y="0" :width="T" :height="T" :fill="`rgba(255,255,255,${t.bv})`"/>
            <circle v-for="(c, ci) in t.circles" :key="ci"
              class="blob" :cx="c.cx" :cy="c.cy" :r="c.r"/>
          </svg>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.outer { overflow: hidden; flex-shrink: 0; }
.inner {
  width: 370px; height: 370px;
  transform-origin: top left;
}

.tile-grid {
  display: grid;
  grid-template-columns: repeat(3, 110px);
  grid-template-rows: repeat(3, 110px);
  gap: 10px;
  padding: 10px;
}

.tile-wrap {
  border-radius: 6px;
  overflow: hidden;
}

.tile-bg { fill: #0f172a; }
.blob    { fill: rgba(var(--dapi-rgb), 0.72); }
</style>
