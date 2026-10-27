# AQLM 2027: Image Analysis with Fiji/ImageJ

Slidev version of the AQLM 2026 lecture (`AQLM_2026_NC.pptx`).

## Running it

You need [Node.js](https://nodejs.org) (already installed here). From this folder:

```sh
npm install        # first time only (or after deleting node_modules)
npm run dev        # starts the deck and opens it at http://localhost:3030
```

Leave `npm run dev` running while you edit: every time you save `slides.md` the
browser updates immediately. Press `Ctrl+C` in the terminal to stop it.

In VS Code you can instead press `Ctrl+Shift+B`, which runs the **Slidev: run
deck** task. Stop it with the trash-can icon on its terminal panel. **Slidev:
export PDF** is under *Terminal → Run Task…*.

### While presenting

| Key / URL | What it does |
|---|---|
| `→` / `Space`, `←` | next / previous slide |
| `f` | fullscreen |
| `o` | overview of all slides (click one to jump) |
| `g` | go to slide number |
| `d` | toggle dark mode (you probably don't want this) |
| http://localhost:3030/presenter | presenter view: current + next slide, speaker notes, timer |
| http://localhost:3030/overview | all slides with their notes on one page |

The presenter view is the PowerPoint "Presenter View" equivalent: open it on your
laptop screen and the plain URL on the projector; they stay in sync.

### Exporting

```sh
npm run export     # writes slides-export.pdf (no internet needed at the lecture)
npm run build      # writes a static website to dist/ that runs without Node
```

`npm run export` needs a headless browser; if it complains, run
`npx playwright install chromium` once. Note that the PDF loses the video and
the animated GIFs.

## Editing

Everything lives in **`slides.md`**. Each slide starts with a line containing
only `---`. A slide looks like this:

```md
---

# Slide title

<div class="abs" style="left:642px; top:353px; width:266px; font-size:18px">

- Bullet one
- Bullet two
  - Indented bullet

</div>

<img class="abs" src="/media/s05-picture-2.png" style="left:145px; top:53px; width:690px; height:483px">

<!--
Speaker notes go in the last HTML comment on the slide.
-->
```

- **Text** is normal Markdown: `**bold**`, `*italic*`, `- bullets`,
  `[link text](https://...)`. A blank line is needed after `<div ...>` and before
  `</div>` for the Markdown inside to work.
- **Position** of each element is in pixels on a 980 × 551 canvas (`left`, `top`,
  `width`, `height`). These numbers were copied from the PowerPoint layout so
  slides look like the original; change them freely, or delete the `<div>`
  wrapper and just write plain Markdown under the title for a simple
  top-to-bottom slide.
- **Images** are in `public/media/` and are referenced as `/media/<name>`. Add
  your own images there.
- **Section divider slides** use `layout: section` in the slide's header block
  (between two `---` lines), which centers the content. Add a line like
  `background: /media/s01-background.jpg` there to put an image behind it.
- **Hidden slides**: `hide: true` in the slide's header block. The slides
  hidden in the original PowerPoint are still hidden (search for `hide: true`).
  Delete that line to show one.
- **Arrows and lines**: `<BlockArrow>` (the thick red PowerPoint arrows) and
  `<Line>` (thin lines and arrows) — see `components/` for their options.

### Changing the look

All the deck-wide styling is in **`style.css`** (title band color and size,
fonts, bullet spacing). The section-divider layout is `layouts/section.vue`.
Slidev also has ready-made themes (https://sli.dev/resources/theme-gallery);
switch with the `theme:` line at the top of `slides.md`, though the
pixel-positioned slides may need touching up after a big theme change.

Slidev docs: https://sli.dev/guide/

## Files

| Path | What |
|---|---|
| `slides.md` | the deck |
| `style.css` | global styles |
| `layouts/section.vue` | section-divider layout |
| `components/` | `BlockArrow` and `Line` |
| `public/media/` | images and the screen-recording video |
| `tools/pptx_to_slidev.py` | the script that converted the PowerPoint (only needed to convert another deck; needs `pip install python-pptx pillow`) |
| `AQLM_2026_NC.pptx` | the original |
