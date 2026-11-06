
# About Me!

<div class="abs" style="left:45px; top:120px; width:454px; font-size:24px">

- Eliceiri Lab since 2017
- Based in Chicago, IL
- Core developer for Fiji and Micro-Manager

</div>

<img class="abs" src="/media/headshot.jpg" style="left:610px; top:145px; width:291px; height:366px; object-fit:cover">

<img class="abs" src="/media/loci.png" style="left:769px; top:11px; width:171px; height:85px">

<img class="abs" src="https://fiji.sc/site/logo.png" style="left:90px; top:300px; width:130px; height:130px">

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
<img v-click="6" class="abs" src="https://fiji.sc/site/logo.png" style="left:38px; top:350px; width:120px; height:120px; object-fit:contain">
<img v-click="6" class="abs" src="https://imagej.net/media/icons/imagej.png" style="left:234px; top:350px; width:120px; height:120px; object-fit:contain">
<div v-click="6" class="abs" style="left:38px; top:478px; width:120px; font-size:18px; text-align:center">

**Fiji**

</div>
<div v-click="6" class="abs" style="left:234px; top:478px; width:120px; font-size:18px; text-align:center">

**ImageJ**

</div>

<!-- Alternatives — revealed on click 7 -->
<img v-click="7" class="abs" src="https://avatars.githubusercontent.com/u/21292410?s=200&v=4" style="left:430px; top:350px; width:120px; height:120px; object-fit:contain">
<div v-click="7" class="abs" style="left:430px; top:478px; width:120px; font-size:18px; text-align:center">

**QuPath**

</div>
<img v-click="7" class="abs" src="https://medschool.vanderbilt.edu/cisr/wp-content/uploads/sites/100/2026/10/751d8d54b4aff0f37c0be5543828cab9-675x480-c-default.png" style="left:626px; top:350px; width:120px; height:120px; object-fit:contain">
<div v-click="7" class="abs" style="left:626px; top:478px; width:120px; font-size:18px; text-align:center">

**Imaris**

</div>
<img v-click="7" class="abs" src="https://cellprofiler.org/files/files/cellprofiler/files/2017_11_21-cp_logo_black_tm_4.png" style="left:822px; top:350px; width:120px; height:120px; object-fit:contain">
<div v-click="7" class="abs" style="left:822px; top:478px; width:120px; font-size:18px; text-align:center">

**Cellprofiler**

</div>

