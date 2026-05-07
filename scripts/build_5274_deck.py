#!/usr/bin/env python3
"""Generate a beautified slide-deck-style PDF for 5274 Quick Take."""
import pathlib
from weasyprint import HTML, CSS

OUT = pathlib.Path("output/5274_quick_take_deck.pdf")
OUT.parent.mkdir(parents=True, exist_ok=True)

# ---- Inline SVG icon library (flat design) -----------------------------
ICONS = {
    "chip": """<svg viewBox='0 0 64 64' xmlns='http://www.w3.org/2000/svg'>
        <rect x='14' y='14' width='36' height='36' rx='4' fill='#1a3a6c'/>
        <rect x='22' y='22' width='20' height='20' rx='2' fill='#60a5fa'/>
        <g stroke='#1a3a6c' stroke-width='2'>
        <line x1='20' y1='6'  x2='20' y2='14'/><line x1='32' y1='6'  x2='32' y2='14'/><line x1='44' y1='6'  x2='44' y2='14'/>
        <line x1='20' y1='50' x2='20' y2='58'/><line x1='32' y1='50' x2='32' y2='58'/><line x1='44' y1='50' x2='44' y2='58'/>
        <line x1='6'  y1='20' x2='14' y2='20'/><line x1='6'  y1='32' x2='14' y2='32'/><line x1='6'  y1='44' x2='14' y2='44'/>
        <line x1='50' y1='20' x2='58' y2='20'/><line x1='50' y1='32' x2='58' y2='32'/><line x1='50' y1='44' x2='58' y2='44'/>
        </g></svg>""",
    "chart": """<svg viewBox='0 0 64 64' xmlns='http://www.w3.org/2000/svg'>
        <rect x='8' y='8' width='48' height='48' rx='4' fill='#eff6ff'/>
        <rect x='14' y='34' width='6' height='16' fill='#3b82f6'/>
        <rect x='24' y='26' width='6' height='24' fill='#3b82f6'/>
        <rect x='34' y='18' width='6' height='32' fill='#1a3a6c'/>
        <rect x='44' y='10' width='6' height='40' fill='#1a3a6c'/>
        </svg>""",
    "shield": """<svg viewBox='0 0 64 64' xmlns='http://www.w3.org/2000/svg'>
        <path d='M32 6 L54 14 V30 C54 44 44 54 32 58 C20 54 10 44 10 30 V14 Z' fill='#10b981'/>
        <path d='M22 32 L29 39 L44 24' stroke='white' stroke-width='4' fill='none' stroke-linecap='round' stroke-linejoin='round'/>
        </svg>""",
    "rocket": """<svg viewBox='0 0 64 64' xmlns='http://www.w3.org/2000/svg'>
        <path d='M32 6 C42 16 46 26 46 36 V46 H18 V36 C18 26 22 16 32 6 Z' fill='#f59e0b'/>
        <circle cx='32' cy='28' r='5' fill='white'/>
        <path d='M18 46 L12 56 L22 50 Z' fill='#ef4444'/>
        <path d='M46 46 L52 56 L42 50 Z' fill='#ef4444'/>
        </svg>""",
    "warn": """<svg viewBox='0 0 64 64' xmlns='http://www.w3.org/2000/svg'>
        <path d='M32 6 L60 56 L4 56 Z' fill='#ef4444'/>
        <rect x='29' y='22' width='6' height='18' rx='2' fill='white'/>
        <circle cx='32' cy='48' r='3' fill='white'/>
        </svg>""",
    "calendar": """<svg viewBox='0 0 64 64' xmlns='http://www.w3.org/2000/svg'>
        <rect x='8' y='12' width='48' height='44' rx='4' fill='#1a3a6c'/>
        <rect x='8' y='12' width='48' height='12' fill='#3b82f6'/>
        <rect x='16' y='6' width='6' height='12' rx='2' fill='#1a3a6c'/>
        <rect x='42' y='6' width='6' height='12' rx='2' fill='#1a3a6c'/>
        <rect x='14' y='28' width='8' height='6' fill='white'/>
        <rect x='28' y='28' width='8' height='6' fill='white'/>
        <rect x='42' y='28' width='8' height='6' fill='#fbbf24'/>
        <rect x='14' y='40' width='8' height='6' fill='white'/>
        <rect x='28' y='40' width='8' height='6' fill='white'/>
        <rect x='42' y='40' width='8' height='6' fill='white'/>
        </svg>""",
    "scale": """<svg viewBox='0 0 64 64' xmlns='http://www.w3.org/2000/svg'>
        <rect x='30' y='10' width='4' height='44' fill='#1a3a6c'/>
        <rect x='14' y='52' width='36' height='4' rx='2' fill='#1a3a6c'/>
        <line x1='32' y1='14' x2='14' y2='28' stroke='#1a3a6c' stroke-width='2'/>
        <line x1='32' y1='14' x2='50' y2='28' stroke='#1a3a6c' stroke-width='2'/>
        <ellipse cx='14' cy='32' rx='10' ry='4' fill='#3b82f6'/>
        <ellipse cx='50' cy='32' rx='10' ry='4' fill='#10b981'/>
        </svg>""",
    "target": """<svg viewBox='0 0 64 64' xmlns='http://www.w3.org/2000/svg'>
        <circle cx='32' cy='32' r='26' fill='#fee2e2'/>
        <circle cx='32' cy='32' r='18' fill='#fca5a5'/>
        <circle cx='32' cy='32' r='10' fill='#ef4444'/>
        <circle cx='32' cy='32' r='4' fill='white'/>
        </svg>""",
    "globe": """<svg viewBox='0 0 64 64' xmlns='http://www.w3.org/2000/svg'>
        <circle cx='32' cy='32' r='24' fill='#3b82f6'/>
        <ellipse cx='32' cy='32' rx='24' ry='10' fill='none' stroke='white' stroke-width='2'/>
        <ellipse cx='32' cy='32' rx='10' ry='24' fill='none' stroke='white' stroke-width='2'/>
        <line x1='8' y1='32' x2='56' y2='32' stroke='white' stroke-width='2'/>
        <line x1='32' y1='8' x2='32' y2='56' stroke='white' stroke-width='2'/>
        </svg>""",
    "doc": """<svg viewBox='0 0 64 64' xmlns='http://www.w3.org/2000/svg'>
        <path d='M14 6 H40 L52 18 V58 H14 Z' fill='#eff6ff' stroke='#1a3a6c' stroke-width='2'/>
        <path d='M40 6 V18 H52' fill='none' stroke='#1a3a6c' stroke-width='2'/>
        <line x1='20' y1='28' x2='44' y2='28' stroke='#3b82f6' stroke-width='2'/>
        <line x1='20' y1='36' x2='44' y2='36' stroke='#3b82f6' stroke-width='2'/>
        <line x1='20' y1='44' x2='36' y2='44' stroke='#3b82f6' stroke-width='2'/>
        </svg>""",
    "chevron": """<svg viewBox='0 0 64 64' xmlns='http://www.w3.org/2000/svg'>
        <circle cx='32' cy='32' r='28' fill='#1a3a6c'/>
        <path d='M26 20 L40 32 L26 44' stroke='white' stroke-width='4' fill='none' stroke-linecap='round' stroke-linejoin='round'/>
        </svg>""",
}

