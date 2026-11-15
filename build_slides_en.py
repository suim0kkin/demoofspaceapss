import base64
from pathlib import Path

OUT = Path(__file__).parent / "en"
OUT.mkdir(exist_ok=True)
IMG_PATH = Path("/Users/wataraiharuki/.gemini/antigravity/brain/777f0328-c1e2-419d-beab-fff0253881ce/.user_uploaded/media_1794723865777_6017e08b.jpg")
IMG_B64 = base64.b64encode(IMG_PATH.read_bytes()).decode("ascii")
IMG_URI = f"data:image/jpeg;base64,{IMG_B64}"

FONT = "'Inter','Helvetica Neue',Arial,'Hiragino Sans','Noto Sans JP',sans-serif"
INK, SUB, LINE, BG, CARD = "#1C1E21", "#65676B", "#DADDE1", "#F5F6F7", "#FFFFFF"
BLUE, ORANGE, GREEN, PURPLE, TEAL = "#0866FF", "#F5533D", "#31A24C", "#7B5CFA", "#0D9AA8"
TOTAL = 7

LOGO_BODY = """
<g fill="currentColor" fill-rule="evenodd">
 <g transform="translate(40,20)"><path d="M22,18 L37,18 L16,96 L1,96 Z"/><path d="M45,18 L60,18 L81,96 L66,96 Z"/><path d="M68,4 H94 V30 H68 Z M76,12 V22 H86 V12 Z"/></g>
 <g transform="translate(144,20)"><path d="M52,8 L72,8 L22,58 L2,58 Z"/><path d="M36,32 H50 V98 H36 Z"/></g>
 <g transform="translate(236,20)"><path d="M4,12 H72 V94 H4 Z M18,26 V80 H58 V26 Z"/></g>
 <g transform="translate(328,20)"><path d="M4,12 H70 V94 H4 V80 H56 V26 H4 Z"/></g>
 <g transform="translate(418,20)"><path d="M22,18 L37,18 L16,96 L1,96 Z"/><path d="M45,18 L60,18 L81,96 L66,96 Z"/><path d="M68,4 H94 V30 H68 Z M76,12 V22 H86 V12 Z"/></g>
 <g transform="translate(522,20)"><path d="M52,8 L72,8 L22,58 L2,58 Z"/><path d="M36,32 H50 V98 H36 Z"/></g>
 <g transform="translate(614,20)"><path d="M4,12 H72 V94 H4 Z M18,26 V80 H58 V26 Z"/></g>
 <g transform="translate(702,20)"><path d="M6,40 H17 V58 H6 Z"/><path d="M23,40 H34 V58 H23 Z"/><path d="M42,40 L56,40 L28,96 L14,96 Z"/></g>
 <g transform="translate(770,20)"><path d="M16,8 H30 V98 H16 Z"/><path d="M30,38 L64,58 L64,74 L30,54 Z"/></g>
</g>"""

def logo(x, y, scale, color=INK):
    return f'<g transform="translate({x},{y}) scale({scale})" style="color:{color}">{LOGO_BODY}</g>'

