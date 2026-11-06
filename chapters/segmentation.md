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

<img class="abs" src="/media/blobs.png" style="left:20px; top:285px; width:157px">
<div class="abs" style="left:20px; top:253px; width:157px; font-size:14px; font-weight:bold; text-align:center">Input image</div>

<img v-click="1" class="abs" src="/media/blobs_thresholding.png" style="left:275px; top:285px; width:157px">
<img v-click="1" class="abs" src="/media/blobs_thresholding_widget.png" style="left:452px; top:305px; width:166px">
<div v-click="1" class="abs" style="left:245px; top:253px; width:420px; font-size:14px; font-weight:bold; text-align:center"><code>Ctrl+Shift+T</code> to threshold</div>

<div v-click="2" class="abs" style="left:645px; top:95px; width:320px; font-size:15px; padding:5px 10px; background:rgba(255,152,0,0.12); border-left:4px solid rgba(255,152,0,0.9)">

**Threshold Strategy** — Otsu is a nice option!

</div>
<div v-click="3" class="abs" style="left:645px; top:130px; width:320px; font-size:15px; padding:5px 10px; background:rgba(76,175,80,0.12); border-left:4px solid rgba(76,175,80,0.9)">

**Dark background** — Select if your objects are bright

</div>
<div v-click="4" class="abs" style="left:645px; top:181px; width:320px; font-size:15px; padding:5px 10px; background:rgba(156,39,176,0.12); border-left:4px solid rgba(156,39,176,0.9)">

**Stack histogram** — Select for a timelapse / z-stack

</div>

<img v-click="5" class="abs" src="/media/blobs_thresholded.png" style="left:755px; top:285px; width:157px">
<div v-click="5" class="abs" style="left:733px; top:253px; width:215px; font-size:14px; font-weight:bold; text-align:center">Click <code>Apply</code> to threshold</div>

<svg class="abs" style="left:0; top:0; width:980px; height:551px; pointer-events:none" viewBox="0 0 980 551" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr8" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0,0 8,3 0,6" fill="#333"/>
    </marker>
  </defs>
  <g v-click="1">
    <path d="M 185 364 H 260" stroke="#333" stroke-width="1.5" fill="none" marker-end="url(#arr8)"/>
  </g>
  <g v-click="2">
    <!-- Threshold strategy highlight -->
    <rect x="472" y="409" width="69" height="14" fill="rgba(255,152,0,0.1)" stroke="rgba(255,152,0,0.9)" stroke-width="1.5" rx="2"/>
  </g>
  <g v-click="3">
    <!-- Dark background highlight -->
    <rect x="466" y="426" width="69" height="14" fill="rgba(76,175,80,0.1)" stroke="rgba(76,175,80,0.9)" stroke-width="1.5" rx="2"/>
  </g>
  <g v-click="4">
    <!-- Stack histogram highlight -->
    <rect x="535" y="426" width="71" height="14" fill="rgba(156,39,176,0.1)" stroke="rgba(156,39,176,0.9)" stroke-width="1.5" rx="2"/>
  </g>
  <g v-click="5">
    <path d="M 628 414 Q 665 414 750 364" stroke="#333" stroke-width="1.5" fill="none" marker-end="url(#arr8)"/>
  </g>
</svg>

---
class: fiji-slide
---

# Labkit: a GUI approach to segmentation

<div class="abs" style="left:0px; top:113px; width:707px; font-size:20px; --nest:1.00">

- `Plugins → Labkit → Open Current Image With Labkit`
- Manually draw on image to indicate foreground and background
- Export to Fiji or save to TIFF/HDF5 when done

</div>

<img class="abs" src="/media/labkit-interface.png" style="left:12px; top:208px; width:464px; height:317px">

<img class="abs" src="/media/labkit-foreground.png" style="left:485px; top:185px; width:214px; height:174px">

<img class="abs" src="/media/labkit-result.png" style="left:626px; top:246px; width:221px; height:177px">

<img class="abs" src="/media/labkit-export.png" style="left:778px; top:330px; width:182px; height:181px">

<BlockArrow dir="right" x="593" y="232" w="69" h="58" color="#96DCF8" rotate="45.224" />

<BlockArrow dir="right" x="750" y="316" w="69" h="58" color="#96DCF8" rotate="45.224" />

---
class: fiji-slide
---

# StarDist: Segmentation via Deep Learning

<img class="abs" src="/media/stardist-result.png" style="left:661px; top:121px; width:141px; height:140px">

- Segments cells using deep learning which can be done with pretrained models
- Broad platform support via `cellcast`
  - `File → New → Script...`
  - `Templates → Appose → Stardist cellcast (Python (Appose))`
  - `Run` button runs on the active image

<img class="abs" src="/media/stardist-cellcast-script.png" style="left:525px; top:284px; width:419px; height:242px">

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