def icon(name, size=64):
    return f"<span class='icon icon-{size}'>{ICONS[name]}</span>"

# ---- Page assembly ------------------------------------------------------
def page(cls, body, page_num=None, total=None):
    foot = ""
    if page_num is not None:
        foot = f"<div class='footer'><span>Finece　•　信驊科技 5274 Quick Take</span><span>{page_num} / {total}</span></div>"
    return f"<section class='page {cls}'>{body}{foot}</section>"

PAGES = []

# Page 1 — Cover
PAGES.append(page("cover", f"""
<div class='cover-deco'>{ICONS['chip']}</div>
<div class='cover-eyebrow'>機構研究 ｜ Quick Take</div>
<h1 class='cover-title'>信驊科技</h1>
<div class='cover-ticker'>5274.TWO　·　Aspeed Technology</div>
<div class='cover-tag'>BMC 全球寡占　·　AI Server 量價齊揚</div>
<div class='cover-meta'>
  <div><span class='lbl'>市場</span><span class='val'>台灣 TPEx</span></div>
  <div><span class='lbl'>會計</span><span class='val'>TIFRS / TWD</span></div>
  <div><span class='lbl'>日期</span><span class='val'>2026 / 05 / 07</span></div>
</div>
<div class='cover-foot'>Finece Global Equity Research</div>
"""))

