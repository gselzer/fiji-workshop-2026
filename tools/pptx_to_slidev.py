"""Convert a .pptx into a Slidev slides.md with absolutely positioned elements.

usage: python convert.py deck.pptx out_dir
"""

import colorsys
import hashlib
import io
import re
import sys
from collections import Counter
from pathlib import Path

from PIL import Image
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE, PP_PLACEHOLDER

sys.stdout.reconfigure(encoding="utf-8")

NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "asvg": "http://schemas.microsoft.com/office/drawing/2016/SVG/main",
    "p14": "http://schemas.microsoft.com/office/powerpoint/2010/main",
}
A = "{%s}" % NS["a"]
R = "{%s}" % NS["r"]

CANVAS_W = 980
EMU_PER_PT = 12700

src, out = Path(sys.argv[1]), Path(sys.argv[2])
prs = Presentation(src)
SW, SH = prs.slide_width, prs.slide_height
PX = CANVAS_W / SW  # px per EMU
PT = CANVAS_W / (SW / EMU_PER_PT)  # px per pt
MEDIA = out / "public" / "media"
MEDIA.mkdir(parents=True, exist_ok=True)

warnings = []


def warn(msg):
    warnings.append(msg)


# ---------------------------------------------------------------- colors
theme_xml = None
for rel in prs.slide_master.part.rels.values():
    if rel.reltype.endswith("/theme"):
        from lxml import etree

        theme_xml = etree.fromstring(rel.target_part.blob)
SCHEME = {}
for el in theme_xml.find(".//a:clrScheme", NS):
    c = el[0]
    SCHEME[el.tag.split("}")[1]] = c.get("lastClr") or c.get("val")
for alias, real in {"tx1": "dk1", "tx2": "dk2", "bg1": "lt1", "bg2": "lt2"}.items():
    SCHEME[alias] = SCHEME[real]


def resolve_color(fill):
    """fill: an element containing a color child (solidFill, schemeClr parent, ...)."""
    if fill is None:
        return None
    c = None
    for child in fill:
        tag = child.tag.split("}")[1]
        if tag == "srgbClr":
            c = child.get("val")
        elif tag == "schemeClr":
            c = SCHEME.get(child.get("val"))
        elif tag == "sysClr":
            c = child.get("lastClr")
        elif tag == "prstClr":
            c = {"black": "000000", "white": "FFFFFF", "red": "FF0000"}.get(child.get("val"))
        else:
            continue
        mods = child
        break
    if c is None:
        return None
    r, g, b = (int(c[i : i + 2], 16) / 255 for i in (0, 2, 4))
    for m in mods:
        tag, v = m.tag.split("}")[1], int(m.get("val", "100000")) / 100000
        if tag in ("lumMod", "lumOff"):
            h, l, s = colorsys.rgb_to_hls(r, g, b)
            l = l * v if tag == "lumMod" else min(1, l + v)
            r, g, b = colorsys.hls_to_rgb(h, l, s)
        elif tag == "shade":
            r, g, b = r * v, g * v, b * v
        elif tag == "tint":
            r, g, b = (x + (1 - x) * (1 - v) for x in (r, g, b))
    return "#%02X%02X%02X" % tuple(round(x * 255) for x in (r, g, b))


def shape_fill(sp):
    sppr = sp.find("p:spPr", NS)
    if sppr is not None:
        if sppr.find("a:noFill", NS) is not None:
            return None
        if (f := sppr.find("a:solidFill", NS)) is not None:
            return resolve_color(f)
    ref = sp.find("p:style/a:fillRef", NS)
    if ref is not None and ref.get("idx") != "0":
        return resolve_color(ref)
    return None


def shape_line(sp, use_style=True):
    """(color, width_px) or None."""
    ln = sp.find("p:spPr/a:ln", NS)
    width = int(ln.get("w")) * PX if ln is not None and ln.get("w") else 1 * PT
    if ln is not None:
        if ln.find("a:noFill", NS) is not None:
            return None
        if (f := ln.find("a:solidFill", NS)) is not None:
            return resolve_color(f), width
    if not use_style:
        return None
    ref = sp.find("p:style/a:lnRef", NS)
    if ref is not None and ref.get("idx") != "0":
        return resolve_color(ref), width
    return None


