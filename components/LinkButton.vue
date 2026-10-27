<!--
  Positioned link button matching the deck's white-box link style.

  Usage:
    <LinkButton left="32" top="462" width="369"
                href="https://imagej.net/Fiji"
                icon="⬇️" label="Download Fiji here!" />

  All position/size values are px numbers on the 980×551 canvas.
  label defaults to the href with the https:// prefix stripped.
-->
<script setup lang="ts">
import { computed } from 'vue'

const props = withDefaults(defineProps<{
  href: string
  label?: string
  icon?: string
  left: number | string
  top: number | string
  width?: number | string
  height?: number | string
}>(), {
  width: 369,
  height: 47,
})

const px = (v: number | string) =>
  typeof v === 'number' || /^\d+(\.\d+)?$/.test(String(v)) ? `${v}px` : v

const posStyle = computed(() => ({
  left: px(props.left),
  top: px(props.top),
  width: px(props.width),
  height: px(props.height),
}))

const displayLabel = computed(() =>
  props.label ?? props.href.replace(/^https?:\/\//, '')
)
</script>

<template>
  <a
    :href="href"
    target="_blank"
    rel="noopener noreferrer"
    class="link-btn abs"
    :style="posStyle"
  >
    <span v-if="icon" class="link-btn-icon">{{ icon }}</span>{{ displayLabel }}
  </a>
</template>

<style scoped>
.link-btn {
  font-size: 22px;
  text-align: center;
  background: #fff;
  border: 1px solid #000;
  color: #000;
  text-decoration: none;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.3em;
  padding: 0 8px;
  box-sizing: border-box;
}
.link-btn-icon {
  flex-shrink: 0;
}
</style>