# Page 2 — TOC / 大綱
PAGES.append(page("toc", f"""
<div class='page-head'>
  <div class='page-eyebrow'>大綱 OUTLINE</div>
  <h2 class='page-title'>本份報告涵蓋</h2>
</div>
<div class='toc-grid'>
  <div class='toc-item'><div class='toc-num'>01</div><div class='toc-icon'>{ICONS['globe']}</div><div class='toc-text'><div class='toc-title'>公司與市場</div><div class='toc-sub'>商業模式與市占地位</div></div></div>
  <div class='toc-item'><div class='toc-num'>02</div><div class='toc-icon'>{ICONS['rocket']}</div><div class='toc-text'><div class='toc-title'>三大買進理由</div><div class='toc-sub'>結構性正向 driver</div></div></div>
  <div class='toc-item'><div class='toc-num'>03</div><div class='toc-icon'>{ICONS['warn']}</div><div class='toc-text'><div class='toc-title'>四大風險</div><div class='toc-sub'>需要密切監控的尾部風險</div></div></div>
  <div class='toc-item'><div class='toc-num'>04</div><div class='toc-icon'>{ICONS['scale']}</div><div class='toc-text'><div class='toc-title'>估值框架</div><div class='toc-sub'>P/E、EV/EBITDA、DCF 加權</div></div></div>
  <div class='toc-item'><div class='toc-num'>05</div><div class='toc-icon'>{ICONS['calendar']}</div><div class='toc-text'><div class='toc-title'>催化日曆</div><div class='toc-sub'>未來 60-90 天事件</div></div></div>
  <div class='toc-item'><div class='toc-num'>06</div><div class='toc-icon'>{ICONS['target']}</div><div class='toc-text'><div class='toc-title'>結論與行動</div><div class='toc-sub'>評等與下一步</div></div></div>
</div>
""", 2, 13))

# Page 3 — Section divider 01
PAGES.append(page("divider divider-blue", f"""
<div class='divider-num'>01</div>
<div class='divider-icon'>{ICONS['globe']}</div>
<h2 class='divider-title'>公司與市場</h2>
<div class='divider-sub'>BMC 寡占地位　·　AI 浪潮中的 fabless 結構性贏家</div>
""", 3, 13))

# Page 4 — Company snapshot
PAGES.append(page("content", f"""
<div class='page-head'>
  <div class='page-eyebrow'>01　公司一句話</div>
  <h2 class='page-title'>BMC 全球市占 70%＋</h2>
</div>
<div class='one-liner'>
  <div class='one-liner-icon'>{ICONS['chip']}</div>
  <div class='one-liner-body'>
    信驊以 <b>BMC（Baseboard Management Controller）</b>標準晶片
    主導全球伺服器遠端管理市場，<b>AI server 出貨潮直接放大量、價、含金量</b>。
    fabless、零重資本、自然 USD hedge、高毛利、高配息。
  </div>
</div>
<div class='kpi-row'>
  <div class='kpi'><div class='kpi-num'>70%＋</div><div class='kpi-lbl'>全球 BMC 市占</div></div>
  <div class='kpi'><div class='kpi-num'>60%＋</div><div class='kpi-lbl'>歷史毛利率</div></div>
  <div class='kpi'><div class='kpi-num'>30%＋</div><div class='kpi-lbl'>歷史 ROE</div></div>
  <div class='kpi'><div class='kpi-num'>80%＋</div><div class='kpi-lbl'>歷史配息率</div></div>
</div>
""", 4, 13))

# Page 5 — Section divider 02
PAGES.append(page("divider divider-orange", f"""
<div class='divider-num'>02</div>
<div class='divider-icon'>{ICONS['rocket']}</div>
<h2 class='divider-title'>三大買進理由</h2>
<div class='divider-sub'>為何信驊是 AI server 結構性贏家</div>
""", 5, 13))

# Page 6 — Reasons
PAGES.append(page("content", f"""
<div class='page-head'>
  <div class='page-eyebrow'>02　REASONS TO BUY</div>
  <h2 class='page-title'>三件值得買的理由</h2>
</div>
<div class='cards-3'>
  <div class='card'>
    <div class='card-icon'>{ICONS['chip']}</div>
    <div class='card-num'>01</div>
    <div class='card-title'>BMC 寡占＋AI 量價齊揚</div>
    <div class='card-body'>每台 AI server BMC 滲透 100%；AST2700 切入更先進製程，function set 升級，ASP 較 AST2600 上修中個位數至雙位數。</div>
  </div>
  <div class='card'>
    <div class='card-icon'>{ICONS['shield']}</div>
    <div class='card-num'>02</div>
    <div class='card-title'>成長＋高息防禦</div>
    <div class='card-body'>毛利 60%＋／營益率 50%＋／ROE 30%＋／淨現金、無有息負債／配息率 80%＋。fabless 模型 capex/sales 個位數，FCF 接近淨利。</div>
  </div>
  <div class='card'>
    <div class='card-icon'>{ICONS['rocket']}</div>
    <div class='card-num'>03</div>
    <div class='card-title'>路徑外 Optionality</div>
    <div class='card-body'>客製 ASIC（Hyperscaler／AI 網通客戶）、車用工控管理 IC、Edge AI controller 提供超出 BMC TAM 的成長拉力。</div>
  </div>
</div>
""", 6, 13))

