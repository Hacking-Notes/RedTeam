#!/usr/bin/env python3
"""Generalized Hacking-Notes README art generator.

Rebuilds assets/header.svg, assets/divider.svg and assets/footer.svg for any
repo from the CONFIG below, matching the Hacker-Roadmap house style. SVGs use
only inline CSS animations (GitHub sandboxes scripts / external fonts).
"""
import random
from pathlib import Path
from xml.sax.saxutils import escape

MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
BG = "#ffffff"; PANEL = "#ffffff"; LINE = "#d0d7de"; TEXT = "#1f2328"; MUTED = "#59636e"
CYAN = "#0891b2"; PURPLE = "#7c3aed"; BAR = "#f6f8fa"
REDUCED = "@media (prefers-reduced-motion: reduce){*{animation:none!important}}"


def header(title, subtitle, pill, tags, accent):
    W, H = 1200, 420
    rnd = random.Random(1337)
    rain = []
    for i in range(34):
        x = 18 + i * 35 + rnd.randint(-6, 6)
        chars = "".join(rnd.choice("01") for _ in range(22))
        dur = rnd.uniform(7, 15); delay = -rnd.uniform(0, dur)
        tsp = "".join(f'<tspan x="{x}" dy="19">{c}</tspan>' for c in chars)
        rain.append(f'<text class="rain" style="animation-duration:{dur:.1f}s;animation-delay:{delay:.1f}s" '
                    f'opacity="{rnd.uniform(0.06, 0.18):.2f}">{tsp}</text>')
    T = title.upper()
    tsize = min(92, int(1080 / max(1, len(T) * 0.70)))
    sub_size = 22
    sub_w = len(subtitle) * sub_size * 0.6
    sub_x = (W - sub_w) / 2
    n = len(subtitle)
    dots = []
    total = len(tags); gap = min(230, 900 / max(1, total))
    start = W / 2 - gap * (total - 1) / 2
    for i, t in enumerate(tags):
        cx = start + i * gap
        lbl = escape(t.upper())
        lw = len(lbl) * 7.3
        dots.append(
            f'<g class="dot" style="animation-delay:{i * 0.35:.2f}s">'
            f'<circle cx="{cx - lw/2 - 12:.0f}" cy="352" r="5" fill="{accent}"/>'
            f'<text x="{cx - lw/2:.0f}" y="357" font-family="{MONO}" font-size="13" fill="{MUTED}" '
            f'letter-spacing="1">{lbl}</text></g>')
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{escape(title)}">
<title>{escape(title)}</title>
<defs>
  <linearGradient id="title" x1="0" x2="1" y1="0" y2="0">
    <stop offset="0" stop-color="{accent}"/><stop offset="0.5" stop-color="{CYAN}"/><stop offset="1" stop-color="{PURPLE}"/>
  </linearGradient>
  <radialGradient id="glow" cx="0.5" cy="0.45" r="0.6">
    <stop offset="0" stop-color="{accent}" stop-opacity="0.10"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="scan" x1="0" x2="0" y1="0" y2="1">
    <stop offset="0" stop-color="{accent}" stop-opacity="0"/><stop offset="0.5" stop-color="{accent}" stop-opacity="0.10"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/>
  </linearGradient>
  <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
    <path d="M40 0 H0 V40" fill="none" stroke="{accent}" stroke-opacity="0.10" stroke-width="1"/>
    <animateTransform attributeName="patternTransform" type="translate" from="0 0" to="0 40" dur="4s" repeatCount="indefinite"/>
  </pattern>
  <linearGradient id="fade" x1="0" x2="0" y1="0" y2="1">
    <stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="0.35" stop-color="#fff" stop-opacity="1"/>
    <stop offset="0.8" stop-color="#fff" stop-opacity="1"/><stop offset="1" stop-color="#fff" stop-opacity="0"/>
  </linearGradient>
  <mask id="fademask"><rect width="{W}" height="{H}" fill="url(#fade)"/></mask>
  <clipPath id="frame"><rect width="{W}" height="{H}" rx="18"/></clipPath>
  <clipPath id="type"><rect class="typer" x="{sub_x:.1f}" y="225" width="{sub_w:.1f}" height="40"/></clipPath>
