---
theme: default
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

Gabriel Selzer

Research Software Engineer

Kevin Eliceiri Lab

University of Wisconsin-Madison / Morgridge Institute for Research

<div class="abs" style="left:132px; top:508px; width:735px; font-size:16px; text-align:center">

*Adapted from the work of Noelle Cataldo, Helen Wilson, Bjorn Paulson, Edward Evans, and more.*

</div>

<img class="abs" src="/media/loci.png" style="left:746px; top:44px; width:185px">

<img class="abs" src="/media/s01-google-shape-192-p49.png" style="left:31px; top:27px; width:250px">

<img class="abs" src="/media/morgridge.png" style="left:360px; top:27px; width:250px;">
---

# About Me!

<div class="abs" style="left:45px; top:120px; width:454px; font-size:24px">

- Eliceiri Lab since 2017
- Based in Chicago, IL
- Core developer for Fiji and Micro-Manager

</div>

<img class="abs" src="/media/headshot.jpg" style="left:610px; top:145px; width:291px; height:366px; object-fit:cover">

<img class="abs" src="/media/loci.png" style="left:769px; top:11px; width:171px; height:85px">

<img class="abs" src="/media/fiji.png" style="left:90px; top:300px; width:130px; height:130px">

<img class="abs" src="/media/micro-manager.png" style="left:245px; top:303px; width:320px; height:124px; padding:4px 10px; background:#000">

---

# Outline

<div class="abs" style="left:36px; top:106px; width:460px; font-size:20px">

- The Bioimaging Pipeline
- Fiji Overview
- Digital Images
  - Fundamentals
  - Visualization
- Quantitative Measurements
- Image Analysis
  - Segmentation
  - Preprocessing
  - Measurements
    - Segment Analysis
    - Tracking
    - Colocalization
- Scripting
<!-- LLMs in Fiji -->

</div>

---

# The Bioimaging Pipeline

```mermaid
%%{init: {"theme": "neutral", "themeVariables": {"fontSize": "20px", "edgeLabelBackground": "#faf8f3"}, "flowchart": {"wrappingWidth": 400}}}%%
flowchart LR
  A["Biological<br>system"] -->|"sample<br>preparation"| B["Sample on the<br>microscope"]
  B -->|"image<br>acquisition"| C["Digital<br>image"]
  C -->|"image analysis"| D["Quantitative<br>measurements"]
  D -->|"statistics"| E["Knowledge about<br>that system"]
  classDef endpoint fill:#dde8e0,stroke:#7f9c88
  class A,E endpoint
```

<!-- Red box around "Digital image -> image analysis -> Quantitative
     measurements", shown on the first click. Position is in slide pixels;
     move it if the diagram changes. -->
<div v-click class="abs" style="left:420px; top:110px; width:325px; height:73px; border:4px solid #d62728; border-radius:8px; padding:0"></div>

<v-click> This lecture seeks to describe: </v-click>

<v-clicks>

- **Inputs:** digital images
- **Outputs:** quantitative measurements
- **Functions:** image analysis pipelines

</v-clicks>

<v-click>This lecture focuses on Fiji/ImageJ...</v-click>

<v-click>but there are many great alternatives!</v-click>

<!-- Fiji / ImageJ — revealed on click 6; red border highlights the focus area -->
<img v-click="6" class="abs" src="/media/s13-picture-2.png" style="left:38px; top:350px; width:120px; height:120px; object-fit:contain">
<img v-click="6" class="abs" src="/media/s13-picture-4.png" style="left:234px; top:350px; width:120px; height:120px; object-fit:contain">
<div v-click="6" class="abs" style="left:38px; top:478px; width:120px; font-size:18px; text-align:center">

**Fiji**

</div>
<div v-click="6" class="abs" style="left:234px; top:478px; width:120px; font-size:18px; text-align:center">

**ImageJ**

</div>

<!-- Alternatives — revealed on click 7 -->
<img v-click="7" class="abs" src="/media/s13-picture-8.jpg" style="left:430px; top:350px; width:120px; height:120px; object-fit:contain">
<div v-click="7" class="abs" style="left:430px; top:478px; width:120px; font-size:18px; text-align:center">

**QuPath**

</div>
<img v-click="7" class="abs" src="/media/s13-picture-10.png" style="left:626px; top:350px; width:120px; height:120px; object-fit:contain">
<div v-click="7" class="abs" style="left:626px; top:478px; width:120px; font-size:18px; text-align:center">

**Imaris**

</div>
<img v-click="7" class="abs" src="/media/s13-picture-12.png" style="left:822px; top:350px; width:120px; height:120px; object-fit:contain">
<div v-click="7" class="abs" style="left:822px; top:478px; width:120px; font-size:18px; text-align:center">

**Cellprofiler**

</div>

---
class: fiji-slide
---

# <u>**F**</u>iji <u>**I**</u>s <u>**J**</u>ust <u>**I**</u>mageJ

<div class="abs" style="left:32px; top:122px; width:298px; font-size:29px">

- **ImageJ 1.x**: image analysis since 1997
- **ImageJ2**: a rewrite for modularity and generality
- **Fiji**: ImageJ + ImageJ2 + popular plugins

</div>

<img class="abs" src="/media/s16-picture-2.png" style="left:467px; top:146px; width:363px; height:388px">

<img class="abs" src="/media/s16-picture-4.png" style="left:329px; top:270px; width:120px; height:120px">

<div class="abs" style="left:139px; top:391px; width:500px; font-size:18px; text-align:center">

Curtis Rueden

</div>

<img class="abs" src="/media/s16-picture-6.png" style="left:848px; top:261px; width:120px; height:120px">

<div class="abs" style="left:830px; top:385px; width:189px; font-size:18px">

Wayne Rasband

</div>

<LinkButton left="32" top="462" width="369" href="https://imagej.net/Fiji" icon="⬇️" label="Download Fiji here!" />

---
class: fiji-slide
---

# Fiji Interface

<!-- Both images on right side; highlights declared after so they render on top -->
<img v-click-hide="5" class="abs" src="/media/FijiInterface.png" style="left:380px; top:75px; width:580px;">
<img v-click="5" class="abs" src="/media/FijiSearch.png" style="left:380px; top:75px; width:580px;">

<!-- Click 1: Menu bar highlight -->
<div v-click="1" class="abs" style="left:380px; top:103px; width:580px; height:22px; background:rgba(255,152,0,0.4); pointer-events:none"></div>
<div v-click="1" class="abs" style="left:20px; top:85px; width:350px; font-size:18px; padding:6px 12px; background:rgba(255,152,0,0.12); border-left:4px solid rgba(255,152,0,0.9)">

**Menu bar** — File, Edit, Image, Process, Analyze, Plugins, Window, Help

</div>

<!-- Click 2: Toolbar highlight -->
<div v-click="2" class="abs" style="left:380px; top:125px; width:580px; height:29px; background:rgba(76,175,80,0.4); pointer-events:none"></div>
<div v-click="2" class="abs" style="left:20px; top:145px; width:350px; font-size:18px; padding:6px 12px; background:rgba(76,175,80,0.12); border-left:4px solid rgba(76,175,80,0.9)">

**Toolbar** — Selection, drawing, and measurement tools

💡 Right-click a tool for shape variants

💡 Double-click a tool to configure it

</div>

<!-- Click 3: Status bar highlight -->
<div v-click="3" class="abs" style="left:380px; top:154px; width:399px; height:23px; background:rgba(156,39,176,0.4); pointer-events:none"></div>
<div v-click="3" class="abs" style="left:20px; top:254px; width:350px; font-size:18px; padding:6px 12px; background:rgba(156,39,176,0.12); border-left:4px solid rgba(156,39,176,0.9)">

**Status bar** — shows memory usage and pixel coordinates

💡 Click it see your Fiji version

</div>

<!-- Click 4: Search highlight (stays visible on click 5) -->
<div v-click="4" class="abs" style="left:779px; top:154px; width:181px; height:23px; background:rgba(0,150,136,0.4); pointer-events:none"></div>
<div v-click="4" class="abs" style="left:20px; top:339px; width:350px; font-size:18px; padding:6px 12px; background:rgba(0,150,136,0.12); border-left:4px solid rgba(0,150,136,0.9)">

**Search** — Ctrl+L (or click the icon) to find any menu command by name

</div>

<LinkButton left="20" top="462" width="350" href="https://imagej.net/Getting_Started" icon="📖" label="Getting Started — ImageJ wiki" />

---
class: fiji-slide
hide: true <!-- TODO: What is the point of this -->
---

# Operating the interface

<div class="abs" style="left:616px; top:137px; width:339px; font-size:24px; --nest:1.00">

- Selections
- Hold shift to make vertical/horizontal lines and perfect circles
- Regions of interest → ROIs
  - Can be added to ROI manager and saved

</div>

<video class="abs" src="/media/s19-screen-recording-2026-02-23-at-1-12-12-p.mov" poster="/media/s19-screen-recording-2026-02-23-at-1-12-12-p.png" controls style="left:24px; top:135px; width:574px; height:374px"></video>

---
class: fiji-slide
hide: true
---

# There is a search bar to easily open certain features

<img class="abs" src="/media/s20-google-shape-274-p21.png" style="left:-15px; top:117px; width:624px; height:448px">

<div class="abs" style="left:608px; top:133px; width:347px; font-size:24px">

- Edit → Options → Search Bar
- Control + L brings up the search bar
- Or simply click the bar at the bottom left of the interface

</div>

<div class="abs" style="left:628px; top:411px; width:308px; height:106px; font-size:20px; text-align:center; border:2px solid #000000">

***Tip: Find more keyboard shortcuts here*** ***<https://imagej.net/ij/docs/shortcuts.html>***

</div>

---
class: fiji-slide
---

# Fiji and all plugins can be manually updated

<img class="abs" src="/media/s21-google-shape-282-p22.png" style="left:40px; top:133px; width:582px; height:337px; border:2px solid #0E2841">

<BlockArrow dir="right" x="252" y="294" w="159" h="56" color="#FF0000" />

<div class="abs" style="left:252px; top:294px; width:159px; height:56px; font-size:18px; text-align:center; display:flex; flex-direction:column; justify-content:center; color:#FFFFFF">

Not this one!

</div>

<BlockArrow dir="right" x="252" y="408" w="159" h="56" color="#3B7D23" />

<div class="abs" style="left:252px; top:408px; width:159px; height:56px; font-size:18px; text-align:center; display:flex; flex-direction:column; justify-content:center; color:#FFFFFF">

Correct

</div>

<LinkButton left="117" top="481" width="428" height="37" href="https://imagej.net/plugins/updater" icon="🔧" />

<!--
Update ImageJ updates the actual ImageJ
Update… updates the plugins
If plugin breaks, get latest ImageJ → If doesn’t put in a request (image.sc)
-->

---
class: fiji-slide
---

# The user can indicate specific update sites

<div class="abs" style="left:650px; top:221px; width:307px; font-size:24px">

- Useful if you want to maintain a specific plugin version for an experiment already started

</div>