def page(n, title, body, defs=""):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" width="1280" height="720" font-family="{FONT}">
{defs}
<rect width="1280" height="720" fill="{BG}"/>
<rect x="0" y="0" width="1280" height="64" fill="{CARD}"/><line x1="0" y1="64" x2="1280" y2="64" stroke="{LINE}"/>
{logo(48, 20, 0.2)}
<text x="1232" y="39" text-anchor="end" font-size="14" fill="{SUB}">{n:02d} / {TOTAL:02d}</text>
<text x="64" y="124" font-size="34" font-weight="700" fill="{INK}">{title}</text>
{body}
</svg>"""

def card(x, y, w, h, fill=CARD):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{fill}" stroke="{LINE}"/>'

def chip(x, y, text, color=BLUE, w=None):
    w = w or (len(text) * 8.5 + 30)
    return (f'<rect x="{x}" y="{y}" width="{w}" height="30" rx="15" fill="{color}" fill-opacity="0.1"/>'
            f'<text x="{x + w/2}" y="{y+20}" text-anchor="middle" font-size="13" font-weight="600" fill="{color}">{text}</text>')

def badge(x, y, num, color=BLUE):
    return (f'<circle cx="{x}" cy="{y}" r="14" fill="{color}"/>'
            f'<text x="{x}" y="{y+5}" text-anchor="middle" font-size="14" font-weight="700" fill="#fff">{num}</text>')

# ---------- 1: cover ----------
s1 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" width="1280" height="720" font-family="{FONT}">
<defs><radialGradient id="glow" cx="50%" cy="38%" r="60%"><stop offset="0" stop-color="{ORANGE}" stop-opacity="0.14"/><stop offset="1" stop-color="{ORANGE}" stop-opacity="0"/></radialGradient>
<linearGradient id="bar" x1="0" x2="1"><stop offset="0" stop-color="{ORANGE}"/><stop offset="1" stop-color="{BLUE}"/></linearGradient></defs>
<rect width="1280" height="720" fill="{BG}"/><rect width="1280" height="720" fill="url(#glow)"/>
<g fill="none" stroke="{LINE}" stroke-width="1.2"><circle cx="640" cy="640" r="260"/><circle cx="640" cy="640" r="380"/><circle cx="640" cy="640" r="500"/></g>
{logo(200, 190, 1.0)}
<rect x="560" y="352" width="160" height="5" rx="2.5" fill="url(#bar)"/>
<text x="640" y="418" text-anchor="middle" font-size="44" font-weight="700" fill="{INK}" letter-spacing="1">PyroCopilot</text>
<text x="640" y="466" text-anchor="middle" font-size="22" fill="{SUB}">3D Earth Thermal &amp; Swidden Intelligence with Multi-Perspective LLM Reasoning</text>
{chip(376, 520, "NASA FIRMS", ORANGE, 126)}{chip(514, 520, "NASA POWER", BLUE, 134)}{chip(660, 520, "Gemini Copilot", PURPLE, 146)}{chip(818, 520, "7-Day Risk", GREEN, 110)}
<text x="640" y="650" text-anchor="middle" font-size="14" fill="{SUB}">NASA Space Apps Challenge  ·  Project Overview (7 Slides)</text>
</svg>"""

# ---------- 2: contents ----------
items = [
    ("01", "Project Overview", "Observe → Model → Explain pipeline and key metrics", ORANGE),
    ("02", "Multi-Perspective LLM Reasoning", "Synthesizing 5 analytical lenses into grounded answers &amp; UI actions", PURPLE),
    ("03", "Live Demo: UI &amp; 4 Core Modules", "AI Chat, 3D Terrain Globe, Forecast Workspace &amp; Timeline Slider", BLUE),
    ("04", "Live Demo: LLM-Orchestrated Workflow", "From natural-language queries to globe focus &amp; weather drivers", TEAL),
    ("05", "Impact, Tech Stack &amp; Design Factors", "Expected impact, architecture stack, and key limitations", GREEN),
]
rows = ""
for i, (num, t, d, c) in enumerate(items):
    y = 160 + i * 102
    rows += (card(64, y, 1152, 84) +
             f'<rect x="64" y="{y}" width="8" height="84" rx="4" fill="{c}"/>'
             f'<text x="108" y="{y+53}" font-size="34" font-weight="700" fill="{c}">{num}</text>'
             f'<text x="196" y="{y+39}" font-size="23" font-weight="700" fill="{INK}">{t}</text>'
             f'<text x="196" y="{y+65}" font-size="15" fill="{SUB}">{d}</text>'
             f'<text x="1168" y="{y+52}" text-anchor="end" font-size="24" fill="{LINE}">›</text>')
s2 = page(2, "Table of Contents", rows)

# ---------- 3: overview ----------
steps = [("Observe", "Collect satellite &amp; weather", ORANGE, ["FIRMS VIIRS (NOAA-20/21)", "MODIS &amp; VIIRS historical archive", "NASA POWER city weather"]),
         ("Model", "Predict with ML models", BLUE, ["Detect: vegetation vs static heat", "FRP harmonization: XGBoost Tweedie", "7-day risk forecast (LightGBM)"]),
         ("Explain", "Reason &amp; control via LLM", PURPLE, ["Gemini Copilot (BYOK)", "Natural language (EN / JA)", "Auto-zoom globe &amp; filter UI"])]
