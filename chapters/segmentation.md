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