<img class="abs" src="/media/s22-google-shape-294-p23.png" style="left:66px; top:109px; width:528px; height:393px">

<LinkButton left="50" top="504" width="582" height="37" href="https://imagej.net/update-sites/following" icon="📦" />

---
class: fiji-slide
---

# Stuck? Help is available!

<img class="abs" src="/media/s23-google-shape-306-p24.png" style="left:19px; top:125px; width:471px; height:362px">

<img class="abs" src="/media/s23-google-shape-305-p24.png" style="left:531px; top:138px; width:399px; height:319px">

<LinkButton left="144" top="505" width="221" height="37" href="https://imagej.net" icon="🌐" />
<LinkButton left="577" top="505" width="305" height="37" href="https://forum.image.sc/" icon="💬" />

<!--
Can also just Google questions! Or ask ChatGPT!

***Virtual memory
-->

---
layout: section
---

# Digital Images

The input

<div style="width:500px; margin: 0 auto">

```mermaid
%%{init: {"theme": "neutral", "themeVariables": {"fontSize": "20px", "edgeLabelBackground": "#faf8f3"}, "flowchart": {"wrappingWidth": 400}}}%%
flowchart LR
  C["Digital<br>image"] -->|"image analysis"| D["Quantitative<br>measurements"]
  classDef endpoint fill:#dde8e0,stroke:#7f9c88
```

</div>

---

# Digital images are structured samples of a system

```mermaid
%%{init: {"theme": "neutral", "themeVariables": {"fontSize": "20px", "edgeLabelBackground": "#faf8f3"}, "flowchart": {"wrappingWidth": 400}}}%%
flowchart LR
  A["Biological<br>system"] -->|"sample<br>preparation"| B["Sample on the<br>microscope"]
  B -->|"image<br>acquisition"| C["Digital<br>image"]
  C -->|"image analysis"| D["Quantitative<br>measurements"]
  D -->|"statistics"| E["Knowledge about<br>that system"]
  classDef endpoint fill:#dde8e0,stroke:#7f9c88
  class A endpoint
  style D fill:#efefef,stroke:#ccc,color:#bbb
  style E fill:#efefef,stroke:#ccc,color:#bbb
  linkStyle 2 stroke:#ccc,color:#bbb
  linkStyle 3 stroke:#ccc,color:#bbb
```
<!-- Red box always visible (no v-click). Position is in slide pixels;
     move it if the diagram changes. -->
<div class="abs" style="left:420px; top:110px; width:325px; height:73px; border:4px solid #d62728; border-radius:8px; padding:0"></div>

<!-- https://bioart.niaid.nih.gov/bioart/677 -->
<img class="abs" src="/media/SkinCrossSection0001.svg" style="left:50px; top:200px; width:100px; height:130px; object-fit:contain">
<Arrow x1="150" y1="265" x2="238" y2="265" />
<!-- https://bioart.niaid.nih.gov/bioart/675 -->
<img class="abs" src="/media/BloodSmearUnstained0001.svg" style="left:240px; top:200px; width:100px; height:130px; object-fit:contain">
<Arrow x1="290" y1="285" x2="290" y2="375" />
<!-- https://bioart.niaid.nih.gov/bioart/503 -->
<img class="abs" src="/media/ConfocalMicroscope0001.svg" style="left:240px; top:380px; width:100px; height:130px; object-fit:contain">
<Arrow x1="350" y1="445" x2="420" y2="445" />
<!-- https://bioart.niaid.nih.gov/bioart/240 -->
<img class="abs" src="/media/HumanSkinCellSwatch.svg" style="left:430px; top:395px; width:100px; height:100px; object-fit:contain; border:3px solid #d62728; border-radius:4px">


---

# Digital images are structured samples of a system

<img class="abs" src="/media/s06-picture-2.png" style="left:23px; top:150px; width:580px; height:339px">

<img class="abs" src="/media/s06-picture-6.png" style="left:640px; top:150px; width:317px; height:339px">

<BlockArrow dir="down" x="160" y="355" w="40" h="64" color="#FF0000" rotate="39.1212" />

<BlockArrow dir="down" x="815" y="218" w="40" h="64" color="#FF0000" rotate="39.1212" />

---

# These samples can be stored in different ways

<img class="abs" src="/media/s07-picture-2.png" style="left:25px; top:145px; width:542px; height:131px">

<img class="abs" src="/media/s07-picture-4.png" style="left:25px; top:287px; width:542px; height:83px">

<img class="abs" src="/media/s07-picture-6.png" style="left:580px; top:193px; width:374px; height:165px">

<div class="abs" style="left:646px; top:392px; width:243px; font-size:20px">

- 8-bit = 256 levels
- 12-bit = 4096 levels
- 16-bit = 65536 levels
- 32-bit = decimal values!

</div>

<div class="abs" style="left:48px; top:434px; width:497px; height:45px; font-size:24px; text-align:center; display:flex; flex-direction:column; justify-content:center; background:#DCEAF7; border:1px solid #000000; color:#000000">

