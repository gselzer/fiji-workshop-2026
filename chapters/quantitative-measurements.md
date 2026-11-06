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