# Page 7 — Section divider 03
PAGES.append(page("divider divider-red", f"""
<div class='divider-num'>03</div>
<div class='divider-icon'>{ICONS['warn']}</div>
<h2 class='divider-title'>四大風險</h2>
<div class='divider-sub'>機構投資人必須監控的尾部風險</div>
""", 7, 13))

# Page 8 — Risks
PAGES.append(page("content", f"""
<div class='page-head'>
  <div class='page-eyebrow'>03　KEY RISKS</div>
  <h2 class='page-title'>四件需要警覺的風險</h2>
</div>
<div class='risk-list'>
  <div class='risk-item risk-high'>
    <div class='risk-head'><span class='risk-tag'>最大尾部風險</span><span class='risk-title'>Hyperscaler 自研 BMC 加速</span></div>
    <div class='risk-body'>AWS／Google／Meta／Microsoft 任一陣營若大規模轉自研，將直接侵蝕高 ASP 段業務。</div>
  </div>
  <div class='risk-item'>
    <div class='risk-head'><span class='risk-tag'>結構性</span><span class='risk-title'>客戶集中度</span></div>
    <div class='risk-body'>前五大客戶歷史佔比 ~50–60%，OEM 換版延遲造成季度級營收波動。</div>
  </div>
  <div class='risk-item'>
    <div class='risk-head'><span class='risk-tag'>地緣</span><span class='risk-title'>中國國產 BMC 替代</span></div>
    <div class='risk-body'>「信創」政策推動瀾起、ZTE Microelectronics 等替代方案。</div>
  </div>
  <div class='risk-item'>
    <div class='risk-head'><span class='risk-tag'>估值</span><span class='risk-title'>Multiple Compression</span></div>
    <div class='risk-body'>高 P/E 區間運行；AI server 展望下修易 EPS×倍數雙殺。</div>
  </div>
</div>
""", 8, 13))

# Page 9 — Section divider 04
PAGES.append(page("divider divider-green", f"""
<div class='divider-num'>04</div>
<div class='divider-icon'>{ICONS['scale']}</div>
<h2 class='divider-title'>估值框架</h2>
<div class='divider-sub'>三法加權　·　目標價推導</div>
""", 9, 13))

# Page 10 — Valuation
PAGES.append(page("content", f"""
<div class='page-head'>
  <div class='page-eyebrow'>04　VALUATION</div>
  <h2 class='page-title'>三法加權估值</h2>
</div>
<table class='val-tbl'>
  <thead><tr><th class='th-method'>方法</th><th class='th-weight'>權重</th><th class='th-assume'>核心假設</th></tr></thead>
  <tbody>
    <tr>
      <td class='val-method'>P/E</td>
      <td><div class='val-bar'><div class='val-bar-fill' style='width:50%;background:#1a3a6c'></div></div><span class='val-pct'>50%</span></td>
      <td class='val-assume'>12M fwd EPS × TPEx IC 設計 peer multiple（聯發科、瑞昱、譜瑞-KY、祥碩 25–35×；信驊 ROE & moat premium）</td>
    </tr>
    <tr>
      <td class='val-method'>EV／<br>EBITDA</td>
      <td><div class='val-bar'><div class='val-bar-fill' style='width:25%;background:#3b82f6'></div></div><span class='val-pct'>25%</span></td>
      <td class='val-assume'>跨境驗證　vs NVDA networking ／ Marvell embedded</td>
    </tr>
    <tr>
      <td class='val-method'>DCF</td>
      <td><div class='val-bar'><div class='val-bar-fill' style='width:25%;background:#10b981'></div></div><span class='val-pct'>25%</span></td>
      <td class='val-assume'>WACC 8.5–10%　·　TGR 3%　·　5Y explicit forecast</td>
    </tr>
  </tbody>
</table>
<div class='val-foot'>加權後得 fair-value range　→　目標價取中位數 ±10% rounded</div>
""", 10, 13))

