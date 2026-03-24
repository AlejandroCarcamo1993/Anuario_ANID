import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('c:/Users/acarcamo/Desktop/WEBS/Anuario SCIA/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

changes = []

# ═══════════════════════════════════════════════════════════════
# CSS — Phase 3 additions
# ═══════════════════════════════════════════════════════════════
CSS_P3 = """
/* ── SEC-TAG — unified section header chip ─────────────── */
.sec-tag {
  display: inline-flex; align-items: center; gap: .5rem;
  font-family: 'Manrope', sans-serif; font-weight: 700;
  font-size: .7rem; letter-spacing: .07em; text-transform: uppercase;
  padding: .35rem .9rem .35rem .65rem;
  background: linear-gradient(135deg, rgba(46,49,146,.09), rgba(46,49,146,.05));
  border: 1px solid rgba(46,49,146,.15);
  border-radius: 9999px; color: var(--blue);
  margin-bottom: .85rem;
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  transition: background .2s, box-shadow .2s;
}
.sec-tag:hover { background: linear-gradient(135deg,rgba(46,49,146,.13),rgba(46,49,146,.08)); box-shadow: 0 2px 8px rgba(46,49,146,.1); }
.sec-tag .material-symbols-outlined { font-size: 1rem; font-variation-settings:'FILL' 1,'wght' 400,'GRAD' 0,'opsz' 20; }
.sec-tag-purple {
  background: linear-gradient(135deg, rgba(122,56,139,.1), rgba(122,56,139,.05));
  border-color: rgba(122,56,139,.18); color: var(--purple);
}
.sec-tag-purple:hover { background: linear-gradient(135deg,rgba(122,56,139,.15),rgba(122,56,139,.08)); box-shadow: 0 2px 8px rgba(122,56,139,.12); }
.sec-tag-light {
  background: rgba(255,255,255,.12);
  border-color: rgba(255,255,255,.25); color: rgba(221,239,251,.9);
}
.sec-tag-light .material-symbols-outlined { color: rgba(221,239,251,.85); }
.sec-tag-green {
  background: linear-gradient(135deg, rgba(26,158,122,.1), rgba(26,158,122,.05));
  border-color: rgba(26,158,122,.18); color: #1a9e7a;
}

/* ── DIVIDER premium ────────────────────────────────────── */
.divider {
  height: 2px;
  background: linear-gradient(90deg, var(--blue) 0%, var(--purple) 50%, transparent 100%);
  border: none; border-radius: 9999px;
  margin: .75rem 0 1.25rem; max-width: 100px;
  opacity: .75;
}

/* ── KPI icon slot ──────────────────────────────────────── */
.kpi-icon {
  display: block; font-size: 1.45rem !important;
  margin-bottom: .45rem;
  font-variation-settings: 'FILL' 1, 'wght' 300, 'GRAD' 0, 'opsz' 24;
  background: linear-gradient(135deg, var(--blue), var(--purple));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
}
.kpi-icon-light {
  background: linear-gradient(135deg, var(--light), #b8def7);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
}
.kpi-icon-green {
  background: linear-gradient(135deg, #1a9e7a, #1a6e9e);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
}

/* ── KPI white — hover lift ─────────────────────────────── */
.kpi-white {
  transition: transform .3s var(--spring), box-shadow .3s var(--smooth);
}
.kpi-white:hover {
  transform: translateY(-4px) scale(1.01);
  box-shadow: var(--glass-shadow-hover);
}

/* ── Section title gradient accent ─────────────────────── */
.sec-title-gradient {
  background: linear-gradient(135deg, var(--navy) 0%, var(--blue) 60%, var(--purple) 100%);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
}
"""

OLD_CSS_ANCHOR = '/* ── SECTION DIVIDER'
NEW_CSS_ANCHOR = CSS_P3 + '\n/* ── SECTION DIVIDER'
if OLD_CSS_ANCHOR in html:
    html = html.replace(OLD_CSS_ANCHOR, NEW_CSS_ANCHOR, 1)
    changes.append('CSS Phase 3')

# ═══════════════════════════════════════════════════════════════
# SECCIÓN 2 — Postulación: badge + eyebrow → sec-tag
# ═══════════════════════════════════════════════════════════════
OLD_S2 = '''    <div class="badge badge-blue">
      <span class="material-symbols-outlined" style="font-size:.85em;">assignment_turned_in</span>
      Sección 2
    </div>
    <span class="sec-eyebrow">Concursos 2024</span>
    <h2 class="sec-title reveal" style="font-size:clamp(1.8rem,3.5vw,2.8rem);margin-bottom:.5rem;">Postulación &amp; Adjudicación</h2>'''
NEW_S2 = '''    <div class="sec-tag reveal">
      <span class="material-symbols-outlined">assignment_turned_in</span>
      Concursos 2024
    </div>
    <h2 class="sec-title sec-title-gradient reveal" style="font-size:clamp(1.8rem,3.5vw,2.8rem);margin-bottom:.5rem;">Postulación &amp; Adjudicación</h2>'''
if OLD_S2 in html:
    html = html.replace(OLD_S2, NEW_S2, 1)
    changes.append('Sec-tag: Postulación')

# ═══════════════════════════════════════════════════════════════
# SECCIÓN 3 — Financiera
# ═══════════════════════════════════════════════════════════════
OLD_S3 = '''    <div class="badge badge-blue">
      <span class="material-symbols-outlined" style="font-size:.85em;">payments</span>
      Sección 3
    </div>
    <span class="sec-eyebrow">Ejecución presupuestaria</span>'''
NEW_S3 = '''    <div class="sec-tag reveal">
      <span class="material-symbols-outlined">payments</span>
      Ejecución presupuestaria
    </div>'''
if OLD_S3 in html:
    html = html.replace(OLD_S3, NEW_S3, 1)
    changes.append('Sec-tag: Financiera')

OLD_S3_TITLE = '''<h2 class="sec-title reveal" style="font-size:clamp(1.8rem,3.5vw,2.8rem);margin-bottom:.5rem;">Gestión Financiera</h2>'''
NEW_S3_TITLE = '''<h2 class="sec-title sec-title-gradient reveal" style="font-size:clamp(1.8rem,3.5vw,2.8rem);margin-bottom:.5rem;">Gestión Financiera</h2>'''
if OLD_S3_TITLE in html:
    html = html.replace(OLD_S3_TITLE, NEW_S3_TITLE, 1)
    changes.append('Title gradient: Financiera')

# ═══════════════════════════════════════════════════════════════
# SECCIÓN 4 — Productividad
# ═══════════════════════════════════════════════════════════════
OLD_S4 = '''    <div class="badge badge-purple">
      <span class="material-symbols-outlined" style="font-size:.85em;">menu_book</span>
      Sección 4
    </div>
    <span class="sec-eyebrow">Outputs de investigación</span>'''
NEW_S4 = '''    <div class="sec-tag sec-tag-purple reveal">
      <span class="material-symbols-outlined">menu_book</span>
      Outputs de investigación
    </div>'''
if OLD_S4 in html:
    html = html.replace(OLD_S4, NEW_S4, 1)
    changes.append('Sec-tag: Productividad')

OLD_S4_TITLE = '''<h2 class="sec-title reveal" style="font-size:clamp(1.8rem,3.5vw,2.8rem);margin-bottom:.5rem;">Productividad Científica</h2>'''
NEW_S4_TITLE = '''<h2 class="sec-title sec-title-gradient reveal" style="font-size:clamp(1.8rem,3.5vw,2.8rem);margin-bottom:.5rem;">Productividad Científica</h2>'''
if OLD_S4_TITLE in html:
    html = html.replace(OLD_S4_TITLE, NEW_S4_TITLE, 1)
    changes.append('Title gradient: Productividad')

# ═══════════════════════════════════════════════════════════════
# SECCIÓN 5 — Capital Humano (dark section)
# ═══════════════════════════════════════════════════════════════
OLD_S5 = '''    <div class="badge badge-light">
      <span class="material-symbols-outlined" style="font-size:.85em;">groups</span>
      Sección 5
    </div>
    <span class="sec-eyebrow sec-eyebrow-light">Equipo investigador</span>
    <h2 class="sec-title sec-title-light reveal" style="font-size:clamp(1.8rem,3.5vw,2.8rem);margin-bottom:.5rem;">Capital Humano</h2>'''
NEW_S5 = '''    <div class="sec-tag sec-tag-light reveal">
      <span class="material-symbols-outlined">groups</span>
      Equipo investigador
    </div>
    <h2 class="sec-title sec-title-light reveal" style="font-size:clamp(1.8rem,3.5vw,2.8rem);margin-bottom:.5rem;">Capital Humano</h2>'''
if OLD_S5 in html:
    html = html.replace(OLD_S5, NEW_S5, 1)
    changes.append('Sec-tag: Capital Humano')

# ═══════════════════════════════════════════════════════════════
# SECCIÓN 6 — Diversidad
# ═══════════════════════════════════════════════════════════════
OLD_S6 = '''    <div class="badge badge-purple">
      <span class="material-symbols-outlined" style="font-size:.85em;">diversity_3</span>
      Sección 6
    </div>
    <span class="sec-eyebrow">Paridad e inclusión</span>
    <h2 class="sec-title reveal" style="font-size:clamp(1.8rem,3.5vw,2.8rem);margin-bottom:.5rem;">Diversidad &amp; Equidad</h2>'''
NEW_S6 = '''    <div class="sec-tag sec-tag-purple reveal">
      <span class="material-symbols-outlined">diversity_3</span>
      Paridad e inclusión
    </div>
    <h2 class="sec-title sec-title-gradient reveal" style="font-size:clamp(1.8rem,3.5vw,2.8rem);margin-bottom:.5rem;">Diversidad &amp; Equidad</h2>'''
if OLD_S6 in html:
    html = html.replace(OLD_S6, NEW_S6, 1)
    changes.append('Sec-tag: Diversidad')

# ═══════════════════════════════════════════════════════════════
# SECCIÓN 7 — Territorio
# ═══════════════════════════════════════════════════════════════
OLD_S7 = '''    <div class="badge badge-light">
      <span class="material-symbols-outlined" style="font-size:.85em;">map</span>
      Sección 7
    </div>
    <span class="sec-eyebrow sec-eyebrow">Distribución geográfica</span>
    <h2 class="sec-title reveal" style="font-size:clamp(1.8rem,3.5vw,2.8rem);margin-bottom:.5rem;">Cobertura Territorial</h2>'''
NEW_S7 = '''    <div class="sec-tag reveal">
      <span class="material-symbols-outlined">map</span>
      Distribución geográfica
    </div>
    <h2 class="sec-title sec-title-gradient reveal" style="font-size:clamp(1.8rem,3.5vw,2.8rem);margin-bottom:.5rem;">Cobertura Territorial</h2>'''
if OLD_S7 in html:
    html = html.replace(OLD_S7, NEW_S7, 1)
    changes.append('Sec-tag: Territorio')

# ═══════════════════════════════════════════════════════════════
# SECCIÓN 8 — Vinculación
# ═══════════════════════════════════════════════════════════════
OLD_S8 = '''    <div class="badge badge-blue">
      <span class="material-symbols-outlined" style="font-size:.85em;">hub</span>
      Sección 8
    </div>
    <span class="sec-eyebrow">Impacto y transferencia</span>
    <h2 class="sec-title reveal" style="font-size:clamp(1.8rem,3.5vw,2.8rem);margin-bottom:.5rem;">Vinculación &amp; Ciencia con Impacto</h2>'''
NEW_S8 = '''    <div class="sec-tag reveal">
      <span class="material-symbols-outlined">hub</span>
      Impacto y transferencia
    </div>
    <h2 class="sec-title sec-title-gradient reveal" style="font-size:clamp(1.8rem,3.5vw,2.8rem);margin-bottom:.5rem;">Vinculación &amp; Ciencia con Impacto</h2>'''
if OLD_S8 in html:
    html = html.replace(OLD_S8, NEW_S8, 1)
    changes.append('Sec-tag: Vinculación')

# ═══════════════════════════════════════════════════════════════
# KPI ICONS — Tab Publicaciones
# ═══════════════════════════════════════════════════════════════
PUB_ICONS = [
    (
        '<div class="kpi kpi-white"><div class="kpi-num" style="font-size:2rem;">1.232</div><div class="kpi-lbl">Inst. Milenio</div>',
        '<div class="kpi kpi-white"><span class="material-symbols-outlined kpi-icon">star</span><div class="kpi-num" style="font-size:2rem;">1.232</div><div class="kpi-lbl">Inst. Milenio</div>'
    ),
    (
        '<div class="kpi kpi-white"><div class="kpi-num" style="font-size:2rem;">774</div><div class="kpi-lbl">Núcleos Milenio</div>',
        '<div class="kpi kpi-white"><span class="material-symbols-outlined kpi-icon">hub</span><div class="kpi-num" style="font-size:2rem;">774</div><div class="kpi-lbl">Núcleos Milenio</div>'
    ),
    (
        '<div class="kpi kpi-white"><div class="kpi-num" style="font-size:2rem;">802</div><div class="kpi-lbl">Centros Basales</div>',
        '<div class="kpi kpi-white"><span class="material-symbols-outlined kpi-icon">foundation</span><div class="kpi-num" style="font-size:2rem;">802</div><div class="kpi-lbl">Centros Basales</div>'
    ),
    (
        '<div class="kpi kpi-white"><div class="kpi-num" style="font-size:2rem;">753</div><div class="kpi-lbl">FONDAP</div>',
        '<div class="kpi kpi-white"><span class="material-symbols-outlined kpi-icon">domain</span><div class="kpi-num" style="font-size:2rem;">753</div><div class="kpi-lbl">FONDAP</div>'
    ),
    (
        '<div class="kpi kpi-white"><div class="kpi-num" style="font-size:2rem;">308</div><div class="kpi-lbl">Anillos</div>',
        '<div class="kpi kpi-white"><span class="material-symbols-outlined kpi-icon">join_right</span><div class="kpi-num" style="font-size:2rem;">308</div><div class="kpi-lbl">Anillos</div>'
    ),
]
for old, new in PUB_ICONS:
    if old in html:
        html = html.replace(old, new, 1)
        changes.append(f'KPI icon: pub {new[60:80]}')

# ═══════════════════════════════════════════════════════════════
# KPI ICONS — Tab Formación (Tesis)
# ═══════════════════════════════════════════════════════════════
TESIS_ICONS = [
    (
        '<div class="kpi kpi-white"><div class="kpi-num" style="font-size:2.2rem;" data-counter data-target="1701">0</div><div class="kpi-lbl">Total Tesis</div>',
        '<div class="kpi kpi-white"><span class="material-symbols-outlined kpi-icon">school</span><div class="kpi-num" style="font-size:2.2rem;" data-counter data-target="1701">0</div><div class="kpi-lbl">Total Tesis</div>'
    ),
    (
        '<div class="kpi kpi-white"><div class="kpi-num" style="font-size:2rem;">52,3%</div><div class="kpi-lbl">Pregrado</div>',
        '<div class="kpi kpi-white"><span class="material-symbols-outlined kpi-icon">book</span><div class="kpi-num" style="font-size:2rem;">52,3%</div><div class="kpi-lbl">Pregrado</div>'
    ),
    (
        '<div class="kpi kpi-white"><div class="kpi-num" style="font-size:2rem;">32,7%</div><div class="kpi-lbl">Magíster</div>',
        '<div class="kpi kpi-white"><span class="material-symbols-outlined kpi-icon">workspace_premium</span><div class="kpi-num" style="font-size:2rem;">32,7%</div><div class="kpi-lbl">Magíster</div>'
    ),
    (
        '<div class="kpi kpi-white"><div class="kpi-num" style="font-size:2rem;">15,0%</div><div class="kpi-lbl">Doctorado</div>',
        '<div class="kpi kpi-white"><span class="material-symbols-outlined kpi-icon">military_tech</span><div class="kpi-num" style="font-size:2rem;">15,0%</div><div class="kpi-lbl">Doctorado</div>'
    ),
]
for old, new in TESIS_ICONS:
    if old in html:
        html = html.replace(old, new, 1)
        changes.append(f'KPI icon: tesis {old[40:65]}')

# ═══════════════════════════════════════════════════════════════
# KPI ICONS — Tab Congresos
# ═══════════════════════════════════════════════════════════════
CONG_ICONS = [
    (
        '<div class="kpi kpi-white"><div class="kpi-num" style="font-size:2rem;" data-counter data-target="6867">0</div><div class="kpi-lbl">Presentaciones</div></div>',
        '<div class="kpi kpi-white"><span class="material-symbols-outlined kpi-icon">podium</span><div class="kpi-num" style="font-size:2rem;" data-counter data-target="6867">0</div><div class="kpi-lbl">Presentaciones</div></div>'
    ),
    (
        '<div class="kpi kpi-white"><div class="kpi-num" style="font-size:2rem;">44%</div><div class="kpi-lbl">Fuera de Chile</div></div>',
        '<div class="kpi kpi-white"><span class="material-symbols-outlined kpi-icon">flight_takeoff</span><div class="kpi-num" style="font-size:2rem;">44%</div><div class="kpi-lbl">Fuera de Chile</div></div>'
    ),
    (
        '<div class="kpi kpi-white"><div class="kpi-num" style="font-size:2rem;" data-counter data-target="52">0</div><div class="kpi-lbl">Países</div></div>',
        '<div class="kpi kpi-white"><span class="material-symbols-outlined kpi-icon">public</span><div class="kpi-num" style="font-size:2rem;" data-counter data-target="52">0</div><div class="kpi-lbl">Países</div></div>'
    ),
    (
        '<div class="kpi kpi-white"><div class="kpi-num" style="font-size:2rem;" data-counter data-target="55">0</div><div class="kpi-lbl">Centros Activos</div></div>',
        '<div class="kpi kpi-white"><span class="material-symbols-outlined kpi-icon">location_city</span><div class="kpi-num" style="font-size:2rem;" data-counter data-target="55">0</div><div class="kpi-lbl">Centros Activos</div></div>'
    ),
]
for old, new in CONG_ICONS:
    if old in html:
        html = html.replace(old, new, 1)
        changes.append(f'KPI icon: cong {old[40:65]}')

# ═══════════════════════════════════════════════════════════════
# KPI ICONS — Vinculación UVE
# ═══════════════════════════════════════════════════════════════
UVE_ICONS = [
    (
        '<div class="kpi kpi-white reveal"><div class="kpi-num" style="font-size:2.3rem;" data-counter data-target="12">0</div><div class="kpi-lbl">Eventos UVE</div></div>',
        '<div class="kpi kpi-white reveal"><span class="material-symbols-outlined kpi-icon">event</span><div class="kpi-num" style="font-size:2.3rem;" data-counter data-target="12">0</div><div class="kpi-lbl">Eventos UVE</div></div>'
    ),
    (
        '<div class="kpi kpi-white reveal reveal-d1"><div class="kpi-num" style="font-size:2.3rem;" data-counter data-target="1500">0</div><div class="kpi-lbl">Participantes</div></div>',
        '<div class="kpi kpi-white reveal reveal-d1"><span class="material-symbols-outlined kpi-icon">groups</span><div class="kpi-num" style="font-size:2.3rem;" data-counter data-target="1500">0</div><div class="kpi-lbl">Participantes</div></div>'
    ),
    (
        '<div class="kpi kpi-white reveal reveal-d2"><div class="kpi-num" style="font-size:2.3rem;" data-counter data-target="50">0</div><div class="kpi-lbl">Centros Participantes</div></div>',
        '<div class="kpi kpi-white reveal reveal-d2"><span class="material-symbols-outlined kpi-icon">business</span><div class="kpi-num" style="font-size:2.3rem;" data-counter data-target="50">0</div><div class="kpi-lbl">Centros Participantes</div></div>'
    ),
]
for old, new in UVE_ICONS:
    if old in html:
        html = html.replace(old, new, 1)
        changes.append(f'KPI icon: UVE {old[40:70]}')

# ═══════════════════════════════════════════════════════════════
# KPI ICONS — Territorio (main section)
# ═══════════════════════════════════════════════════════════════
TER_ICONS = [
    (
        '<div class="kpi kpi-white reveal"><div class="kpi-num" style="font-size:2.5rem;" data-counter data-target="494">0</div><div class="kpi-lbl">Iniciativas Totales</div></div>',
        '<div class="kpi kpi-white reveal"><span class="material-symbols-outlined kpi-icon">pin_drop</span><div class="kpi-num" style="font-size:2.5rem;" data-counter data-target="494">0</div><div class="kpi-lbl">Iniciativas Totales</div></div>'
    ),
    (
        '<div class="kpi kpi-white reveal reveal-d1"><div class="kpi-num" style="font-size:2.5rem;" data-counter data-target="3">0</div><div class="kpi-lbl">Regiones Principales</div>',
        '<div class="kpi kpi-white reveal reveal-d1"><span class="material-symbols-outlined kpi-icon">leaderboard</span><div class="kpi-num" style="font-size:2.5rem;" data-counter data-target="3">0</div><div class="kpi-lbl">Regiones Principales</div>'
    ),
    (
        '<div class="kpi kpi-white reveal reveal-d2"><div class="kpi-num" style="font-size:2.5rem;" data-counter data-target="248">0</div><div class="kpi-lbl">RM (Región Líder)</div>',
        '<div class="kpi kpi-white reveal reveal-d2"><span class="material-symbols-outlined kpi-icon">location_on</span><div class="kpi-num" style="font-size:2.5rem;" data-counter data-target="248">0</div><div class="kpi-lbl">RM (Región Líder)</div>'
    ),
]
for old, new in TER_ICONS:
    if old in html:
        html = html.replace(old, new, 1)
        changes.append(f'KPI icon: Territorio {old[40:70]}')

# ═══════════════════════════════════════════════════════════════
# KPI ICONS — Diversidad (main)
# ═══════════════════════════════════════════════════════════════
DIV_ICONS = [
    (
        '<div class="kpi kpi-white reveal"><div class="kpi-num" style="font-size:2.3rem;" data-counter data-target="3547">0</div><div class="kpi-lbl">Personas Totales</div></div>',
        '<div class="kpi kpi-white reveal"><span class="material-symbols-outlined kpi-icon">diversity_3</span><div class="kpi-num" style="font-size:2.3rem;" data-counter data-target="3547">0</div><div class="kpi-lbl">Personas Totales</div></div>'
    ),
    (
        '<div class="kpi kpi-white reveal reveal-d1"><div class="kpi-num" style="font-size:2.3rem;">36,0%</div><div class="kpi-lbl">Mujeres (1.278)</div></div>',
        '<div class="kpi kpi-white reveal reveal-d1"><span class="material-symbols-outlined kpi-icon" style="background:linear-gradient(135deg,var(--purple),#c06dd6);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">female</span><div class="kpi-num" style="font-size:2.3rem;">36,0%</div><div class="kpi-lbl">Mujeres (1.278)</div></div>'
    ),
    (
        '<div class="kpi kpi-white reveal reveal-d2"><div class="kpi-num" style="font-size:2.3rem;">64,0%</div><div class="kpi-lbl">Hombres (2.269)</div></div>',
        '<div class="kpi kpi-white reveal reveal-d2"><span class="material-symbols-outlined kpi-icon">male</span><div class="kpi-num" style="font-size:2.3rem;">64,0%</div><div class="kpi-lbl">Hombres (2.269)</div></div>'
    ),
    (
        '<div class="kpi kpi-white reveal reveal-d3"><div class="kpi-num" style="font-size:2.3rem;">1,78</div><div class="kpi-lbl">Razón H/M</div>',
        '<div class="kpi kpi-white reveal reveal-d3"><span class="material-symbols-outlined kpi-icon">balance</span><div class="kpi-num" style="font-size:2.3rem;">1,78</div><div class="kpi-lbl">Razón H/M</div>'
    ),
]
for old, new in DIV_ICONS:
    if old in html:
        html = html.replace(old, new, 1)
        changes.append(f'KPI icon: Diversidad {old[40:70]}')

# ═══════════════════════════════════════════════════════════════
# KPI ICONS — Postulación (main)
# ═══════════════════════════════════════════════════════════════
POST_ICONS = [
    (
        '<div class="kpi kpi-white reveal">\n        <div class="kpi-num" style="font-size:2.4rem;" data-counter data-target="1985">0</div>\n        <div class="kpi-lbl">Total Postulaciones</div>',
        '<div class="kpi kpi-white reveal">\n        <span class="material-symbols-outlined kpi-icon">send</span>\n        <div class="kpi-num" style="font-size:2.4rem;" data-counter data-target="1985">0</div>\n        <div class="kpi-lbl">Total Postulaciones</div>'
    ),
    (
        '<div class="kpi kpi-white reveal reveal-d1">\n        <div class="kpi-num" style="font-size:2.4rem;" data-counter data-target="272">0</div>\n        <div class="kpi-lbl">Total Adjudicaciones</div>',
        '<div class="kpi kpi-white reveal reveal-d1">\n        <span class="material-symbols-outlined kpi-icon">task_alt</span>\n        <div class="kpi-num" style="font-size:2.4rem;" data-counter data-target="272">0</div>\n        <div class="kpi-lbl">Total Adjudicaciones</div>'
    ),
    (
        '<div class="kpi kpi-white reveal reveal-d2">\n        <div class="kpi-num" style="font-size:2.4rem;">13,7%</div>\n        <div class="kpi-lbl">Tasa Global Adjudicación</div>',
        '<div class="kpi kpi-white reveal reveal-d2">\n        <span class="material-symbols-outlined kpi-icon">percent</span>\n        <div class="kpi-num" style="font-size:2.4rem;">13,7%</div>\n        <div class="kpi-lbl">Tasa Global Adjudicación</div>'
    ),
    (
        '<div class="kpi kpi-white reveal reveal-d3">\n        <div class="kpi-num" style="font-size:2.4rem;">39,7%</div>\n        <div class="kpi-lbl">Part. Femenina Adjudicada</div>',
        '<div class="kpi kpi-white reveal reveal-d3">\n        <span class="material-symbols-outlined kpi-icon" style="background:linear-gradient(135deg,var(--purple),#c06dd6);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">female</span>\n        <div class="kpi-num" style="font-size:2.4rem;">39,7%</div>\n        <div class="kpi-lbl">Part. Femenina Adjudicada</div>'
    ),
]
for old, new in POST_ICONS:
    if old in html:
        html = html.replace(old, new, 1)
        changes.append(f'KPI icon: Post {old[40:70]}')
    else:
        changes.append(f'SKIP Post {old[40:70]}')

# ═══════════════════════════════════════════════════════════════
# Save
# ═══════════════════════════════════════════════════════════════
with open('c:/Users/acarcamo/Desktop/WEBS/Anuario SCIA/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Phase 3 complete — {len(changes)} changes')
for c in changes:
    if 'SKIP' in c:
        print(f'  -- {c}')
    else:
        print(f'  OK {c}')

import os
size = os.path.getsize('c:/Users/acarcamo/Desktop/WEBS/Anuario SCIA/index.html')
lines = html.count('\n')
print(f'\nSize: {size//1024} KB | Lines: {lines}')
