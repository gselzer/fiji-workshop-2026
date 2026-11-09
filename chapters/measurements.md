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

<img class="abs" src="/media/fiji-analyze-particles-dialog.png" style="left:565px; top:132px; width:350px; height:345px">

---
class: fiji-slide
---

# Selecting measurements

<div class="abs" style="left:760px; top:15px;">
  <div style="position:relative">
    <ShapeGraphic :scale="0.5" />
    <div style="position:absolute; top:-6px; right:-6px;">
      <ShapeGraphic :scale="0.25" segmented />
    </div>
  </div>
</div>

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

<img class="abs" src="/media/trackmate-animation.gif" style="left:67px; top:366px; width:403px; height:174px">

<img class="abs" src="/media/trackmate-interface.png" style="left:546px; top:126px; width:401px; height:414px">

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
- *Quite the rabbit hole...*

</div>

<img class="abs" src="/media/colocalization_wang_et_al.png" style="left:600px; top:130px; width:225px">
<div class="abs" style="left:600px; top:520px; width:250px; font-size:14px">Adapted from Wang. et al (2019)</div>

---
class: fiji-slide
---

# Colocalization in Fiji: `Coloc2`

<div class="abs" style="left:760px; top:15px;">
  <div style="position:relative">
    <ColocGraphic :scale="0.5" />
    <div style="position:absolute; top:-6px; right:-6px;">
      <ColocGraphic :scale="0.25" segmented />
    </div>
  </div>
</div>

<div class="abs" style="left:33px; top:131px; width:460px; font-size:26px">

- `Analyze → Colocalization → Coloc 2`
  - Comes with Fiji!
- Allows a ROI or a binary pixel mask
- Supports Li, Manders', Kendall's, Spearman's Colocalization Coefficients

</div>

<LinkButton left="50" top="502" width="419" height="32" href="https://imagej.net/plugins/coloc-2" icon="🔬" label="Coloc 2 - ImageJ Wiki" />

<img class="abs" src="/media/coloc2_dialog.png" style="left:600px; top:130px; width:212px">


