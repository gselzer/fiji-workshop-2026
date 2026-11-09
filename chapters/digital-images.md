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

<img class="abs" src="/media/confocal-sampling-image.png" style="left:23px; top:150px; width:580px; height:339px">

<img class="abs" src="/media/confocal-sampling-detail.png" style="left:640px; top:150px; width:317px; height:339px">

<BlockArrow dir="down" x="160" y="355" w="40" h="64" color="#FF0000" rotate="39.1212" />

<BlockArrow dir="down" x="815" y="218" w="40" h="64" color="#FF0000" rotate="39.1212" />

---

# These samples can be stored in different ways

<img class="abs" src="/media/bit-depth-grayscale-gradient.png" style="left:25px; top:145px; width:542px; height:131px">

<img class="abs" src="/media/bit-depth-discrete-levels.png" style="left:25px; top:287px; width:542px; height:83px">

<img class="abs" src="/media/bit-depth-chart.png" style="left:580px; top:193px; width:374px; height:165px">

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

<img class="abs" src="/media/bit-depth-photo-comparison.jpg" style="left:38px; top:121px; width:584px; height:388px">

<div class="abs" style="left:-17px; top:522px; width:695px; font-size:14px; text-align:center">

*Adapted from:* <https://gregbenzphotography.com/photography-tips/8-vs-16-bit-depth-photoshop/>

</div>

<div class="abs" style="left:661px; top:147px; width:281px; font-size:24px">

- Tradeoff: Disk space vs. resolution
- Screen resolution tops out around 8-10 bits

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
<img src="/media/fiji-image-properties.png" style="width:100%; max-height:340px; object-fit:contain">
</div>

<!-- Graphic 4: OME logo below text on click 3 -->
<div v-click="4" class="abs" style="left:32px; top:355px; width:280px">
<img src="/media/ome-logo.png" style="width:100%; object-fit:contain">
</div>


---

# Quality In → Quality Out

<img class="abs" src="/media/mouse-cortex-confocal.png" style="left:521px; top:125px; width:402px; height:422px">

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
- `File → Open…`
- Bio-Formats supports **many** proprietary file formats
  - `.nd2` for Nikon
  - `.czi` for Zeiss
  - `.sld` for 3i
  - ...

</div>

<!-- TODO Consider replacing with a GIF, maybe opening https://zenodo.org/records/5277605-->
<!-- TODO Highlight Virtual Stacks -->
<img class="abs" src="/media/bioformats-import-dialog.png" style="left:335px; top:132px; width:625px; height:383px">

---
class: fiji-slide
---

# Visualizing your data

<img class="abs" src="/media/fiji-2d-viewer.png" style="left:341px; top:215px; width:213px; height:244px">

<img class="abs" src="/media/fiji-hyperstack-viewer.png" style="left:805px; top:211px; width:143px; height:240px">

<img class="abs" src="/media/fiji-3d-stack-viewer.png" style="left:573px; top:215px; width:201px; height:244px">

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

<img class="abs" src="/media/fiji-zstack.png" style="left:11px; top:181px; width:293px; height:354px">

<img class="abs" src="/media/fiji-orthogonal-yz.png" style="left:518px; top:170px; width:97px; height:221px">

<img class="abs" src="/media/fiji-orthogonal-xz.png" style="left:325px; top:408px; width:193px; height:128px">

<img class="abs" src="/media/fiji-orthogonal-xy.png" style="left:325px; top:170px; width:193px; height:237px">

<img class="abs" src="/media/fiji-3d-viewer.png" style="left:646px; top:181px; width:323px; height:343px">

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

<img class="abs" src="/media/lut-grayscale-comparison.png" style="left:29px; top:126px; width:495px; height:190px">

<img class="abs" src="/media/lut-color-examples.png" style="left:37px; top:323px; width:296px; height:213px">

<img class="abs" src="/media/lut-hilo-example.png" style="left:348px; top:323px; width:181px; height:206px">

---
class: fiji-slide
---

# Add a scale bar for publication images

<div class="abs" style="left:74px; top:123px; width:506px; font-size:24px">

`Analyze → Tools → Scale Bar`

</div>

<img class="abs" src="/media/fiji-scale-bar-dialog.png" style="left:639px; top:126px; width:286px; height:404px">

<img class="abs" src="/media/mouse-hippocampus-scale-bar.png" style="left:74px; top:234px; width:475px; height:296px">

<div class="abs" style="left:77px; top:239px; width:234px; font-size:18px">

<span style="color:#FFFFFF">*Mouse, hippocampus, 10x, Nikon A1R confocal*</span>

</div>

<div class="abs" style="left:74px; top:500px; width:234px; font-size:18px">

<span style="color:#FFFFFF">*Noelle Cataldo*</span>

</div>

<!--
Come much earlier
-->