def is_dashed(sp):
    d = sp.find("p:spPr/a:ln/a:prstDash", NS)
    return d is not None and d.get("val", "solid") != "solid"


# ---------------------------------------------------------------- geometry
def xfrm_of(el):
    for path in ("p:spPr/a:xfrm", "p:grpSpPr/a:xfrm"):
        x = el.find(path, NS)
        if x is not None:
            return x
    return None


def box(el, tf):
    """Absolute (x, y, w, h, rot, flipH, flipV) in px, via group transform tf."""
    x = xfrm_of(el)
    if x is None or x.find("a:off", NS) is None:
        # placeholder inheriting its position from the layout
        shp = SHAPE_BY_EL[el]
        ox, oy, cx, cy = shp.left, shp.top, shp.width, shp.height
        x = {}
    else:
        off, ext = x.find("a:off", NS), x.find("a:ext", NS)
        ox, oy = int(off.get("x")), int(off.get("y"))
        cx, cy = int(ext.get("cx")), int(ext.get("cy"))
    X0, Y0, sx, sy = tf
    rot = int(x.get("rot", "0")) / 60000
    return (
        X0 + ox * sx,
        Y0 + oy * sy,
        cx * sx,
        cy * sy,
        rot,
        x.get("flipH") == "1",
        x.get("flipV") == "1",
    )


def group_tf(grp, tf):
    x = grp.find("p:grpSpPr/a:xfrm", NS)
    off, ext = x.find("a:off", NS), x.find("a:ext", NS)
    choff, chext = x.find("a:chOff", NS), x.find("a:chExt", NS)
    X0, Y0, sx, sy = tf
    gx, gy = X0 + int(off.get("x")) * sx, Y0 + int(off.get("y")) * sy
    kx = int(ext.get("cx")) / int(chext.get("cx")) * sx
    ky = int(ext.get("cy")) / int(chext.get("cy")) * sy
    return (gx - int(choff.get("x")) * kx, gy - int(choff.get("y")) * ky, kx, ky)


def n(v):
    return str(round(v))


def pos_style(b, height=True):
    x, y, w, h, rot, fh, fv = b
    s = f"left:{n(x)}px; top:{n(y)}px; width:{n(w)}px"
    if height:
        s += f"; height:{n(h)}px"
    tr = []
    if rot:
        tr.append(f"rotate({rot:g}deg)")
    if fh:
        tr.append("scaleX(-1)")
    if fv:
        tr.append("scaleY(-1)")
    if tr:
        s += "; transform:" + " ".join(tr)
    return s


# ---------------------------------------------------------------- text
def clean(t):
    return t.replace("", "→").replace("\u000b", " ").replace("\xa0", " ")


def esc(t):
    t = clean(t)
    t = t.replace("\\", "\\\\")
    t = re.sub(r"([*_`\[\]$~])", r"\\\1", t)
    t = t.replace("<", "&lt;").replace(">", "&gt;").replace("{{", "{&#8203;{")
    # keep markdown's typographer from turning (C) into a copyright sign etc.
    t = re.sub(r"\((c|r|tm|p)\)", r"&#40;\1)", t, flags=re.I)
    return t


def esc_line_start(t):
    # stop markdown from reading a paragraph start as a list/heading/quote
    return re.sub(r"^(\s*)([-+#]|\d+[.)])", lambda m: m.group(1) + "\\" + m.group(2) if not m.group(2)[0].isdigit() else m.group(1) + m.group(2)[:-1] + "\\" + m.group(2)[-1], t)


def lvl_ppr(lst, level):
    if lst is None:
        return None
    return lst.find(f"a:lvl{level + 1}pPr", NS)