**[ImageJ User Guide: Types and Formats](https://imagej.net/docs/guide/146-7.html)**

</div>

---

# These samples can be stored in different ways

<img class="abs" src="/media/s08-picture-2.jpg" style="left:38px; top:121px; width:584px; height:388px">

<div class="abs" style="left:-17px; top:522px; width:695px; font-size:14px; text-align:center">

*Adapted from:* <https://gregbenzphotography.com/photography-tips/8-vs-16-bit-depth-photoshop/>

</div>

<div class="abs" style="left:661px; top:147px; width:281px; font-size:24px">

- Tradeoff: Disk space vs. resolution
- Screen resolution tops out around 8-10 bits

</div>

---
hide: true  <!-- TODO: What is this supposed to show? -->
---

# 3D representations can also be used to visualize bit depth

<img class="abs" src="/media/s09-picture-6.png" style="left:12px; top:145px; width:311px; height:311px">

<img class="abs" src="/media/s09-picture-8.png" style="left:334px; top:145px; width:311px; height:311px">

<img class="abs" src="/media/s09-picture-8-2.png" style="left:669px; top:145px; width:311px; height:311px">

<div class="abs" style="left:748px; top:465px; width:114px; font-size:33px">

**32 bit**

</div>

<div class="abs" style="left:433px; top:465px; width:114px; font-size:33px">

**16 bit**

</div>

<div class="abs" style="left:133px; top:465px; width:114px; font-size:33px">

**8 bit**

</div>

<div class="abs" style="left:762px; top:108px; width:338px; font-size:18px">

Courtesy of Edward Evans

</div>

---

# **Metadata** organizes your samples

<div class="abs" style="left:32px; top:125px; width:500px; font-size:26px">

- Dimension ordering

<v-click>

- Dimensions labels

</v-click>
<v-click>

- Pixel size, voxel size, time intervals

</v-click>
<v-click>

- ...and many, many more attributes...

</v-click>
<v-click>

- File types (.tif, .png, .asc, .nd2) signal the schema
  - use OME if you can!

</v-click>

</div>

<!-- Graphic 1: dimension ordering — visible initially, hides at click 1 -->
<div v-click-hide="1" class="abs" style="left:520px; top:108px; width:440px">
<div style="display:flex; flex-direction:column; align-items:center; gap:20px">
<div style="text-align:center">
  <div style="font-size:16px; font-weight:bold; margin-bottom:2px">XY order</div>
  <div style="font-size:12px; color:#666; margin-bottom:8px">column-major · scans <strong>↓</strong> then →</div>
  <div style="display:inline-grid; grid-template-columns:repeat(4,38px); grid-template-rows:repeat(3,38px); gap:3px; outline:2px solid #ccc">
    <div style="display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:bold;background:rgba(52,119,194,0.12);color:#333">0</div>
    <div style="display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:bold;background:rgba(52,119,194,0.34);color:#333">3</div>
    <div style="display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:bold;background:rgba(52,119,194,0.56);color:#333">6</div>
    <div style="display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:bold;background:rgba(52,119,194,0.77);color:#fff">9</div>
    <div style="display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:bold;background:rgba(52,119,194,0.19);color:#333">1</div>
    <div style="display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:bold;background:rgba(52,119,194,0.41);color:#333">4</div>
    <div style="display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:bold;background:rgba(52,119,194,0.63);color:#fff">7</div>
    <div style="display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:bold;background:rgba(52,119,194,0.85);color:#fff">10</div>
    <div style="display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:bold;background:rgba(52,119,194,0.27);color:#333">2</div>
    <div style="display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:bold;background:rgba(52,119,194,0.48);color:#333">5</div>
    <div style="display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:bold;background:rgba(52,119,194,0.70);color:#fff">8</div>
    <div style="display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:bold;background:rgba(52,119,194,0.92);color:#fff">11</div>
  </div>
  <div style="font-size:11px;color:#999;margin-top:4px">← x (col) →</div>
</div>
<div style="text-align:center">
  <div style="font-size:16px; font-weight:bold; margin-bottom:2px">YX order</div>
  <div style="font-size:12px; color:#666; margin-bottom:8px">row-major · scans <strong>→</strong> then ↓</div>
  <div style="display:inline-grid; grid-template-columns:repeat(4,38px); grid-template-rows:repeat(3,38px); gap:3px; outline:2px solid #ccc">
    <div style="display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:bold;background:rgba(212,100,20,0.12);color:#333">0</div>
    <div style="display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:bold;background:rgba(212,100,20,0.19);color:#333">1</div>
    <div style="display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:bold;background:rgba(212,100,20,0.27);color:#333">2</div>
    <div style="display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:bold;background:rgba(212,100,20,0.34);color:#333">3</div>
    <div style="display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:bold;background:rgba(212,100,20,0.41);color:#333">4</div>
    <div style="display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:bold;background:rgba(212,100,20,0.48);color:#333">5</div>
    <div style="display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:bold;background:rgba(212,100,20,0.56);color:#333">6</div>
    <div style="display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:bold;background:rgba(212,100,20,0.63);color:#fff">7</div>
    <div style="display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:bold;background:rgba(212,100,20,0.70);color:#fff">8</div>
    <div style="display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:bold;background:rgba(212,100,20,0.77);color:#fff">9</div>
    <div style="display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:bold;background:rgba(212,100,20,0.85);color:#fff">10</div>
    <div style="display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:bold;background:rgba(212,100,20,0.92);color:#fff">11</div>
  </div>
  <div style="font-size:11px;color:#999;margin-top:4px">← x (col) →</div>
</div>
</div>
<div style="text-align:center;font-size:11px;color:#aaa;margin-top:8px">cell number = byte position · lighter = stored first</div>
</div>

<!-- Graphic 2: dimension types — z-stack, time series, multichannel (vertical) -->
<div v-click="[1, 2]" class="abs" style="left:520px; top:108px; width:440px">
<div style="display:flex; flex-direction:column; align-items:center; justify-content:space-evenly; height:420px">

  <!-- Z-stack: 4 blue planes -->
  <div style="text-align:center">
    <div style="position:relative; width:222px; height:107px; margin:0 auto">
      <div style="position:absolute; left:0; top:0; width:180px; height:65px; background:rgba(70,130,180,0.28); border:1.5px solid #4682b4">
        <div style="position:absolute; top:3px; left:4px; font-size:11px; color:#4682b4">z=3</div>
      </div>
      <div style="position:absolute; left:14px; top:14px; width:180px; height:65px; background:rgba(70,130,180,0.44); border:1.5px solid #4682b4"></div>
      <div style="position:absolute; left:28px; top:28px; width:180px; height:65px; background:rgba(70,130,180,0.62); border:1.5px solid #4682b4"></div>
      <div style="position:absolute; left:42px; top:42px; width:180px; height:65px; background:rgba(70,130,180,0.82); border:1.5px solid #4682b4">
        <div style="position:absolute; top:3px; left:4px; font-size:11px; color:#1a4a7a">z=0</div>
        <div style="position:absolute; bottom:4px; right:6px; font-size:11px; color:#1a4a7a; font-weight:bold">XY</div>
      </div>
    </div>
    <div style="font-size:14px; font-weight:bold; margin-top:6px">Z-stack &nbsp;<span style="color:#888; font-weight:normal; font-size:12px">XYZ</span></div>
  </div>

  <!-- Multichannel: TRITC (amber), FITC (yellow-green), DAPI (blue) -->
  <div style="text-align:center">
    <div style="position:relative; width:216px; height:101px; margin:0 auto">
      <div style="position:absolute; left:0; top:0; width:180px; height:65px; background:rgba(var(--tritc-rgb),0.55); border:1.5px solid var(--tritc-border)">
        <div style="position:absolute; top:3px; right:6px; font-size:11px; color:#7a5500; font-weight:bold">TRITC</div>
      </div>
      <div style="position:absolute; left:18px; top:18px; width:180px; height:65px; background:rgba(var(--fitc-rgb),0.55); border:1.5px solid var(--fitc-border)">
        <div style="position:absolute; top:3px; right:6px; font-size:11px; color:#3d6000; font-weight:bold">FITC</div>
      </div>
      <div style="position:absolute; left:36px; top:36px; width:180px; height:65px; background:rgba(var(--dapi-rgb),0.65); border:1.5px solid var(--dapi-border)">
        <div style="position:absolute; top:3px; right:6px; font-size:11px; color:#00008b; font-weight:bold">DAPI</div>
        <div style="position:absolute; bottom:4px; right:6px; font-size:11px; color:#00008b; font-weight:bold">XY</div>
      </div>
    </div>
    <div style="font-size:14px; font-weight:bold; margin-top:6px">Multichannel &nbsp;<span style="color:#888; font-weight:normal; font-size:12px">XYC</span></div>
  </div>

  <!-- Time + Multichannel: 2 time points × 3 channels, 5px intra-group offset, 18px inter-group gap -->
  <div style="text-align:center">
    <div style="position:relative; width:218px; height:103px; margin:0 auto">
      <!-- t=1 group (back) -->
      <div style="position:absolute; left:0; top:0; width:180px; height:65px; background:rgba(var(--tritc-rgb),0.42); border:1.5px solid var(--tritc-border)"></div>
      <div style="position:absolute; left:5px; top:5px; width:180px; height:65px; background:rgba(var(--fitc-rgb),0.45); border:1.5px solid var(--fitc-border)"></div>
      <div style="position:absolute; left:10px; top:10px; width:180px; height:65px; background:rgba(var(--dapi-rgb),0.5); border:1.5px solid var(--dapi-border)">
        <div style="position:absolute; top:3px; left:4px; font-size:10px; color:#fff; font-weight:bold">t=1</div>
      </div>
      <!-- t=0 group (front), 18px gap from t=1 -->
      <div style="position:absolute; left:28px; top:28px; width:180px; height:65px; background:rgba(var(--tritc-rgb),0.55); border:1.5px solid var(--tritc-border)"></div>
      <div style="position:absolute; left:33px; top:33px; width:180px; height:65px; background:rgba(var(--fitc-rgb),0.55); border:1.5px solid var(--fitc-border)"></div>
      <div style="position:absolute; left:38px; top:38px; width:180px; height:65px; background:rgba(var(--dapi-rgb),0.65); border:1.5px solid var(--dapi-border)">
        <div style="position:absolute; top:3px; left:4px; font-size:10px; color:#fff; font-weight:bold">t=0</div>
        <div style="position:absolute; bottom:4px; right:6px; font-size:11px; color:#00008b; font-weight:bold">XY</div>
      </div>
    </div>
    <div style="font-size:14px; font-weight:bold; margin-top:6px">Time + Multichannel &nbsp;<span style="color:#888; font-weight:normal; font-size:12px">XYCT</span></div>
  </div>

</div>
</div>

<!-- Graphic 3: Fiji Image Properties dialog -->
<div v-click="2" class="abs" style="left:520px; top:108px; width:440px; text-align:center">
<div style="font-size:20px; font-weight:bold; margin-bottom:8px">Image → Properties</div>
<img src="/media/s11-picture-9.png" style="width:100%; max-height:340px; object-fit:contain">
</div>

<!-- Graphic 4: OME logo below text on click 3 -->
<div v-click="4" class="abs" style="left:32px; top:355px; width:280px">
<img src="/media/ome-logo.png" style="width:100%; object-fit:contain">
</div>


---

# Quality In → Quality Out

<img class="abs" src="/media/s14-picture-3.png" style="left:521px; top:125px; width:402px; height:422px">

<div class="abs" style="left:32px; top:125px; width:508px; font-size:29px">

- A clean image is the first step to successful analysis
- Common artifacts include:
  - Scratches
  - Debris
  - Poor Staining
  - Uneven Illumination
  - Spectral Crosstalk/Bleed-Through
  - Improper Stitching
  - Focus Drift
  - Saturated Signal
  - Inconsistent Parameters

</div>

<BlockArrow dir="right" x="187" y="290" w="340" h="17" color="#FF0000" />

<div class="abs" style="left:688px; top:125px; width:234px; font-size:18px; text-align:right">

<span style="color:#FFFFFF">*Mouse, retrosplenial cortex, 10x, Nikon A1R confocal*</span>

</div>

<div class="abs" style="left:688px; top:517px; width:234px; font-size:18px; text-align:right">

<span style="color:#FFFFFF">*Noelle Cataldo*</span>

</div>

<div class="abs" style="left:472px; top:73px; width:500px; height:25px; font-size:14px; background:#FFFFFF; border:1px solid #104862">

<https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3002167>

</div>

<!--
Reference Kevin’s paper about good data in and good data out : https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3002167
-->

---
class: fiji-slide
---

# Opening images in Fiji

<div class="abs" style="left:20px; top:127px; width:310px; font-size:24px; --nest:1.00">

- Drag and drop
- File → Open…
- Bio-Formats supports **many** proprietary file formats
  - `.nd2` for Nikon
  - `.czi` for Zeiss
  - `.sld` for 3i
  - ...

</div>

<!-- TODO Consider replacing with a GIF, maybe opening https://zenodo.org/records/5277605-->
<!-- TODO Highlight Virtual Stacks -->
<img class="abs" src="/media/s25-picture-7.png" style="left:335px; top:132px; width:625px; height:383px">

---
class: fiji-slide
---

# Visualizing your data

<img class="abs" src="/media/s27-picture-6.png" style="left:341px; top:215px; width:213px; height:244px">

<img class="abs" src="/media/s27-picture-8.png" style="left:805px; top:211px; width:143px; height:240px">

<img class="abs" src="/media/s27-picture-10.png" style="left:573px; top:215px; width:201px; height:244px">

<div class="abs" style="left:21px; top:141px; width:320px; font-size:24px">

- 2D is an image
- 3D has a slider
- (4+)D "Hyperstacks" have multiple sliders
- `File → Open Samples` for examples of each!

</div>

<div class="abs" style="left:419px; top:162px; width:56px; font-size:29px">

**2D**

</div>

<div class="abs" style="left:639px; top:162px; width:56px; font-size:29px">

**3D**

</div>

<div class="abs" style="left:792px; top:162px; width:170px; font-size:29px">

**Hyperstack**

</div>

<!--
Z stack → Series of images taken at different focal planes along the depth of a sample
Talk about max intensity projection
-->

---
class: fiji-slide
hide: true
---

# There are multiple ways to look at 3D data: *Reslice*

<div class="abs" style="left:66px; top:111px; width:125px; font-size:20px; text-align:center">

Z Stack

</div>

<div class="abs" style="left:444px; top:133px; width:414px; font-size:20px; text-align:center">

**To get a different view:**

`Image → Stacks → Reslice`

</div>

<img class="abs" src="/media/s28-picture-7.png" style="left:11px; top:181px; width:293px; height:354px">

<img class="abs" src="/media/s28-picture-19.png" style="left:363px; top:214px; width:253px; height:290px">

<img class="abs" src="/media/s28-picture-21.png" style="left:652px; top:247px; width:306px; height:224px">

---
class: fiji-slide
---

# There are multiple ways to look at 3D data: *Orthogonal and 3D*

<div class="abs" style="left:66px; top:111px; width:125px; font-size:20px; text-align:center">

Z Stack

</div>

<div class="abs" style="left:256px; top:107px; width:414px; font-size:20px; text-align:center">

Orthogonal View

`Image → Stacks → Orthogonal Views`

</div>

<div class="abs" style="left:642px; top:104px; width:320px; font-size:20px; text-align:center">

3D View

`Plugins → 3D Viewer`

</div>

<img class="abs" src="/media/s28-picture-7.png" style="left:11px; top:181px; width:293px; height:354px">

<img class="abs" src="/media/s29-picture-9.png" style="left:518px; top:170px; width:97px; height:221px">

<img class="abs" src="/media/s29-picture-13.png" style="left:325px; top:408px; width:193px; height:128px">

<img class="abs" src="/media/s29-picture-15.png" style="left:325px; top:170px; width:193px; height:237px">

<img class="abs" src="/media/s29-picture-17.png" style="left:646px; top:181px; width:323px; height:343px">

---
class: fiji-slide
---

# Look up tables (LUT) **map** pixel values color assignments

<style>
.slidev-layout.default h1 { font-size: 40px; }
</style>

<div class="abs" style="left:569px; top:152px; width:382px; font-size:24px; --nest:1.00">

<!-- TODO: Show some use cases? e.g. when glasbey is useful-->
- Does **not** change the data in the image
  - "1 is red, 2 is blue, ..."
- LUT **can** change user perceptions
  - Color-blindness
- Fiji offers calibration bars
- *Use `glasbey` for label images*
- *Use `HiLo` during acquisition*
  - Just dark vs. no signal
  - Just bright vs. saturated

</div>

<img class="abs" src="/media/s26-google-shape-332-p27.png" style="left:29px; top:126px; width:495px; height:190px">

<img class="abs" src="/media/s26-google-shape-334-p27.png" style="left:37px; top:323px; width:296px; height:213px">

<img class="abs" src="/media/s26-google-shape-333-p27.png" style="left:348px; top:323px; width:181px; height:206px">

---
class: fiji-slide
---

# Add a scale bar for publication images

<div class="abs" style="left:74px; top:123px; width:506px; font-size:24px">

`Analyze → Tools → Scale Bar`

</div>

<img class="abs" src="/media/s34-picture-5.png" style="left:639px; top:126px; width:286px; height:404px">

<img class="abs" src="/media/s34-picture-9.png" style="left:74px; top:234px; width:475px; height:296px">

<div class="abs" style="left:77px; top:239px; width:234px; font-size:18px">

<span style="color:#FFFFFF">*Mouse, hippocampus, 10x, Nikon A1R confocal*</span>

</div>

<div class="abs" style="left:74px; top:500px; width:234px; font-size:18px">

<span style="color:#FFFFFF">*Noelle Cataldo*</span>

</div>

<!--
Come much earlier
-->

---
layout: section
---

# Quantitative Measurements

The output

<div style="width:500px; margin: 0 auto">

```mermaid
%%{init: {"theme": "neutral", "themeVariables": {"fontSize": "20px", "edgeLabelBackground": "#faf8f3"}, "flowchart": {"wrappingWidth": 400}}}%%
flowchart LR
  C["Digital<br>image"] -->|"image analysis"| D["Quantitative<br>measurements"]
  classDef endpoint fill:#dde8e0,stroke:#7f9c88
```

</div>

---

# What questions can be answered with quantitative measurements?

<!-- TODO a grid here could be nice -->

<div class="abs" style="left:33px; top:131px; width:420px; font-size:29px">

- How many X are there?

<v-click>

- What shape/size is X?

</v-click>
<v-click>

- How bright is X?

</v-click>
<v-click>

- Does X move?

</v-click>
<v-click>

- Does X appear near Y?

</v-click>
<v-click>

*...but how can we get from images to measurements?*

</v-click>

</div>

<div v-click-hide="1" class="abs" style="left:464px; top:80px; width:480px; height:440px; display:flex; align-items:center; justify-content:center">
  <CountGraphic />
</div>

<div v-click="[1, 2]" class="abs" style="left:464px; top:80px; width:480px; height:440px; display:flex; align-items:center; justify-content:center">
  <ShapeGraphic />
</div>

<div v-click="[2, 3]" class="abs" style="left:464px; top:80px; width:480px; height:440px; display:flex; align-items:center; justify-content:center">
  <IntensityGraphic />
</div>

<div v-click="[3, 4]" class="abs" style="left:464px; top:80px; width:480px; height:440px; display:flex; align-items:center; justify-content:center">
  <MotionGraphic />
</div>

<div v-click="4" class="abs" style="left:464px; top:80px; width:480px; height:440px; display:flex; align-items:center; justify-content:center">
  <ColocGraphic />
</div>

---

# Image Analysis, *simplified*

<div style="width:800px; margin: 40px auto 0">

```mermaid
%%{init: {"theme": "neutral", "themeVariables": {"fontSize": "20px", "edgeLabelBackground": "#faf8f3"}, "flowchart": {"wrappingWidth": 200}}}%%
flowchart LR
  C["Digital<br>image"] --> analysis --> D["Quantitative<br>measurements"]
  subgraph analysis ["Image Analysis"]
    direction LR
    A["Preprocessing"] --> B["Segmentation"] --> M["Measurement"]
  end
  classDef endpoint fill:#dde8e0,stroke:#7f9c88
  class C,D endpoint
```

</div>

<Line v-click="1" x1="320" y1="375" x2="350" y2="270" color="#e57373" width="2" arrow="end" />
<div v-click="1" class="abs" style="left:220px; top:378px; width:200px; font-size:16px; text-align:center; color:#d32f2f">
  Making it easy to spot objects of interest
</div>

<Line v-click="2" x1="490" y1="455" x2="490" y2="270" color="#e57373" width="2" arrow="end" />
<div v-click="2" class="abs" style="left:390px; top:458px; width:200px; font-size:16px; text-align:center; color:#d32f2f">
  Identifying where objects are
</div>

<Line v-click="3" x1="660" y1="375" x2="640" y2="270" color="#e57373" width="2" arrow="end" />
<div v-click="3" class="abs" style="left:560px; top:378px; width:200px; font-size:16px; text-align:center; color:#d32f2f">
  Quantifying properties of each object
</div>

---
layout: section
---

# Segmentation

Finding the objects

<div style="width:800px; margin: 40px auto 0">

```mermaid
%%{init: {"theme": "neutral", "themeVariables": {"fontSize": "20px", "edgeLabelBackground": "#faf8f3"}, "flowchart": {"wrappingWidth": 200}}}%%
flowchart LR
  C["Digital<br>image"] --> analysis --> D["Quantitative<br>measurements"]
  subgraph analysis ["Image Analysis"]
    direction LR
    A["Preprocessing"] --> B["Segmentation"] --> M["Measure"]
  end
  classDef endpoint fill:#dde8e0,stroke:#7f9c88
  classDef highlight fill:#e57373,stroke:#d32f2f
  class C,D endpoint
  class B highlight
```

</div>

---

# Segmentation answers "where are my objects?"

- Derives pixel labels or object boundaries against an image
- Generally based on pixel intensity

<img class="abs" src="/media/blobs_segmentation_overview.png" style="left:100px; top:250px;width:743px; height:271px">

---
class: fiji-slide
---

# Classical segmentation in Fiji

<img class="abs" src="/media/blobs.png" style="left:20px; top:210px; width:185px">
<div class="abs" style="left:20px; top:178px; width:185px; font-size:14px; font-weight:bold; text-align:center">Input image</div>

<img v-click="1" class="abs" src="/media/blobs_thresholding.png" style="left:265px; top:210px; width:185px">
<img v-click="1" class="abs" src="/media/blobs_thresholding_widget.png" style="left:462px; top:230px; width:195px">
<div v-click="1" class="abs" style="left:245px; top:178px; width:420px; font-size:14px; font-weight:bold; text-align:center"><code>Ctrl+Shift+T</code> to threshold</div>

<div v-click="2" class="abs" style="left:440px; top:482px; width:120px; font-size:12px; color:#c03000; text-align:center; line-height:1.3">
  <strong>Dark background</strong><br>
  <span style="font-size:10px">Select if your objects are bright</span>
</div>
<div v-click="2" class="abs" style="left:556px; top:482px; width:120px; font-size:12px; color:#004080; text-align:center; line-height:1.3">
  <strong>Stack histogram</strong><br>
  <span style="font-size:10px">Select for a timelapse / z-stack</span>
</div>

<img v-click="3" class="abs" src="/media/blobs_thresholded.png" style="left:755px; top:210px; width:185px">
<div v-click="3" class="abs" style="left:733px; top:178px; width:215px; font-size:14px; font-weight:bold; text-align:center">Click <code>Apply</code> to threshold</div>

<svg class="abs" style="left:0; top:0; width:980px; height:551px; pointer-events:none" viewBox="0 0 980 551" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr8" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0,0 8,3 0,6" fill="#333"/>
    </marker>
    <marker id="arr8-o" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0,0 8,3 0,6" fill="#c03000"/>
    </marker>
    <marker id="arr8-b" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0,0 8,3 0,6" fill="#004080"/>
    </marker>
  </defs>
  <g v-click="1">
    <path d="M 205 316 H 260" stroke="#333" stroke-width="1.5" fill="none" marker-end="url(#arr8)"/>
  </g>
  <g v-click="2">
    <!-- Dark background highlight -->
    <rect x="478" y="372" width="81" height="16" fill="rgba(192,48,0,0.1)" stroke="#c03000" stroke-width="1.5" rx="2"/>
    <!-- Stack histogram highlight -->
    <rect x="560" y="372" width="84" height="16" fill="rgba(0,64,128,0.1)" stroke="#004080" stroke-width="1.5" rx="2"/>
    <!-- Callout arrows -->
    <path d="M 500 479 L 519 392" stroke="#c03000" stroke-width="1.2" fill="none" marker-end="url(#arr8-o)"/>
    <path d="M 616 479 L 605 392" stroke="#004080" stroke-width="1.2" fill="none" marker-end="url(#arr8-b)"/>
  </g>
  <g v-click="3">
    <path d="M 657 358 Q 700 358 750 316" stroke="#333" stroke-width="1.5" fill="none" marker-end="url(#arr8)"/>
  </g>
</svg>

---
class: fiji-slide
hide: true <!-- TODO: What to do with this...-->
---

# Pitfalls in Classical Segmentation

<div class="abs" style="left:36px; top:95px; width:420px; font-size:20px">

**1. Choose the right threshold**
- Fiji's preset thresholds differ — try them on your data

</div>

<div class="abs" style="left:510px; top:95px; width:420px; font-size:20px">

**2. Touching objects → use watershed**
- Process → Binary → Watershed

</div>

<img class="abs" src="/media/s61-picture-7.png" style="left:36px; top:175px; width:205px; height:202px">

<div class="abs" style="left:50px; top:187px; width:95px; height:28px; font-size:18px; background:#FFFFFF">

**Default**

</div>

<img class="abs" src="/media/s61-picture-10.png" style="left:258px; top:175px; width:205px; height:204px">

<div class="abs" style="left:272px; top:187px; width:130px; height:28px; font-size:18px; background:#FFFFFF">

**Percentile**

</div>

<img class="abs" src="/media/s64-picture-2.png" style="left:510px; top:175px; width:140px; height:147px">

<BlockArrow dir="right" x="653" y="228" w="25" h="35" color="#FF0000" />

<img class="abs" src="/media/s64-picture-12.png" style="left:681px; top:175px; width:140px; height:147px">

<BlockArrow dir="right" x="824" y="228" w="25" h="35" color="#FF0000" />

<img class="abs" src="/media/s64-picture-13.png" style="left:852px; top:175px; width:140px; height:147px">

<!--
Default → Calculates mean background and mean object intensity
Percentile → Assumes a certain percentage of pixels are in the foreground
In the end, just use whichever works for your data
Be sure to pay attention to the "Dark Background" box and check when it applies
Watershed: separates touching objects that merge after thresholding
-->

---
class: fiji-slide
---

# Labkit: a GUI approach to segmentation

<div class="abs" style="left:0px; top:113px; width:707px; font-size:20px; --nest:1.00">

- `Plugins → Labkit → Open Current Image With Labkit`
- Manually draw on image to indicate foreground and background
- Export to Fiji or save to TIFF/HDF5 when done

</div>

<img class="abs" src="/media/s62-picture-5.png" style="left:12px; top:208px; width:464px; height:317px">

<img class="abs" src="/media/s62-picture-7.png" style="left:485px; top:185px; width:214px; height:174px">

<img class="abs" src="/media/s62-picture-9.png" style="left:626px; top:246px; width:221px; height:177px">

<img class="abs" src="/media/s62-picture-11.png" style="left:778px; top:330px; width:182px; height:181px">

<BlockArrow dir="right" x="593" y="232" w="69" h="58" color="#96DCF8" rotate="45.224" />

<BlockArrow dir="right" x="750" y="316" w="69" h="58" color="#96DCF8" rotate="45.224" />

---
class: fiji-slide
---

# StarDist: Segmentation via Deep Learning

<img class="abs" src="/media/s63-picture-2.png" style="left:661px; top:121px; width:141px; height:140px">

- Segments cells using deep learning which can be done with pretrained models
- Broad platform support via `cellcast`
  - `File → New → Script...`
  - `Templates → Appose → Stardist cellcast (Python (Appose))`
  - `Run` button runs on the active image

<img class="abs" src="/media/s63-picture-4.png" style="left:525px; top:284px; width:419px; height:242px">

---

# Classical vs ML Segmentation

<div class="abs" style="left:20px; top:100px; width:440px; font-size:20px">

**Classical** (thresholding, watershed)

✅ No training data needed
<br>
✅ Fast to set up and easy to debug
<br>
✅ Interpretable, explicit parameters
<br>

</div>

<Line x1="490" y1="90" x2="490" y2="210" color="#aaaaaa" width="2" />

<div class="abs" style="left:510px; top:100px; width:440px; font-size:20px">

**ML-based** (StarDist, Cellpose, …)

✅ Robust to intensity and background variation
<br>
✅ Handles touching and irregular shapes
<br>
✅ Generalizes to new conditions
<br>

</div>

<img v-click="1" class="abs" src="/media/hela_threshold_naive.png" style="left:25px; top:270px; width:300px">
<div v-click="1" class="abs" style="left:25px; top:524px; width:300px; text-align:center; font-size:14px; color:#555">Otsu Threshold</div>

<img v-click="2" class="abs" src="/media/hela_threshold_stardist.png" style="left:335px; top:270px; width:300px">
<div v-click="2" class="abs" style="left:335px; top:524px; width:300px; text-align:center; font-size:14px; color:#555">StarDist Segmentation</div>

<!-- Gaussian blur of sigma=20, then subtracted from the original-->
<img v-click="3" class="abs" src="/media/hela_threshold_preprocessed.png" style="left:645px; top:270px; width:300px">
<div v-click="3" class="abs" style="left:645px; top:524px; width:300px; text-align:center; font-size:14px; color:#555"><em>Gaussian Highpass</em> + Otsu Threshold</div>

---
layout: section

---

# Preprocessing

readying your data for segmentation

<div style="width:800px; margin: 40px auto 0">

```mermaid
%%{init: {"theme": "neutral", "themeVariables": {"fontSize": "20px", "edgeLabelBackground": "#faf8f3"}, "flowchart": {"wrappingWidth": 200}}}%%
flowchart LR
  C["Digital<br>image"] --> analysis --> D["Quantitative<br>measurements"]
  subgraph analysis ["Image Analysis"]
    direction LR
    A["Preprocessing"] --> B["Segmentation"] --> M["Measure"]
  end
  classDef endpoint fill:#dde8e0,stroke:#7f9c88
  classDef highlight fill:#e57373,stroke:#d32f2f
  class C,D endpoint
  class A highlight
```

</div>

---

# Sometimes your objects don't fit in the FOV

<div class="abs" style="left:42px; top:133px; width:516px; font-size:24px; --nest:1.00">

- Imaging large samples at high resolution requires a tiled scan
  - Will not fit in single field of view

</div>
---
class: fiji-slide
---

# Stitching in Fiji

<div class="abs" style="left:42px; top:133px; width:516px; font-size:24px; --nest:1.00">

- Create one large image from many tiles
- `Plugins → Stitching → Grid/Collection stitching`
- `Positions from file` option uses image metadata
  - Other options compute tile positions given parameters

</div>

<img class="abs" src="/media/s57-picture-4.png" style="left:637px; top:118px; width:233px; height:426px">

---
hide: true
---

# How do I stitch tiled images with the Grid/Collection Stitching plugin?

<div class="abs" style="left:42px; top:122px; width:414px; font-size:24px; --nest:1.00">

- Plugins → Stitching → Grid/Collection Stitching
- Select the Type and Order based on how images were collected/labeled
- Input necessary parameters including:
  - Grid Size
  - Overlap
  - First file index i → Are your tiles labeled in order 1, 2, 3, etc
  - File names for tiles → \[name\]-{i} where i is the file index
  - Unselect compute overlap

</div>

<img class="abs" src="/media/s58-picture-4.png" style="left:582px; top:148px; width:72px; height:91px">

<img class="abs" src="/media/s58-picture-6.png" style="left:706px; top:145px; width:70px; height:92px">

<img class="abs" src="/media/s58-picture-8.png" style="left:820px; top:148px; width:71px; height:91px">

<img class="abs" src="/media/s58-picture-10.png" style="left:582px; top:277px; width:76px; height:92px">

<img class="abs" src="/media/s58-picture-12.png" style="left:710px; top:277px; width:67px; height:90px">

<img class="abs" src="/media/s58-picture-14.png" style="left:825px; top:277px; width:65px; height:92px">

<img class="abs" src="/media/s58-picture-16.png" style="left:582px; top:409px; width:70px; height:91px">

<img class="abs" src="/media/s58-picture-18.png" style="left:710px; top:409px; width:67px; height:91px">

<img class="abs" src="/media/s58-picture-20.png" style="left:824px; top:409px; width:72px; height:90px">

<Line x1="658" y1="182" x2="706" y2="182" color="#FF0000" width="5" arrow="end" />

<Line x1="778" y1="182" x2="826" y2="182" color="#FF0000" width="5" arrow="end" />

<Line x1="654" y1="319" x2="703" y2="319" color="#FF0000" width="5" arrow="end" />

<Line x1="778" y1="319" x2="826" y2="319" color="#FF0000" width="5" arrow="end" />

<Line x1="654" y1="451" x2="703" y2="451" color="#FF0000" width="5" arrow="end" />

<Line x1="779" y1="451" x2="828" y2="451" color="#FF0000" width="5" arrow="end" />

<Line x1="820" y1="224" x2="654" y2="277" color="#FF0000" width="5" arrow="end" />

<Line x1="820" y1="369" x2="662" y2="409" color="#FF0000" width="5" arrow="end" />

---

# Image histograms aid image analysis

<div class="abs" style="left:0px; top:106px; width:460px; font-size:22px; --nest:1.00">

- Describes distribution of pixel intensities in your image
- Segmentation separates foreground (**signal**) from background (**noise**)
  - *harder when they overlap in the histogram*
- Compressed/cutoff histograms mean low contrast
  - *Post-hoc contrast adjustment is a workaround*

</div>

<img class="abs" src="/media/m51.png" style="left:660px; top:100px; width:290px">

<img class="abs" src="/media/m51_b&c.png" style="left:480px; top:320px; width:240px">

---
class: fiji-slide
---

# Adjust Brightness/Contrast in Fiji

<div class="abs" style="left:0px; top:127px; width:453px; font-size:24px; --nest:1.00">

- `Process → Adjust → Brightness/Contrast`
- Good way to visualize data without changing the pixel values
- Linear transformation!
  - **If "Apply" is selected pixel values will change**

</div>

<img class="abs" src="/media/s31-picture-5.png" style="left:473px; top:133px; width:217px; height:372px">

<img class="abs" src="/media/s31-picture-12.png" style="left:728px; top:135px; width:217px; height:368px">

<img class="abs" src="/media/s31-picture-14.png" style="left:658px; top:223px; width:104px; height:209px">

<BlockArrow dir="right" x="651" y="180" w="116" h="29" color="#FF0000" />

<BlockArrow dir="right" x="658" y="448" w="116" h="29" color="#FF0000" />

---
class: fiji-slide
---

# Contrast-Limited Adaptive Histogram Equalization

<div class="abs" style="left:0px; top:107px; width:531px; font-size:24px; --nest:1.00">

- `Process → Enhance Local Contrast (CLAHE)`
- Enhances contrast **locally**
  - **non-linear**
  - Good for uneven illumination
  - Handles near-constant regions nicely
<!-- TODO: Some graphical illustrations of these concepts might be nice-->
- Parameters
  - `Block Size` → Defines region around a pixel where histogram is equalized
  - `Histogram Bins` → Number of bins used for equalization
  - `Max Slope` → Large values = maximum local contrast whereas 1 = original image

</div>

<img class="abs" src="/media/s33-picture-5.png" style="left:525px; top:199px; width:211px; height:338px">

<img class="abs" src="/media/s33-picture-12.png" style="left:761px; top:199px; width:211px; height:338px">

<img class="abs" src="/media/s33-picture-8.png" style="left:652px; top:150px; width:192px; height:174px">

<BlockArrow dir="right" x="690" y="484" w="116" h="29" color="#FF0000" />

<LinkButton left="613" top="114" width="271" height="31" href="https://imagej.net/plugins/clahe" icon="🔧" label="Plugin Documentation" />

<!--
If you don’t know what the input parameters mean, play around until you figure out what works for your data.
-->

---

# What can we do when data is noisy?

<!-- TODO: Add in nuclei1-->

<!-- TODO: Make a script to recreate -->
<img class="abs" src="/media/nuclei2_plus_threshold.gif" style="left:31px; top:167px; width:567px;">

<div class="abs" style="left:627px; top:167px; width:321px; font-size:20px">

Data info:

- Widefield fluorescence, 20x/0.75NA
- Voxel dimensions: 0.124x0.124x0.200 um
- Emission peak wavelength: 500 nm

Source:

- Simulated data from the Light Microscopy Research Group (LMRG) Image Analysis Study

</div>

---

# Mean filter multiplication suppresses noise

<div class="abs" style="left:690px; top:148px; width:275px; font-size:20px">

***Mean filter***: computes *local* average, *suppressing noise*
<br>

***Multiply***:
- nuclei (bright × high mean) amplified
- noise spikes (bright × low mean) suppressed.
<br>

***Net effect***: pushes the two populations further apart in intensity.

</div>

<div class="abs" style="left:34px; top:118px; width:245px; font-size:14px; font-weight:bold; text-align:center; color:#666">Without mean multiplication</div>
<img class="abs" src="/media/nuclei2.png" style="left:34px; top:148px; width:245px">
<img class="abs" src="/media/nuclei2_otsu.png" style="left:163px; top:311px; width:116px">

<div class="abs" style="left:368px; top:118px; width:245px; font-size:14px; font-weight:bold; text-align:center; color:#666">With mean multiplication</div>
<img class="abs" src="/media/nuclei2_mean_multiplied.png" style="left:368px; top:148px; width:245px">
<img class="abs" src="/media/nuclei2_mean_multiplied_otsu.png" style="left:497px; top:311px; width:116px">

---
class: fiji-slide
---

# Mean filter multiplication in Fiji

<img class="abs" src="/media/nuclei2.png" style="left:20px; top:115px; width:185px">
<div class="abs" style="left:20px; top:82px; width:185px; font-size:14px; font-weight:bold; text-align:center">Input image</div>

<img v-click="1" class="abs" src="/media/nuclei2_mean.png" style="left:225px; top:325px; width:185px">
<div v-click="1" class="abs" style="left:192px; top:300px; width:250px; font-size:14px; font-weight:bold; text-align:center">Mean filter (<code>radius=5</code>)</div>

<img v-click="2" class="abs" src="/media/nuclei2_mean_multiplied.png" style="left:435px; top:115px; width:185px">
<div v-click="2" class="abs" style="left:435px; top:82px; width:185px; font-size:14px; font-weight:bold; text-align:center">Multiply</div>

<img v-click="3" class="abs" src="/media/nuclei2_mean_multiplied_otsu.png" style="left:645px; top:325px; width:185px">
<div v-click="3" class="abs" style="left:608px; top:300px; width:258px; font-size:14px; font-weight:bold; text-align:center">Otsu threshold</div>

<svg class="abs" style="left:0; top:0; width:980px; height:551px; pointer-events:none" viewBox="0 0 980 551" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-mean" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0,0 8,3 0,6" fill="#333"/>
    </marker>
  </defs>
  <g v-click="1">
    <path d="M 112 355 V 402 Q 112 417 127 417 H 220" stroke="#333" stroke-width="1.5" fill="none" marker-end="url(#arr-mean)"/>
  </g>
  <g v-click="2">
    <!-- branch from input image right-center -->
    <path d="M 215 207 H 420" stroke="#333" stroke-width="1.5" fill="none"/>
    <!-- branch from mean filter top-center, curves up then right to junction -->
    <path d="M 317 295 V 220 Q 317 207 332 207 H 420" stroke="#333" stroke-width="1.5" fill="none"/>
    <!-- merged arrow into multiply image -->
    <path d="M 420 207 H 430" stroke="#333" stroke-width="1.5" fill="none" marker-end="url(#arr-mean)"/>
  </g>
  <g v-click="3">
    <path d="M 527 355 V 402 Q 527 417 542 417 H 640" stroke="#333" stroke-width="1.5" fill="none" marker-end="url(#arr-mean)"/>
  </g>
</svg>

---
class: fiji-slide
---

# Background subtraction improved thresholding

<img class="abs" src="/media/s43-google-shape-588-p91.gif" style="left:178px; top:119px; width:623px; height:415px">

<div class="abs" style="left:146px; top:213px; width:95px; transform:rotate(-90deg); font-size:12px; text-align:center">

<span style="color:#FFFF00">**nuclei 2**</span>

</div>

<div class="abs" style="left:146px; top:406px; width:95px; transform:rotate(-90deg); font-size:12px; text-align:center">

<span style="color:#FFFF00">**nuclei 2**</span>

</div>

---
class: fiji-slide
---

# Aside: Image Math in Fiji

<div class="abs" style="left:23px; top:132px; width:501px; font-size:20px; --nest:1.00">

- `Process → Image Calculator...`

</div>

<div class="abs" style="left:533px; top:132px; width:447px; font-size:20px; --nest:1.00">

Binary operations:
- Add, Subtract, Divide, Multiply
- AND, OR, XOR
  - *AND* helps find overlapping particles
- Min, Max, Average
- Difference: `|image1 - image2|`
- Copy: `image1 = image2`
- Transparent-Zero: `image1` is transparent where `image2 = 0`

</div>

<img class="abs" src="/media/s39-picture-10.png" style="left:117px; top:200px; width:280px; height:251px">

<div class="abs" style="left:130px; top:375px; width:250px; height:26px; border:2px solid #FF0000; padding:0"></div>

<div class="abs" style="left:150px; top:480px; width:305px; font-size:15px; font-weight:bold; color:#CC0000">Don't overwrite your data!</div>
<Line x1="220" y1="480" x2="220" y2="410" color="#CC0000" width="2" arrow="end" />

---
<!-- TODO: Ask Ed about this slide-->
hide: true
---

# Surface plots are a good way to visualize this change in pixel value: *Before*

<img class="abs" src="/media/s44-google-shape-531-p86.png" style="left:331px; top:151px; width:292px; height:249px">

<img class="abs" src="/media/s44-google-shape-532-p86.png" style="left:643px; top:150px; width:292px; height:249px">

<div class="abs" style="left:357px; top:107px; width:232px; font-size:18px; text-align:center">

*Nuclei 1 crop surface plot*

</div>

<div class="abs" style="left:670px; top:107px; width:232px; font-size:18px; text-align:center">

*Nuclei 2 crop surface plot*

</div>

<div class="abs" style="left:33px; top:162px; width:277px; font-size:24px; --nest:1.00">

- Surface plot → 3D visualization tool that maps intensities of a 2D image
  - Creates a topographic map
- Analyze → Surface Plot…

</div>

<img class="abs" src="/media/s41-google-shape-540-p87.png" style="left:423px; top:409px; width:135px; height:135px">

<img class="abs" src="/media/s41-google-shape-543-p87.png" style="left:732px; top:409px; width:135px; height:135px">

---
hide: true
---

# Surface plots are a good way to visualize this change in pixel value: *After*

<div class="abs" style="left:211px; top:137px; width:232px; font-size:18px; text-align:center">

*Nuclei 1 crop surface plot*

</div>

<div class="abs" style="left:683px; top:139px; width:232px; font-size:18px; text-align:center">

*Nuclei 2 crop surface plot*

</div>

<img class="abs" src="/media/s45-google-shape-571-p89.png" style="left:180px; top:169px; width:292px; height:248px">

<img class="abs" src="/media/s45-google-shape-572-p89.png" style="left:650px; top:168px; width:300px; height:255px">

<div class="abs" style="left:253px; top:458px; width:475px; font-size:18px">

- Decreased background shown by bottom of slope (left)
- Greater range of values

</div>

<img class="abs" src="/media/s41-google-shape-542-p87.png" style="left:16px; top:228px; width:150px; height:150px">

<img class="abs" src="/media/s41-google-shape-545-p87.png" style="left:484px; top:228px; width:154px; height:154px">

---

# What if the background is non-uniform?

<img class="abs" src="/media/s47-google-shape-607-p94.png" style="left:29px; top:133px; width:449px; height:394px">

<div v-click.hide="1" class="abs" style="left:503px; top:141px; width:449px; font-size:24px">

- 100x confocal microscopy.
- 3D data (X, Y, Channel).
- Must deal with large hazy structures (*i.e.* nuclear shadow).
- Must preserve puncta.

</div>

<div v-click.hide="1" class="abs" style="left:195px; top:369px; width:56px; height:52px; border:2px dashed #91DAED; padding:0"></div>

<Line v-click.hide="1" x1="492" y1="349" x2="250" y2="372" color="#91DAED" width="2" />

<Line v-click.hide="1" x1="251" y1="421" x2="493" y2="524" color="#91DAED" width="2" />

<img v-click.hide="1" class="abs" src="/media/s47-google-shape-611-p94.png" style="left:488px; top:346px; width:189px; height:179px">

<img v-click="1" class="abs" src="/media/non_uniform_background_classic_threshold.gif" style="left:503px; top:133px; width:415px; height:364px">

<div v-click="1" class="abs" style="left:503px; top:499px; width:415px; font-size:16px; text-align:center; font-style:italic; color:#888">

Classical threshold

</div>

<div class="abs" style="left:749px; top:517px; width:231px; font-size:16px; text-align:right">

Data from Sofia Romero

</div>

<!--
High pass filter → Keep highest pixel values ("outliers")
-->

---

# Gaussian blur subtractsions extract puncta signal from the background

<img class="abs" src="/media/s47-google-shape-607-p94.png" style="left:17px; top:166px; width:306px; height:269px">

<img class="abs" src="/media/s48-google-shape-619-p95.png" style="left:337px; top:166px; width:306px; height:269px">

<img class="abs" src="/media/s48-google-shape-620-p95.png" style="left:659px; top:166px; width:306px; height:269px">

<div class="abs" style="left:124px; top:450px; width:92px; font-size:18px; text-align:center">

**Input**

</div>

<div class="abs" style="left:385px; top:450px; width:209px; font-size:18px; text-align:center">

**Gaussian blur (σ = 5)**

</div>

<div class="abs" style="left:724px; top:450px; width:175px; font-size:18px; text-align:center">

**blur - input**

</div>

<div class="abs" style="left:749px; top:517px; width:231px; font-size:16px; text-align:right">

Data from Sofia Romero

</div>

<div class="abs" style="left:17px; top:488px; width:513px; font-size:18px">

- Small gaussian filters (σ = \~ 2) suppress noise.
- Larger gaussian filters (σ = \~ &gt;5) suppress large structures.

</div>

<!--
Blur the image where the structures you are trying to keep are not visible-- retains the strucutes you don't want (haze).

Difference of gaussian captures features inside of feature valley, but doesn't always work.

Can remove small noise with small gaussian or large gauissina...
-->

---
class: fiji-slide
---

# Gaussian subtraction in Fiji

<img class="abs" src="/media/s47-google-shape-607-p94.png" style="left:20px; top:115px; width:155px; height:136px">
<div class="abs" style="left:20px; top:82px; width:155px; font-size:14px; font-weight:bold; text-align:center">Input image</div>

<img v-click="1" class="abs" src="/media/s48-google-shape-619-p95.png" style="left:188px; top:345px; width:155px; height:136px">
<div v-click="1" class="abs" style="left:160px; top:486px; width:210px; font-size:14px; font-weight:bold; text-align:center">Gaussian blur<br><code>Filters → Gaussian Blur</code></div>

<img v-click="2" class="abs" src="/media/s48-google-shape-620-p95.png" style="left:355px; top:115px; width:155px; height:136px">
<div v-click="2" class="abs" style="left:330px; top:82px; width:205px; font-size:14px; font-weight:bold; text-align:center">Subtract blur − input<br><code>Image Calculator</code></div>

<img v-click="3" class="abs" src="/media/s49-google-shape-630-p96.png" style="left:523px; top:345px; width:155px; height:136px">
<div v-click="3" class="abs" style="left:495px; top:486px; width:210px; font-size:14px; font-weight:bold; text-align:center">Apply threshold<br><code>Ctrl+Shift+T</code></div>

<img v-click="4" class="abs" src="/media/s50-google-shape-641-p97.png" style="left:690px; top:115px; width:155px; height:136px">
<div v-click="4" class="abs" style="left:685px; top:82px; width:160px; font-size:14px; font-weight:bold; text-align:center">Result overlay</div>

<div class="abs" style="left:835px; top:368px; width:140px; border:1px solid #888; border-radius:6px; overflow:hidden; padding:0; background:#fff">
  <img src="/media/s49-google-shape-629-p96.png" style="width:100%; display:block">
  <div style="font-size:11px; text-align:center; padding:2px 0; line-height:1.2">Original threshold</div>
</div>

<svg class="abs" style="left:0; top:0; width:980px; height:551px; pointer-events:none" viewBox="0 0 980 551" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-gauss" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0,0 8,3 0,6" fill="#333"/>
    </marker>
  </defs>
  <g v-click="1">
    <path d="M 97 256 V 398 Q 97 413 112 413 H 183" stroke="#333" stroke-width="1.5" fill="none" marker-end="url(#arr-gauss)"/>
  </g>
  <g v-click="2">
    <!-- branch from input image right-center -->
    <path d="M 185 183 H 340" stroke="#333" stroke-width="1.5" fill="none"/>
    <!-- branch from Gaussian blur top-center, curves up then right to junction -->
    <path d="M 265 335 V 196 Q 265 183 280 183 H 340" stroke="#333" stroke-width="1.5" fill="none"/>
    <!-- merged arrow into subtraction image -->
    <path d="M 340 183 H 350" stroke="#333" stroke-width="1.5" fill="none" marker-end="url(#arr-gauss)"/>
  </g>
  <g v-click="3">
    <path d="M 432 256 V 398 Q 432 413 447 413 H 518" stroke="#333" stroke-width="1.5" fill="none" marker-end="url(#arr-gauss)"/>
  </g>
  <g v-click="4">
    <path d="M 600 335 V 196 Q 600 183 615 183 H 685" stroke="#333" stroke-width="1.5" fill="none" marker-end="url(#arr-gauss)"/>
  </g>
</svg>

<div class="abs" style="left:749px; top:517px; width:231px; font-size:16px; text-align:right">

Data from Sofia Romero

</div>

---
hide: true
---

# Interested in performing this function? Use the script!

<img class="abs" src="/media/s51-google-shape-662-p99.png" style="left:117px; top:125px; width:745px; height:365px">

<div class="abs" style="left:222px; top:503px; width:535px; height:37px; font-size:24px; text-align:center; background:#FFFFFF; border:1px solid #000000; color:#000000">

<span style="color:#0000FF">**<https://github.com/elevans/fiji-scripts/>**</span>

</div>

---

# Deconvolution "undoes" diffraction blur

<img class="abs" src="/media/s53-google-shape-169-p24.png" style="left:495px; top:124px; width:426px; height:111px">

<div class="abs" style="left:771px; top:248px; width:94px; font-size:18px">

**Output**

</div>

<div class="abs" style="left:566px; top:251px; width:69px; font-size:18px">

**Input**

</div>

<img class="abs" src="/media/s53-google-shape-173-p24.gif" style="left:614px; top:290px; width:205px; height:233px">

<div class="abs" style="left:0px; top:121px; width:473px; font-size:20px; --nest:1.00">

- Out of focus light leads to loss of contrast
  - Deconvolution models the *point spread function* to recover ground truth
- *Why use deconvolution?*
  - Improves clarity
  - Aids in segmentation
- Multiple types of deconvolution exist
  - Weiner
  - Richardson-Lucy

</div>

<LinkButton left="42" top="493" width="354" height="30" href="https://imagej.net/imaging/deconvolution" icon="🔬" label="Deconvolution - ImageJ Wiki" />

<div class="abs" style="left:564px; top:522px; width:301px; font-size:10px; text-align:center">

*Adapted from Scientific Volume Imaging (SVI) and Codicals*

</div>

---

# … using the point spread function

<div class="abs" style="left:0px; top:107px; width:473px; font-size:20px; --nest:1.00">

- **Point Spread Function (PSF)**: Point source of light as imaged through a lens or series of lenses
  - Captures optical diffraction, abberations
- PSFs can be:
  - **Measured** – Obtained by imaging sub-resolution sized beads
    - Averaging can suppress noise
  - **Theoretical (Synthetic)** – Generated by a computer based on parameters
    - Simulated with simple Gaussian kernels or more complex models

</div>

<img class="abs" src="/media/s54-google-shape-187-p26.gif" style="left:512px; top:157px; width:209px; height:209px">

<img class="abs" src="/media/s54-google-shape-188-p26.gif" style="left:582px; top:317px; width:64px; height:209px; transform:rotate(90deg)">

<div class="abs" style="left:532px; top:474px; width:164px; font-size:18px; text-align:center">

**Simulated PSF**

</div>

<img class="abs" src="/media/s54-google-shape-190-p26.gif" style="left:729px; top:376px; width:206px; height:92px">

<img class="abs" src="/media/s54-google-shape-191-p26.gif" style="left:728px; top:156px; width:209px; height:209px">

<div class="abs" style="left:772px; top:470px; width:122px; font-size:18px; text-align:center">

**Real PSF**

</div>

<div class="abs" style="left:461px; top:243px; width:61px; transform:rotate(-90deg); font-size:18px; text-align:center">

**XY**

</div>

<div class="abs" style="left:461px; top:398px; width:61px; transform:rotate(-90deg); font-size:18px; text-align:center">

**XZ**

</div>

---

<!-- TODO: Get a slide showing this in Fiji -->
# Richardson-Lucy Total Variation Deconvolution

<div class="abs" style="left:0px; top:149px; width:377px; font-size:20px">

- Richardson-Lucy Total Variation (TV) → Iterative algorithm for recovering the underling image from a blurred dataset using a PSF
- Original Richardsen-Lucy amplifies noise after a small number of iterations
- Richardson-Lucy TV avoids this noise accumulation leading to better image recovery and object edges

</div>

<img class="abs" src="/media/s55-google-shape-202-p27.png" style="left:426px; top:293px; width:486px; height:203px">

<div class="abs" style="left:448px; top:498px; width:81px; font-size:16px; text-align:center">

**Input**

</div>

<div class="abs" style="left:569px; top:497px; width:81px; font-size:16px; text-align:center">

**Blurred input**

</div>

<div class="abs" style="left:640px; top:498px; width:185px; font-size:16px; text-align:center">

**Richardson-**

**Lucy**

</div>

<div class="abs" style="left:783px; top:497px; width:130px; font-size:16px; text-align:center">

**Richardson-Lucy TV**

</div>

<img class="abs" src="/media/s55-google-shape-208-p27.png" style="left:422px; top:116px; width:490px; height:177px">

<div class="abs" style="left:0px; top:524px; width:436px; font-size:14px">

Adapted from Dey *et al*. Microscopy Research and Technique (2006)

</div>

---
layout: section
---

# Measurement & Feature Analysis
Measuring properties of segmented objects

<div style="width:800px; margin: 40px auto 0">

```mermaid
%%{init: {"theme": "neutral", "themeVariables": {"fontSize": "20px", "edgeLabelBackground": "#faf8f3"}, "flowchart": {"wrappingWidth": 200}}}%%
flowchart LR
  C["Digital<br>image"] --> analysis --> D["Quantitative<br>measurements"]
  subgraph analysis ["Image Analysis"]
    direction LR
    A["Preprocessing"] --> B["Segmentation"] --> M["Measure"]
  end
  classDef endpoint fill:#dde8e0,stroke:#7f9c88
  classDef highlight fill:#e57373,stroke:#d32f2f
  class C,D endpoint
  class M highlight
```

</div>

---

# What questions can be answered, *revisited*?

<div class="abs" style="left:20px; top:120px; width:940px; display:flex; flex-wrap:wrap; gap:15px; justify-content:center; align-items:flex-start">
  <div style="display:flex; flex-direction:column; align-items:center; gap:5px">
    <div style="position:relative">
      <CountGraphic :scale="0.7" />
      <div v-click="1" style="position:absolute; top:-6px; right:-6px;">
        <CountGraphic :scale="0.35" segmented />
      </div>
    </div>
    <span style="font-size:15px; text-align:center">How <b>many</b> X are there?</span>
  </div>
  <div style="display:flex; flex-direction:column; align-items:center; gap:5px">
    <div style="position:relative">
      <ShapeGraphic :scale="0.7" />
      <div v-click="1" style="position:absolute; top:-6px; right:-6px;">
        <ShapeGraphic :scale="0.35" segmented />
      </div>
    </div>
    <span style="font-size:15px; text-align:center">What <b>shape/size</b> is X?</span>
  </div>
  <div style="display:flex; flex-direction:column; align-items:center; gap:5px">
    <div style="position:relative">
      <IntensityGraphic :scale="0.7" />
      <div v-click="1" style="position:absolute; top:-6px; right:-6px;">
        <IntensityGraphic :scale="0.35" segmented />
      </div>
    </div>
    <span style="font-size:15px; text-align:center">How <b>bright</b> is X?</span>
  </div>
  <div style="display:flex; flex-direction:column; align-items:center; gap:5px">
    <div style="position:relative">
      <MotionGraphic :scale="0.7" />
      <div v-click="1" style="position:absolute; top:-6px; right:-6px;">
        <MotionGraphic :scale="0.35" segmented />
      </div>
    </div>
    <span style="font-size:15px; text-align:center">Does X <b>move</b>?</span>
  </div>
  <div style="display:flex; flex-direction:column; align-items:center; gap:5px">
    <div style="position:relative">
      <ColocGraphic :scale="0.7" />
      <div v-click="1" style="position:absolute; top:-6px; right:-6px;">
        <ColocGraphic :scale="0.35" segmented />
      </div>
    </div>
    <span style="font-size:15px; text-align:center">Does X appear <b>near</b> Y?</span>
  </div>
</div>

---
class: fiji-slide
---

# Fiji's `Analyze Particles`

<div class="abs" style="left:760px; top:15px;">
  <div style="position:relative">
    <ShapeGraphic :scale="0.5" />
    <div style="position:absolute; top:-6px; right:-6px;">
      <ShapeGraphic :scale="0.25" segmented />
    </div>
  </div>
</div>

<div class="abs" style="left:41px; top:132px; width:419px; font-size:24px; --nest:1.00">

- `Analyze → Analyze Particles`
  - Requires a **binary 8-bit** image
- `Size`/`Circularity` filter particles
- `Show` tailors particle visualization
- `Clear Results` removes previous measurements
  - Untoggle when analyzing multiple images

</div>

<LinkButton left="530" top="502" width="419" height="32" href="https://imagej.net/imaging/particle-analysis" icon="🔬" label="Particle Analysis - ImageJ Wiki" />

<img class="abs" src="/media/s65-picture-15.png" style="left:565px; top:132px; width:350px; height:345px">

---
class: fiji-slide
---

# Selecting measurements

<div class="abs" style="left:11px; top:134px; width:621px; font-size:24px; --nest:1.00">

`Analyze → Set Measurements…`
  - **Area:** Pixels in the segment
  - **Shape Descriptors:** Circularity, etc.
  - **Mean Gray Value:** Integrated density divided by the number of pixels
  - *many* more options
  - **Redirect to:** The target for statistical calculations
    - If `None`, `Mean` will be `255`!

</div>

<LinkButton left="36" top="502" width="580" height="32" href="https://imagej.net/ij/docs/menus/analyze.html" icon="📖" label="Analyze Menu - ImageJ Docs" />

<img class="abs" src="/media/blobs_set_measurements.png" style="left:675px; top:118px; height:413px">

---
class: fiji-slide
---

# Fiji's `Analyze Particles`

<div class="abs" style="left:760px; top:15px;">
  <div style="position:relative">
    <ShapeGraphic :scale="0.5" />
    <div style="position:absolute; top:-6px; right:-6px;">
      <ShapeGraphic :scale="0.25" segmented />
    </div>
  </div>
</div>

<img class="abs" src="/media/blobs_thresholded.png" style="left:20px; top:208px; width:185px">
<div class="abs" style="left:20px; top:178px; width:185px; font-size:14px; font-weight:bold; text-align:center">Segmented image</div>

<img v-click="1" class="abs" src="/media/blobs_set_measurements.png" style="left:235px; top:208px; width:155px">
<div v-click="1" class="abs" style="left:205px; top:168px; width:215px; font-size:13px; font-weight:bold; text-align:center"><code>Analyze → Set Measurements</code> (if necessary)</div>

<img v-click="2" class="abs" src="/media/blobs_analyze_widget.png" style="left:415px; top:228px; width:125px">
<div v-click="2" class="abs" style="left:395px; top:178px; width:165px; font-size:13px; font-weight:bold; text-align:center"><code>Analyze → Analyze Particles</code></div>

<img v-click="3" class="abs" src="/media/blobs_analyzed.png" style="left:565px; top:208px; width:185px">
<img v-click="3" class="abs" src="/media/blobs_measurements.png" style="left:675px; top:290px; width:240px">
<div v-click="3" class="abs" style="left:652px; top:268px; width:393px; font-size:14px; font-weight:bold; text-align:center">Objects detected and measured</div>


<img v-click="4" class="abs" src="/media/blobs_measurements_save_as.png" style="left:675px; top:290px; width:240px">

<svg class="abs" style="left:0; top:0; width:980px; height:551px; pointer-events:none" viewBox="0 0 980 551" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-meas" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0,0 8,3 0,6" fill="#333"/>
    </marker>
  </defs>
  <g v-click="1">
    <path d="M 205 300 H 232" stroke="#333" stroke-width="1.5" fill="none" marker-end="url(#arr-meas)"/>
  </g>
  <g v-click="2">
    <path d="M 390 300 H 412" stroke="#333" stroke-width="1.5" fill="none" marker-end="url(#arr-meas)"/>
  </g>
  <g v-click="3">
    <path d="M 540 300 H 562" stroke="#333" stroke-width="1.5" fill="none" marker-end="url(#arr-meas)"/>
  </g>
</svg>

<div v-click="4" class="abs" style="left:720px; top:430px; width:150px; font-size:15px; padding:7px 14px; border:1.5px solid rgb(249, 144, 144); border-radius:6px; background:rgb(255, 214, 214); text-align:center">
  Save results as CSV: <strong>File → Save As...</strong>
</div>

---
class: fiji-slide
---

# TrackMate for particle tracking

<div class="abs" style="left:760px; top:15px;">
  <div style="position:relative">
    <MotionGraphic :scale="0.5" />
    <div style="position:absolute; top:-6px; right:-6px;">
      <MotionGraphic :scale="0.25" segmented />
    </div>
  </div>
</div>

<div class="abs" style="left:17px; top:107px; width:561px; font-size:18px; --nest:1.00">

- `Plugins → Tracking → TrackMate`
  - Comes with Fiji!
- Multiple tracking algorithms available
- Step-by-step instructions
- Handles:
  - Segmentation (integrated)
  - Linking tracks/object jumps across frames
  - Cell fates
  - Recognizing splitting and merging objects

</div>

<img class="abs" src="/media/s68-google-shape-282-p37.gif" style="left:67px; top:366px; width:403px; height:174px">

<img class="abs" src="/media/s68-google-shape-280-p37.png" style="left:546px; top:126px; width:401px; height:414px">

---

# Colocalization

<div class="abs" style="left:760px; top:15px;">
  <div style="position:relative">
    <ColocGraphic :scale="0.5" />
    <div style="position:absolute; top:-6px; right:-6px;">
      <ColocGraphic :scale="0.25" segmented />
    </div>
  </div>
</div>

<div class="abs" style="left:33px; top:131px; width:460px; font-size:26px">

- Computational approach to quantify label co-occurrence
- Suggests physical proximity or co-expression
- **Pixel-based:** Pearson's / Manders' correlation coefficients
- **Object-based:** fraction of objects that overlap with a counterpart channel

</div>

---
layout: section
---

# Scripting

---

# Scripting facilitates *replication*

- Experiments contain many datasets
- Experiments are often repeated, iterated on
- Processes must (should) be published for replication
  - The **R** in [**FAIR science**](https://doi.org/10.1038/sdata.2016.18)

<div style="display:grid; grid-template-areas:'overlay'; width:800px; margin:40px auto 0">
<div v-click-hide="1" style="grid-area:overlay">

```mermaid
%%{init: {"theme": "neutral", "themeVariables": {"fontSize": "20px", "edgeLabelBackground": "#faf8f3"}, "flowchart": {"wrappingWidth": 200}}}%%
flowchart LR
  C["Digital<br>image"] --> analysis --> D["Quantitative<br>measurements"]
  subgraph analysis ["Image Analysis"]
    direction LR
    A["Preprocessing"] --> B["Segmentation"] --> M["Measure"]
  end
  classDef endpoint fill:#dde8e0,stroke:#7f9c88
  class C,D endpoint
```

</div>
<div v-click="1" style="grid-area:overlay">

```mermaid
%%{init: {"theme": "neutral", "themeVariables": {"fontSize": "20px", "edgeLabelBackground": "#faf8f3"}, "flowchart": {"wrappingWidth": 200}}}%%
flowchart LR
  C1["Image 1"] --> analysis
  C2["Image 2"] --> analysis
  Cn["⋮"] --> analysis
  analysis --> D1["Results 1"]
  analysis --> D2["Results 2"]
  analysis --> Dn["⋮"]
  subgraph analysis ["Image Analysis"]
    direction LR
    A["Preprocessing"] --> B["Segmentation"] --> M["Measure"]
  end
  classDef endpoint fill:#fde8d0,stroke:#c08060
  class C1,C2,Cn,D1,D2,Dn endpoint
```

</div>
</div>

---
class: fiji-slide
---

# Scripting in Fiji

<div class="abs" style="left:23px; top:115px; width:441px; font-size:22px; --nest:0.85">

`File → New → Script...`

**Supported Languages:**  
- Groovy
- Python
- *ImageJ Macro*,
- ...

</div>

<img class="abs" src="/media/mcw_s46_img0.png" style="left:459px; top:111px; width:494px">

<LinkButton left="14" top="490" width="430" height="36" href="https://imagej.net/scripting/script-editor" icon="📖" label="Script Editor - ImageJ Wiki" />

---
class: fiji-slide
---

# Scripting in Fiji: **Macros**

<div class="abs" style="left:28px; top:77px; width:448px; font-size:22px; --nest:0.85">

- Less powerful
- Older (predates Fiji)
- Easy to learn, *record*, and use

</div>

<img class="abs" src="/media/mcw_s47_img0.png" style="left:514px; top:72px; width:433px">
<img class="abs" src="/media/mcw_s47_img1.png" style="left:33px; top:223px; width:382px">
<img class="abs" src="/media/mcw_s47_img2.png" style="left:318px; top:295px; width:155px">

<LinkButton left="105" top="479" width="333" height="50" href="https://imagej.net/scripting/macro#the-recorder" icon="⏺" label="ImageJ Macro Recorder" />
<LinkButton left="568" top="479" width="359" height="50" href="https://imagej.net/ij/developer/macro/functions.html" icon="📋" label="Built-in Macro Functions" />

---
class: fiji-slide
---

# Writing a macro

<div class="abs" style="left:7px; top:100px; width:450px; font-size:20px">

- Open an image
- `Plugins → Macros → Record...`
- run your workflow
- `Create`
  - Export to **Script Editor**
- `Run`
  - Uses the active image
- `File → Save As...`
  - Saves as a *SciJava Script*

</div>

<img class="abs" src="/media/macro_recording.gif" style="left:350px; top:137px; width:600px">

<LinkButton left="350" top="490" width="600" height="36" href="https://imagej.net/scripting/macro#the-recorder" icon="📖" label="imagej.net/scripting/macro#the-recorder" />

---
class: fiji-slide
hide: true <!-- Shows the same thing as the above slide -->
---

# How to write a macro

<div class="abs" style="left:59px; top:84px; width:420px; font-size:20px; --nest:0.85">

- Open sample images
  - Download/unpack "images/C3-jw-30min.zip"
  - *Plugins → Bio-Formats → Bio-Formats Importer*
  - Open "C3-jw-30min 5_c5.tif"
- Apply Gaussian blur
- Apply a threshold **(Shift+T)**
- Create Mask
- Watershed
- Analyze Particles...
  - Size: 200-Infinity
  - Exclude on edges; Add to Manager

</div>

<img class="abs" src="/media/mcw_s49_img0.png" style="left:506px; top:143px; width:455px">

<LinkButton left="220" top="490" width="575" height="36" href="https://imagej.net/scripting/macro#the-recorder" icon="📖" label="imagej.net/scripting/macro#the-recorder" />

---
class: fiji-slide
hide: true <!-- Shows the same thing as the above slide -->
---

# How to write a macro

<div class="abs" style="left:54px; top:174px; width:430px; font-size:22px; --nest:0.85">

- Click the **"Create"** button
- Use script parameters
- `setBatchMode(true)`
- Use image IDs
- Store in scripts
  - In a folder matching the desired menu
  - Use underscore for spaces

</div>

<img class="abs" src="/media/mcw_s50_img0.png" style="left:500px; top:128px; width:462px">

<LinkButton left="220" top="490" width="575" height="36" href="https://imagej.net/scripting/macro#the-recorder" icon="📖" label="imagej.net/scripting/macro#the-recorder" />

---
hide: true
---

# Let's write a script together: Finding the center of mass

<div class="abs" style="left:30px; top:109px; width:418px; font-size:18px; --nest:0.85">

**Key points:**
- Language: Python (Jython)
- Don't stress, only 25 lines of code.
- Fiji makes interactive image processing scripts easy.
  - *i.e. script parameters.*
- Knowing / familiarity with the ImageJ/Fiji is crucial to writing powerful Fiji scripts.
- **Its Okay to use AI/LLMs for help! Just check it!**

</div>

<img class="abs" src="/media/mcw_s51_img0.png" style="left:461px; top:128px; width:490px">

---

# Other applications handle replication differently

<img class="abs" src="/media/mcw_s45_img0.png" style="left:50px; top:76px; width:378px">
<img class="abs" src="/media/mcw_s45_img3.png" style="left:70px; top:455px; width:322px">
<img class="abs" src="/media/mcw_s45_img1.png" style="left:544px; top:120px; width:349px">
<img class="abs" src="/media/mcw_s45_img4.png" style="left:637px; top:461px; width:216px">

---
layout: section
hide: true <!-- Uncomment when there is a lab exercise -->
---

# Part 2: Lab Exercise

<div class="abs" style="left:245px; top:323px; width:490px; height:42px; font-size:29px; text-align:center; background:#FFFFFF; border:2px solid #61CBF4">

<https://tinyurl.com/AQLM2026ImageJ>

</div>