cols = ""
for i, (en, sub_t, c, lines) in enumerate(steps):
    x = 64 + i * 400
    cols += card(x, 166, 352, 300)
    cols += f'<circle cx="{x+44}" cy="218" r="22" fill="{c}"/><text x="{x+44}" y="225" text-anchor="middle" font-size="20" font-weight="700" fill="#fff">{i+1}</text>'
    cols += f'<text x="{x+80}" y="214" font-size="24" font-weight="700" fill="{INK}">{en}</text><text x="{x+80}" y="240" font-size="14" fill="{SUB}">{sub_t}</text>'
    for j, l in enumerate(lines):
        cols += f'<circle cx="{x+32}" cy="{296+j*52}" r="4" fill="{c}"/><text x="{x+48}" y="{301+j*52}" font-size="15" fill="{INK}">{l}</text>'
    if i < 2:
        cols += f'<path d="M{x+362} 316 h28 m-8 -8 l8 8 l-8 8" fill="none" stroke="{SUB}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>'
kpis = [("3", "Fire Source Classes", "Wildfire / Swidden / Industrial"), ("2", "Harmonized Sensors", "MODIS + VIIRS"), ("7d", "Forecast Horizon", "Fire probability within 50 km"), ("Static", "Serverless Hosting", "GitHub Pages + BYOK")]
for i, (v, l, s) in enumerate(kpis):
    x = 64 + i * 292
    cols += card(x, 500, 268, 160) + f'<text x="{x+24}" y="564" font-size="40" font-weight="700" fill="{BLUE}">{v}</text><text x="{x+24}" y="601" font-size="17" font-weight="600" fill="{INK}">{l}</text><text x="{x+24}" y="628" font-size="14" fill="{SUB}">{s}</text>'
s3 = page(3, "Project Overview  —  Observe → Model → Explain", cols)

# ---------- 4: LLM multi-perspective ----------
lenses = [("Source Classification", "Distinguish swidden, wildfire &amp;\nindustrial via spatial persistence", ORANGE, (64, 156)),
          ("Weather Context", "30-day temperature &amp; rainfall\nfrom NASA POWER features", BLUE, (64, 326)),
          ("Sensor Reliability", "Account for MODIS/VIIRS gap\n&amp; FRP harmonization stats", TEAL, (64, 496)),
          ("Regional Context", "Hotspot gazetteer (Amazon,\nBorneo) + EN/JA aliases", PURPLE, (884, 156)),
          ("Temporal Dynamics", "Weekly timeseries &amp;\n7-day risk trajectory", GREEN, (884, 326))]
body = ""
cx, cy = 640, 336
for t, d, c, (x, y) in lenses:
    ax = x + 332 if x < 600 else x
    body += f'<path d="M{ax} {y+66} C {ax + (60 if x<600 else -60)} {y+66}, {cx + (-120 if x<600 else 120)} {cy}, {cx + (-92 if x<600 else 92)} {cy}" fill="none" stroke="{c}" stroke-width="2" stroke-dasharray="5 5"/>'
for t, d, c, (x, y) in lenses:
    body += card(x, y, 332, 132) + f'<rect x="{x}" y="{y}" width="6" height="132" rx="3" fill="{c}"/>'
    body += f'<text x="{x+26}" y="{y+44}" font-size="19" font-weight="700" fill="{INK}">{t}</text>'
    for k, ln in enumerate(d.split("\n")):
        body += f'<text x="{x+26}" y="{y+76+k*23}" font-size="14" fill="{SUB}">{ln}</text>'
body += f'<circle cx="{cx}" cy="{cy}" r="92" fill="{PURPLE}" fill-opacity="0.08" stroke="{PURPLE}" stroke-width="2"/>'
body += f'<circle cx="{cx}" cy="{cy}" r="70" fill="{PURPLE}"/><text x="{cx}" y="{cy-4}" text-anchor="middle" font-size="26" font-weight="700" fill="#fff">LLM</text><text x="{cx}" y="{cy+22}" text-anchor="middle" font-size="13" fill="#fff" fill-opacity="0.9">Gemini Copilot</text>'
body += f'<rect x="884" y="496" width="332" height="132" rx="16" fill="{INK}"/>'
body += f'<text x="910" y="540" font-size="19" font-weight="700" fill="#fff">Unified Response</text>'
for k, ln in enumerate(["Judgment + Evidence + Caveats", "UI Control JSON (Zoom / Filter)"]):
    body += f'<text x="910" y="{574+k*26}" font-size="14" fill="#fff" fill-opacity="0.85">{ln}</text>'