</defs>
<style>
  .rain{{font-family:{MONO};font-size:15px;fill:{accent};animation:fall linear infinite}}
  @keyframes fall{{from{{transform:translateY(-440px)}}to{{transform:translateY(440px)}}}}
  .scan{{animation:scan 6s linear infinite}}
  @keyframes scan{{from{{transform:translateY(-140px)}}to{{transform:translateY({H}px)}}}}
  .typer{{transform-box:fill-box;transform-origin:left;animation:type 9s steps({n},end) infinite}}
  @keyframes type{{0%{{transform:scaleX(0)}}45%,90%{{transform:scaleX(1)}}100%{{transform:scaleX(0)}}}}
  .cursor{{animation:cur 9s steps({n},end) infinite,blink 1s step-end infinite}}
  @keyframes cur{{0%{{transform:translateX(0)}}45%,90%{{transform:translateX({sub_w:.1f}px)}}100%{{transform:translateX(0)}}}}
  @keyframes blink{{50%{{opacity:0}}}}
  .g1{{animation:g1 5s infinite}} .g2{{animation:g2 5s infinite}}
  @keyframes g1{{0%,88%,100%{{transform:translate(0,0);opacity:0}}90%{{transform:translate(-5px,2px);opacity:.8}}93%{{transform:translate(4px,-2px);opacity:.8}}96%{{transform:translate(-2px,0);opacity:.6}}}}
  @keyframes g2{{0%,88%,100%{{transform:translate(0,0);opacity:0}}90%{{transform:translate(5px,-2px);opacity:.8}}93%{{transform:translate(-4px,2px);opacity:.8}}96%{{transform:translate(2px,0);opacity:.6}}}}
  .dot{{animation:pulse 2.4s ease-in-out infinite}}
  @keyframes pulse{{0%,100%{{opacity:.55}}50%{{opacity:1}}}}
  .badge{{animation:pulse 3s ease-in-out infinite}}
  {REDUCED}
</style>
<g clip-path="url(#frame)">
  <rect width="{W}" height="{H}" fill="{BG}"/>
  <rect width="{W}" height="{H}" fill="url(#grid)" mask="url(#fademask)"/>
  <g mask="url(#fademask)">{''.join(rain)}</g>
  <rect width="{W}" height="{H}" fill="url(#glow)"/>
  <rect class="scan" width="{W}" height="140" fill="url(#scan)"/>
  <g class="badge">
    <rect x="{W/2 - 150}" y="58" width="300" height="30" rx="15" fill="{accent}" fill-opacity="0.08" stroke="{accent}" stroke-opacity="0.45"/>
    <text x="{W/2}" y="78" text-anchor="middle" font-family="{MONO}" font-size="13" letter-spacing="3" fill="{accent}">[ {escape(pill.upper())} ]</text>
  </g>
  <g font-family="{SANS}" font-size="{tsize}" font-weight="800" text-anchor="middle" letter-spacing="4">
    <text class="g1" x="{W/2}" y="195" fill="#db2777">{escape(T)}</text>
    <text class="g2" x="{W/2}" y="195" fill="{CYAN}">{escape(T)}</text>
    <text x="{W/2}" y="195" fill="url(#title)">{escape(T)}</text>
  </g>
  <g clip-path="url(#type)">
    <text x="{sub_x:.1f}" y="254" font-family="{MONO}" font-size="{sub_size}" fill="{TEXT}" xml:space="preserve">{escape(subtitle)}</text>
  </g>
  <rect class="cursor" x="{sub_x + 2:.1f}" y="234" width="12" height="26" fill="{accent}"/>
  <path d="M{W/2 - 420} 310 H{W/2 + 420}" stroke="{LINE}" stroke-width="1"/>
  {''.join(dots)}
  <rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="18" fill="none" stroke="{accent}" stroke-opacity="0.25"/>
</g>
</svg>"""


def divider(accent):
    W, H = 1200, 24
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="divider">
<defs>
  <linearGradient id="p" x1="0" x2="1"><stop offset="0" stop-color="{accent}" stop-opacity="0"/><stop offset="0.5" stop-color="{CYAN}"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/></linearGradient>
</defs>
<style>
  .pulse{{animation:move 4s ease-in-out infinite}}
  @keyframes move{{0%{{transform:translateX(-240px)}}100%{{transform:translateX({W}px)}}}}
  {REDUCED}
</style>
<path d="M0 12 H{W}" stroke="{LINE}" stroke-width="2"/>
<rect class="pulse" x="0" y="10" width="240" height="4" rx="2" fill="url(#p)"/>
<g fill="{accent}"><rect x="{W/2 - 4}" y="8" width="8" height="8" transform="rotate(45 {W/2} 12)"/></g>
</svg>"""


def footer(name, msg, accent):
    W, H = 1200, 170
    size = 18
    w = len(msg) * size * 0.6
    x = (W - w - 24) / 2 + 24
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Happy hacking">
<title>Happy hacking</title>
<defs>
  <linearGradient id="t" x1="0" x2="1"><stop offset="0" stop-color="{accent}"/><stop offset="1" stop-color="{CYAN}"/></linearGradient>
  <clipPath id="type"><rect class="typer" x="{x:.0f}" y="60" width="{w:.0f}" height="30"/></clipPath>
</defs>
<style>
  .typer{{transform-box:fill-box;transform-origin:left;animation:type 8s steps({len(msg)},end) infinite}}
  @keyframes type{{0%{{transform:scaleX(0)}}45%,90%{{transform:scaleX(1)}}100%{{transform:scaleX(0)}}}}
  .cursor{{animation:cur 8s steps({len(msg)},end) infinite,blink 1s step-end infinite}}
  @keyframes cur{{0%{{transform:translateX(0)}}45%,90%{{transform:translateX({w:.0f}px)}}100%{{transform:translateX(0)}}}}
  @keyframes blink{{50%{{opacity:0}}}}
  {REDUCED}