def para_props(p, lst, level, default_bullet):
    ppr = p.find("a:pPr", NS)
    bullet = None
    algn = None
    for src_ in (ppr, lvl_ppr(lst, level)):
        if src_ is None:
            continue
        if bullet is None:
            if src_.find("a:buNone", NS) is not None:
                bullet = False
            elif src_.find("a:buChar", NS) is not None:
                bullet = "-"
            elif src_.find("a:buAutoNum", NS) is not None:
                bullet = "1."
        if algn is None:
            algn = src_.get("algn")
    if bullet is None:
        bullet = "-" if default_bullet else False
    return bullet, algn or "l"


def run_items(p, lst, level, default_sz, part, scale):
    """Yield dicts describing runs in paragraph p."""
    lvl = lvl_ppr(lst, level)
    lvl_rpr = lvl.find("a:defRPr", NS) if lvl is not None else None
    for child in p:
        tag = child.tag.split("}")[1]
        if tag == "br":
            yield {"br": True}
            continue
        if tag not in ("r", "fld"):
            continue
        t = child.find("a:t", NS)
        text = t.text if t is not None and t.text else ""
        if not text:
            continue
        rpr = child.find("a:rPr", NS)

        def attr(name):
            for e in (rpr, lvl_rpr):
                if e is not None and e.get(name) is not None:
                    return e.get(name)
            return None

        sz = attr("sz")
        size = (int(sz) / 100 if sz else default_sz) * scale
        color = None
        for e in (rpr, lvl_rpr):
            if e is not None and (f := e.find("a:solidFill", NS)) is not None:
                color = resolve_color(f)
                break
        link = None
        if rpr is not None and (h := rpr.find("a:hlinkClick", NS)) is not None:
            rid = h.get(R + "id")
            if rid and rid in part.rels:
                rel = part.rels[rid]
                link = rel.target_ref if rel.is_external else None
        yield {
            "text": text,
            "b": attr("b") == "1",
            "i": attr("i") == "1",
            "u": (attr("u") or "none") != "none",
            "size": size,
            "color": color,
            "link": link,
            "sup": int(attr("baseline") or 0) > 0,
            "sub": int(attr("baseline") or 0) < 0,
        }


def fmt_runs(runs, expected_size, default_color, in_title=False):
    # merge adjacent runs with identical formatting
    merged = []
    for r in runs:
        if "br" in r:
            merged.append(r)
            continue
        key = {k: v for k, v in r.items() if k != "text"}
        if merged and "br" not in merged[-1] and {k: v for k, v in merged[-1].items() if k != "text"} == key:
            merged[-1]["text"] += r["text"]
        else:
            merged.append(dict(r))
    out_ = []
    for r in merged:
        if "br" in r:
            out_.append("<br>")
            continue
        text = clean(r["text"])
        lead = text[: len(text) - len(text.lstrip())]
        trail = text[len(text.rstrip()) :]
        core = text.strip()
        if not core:
            out_.append(" " if text else "")
            continue
        s = esc(core)
        if r["link"]:
            if re.fullmatch(r"https?://\S+", core):
                s = f"<{core}>"
            else:
                s = f"[{s}]({r['link'].strip()})"
        elif re.fullmatch(r"https?://\S+", core):
            s = f"<{core}>"
        if r["b"]:
            s = f"**{s}**"
        if r["i"]:
            s = f"*{s}*"
        if r["u"] and not r["link"]:
            s = f"<u>{s}</u>"
        if r["sup"]:
            s = f"<sup>{s}</sup>"
        if r["sub"]:
            s = f"<sub>{s}</sub>"
        style = []
        near_black = r["color"] and max(int(r["color"][i : i + 2], 16) for i in (1, 3, 5)) < 0x40
        if r["color"] and r["color"] != default_color and not (near_black and not default_color) and not r["link"]:
            style.append(f"color:{r['color']}")
        if not in_title and expected_size and abs(r["size"] - expected_size) > 2 and not (r["sup"] or r["sub"]):
            style.append(f"font-size:{n(r['size'] * PT)}px")
        if style:
            s = f'<span style="{"; ".join(style)}">{s}</span>'
        out_.append(lead + s + trail)
    return "".join(out_).strip()


LEVEL_RATIO = 0.86  # matches the nested-list font-size rule in style.css