body += f'<path d="M{cx} {cy+92} V 562 H 880" fill="none" stroke="{INK}" stroke-width="2" marker-end="url(#arr)"/>'
body += card(420, 596, 420, 72) + f'<text x="440" y="626" font-size="13" font-weight="700" fill="{PURPLE}">Sample Query</text><text x="440" y="650" font-size="14" fill="{INK}">"Are this week\'s fires in Borneo swidden? 7d risk?"</text>'
s4 = page(4, "Multi-Perspective LLM Reasoning  —  5 Analytical Lenses", body,
          defs=f'<defs><marker id="arr" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="{INK}"/></marker></defs>')

# ---------- 5: demo UI tour (uses uploaded screenshot) ----------
defs5 = '<defs><clipPath id="demoClip"><rect x="64" y="160" width="720" height="450" rx="14"/></clipPath></defs>'
b5 = card(60, 156, 728, 458, fill="#0D1117")
b5 += f'<g clip-path="url(#demoClip)"><image href="{IMG_URI}" x="64" y="128" width="720" height="482" preserveAspectRatio="xMidYMin slice"/></g>'

callouts = [
    (1, 148, 250, PURPLE, "AI Chat (BYOK)", "Natural-language country, city &amp; topic\nqueries auto-sync globe &amp; panels"),
    (2, 370, 320, ORANGE, "3D Terrain Globe", "Interactive 3D heat &amp; 7-day risk\nvisualization with region highlight"),
    (3, 580, 260, BLUE, "Forecast Workspace", "Switch 7-Day Risk, Live Detections,\nWeekly Trends &amp; Regional Matrix"),
    (4, 390, 565, GREEN, "Timeline Slider", "Scrub historical dates (e.g. 2023-03-20)\nand play thermal evolution"),
]
for num, px, py, col, title, desc in callouts:
    b5 += f'<circle cx="{px}" cy="{py}" r="18" fill="{col}" fill-opacity="0.25"/>'
    b5 += badge(px, py, num, col)

for i, (num, px, py, col, title, desc) in enumerate(callouts):
    cy_card = 160 + i * 116
    b5 += card(816, cy_card, 400, 102)
    b5 += badge(848, cy_card + 34, num, col)
    b5 += f'<text x="876" y="{cy_card+40}" font-size="18" font-weight="700" fill="{INK}">{title}</text>'
    for k, ln in enumerate(desc.split("\n")):
        b5 += f'<text x="840" y="{cy_card+66+k*20}" font-size="14" fill="{SUB}">{ln}</text>'

b5 += f'<text x="64" y="644" font-size="14" fill="{SUB}">Live deployment (suim0kkin.github.io/pyrocopilot/) — AI chat, 3D globe &amp; analytics unified in one static web app</text>'
s5 = page(5, "Live Demo: UI &amp; 4 Core Modules", b5, defs=defs5)

# ---------- 6: demo workflow & multi-perspective evidence ----------
defs6 = ('<defs>'
         '<clipPath id="clipChat"><rect x="64" y="160" width="320" height="390" rx="14"/></clipPath>'
         '<clipPath id="clipWork"><rect x="856" y="160" width="360" height="390" rx="14"/></clipPath>'
         '<marker id="arr6" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1C1E21"/></marker>'
         '</defs>')
b6 = ""
b6 += card(60, 156, 328, 398, fill="#0D1117")
b6 += f'<g clip-path="url(#clipChat)"><image href="{IMG_URI}" x="44" y="34" width="1180" height="738"/></g>'
b6 += chip(76, 566, "1. Query &amp; Preset Prompts", PURPLE, 220)

mid_cards = [
    ("Intent &amp; Entity Extraction", "Parse prompts (e.g. 'Amazon Swidden &amp; Weather')\nto target country, timeframe &amp; analytical lens", PURPLE),
    ("Auto-Control 3D Globe", "Fly camera to target region, highlight bounds,\nand toggle 7-Day Risk or Timeline layers", ORANGE),
    ("Weather × Fire Drivers", "Surface multi-factor drivers per city, such as\n'7d recent fire · 7mm 30d rain'", BLUE),
]
for i, (t, d, c) in enumerate(mid_cards):
    y = 160 + i * 136
    b6 += card(420, y, 404, 118)
    b6 += f'<rect x="420" y="{y}" width="6" height="118" rx="3" fill="{c}"/>'
    b6 += f'<text x="442" y="{y+36}" font-size="18" font-weight="700" fill="{INK}">{t}</text>'
    for k, ln in enumerate(d.split("\n")):
        b6 += f'<text x="442" y="{y+64+k*22}" font-size="14" fill="{SUB}">{ln}</text>'

