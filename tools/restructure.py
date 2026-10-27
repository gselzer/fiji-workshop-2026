#!/usr/bin/env python3
"""Restructure slides.md into the new agreed slide order."""

import re
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(BASE, 'slides.md')


def is_yaml_fm(text):
    """True if the segment's first non-empty line looks like a YAML key."""
    stripped = text.strip()
    if not stripped:
        return False
    first = stripped.splitlines()[0].strip()
    return bool(re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*\s*:', first))


def parse(content):
    """Return a list of logical slides.
    Each slide is a list of raw string segments:
      [content]        for a plain slide
      [fm, content]    for a frontmatter slide
    """
    lines = content.split('\n')
    sep_pos = [i for i, l in enumerate(lines) if l.rstrip() == '---']

    segs = []
    prev = 0
    for pos in sep_pos:
        segs.append('\n'.join(lines[prev:pos]))
        prev = pos + 1
    segs.append('\n'.join(lines[prev:]))

    # segs[0] = empty string before the very first ---
    slides = []
    i = 1
    while i < len(segs):
        if is_yaml_fm(segs[i]) and i + 1 < len(segs):
            slides.append([segs[i], segs[i + 1]])
            i += 2
        else:
            slides.append([segs[i]])
            i += 1
    return slides


def render(ordered_slides):
    """Reconstruct file content from an ordered list of logical slides."""
    all_segs = []
    for s in ordered_slides:
        all_segs.extend(s)
    return '---\n' + '\n---\n'.join(all_segs)


# ── New slides ──────────────────────────────────────────────────────────────

def section(title, subtitle=''):
    sub = f'\n{subtitle}' if subtitle else ''
    return ['layout: section\n', f'\n# {title}{sub}\n\n']


def plain(body):
    return [f'\n{body}\n']


S_PREPROCESSING = section('Preprocessing')
S_TRACKING      = section('Tracking')
S_FEATURE       = section('Intensity & Feature Analysis',
                           'Measuring properties of segmented objects')
S_COLOC         = section('Colocalization', 'Do two signals appear together?')

S_FEATURE_THEORY = plain(
    '# What can we measure?\n\n'
    '<div class="abs" style="left:33px; top:131px; width:900px; font-size:26px">\n\n'
    '- **Area / Volume** — how big is the object?\n'
    '- **Intensity** (mean, median, integrated density) — how bright?\n'
    '- **Shape descriptors** — circularity, aspect ratio, solidity\n'
    '- **Position** — centroid, nearest-neighbour distance\n\n'
    '</div>\n\n'
    '<div class="abs" style="left:33px; top:420px; width:900px; font-size:20px">\n\n'
    'Measured via **Analyze → Set Measurements** then '
    '**Analyze → Measure** or **Analyze → Analyze Particles**\n\n'
    '</div>'
)

S_COLOC_THEORY = plain(
    '# Colocalization\n\n'
    '<div class="abs" style="left:33px; top:131px; width:460px; font-size:26px">\n\n'
    '- Two fluorescent labels appear in the same region\n'
    '- Suggests physical proximity or co-expression\n'
    '- **Pixel-based:** Pearson\'s / Manders\' correlation coefficients\n'
    '- **Object-based:** fraction of objects that overlap with a counterpart channel\n\n'
    '</div>'
)

NEW = {
    'S_PREPROCESSING':  S_PREPROCESSING,
    'S_TRACKING':       S_TRACKING,
    'S_FEATURE':        S_FEATURE,
    'S_FEATURE_THEORY': S_FEATURE_THEORY,
    'S_COLOC':          S_COLOC,
    'S_COLOC_THEORY':   S_COLOC_THEORY,
}

# ── New order ────────────────────────────────────────────────────────────────
# Drops original [39] Background Subtraction FM and [73] Setting Measurements FM.
# Inserts 6 new slides.

ORDER = [
    0,                                             # FM Title (global FM + title)
    1, 2,                                          # About Me, Outline
    3, 4,                                          # FM Overview, Pipeline
    15, 16,                                        # FM Image Analysis Pipelines + tools
    17, 18, 19, 20, 21, 22, 23, 24, 25,            # FM Fiji Overview + 8 Fiji slides
    5, 6, 7, 8, 9, 10, 11, 12,                     # FM Digital Images + slides + Metadata + Quality
    26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37,  # FM Visualizing + 11 slides
    13, 14,                                        # FM Quantitative Measurements + questions
    'S_PREPROCESSING',
    39, 40, 41,                                    # BG subtraction intro (drop FM [38])
    42, 43, 44, 45, 46, 47,                        # FM Method 1 + slides
    48, 49, 50, 51, 52, 53,                        # FM Method 2 + slides
    58, 59, 60,                                    # FM Stitching + slides
    54, 55, 56, 57,                                # FM Deconvolution + slides
    61, 62, 63, 66, 64, 65, 71, 67, 68, 69,       # FM Segmentation (reordered, +AI [71])
    'S_TRACKING',
    70,                                            # TrackMate
    'S_FEATURE',
    'S_FEATURE_THEORY',
    73, 74, 75, 76, 77,                            # Set Measurements slides (drop FM [72])
    'S_COLOC',
    'S_COLOC_THEORY',
    78, 79, 80, 81, 82, 83,                        # FM Scripting + slides
    84,                                            # FM Part 2: Lab Exercise
]

# ── Run ──────────────────────────────────────────────────────────────────────

with open(PATH, 'r', encoding='utf-8') as f:
    content = f.read()

slides = parse(content)

log_path = os.path.join(BASE, 'tools', 'restructure_log.txt')
with open(log_path, 'w', encoding='utf-8') as log:
    log.write(f'Parsed {len(slides)} logical slides:\n')
    for i, s in enumerate(slides):
        body = s[1] if len(s) == 2 else s[0]
        preview = body.strip()[:65].replace('\n', ' ')
        log.write(f'  [{i:02d}] {"FM" if len(s) == 2 else "  "}: {preview}\n')
print(f'Parsed {len(slides)} logical slides  (see tools/restructure_log.txt)')

if len(slides) != 85:
    print(f'\nERROR: expected 86 slides, got {len(slides)}. Aborting.')
    raise SystemExit(1)

ordered = []
for item in ORDER:
    ordered.append(NEW[item] if isinstance(item, str) else slides[item])

result = render(ordered)

with open(PATH, 'w', encoding='utf-8', newline='\n') as f:
    f.write(result)

print(f'\nWrote {len(ordered)} logical slides to {PATH}')
