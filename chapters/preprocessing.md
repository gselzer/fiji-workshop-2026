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

<img class="abs" src="/media/fiji-stitching-dialog.png" style="left:637px; top:118px; width:233px; height:426px">

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

<img class="abs" src="/media/stitching-tile-1.png" style="left:582px; top:148px; width:72px; height:91px">

<img class="abs" src="/media/stitching-tile-2.png" style="left:706px; top:145px; width:70px; height:92px">

<img class="abs" src="/media/stitching-tile-3.png" style="left:820px; top:148px; width:71px; height:91px">

<img class="abs" src="/media/stitching-tile-4.png" style="left:582px; top:277px; width:76px; height:92px">

<img class="abs" src="/media/stitching-tile-5.png" style="left:710px; top:277px; width:67px; height:90px">

<img class="abs" src="/media/stitching-tile-6.png" style="left:825px; top:277px; width:65px; height:92px">

<img class="abs" src="/media/stitching-tile-7.png" style="left:582px; top:409px; width:70px; height:91px">

<img class="abs" src="/media/stitching-tile-8.png" style="left:710px; top:409px; width:67px; height:91px">

<img class="abs" src="/media/stitching-tile-9.png" style="left:824px; top:409px; width:72px; height:90px">

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

<img class="abs" src="/media/fiji-bc-before.png" style="left:473px; top:133px; width:217px; height:372px">

<img class="abs" src="/media/fiji-bc-after.png" style="left:728px; top:135px; width:217px; height:368px">

<img class="abs" src="/media/fiji-bc-dialog.png" style="left:658px; top:223px; width:104px; height:209px">

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

<img class="abs" src="/media/clahe-before.png" style="left:525px; top:199px; width:211px; height:338px">

<img class="abs" src="/media/clahe-after.png" style="left:761px; top:199px; width:211px; height:338px">

<img class="abs" src="/media/fiji-clahe-dialog.png" style="left:652px; top:150px; width:192px; height:174px">

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

<img class="abs" src="/media/nuclei-bg-subtraction-demo.gif" style="left:178px; top:119px; width:623px; height:415px">

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

<img class="abs" src="/media/fiji-image-calculator.png" style="left:117px; top:200px; width:280px; height:251px">

<div class="abs" style="left:130px; top:375px; width:250px; height:26px; border:2px solid #FF0000; padding:0"></div>

<div class="abs" style="left:150px; top:480px; width:305px; font-size:15px; font-weight:bold; color:#CC0000">Don't overwrite your data!</div>
<Line x1="220" y1="480" x2="220" y2="410" color="#CC0000" width="2" arrow="end" />

---
<!-- TODO: Ask Ed about this slide-->
hide: true
---

# Surface plots are a good way to visualize this change in pixel value: *Before*

<img class="abs" src="/media/nuclei1-surface-plot-before.png" style="left:331px; top:151px; width:292px; height:249px">

<img class="abs" src="/media/nuclei2-surface-plot-before.png" style="left:643px; top:150px; width:292px; height:249px">

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

<img class="abs" src="/media/nuclei1-crop-before.png" style="left:423px; top:409px; width:135px; height:135px">

<img class="abs" src="/media/nuclei2-crop-before.png" style="left:732px; top:409px; width:135px; height:135px">

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

<img class="abs" src="/media/nuclei1-surface-plot-after.png" style="left:180px; top:169px; width:292px; height:248px">

<img class="abs" src="/media/nuclei2-surface-plot-after.png" style="left:650px; top:168px; width:300px; height:255px">

<div class="abs" style="left:253px; top:458px; width:475px; font-size:18px">

- Decreased background shown by bottom of slope (left)
- Greater range of values

</div>

<img class="abs" src="/media/nuclei1-crop-after.png" style="left:16px; top:228px; width:150px; height:150px">

<img class="abs" src="/media/nuclei2-crop-after.png" style="left:484px; top:228px; width:154px; height:154px">

---

# What if the background is non-uniform?

<img class="abs" src="/media/confocal-nonuniform-bg.png" style="left:29px; top:133px; width:449px; height:394px">

<div v-click.hide="1" class="abs" style="left:503px; top:141px; width:449px; font-size:24px">

- 100x confocal microscopy.
- 3D data (X, Y, Channel).
- Must deal with large hazy structures (*i.e.* nuclear shadow).
- Must preserve puncta.

</div>

<div v-click.hide="1" class="abs" style="left:195px; top:369px; width:56px; height:52px; border:2px dashed #91DAED; padding:0"></div>