b6 += f'<path d="M392 355 H 416" stroke="{INK}" stroke-width="2" marker-end="url(#arr6)"/>'
b6 += f'<path d="M828 355 H 852" stroke="{INK}" stroke-width="2" marker-end="url(#arr6)"/>'

b6 += card(852, 156, 368, 398, fill="#0D1117")
b6 += f'<g clip-path="url(#clipWork)"><image href="{IMG_URI}" x="424" y="64" width="820" height="513"/></g>'
b6 += chip(868, 566, "2. Ranked Risk &amp; Key Drivers", BLUE, 240)

b6 += card(64, 612, 1152, 68)
b6 += f'<text x="88" y="652" font-size="15" font-weight="700" fill="{INK}">Observed in Demo:</text>'
b6 += f'<text x="242" y="652" font-size="15" fill="{SUB}">666 of 1,251 global cities flagged High Risk (≥50%), with peak city Nampula (99%) explained by fire + rainfall drivers</text>'
s6 = page(6, "Live Demo: LLM-Orchestrated Multi-Perspective Analysis", b6, defs=defs6)

# ---------- 7: impact & stack ----------
b7 = card(64, 156, 560, 330)
b7 += f'<text x="92" y="200" font-size="22" font-weight="700" fill="{INK}">Intended Impact</text>'
impacts = [("Fewer False Alarms", "Separate fire types to prevent overestimation", ORANGE),
           ("Proactive Decisions", "See 7-day forecast alongside live heat", BLUE),
           ("Accessible Analytics", "No GIS expertise needed via EN/JA chat", PURPLE),
           ("Forest &amp; Peat Monitoring", "Support policy on swidden vs wildfire", GREEN)]
for i, (t, d, c) in enumerate(impacts):
    y = 228 + i * 62
    b7 += f'<rect x="92" y="{y}" width="8" height="46" rx="4" fill="{c}"/><text x="116" y="{y+20}" font-size="17" font-weight="700" fill="{INK}">{t}</text><text x="116" y="{y+42}" font-size="14" fill="{SUB}">{d}</text>'
b7 += card(656, 156, 560, 330) + f'<text x="684" y="200" font-size="22" font-weight="700" fill="{INK}">Tech Stack</text>'
stack = [("Python", ORANGE, 86), ("JavaScript", ORANGE, 108), ("LightGBM", BLUE, 100), ("XGBoost", BLUE, 96), ("Polars", BLUE, 80),
         ("D3.js / TopoJSON", PURPLE, 146), ("Custom 3D Globe", PURPLE, 144), ("Gemini API", PURPLE, 108), ("Kaggle", GREEN, 82), ("GitHub Pages", GREEN, 122)]
x, y = 684, 228
for t, c, w in stack:
    if x + w > 1190:
        x, y = 684, y + 46
    b7 += chip(x, y, t, c, w); x += w + 12
b7 += f'<text x="684" y="436" font-size="14" fill="{SUB}">No dedicated GPU needed · Shared feature code across train &amp; inference</text>'
b7 += card(64, 516, 1152, 144) + f'<rect x="64" y="516" width="1152" height="6" rx="3" fill="{ORANGE}"/>'
b7 += f'<text x="92" y="560" font-size="20" font-weight="700" fill="{INK}">Design Considerations &amp; Limitations</text>'
cons = ["Cross-sensor bias corrected via FRP harmonization", "User-provided Gemini key (BYOK)",
        "Probabilistic risk; not a substitute for official alerts", "FIRMS NRT detections carry ingestion latency"]
for i, t in enumerate(cons):
    cx_ = 92 + (i % 2) * 560; cy_ = 594 + (i // 2) * 32
    b7 += f'<circle cx="{cx_}" cy="{cy_-5}" r="4" fill="{ORANGE}"/><text x="{cx_+16}" y="{cy_}" font-size="15" fill="{INK}">{t}</text>'
s7 = page(7, "Impact, Tech Stack &amp; Design Factors", b7)

slides = [
    ("01_cover", s1),
    ("02_contents", s2),
    ("03_overview", s3),
    ("04_llm_multiperspective", s4),
    ("05_demo_workspace", s5),
    ("06_demo_workflow", s6),
    ("07_impact_stack", s7),
]
for name, svg in slides:
    (OUT / f"{name}.svg").write_text(svg, encoding="utf-8")
print("generated 7 english slides")
