import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('c:/Users/acarcamo/Desktop/WEBS/Anuario SCIA/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

changes = []

# ════════════════════════════════════════════════════════════════
# 1. CSS — Visual impact improvements block
# ════════════════════════════════════════════════════════════════
AUDIT_CSS = """
/* ══════════════════════════════════════════════════════════════
   AUDIT V1 — Dynamic & Impact Visual Improvements
══════════════════════════════════════════════════════════════ */

/* ── SECTION DECORATIVE NUMBER ─────────────────────────────── */
.sec-deco-num {
  position: absolute;
  top: 2.5rem; right: 2.5rem;
  font-family: 'Manrope', sans-serif;
  font-weight: 800;
  font-size: clamp(5rem, 12vw, 9rem);
  line-height: 1;
  letter-spacing: -0.06em;
  pointer-events: none;
  user-select: none;
  z-index: 0;
  background: linear-gradient(135deg, var(--blue) 0%, var(--purple) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  opacity: 0.042;
  font-variant-numeric: tabular-nums;
}
.sec-dark .sec-deco-num,
.sec-mid  .sec-deco-num {
  opacity: 0.10;
  background: linear-gradient(135deg, rgba(221,239,251,.9), rgba(155,89,182,.6));
  -webkit-background-clip: text;
  background-clip: text;
}

/* ── KPI CARD TOP ACCENT STRIPE ────────────────────────────── */
.kpi-white {
  position: relative; overflow: hidden;
}
.kpi-white::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3px;
  border-radius: var(--r-xl) var(--r-xl) 0 0;
  background: linear-gradient(90deg, var(--blue), var(--purple));
  opacity: 0.55;
  pointer-events: none;
  z-index: 1;
}
.kpi-glass::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 2px;
  border-radius: var(--r-xl) var(--r-xl) 0 0;
  background: linear-gradient(90deg, rgba(221,239,251,.65), rgba(155,89,182,.45));
  pointer-events: none;
  z-index: 1;
}
.kpi-fin::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 2px;
  border-radius: var(--r-xl) var(--r-xl) 0 0;
  background: linear-gradient(90deg, rgba(221,239,251,.5), rgba(155,89,182,.35));
  pointer-events: none;
  z-index: 1;
}

/* ── KPI NUM — bolder for impact ───────────────────────────── */
.kpi-num {
  font-weight: 800 !important;
  letter-spacing: -0.025em;
}
.kpi-num-light {
  text-shadow: 0 0 48px rgba(100,120,220,.35);
}

/* ── KPI HOVER — more pronounced lift ─────────────────────── */
.kpi-white {
  transition: transform .28s var(--spring), box-shadow .28s var(--smooth) !important;
}
.kpi-white:hover {
  transform: translateY(-6px) scale(1.012) !important;
  box-shadow:
    0 1px 0 rgba(255,255,255,.95) inset,
    0 24px 56px rgba(46,49,146,.18),
    0 6px 20px rgba(46,49,146,.10),
    0 0 0 1.5px rgba(46,49,146,.07) !important;
}
.kpi-glass:hover {
  transform: translateY(-5px) scale(1.01) !important;
  box-shadow:
    0 1px 0 rgba(255,255,255,.22) inset,
    0 24px 56px rgba(0,0,0,.38),
    0 6px 20px rgba(0,0,0,.22) !important;
}

/* ── INSIGHT BLOCK — left accent border redesign ───────────── */
.insight {
  position: relative;
  border-left: 3px solid var(--blue) !important;
  border-left-color: var(--blue) !important;
  padding: 1.1rem 1.4rem 1.1rem 1.5rem !important;
  border-radius: 0 var(--r-md) var(--r-md) 0 !important;
  background: linear-gradient(135deg,
    rgba(46,49,146,.055),
    rgba(122,56,139,.025)) !important;
}
.insight-light {
  border-left-color: rgba(221,239,251,.65) !important;
  background: linear-gradient(135deg,
    rgba(255,255,255,.08),
    rgba(155,89,182,.05)) !important;
}
.insight-hdr {
  font-weight: 700 !important;
  letter-spacing: .02em !important;
  margin-bottom: .55rem !important;
}
.insight-hdr .material-symbols-outlined {
  font-size: 1rem !important;
}

/* ── SECTION TAG — slightly bigger ────────────────────────── */
.sec-tag {
  font-size: .72rem !important;
  padding: .38rem 1rem .38rem .7rem !important;
  margin-bottom: 1rem !important;
  box-shadow: 0 2px 12px rgba(46,49,146,.08) !important;
}

/* ── SECTION TITLE — larger ────────────────────────────────── */
.sec-title {
  font-size: clamp(2rem, 4.5vw, 3.2rem) !important;
}

/* ── DIVIDER — wider, more visible ─────────────────────────── */
.divider {
  width: 64px !important;
  max-width: 64px !important;
  height: 2.5px !important;
  margin-top: .6rem !important;
  margin-bottom: 1.5rem !important;
  opacity: .9 !important;
  border-radius: 9999px !important;
}

/* ── CHART BOX — hover lift ─────────────────────────────────── */
.chart-box {
  transition: transform .28s var(--spring), box-shadow .28s var(--smooth) !important;
}
.chart-box:hover {
  transform: translateY(-3px) !important;
  box-shadow:
    0 1px 0 rgba(255,255,255,.95) inset,
    0 28px 60px rgba(46,49,146,.15),
    0 4px 16px rgba(46,49,146,.08) !important;
}
.chart-box-dark:hover {
  transform: translateY(-3px) !important;
  box-shadow:
    0 1px 0 rgba(255,255,255,.18) inset,
    0 24px 52px rgba(0,0,0,.40) !important;
}

/* ── TIMELINE — grid layout (2–3 columns) ──────────────────── */
.tl-wrap {
  display: grid !important;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)) !important;
  gap: 1rem !important;
  position: relative !important;
}
.tl-dot { display: none !important; }
.tl-item {
  padding-left: 0 !important;
  border-left: none !important;
  position: relative;
}
.tl-item > div {
  height: 100% !important;
  display: flex !important;
  flex-direction: column !important;
  border-top: 3px solid !important;
  border-image: linear-gradient(90deg, var(--blue), var(--purple)) 1 !important;
  border-radius: 0 0 .85rem .85rem !important;
  transition: transform .25s var(--spring), box-shadow .25s var(--smooth) !important;
}
.tl-item > div:hover {
  transform: translateY(-4px) !important;
  box-shadow:
    0 1px 0 rgba(255,255,255,.98) inset,
    0 20px 48px rgba(46,49,146,.14),
    0 4px 16px rgba(46,49,146,.08) !important;
}

/* ── SECTION BG SUBTLE GRID TEXTURE ────────────────────────── */
.sec-light::after,
.sec-tinted::after {
  content: '';
  position: absolute;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  background-image:
    radial-gradient(circle, rgba(46,49,146,.038) 1.2px, transparent 1.2px);
  background-size: 30px 30px;
  mask-image: radial-gradient(ellipse 80% 90% at 50% 50%, black 30%, transparent 100%);
  -webkit-mask-image: radial-gradient(ellipse 80% 90% at 50% 50%, black 30%, transparent 100%);
}

/* ── REVEAL animation — more travel ────────────────────────── */
.reveal {
  opacity: 0;
  transform: translateY(22px);
  transition: opacity .7s var(--ease-out), transform .7s var(--ease-out) !important;
}
.reveal.visible {
  opacity: 1 !important;
  transform: translateY(0) !important;
}
.reveal-d1.visible { transition-delay: .1s !important; }
.reveal-d2.visible { transition-delay: .2s !important; }
.reveal-d3.visible { transition-delay: .3s !important; }

/* ── NAVBAR — year selector alignment ──────────────────────── */
#navbar { gap: 1rem !important; }

/* ── FOOTER blobs ───────────────────────────────────────────── */
.kpi-fin {
  transition: transform .28s var(--spring), box-shadow .28s var(--smooth) !important;
}
.kpi-fin:hover {
  transform: translateY(-5px) scale(1.01) !important;
}
"""

OLD_STYLE_CLOSE = '</style>\n<script src="https://cdn.tailwindcss.com">'
NEW_STYLE_CLOSE = AUDIT_CSS + '</style>\n<script src="https://cdn.tailwindcss.com">'

if OLD_STYLE_CLOSE in html:
    html = html.replace(OLD_STYLE_CLOSE, NEW_STYLE_CLOSE, 1)
    changes.append('CSS: full audit improvements block')
else:
    changes.append('SKIP CSS anchor not found')

# ════════════════════════════════════════════════════════════════
# 2. HTML — Section decorative numbers (02–08)
# ════════════════════════════════════════════════════════════════
section_nums = [
    # (search_anchor, section_number)
    (
        '<span class="material-symbols-outlined">assignment_turned_in</span>\n      Concursos 2024',
        '02',
    ),
    (
        '<span class="material-symbols-outlined">payments</span>\n      Ejecución presupuestaria',
        '03',
    ),
    (
        '<span class="material-symbols-outlined">menu_book</span>',
        '04',
    ),
    (
        '<span class="material-symbols-outlined">groups</span>\n      Equipo investigador',
        '05',
    ),
    (
        '<span class="material-symbols-outlined">diversity_3</span>\n      Paridad e inclusión',
        '06',
    ),
    (
        '<span class="material-symbols-outlined">map</span>\n      Distribución geográfica',
        '07',
    ),
    (
        '<span class="material-symbols-outlined">hub</span>\n      Impacto y transferencia',
        '08',
    ),
]

for anchor, num in section_nums:
    if anchor in html:
        html = html.replace(anchor, f'<div class="sec-deco-num">{num}</div>\n    ' + anchor.split('\n')[0] + ('\n' + '\n'.join(anchor.split('\n')[1:]) if '\n' in anchor else ''), 1)
        changes.append(f'HTML: sec-deco-num {num} added')
    else:
        changes.append(f'SKIP sec-deco-num {num}: anchor not found')

# ════════════════════════════════════════════════════════════════
# 3. JS — Gestión chart data labels plugin (before initChart call)
# ════════════════════════════════════════════════════════════════
GESTION_PLUGIN = """
// ── GESTIÓN CHART — Direct value labels on bars ───────────────
const gestionLabelPlugin = {
  id: 'gestionLabels',
  afterDatasetsDraw(chart) {
    if (chart.canvas.id !== 'chartGestion') return;
    const { ctx } = chart;
    const meta = chart.getDatasetMeta(0);
    chart.data.datasets[0].data.forEach(function(value, i) {
      if (!value) return;
      const bar = meta.data[i];
      if (!bar) return;
      const barWidth = bar.x - bar.base;
      const formatted = value >= 1000000
        ? 'M$' + (value / 1000000).toFixed(1) + 'M'
        : 'M$' + (value / 1000).toFixed(0) + 'k';
      const inside = barWidth > 90;
      const labelX = inside ? bar.x - 7 : bar.x + 7;
      const align  = inside ? 'right' : 'left';
      const color  = inside ? 'rgba(255,255,255,0.88)' : 'rgba(100,116,139,0.9)';
      ctx.save();
      ctx.font = "600 8.5px 'Inter', sans-serif";
      ctx.fillStyle = color;
      ctx.textAlign = align;
      ctx.textBaseline = 'middle';
      ctx.fillText(formatted, labelX, bar.y);
      ctx.restore();
    });
  }
};
Chart.register(gestionLabelPlugin);

"""

OLD_GESTION_INIT = "// ── GESTIÓN HORIZONTAL BAR ─────────────────────"
NEW_GESTION_INIT = GESTION_PLUGIN + "// ── GESTIÓN HORIZONTAL BAR ─────────────────────"

if OLD_GESTION_INIT in html:
    html = html.replace(OLD_GESTION_INIT, NEW_GESTION_INIT, 1)
    changes.append('JS: Gestión chart data labels plugin registered')
else:
    changes.append('SKIP Gestión label plugin anchor not found')

# ════════════════════════════════════════════════════════════════
# 4. HTML — Enhance the timeline section header
# ════════════════════════════════════════════════════════════════
OLD_TL_HEADER = '''      <h3 style="font-family:'Manrope',sans-serif;font-weight:800;font-size:1.1rem;color:var(--navy);margin-bottom:1.5rem;">
        <span class="material-symbols-outlined" style="color:var(--blue);">timeline</span>
        Hitos de Vinculación 2024
      </h3>'''

NEW_TL_HEADER = '''      <div style="display:flex;align-items:center;gap:1rem;margin-bottom:1.5rem;flex-wrap:wrap;">
        <h3 style="font-family:'Manrope',sans-serif;font-weight:800;font-size:1.25rem;color:var(--navy);display:flex;align-items:center;gap:.5rem;margin:0;">
          <span style="width:34px;height:34px;border-radius:.75rem;background:linear-gradient(135deg,var(--blue),var(--purple));display:inline-flex;align-items:center;justify-content:center;flex-shrink:0;">
            <span class="material-symbols-outlined" style="color:white;font-size:1rem;">timeline</span>
          </span>
          Hitos de Vinculación 2024
        </h3>
        <span style="font-size:.68rem;font-weight:700;color:var(--muted);background:rgba(46,49,146,.07);border:1px solid rgba(46,49,146,.12);padding:.2rem .65rem;border-radius:9999px;letter-spacing:.06em;">6 EVENTOS</span>
      </div>'''

if OLD_TL_HEADER in html:
    html = html.replace(OLD_TL_HEADER, NEW_TL_HEADER, 1)
    changes.append('HTML: timeline header redesigned')
else:
    changes.append('SKIP timeline header not found')

# ════════════════════════════════════════════════════════════════
# 5. HTML — Hallazgos científicos section header upgrade
# ════════════════════════════════════════════════════════════════
OLD_HALLAZGOS = '''      <h3 style="font-family:'Manrope',sans-serif;font-weight:800;font-size:1.3rem;color:var(--navy);margin-bottom:1.5rem;">
        <span class="material-symbols-outlined" style="color:var(--purple);">biotech</span>
        Hallazgos Científicos Destacados 2024
      </h3>'''

NEW_HALLAZGOS = '''      <div style="display:flex;align-items:center;gap:1rem;margin-bottom:1.75rem;flex-wrap:wrap;">
        <h3 style="font-family:'Manrope',sans-serif;font-weight:800;font-size:1.25rem;color:var(--navy);display:flex;align-items:center;gap:.55rem;margin:0;">
          <span style="width:34px;height:34px;border-radius:.75rem;background:linear-gradient(135deg,var(--purple),#9B6EBF);display:inline-flex;align-items:center;justify-content:center;flex-shrink:0;">
            <span class="material-symbols-outlined" style="color:white;font-size:1rem;">biotech</span>
          </span>
          Hallazgos Científicos Destacados 2024
        </h3>
        <span style="font-size:.68rem;font-weight:700;color:var(--purple);background:rgba(122,56,139,.08);border:1px solid rgba(122,56,139,.18);padding:.2rem .65rem;border-radius:9999px;letter-spacing:.06em;">3 SELECCIONADOS</span>
      </div>'''

if OLD_HALLAZGOS in html:
    html = html.replace(OLD_HALLAZGOS, NEW_HALLAZGOS, 1)
    changes.append('HTML: Hallazgos científicos header upgraded')
else:
    changes.append('SKIP Hallazgos header not found')

# ════════════════════════════════════════════════════════════════
# 6. JS — Tesis chart direct labels (stacked total at top of bar)
# ════════════════════════════════════════════════════════════════
TESIS_LABEL_PLUGIN = """
// ── STACKED BAR TOTAL LABELS plugin ─────────────────────────────
const stackedTotalPlugin = {
  id: 'stackedTotals',
  afterDatasetsDraw(chart) {
    const allowedIds = ['chartTesis', 'chartCongresos'];
    if (!allowedIds.includes(chart.canvas.id)) return;
    const { ctx, data } = chart;
    const nDatasets = data.datasets.length;
    const nPoints   = data.datasets[0].data.length;
    for (let i = 0; i < nPoints; i++) {
      let total = 0;
      for (let d = 0; d < nDatasets; d++) total += (data.datasets[d].data[i] || 0);
      const lastMeta = chart.getDatasetMeta(nDatasets - 1);
      const bar = lastMeta.data[i];
      if (!bar) continue;
      ctx.save();
      ctx.font = "700 9px 'Manrope', sans-serif";
      ctx.fillStyle = 'rgba(71,85,105,0.85)';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'bottom';
      ctx.fillText(total.toLocaleString('es-CL'), bar.x, bar.y - 4);
      ctx.restore();
    }
  }
};
Chart.register(stackedTotalPlugin);

"""

OLD_TESIS_ANCHOR = "// ── TESIS ──────────────────────────────────────"
NEW_TESIS_ANCHOR = TESIS_LABEL_PLUGIN + "// ── TESIS ──────────────────────────────────────"

if OLD_TESIS_ANCHOR in html:
    html = html.replace(OLD_TESIS_ANCHOR, NEW_TESIS_ANCHOR, 1)
    changes.append('JS: stackedTotals plugin for Tesis/Congresos charts')
else:
    changes.append('SKIP stackedTotals anchor not found')

# ════════════════════════════════════════════════════════════════
# 7. HTML — UVE dimension cards upgrade
# ════════════════════════════════════════════════════════════════
# Upgrade the UVE dimension section title
OLD_UVE_DIM = '''    <!-- UVE Dimensions -->'''
NEW_UVE_DIM = '''    <!-- UVE Dimensions -->'''
# (Keep existing — it already has dimension cards)

# ════════════════════════════════════════════════════════════════
# 8. HTML — Postulacion section: add badge count to KPI detail
# ════════════════════════════════════════════════════════════════
# Already has gender badges — no change needed

# ════════════════════════════════════════════════════════════════
# 9. JS — Section number staggered fade-in animation
# ════════════════════════════════════════════════════════════════
SEC_NUM_ANIM_CSS = """
/* ── SEC-DECO-NUM entrance animation ────────────────────────── */
@keyframes decoNumIn {
  0%   { opacity: 0; transform: translateX(20px) scale(0.92); }
  100% { opacity: 0.042; transform: translateX(0) scale(1); }
}
.sec-deco-num {
  animation: decoNumIn 1.2s var(--ease-out) forwards;
}
.sec-dark .sec-deco-num,
.sec-mid  .sec-deco-num {
  animation: decoNumIn 1.2s var(--ease-out) forwards;
  opacity: 0.10;
}
"""

OLD_TW_SCRIPT = '<script src="https://cdn.tailwindcss.com"></script>'
NEW_TW_SCRIPT = '<script src="https://cdn.tailwindcss.com"></script>\n<style>' + SEC_NUM_ANIM_CSS + '</style>'

if OLD_TW_SCRIPT in html:
    html = html.replace(OLD_TW_SCRIPT, NEW_TW_SCRIPT, 1)
    changes.append('CSS: sec-deco-num entrance animation')
else:
    changes.append('SKIP tailwind script anchor not found')

# ════════════════════════════════════════════════════════════════
# Save
# ════════════════════════════════════════════════════════════════
with open('c:/Users/acarcamo/Desktop/WEBS/Anuario SCIA/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'audit_v1 — {len(changes)} changes:')
for c in changes:
    print(f'  {"--" if "SKIP" in c else "OK"} {c}')

import os
size = os.path.getsize('c:/Users/acarcamo/Desktop/WEBS/Anuario SCIA/index.html')
content = open('c:/Users/acarcamo/Desktop/WEBS/Anuario SCIA/index.html', encoding='utf-8').read()
opens  = content.count('<div')
closes = content.count('</div>')
print(f'\nBalance: {opens}/{closes} ({opens-closes}) | Size: {size//1024} KB')
