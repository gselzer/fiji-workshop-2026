---
theme: default
addons:
  - slidev-addon-qrcode
title: Image Analysis with Fiji/ImageJ
info: |
  AQLM image analysis lecture
colorSchema: light
aspectRatio: 16/9
canvasWidth: 980
transition: none
layout: section
---

# Image Analysis with Fiji/ImageJ

<div style="text-align:left">

Gabriel Selzer

Research Software Engineer, Eliceiri Lab

University of Wisconsin-Madison / Morgridge Institute for Research

</div>

<div class="abs" style="left:80px; top:508px; font-size:16px; text-align:left">

*Adapted from the work of Noelle Cataldo, Helen Wilson, Bjorn Paulson, Edward Evans, and more.*

</div>

<img class="abs" src="/media/loci.png" style="left:746px; top:44px; width:185px">

<img class="abs" src="/media/uw-logo.png" style="left:31px; top:27px; width:250px">

<img class="abs" src="/media/morgridge.png" style="left:360px; top:27px; width:250px;">

<div class="abs" style="left:800px; top:360px; text-align:center; font-size:13px; color:#555; border:1.5px solid #7a7a7a; border-radius:10px; padding:8px 10px">

**Slides**
<QRCode data="https://gselzer.github.io/fiji-workshop/" :width="148" :height="148" :dotsOptions="{type: 'rounded', color: 'black' }" />

</div>

---
src: ./chapters/intro.md
---

---
src: ./chapters/fiji-overview.md
---

---
src: ./chapters/digital-images.md
---

---
src: ./chapters/quantitative-measurements.md
---

---
src: ./chapters/segmentation.md
---

---
src: ./chapters/preprocessing.md
---

---
src: ./chapters/measurements.md
---

---
src: ./chapters/scripting.md
---

---

# Take-home messages

- Quality images in → Quality measurements out
  - Watch your histograms during acquisition
- Pre-processing can rescue difficult segmentations
- Record your workflows
  - Ideally write scripts
- Help is available at the image.sc forum

<b>Questions?</b>

<div class="abs" style="left:550px; top:90px; width:350px; background:#e3f2fd; border:1.5px solid #0E2841; border-radius:10px; padding:12px">

<div style="font-size:22px; font-weight:bold; margin-bottom:10px; display:flex; align-items:center; justify-content:center; gap:6px">
  Fiji @
  <img src="/media/loci.png" style="height:28px; object-fit:contain">
</div>

<div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; justify-items:center">
  <div style="display:flex; flex-direction:column; align-items:center; gap:4px">
    <img src="https://loci.wisc.edu/wp-content/uploads/sites/1939/2023/01/Curtis2-150x150.jpg" style="height:120px;">
    <div style="font-size:13px; text-align:center">Curtis Rueden</div>
  </div>
  <div style="display:flex; flex-direction:column; align-items:center; gap:4px">
    <img src="https://loci.wisc.edu/wp-content/uploads/sites/1939/2023/01/Screen-Shot-2023-01-31-at-2.09.32-PM-150x150.png" style="height:120px;">
    <div style="font-size:13px; text-align:center">Mark Hiner-Weir</div>
  </div>
  <div style="display:flex; flex-direction:column; align-items:center; gap:4px">
    <img src="https://loci.wisc.edu/wp-content/uploads/sites/1939/2023/01/Evans_Edward-II-e1521132292607-240x300-1-e1589998832473-150x150.jpg" style="height:120px;">
    <div style="font-size:13px; text-align:center">Edward Evans</div>
  </div>
  <div style="display:flex; flex-direction:column; align-items:center; gap:4px">
    <img src="https://loci.wisc.edu/wp-content/uploads/sites/1939/2023/01/gabriel-150x150.jpg" style="height:120px;">
    <div style="font-size:13px; text-align:center">Gabriel Selzer</div>
  </div>
</div>

</div>
