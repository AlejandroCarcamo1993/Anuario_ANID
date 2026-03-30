import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('c:/Users/acarcamo/Desktop/WEBS/Anuario SCIA/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

changes = []

# ═══════════════════════════════════════════════════════════════
# FIX 1 — Financiera: y-axis más legible, x-axis formato mejor,
#          altura del chart reducida (menos scroll)
# ═══════════════════════════════════════════════════════════════
OLD_GESTION_Y = '''      y: {
        grid: { color: 'rgba(46,49,146,0.04)', lineWidth: 1 },
        border: { display: false },
        ticks: { color: '#9ca3af', font: { size: 10 }, padding: 4 }
      }
    },
    animation: { duration: 900, easing: 'easeOutQuart' }'''
NEW_GESTION_Y = '''      y: {
        grid: { display: false },
        border: { display: false },
        ticks: { color: '#475569', font: { size: 11, weight: '500' }, padding: 10 }
      }
    },
    animation: { duration: 900, easing: 'easeOutQuart' }'''
if OLD_GESTION_Y in html:
    html = html.replace(OLD_GESTION_Y, NEW_GESTION_Y, 1)
    changes.append('Gestión: y-axis font 10→11 w500, no grid')

# también mejorar el x-axis de gestión
OLD_GESTION_X = '''        ticks: {
          callback: v => 'M$' + (v/1000000).toFixed(0) + 'M',
          color: '#9ca3af', font: { size: 10 }
        }'''
NEW_GESTION_X = '''        ticks: {
          callback: v => v >= 1000000 ? 'M$' + (v/1000000).toFixed(0) + 'M' : 'M$' + (v/1000).toFixed(0) + 'k',
          color: '#94a3b8', font: { size: 9 }, maxRotation: 0
        }'''
if OLD_GESTION_X in html:
    html = html.replace(OLD_GESTION_X, NEW_GESTION_X, 1)
    changes.append('Gestión: x-axis ticks formato mejorado')

# ═══════════════════════════════════════════════════════════════
# FIX 2 — Vinculación: reducir espaciado entre header y contenido
#          para que timeline sea visible más rápido
# ═══════════════════════════════════════════════════════════════
OLD_VIN_SUB = '''    <p class="sec-sub reveal" style="margin-bottom:3rem;">Estrategia de vinculación UVE 2024 y hallazgos científicos destacados del año.</p>


    <!-- UVE KPIs -->
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:1rem;margin-bottom:2.5rem;">'''
NEW_VIN_SUB = '''    <p class="sec-sub reveal" style="margin-bottom:1.5rem;">Estrategia de vinculación UVE 2024 y hallazgos científicos destacados del año.</p>

    <!-- UVE KPIs -->
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:1rem;margin-bottom:1.5rem;">'''
if OLD_VIN_SUB in html:
    html = html.replace(OLD_VIN_SUB, NEW_VIN_SUB, 1)
    changes.append('Vinculación: margin-bottom 3rem→1.5rem header')

# reducir gap entre dimensiones UVE y timeline
OLD_VIN_DIM = '''    <!-- Timeline de hitos -->
    <div class="reveal" style="margin-bottom:3.5rem;">'''
NEW_VIN_DIM = '''    <!-- Timeline de hitos -->
    <div class="reveal" style="margin-bottom:2rem;">'''
if OLD_VIN_DIM in html:
    html = html.replace(OLD_VIN_DIM, NEW_VIN_DIM, 1)
    changes.append('Vinculación: timeline margin-bottom 3.5→2rem')

# reducir margin del grid UVE dimensions
OLD_VIN_GRID = '''    <!-- UVE Dimensions -->
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:1rem;margin-bottom:3rem;" class="reveal">'''
NEW_VIN_GRID = '''    <!-- UVE Dimensions -->
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:1rem;margin-bottom:1.5rem;" class="reveal">'''
if OLD_VIN_GRID in html:
    html = html.replace(OLD_VIN_GRID, NEW_VIN_GRID, 1)
    changes.append('Vinculación: dimension grid margin-bottom 3→1.5rem')

# ═══════════════════════════════════════════════════════════════
# FIX 3 — Postulación: reducir espacio vacío inferior
# ═══════════════════════════════════════════════════════════════
OLD_POST_CHARTS = '''    <!-- Charts row -->
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;margin-bottom:2rem;" class="reveal">'''
NEW_POST_CHARTS = '''    <!-- Charts row -->
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;margin-bottom:1.25rem;" class="reveal">'''
if OLD_POST_CHARTS in html:
    html = html.replace(OLD_POST_CHARTS, NEW_POST_CHARTS, 1)
    changes.append('Postulación: chart row margin-bottom 2→1.25rem')

# ═══════════════════════════════════════════════════════════════
# FIX 4 — Congresos: y-grid off + label mejor legibilidad
# ═══════════════════════════════════════════════════════════════
OLD_CONG_Y = '''      y: {
        stacked: true,
        grid: { color: 'rgba(46,49,146,0.04)', lineWidth: 1 },
        border: { display: false },
        ticks: { color: '#9ca3af', font: { size: 10 } }
      }
    }
  }
});

// ── DIVULGACION'''
NEW_CONG_Y = '''      y: {
        stacked: true,
        grid: { display: false },
        border: { display: false },
        ticks: { color: '#475569', font: { size: 10.5, weight: '500' }, padding: 6 }
      }
    }
  }
});

// ── DIVULGACION'''
if OLD_CONG_Y in html:
    html = html.replace(OLD_CONG_Y, NEW_CONG_Y, 1)
    changes.append('Congresos: y-grid off + label weight')

# ═══════════════════════════════════════════════════════════════
# FIX 5 — Tesis: y-grid off, label mejor
# ═══════════════════════════════════════════════════════════════
OLD_TESIS_Y = '''      y: {
        stacked: true,
        grid: { color: 'rgba(46,49,146,0.04)', lineWidth: 1 },
        border: { display: false },
        ticks: { color: '#9ca3af', font: { size: 10 } }
      }
    }
  }
});

// ── CONGRESOS'''
NEW_TESIS_Y = '''      y: {
        stacked: true,
        grid: { display: false },
        border: { display: false },
        ticks: { color: '#475569', font: { size: 10.5, weight: '500' }, padding: 6 }
      }
    }
  }
});

// ── CONGRESOS'''
if OLD_TESIS_Y in html:
    html = html.replace(OLD_TESIS_Y, NEW_TESIS_Y, 1)
    changes.append('Tesis: y-grid off + label weight')

# ═══════════════════════════════════════════════════════════════
# FIX 6 — Patentes: y-grid off
# ═══════════════════════════════════════════════════════════════
OLD_PAT_Y = '''      y: {
        stacked: true,
        grid: { color: 'rgba(46,49,146,0.04)', lineWidth: 1 },
        border: { display: false },
        ticks: { color: '#9ca3af', font: { size: 10 } }
      }
    }
  }
});

// ── TESIS'''
NEW_PAT_Y = '''      y: {
        stacked: true,
        grid: { display: false },
        border: { display: false },
        ticks: { color: '#475569', font: { size: 10.5, weight: '500' }, padding: 6 }
      }
    }
  }
});

// ── TESIS'''
if OLD_PAT_Y in html:
    html = html.replace(OLD_PAT_Y, NEW_PAT_Y, 1)
    changes.append('Patentes: y-grid off + label weight')

# ═══════════════════════════════════════════════════════════════
# FIX 7 — Gestión: altura del chart 420px → 380px
#          para que quede más compacto
# ═══════════════════════════════════════════════════════════════
OLD_GESTION_H = 'style="height:420px;"><canvas id="chartGestion">'
NEW_GESTION_H = 'style="height:380px;"><canvas id="chartGestion">'
if OLD_GESTION_H in html:
    html = html.replace(OLD_GESTION_H, NEW_GESTION_H, 1)
    changes.append('Gestión: chart height 420→380px')

# ═══════════════════════════════════════════════════════════════
# FIX 8 — CSS: kpi-white hover más suave + padding bottom uniforme
# ═══════════════════════════════════════════════════════════════
OLD_KPI_HOVER = '''.kpi-white:hover {
  transform: translateY(-4px) scale(1.01);
  box-shadow: var(--glass-shadow-hover);
}'''
NEW_KPI_HOVER = '''.kpi-white:hover {
  transform: translateY(-5px) scale(1.015);
  box-shadow: var(--glass-shadow-hover), 0 0 0 1px rgba(46,49,146,.08);
}'''
if OLD_KPI_HOVER in html:
    html = html.replace(OLD_KPI_HOVER, NEW_KPI_HOVER, 1)
    changes.append('kpi-white: hover mejorado con outline sutil')

# ═══════════════════════════════════════════════════════════════
# Save
# ═══════════════════════════════════════════════════════════════
with open('c:/Users/acarcamo/Desktop/WEBS/Anuario SCIA/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Fix2 — {len(changes)} changes:')
for c in changes:
    print(f'  {"--" if "SKIP" in c else "OK"} {c}')

content = open('c:/Users/acarcamo/Desktop/WEBS/Anuario SCIA/index.html', encoding='utf-8').read()
opens = content.count('<div'); closes = content.count('</div>')
import os; size = os.path.getsize('c:/Users/acarcamo/Desktop/WEBS/Anuario SCIA/index.html')
print(f'\nBalance: {opens}/{closes} | Size: {size//1024} KB')
