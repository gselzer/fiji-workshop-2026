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

