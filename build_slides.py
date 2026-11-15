import base64
from pathlib import Path

OUT = Path(__file__).parent
IMG_PATH = Path("/Users/wataraiharuki/.gemini/antigravity/brain/777f0328-c1e2-419d-beab-fff0253881ce/.user_uploaded/media_1794723865777_6017e08b.jpg")
IMG_B64 = base64.b64encode(IMG_PATH.read_bytes()).decode("ascii")
IMG_URI = f"data:image/jpeg;base64,{IMG_B64}"

FONT = "'Hiragino Sans','Noto Sans JP','Inter','Helvetica Neue',Arial,sans-serif"
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
    w = w or (len(text) * 9 + 28)
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
<text x="640" y="466" text-anchor="middle" font-size="22" fill="{SUB}">LLMが多角的に判断する 3D地球儀 火災・熱異常インテリジェンス</text>
{chip(404, 520, "NASA FIRMS", ORANGE, 130)}{chip(546, 520, "NASA POWER", BLUE, 130)}{chip(688, 520, "Gemini Copilot", PURPLE, 150)}{chip(850, 520, "7-Day Risk", GREEN, 100)}
<text x="640" y="650" text-anchor="middle" font-size="14" fill="{SUB}">NASA Space Apps Challenge  ·  Project Overview (7 Slides)</text>
</svg>"""

# ---------- 2: contents ----------
items = [
    ("01", "プロジェクト概要", "観測 → ML推定 → LLM解釈の3ステップと基本指標", ORANGE),
    ("02", "LLMによる多角的判断", "5つの視点を統合し、根拠＋地図操作を出力する仕組み", PURPLE),
    ("03", "デモ画面：UIと4つの主要機能", "AI Chat・3D地球儀・予測ワークスペース・タイムライン", BLUE),
    ("04", "デモ画面：LLM連動のリアルタイム分析", "自然言語クエリから地球儀フォーカスと気象ドライバー提示まで", TEAL),
    ("05", "インパクト・技術・設計上の配慮", "期待される効果、使用技術スタック、制約と限界", GREEN),
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
s2 = page(2, "目次", rows)

# ---------- 3: overview ----------
steps = [("Observe", "観測データを集める", ORANGE, ["FIRMS VIIRS (NOAA-20/21)", "MODIS / VIIRS 過去データ", "NASA POWER 都市別気象"]),
         ("Model", "機械学習で推定する", BLUE, ["検知: 植生火災 vs 静的熱源", "FRP調和: XGBoost Tweedie", "7日先リスク (LightGBM)"]),
         ("Explain", "LLMが解釈・操作する", PURPLE, ["Gemini Copilot (BYOK)", "自然言語で質問 (日/英)", "地球儀をズーム・強調表示"])]
cols = ""
for i, (en, ja, c, lines) in enumerate(steps):
    x = 64 + i * 400
    cols += card(x, 166, 352, 300)
    cols += f'<circle cx="{x+44}" cy="218" r="22" fill="{c}"/><text x="{x+44}" y="225" text-anchor="middle" font-size="20" font-weight="700" fill="#fff">{i+1}</text>'
    cols += f'<text x="{x+80}" y="214" font-size="24" font-weight="700" fill="{INK}">{en}</text><text x="{x+80}" y="240" font-size="15" fill="{SUB}">{ja}</text>'
    for j, l in enumerate(lines):
        cols += f'<circle cx="{x+32}" cy="{296+j*52}" r="4" fill="{c}"/><text x="{x+48}" y="{301+j*52}" font-size="16" fill="{INK}">{l}</text>'
    if i < 2:
        cols += f'<path d="M{x+362} 316 h28 m-8 -8 l8 8 l-8 8" fill="none" stroke="{SUB}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>'
kpis = [("3", "火災の種類を区別", "山火事 / 焼畑 / 産業熱源"), ("2", "センサーを統合", "MODIS + VIIRS"), ("7日", "先までのリスク", "50km圏の発生確率"), ("静的", "サーバー不要配信", "GitHub Pages")]
for i, (v, l, s) in enumerate(kpis):
    x = 64 + i * 292
    cols += card(x, 500, 268, 160) + f'<text x="{x+24}" y="564" font-size="42" font-weight="700" fill="{BLUE}">{v}</text><text x="{x+24}" y="601" font-size="17" font-weight="600" fill="{INK}">{l}</text><text x="{x+24}" y="628" font-size="14" fill="{SUB}">{s}</text>'
s3 = page(3, "プロジェクト概要  —  観測 → 推定 → 解釈", cols)

# ---------- 4: LLM multi-perspective ----------
lenses = [("発生源の種別", "焼畑・山火事・産業を\n空間的な再発性で区別", ORANGE, (64, 156)),
          ("気象コンテキスト", "直近30日の気温・降水など\nNASA POWER特徴量", BLUE, (64, 326)),
          ("センサー信頼性", "MODIS/VIIRSの差と\nFRP調和統計を考慮", TEAL, (64, 496)),
          ("地域・社会文脈", "アマゾン・ボルネオ等の\n地名辞書と日本語エイリアス", PURPLE, (884, 156)),
          ("時間変化・予測", "週次時系列と\n7日先リスクの推移", GREEN, (884, 326))]
body = ""
cx, cy = 640, 336
for t, d, c, (x, y) in lenses:
    ax = x + 332 if x < 600 else x
    body += f'<path d="M{ax} {y+66} C {ax + (60 if x<600 else -60)} {y+66}, {cx + (-120 if x<600 else 120)} {cy}, {cx + (-92 if x<600 else 92)} {cy}" fill="none" stroke="{c}" stroke-width="2" stroke-dasharray="5 5"/>'
for t, d, c, (x, y) in lenses:
    body += card(x, y, 332, 132) + f'<rect x="{x}" y="{y}" width="6" height="132" rx="3" fill="{c}"/>'
    body += f'<text x="{x+28}" y="{y+44}" font-size="20" font-weight="700" fill="{INK}">{t}</text>'
    for k, ln in enumerate(d.split("\n")):
        body += f'<text x="{x+28}" y="{y+78+k*24}" font-size="15" fill="{SUB}">{ln}</text>'
body += f'<circle cx="{cx}" cy="{cy}" r="92" fill="{PURPLE}" fill-opacity="0.08" stroke="{PURPLE}" stroke-width="2"/>'
body += f'<circle cx="{cx}" cy="{cy}" r="70" fill="{PURPLE}"/><text x="{cx}" y="{cy-4}" text-anchor="middle" font-size="26" font-weight="700" fill="#fff">LLM</text><text x="{cx}" y="{cy+22}" text-anchor="middle" font-size="13" fill="#fff" fill-opacity="0.9">Gemini Copilot</text>'
body += f'<rect x="884" y="496" width="332" height="132" rx="16" fill="{INK}"/>'
body += f'<text x="912" y="540" font-size="20" font-weight="700" fill="#fff">統合された回答</text>'
for k, ln in enumerate(["判断 + 根拠 + 不確実性", "地図操作JSON (ズーム/強調)"]):
    body += f'<text x="912" y="{574+k*26}" font-size="15" fill="#fff" fill-opacity="0.85">{ln}</text>'
body += f'<path d="M{cx} {cy+92} V 562 H 880" fill="none" stroke="{INK}" stroke-width="2" marker-end="url(#arr)"/>'
body += card(420, 596, 420, 72) + f'<text x="440" y="628" font-size="14" font-weight="700" fill="{PURPLE}">質問例</text><text x="440" y="651" font-size="15" fill="{INK}">「ボルネオの今週の火災は焼畑？リスクは？」</text>'
s4 = page(4, "LLMによる多角的判断  —  5つの視点を統合", body,
          defs=f'<defs><marker id="arr" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="{INK}"/></marker></defs>')

# ---------- 5: demo UI tour (uses uploaded screenshot) ----------
# Image placed at x=64, y=160, w=720, h=450 (aspect 1024:640 = 1.6)
# Crop top browser chrome subtly using clipPath starting slightly below macOS bar if desired, or show full clean window
defs5 = '<defs><clipPath id="demoClip"><rect x="64" y="160" width="720" height="450" rx="14"/></clipPath></defs>'
b5 = card(60, 156, 728, 458, fill="#0D1117")
# Shift image up by 34px inside clip so macOS menu bar & browser tabs are cropped cleanly, keeping address bar/app UI crisp
b5 += f'<g clip-path="url(#demoClip)"><image href="{IMG_URI}" x="64" y="128" width="720" height="482" preserveAspectRatio="xMidYMin slice"/></g>'

# Callout badges on the screenshot (coordinates tuned to 720px wide image at x=64, y=128..610)
# 1: Left AI Chat panel (~x=150, y=310)
# 2: Center 3D Globe (~x=360, y=330)
# 3: Right Workspace (~x=590, y=320)
# 4: Bottom Timeline (~x=390, y=565)
callouts = [
    (1, 148, 250, PURPLE, "AI Chat (BYOK)", "国名・都市名・キーワード入力で\n地図とパネルを自動連動"),
    (2, 370, 320, ORANGE, "3D Terrain Globe", "熱異常・7日先リスクを\n地球儀上にヒート表示"),
    (3, 580, 260, BLUE, "Forecast Workspace", "7日リスク・ライブ検知・\n週次推移・地域比較を切替"),
    (4, 390, 565, GREEN, "Timeline Slider", "過去の日付へ遡り\n熱分布の変化を再生"),
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
        b5 += f'<text x="840" y="{cy_card+68+k*20}" font-size="14" fill="{SUB}">{ln}</text>'

b5 += f'<text x="64" y="644" font-size="14" fill="{SUB}">実際のデモ画面 (suim0kkin.github.io/pyrocopilot/) — 単一の静的Webアプリ上でAI対話・3D地球儀・統計パネルが統合動作</text>'
s5 = page(5, "デモ画面：UIと4つの主要機能", b5, defs=defs5)

# ---------- 6: demo workflow & multi-perspective evidence ----------
# Show zoomed/focused crops or key excerpts alongside structured explanation
defs6 = ('<defs>'
         '<clipPath id="clipChat"><rect x="64" y="160" width="320" height="390" rx="14"/></clipPath>'
         '<clipPath id="clipWork"><rect x="856" y="160" width="360" height="390" rx="14"/></clipPath>'
         '<marker id="arr6" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1C1E21"/></marker>'
         '</defs>')
b6 = ""
# Left: cropped AI Chat panel from the screenshot (left side of 1024x640 image)
b6 += card(60, 156, 328, 398, fill="#0D1117")
b6 += f'<g clip-path="url(#clipChat)"><image href="{IMG_URI}" x="44" y="34" width="1180" height="738"/></g>'
b6 += chip(76, 566, "① 自然言語＋プリセット指示", PURPLE, 220)

# Center: LLM Orchestration steps connecting Left (Prompt) -> Right (Multi-perspective Workspace)
mid_cards = [
    ("意図抽出と対象絞り込み", "「日本 7-Day予測」「Amazon 焼畑・気象」等の\n指示から地域・期間・分析軸を特定", PURPLE),
    ("3D地球儀の自動制御", "対象エリアへカメラを移動・拡大し\nハイライト範囲とレイヤーを自動切替", ORANGE),
    ("気象×火災ドライバー提示", "「7d recent fire · 7mm 30d rain」のように\n直近火災と30日降水量を根拠として統合表示", BLUE),
]
for i, (t, d, c) in enumerate(mid_cards):
    y = 160 + i * 136
    b6 += card(420, y, 404, 118)
    b6 += f'<rect x="420" y="{y}" width="6" height="118" rx="3" fill="{c}"/>'
    b6 += f'<text x="444" y="{y+36}" font-size="18" font-weight="700" fill="{INK}">{t}</text>'
    for k, ln in enumerate(d.split("\n")):
        b6 += f'<text x="444" y="{y+64+k*22}" font-size="14" fill="{SUB}">{ln}</text>'

# Arrows between left -> mid -> right
b6 += f'<path d="M392 355 H 416" stroke="{INK}" stroke-width="2" marker-end="url(#arr6)"/>'
b6 += f'<path d="M828 355 H 852" stroke="{INK}" stroke-width="2" marker-end="url(#arr6)"/>'

# Right: cropped Workspace panel from the screenshot (right side of 1024x640 image)
b6 += card(852, 156, 368, 398, fill="#0D1117")
b6 += f'<g clip-path="url(#clipWork)"><image href="{IMG_URI}" x="424" y="64" width="820" height="513"/></g>'
b6 += chip(868, 566, "② 統合結果（高リスク都市・要因）", BLUE, 250)

b6 += card(64, 612, 1152, 68)
b6 += f'<text x="88" y="652" font-size="15" font-weight="600" fill="{INK}">デモ実例の見どころ：</text>'
b6 += f'<text x="260" y="652" font-size="15" fill="{SUB}">1,251都市中 666都市が高リスク(≥50%)と判定され、ピーク都市 Nampula (99%) の要因まで一画面で説明可能</text>'
s6 = page(6, "デモ画面にみる「LLM連動の多角的分析」", b6, defs=defs6)

# ---------- 7: impact & stack ----------
b7 = card(64, 156, 560, 330)
b7 += f'<text x="92" y="200" font-size="22" font-weight="700" fill="{INK}">期待されるインパクト</text>'
impacts = [("誤警報の低減", "火災種別を分けて過大評価を防ぐ", ORANGE), ("先読みの意思決定", "「今」だけでなく7日先まで把握", BLUE),
           ("誰でも使える分析", "専門知識なしで対話・直感操作", PURPLE), ("森林・泥炭火災の監視", "焼畑と山火事の政策議論を支援", GREEN)]
for i, (t, d, c) in enumerate(impacts):
    y = 228 + i * 62
    b7 += f'<rect x="92" y="{y}" width="8" height="46" rx="4" fill="{c}"/><text x="116" y="{y+20}" font-size="17" font-weight="700" fill="{INK}">{t}</text><text x="116" y="{y+42}" font-size="14" fill="{SUB}">{d}</text>'
b7 += card(656, 156, 560, 330) + f'<text x="684" y="200" font-size="22" font-weight="700" fill="{INK}">技術スタック</text>'
stack = [("Python", ORANGE, 90), ("JavaScript", ORANGE, 110), ("LightGBM", BLUE, 100), ("XGBoost", BLUE, 96), ("Polars", BLUE, 80),
         ("D3.js / TopoJSON", PURPLE, 150), ("自作3D地球儀", PURPLE, 130), ("Gemini API", PURPLE, 110), ("Kaggle", GREEN, 80), ("GitHub Pages", GREEN, 120)]
x, y = 684, 228
for t, c, w in stack:
    if x + w > 1190:
        x, y = 684, y + 46
    b7 += chip(x, y, t, c, w); x += w + 12
b7 += f'<text x="684" y="436" font-size="14" fill="{SUB}">専用GPU不要 · 学習/推論で特徴量コードを共有</text>'
b7 += card(64, 516, 1152, 144) + f'<rect x="64" y="516" width="1152" height="6" rx="3" fill="{ORANGE}"/>'
b7 += f'<text x="92" y="560" font-size="20" font-weight="700" fill="{INK}">設計上の配慮と限界</text>'
cons = ["センサー間バイアスをFRP調和で補正", "Gemini鍵はユーザー持ち込み (BYOK)", "予測は確率であり公式警報の代替ではない", "FIRMS検知には遅延がある"]
for i, t in enumerate(cons):
    cx_ = 92 + (i % 2) * 560; cy_ = 594 + (i // 2) * 32
    b7 += f'<circle cx="{cx_}" cy="{cy_-5}" r="4" fill="{ORANGE}"/><text x="{cx_+16}" y="{cy_}" font-size="16" fill="{INK}">{t}</text>'
s7 = page(7, "インパクト・技術・設計上の配慮", b7)

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
print("generated 7 slides")