# Page 11 — Catalyst calendar
PAGES.append(page("content", f"""
<div class='page-head'>
  <div class='page-eyebrow'>05　CATALYSTS</div>
  <h2 class='page-title'>未來 60–90 天催化</h2>
</div>
<table class='cat-tbl'>
  <tr><td class='cat-date'>5/10 前</td><td class='cat-dot'><span style='background:#3b82f6'></span></td><td class='cat-title'>4 月月營收公告</td><td class='cat-stars'>★★★</td><td class='cat-note'>確認 1Q26 momentum</td></tr>
  <tr><td class='cat-date'>5/15 前</td><td class='cat-dot'><span style='background:#3b82f6'></span></td><td class='cat-title'>1Q26 季報申報截止</td><td class='cat-stars'>★★★</td><td class='cat-note'>TIFRS 三表完整數字</td></tr>
  <tr class='cat-highlight'><td class='cat-date'>季報後同週</td><td class='cat-dot'><span style='background:#f59e0b'></span></td><td class='cat-title'>1Q26 法說會</td><td class='cat-stars'>★★★★</td><td class='cat-note'>2026 全年展望、AST2700 ramp</td></tr>
  <tr><td class='cat-date'>5/20–24</td><td class='cat-dot'><span style='background:#10b981'></span></td><td class='cat-title'>Computex 2026</td><td class='cat-stars'>★★★</td><td class='cat-note'>AI server 平台展示與生態鏈訊號</td></tr>
</table>
""", 11, 13))

# Page 12 — Conclusion
PAGES.append(page("content conclusion", f"""
<div class='page-head'>
  <div class='page-eyebrow'>06　CONCLUSION</div>
  <h2 class='page-title'>結論與行動建議</h2>
</div>
<div class='conclusion-block'>
  <div class='rating-card'>
    <div class='rating-icon'>{ICONS['target']}</div>
    <div class='rating-eyebrow'>建議</div>
    <div class='rating-main'>BUY</div>
    <div class='rating-sub'>草案，待估值數據確認</div>
  </div>
  <div class='actions'>
    <div class='action-title'>立即可做的下一步</div>
    <div class='action-list'>
      <div class='action-item'><div class='action-num'>1</div><div><b>資料層　</b>於 .mcp.json 接 TEJ／Bloomberg／Refinitiv，自動取得 consensus 與歷年三表</div></div>
      <div class='action-item'><div class='action-num'>2</div><div><b>建模層　</b>跑 model-update skill 建 5274 三表＋ DCF＋peer comps（Excel）</div></div>
      <div class='action-item'><div class='action-num'>3</div><div><b>完整初評　</b>以 Quick Take 為 thesis 骨架，跑 initiate 30–50 頁 DOCX 終稿</div></div>
      <div class='action-item'><div class='action-num'>4</div><div><b>監控層　</b>催化排入 catalyst tracker（catalysts 指令）</div></div>
    </div>
  </div>
</div>
""", 12, 13))

# Page 13 — Disclaimer
PAGES.append(page("disclaimer", f"""
<div class='page-head'>
  <div class='page-eyebrow'>合規免責　COMPLIANCE</div>
  <h2 class='page-title'>本報告之使用限制</h2>
</div>
<div class='disclaim-grid'>
  <div class='disclaim-card'>
    <div class='disclaim-icon'>{ICONS['doc']}</div>
    <div class='disclaim-text'>
      <div class='disclaim-title'>分析師工作底稿</div>
      <div class='disclaim-body'>本 Quick Take 為 analyst work product，需經合格專業人員審核後始得對外。</div>
    </div>
  </div>
  <div class='disclaim-card'>
    <div class='disclaim-icon'>{ICONS['shield']}</div>
    <div class='disclaim-text'>
      <div class='disclaim-title'>非投資建議</div>
      <div class='disclaim-body'>內容不構成投資、法律、稅務或會計建議；發布外部須符合適用司法管轄區研究規範。</div>
    </div>
  </div>
  <div class='disclaim-card'>
    <div class='disclaim-icon'>{ICONS['warn']}</div>
    <div class='disclaim-text'>
      <div class='disclaim-title'>數字驗證</div>
      <div class='disclaim-body'>所有標註之具體數字必須以 MOPS／TEJ／Bloomberg 等 primary source 驗證後方可使用。</div>
    </div>
  </div>
  <div class='disclaim-card'>
    <div class='disclaim-icon'>{ICONS['globe']}</div>
    <div class='disclaim-text'>
      <div class='disclaim-title'>適用法規</div>
      <div class='disclaim-body'>台灣 FSC ／ FCA COBS ／ SEC Reg AC ／ FINRA 2241 等同等規定。</div>
    </div>
  </div>
</div>
<div class='disclaim-foot'>© 2026 Finece　·　Confidential analyst work product　·　Generated by Finece global-equity-research plugin</div>
""", 13, 13))