def text_body(sp, part, kind, default_color=None):
    """Return (markdown, base_font_px, align, anchor) or None if empty."""
    txb = sp.find("p:txBody", NS)
    if txb is None:
        return None
    lst = txb.find("a:lstStyle", NS)
    bodypr = txb.find("a:bodyPr", NS)
    scale = 1.0
    if bodypr is not None and (na := bodypr.find("a:normAutofit", NS)) is not None and na.get("fontScale"):
        scale = int(na.get("fontScale")) / 100000
    default_sz = {"title": 44, "subtitle": 24, "body": 28}.get(kind, 18)
    default_bullet = kind == "body"
    paras = []
    for p in txb.findall("a:p", NS):
        ppr = p.find("a:pPr", NS)
        level = int(ppr.get("lvl", "0")) if ppr is not None else 0
        runs = list(run_items(p, lst, level, default_sz, part, scale))
        if not any(r.get("text", "").strip() for r in runs):
            continue
        bullet, algn = para_props(p, lst, level, default_bullet)
        paras.append((level, bullet, algn, runs))
    if not paras:
        return None
    # base font size: most common size among top-level text (weighted by length)
    sizes = Counter()
    min_level = min(lv for lv, *_ in paras)
    for lv, _, _, runs in paras:
        for r in runs:
            if "text" in r and lv == min_level:
                sizes[round(r["size"], 1)] += len(r["text"])
    base = sizes.most_common(1)[0][0]
    # size ratio of nested bullets to their parent, per box
    sub = Counter()
    for lv, bullet, _, runs in paras:
        if bullet and lv == min_level + 1:
            for r in runs:
                if "text" in r:
                    sub[round(r["size"], 1)] += len(r["text"])
    nest = sub.most_common(1)[0][0] / base if sub else LEVEL_RATIO
    aligns = {a for _, _, a, _ in paras}
    align = aligns.pop() if len(aligns) == 1 else "l"
    anchor = bodypr.get("anchor", "t") if bodypr is not None else "t"

    lines = []
    prev_bullet = None
    for lv, bullet, algn, runs in paras:
        rel = lv - min_level
        expected = base * (nest**rel if bullet else 1)
        md = fmt_runs(runs, expected, default_color, in_title=kind == "title")
        if kind == "title":
            lines.append(md)
            continue
        if bullet:
            if prev_bullet is False:
                lines.append("")
            lines.append("  " * rel + f"{bullet} {md}")
        else:
            if lines:
                lines.append("")
            lines.append(esc_line_start(md))
        prev_bullet = bool(bullet)
    if kind == "title":
        return "<br>".join(lines), base, align, anchor, nest
    return "\n".join(lines), base, align, anchor, nest


# ---------------------------------------------------------------- media
media_names = {}
used_names = set()


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:40] or "img"


def save_media(blob, ext, slide_no, name, crop=None, fade=None):
    key = hashlib.sha1(blob + repr((crop, fade)).encode()).hexdigest()
    if key in media_names:
        return media_names[key]
    ext = ext.lower().replace("jpeg", "jpg")
    if (crop or fade) and ext in ("png", "jpg"):
        im = Image.open(io.BytesIO(blob))
        if crop:
            W, H = im.size
            l, t, r, b = (max(0.0, c) for c in crop)
            box_ = (round(W * l), round(H * t), round(W * (1 - r)), round(H * (1 - b)))
            im = im.crop(box_)
        if fade:
            # bake picture transparency in, as if over a white slide
            im = Image.blend(Image.new("RGB", im.size, "white"), im.convert("RGB"), fade)
        buf = io.BytesIO()
        if ext == "jpg":
            im.convert("RGB").save(buf, "JPEG", quality=92)
        else:
            im.save(buf, "PNG", optimize=True)
        blob = buf.getvalue()
        crop = None
    fname = f"s{slide_no:02d}-{slug(name)}.{ext}"
    i = 2
    while fname in used_names:
        fname = f"s{slide_no:02d}-{slug(name)}-{i}.{ext}"
        i += 1
    used_names.add(fname)
    (MEDIA / fname).write_bytes(blob)
    media_names[key] = (fname, crop)
    return fname, crop


