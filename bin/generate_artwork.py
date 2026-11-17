#!/usr/bin/env python3
"""Generate the illustrated cover images for projects and publications.

Each illustration is written as an SVG (one shared visual style) and then
rasterised to PNG with ImageMagick:

    python3 bin/generate_artwork.py

Outputs:
    assets/img/projects/<name>.png
    assets/img/publication_preview/<name>.png
"""

import random
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
W, H = 1200, 750

# Palette
BG0, BG1 = "#0d0f24", "#25124a"
MAGENTA = "#e44fd8"
VIOLET = "#9b6bff"
CYAN = "#3fd4f0"
AMBER = "#ffbf47"
GREEN = "#3ddc97"
RED = "#ff6b7a"
INK = "#e9e6ff"
DIM = "#8f8bb8"
PANEL = "#171a3a"
PANEL2 = "#1f2350"
SANS = "Noto Sans, sans-serif"
MONO = "Source Code Pro, Noto Sans Mono, monospace"


def frame(body, label, accent=MAGENTA, seed=0):
    """Wrap an illustration body in the common background, grid and label."""
    rnd = random.Random(seed)
    stars = "".join(
        f'<circle cx="{rnd.uniform(0, W):.0f}" cy="{rnd.uniform(0, H):.0f}" '
        f'r="{rnd.choice([0.8, 1.1, 1.5])}" fill="#fff" opacity="{rnd.uniform(0.15, 0.5):.2f}"/>'
        for _ in range(70)
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{BG0}"/><stop offset="1" stop-color="{BG1}"/>
  </linearGradient>
  <radialGradient id="halo" cx="0.5" cy="0.5" r="0.5">
    <stop offset="0" stop-color="{accent}" stop-opacity="0.35"/>
    <stop offset="1" stop-color="{accent}" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="halo2" cx="0.5" cy="0.5" r="0.5">
    <stop offset="0" stop-color="{CYAN}" stop-opacity="0.22"/>
    <stop offset="1" stop-color="{CYAN}" stop-opacity="0"/>
  </radialGradient>
  <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
    <path d="M40 0H0V40" fill="none" stroke="#ffffff" stroke-opacity="0.045" stroke-width="1"/>
  </pattern>
  <filter id="glow" filterUnits="userSpaceOnUse" x="0" y="0" width="{W}" height="{H}">
    <feGaussianBlur stdDeviation="7" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <filter id="soft" x="-20%" y="-20%" width="140%" height="140%">
    <feGaussianBlur stdDeviation="16"/>
  </filter>
  <filter id="shadow" x="-20%" y="-20%" width="140%" height="150%">
    <feDropShadow dx="0" dy="14" stdDeviation="16" flood-color="#000" flood-opacity="0.45"/>
  </filter>
</defs>
<rect width="{W}" height="{H}" fill="url(#bg)"/>
<rect width="{W}" height="{H}" fill="url(#grid)"/>
<circle cx="{W * 0.72}" cy="{H * 0.38}" r="420" fill="url(#halo)"/>
<circle cx="{W * 0.18}" cy="{H * 0.85}" r="360" fill="url(#halo2)"/>
{stars}
{body}
<g font-family="{MONO}" font-size="22" letter-spacing="3">
  <rect x="40" y="{H - 74}" width="{len(label) * 16.6 + 50}" height="40" rx="20" fill="#000" fill-opacity="0.35" stroke="{accent}" stroke-opacity="0.6"/>
  <circle cx="62" cy="{H - 54}" r="6" fill="{accent}"/>
  <text x="78" y="{H - 46}" fill="{INK}">{label}</text>
</g>
</svg>"""


def window(x, y, w, h, title="", fill=PANEL):
    dots = "".join(
        f'<circle cx="{x + 24 + i * 22}" cy="{y + 22}" r="6" fill="{c}"/>'
        for i, c in enumerate([RED, AMBER, GREEN])
    )
    return f"""<g filter="url(#shadow)">
  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{fill}" stroke="#ffffff" stroke-opacity="0.12"/>
  <path d="M{x} {y + 44}h{w}" stroke="#ffffff" stroke-opacity="0.08"/>
  {dots}
  <text x="{x + w / 2}" y="{y + 29}" text-anchor="middle" font-family="{MONO}" font-size="17" fill="{DIM}">{title}</text>
</g>"""


def photo_tile(x, y, w, h, scene, rnd):
    """A tiny abstract 'photo': sky gradient, sun/moon and hills."""
    skies = [("#ff9a8b", "#6a3093"), ("#5ee7df", "#3b4cca"), ("#f6d365", "#fd7f6f"),
             ("#a1c4fd", "#5b2a86"), ("#43e97b", "#1f6f8b"), ("#fbc2eb", "#4a3f9e")]
    a, b = skies[scene % len(skies)]
    gid = f"sky{scene}_{int(x)}_{int(y)}"
    sun_x = x + w * rnd.uniform(0.2, 0.8)
    sun_y = y + h * rnd.uniform(0.2, 0.45)
    hill1 = f"M{x} {y + h * 0.75} Q{x + w * 0.3} {y + h * rnd.uniform(0.45, 0.6)} {x + w * 0.6} {y + h * 0.72} T{x + w} {y + h * 0.66} V{y + h} H{x}Z"
    hill2 = f"M{x} {y + h * 0.88} Q{x + w * 0.5} {y + h * rnd.uniform(0.62, 0.75)} {x + w} {y + h * 0.85} V{y + h} H{x}Z"
    return f"""<defs><linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></linearGradient>
<clipPath id="c{gid}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12"/></clipPath></defs>
<g clip-path="url(#c{gid})">
<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#{gid})"/>
<circle cx="{sun_x:.0f}" cy="{sun_y:.0f}" r="{min(w, h) * 0.12:.0f}" fill="#fff" opacity="0.8"/>
<path d="{hill1}" fill="#000" opacity="0.25"/>
<path d="{hill2}" fill="#000" opacity="0.4"/>
</g>"""


# --------------------------------------------------------------------------
# Illustrations
# --------------------------------------------------------------------------


def needle():
    rnd = random.Random(3)
    tiles = []
    gx, gy, tw, th, gap = 560, 110, 165, 120, 18
    best = (1, 1)
    for r in range(4):
        for c in range(3):
            x, y = gx + c * (tw + gap), gy + r * (th + gap)
            op = 1 if (r, c) == best else 0.38
            tiles.append(f'<g opacity="{op}">{photo_tile(x, y, tw, th, r * 3 + c, rnd)}</g>')
    bx, by = gx + best[1] * (tw + gap), gy + best[0] * (th + gap)
    hl = f"""<rect x="{bx - 6}" y="{by - 6}" width="{tw + 12}" height="{th + 12}" rx="16" fill="none" stroke="{AMBER}" stroke-width="5" filter="url(#glow)"/>
<g transform="translate({bx + tw - 18},{by - 14})"><circle r="22" fill="{AMBER}"/><text y="8" text-anchor="middle" font-family="{SANS}" font-weight="700" font-size="20" fill="{BG0}">#1</text></g>"""
    query = f"""<g filter="url(#shadow)">
<rect x="70" y="210" width="400" height="150" rx="22" fill="{PANEL2}" stroke="{MAGENTA}" stroke-opacity="0.7" stroke-width="2"/>
</g>
<text x="98" y="250" font-family="{MONO}" font-size="18" fill="{DIM}">query&gt;</text>
<text x="98" y="290" font-family="{SANS}" font-size="25" fill="{INK}">"a lone sun setting behind</text>
<text x="98" y="326" font-family="{SANS}" font-size="25" fill="{INK}">two rolling hills"</text>
<path d="M470 285 C 520 285, 520 {by + th / 2}, {bx - 10} {by + th / 2}" fill="none" stroke="{MAGENTA}" stroke-width="4" stroke-dasharray="2 10" stroke-linecap="round" filter="url(#glow)"/>
<g transform="translate(90 590) rotate(-14)">
  <path d="M0 0 L300 -6 L300 6 Z" fill="#dfe4ff"/>
  <ellipse cx="270" cy="0" rx="16" ry="4" fill="{BG0}"/>
  <path d="M286 0 C 340 -40, 360 40, 420 0" fill="none" stroke="{MAGENTA}" stroke-width="3"/>
</g>"""
    return frame("".join(tiles) + hl + query, "NEEDLE · TEXT→IMAGE RETRIEVAL", MAGENTA, 1)


def needledb():
    rnd = random.Random(8)
    cyl = []
    cx, top = 330, 230
    for i in range(3):
        y = top + i * 95
        cyl.append(f"""<path d="M{cx - 170} {y} v80 a170 42 0 0 0 340 0 v-80" fill="{PANEL2}" stroke="{CYAN}" stroke-opacity="0.6" stroke-width="2"/>
<ellipse cx="{cx}" cy="{y}" rx="170" ry="42" fill="#2a2f6a" stroke="{CYAN}" stroke-opacity="0.8" stroke-width="2"/>""")
    cyl.reverse()
    flows = []
    for i in range(6):
        y = 150 + i * 80
        x = 740 + (i % 2) * 70
        flows.append(photo_tile(x, y, 110, 66, i + 2, rnd))
        flows.append(f'<path d="M{x - 10} {y + 33} C {x - 120} {y + 33}, 600 {330}, 520 {330}" fill="none" stroke="{CYAN}" stroke-opacity="0.45" stroke-width="2" stroke-dasharray="6 8"/>')
    idx = "".join(
        f'<rect x="{960 + (i % 4) * 44}" y="{220 + (i // 4) * 44}" width="34" height="34" rx="6" fill="{[VIOLET, CYAN, MAGENTA, AMBER][i % 4]}" opacity="{0.35 + 0.15 * (i % 3)}"/>'
        for i in range(16)
    )
    body = f"""{''.join(cyl)}
<text x="{cx}" y="{top + 8}" text-anchor="middle" font-family="{MONO}" font-size="24" fill="{INK}">vector index</text>
{''.join(flows)}
{idx}
<text x="1034" y="420" text-anchor="middle" font-family="{MONO}" font-size="18" fill="{DIM}">embeddings</text>
<g transform="translate(150 610) rotate(-12)"><path d="M0 0 L360 -5 L360 5 Z" fill="#dfe4ff"/><ellipse cx="330" cy="0" rx="14" ry="3.5" fill="{BG0}"/></g>"""
    return frame(body, "NEEDLEDB · GENAI IMAGE DATABASE", CYAN, 2)


def rsr():
    rnd = random.Random(5)
    cell, ox, oy, n, m = 42, 90, 140, 10, 8
    cols = {1: GREEN, -1: RED, 0: "#3a3f78"}
    cells = []
    for i in range(n):
        for j in range(m):
            v = rnd.choice([1, -1, 0, 0, 1, -1])
            cells.append(f'<rect x="{ox + j * cell}" y="{oy + i * cell}" width="{cell - 5}" height="{cell - 5}" rx="6" fill="{cols[v]}" opacity="{0.9 if v else 0.6}"/>')
            sym = {1: "+1", -1: "−1", 0: "0"}[v]
            cells.append(f'<text x="{ox + j * cell + (cell - 5) / 2}" y="{oy + i * cell + 26}" text-anchor="middle" font-family="{MONO}" font-size="15" fill="#0d0f24" opacity="0.75">{sym}</text>')
    brackets = "".join(
        f'<path d="M{ox - 18} {oy + k * cell * 2.5 + 4} h-10 v{cell * 2.5 - 12} h10" fill="none" stroke="{AMBER}" stroke-width="3"/>'
        for k in range(4)
    )
    arrow = f'<path d="M470 350 H600" stroke="{MAGENTA}" stroke-width="6" stroke-linecap="round" filter="url(#glow)"/><path d="M590 334 L612 350 L590 366" fill="none" stroke="{MAGENTA}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'
    blocks = []
    for k in range(4):
        y = 170 + k * 95
        blocks.append(f'<rect x="650" y="{y}" width="{140 + k * 30}" height="60" rx="12" fill="{PANEL2}" stroke="{AMBER}" stroke-opacity="0.8" stroke-width="2"/>')
        blocks.append(f'<text x="672" y="{y + 38}" font-family="{MONO}" font-size="20" fill="{INK}">seg {k} → Σ</text>')
    speed = "".join(
        f'<path d="M{900 + i * 12} {460 + i * 26} h{220 - i * 30}" stroke="{CYAN}" stroke-width="4" stroke-linecap="round" opacity="{0.8 - i * 0.12}"/>'
        for i in range(5)
    )
    badge = f"""<g filter="url(#glow)"><text x="1045" y="320" text-anchor="middle" font-family="{SANS}" font-weight="800" font-size="110" fill="{AMBER}">24×</text></g>
<text x="1045" y="372" text-anchor="middle" font-family="{MONO}" font-size="22" fill="{INK}">faster than NumPy</text>
<text x="1045" y="410" text-anchor="middle" font-family="{MONO}" font-size="22" fill="{DIM}">2.5× on quantised LLMs</text>"""
    return frame("".join(cells) + brackets + arrow + "".join(blocks) + speed + badge,
                 "RSR · BINARY/TERNARY MATMUL", AMBER, 3)


def person(x, y, s, color, op=1.0, dashed=False):
    stroke = f'stroke="{color}" stroke-width="3" stroke-dasharray="6 6" fill="none"' if dashed else f'fill="{color}"'
    return f"""<g opacity="{op}"><circle cx="{x}" cy="{y}" r="{s * 0.32}" {stroke}/>
<path d="M{x - s * 0.55} {y + s * 1.05} Q{x - s * 0.55} {y + s * 0.42} {x} {y + s * 0.42} Q{x + s * 0.55} {y + s * 0.42} {x + s * 0.55} {y + s * 1.05} Z" {stroke}/></g>"""


def chameleon():
    rnd = random.Random(11)
    people = []
    palette = [VIOLET, CYAN, "#7fa4ff"]
    for i in range(5):
        for j in range(6):
            x, y = 110 + j * 82, 150 + i * 98
            if (i, j) in [(1, 4), (3, 1), (4, 5)]:
                people.append(person(x, y, 52, AMBER))
            else:
                people.append(person(x, y, 52, rnd.choice(palette), 0.55))
    gen = []
    for k, (x, y) in enumerate([(770, 210), (880, 250), (990, 210), (820, 360), (940, 380), (1060, 340)]):
        gen.append(person(x, y, 64, AMBER, 0.95))
        gen.append(f'<path d="M{x + 30} {y - 34} l4 -12 l4 12 l12 4 l-12 4 l-4 12 l-4 -12 l-12 -4z" fill="#fff" filter="url(#glow)"/>')
    arrow = f'<path d="M600 320 C 650 260, 690 260, 730 280" fill="none" stroke="{MAGENTA}" stroke-width="5" stroke-linecap="round" filter="url(#glow)"/><path d="M716 266 L734 282 L712 292" fill="none" stroke="{MAGENTA}" stroke-width="5" stroke-linecap="round"/>'
    bars = "".join(
        f'<rect x="{760 + i * 70}" y="{600 - h}" width="46" height="{h}" rx="8" fill="{c}"/>'
        for i, (h, c) in enumerate([(120, VIOLET), (112, CYAN), (104, "#7fa4ff"), (100, AMBER)])
    )
    bars += f'<rect x="970" y="540" width="46" height="60" rx="8" fill="{AMBER}" opacity="0.35"/><path d="M745 602 H1040" stroke="{DIM}" stroke-width="2"/><text x="900" y="640" text-anchor="middle" font-family="{MONO}" font-size="20" fill="{INK}">coverage restored</text>'
    return frame("".join(people) + arrow + "".join(gen) + bars, "CHAMELEON · FAIR AUGMENTATION", AMBER, 4)


def code_line(x, y, parts):
    out, cx = [], x
    for txt, col in parts:
        out.append(f'<text x="{cx}" y="{y}" font-family="{MONO}" font-size="22" fill="{col}" xml:space="preserve">{txt}</text>')
        cx += len(txt) * 13.2
    return "".join(out)


def delulu():
    x0, y0 = 90, 90
    win = window(x0, y0, 760, 520, "fim_task.py")
    kw, fn, st, cm = MAGENTA, CYAN, AMBER, DIM
    lines = [
        [("import ", kw), ("json", INK)],
        [("", INK)],
        [("def ", kw), ("load_config", fn), ("(path):", INK)],
        [("    with ", kw), ("open", fn), ("(path) ", INK), ("as ", kw), ("f:", INK)],
    ]
    body = [win]
    for i, ln in enumerate(lines):
        body.append(code_line(x0 + 40, y0 + 95 + i * 38, ln))
    hy = y0 + 95 + 4 * 38 - 26
    body.append(f'<rect x="{x0 + 30}" y="{hy}" width="690" height="128" rx="10" fill="{MAGENTA}" fill-opacity="0.10" stroke="{MAGENTA}" stroke-dasharray="8 6" stroke-width="2"/>')
    body.append(f'<text x="{x0 + 706}" y="{hy + 24}" text-anchor="end" font-family="{MONO}" font-size="15" fill="{MAGENTA}">&lt;MIDDLE&gt;</text>')
    body.append(code_line(x0 + 40, hy + 50, [("        cfg = json.", INK), ("load_yaml_safe", RED), ("(f)", INK)]))
    body.append(f'<path d="M{x0 + 40 + 19 * 13.2} {hy + 43} h{14 * 13.2}" stroke="{RED}" stroke-width="3"/>')
    body.append(code_line(x0 + 40, hy + 98, [("        cfg = json.", INK), ("load", GREEN), ("(f)", INK)]))
    after = [
        [("    return ", kw), ("cfg", INK)],
        [("", INK)],
        [("# suffix continues…", cm)],
    ]
    for i, ln in enumerate(after):
        body.append(code_line(x0 + 40, hy + 175 + i * 38, ln))
    body.append(f"""<g transform="translate(900 200)" filter="url(#shadow)">
<rect width="250" height="110" rx="18" fill="{PANEL2}" stroke="{RED}" stroke-width="2"/>
<circle cx="44" cy="55" r="22" fill="{RED}"/><path d="M34 45 l20 20 M54 45 l-20 20" stroke="{BG0}" stroke-width="5" stroke-linecap="round"/>
<text x="80" y="50" font-family="{SANS}" font-size="22" font-weight="700" fill="{INK}">hallucinated</text>
<text x="80" y="80" font-family="{MONO}" font-size="16" fill="{DIM}">AttributeError</text></g>
<g transform="translate(900 360)" filter="url(#shadow)">
<rect width="250" height="110" rx="18" fill="{PANEL2}" stroke="{GREEN}" stroke-width="2"/>
<circle cx="44" cy="55" r="22" fill="{GREEN}"/><path d="M33 56 l8 9 l15 -18" fill="none" stroke="{BG0}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
<text x="80" y="50" font-family="{SANS}" font-size="22" font-weight="700" fill="{INK}">verified</text>
<text x="80" y="80" font-family="{MONO}" font-size="16" fill="{DIM}">tests pass ✓</text></g>
<path d="M852 280 H895" stroke="{RED}" stroke-width="3" stroke-dasharray="4 6"/>
<path d="M852 400 H895" stroke="{GREEN}" stroke-width="3" stroke-dasharray="4 6"/>""")
    return frame("".join(body), "DELULU-FIM · CODE HALLUCINATION", MAGENTA, 5)


def synthetic():
    body = []
    # frontier model node
    body.append(f"""<g filter="url(#glow)"><circle cx="210" cy="330" r="92" fill="none" stroke="{VIOLET}" stroke-width="4"/></g>
<circle cx="210" cy="330" r="70" fill="{PANEL2}"/>
<path d="M210 288 l12 30 l30 12 l-30 12 l-12 30 l-12 -30 l-30 -12 l30 -12z" fill="{VIOLET}"/>
<text x="210" y="460" text-anchor="middle" font-family="{MONO}" font-size="20" fill="{INK}">frontier model</text>""")
    cards = [(GREEN, "gold", "json.load(f)"), (RED, "hard negative", "json.loads_file(f)"), (RED, "hard negative", "f.read_json()")]
    for i, (c, tag, code) in enumerate(cards):
        y = 160 + i * 130
        body.append(f'<path d="M305 330 C 360 330, 360 {y + 45}, 420 {y + 45}" fill="none" stroke="{c}" stroke-opacity="0.6" stroke-width="3"/>')
        body.append(f"""<g filter="url(#shadow)"><rect x="420" y="{y}" width="330" height="90" rx="16" fill="{PANEL}" stroke="{c}" stroke-width="2"/></g>
<text x="444" y="{y + 34}" font-family="{SANS}" font-size="17" font-weight="700" fill="{c}" letter-spacing="2">{tag.upper()}</text>
<text x="444" y="{y + 68}" font-family="{MONO}" font-size="21" fill="{INK}">{code}</text>""")
    body.append(f'<path d="M770 335 H840" stroke="{MAGENTA}" stroke-width="6" stroke-linecap="round" filter="url(#glow)"/><path d="M828 319 L848 335 L828 351" fill="none" stroke="{MAGENTA}" stroke-width="6" stroke-linecap="round"/>')
    # bar chart
    base = 560
    body.append(f'<path d="M880 {base} H1140" stroke="{DIM}" stroke-width="2"/>')
    body.append(f'<rect x="910" y="{base - 200}" width="80" height="200" rx="10" fill="#4b4f8a"/>')
    body.append(f'<rect x="1030" y="{base - 290}" width="80" height="290" rx="10" fill="{GREEN}" filter="url(#glow)"/>')
    body.append(f'<text x="950" y="{base + 34}" text-anchor="middle" font-family="{MONO}" font-size="18" fill="{DIM}">base</text>')
    body.append(f'<text x="1070" y="{base + 34}" text-anchor="middle" font-family="{MONO}" font-size="18" fill="{INK}">tuned</text>')
    body.append(f'<text x="1070" y="{base - 310}" text-anchor="middle" font-family="{SANS}" font-weight="800" font-size="46" fill="{GREEN}">+22%</text>')
    return frame("".join(body), "SYNTHETIC HARD NEGATIVES · FIM", GREEN, 6)


def bibtex():
    body = [window(110, 100, 620, 500, "references.bib")]
    rows = [
        (INK, "@inproceedings{smith2024,"),
        (INK, "  title  = {Deep Retrieval at Scale},"),
        (RED, "- author = {Smith, J. and Doe, A.},"),
        (GREEN, "+ author = {Smith, Jane and Lee, Kai},"),
        (RED, "- year   = {2023},"),
        (GREEN, "+ year   = {2024},"),
        (GREEN, "+ doi    = {10.1145/3626246},"),
        (INK, "}"),
    ]
    for i, (c, t) in enumerate(rows):
        y = 190 + i * 46
        if c in (RED, GREEN):
            body.append(f'<rect x="130" y="{y - 30}" width="580" height="40" rx="6" fill="{c}" fill-opacity="0.13"/>')
        body.append(f'<text x="150" y="{y}" font-family="{MONO}" font-size="21" fill="{c}" xml:space="preserve">{t.replace("&", "&amp;")}</text>')
    # magnifier
    body.append(f"""<g transform="translate(900 320)">
<circle r="120" fill="{CYAN}" fill-opacity="0.08" stroke="{CYAN}" stroke-width="12" filter="url(#glow)"/>
<path d="M85 85 L170 170" stroke="{CYAN}" stroke-width="26" stroke-linecap="round"/>
<path d="M-50 4 l34 36 l70 -80" fill="none" stroke="{GREEN}" stroke-width="18" stroke-linecap="round" stroke-linejoin="round"/>
</g>
<text x="900" y="560" text-anchor="middle" font-family="{MONO}" font-size="20" fill="{DIM}">CrossRef · Semantic Scholar</text>""")
    return frame("".join(body), "BIBTEX VERIFIER", CYAN, 7)


def glimpse():
    body = [f"""<g filter="url(#shadow)"><rect x="120" y="70" width="520" height="610" rx="10" fill="#f4f2fb"/></g>
<rect x="170" y="120" width="420" height="22" rx="4" fill="#2b2d52"/>
<rect x="230" y="155" width="300" height="12" rx="4" fill="#9a98b8"/>"""]
    rnd = random.Random(2)
    y = 200
    for i in range(16):
        w = rnd.randint(330, 420) if i % 5 != 4 else rnd.randint(160, 260)
        body.append(f'<rect x="170" y="{y}" width="{w}" height="10" rx="4" fill="#c9c6dd"/>')
        if i == 6:
            body.append(f'<rect x="{170 + w + 8}" y="{y - 8}" width="44" height="26" rx="6" fill="{MAGENTA}" fill-opacity="0.2" stroke="{MAGENTA}" stroke-width="2"/><text x="{170 + w + 30}" y="{y + 10}" text-anchor="middle" font-family="{MONO}" font-size="16" fill="{MAGENTA}">[12]</text>')
            cite = (170 + w + 52, y + 5)
        y += 28 if i % 5 != 4 else 44
    px, py = 700, 210
    body.append(f'<path d="M{cite[0]} {cite[1]} C {cite[0] + 60} {cite[1]}, {px - 60} {py + 60}, {px} {py + 60}" fill="none" stroke="{MAGENTA}" stroke-width="3" stroke-dasharray="3 8" stroke-linecap="round"/>')
    body.append(f"""<g filter="url(#shadow)"><rect x="{px}" y="{py}" width="420" height="330" rx="20" fill="{PANEL2}" stroke="{MAGENTA}" stroke-width="2"/></g>
<text x="{px + 28}" y="{py + 46}" font-family="{MONO}" font-size="17" fill="{MAGENTA}">[12] · arXiv</text>
<text x="{px + 28}" y="{py + 88}" font-family="{SANS}" font-size="25" font-weight="700" fill="{INK}">Attention Is All</text>
<text x="{px + 28}" y="{py + 120}" font-family="{SANS}" font-size="25" font-weight="700" fill="{INK}">You Need</text>
<text x="{px + 28}" y="{py + 154}" font-family="{SANS}" font-size="17" fill="{DIM}">Vaswani et al. · 2017</text>""")
    for i in range(5):
        body.append(f'<rect x="{px + 28}" y="{py + 182 + i * 24}" width="{[360, 340, 365, 300, 210][i]}" height="10" rx="4" fill="#4b4f8a"/>')
    return frame("".join(body), "GLIMPSE · CITATION PEEK", VIOLET, 8)


def fairem():
    def table(x, y, color, rows):
        out = [f'<g filter="url(#shadow)"><rect x="{x}" y="{y}" width="300" height="{60 + rows * 52}" rx="16" fill="{PANEL}" stroke="{color}" stroke-opacity="0.7" stroke-width="2"/></g>',
               f'<rect x="{x}" y="{y}" width="300" height="48" rx="16" fill="{color}" fill-opacity="0.25"/>']
        for r in range(rows):
            out.append(f'<rect x="{x + 22}" y="{y + 70 + r * 52}" width="{150 + (r * 37) % 90}" height="16" rx="6" fill="#4b4f8a"/>')
            out.append(f'<circle cx="{x + 270}" cy="{y + 78 + r * 52}" r="9" fill="{[VIOLET, AMBER][r % 2]}"/>')
        return "".join(out)
    body = [table(90, 150, CYAN, 6), table(810, 150, CYAN, 6)]
    for a, b, ok in [(0, 1, True), (1, 0, True), (2, 3, False), (3, 2, True), (4, 5, False), (5, 4, True)]:
        y1, y2 = 228 + a * 52, 228 + b * 52
        c = GREEN if ok else RED
        body.append(f'<path d="M390 {y1} C 600 {y1}, 600 {y2}, 810 {y2}" fill="none" stroke="{c}" stroke-width="3" stroke-opacity="0.75"/>')
    body.append(f"""<g transform="translate(600 140)">
<path d="M0 0 V120" stroke="{AMBER}" stroke-width="6"/><path d="M-110 0 H110" stroke="{AMBER}" stroke-width="6" stroke-linecap="round"/>
<path d="M-110 0 L-150 70 H-70 Z M110 0 L70 70 H150 Z" fill="none" stroke="{AMBER}" stroke-width="4" stroke-linejoin="round"/>
<path d="M-150 70 a40 14 0 0 0 80 0 M70 70 a40 14 0 0 0 80 0" fill="{AMBER}" fill-opacity="0.3" stroke="{AMBER}" stroke-width="4"/>
<circle cx="0" cy="-8" r="10" fill="{AMBER}"/></g>""")
    return frame("".join(body), "FAIREM360 · RESPONSIBLE MATCHING", CYAN, 9)


def coverage():
    rnd = random.Random(21)
    body = [f'<rect x="120" y="100" width="620" height="520" rx="20" fill="{PANEL}" stroke="#ffffff" stroke-opacity="0.12"/>']
    holes = [(560, 230, 70), (300, 500, 60)]
    for _ in range(260):
        x, y = rnd.uniform(140, 720), rnd.uniform(120, 600)
        if any((x - hx) ** 2 + (y - hy) ** 2 < (hr + 10) ** 2 for hx, hy, hr in holes):
            continue
        body.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="5" fill="{rnd.choice([VIOLET, CYAN])}" opacity="0.75"/>')
    for hx, hy, hr in holes:
        body.append(f'<circle cx="{hx}" cy="{hy}" r="{hr}" fill="{RED}" fill-opacity="0.12" stroke="{RED}" stroke-width="3" stroke-dasharray="8 7"/>')
        body.append(f'<text x="{hx}" y="{hy + 8}" text-anchor="middle" font-family="{MONO}" font-size="22" fill="{RED}">gap</text>')
    body.append(f"""<g font-family="{SANS}" fill="{INK}">
<text x="820" y="240" font-size="40" font-weight="700">coverage</text>
<text x="820" y="290" font-size="24" fill="{DIM}">find under-represented</text>
<text x="820" y="322" font-size="24" fill="{DIM}">regions, then fill them</text></g>
<g transform="translate(820 380)">""" +
        "".join(f'<rect x="{i * 56}" y="{150 - h}" width="40" height="{h}" rx="8" fill="{c}"/>' for i, (h, c) in enumerate([(140, VIOLET), (120, CYAN), (36, RED), (130, VIOLET), (24, RED)])) +
        "</g>")
    return frame("".join(body), "COVERAGE · TRUSTWORTHY AI", RED, 10)


def graphmine():
    rnd = random.Random(31)
    nodes = [(rnd.uniform(130, 1070), rnd.uniform(110, 600)) for _ in range(34)]
    motif = [(560, 300), (700, 250), (680, 410), (820, 360)]
    nodes += motif
    edges = set()
    for i, (x, y) in enumerate(nodes):
        d = sorted(range(len(nodes)), key=lambda j: (nodes[j][0] - x) ** 2 + (nodes[j][1] - y) ** 2)
        for j in d[1:4]:
            edges.add(tuple(sorted((i, j))))
    body = []
    for i, j in edges:
        body.append(f'<path d="M{nodes[i][0]:.0f} {nodes[i][1]:.0f} L{nodes[j][0]:.0f} {nodes[j][1]:.0f}" stroke="{VIOLET}" stroke-opacity="0.35" stroke-width="2"/>')
    m0 = len(nodes) - 4
    for a, b in [(0, 1), (1, 2), (0, 2), (1, 3), (2, 3)]:
        body.append(f'<path d="M{motif[a][0]} {motif[a][1]} L{motif[b][0]} {motif[b][1]}" stroke="{AMBER}" stroke-width="6" filter="url(#glow)"/>')
    for k, (x, y) in enumerate(nodes):
        hot = k >= m0
        body.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{16 if hot else 10}" fill="{AMBER if hot else PANEL2}" stroke="{AMBER if hot else CYAN}" stroke-width="3"/>')
    return frame("".join(body), "GRAPH PATTERN MINING", AMBER, 11)


def multimodal():
    cx, cy = 600, 360
    body = [f"""<circle cx="{cx}" cy="{cy}" r="250" fill="none" stroke="{VIOLET}" stroke-opacity="0.35" stroke-width="2" stroke-dasharray="4 10"/>
<circle cx="{cx}" cy="{cy}" r="170" fill="none" stroke="{CYAN}" stroke-opacity="0.25" stroke-width="2"/>
<g filter="url(#shadow)">
<path d="M{cx - 90} {cy - 60} v120 a90 26 0 0 0 180 0 v-120" fill="{PANEL2}" stroke="{MAGENTA}" stroke-width="3"/>
<ellipse cx="{cx}" cy="{cy - 60}" rx="90" ry="26" fill="#2f2f72" stroke="{MAGENTA}" stroke-width="3"/>
<path d="M{cx - 90} {cy} a90 26 0 0 0 180 0" fill="none" stroke="{MAGENTA}" stroke-width="2" opacity="0.6"/></g>
<path d="M{cx} {cy - 10} l10 24 l24 10 l-24 10 l-10 24 l-10 -24 l-24 -10 l24 -10z" fill="{AMBER}" filter="url(#glow)"/>"""]
    rnd = random.Random(4)
    sats = {
        "image": (cx - 250, cy - 40),
        "text": (cx + 230, cy - 120),
        "audio": (cx + 200, cy + 170),
        "table": (cx - 160, cy + 200),
        "video": (cx - 80, cy - 260),
    }
    for name, (x, y) in sats.items():
        body.append(f'<path d="M{cx} {cy} L{x} {y}" stroke="{CYAN}" stroke-opacity="0.35" stroke-width="2"/>')
        body.append(f'<g filter="url(#shadow)"><rect x="{x - 62}" y="{y - 46}" width="124" height="92" rx="18" fill="{PANEL}" stroke="{CYAN}" stroke-opacity="0.7" stroke-width="2"/></g>')
        if name == "image":
            body.append(photo_tile(x - 44, y - 30, 88, 60, 1, rnd))
        elif name == "text":
            body.extend(f'<rect x="{x - 44}" y="{y - 26 + i * 16}" width="{[88, 70, 82, 50][i]}" height="8" rx="4" fill="{INK}" opacity="0.7"/>' for i in range(4))
        elif name == "audio":
            body.append("".join(f'<rect x="{x - 46 + i * 9}" y="{y - h / 2}" width="5" height="{h}" rx="2.5" fill="{GREEN}"/>' for i, h in enumerate([10, 24, 40, 18, 52, 30, 14, 44, 26, 12, 8])))
        elif name == "table":
            body.extend(f'<rect x="{x - 44 + c * 30}" y="{y - 28 + r * 20}" width="26" height="16" rx="3" fill="{AMBER}" opacity="{0.4 + 0.2 * ((r + c) % 3)}"/>' for r in range(3) for c in range(3))
        elif name == "video":
            body.append(f'<rect x="{x - 44}" y="{y - 30}" width="88" height="60" rx="8" fill="{VIOLET}" opacity="0.5"/><path d="M{x - 12} {y - 16} L{x + 18} {y} L{x - 12} {y + 16}Z" fill="{INK}"/>')
    return frame("".join(body), "GENAI × MULTIMODAL DATA", MAGENTA, 12)


def taskaware():
    body = []
    groups = [(VIOLET, 300), (CYAN, 260), (AMBER, 90), (MAGENTA, 60)]
    base = 560
    for i, (c, h) in enumerate(groups):
        x = 140 + i * 120
        body.append(f'<rect x="{x}" y="{base - h}" width="80" height="{h}" rx="10" fill="{c}"/>')
    body.append(f'<path d="M120 {base} H600" stroke="{DIM}" stroke-width="2"/><text x="360" y="{base + 46}" text-anchor="middle" font-family="{MONO}" font-size="20" fill="{DIM}">before</text>')
    body.append(f'<path d="M640 360 H730" stroke="{MAGENTA}" stroke-width="6" stroke-linecap="round" filter="url(#glow)"/><path d="M718 344 L738 360 L718 376" fill="none" stroke="{MAGENTA}" stroke-width="6" stroke-linecap="round"/>')
    for i, (c, h) in enumerate(groups):
        x = 780 + i * 100
        body.append(f'<rect x="{x}" y="{base - h}" width="70" height="{h}" rx="10" fill="{c}"/>')
        if h < 250:
            add = 250 - h
            body.append(f'<rect x="{x}" y="{base - h - add}" width="70" height="{add}" rx="10" fill="{c}" fill-opacity="0.25" stroke="{c}" stroke-width="3" stroke-dasharray="7 6"/>')
            body.append(f'<path d="M{x + 35} {base - 270} l6 -14 l6 14 l14 6 l-14 6 l-6 14 l-6 -14 l-14 -6z" fill="#fff" filter="url(#glow)"/>')
    body.append(f'<path d="M760 {base} H1180" stroke="{DIM}" stroke-width="2"/><text x="975" y="{base + 46}" text-anchor="middle" font-family="{MONO}" font-size="20" fill="{DIM}">after (worst-group ↑)</text>')
    return frame("".join(body), "TASK-AWARE AUGMENTATION", VIOLET, 13)


ART = {
    "projects/needle": needle,
    "projects/needledb": needledb,
    "projects/rsr": rsr,
    "projects/chameleon": chameleon,
    "projects/delulu": delulu,
    "projects/synthetic_hallucinations": synthetic,
    "projects/bibtex_verifier": bibtex,
    "projects/glimpse": glimpse,
    "projects/fairem360": fairem,
    "projects/coverage": coverage,
    "projects/graph_mining": graphmine,
    "projects/multimodal": multimodal,
    "projects/task_aware": taskaware,
}


def main():
    out_dir = ROOT / "assets" / "img"
    for name, fn in ART.items():
        svg = out_dir / f"{name}.svg"
        png = out_dir / f"{name}.png"
        svg.parent.mkdir(parents=True, exist_ok=True)
        svg.write_text(fn())
        subprocess.run(["magick", "-background", "none", f"RSVG:{svg}", "-strip", "-quality", "92", str(png)], check=True)
        svg.unlink()
        print("wrote", png.relative_to(ROOT))


if __name__ == "__main__":
    main()
