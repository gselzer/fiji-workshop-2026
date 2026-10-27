<!--
  Title/section-divider slide: content centered on the slide, optionally
  over a full-bleed background image. Use in a slide's frontmatter:

    ---
    layout: section
    background: /media/s01-background.jpg   (optional)
    ---
-->
<script setup lang="ts">
defineProps<{ background?: string }>()
</script>

<template>
  <div
    class="slidev-layout section h-full w-full grid place-content-center text-center"
    :style="background ? { backgroundImage: `url(${background})`, backgroundSize: 'cover', backgroundPosition: 'center' } : {}"
  >
    <slot />
  </div>
</template>