def get_alpha(pic):
    am = pic.find("p:blipFill/a:blip/a:alphaModFix", NS)
    if am is None:
        return None
    a = int(am.get("amt", "100000")) / 100000
    return a if a < 0.999 else None


def get_crop(pic):
    sr = pic.find("p:blipFill/a:srcRect", NS)
    if sr is None:
        return None
    c = tuple(int(sr.get(k, "0")) / 100000 for k in ("l", "t", "r", "b"))
    return c if any(c) else None


# ---------------------------------------------------------------- shapes
def ph_kind(el):
    ph = el.find("p:nvSpPr/p:nvPr/p:ph", NS)
    if ph is None:
        return None
    return ph.get("type", "body")


def is_title_box(el, b):
    name = el.find("p:nvSpPr/p:cNvPr", NS).get("name", "")
    x, y, w, h, *_ = b
    return name.startswith("Title") and y < SH * PX * 0.05 and w > CANVAS_W * 0.9


def render_text_div(md, base, align, anchor, nest, b, extra_style="", height=False):
    style = pos_style(b, height=height or anchor != "t")
    style += f"; font-size:{n(base * PT)}px"
    if abs(nest - LEVEL_RATIO) > 0.03:
        style += f"; --nest:{nest:.2f}"
    if align == "ctr":
        style += "; text-align:center"
    elif align == "r":
        style += "; text-align:right"
    if anchor in ("ctr", "b"):
        style += "; display:flex; flex-direction:column; justify-content:" + ("center" if anchor == "ctr" else "flex-end")
    style += extra_style
    return f'<div class="abs" style="{style}">\n\n{md}\n\n</div>'


ARROWS = {"rightArrow": "right", "leftArrow": "left", "upArrow": "up", "downArrow": "down"}
FLIP_DIR = {"right": "left", "left": "right", "up": "down", "down": "up"}


