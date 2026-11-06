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

<img class="abs" src="/media/script_editor.png" style="left:459px; top:111px; width:494px">

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

<img class="abs" src="/media/macro_docs.png" style="left:514px; top:72px; width:433px">
<img class="abs" src="/media/macro_recorder.png" style="left:33px; top:223px; width:382px">
<img class="abs" src="/media/blobs_analyzed.png" style="left:318px; top:295px; width:155px">

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

# Other applications handle replication differently

<img class="abs" src="/media/cell_profiler_collage.png" style="left:50px; top:76px; width:378px">
<img class="abs" src="/media/cell_profiler_logo.png" style="left:70px; top:455px; width:322px">
<img class="abs" src="/media/knime_screenshot.png" style="left:544px; top:120px; width:349px">
<img class="abs" src="/media/knime_logo.png" style="left:637px; top:461px; width:216px">