# ---- CSS ----------------------------------------------------------------
CSS_TEXT = """
@page {
  size: A4 landscape;       /* 297mm x 210mm */
  margin: 0;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
html, body {
  font-family: "Noto Sans CJK TC", "Source Han Sans TC", "PingFang TC", sans-serif;
  color: #1f2937;
  font-weight: 400;
}
.page {
  width: 297mm; height: 210mm;
  padding: 12mm 16mm 14mm 16mm;
  page-break-after: always;
  position: relative;
  background: #ffffff;
  overflow: hidden;
}
.icon { display: inline-block; vertical-align: middle; }
.icon svg { display: block; width: 100%; height: 100%; }

/* ---- Footer ---- */
.footer {
  position: absolute;
  bottom: 6mm; left: 16mm; right: 16mm;
  display: flex; justify-content: space-between;
  font-size: 24px; font-weight: 400; color: #94a3b8;
  border-top: 1px solid #e5e7eb; padding-top: 4mm;
}

/* ---- Cover ---- */
.cover { background: linear-gradient(135deg, #1a3a6c 0%, #3b82f6 100%); color: white; padding: 20mm 22mm; }
.cover-deco { position: absolute; right: -30mm; bottom: -30mm; width: 180mm; height: 180mm; opacity: 0.10; }
.cover-deco svg { width: 100%; height: 100%; }
.cover-eyebrow { font-size: 28px; font-weight: 500; letter-spacing: 6px; opacity: 0.85; margin-bottom: 8mm; }
.cover-title { font-size: 130px; font-weight: 900; line-height: 1.0; letter-spacing: -2px; margin-bottom: 6mm; }
.cover-ticker { font-size: 40px; font-weight: 700; opacity: 0.95; margin-bottom: 4mm; }
.cover-tag { font-size: 30px; font-weight: 400; opacity: 0.85; margin-bottom: 16mm; }
.cover-meta { display: flex; gap: 14mm; }
.cover-meta > div { display: flex; flex-direction: column; gap: 2mm; }
.cover-meta .lbl { font-size: 24px; font-weight: 400; opacity: 0.7; letter-spacing: 2px; }
.cover-meta .val { font-size: 28px; font-weight: 700; }
.cover-foot { position: absolute; bottom: 12mm; left: 22mm; font-size: 24px; font-weight: 500; letter-spacing: 4px; opacity: 0.85; }

/* ---- Page head ---- */
.page-head { margin-bottom: 6mm; padding-bottom: 4mm; border-bottom: 3px solid #1a3a6c; }
.page-eyebrow { font-size: 24px; font-weight: 500; letter-spacing: 4px; color: #6b7280; margin-bottom: 3mm; }
.page-title { font-size: 56px; font-weight: 900; color: #1a3a6c; line-height: 1.1; }

/* ---- TOC ---- */
.toc-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 6mm 8mm; margin-top: 3mm; }
.toc-item { display: grid; grid-template-columns: 22mm 22mm 1fr; gap: 5mm; align-items: center; padding: 5mm 6mm; background: #f8fafc; border-radius: 4mm; border-left: 5px solid #1a3a6c; }
.toc-num { font-size: 40px; font-weight: 900; color: #cbd5e1; }
.toc-icon { width: 22mm; height: 22mm; }
.toc-title { font-size: 28px; font-weight: 700; color: #1f2937; margin-bottom: 1mm; }
.toc-sub { font-size: 24px; font-weight: 400; color: #6b7280; }

/* ---- Section divider ---- */
.divider { display: flex; flex-direction: column; justify-content: center; padding: 20mm 28mm; color: white; }
.divider-blue   { background: linear-gradient(135deg, #1a3a6c 0%, #3b82f6 100%); }
.divider-orange { background: linear-gradient(135deg, #92400e 0%, #f59e0b 100%); }
.divider-red    { background: linear-gradient(135deg, #7f1d1d 0%, #ef4444 100%); }
.divider-green  { background: linear-gradient(135deg, #065f46 0%, #10b981 100%); }
.divider-num { font-size: 240px; font-weight: 900; line-height: 1; opacity: 0.20; position: absolute; right: 28mm; top: 24mm; }
.divider-icon { width: 70mm; height: 70mm; opacity: 0.95; margin-bottom: 6mm; }
.divider-icon svg { width: 100%; height: 100%; }
.divider-title { font-size: 96px; font-weight: 900; line-height: 1.0; margin-bottom: 4mm; }
.divider-sub { font-size: 28px; font-weight: 500; opacity: 0.9; }
.divider .footer { color: rgba(255,255,255,0.6); border-top-color: rgba(255,255,255,0.2); }

/* ---- One-liner ---- */
.one-liner { display: grid; grid-template-columns: 30mm 1fr; gap: 6mm; padding: 6mm 7mm; background: #eff6ff; border-radius: 4mm; border-left: 6px solid #1a3a6c; align-items: center; margin-bottom: 6mm; }
.one-liner-icon { width: 30mm; height: 30mm; }
.one-liner-body { font-size: 26px; font-weight: 400; line-height: 1.5; color: #1f2937; }
.one-liner-body b { color: #1a3a6c; font-weight: 700; }

/* ---- KPI row ---- */
.kpi-row { display: grid; grid-template-columns: repeat(4,1fr); gap: 5mm; }
.kpi { background: #f8fafc; border-radius: 4mm; padding: 6mm 4mm; text-align: center; border-bottom: 4px solid #3b82f6; }
.kpi-num { font-size: 60px; font-weight: 900; color: #1a3a6c; line-height: 1.0; margin-bottom: 3mm; white-space: nowrap; }
.kpi-lbl { font-size: 24px; font-weight: 500; color: #6b7280; }

/* ---- 3-card grid ---- */
.cards-3 { display: grid; grid-template-columns: repeat(3,1fr); gap: 5mm; margin-top: 3mm; }
.card { padding: 6mm 7mm; background: #f8fafc; border-radius: 4mm; border-top: 6px solid #f59e0b; position: relative; }
.card-icon { width: 22mm; height: 22mm; margin-bottom: 3mm; }
.card-num { position: absolute; top: 5mm; right: 7mm; font-size: 28px; font-weight: 900; color: #cbd5e1; }
.card-title { font-size: 28px; font-weight: 700; color: #1a3a6c; line-height: 1.2; margin-bottom: 3mm; }
.card-body { font-size: 24px; font-weight: 400; color: #374151; line-height: 1.5; }

/* ---- Risk list ---- */
.risk-list { display: grid; grid-template-columns: 1fr 1fr; gap: 4mm; margin-top: 2mm; }
.risk-item { padding: 5mm 6mm; background: #fef2f2; border-radius: 4mm; border-left: 6px solid #ef4444; page-break-inside: avoid; }
.risk-item.risk-high { background: #fee2e2; border-left-width: 8px; grid-column: 1 / span 2; }
.risk-head { display: flex; gap: 4mm; align-items: center; margin-bottom: 3mm; flex-wrap: wrap; }
.risk-tag { font-size: 24px; font-weight: 700; letter-spacing: 2px; color: white; background: #ef4444; padding: 1mm 3mm; border-radius: 2mm; }
.risk-item.risk-high .risk-tag { background: #991b1b; }
.risk-title { font-size: 28px; font-weight: 700; color: #7f1d1d; }
.risk-item.risk-high .risk-title { font-size: 32px; }
.risk-body { font-size: 24px; font-weight: 400; color: #374151; line-height: 1.5; }

/* ---- Valuation table (HTML table for reliable rendering) ---- */
.val-tbl { width: 100%; border-collapse: separate; border-spacing: 0; margin-top: 3mm; border: 1px solid #e5e7eb; border-radius: 4mm; overflow: hidden; }
.val-tbl thead th { background: #1a3a6c; color: white; font-size: 24px; font-weight: 700; letter-spacing: 2px; padding: 4mm 7mm; text-align: left; }
.val-tbl .th-method { width: 32mm; }
.val-tbl .th-weight { width: 78mm; }
.val-tbl tbody td { padding: 5mm 7mm; border-bottom: 1px solid #e5e7eb; vertical-align: middle; }
.val-tbl tbody tr:last-child td { border-bottom: 0; }
.val-method { font-size: 30px; font-weight: 900; color: #1a3a6c; }
.val-bar { background: #e5e7eb; border-radius: 2mm; height: 8mm; overflow: hidden; display: inline-block; width: 42mm; vertical-align: middle; }
.val-bar-fill { height: 100%; }
.val-pct { font-size: 26px; font-weight: 700; color: #1a3a6c; margin-left: 4mm; vertical-align: middle; }
.val-assume { font-size: 24px; font-weight: 400; color: #374151; line-height: 1.45; }
.val-foot { margin-top: 5mm; padding: 4mm 6mm; background: #f8fafc; border-radius: 3mm; font-size: 26px; font-weight: 500; color: #1a3a6c; text-align: center; }

/* ---- Catalyst table (HTML table for reliable rendering) ---- */
.cat-tbl { width: 100%; border-collapse: separate; border-spacing: 0 3mm; margin-top: 2mm; }
.cat-tbl tr { background: #f8fafc; }
.cat-tbl tr.cat-highlight { background: #fef3c7; }
.cat-tbl td { padding: 5mm 4mm; vertical-align: middle; border-top: 1px solid #f8fafc; border-bottom: 1px solid #f8fafc; }
.cat-tbl tr.cat-highlight td { border-color: #fef3c7; }
.cat-tbl td:first-child { padding-left: 6mm; border-left: 1px solid #f8fafc; border-top-left-radius: 3mm; border-bottom-left-radius: 3mm; }
.cat-tbl td:last-child { padding-right: 6mm; border-right: 1px solid #f8fafc; border-top-right-radius: 3mm; border-bottom-right-radius: 3mm; }
.cat-tbl tr.cat-highlight td:first-child { border-left: 5px solid #f59e0b; padding-left: 4mm; }
.cat-date { font-size: 24px; font-weight: 700; color: #1a3a6c; white-space: nowrap; width: 38mm; }
.cat-dot { width: 14mm; }
.cat-dot span { display: inline-block; width: 10mm; height: 10mm; border-radius: 50%; }
.cat-title { font-size: 26px; font-weight: 700; color: #1f2937; }
.cat-stars { font-size: 24px; color: #94a3b8; white-space: nowrap; padding: 0 6mm; }
.cat-note { font-size: 24px; font-weight: 400; color: #6b7280; }

/* ---- Conclusion ---- */
.conclusion-block { display: grid; grid-template-columns: 95mm 1fr; gap: 8mm; margin-top: 3mm; }
.rating-card { background: linear-gradient(135deg, #065f46 0%, #10b981 100%); color: white; border-radius: 6mm; padding: 8mm 6mm; text-align: center; }
.rating-icon { width: 28mm; height: 28mm; margin: 0 auto 3mm auto; }
.rating-eyebrow { font-size: 24px; font-weight: 500; letter-spacing: 4px; opacity: 0.85; margin-bottom: 2mm; }
.rating-main { font-size: 88px; font-weight: 900; line-height: 1.0; margin-bottom: 3mm; }
.rating-sub { font-size: 24px; font-weight: 400; opacity: 0.85; }
.actions { padding: 4mm 6mm; }
.action-title { font-size: 30px; font-weight: 700; color: #1a3a6c; margin-bottom: 5mm; padding-bottom: 3mm; border-bottom: 2px solid #e5e7eb; }
.action-list { display: flex; flex-direction: column; gap: 4mm; }
.action-item { display: grid; grid-template-columns: 14mm 1fr; gap: 4mm; align-items: start; font-size: 24px; font-weight: 400; color: #374151; line-height: 1.5; }
.action-item b { color: #1a3a6c; font-weight: 700; }
.action-num { width: 12mm; height: 12mm; border-radius: 50%; background: #1a3a6c; color: white; font-size: 24px; font-weight: 900; text-align: center; line-height: 12mm; }

/* ---- Disclaimer (flex-based to avoid weasyprint nested-grid sizing bug) ---- */
.disclaim-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 5mm; }
.disclaim-card {
  padding: 6mm; background: #f8fafc; border-radius: 4mm;
  border-left: 5px solid #6b7280;
  display: flex; flex-direction: row; align-items: flex-start; gap: 5mm;
  page-break-inside: avoid;
}
.disclaim-icon { flex: 0 0 22mm; width: 22mm; height: 22mm; }
.disclaim-text { flex: 1 1 0; min-width: 0; }
.disclaim-title { font-size: 28px; font-weight: 700; color: #1a3a6c; margin-bottom: 2mm; }
.disclaim-body { font-size: 24px; font-weight: 400; color: #374151; line-height: 1.45; }
.disclaim-foot { position: absolute; bottom: 12mm; left: 16mm; right: 16mm; text-align: center; font-size: 24px; font-weight: 400; color: #94a3b8; padding-top: 4mm; border-top: 1px solid #e5e7eb; }
.disclaimer .footer { display: none; }
"""

html_doc = f"""<!DOCTYPE html><html lang='zh-TW'><head><meta charset='utf-8'><title>5274 Quick Take Deck</title></head>
<body>{''.join(PAGES)}</body></html>"""

HTML(string=html_doc).write_pdf(
    str(OUT),
    stylesheets=[CSS(string=CSS_TEXT)],
    optimize_size=(),
)
print(f"Wrote {OUT}")