def convert_shapes(elements, part, slide_no, tf, ctx):
    for el in elements:
        tag = el.tag.split("}")[1]
        if tag == "grpSp":
            convert_shapes(list(el)[2:], part, slide_no, group_tf(el, tf), ctx)
            continue
        if tag in ("nvGrpSpPr", "grpSpPr", "extLst"):
            continue
        if tag == "AlternateContent":
            choice = el[0]
            convert_shapes(list(choice), part, slide_no, tf, ctx)
            continue
        if tag == "graphicFrame":
            warn(f"slide {slide_no}: graphicFrame (table/chart) skipped")
            continue
        b = box(el, tf)
        name = el.find(".//p:cNvPr", NS).get("name", "")

        if tag == "pic":
            convert_pic(el, b, part, slide_no, name, ctx)
            continue

        if tag == "cxnSp":
            ln = shape_line(el)
            if ln is None:
                continue
            color, width = ln
            x, y, w, h, rot, fh, fv = b
            x1, y1, x2, y2 = x, y, x + w, y + h
            if fh:
                x1, x2 = x2, x1
            if fv:
                y1, y2 = y2, y1
            lnel = el.find("p:spPr/a:ln", NS)
            head = lnel is not None and lnel.find("a:headEnd", NS) is not None and lnel.find("a:headEnd", NS).get("type", "none") != "none"
            tail = lnel is not None and lnel.find("a:tailEnd", NS) is not None and lnel.find("a:tailEnd", NS).get("type", "none") != "none"
            arrow = {(True, True): "both", (False, True): "end", (True, False): "start"}.get((head, tail))
            attrs = f'x1="{n(x1)}" y1="{n(y1)}" x2="{n(x2)}" y2="{n(y2)}" color="{color}" width="{n(width)}"'
            if arrow:
                attrs += f' arrow="{arrow}"'
            if is_dashed(el):
                attrs += " dashed"
            ctx["body"].append(f"<Line {attrs} />")
            continue

        if tag != "sp":
            warn(f"slide {slide_no}: unknown element {tag} skipped")
            continue

        kind = ph_kind(el)
        if kind in ("sldNum", "dt", "ftr"):
            continue
        if kind in ("title", "ctrTitle") or (kind is None and is_title_box(el, b)):
            tb = text_body(el, part, "title")
            if tb:
                ctx["title"] = tb
            continue

        geom = el.find("p:spPr/a:prstGeom", NS)
        prst = geom.get("prst") if geom is not None else ("rect" if kind else None)
        is_txbox = el.find("p:nvSpPr/p:cNvSpPr", NS).get("txBox") == "1" or kind is not None
        font_ref = el.find("p:style/a:fontRef", NS)
        default_color = resolve_color(font_ref) if font_ref is not None else None
        tb = text_body(el, part, {"subTitle": "subtitle", "body": "body", None: None}.get(kind, "body"), default_color)

        if kind == "subTitle" and ctx["cover"]:
            if tb:
                ctx["flow"].append(tb[0])
            continue

        if prst in ARROWS:
            d = ARROWS[prst]
            x, y, w, h, rot, fh, fv = b
            if (fh and d in ("left", "right")) or (fv and d in ("up", "down")):
                d = FLIP_DIR[d]
            color = shape_fill(el) or "currentColor"
            adj = {g.get("name"): int(g.get("fmla").split()[1]) / 1000 for g in el.findall("p:spPr/a:prstGeom/a:avLst/a:gd", NS)}
            extra = "".join(f' {k}="{v:g}"' for k, v in adj.items() if k in ("adj1", "adj2"))
            rot_attr = f' rotate="{rot:g}"' if rot else ""
            ctx["body"].append(
                f'<BlockArrow dir="{d}" x="{n(x)}" y="{n(y)}" w="{n(w)}" h="{n(h)}" color="{color}"{extra}{rot_attr} />'
            )
            if tb:
                md, base, align, anchor, nest = tb
                st = f"; color:{default_color}" if default_color else ""
                ctx["body"].append(render_text_div(md, base, align, anchor, nest, (x, y, w, h, rot, False, False), st))
            continue

        if prst in ("rect", "roundRect", "ellipse", None) or prst:
            if prst not in ("rect", "roundRect", "ellipse"):
                warn(f"slide {slide_no}: shape geometry {prst!r} ({name}) drawn as a rectangle")
            fill = shape_fill(el)
            line = shape_line(el)
            st = ""
            if fill:
                st += f"; background:{fill}"
            if line:
                st += f"; border:{n(max(1, line[1]))}px {'dashed' if is_dashed(el) else 'solid'} {line[0]}"
            if prst == "roundRect":
                st += "; border-radius:12px"
            if prst == "ellipse":
                st += "; border-radius:50%"
            if default_color:
                st += f"; color:{default_color}"
            if tb:
                md, base, align, anchor, nest = tb
                ctx["body"].append(render_text_div(md, base, align, anchor, nest, b, st, height=bool(fill or line)))
            elif fill or line:
                ctx["body"].append(f'<div class="abs" style="{pos_style(b)}{st}; padding:0"></div>')
            continue