<Line v-click.hide="1" x1="492" y1="349" x2="250" y2="372" color="#91DAED" width="2" />

<Line v-click.hide="1" x1="251" y1="421" x2="493" y2="524" color="#91DAED" width="2" />

<img v-click.hide="1" class="abs" src="/media/confocal-nonuniform-bg-puncta.png" style="left:488px; top:346px; width:189px; height:179px">

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

<img class="abs" src="/media/confocal-nonuniform-bg.png" style="left:17px; top:166px; width:306px; height:269px">

<img class="abs" src="/media/gaussian-blur-result.png" style="left:337px; top:166px; width:306px; height:269px">

<img class="abs" src="/media/gaussian-subtraction-result.png" style="left:659px; top:166px; width:306px; height:269px">

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

<img class="abs" src="/media/confocal-nonuniform-bg.png" style="left:20px; top:115px; width:155px; height:136px">
<div class="abs" style="left:20px; top:82px; width:155px; font-size:14px; font-weight:bold; text-align:center">Input image</div>

<img v-click="1" class="abs" src="/media/gaussian-blur-result.png" style="left:188px; top:345px; width:155px; height:136px">
<div v-click="1" class="abs" style="left:160px; top:486px; width:210px; font-size:14px; font-weight:bold; text-align:center">Gaussian blur<br><code>Filters → Gaussian Blur</code></div>

<img v-click="2" class="abs" src="/media/gaussian-subtraction-result.png" style="left:355px; top:115px; width:155px; height:136px">
<div v-click="2" class="abs" style="left:330px; top:82px; width:205px; font-size:14px; font-weight:bold; text-align:center">Subtract blur − input<br><code>Image Calculator</code></div>

<img v-click="3" class="abs" src="/media/gaussian-subtraction-threshold.png" style="left:523px; top:345px; width:155px; height:136px">
<div v-click="3" class="abs" style="left:495px; top:486px; width:210px; font-size:14px; font-weight:bold; text-align:center">Apply threshold<br><code>Ctrl+Shift+T</code></div>

<img v-click="4" class="abs" src="/media/gaussian-subtraction-overlay.png" style="left:690px; top:115px; width:155px; height:136px">
<div v-click="4" class="abs" style="left:685px; top:82px; width:160px; font-size:14px; font-weight:bold; text-align:center">Result overlay</div>

<div class="abs" style="left:835px; top:368px; width:140px; border:1px solid #888; border-radius:6px; overflow:hidden; padding:0; background:#fff">
  <img src="/media/gaussian-subtraction-orig-threshold.png" style="width:100%; display:block">
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

<img class="abs" src="/media/gaussian-subtraction-script.png" style="left:117px; top:125px; width:745px; height:365px">

<div class="abs" style="left:222px; top:503px; width:535px; height:37px; font-size:24px; text-align:center; background:#FFFFFF; border:1px solid #000000; color:#000000">

<span style="color:#0000FF">**<https://github.com/elevans/fiji-scripts/>**</span>

</div>

---

# Deconvolution "undoes" diffraction blur

<img class="abs" src="/media/deconvolution-comparison.png" style="left:495px; top:124px; width:426px; height:111px">

<div class="abs" style="left:771px; top:248px; width:94px; font-size:18px">

**Output**

</div>

<div class="abs" style="left:566px; top:251px; width:69px; font-size:18px">

**Input**

</div>

<img class="abs" src="/media/deconvolution-animation.gif" style="left:614px; top:290px; width:205px; height:233px">

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

<img class="abs" src="/media/psf-simulated-xy.gif" style="left:512px; top:157px; width:209px; height:209px">

<img class="abs" src="/media/psf-simulated-xz.gif" style="left:582px; top:317px; width:64px; height:209px; transform:rotate(90deg)">

<div class="abs" style="left:532px; top:474px; width:164px; font-size:18px; text-align:center">

**Simulated PSF**

</div>

<img class="abs" src="/media/psf-real-xz.gif" style="left:729px; top:376px; width:206px; height:92px">

<img class="abs" src="/media/psf-real-xy.gif" style="left:728px; top:156px; width:209px; height:209px">

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

<img class="abs" src="/media/rl-deconvolution-comparison.png" style="left:426px; top:293px; width:486px; height:203px">

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

<img class="abs" src="/media/rl-deconvolution-cells.png" style="left:422px; top:116px; width:490px; height:177px">

<div class="abs" style="left:0px; top:524px; width:436px; font-size:14px">

Adapted from Dey *et al*. Microscopy Research and Technique (2006)

</div>

