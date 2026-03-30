import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('c:/Users/acarcamo/Desktop/WEBS/Anuario SCIA/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

changes = []

# ═══════════════════════════════════════════════════════════════
# HERO — REDISEÑO COMPLETO
# Problemas: donut pequeño (260px), insight dentro del chart-box
# comprime el canvas, layout 1fr 1fr desbalanceado
# ═══════════════════════════════════════════════════════════════

OLD_HERO_CHART = '''    <!-- Donut chart + note -->
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:2rem;align-items:center;" class="reveal">
      <div class="chart-box-dark">
        <div class="chart-hdr">
          <div><div class="chart-ttl chart-ttl-light"><span class="material-symbols-outlined">donut_large</span> Distribución por Instrumento</div><div class="chart-sub" style="color:rgba(221,239,251,.4);">Datos 2024 · SCIA</div></div>
          <span class="chart-badge" style="background:rgba(255,255,255,.08);color:rgba(221,239,251,.7);border-color:rgba(255,255,255,.15);">SCIA 2024</span>
        </div>
        <div class="chart-body">
          <canvas id="chartHeroDonut" style="max-height:260px;"></canvas>
          <div class="insight insight-light reveal">
            <div class="insight-hdr">
              <span class="material-symbols-outlined">emoji_objects</span>
              <span class="insight-label">Lectura clave</span>
            </div>
            <p>El <strong>76,5% del total</strong> se concentra en solo 3 instrumentos (Equipamiento Mediano, Anillos, Núcleos Milenio), lo que refleja una cartera dominada por proyectos de infraestructura y redes colaborativas de mediana escala. Esta concentración sugiere <strong>alta dependencia de concursos competitivos</strong> y menor participación de centros de largo aliento en el conteo total.</p>
          </div>
          <p class="data-cap" style="color:rgba(221,239,251,.5);">
            <span class="material-symbols-outlined" style="font-size:0.85em;">source</span>
            Fuente: DB Proyectos SCIA 26.06
          </p>
        </div>
      </div>
      <div>
        <div style="display:flex;flex-direction:column;gap:1rem;">
          <!-- Instrumento rows mejorados con progress bars -->
          <style>
          .instr-row { display:flex; flex-direction:column; gap:.3rem; padding:.85rem 1rem; background:rgba(255,255,255,.065); border-radius:.9rem; border:1px solid rgba(255,255,255,.1); backdrop-filter:blur(8px); transition:background .2s; }
          .instr-row:hover { background:rgba(255,255,255,.1); }
          .instr-top { display:flex; justify-content:space-between; align-items:center; }
          .instr-bar { height:3px; border-radius:9999px; background:rgba(255,255,255,.12); overflow:hidden; margin-top:.3rem; }
          .instr-fill { height:100%; border-radius:9999px; transition:width 1.5s cubic-bezier(0,0,.2,1); width:0; }
          </style>
          <div class="instr-row" data-fill="42.5" data-color="#DDEFFB">
            <div class="instr-top">
              <div style="display:flex;align-items:center;gap:.6rem;">
                <div style="width:10px;height:10px;border-radius:3px;background:#DDEFFB;flex-shrink:0;"></div>
                <span style="font-size:.8rem;color:rgba(221,239,251,.88);font-weight:500;">Equipamiento Mediano</span>
              </div>
              <div style="display:flex;align-items:center;gap:.5rem;">
                <span style="font-size:.7rem;color:rgba(221,239,251,.45);">42,5%</span>
                <span style="font-size:1.15rem;font-family:'Manrope',sans-serif;font-weight:800;color:var(--light);">201</span>
              </div>
            </div>
            <div class="instr-bar"><div class="instr-fill" style="background:linear-gradient(90deg,rgba(221,239,251,.7),rgba(221,239,251,.3));"></div></div>
          </div>
          <div class="instr-row" data-fill="22.8" data-color="#7A388B">
            <div class="instr-top">
              <div style="display:flex;align-items:center;gap:.6rem;">
                <div style="width:10px;height:10px;border-radius:3px;background:#9B59B6;flex-shrink:0;"></div>
                <span style="font-size:.8rem;color:rgba(221,239,251,.88);font-weight:500;">Anillos de Investigación</span>
              </div>
              <div style="display:flex;align-items:center;gap:.5rem;">
                <span style="font-size:.7rem;color:rgba(221,239,251,.45);">22,8%</span>
                <span style="font-size:1.15rem;font-family:'Manrope',sans-serif;font-weight:800;color:var(--light);">108</span>
              </div>
            </div>
            <div class="instr-bar"><div class="instr-fill" style="background:linear-gradient(90deg,rgba(122,56,139,.9),rgba(122,56,139,.4));"></div></div>
          </div>
          <div class="instr-row" data-fill="11.2" data-color="#4A5CC7">
            <div class="instr-top">
              <div style="display:flex;align-items:center;gap:.6rem;">
                <div style="width:10px;height:10px;border-radius:3px;background:#4A5CC7;flex-shrink:0;"></div>
                <span style="font-size:.8rem;color:rgba(221,239,251,.88);font-weight:500;">Núcleos Milenio</span>
              </div>
              <div style="display:flex;align-items:center;gap:.5rem;">
                <span style="font-size:.7rem;color:rgba(221,239,251,.45);">11,2%</span>
                <span style="font-size:1.15rem;font-family:'Manrope',sans-serif;font-weight:800;color:var(--light);">53</span>
              </div>
            </div>
            <div class="instr-bar"><div class="instr-fill" style="background:linear-gradient(90deg,rgba(74,92,199,.9),rgba(74,92,199,.4));"></div></div>
          </div>
          <div class="instr-row" data-fill="23.5" data-color="#6b7280">
            <div class="instr-top">
              <div style="display:flex;align-items:center;gap:.6rem;">
                <div style="width:10px;height:10px;border-radius:3px;background:rgba(255,255,255,.35);flex-shrink:0;"></div>
                <span style="font-size:.8rem;color:rgba(221,239,251,.88);font-weight:500;">Resto de instrumentos</span>
              </div>
              <div style="display:flex;align-items:center;gap:.5rem;">
                <span style="font-size:.7rem;color:rgba(221,239,251,.45);">23,5%</span>
                <span style="font-size:1.15rem;font-family:'Manrope',sans-serif;font-weight:800;color:var(--light);">111</span>
              </div>
            </div>
            <div class="instr-bar"><div class="instr-fill" style="background:linear-gradient(90deg,rgba(255,255,255,.4),rgba(255,255,255,.15));"></div></div>
          </div>
        </div>
      </div>
    </div>'''

NEW_HERO_CHART = '''    <!-- Donut chart + instrument rows — layout 3:2 -->
    <div style="display:grid;grid-template-columns:3fr 2fr;gap:2rem;align-items:start;" class="reveal">
      <!-- Donut: sin insight adentro para que el canvas respire -->
      <div class="chart-box-dark">
        <div class="chart-hdr">
          <div>
            <div class="chart-ttl chart-ttl-light"><span class="material-symbols-outlined">donut_large</span> Distribución por Instrumento</div>
            <div class="chart-sub" style="color:rgba(221,239,251,.4);">473 iniciativas vigentes · 2024</div>
          </div>
          <span class="chart-badge" style="background:rgba(255,255,255,.08);color:rgba(221,239,251,.7);border-color:rgba(255,255,255,.15);">SCIA 2024</span>
        </div>
        <div class="chart-body" style="padding-top:.5rem;">
          <canvas id="chartHeroDonut" style="height:300px;max-height:300px;"></canvas>
          <p class="data-cap" style="color:rgba(221,239,251,.4);margin-top:.75rem;">
            <span class="material-symbols-outlined" style="font-size:0.85em;">source</span>
            Fuente: DB Proyectos SCIA 26.06
          </p>
        </div>
      </div>

      <!-- Instrument rows — rediseñados: más grandes y legibles -->
      <div style="display:flex;flex-direction:column;gap:0;">
        <div style="font-size:.62rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:rgba(221,239,251,.35);margin-bottom:.85rem;">
          Iniciativas por instrumento
        </div>
        <style>
        .instr-row { display:flex; flex-direction:column; gap:.4rem; padding:1rem 1.1rem; background:rgba(255,255,255,.06); border-radius:1rem; border:1px solid rgba(255,255,255,.09); backdrop-filter:blur(8px); transition:background .22s, transform .22s; cursor:default; }
        .instr-row + .instr-row { margin-top:.6rem; }
        .instr-row:hover { background:rgba(255,255,255,.1); transform:translateX(4px); }
        .instr-top { display:flex; justify-content:space-between; align-items:center; }
        .instr-bar { height:4px; border-radius:9999px; background:rgba(255,255,255,.1); overflow:hidden; }
        .instr-fill { height:100%; border-radius:9999px; transition:width 1.6s cubic-bezier(0,0,.2,1); width:0; }
        .instr-num { font-size:1.5rem; font-family:'Manrope',sans-serif; font-weight:800; color:var(--light); line-height:1; }
        .instr-pct { font-size:.7rem; color:rgba(221,239,251,.45); font-weight:500; }
        .instr-name { font-size:.82rem; color:rgba(221,239,251,.82); font-weight:500; }
        </style>

        <div class="instr-row" data-fill="42.5">
          <div class="instr-top">
            <div style="display:flex;align-items:center;gap:.55rem;">
              <div style="width:8px;height:28px;border-radius:4px;background:linear-gradient(to bottom,rgba(221,239,251,.9),rgba(221,239,251,.4));flex-shrink:0;"></div>
              <div>
                <div class="instr-name">Equipamiento Mediano</div>
                <div class="instr-pct">42,5% del total</div>
              </div>
            </div>
            <div class="instr-num">201</div>
          </div>
          <div class="instr-bar"><div class="instr-fill" style="background:linear-gradient(90deg,rgba(221,239,251,.75),rgba(221,239,251,.25));"></div></div>
        </div>

        <div class="instr-row" data-fill="22.8">
          <div class="instr-top">
            <div style="display:flex;align-items:center;gap:.55rem;">
              <div style="width:8px;height:28px;border-radius:4px;background:linear-gradient(to bottom,rgba(155,89,182,.95),rgba(122,56,139,.5));flex-shrink:0;"></div>
              <div>
                <div class="instr-name">Anillos de Investigación</div>
                <div class="instr-pct">22,8% del total</div>
              </div>
            </div>
            <div class="instr-num">108</div>
          </div>
          <div class="instr-bar"><div class="instr-fill" style="background:linear-gradient(90deg,rgba(155,89,182,.85),rgba(122,56,139,.35));"></div></div>
        </div>

        <div class="instr-row" data-fill="11.2">
          <div class="instr-top">
            <div style="display:flex;align-items:center;gap:.55rem;">
              <div style="width:8px;height:28px;border-radius:4px;background:linear-gradient(to bottom,rgba(74,92,199,.95),rgba(46,49,146,.5));flex-shrink:0;"></div>
              <div>
                <div class="instr-name">Núcleos Milenio</div>
                <div class="instr-pct">11,2% del total</div>
              </div>
            </div>
            <div class="instr-num">53</div>
          </div>
          <div class="instr-bar"><div class="instr-fill" style="background:linear-gradient(90deg,rgba(74,92,199,.85),rgba(46,49,146,.3));"></div></div>
        </div>

        <div class="instr-row" data-fill="23.5">
          <div class="instr-top">
            <div style="display:flex;align-items:center;gap:.55rem;">
              <div style="width:8px;height:28px;border-radius:4px;background:linear-gradient(to bottom,rgba(255,255,255,.38),rgba(255,255,255,.12));flex-shrink:0;"></div>
              <div>
                <div class="instr-name">Otros instrumentos</div>
                <div class="instr-pct">23,5% del total</div>
              </div>
            </div>
            <div class="instr-num">111</div>
          </div>
          <div class="instr-bar"><div class="instr-fill" style="background:linear-gradient(90deg,rgba(255,255,255,.38),rgba(255,255,255,.1));"></div></div>
        </div>
      </div>
    </div>

    <!-- Insight full-width debajo del grid -->
    <div class="insight insight-light reveal" style="margin-top:1.75rem;">
      <div class="insight-hdr">
        <span class="material-symbols-outlined">emoji_objects</span>
        <span class="insight-label">Lectura clave · Concentración de cartera</span>
      </div>
      <p>El <strong>76,5% del total</strong> se concentra en solo 3 instrumentos (Equipamiento Mediano, Anillos, Núcleos Milenio), reflejando una cartera dominada por proyectos de mediana escala y redes colaborativas. Esta concentración sugiere <strong>alta dependencia de concursos competitivos</strong> y menor peso relativo de los centros de largo aliento en el conteo total de iniciativas.</p>
    </div>'''

if OLD_HERO_CHART in html:
    html = html.replace(OLD_HERO_CHART, NEW_HERO_CHART, 1)
    changes.append('Hero: layout 3:2, donut 300px, insight full-width, instr-rows rediseñadas')
else:
    changes.append('SKIP Hero (no match)')

# ═══════════════════════════════════════════════════════════════
# PIRÁMIDE — Reemplazar custom HTML con Chart.js butterfly
# ═══════════════════════════════════════════════════════════════

# 1. HTML: reemplazar el contenido interno del chart-body de la pirámide
OLD_PYRAMID_HTML = '''        <div style="display:flex;justify-content:center;gap:2rem;font-size:.7rem;color:rgba(221,239,251,.6);margin-bottom:1rem;">
          <span>← <span style="background:rgba(122,56,139,.7);padding:.1rem .4rem;border-radius:4px;color:white;">Mujeres</span></span>
          <span style="font-family:'Manrope',sans-serif;font-weight:700;color:rgba(221,239,251,.5);">Tramo</span>
          <span><span style="background:rgba(46,49,146,.7);padding:.1rem .4rem;border-radius:4px;color:white;">Hombres</span> →</span>
        </div>
        <div id="pyramid" style="max-width:600px;margin:0 auto;"></div>'''
NEW_PYRAMID_HTML = '''        <!-- Leyenda compacta -->
        <div style="display:flex;justify-content:center;align-items:center;gap:1.5rem;font-size:.72rem;color:rgba(221,239,251,.65);margin-bottom:1rem;">
          <span style="display:flex;align-items:center;gap:.4rem;"><span style="width:12px;height:12px;border-radius:3px;background:rgba(155,90,191,.9);display:inline-block;"></span> Mujeres</span>
          <span style="display:flex;align-items:center;gap:.4rem;"><span style="width:12px;height:12px;border-radius:3px;background:rgba(46,49,146,.9);display:inline-block;"></span> Hombres</span>
        </div>
        <div style="position:relative;height:360px;">
          <canvas id="pyramidChart"></canvas>
        </div>'''

if OLD_PYRAMID_HTML in html:
    html = html.replace(OLD_PYRAMID_HTML, NEW_PYRAMID_HTML, 1)
    changes.append('Pirámide HTML: canvas Chart.js reemplaza divs')
else:
    changes.append('SKIP Pirámide HTML')

# 2. JS: reemplazar la lógica de pirámide custom con Chart.js butterfly
OLD_PYRAMID_JS = '''// ── PYRAMID ───────────────────────────────────
const pyramidData = [
  { label: '65+',  f: 30,  m: 80  },
  { label: '60-64',f: 52,  m: 130 },
  { label: '55-59',f: 90,  m: 180 },
  { label: '50-54',f: 145, m: 240 },
  { label: '45-49',f: 180, m: 285 },
  { label: '40-44',f: 247, m: 375 },
  { label: '35-39',f: 210, m: 310 },
  { label: '30-34',f: 95,  m: 100 },
  { label: '25-29',f: 18,  m: 15  },
  { label: '<25',  f: 3,   m: 2   },
];
const maxPyr = Math.max(...pyramidData.map(d => Math.max(d.f, d.m)));
const pyrEl = document.getElementById('pyramid');
pyramidData.forEach(row => {
  const fPct = (row.f / maxPyr * 45);
  const mPct = (row.m / maxPyr * 45);
  pyrEl.innerHTML += `
    <div class="pyr-row">
      <div class="pyr-lbl">${row.label}</div>
      <div style="flex:1;display:flex;justify-content:flex-end;">
        <div class="pyr-L" data-w="${fPct}" style="width:0%;max-width:${fPct}%;"></div>
      </div>
      <div class="pyr-center">${row.f+row.m}</div>
      <div style="flex:1;">
        <div class="pyr-R" data-w="${mPct}" style="width:0%;max-width:${mPct}%;"></div>'''

NEW_PYRAMID_JS = '''// ── PYRAMID — Chart.js butterfly (diverging horizontal bar) ────
// Valores negativos = mujeres (izquierda), positivos = hombres (derecha)
new Chart(document.getElementById('pyramidChart'), {
  type: 'bar',
  data: {
    labels: ['65+','60-64','55-59','50-54','45-49','40-44','35-39','30-34','25-29','<25'],
    datasets: [
      {
        label: 'Mujeres',
        data: [-30, -52, -90, -145, -180, -247, -210, -95, -18, -3],
        backgroundColor: 'rgba(155,90,191,0.82)',
        hoverBackgroundColor: 'rgba(155,90,191,1)',
        borderRadius: { topLeft: 6, topRight: 0, bottomLeft: 6, bottomRight: 0 },
        borderSkipped: false,
      },
      {
        label: 'Hombres',
        data: [80, 130, 180, 240, 285, 375, 310, 100, 15, 2],
        backgroundColor: 'rgba(46,49,146,0.82)',
        hoverBackgroundColor: 'rgba(46,49,146,1)',
        borderRadius: { topLeft: 0, topRight: 6, bottomLeft: 0, bottomRight: 6 },
        borderSkipped: false,
      }
    ]
  },
  options: {
    indexAxis: 'y',
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { display: false },
      tooltip: {
        callbacks: {
          title: ctx => 'Tramo ' + ctx[0].label,
          label: ctx => {
            const v = Math.abs(ctx.raw);
            const total = ctx.datasetIndex === 0
              ? v + [80,130,180,240,285,375,310,100,15,2][ctx.dataIndex]
              : v + [30,52,90,145,180,247,210,95,18,3][ctx.dataIndex];
            const pct = (v / total * 100).toFixed(0);
            return ` ${ctx.dataset.label}: ${v} (${pct}%)`;
          }
        }
      }
    },
    scales: {
      x: {
        min: -420, max: 420,
        grid: { color: 'rgba(255,255,255,0.06)', lineWidth: 1 },
        border: { display: false },
        ticks: {
          callback: v => Math.abs(v),
          color: 'rgba(221,239,251,0.4)',
          font: { size: 10 },
          stepSize: 100,
        }
      },
      y: {
        grid: { display: false },
        border: { display: false },
        ticks: {
          color: 'rgba(221,239,251,0.75)',
          font: { size: 11, weight: '600', family: "'Manrope', sans-serif" },
          padding: 8,
        }
      }
    },
    animation: { duration: 1000, easing: 'easeOutQuart' }
  }
});

// LEGACY pyramid removed (replaced by Chart.js butterfly above)
// ── DUMMY to skip old forEach ──
const _pyramidDummy = (() => {
  const pyramidData = [];'''

if OLD_PYRAMID_JS in html:
    html = html.replace(OLD_PYRAMID_JS, NEW_PYRAMID_JS, 1)
    changes.append('Pirámide JS: Chart.js butterfly reemplaza custom HTML')
else:
    changes.append('SKIP Pirámide JS')

# ═══════════════════════════════════════════════════════════════
# Hero KPI — margin-bottom 3rem → 2rem (más compacto arriba)
# ═══════════════════════════════════════════════════════════════
OLD_KPI_MB = '''    <!-- 4 KPI cards -->
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:1rem;margin-bottom:3rem;">'''
NEW_KPI_MB = '''    <!-- 4 KPI cards -->
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:1rem;margin-bottom:2rem;">'''
if OLD_KPI_MB in html:
    html = html.replace(OLD_KPI_MB, NEW_KPI_MB, 1)
    changes.append('Hero KPIs: margin-bottom 3→2rem')

# ═══════════════════════════════════════════════════════════════
# Hero header — margin-bottom 3rem → 2rem
# ═══════════════════════════════════════════════════════════════
OLD_HDR_MB = '''    <!-- Header text -->
    <div style="max-width:700px;margin-bottom:3rem;">'''
NEW_HDR_MB = '''    <!-- Header text -->
    <div style="max-width:700px;margin-bottom:2rem;">'''
if OLD_HDR_MB in html:
    html = html.replace(OLD_HDR_MB, NEW_HDR_MB, 1)
    changes.append('Hero header: margin-bottom 3→2rem')

# ═══════════════════════════════════════════════════════════════
# Save
# ═══════════════════════════════════════════════════════════════
with open('c:/Users/acarcamo/Desktop/WEBS/Anuario SCIA/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Redesign — {len(changes)} changes:')
for c in changes:
    print(f'  {"--" if "SKIP" in c else "OK"} {c}')

content = open('c:/Users/acarcamo/Desktop/WEBS/Anuario SCIA/index.html', encoding='utf-8').read()
opens = content.count('<div'); closes = content.count('</div>')
import os; size = os.path.getsize('c:/Users/acarcamo/Desktop/WEBS/Anuario SCIA/index.html')
print(f'\nBalance: {opens}/{closes} ({opens-closes}) | Size: {size//1024} KB')
