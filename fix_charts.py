import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('c:/Users/acarcamo/Desktop/WEBS/Anuario SCIA/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

changes = []

# ═══════════════════════════════════════════════════════════════
# FIX 1 — pubDonut: cutout más grueso + center text + sin bordes
# ═══════════════════════════════════════════════════════════════
OLD_PUB_DONUT = '''function pubDonut(id, total, q1, color1, color2) {
  const q1v = q1;
  const rest = total - q1v;
  const q2 = Math.round(rest * 0.52);
  const q3 = Math.round(rest * 0.28);
  const q4 = rest - q2 - q3;
  initChart(id, {
    type: 'doughnut',
    data: {
      labels: ['Q1', 'Q2', 'Q3', 'Q4'],
      datasets: [{
        data: [q1v, q2, q3, q4],
        backgroundColor: [color1, color2, C.pale, 'rgba(46,49,146,0.15)'],
        borderWidth: 2,
        borderColor: '#fff',
        hoverOffset: 6,
      }]
    },
    options: {
      responsive: true, maintainAspectRatio: true,
      cutout: '82%',
      plugins: {
        legend: { display: true },
        tooltip: {
          callbacks: {
            label: ctx => ` ${ctx.label}: ${ctx.raw} (${(ctx.raw/total*100).toFixed(1)}%)`
          }
        }
      }
    }
  });
}'''

NEW_PUB_DONUT = '''function pubDonut(id, total, q1, color1, color2) {
  const q1v = q1;
  const rest = total - q1v;
  const q2 = Math.round(rest * 0.52);
  const q3 = Math.round(rest * 0.28);
  const q4 = rest - q2 - q3;
  // Center-text plugin scoped to this chart instance
  const centerPlugin = {
    id: 'center_' + id,
    beforeDraw(chart) {
      if (chart.canvas.id !== id) return;
      const { ctx, chartArea } = chart;
      if (!chartArea) return;
      const cx = (chartArea.left + chartArea.right) / 2;
      const cy = (chartArea.top + chartArea.bottom) / 2;
      ctx.save();
      ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
      ctx.font = "700 20px 'Manrope', sans-serif";
      ctx.fillStyle = '#11113A';
      ctx.fillText(total.toLocaleString('es-CL'), cx, cy - 8);
      ctx.font = "600 9px 'Inter', sans-serif";
      ctx.fillStyle = '#64748b';
      ctx.fillText('Q1: ' + (q1v / total * 100).toFixed(0) + '%', cx, cy + 10);
      ctx.restore();
    }
  };
  initChart(id, {
    type: 'doughnut',
    data: {
      labels: ['Q1', 'Q2', 'Q3', 'Q4'],
      datasets: [{
        data: [q1v, q2, q3, q4],
        backgroundColor: [color1, color2, C.pale, 'rgba(46,49,146,0.1)'],
        borderWidth: 0,
        hoverOffset: 10,
      }]
    },
    plugins: [centerPlugin],
    options: {
      responsive: true, maintainAspectRatio: true,
      cutout: '68%',
      plugins: {
        legend: {
          display: true,
          position: 'bottom',
          labels: { padding: 12, font: { size: 10 } }
        },
        tooltip: {
          callbacks: {
            label: ctx => ` ${ctx.label}: ${ctx.raw} (${(ctx.raw/total*100).toFixed(1)}%)`
          }
        }
      }
    }
  });
}'''

if OLD_PUB_DONUT in html:
    html = html.replace(OLD_PUB_DONUT, NEW_PUB_DONUT, 1)
    changes.append('pubDonut: thick ring + center text')
else:
    changes.append('SKIP pubDonut (not found verbatim)')

# ═══════════════════════════════════════════════════════════════
# FIX 2 — Hero donut: cutout 82% → 72% (más consistente)
# ═══════════════════════════════════════════════════════════════
OLD_HERO_CUT = '''    cutout: '82%',
    plugins: {
      legend: { display: true, labels: { color: 'rgba(221,239,251,0.75)', font: { size: 11, weight: '600' } } },'''
NEW_HERO_CUT = '''    cutout: '72%',
    plugins: {
      legend: { display: true, labels: { color: 'rgba(221,239,251,0.75)', font: { size: 11, weight: '600' } } },'''
if OLD_HERO_CUT in html:
    html = html.replace(OLD_HERO_CUT, NEW_HERO_CUT, 1)
    changes.append('Hero donut: cutout 82->72%')

# ═══════════════════════════════════════════════════════════════
# FIX 3 — Barras con borderRadius más generoso (6 → 8)
#         y barThickness en Tesis/Congresos para más impacto
# ═══════════════════════════════════════════════════════════════
# Postulación bars
OLD_POST_BR = '''{ label: 'Hombres', data: [1230, 164], backgroundColor: C.blue, borderRadius: 6, borderSkipped: 'bottom' },
      { label: 'Mujeres', data: [755, 108], backgroundColor: C.purple, borderRadius: 6, borderSkipped: 'bottom' },'''
NEW_POST_BR = '''{ label: 'Hombres', data: [1230, 164], backgroundColor: C.blue, borderRadius: 8, borderSkipped: 'bottom' },
      { label: 'Mujeres', data: [755, 108], backgroundColor: C.purple, borderRadius: 8, borderSkipped: 'bottom' },'''
if OLD_POST_BR in html:
    html = html.replace(OLD_POST_BR, NEW_POST_BR, 1)
    changes.append('Postulacion: borderRadius 6→8')

# ═══════════════════════════════════════════════════════════════
# FIX 4 — Diversidad: añadir línea de referencia de paridad (50%)
#         usando anotación inline en el chart
# ═══════════════════════════════════════════════════════════════
OLD_DIV_CHART = '''initChart('chartDiversidad', {
  type: 'bar',
  data: {
    labels: ['Ctro. Servicios','Ctro. Educación','FONDAP','Inst. Milenio','Núcleos Milenio','Ctros. Regionales','Ctros. Basales','Equip. Mediano'],
    datasets: [{
      label: '% Participación Femenina',
      data: [66.7, 48.0, 39, 37, 35, 32, 28.4, 26.9],
      backgroundColor: ctx => {
        const v = ctx.raw;
        if (v >= 50) return C.teal;
        if (v >= 40) return C.blue;
        if (v >= 35) return C.mid;
        if (v >= 30) return C.purple;
        return C.lav;
      },
      borderRadius: { topLeft: 0, topRight: 6, bottomLeft: 0, bottomRight: 6 },
      borderSkipped: 'left',
    }]
  },
  options: {
    indexAxis: 'y',
    responsive: true, maintainAspectRatio: false,
    plugins: {
      legend: { display: false },
      tooltip: { callbacks: { label: ctx => ` ${ctx.raw}% mujeres` } }
    },
    scales: {
      x: {
        max: 80,
        grid: { color: 'rgba(46,49,146,0.04)', lineWidth: 1 },
        border: { display: false },
        ticks: { callback: v => v + '%', color: '#9ca3af', font: { size: 10 } }
      },
      y: {
        grid: { color: 'rgba(46,49,146,0.04)', lineWidth: 1 },
        border: { display: false },
        ticks: { color: '#9ca3af', font: { size: 10 } }
      }
    }
  }
});'''

NEW_DIV_CHART = '''// Parity reference line plugin for Diversidad chart
const parityLinePlugin = {
  id: 'parityLine',
  afterDraw(chart) {
    if (chart.canvas.id !== 'chartDiversidad') return;
    const { ctx, scales: { x, y } } = chart;
    if (!x || !y) return;
    const xPx = x.getPixelForValue(50);
    ctx.save();
    ctx.beginPath();
    ctx.moveTo(xPx, y.top);
    ctx.lineTo(xPx, y.bottom);
    ctx.setLineDash([4, 4]);
    ctx.strokeStyle = 'rgba(26,158,122,0.55)';
    ctx.lineWidth = 1.5;
    ctx.stroke();
    ctx.setLineDash([]);
    ctx.font = "600 9px 'Inter', sans-serif";
    ctx.fillStyle = 'rgba(26,158,122,0.7)';
    ctx.textAlign = 'center';
    ctx.fillText('50% paridad', xPx, y.top - 6);
    ctx.restore();
  }
};
initChart('chartDiversidad', {
  type: 'bar',
  data: {
    labels: ['Ctro. Servicios','Ctro. Educación','FONDAP','Inst. Milenio','Núcleos Milenio','Ctros. Regionales','Ctros. Basales','Equip. Mediano'],
    datasets: [{
      label: '% Participación Femenina',
      data: [66.7, 48.0, 39, 37, 35, 32, 28.4, 26.9],
      backgroundColor: ctx => {
        const v = ctx.raw;
        if (v >= 50) return C.teal;
        if (v >= 40) return C.blue;
        if (v >= 35) return C.mid;
        if (v >= 30) return C.purple;
        return C.lav;
      },
      borderRadius: { topLeft: 0, topRight: 8, bottomLeft: 0, bottomRight: 8 },
      borderSkipped: 'left',
    }]
  },
  plugins: [parityLinePlugin],
  options: {
    indexAxis: 'y',
    responsive: true, maintainAspectRatio: false,
    plugins: {
      legend: { display: false },
      tooltip: {
        callbacks: {
          label: ctx => ` ${ctx.raw}% mujeres`,
          afterLabel: ctx => ctx.raw >= 50 ? ' ✓ Sobre paridad' : ` Brecha: ${(50-ctx.raw).toFixed(1)}pp`
        }
      }
    },
    scales: {
      x: {
        max: 80,
        grid: { color: 'rgba(46,49,146,0.04)', lineWidth: 1 },
        border: { display: false },
        ticks: { callback: v => v + '%', color: '#9ca3af', font: { size: 10 } }
      },
      y: {
        grid: { display: false },
        border: { display: false },
        ticks: { color: '#64748b', font: { size: 11 }, padding: 8 }
      }
    }
  }
});'''

if OLD_DIV_CHART in html:
    html = html.replace(OLD_DIV_CHART, NEW_DIV_CHART, 1)
    changes.append('Diversidad: paridad ref line + y-grid off')
else:
    changes.append('SKIP Diversidad (not found verbatim)')

# ═══════════════════════════════════════════════════════════════
# FIX 5 — Gestión financiera: mejorar legibilidad del eje X
#         (format M$ abreviados) y color más rico para barras top
# ═══════════════════════════════════════════════════════════════
OLD_GESTION_TICKS = '''      y: {
        grid: { color: 'rgba(46,49,146,0.04)', lineWidth: 1 },
        border: { display: false },
        ticks: { color: '#64748b', font: { size: 10 }, padding: 4 }
      }
    },
    animation: { duration: 900, easing: 'easeOutQuart' }'''
NEW_GESTION_TICKS = '''      y: {
        grid: { display: false },
        border: { display: false },
        ticks: { color: '#475569', font: { size: 10, weight: '500' }, padding: 8 }
      }
    },
    animation: { duration: 900, easing: 'easeOutQuart' }'''
if OLD_GESTION_TICKS in html:
    html = html.replace(OLD_GESTION_TICKS, NEW_GESTION_TICKS, 1)
    changes.append('Gestión: y-grid off, label weight 500')

# ═══════════════════════════════════════════════════════════════
# FIX 6 — Congresos stacked: separar nacional vs intl con colores
#         más distintos y borderRadius mejorado
# ═══════════════════════════════════════════════════════════════
OLD_CONG_DATASETS = '''      { label: 'Nacional', data: [998,929,623,541,411,100,41], backgroundColor: C.blue, borderRadius: 6, borderSkipped: 'bottom' },
      { label: 'Internacional', data: [873,811,544,560,362,38,11], backgroundColor: C.purple, borderRadius: 6, borderSkipped: 'bottom' },'''
NEW_CONG_DATASETS = '''      { label: 'Nacional', data: [998,929,623,541,411,100,41], backgroundColor: 'rgba(46,49,146,0.82)', borderRadius: { topLeft: 6, topRight: 6, bottomLeft: 0, bottomRight: 0 }, borderSkipped: 'bottom' },
      { label: 'Internacional', data: [873,811,544,560,362,38,11], backgroundColor: 'rgba(122,56,139,0.88)', borderRadius: { topLeft: 6, topRight: 6, bottomLeft: 0, bottomRight: 0 }, borderSkipped: 'bottom' },'''
if OLD_CONG_DATASETS in html:
    html = html.replace(OLD_CONG_DATASETS, NEW_CONG_DATASETS, 1)
    changes.append('Congresos: borderRadius top only')

# ═══════════════════════════════════════════════════════════════
# FIX 7 — Tesis: borderRadius mejorado + doctorado más visible
# ═══════════════════════════════════════════════════════════════
OLD_TESIS_DOC = "{ label: 'Doctorado', data: [106,48,50,35,3,1], backgroundColor: C.pale, borderRadius: 6, borderSkipped: 'bottom' },"
NEW_TESIS_DOC = "{ label: 'Doctorado', data: [106,48,50,35,3,1], backgroundColor: C.mid, borderRadius: 6, borderSkipped: 'bottom' },"
if OLD_TESIS_DOC in html:
    html = html.replace(OLD_TESIS_DOC, NEW_TESIS_DOC, 1)
    changes.append('Tesis: doctorado color pale→mid')

# ═══════════════════════════════════════════════════════════════
# FIX 8 — Screenshot timing: 1200ms → 3500ms
# ═══════════════════════════════════════════════════════════════
with open('c:/Users/acarcamo/Desktop/WEBS/Anuario SCIA/screenshot.js', 'r', encoding='utf-8') as f:
    sjs = f.read()

sjs2 = sjs.replace(
    'await page.waitForTimeout(1200); // let reveal + counters animate',
    'await page.waitForTimeout(3500); // let reveal + counters animate'
).replace(
    'await page.waitForTimeout(2000); // wait for fonts + charts',
    'await page.waitForTimeout(2800); // wait for fonts + charts'
)
if sjs2 != sjs:
    with open('c:/Users/acarcamo/Desktop/WEBS/Anuario SCIA/screenshot.js', 'w', encoding='utf-8') as f:
        f.write(sjs2)
    changes.append('Screenshot: timing 1200→3500ms / 2000→2800ms')

# ═══════════════════════════════════════════════════════════════
# Save
# ═══════════════════════════════════════════════════════════════
with open('c:/Users/acarcamo/Desktop/WEBS/Anuario SCIA/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Chart fixes — {len(changes)} changes:')
for c in changes:
    print(f'  {"--" if "SKIP" in c else "OK"} {c}')

content = open('c:/Users/acarcamo/Desktop/WEBS/Anuario SCIA/index.html', encoding='utf-8').read()
opens = content.count('<div')
closes = content.count('</div>')
import os
size = os.path.getsize('c:/Users/acarcamo/Desktop/WEBS/Anuario SCIA/index.html')
print(f'\nBalance: {opens}/{closes} ({opens-closes}) | Size: {size//1024} KB')