</style>
<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16" fill="{BG}" stroke="{accent}" stroke-opacity="0.25"/>
<text x="{x - 24:.0f}" y="82" font-family="{MONO}" font-size="{size}" fill="{accent}">$</text>
<g clip-path="url(#type)"><text x="{x:.0f}" y="82" font-family="{MONO}" font-size="{size}" fill="{TEXT}" xml:space="preserve">{escape(msg)}</text></g>
<rect class="cursor" x="{x + 2:.0f}" y="66" width="10" height="22" fill="{accent}"/>
<text x="{W/2}" y="128" text-anchor="middle" font-family="{SANS}" font-size="15" fill="{MUTED}">{escape(name)} · by <tspan fill="url(#t)" font-weight="700">Hacking-Notes</tspan></text>
</svg>"""


def card(title, tag, pill, accent, num="//"):
    """A repo preview card in the house style."""
    W, H = 560, 200
    c = accent
    def rpath(x, y, w, h, r):
        return (f"M{x+r} {y} H{x+w-r} A{r} {r} 0 0 1 {x+w} {y+r} V{y+h-r} "
                f"A{r} {r} 0 0 1 {x+w-r} {y+h} H{x+r} A{r} {r} 0 0 1 {x} {y+h-r} "
                f"V{y+r} A{r} {r} 0 0 1 {x+r} {y} Z")
    border = rpath(1.5, 1.5, W-3, H-3, 16)
    tag = (tag[:60])
    pill_w = len(pill) * 7.8 + 26
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{escape(title)}">
<title>{escape(title)}</title>
<defs>
  <radialGradient id="g" cx="0.12" cy="0.15" r="0.9">
    <stop offset="0" stop-color="{c}" stop-opacity="0.16"/><stop offset="1" stop-color="{c}" stop-opacity="0"/>
  </radialGradient>
  <pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.2" fill="{c}" fill-opacity="0.16"/></pattern>
</defs>
<style>
  .sweep{{stroke-dasharray:22 98;animation:sw 5s linear infinite}}
  @keyframes sw{{to{{stroke-dashoffset:-120}}}}
  .blink{{animation:bl 1.4s step-end infinite}} @keyframes bl{{50%{{opacity:.25}}}}
  {REDUCED}
</style>
<rect x="1.5" y="1.5" width="{W-3}" height="{H-3}" rx="16" fill="{PANEL}"/>
<rect x="1.5" y="1.5" width="{W-3}" height="{H-3}" rx="16" fill="url(#g)"/>
<rect x="{W-150}" y="1.5" width="148" height="{H-3}" fill="url(#dots)"/>
<path d="{border}" fill="none" stroke="{c}" stroke-opacity="0.22" stroke-width="1.5"/>
<path class="sweep" d="{border}" pathLength="120" fill="none" stroke="{c}" stroke-width="2.5" stroke-linecap="round"/>
<circle cx="34" cy="34" r="5" fill="#ff5f57"/><circle cx="52" cy="34" r="5" fill="#febc2e"/><circle cx="70" cy="34" r="5" fill="#28c840"/>
<text x="{W-28}" y="40" text-anchor="end" font-family="{MONO}" font-size="22" font-weight="700" fill="{c}" fill-opacity="0.5">{escape(num)}</text>
<text x="34" y="92" font-family="{SANS}" font-size="28" font-weight="800" fill="{TEXT}">{escape(title)}</text>
<text x="34" y="122" font-family="{SANS}" font-size="15.5" fill="{MUTED}">{escape(tag)}</text>
<rect x="34" y="{H-50}" width="{pill_w:.0f}" height="27" rx="13" fill="{c}" fill-opacity="0.12" stroke="{c}" stroke-opacity="0.5"/>
<text x="{34 + pill_w/2:.0f}" y="{H-31}" text-anchor="middle" font-family="{MONO}" font-size="12" font-weight="700" letter-spacing="1" fill="{c}">{escape(pill)}</text>
<text x="{34 + pill_w + 16:.0f}" y="{H-31}" font-family="{MONO}" font-size="13" fill="{MUTED}">cd ~/{escape(title.lower().replace(' ','-'))} <tspan class="blink" fill="{c}">_</tspan></text>
</svg>"""


def build(target_dir, cfg):
    a = Path(target_dir) / "assets"
    a.mkdir(parents=True, exist_ok=True)
    (a / "header.svg").write_text(header(cfg["title"], cfg["subtitle"], cfg["pill"], cfg["tags"], cfg["accent"]).strip() + "\n", encoding="utf-8")
    (a / "divider.svg").write_text(divider(cfg["accent"]).strip() + "\n", encoding="utf-8")
    (a / "footer.svg").write_text(footer(cfg["name"], cfg["footer"], cfg["accent"]).strip() + "\n", encoding="utf-8")
    print("assets ->", target_dir)