def convert_pic(el, b, part, slide_no, name, ctx):
    x, y, w, h, *_ = b
    # full-bleed picture at the back of a cover slide -> slide background
    if ctx["cover"] and not ctx["body"] and w > CANVAS_W * 0.98 and x <= 1 and y <= 1:
        blip = el.find(".//a:blip", NS)
        img = part.related_part(blip.get(R + "embed"))
        fname, _ = save_media(img.blob, img.partname.ext, slide_no, "background", get_crop(el), get_alpha(el))
        ctx["background"] = fname
        return
    # video?
    vid = el.find("p:nvPicPr/p:nvPr/a:videoFile", NS)
    if vid is not None:
        media = el.find(".//p14:media", NS)
        rid = media.get(R + "embed") if media is not None else vid.get(R + "link")
        vpart = part.related_part(rid)
        fname, _ = save_media(vpart.blob, vpart.partname.ext, slide_no, name)
        poster = ""
        blip = el.find(".//a:blip", NS)
        if blip is not None and blip.get(R + "embed"):
            pp = part.related_part(blip.get(R + "embed"))
            pname, _ = save_media(pp.blob, pp.partname.ext, slide_no, name + "-poster")
            poster = f' poster="/media/{pname}"'
        ctx["body"].append(f'<video class="abs" src="/media/{fname}"{poster} controls style="{pos_style(b)}"></video>')
        return
    svg = el.find(".//asvg:svgBlip", NS)
    blip = el.find(".//a:blip", NS)
    rid = svg.get(R + "embed") if svg is not None else blip.get(R + "embed")
    img = part.related_part(rid)
    crop = get_crop(el)
    fname, crop = save_media(img.blob, img.partname.ext, slide_no, name, crop)
    st = pos_style(b)
    if (alpha := get_alpha(el)) is not None:
        st += f"; opacity:{alpha:g}"
    line = shape_line(el, use_style=False)
    if line:
        st += f"; border:{n(max(1, line[1]))}px solid {line[0]}"
    if crop:
        # CSS crop for formats we don't re-encode (gif/svg)
        l, t, r, bt = crop
        iw, ih = 100 / (1 - l - r), 100 / (1 - t - bt)
        ctx["body"].append(
            f'<div class="abs" style="{st}; overflow:hidden; padding:0">'
            f'<img src="/media/{fname}" style="position:absolute; max-width:none; width:{iw:.1f}%; height:{ih:.1f}%; left:{-l * iw:.1f}%; top:{-t * ih:.1f}%"></div>'
        )
    else:
        ctx["body"].append(f'<img class="abs" src="/media/{fname}" style="{st}">')


# ---------------------------------------------------------------- slides
def notes_of(slide):
    if not slide.has_notes_slide:
        return ""
    t = slide.notes_slide.notes_text_frame.text
    t = clean(t).strip().replace("-->", "-- >")
    return re.sub(r"\n{3,}", "\n\n", t)


chunks = []
for idx, slide in enumerate(prs.slides, 1):
    layout = slide.slide_layout.name
    ctx = {
        "cover": layout == "Title Slide",
        "body": [],
        "flow": [],
        "title": None,
        "background": None,
    }
    SHAPE_BY_EL = {shp._element: shp for shp in slide.shapes}
    convert_shapes(list(slide.shapes._spTree)[2:], slide.part, idx, (0, 0, PX, PX), ctx)

    fm = {}
    if ctx["cover"]:
        fm["layout"] = "section"
        if ctx["background"]:
            fm["background"] = f"/media/{ctx['background']}"
    if slide._element.get("show") == "0":
        fm["hide"] = "true"

    lines = []
    if ctx["title"]:
        md, base, *_ = ctx["title"]
        lines.append(f"# {md}")
        default_title = 44 if not ctx["cover"] else None
        if default_title and abs(base - default_title) > 1:
            lines.append("")
            lines.append(f"<style>\n.slidev-layout.default h1 {{ font-size: {n(base * PT)}px; }}\n</style>")
    for f in ctx["flow"]:
        lines.append("")
        lines.append(f)
    for item in ctx["body"]:
        lines.append("")
        lines.append(item)
    nt = notes_of(slide)
    if nt:
        lines.append("")
        lines.append(f"<!--\n{nt}\n-->")
    chunks.append((idx, fm, "\n".join(lines)))

HEADMATTER = """\
theme: default
title: Image Analysis with Fiji/ImageJ
info: |
  AQLM image analysis lecture, converted from AQLM_2026_NC.pptx.
colorSchema: light
aspectRatio: 16/9
canvasWidth: 980
transition: none
"""

parts = []
for idx, fm, body in chunks:
    fm_text = "".join(f"{k}: {v}\n" for k, v in fm.items())
    if idx == 1:
        parts.append(f"---\n{HEADMATTER}{fm_text}---\n\n{body}\n")
    else:
        header = f"---\n{fm_text}---\n\n" if fm_text else "---\n\n"
        parts.append(f"{header}<!-- slide {idx} -->\n\n{body}\n")
(out / "slides.md").write_text("\n".join(parts), encoding="utf-8")
print(f"wrote {len(chunks)} slides, {len(media_names)} media files")
for w in warnings:
    print("WARN", w)
