import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('c:/Users/acarcamo/Desktop/WEBS/Anuario SCIA/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

changes = []

# ════════════════════════════════════════════════════════════════
# 1. CSS — Year selector, delta badges, toast, banner
# ════════════════════════════════════════════════════════════════
OLD_CSS_ANCHOR = '''.data-cap {
  font-size: .67rem; color: #94a3b8; font-style: italic;
  margin-top: 1.25rem; display: flex; align-items: center; gap: .35rem;
}'''

NEW_CSS_ANCHOR = '''.data-cap {
  font-size: .67rem; color: #94a3b8; font-style: italic;
  margin-top: 1.25rem; display: flex; align-items: center; gap: .35rem;
}

/* ── YEAR SELECTOR ─────────────────────────────── */
#year-selector {
  display: flex; align-items: center; gap: .3rem; flex-shrink: 0; margin-left: auto;
}
.yr-btn {
  font-family: 'Manrope', sans-serif; font-weight: 700; font-size: .63rem;
  padding: .27rem .62rem; border: 1px solid rgba(46,49,146,.18); border-radius: 9999px;
  background: transparent; color: var(--muted); cursor: pointer;
  transition: all .2s; white-space: nowrap; line-height: 1.4;
}
.yr-btn:hover { background: rgba(46,49,146,.07); color: var(--blue); border-color: rgba(46,49,146,.3); }
.yr-btn.yr-active {
  background: var(--blue); color: white; border-color: var(--blue);
  box-shadow: 0 2px 8px rgba(46,49,146,.28);
}
.yr-btn.yr-soon { opacity: .38; cursor: not-allowed; pointer-events: none; }
.yr-btn.yr-compare { border-color: rgba(122,56,139,.22); color: var(--purple); }
.yr-btn.yr-compare:hover { background: rgba(122,56,139,.08); }
.yr-btn.yr-active.yr-compare {
  background: linear-gradient(135deg, var(--blue), var(--purple)); border-color: transparent;
}
/* ── KPI DELTA BADGE ───────────────────────────── */
.kpi-delta {
  display: inline-flex; align-items: center; gap: .2rem;
  font-size: .6rem; font-weight: 700; padding: .1rem .42rem;
  border-radius: 9999px; margin-top: .3rem; font-family: 'Manrope', sans-serif;
}
.kpi-delta.up   { background: rgba(26,158,122,.12); color: #1a9e7a; }
.kpi-delta.down { background: rgba(200,50,50,.10);  color: #c03030; }
.kpi-delta.flat { background: rgba(100,116,139,.10);color: #64748b; }
/* ── TOAST ─────────────────────────────────────── */
#anuario-toast {
  position: fixed; bottom: 1.75rem; left: 50%;
  transform: translateX(-50%) translateY(80px);
  background: rgba(10,10,36,.95); backdrop-filter: blur(20px);
  border: 1px solid rgba(255,255,255,.12); color: rgba(221,239,251,.92);
  font-family: 'Manrope', sans-serif; font-weight: 600; font-size: .76rem;
  padding: .65rem 1.4rem; border-radius: 9999px;
  box-shadow: 0 8px 32px rgba(0,0,0,.3); z-index: 9999;
  transition: transform .35s cubic-bezier(0,0,.2,1), opacity .35s;
  opacity: 0; pointer-events: none; white-space: nowrap;
}
#anuario-toast.show { transform: translateX(-50%) translateY(0); opacity: 1; }
/* ── YEAR BANNER ────────────────────────────────── */
#year-banner {
  position: fixed; top: 60px; left: 0; right: 0; z-index: 990;
  background: linear-gradient(90deg, var(--blue), var(--purple));
  color: white; text-align: center;
  font-family: 'Manrope', sans-serif; font-weight: 700; font-size: .7rem;
  padding: .32rem 1rem; letter-spacing: .05em;
  transform: translateY(-100%); transition: transform .32s var(--ease-out);
  pointer-events: none;
}
#year-banner.show { transform: translateY(0); }'''

if OLD_CSS_ANCHOR in html:
    html = html.replace(OLD_CSS_ANCHOR, NEW_CSS_ANCHOR, 1)
    changes.append('CSS: year selector + delta + toast + banner')
else:
    changes.append('SKIP CSS anchor not found')

# ════════════════════════════════════════════════════════════════
# 2. HTML — Year selector in navbar + toast + banner elements
# ════════════════════════════════════════════════════════════════
OLD_NAV_END = '''    <a href="#vinculacion" class="nav-link">Vinculación</a>
  </div>
</nav>'''

NEW_NAV_END = '''    <a href="#vinculacion" class="nav-link">Vinculación</a>
  </div>
  <!-- Year Selector -->
  <div id="year-selector">
    <button class="yr-btn yr-active" data-year="2024" onclick="setActiveYear(2024)">2024</button>
    <button class="yr-btn" data-year="2025" onclick="setActiveYear(2025)">2025</button>
    <button class="yr-btn" data-year="2026" onclick="setActiveYear(2026)">2026</button>
    <button class="yr-btn yr-compare" data-year="compare" onclick="enterCompare()">⇄ Comparar</button>
  </div>
</nav>
<!-- Toast notification -->
<div id="anuario-toast"></div>
<!-- Year banner -->
<div id="year-banner"></div>'''

if OLD_NAV_END in html:
    html = html.replace(OLD_NAV_END, NEW_NAV_END, 1)
    changes.append('HTML: year selector in navbar + toast + banner elements')
else:
    changes.append('SKIP navbar end not found')

# ════════════════════════════════════════════════════════════════
# 3. HTML — data-kpi attributes on KPI counter elements
# ════════════════════════════════════════════════════════════════
kpi_simple = [
    # Hero / Panorama
    ('data-counter data-target="473"', 'data-counter data-target="473" data-kpi="panorama.iniciativas"'),
    ('data-counter data-target="385"', 'data-counter data-target="385" data-kpi="panorama.proyectos"'),
    # Postulación
    ('data-counter data-target="1985"', 'data-counter data-target="1985" data-kpi="postulacion.totalPostulaciones"'),
    # Capital Humano
    ('data-counter data-target="2807"', 'data-counter data-target="2807" data-kpi="capitalHumano.total"'),
    # Diversidad
    ('data-counter data-target="3547"', 'data-counter data-target="3547" data-kpi="diversidad.total"'),
    # Territorio
    ('data-counter data-target="494"', 'data-counter data-target="494" data-kpi="territorio.iniciativas"'),
    ('data-counter data-target="248"', 'data-counter data-target="248" data-kpi="territorio.rmCount"'),
    # Vinculación
    ('data-counter data-target="12"', 'data-counter data-target="12" data-kpi="vinculacion.eventosUVE"'),
    ('data-counter data-target="1500"', 'data-counter data-target="1500" data-kpi="vinculacion.participantes"'),
    # Productividad
    ('data-counter data-target="1701"', 'data-counter data-target="1701" data-kpi="productividad.tesis.total"'),
    ('data-counter data-target="6867"', 'data-counter data-target="6867" data-kpi="productividad.congresos.presentaciones"'),
    ('data-counter data-target="1130"', 'data-counter data-target="1130" data-kpi="productividad.divulgacion.actividades"'),
    # Financial currency
    ('data-currency="M$88.190.665"', 'data-currency="M$88.190.665" data-kpi-currency="panorama.presupuesto"'),
]

# Centros vigentes 72 — needs specific context to avoid ambiguity
OLD_72 = 'data-counter data-target="72">0</div>\n        <div class="kpi-lbl kpi-lbl-light">Centros Vigentes'
NEW_72 = 'data-counter data-target="72" data-kpi="panorama.centros">0</div>\n        <div class="kpi-lbl kpi-lbl-light">Centros Vigentes'

OLD_272 = 'data-counter data-target="272">0</div>\n        <div class="kpi-lbl">Total Adjudicaciones'
NEW_272 = 'data-counter data-target="272" data-kpi="postulacion.totalAdjudicaciones">0</div>\n        <div class="kpi-lbl">Total Adjudicaciones'

OLD_50 = 'data-counter data-target="50">0</div><div class="kpi-lbl">Centros Participantes</div></div>\n    </div>\n\n    <!-- UVE Dimensions'
NEW_50 = 'data-counter data-target="50" data-kpi="vinculacion.centrosParticipantes">0</div><div class="kpi-lbl">Centros Participantes</div></div>\n    </div>\n\n    <!-- UVE Dimensions'

for old, new in kpi_simple:
    if old in html:
        html = html.replace(old, new, 1)
        changes.append(f'HTML: data-kpi {old[:50]}')
    else:
        changes.append(f'SKIP kpi: {old[:50]}')

for old, new in [(OLD_72, NEW_72), (OLD_272, NEW_272), (OLD_50, NEW_50)]:
    if old in html:
        html = html.replace(old, new, 1)
        changes.append('HTML: data-kpi contextual match OK')
    else:
        changes.append(f'SKIP contextual kpi: {old[:60]}')

# ════════════════════════════════════════════════════════════════
# 4. JS — Store pyramidChart in chartsInit (for update support)
# ════════════════════════════════════════════════════════════════
OLD_PYRAMID = "new Chart(document.getElementById('pyramidChart'), {"
NEW_PYRAMID = "chartsInit['pyramidChart'] = new Chart(document.getElementById('pyramidChart'), {"
if OLD_PYRAMID in html:
    html = html.replace(OLD_PYRAMID, NEW_PYRAMID, 1)
    changes.append('JS: pyramidChart stored in chartsInit')
else:
    changes.append('SKIP pyramidChart not found')

# ════════════════════════════════════════════════════════════════
# 5. JS — Make centerTextHero dynamic
# ════════════════════════════════════════════════════════════════
OLD_HERO_TXT = "    ctx.fillText('473', cx, cy - 8);"
NEW_HERO_TXT = "    ctx.fillText((ANUARIO[activeYear]?.panorama?.iniciativas ?? 473).toLocaleString('es-CL'), cx, cy - 8);"
if OLD_HERO_TXT in html:
    html = html.replace(OLD_HERO_TXT, NEW_HERO_TXT, 1)
    changes.append('JS: centerTextHero reads ANUARIO[activeYear]')
else:
    changes.append('SKIP centerTextHero text not found')

# ════════════════════════════════════════════════════════════════
# 6. JS — Insert ANUARIO data object at top of <script>
# ════════════════════════════════════════════════════════════════
ANUARIO_JS = r"""// ══════════════════════════════════════════════════════════════
//  ANUARIO SCIA — Arquitectura Multi-Año
//  Para agregar datos 2025: copiar bloque 2024 dentro de ANUARIO,
//  cambiar la clave a 2025 y actualizar los valores.
// ══════════════════════════════════════════════════════════════
let activeYear = 2024;
let compareMode = false;

const ANUARIO = {
  2024: {
    meta: { titulo: 'Anuario SCIA 2024', año: 2024 },

    panorama: {
      iniciativas: 473,
      centros:      72,
      proyectos:   385,
      presupuesto: 88190665,
      instrumentos: {
        equipamientoMediano:  { n: 201, pct: 42.5 },
        anillosInvestigacion: { n: 108, pct: 22.8 },
        nucleosMilenio:       { n:  53, pct: 11.2 },
        resto:                { n: 111, pct: 23.5 },
      }
    },

    postulacion: {
      totalPostulaciones:  1985,
      totalAdjudicaciones:  272,
      tasaGlobal:          13.7,
      partFemenina:        39.7,
      hombresPost: 1230, mujeresPost:  755,
      hombresAdj:   164, mujeresAdj:   108,
      tasaHombres: 13.3, tasaMujeres: 14.3,
    },

    financiera: {
      ejecutadoFondos:    64358830,
      ejecutadoProyectos: 80129246,
      totalEjecutado:     88190665,
      porInstrumento: {
        labels: ['Centros Basales','FONDAP','Anillos Temáticos','Equip. Mediano',
                 'Inst. Milenio','Núcleos Milenio','Ctros. Regionales','Equip. Mayor',
                 'Excelencia Intl.','Ctros. Tecnológicos','Anillos C&T','Ctros. Educación',
                 'Exped. Científicas','Ctros. Servicios','PME','Excedentes','Gastos Operac.'],
        data: [19952513,13957323,8942208,8567729,8465252,6065641,5569276,
               4774075,4535084,2095583,1689120,1400000,990185,630000,205628,199654,151394],
      }
    },

    productividad: {
      pub: {
        institutosMilenio: { total: 1232, q1: 713 },
        nucleosMilenio:    { total:  774, q1: 403 },
        centrosBasales: 802, fondap: 753, anillos: 308,
      },
      tesis: {
        total: 1701,
        pregradoPct: 52.3, pregradoN:   890,
        magisterPct: 32.7, magisterN:   556,
        doctoradoPct: 15.0, doctoradoN: 255,
        labels: ['Ctros. Basales','FONDAP','Inst. Milenio','Núcleos Milenio','Ctros. Educación','Ctros. Regionales'],
        pregrado:  [369,157,153,123,12,4],
        magister:  [231,95,90,77,8,3],
        doctorado: [106,48,50,35,3,1],
      },
      congresos: {
        presentaciones:  6867,
        fueraChilePct:     44,
        paises:            52,
        centrosActivos:    55,
        labels: ['Ctros. Basales','Inst. Milenio','Núcleos Milenio','FONDAP','Anillos','Ctros. Educación','Ctros. Regionales'],
        nacional:      [998,929,623,541,411,100,41],
        internacional: [873,811,544,560,362,38,11],
      },
      divulgacion: {
        actividades:          1130,
        participantes:     2359046,
        promedioPorCentro:     25,
        centrosParticipantes:  52,
        labels: ['Ctros. Basales','FONDAP','Anillos','Ctros. Regionales','Ctros. Educación'],
        medianaAsistentes: [50, 36, 30, 24.5, 4],
      },
      patentes: {
        labels: ['Ctros. Basales','Inst. Milenio','Anillos','FONDAP','Núcleos'],
        patentes:    [26,10,4,4,1],
        derechoAutor: [7,1,0,0,0],
        marcas:       [3,0,0,0,0],
        secretoInd:   [3,0,0,0,0],
        servicioPi:   [1,0,0,0,0],
      }
    },

    capitalHumano: {
      total:        2807,
      hombres:      1737,
      mujeres:      1070,
      mujeresPct:   38.1,
      tramo3554Pct: 72.7,
      piramide: {
        labels: ['65+','60-64','55-59','50-54','45-49','40-44','35-39','30-34','25-29','<25'],
        mujeres: [-30,-52,-90,-145,-180,-247,-210,-95,-18,-3],
        hombres: [ 80, 130, 180, 240, 285, 375, 310, 100,  15,  2],
      }
    },

    diversidad: {
      total:    3547,
      mujeres:  1278, mujeresPct: 36.0,
      hombres:  2269, hombresPct: 64.0,
      razonHM:  1.78,
      liderazgoDirectivoPct: 34.9,
      liderazgoInvPct:       34.6,
      liderazgoJovenesPct:   45.5,
      labels: ['Ctro. Servicios','Ctro. Educación','FONDAP','Inst. Milenio',
               'Núcleos Milenio','Ctros. Regionales','Ctros. Basales','Equip. Mediano'],
      partFemenina: [66.7, 48.0, 39, 37, 35, 32, 28.4, 26.9],
    },

    territorio: {
      iniciativas:         494,
      regionesPrincipales:   3,
      regionesPrincPct:   72.9,
      rmCount:             248,
      rmPct:              50.2,
      regiones: {
        'map_chile_Metropolitana':   { name: 'Metropolitana',      count: 248, pct: '50.2' },
        'map_chile_Valparaiso':      { name: 'Valparaíso',         count:  57, pct: '11.5' },
        'map_chile_Biobio':          { name: 'Biobío',             count:  55, pct: '11.1' },
        'map_chile_Antofagasta':     { name: 'Antofagasta',        count:  20, pct: '4.0'  },
        'map_chile_Maule':           { name: 'Maule',              count:  18, pct: '3.6'  },
        'map_chile_Coquimbo':        { name: 'Coquimbo',           count:  16, pct: '3.2'  },
        'map_chile_Los_Rios':        { name: 'Los Ríos',           count:  16, pct: '3.2'  },
        'map_chile_Araucania':       { name: 'Araucanía',          count:  15, pct: '3.0'  },
        'map_chile_Tarapaca':        { name: 'Tarapacá',           count:   8, pct: '1.6'  },
        'map_chile_Los_Lagos':       { name: 'Los Lagos',          count:   7, pct: '1.4'  },
        'map_chile_AricaParinacota': { name: 'Arica y Parinacota', count:   4, pct: '0.8'  },
        'map_chile_OHiggins':        { name: "O'Higgins",          count:   4, pct: '0.8'  },
        'map_chile_Nuble':           { name: 'Ñuble',              count:   3, pct: '0.6'  },
        'map_chile_Atacama':         { name: 'Atacama',            count:   2, pct: '0.4'  },
        'map_chile_Aysen':           { name: 'Aysén',              count:   1, pct: '0.2'  },
        'map_chile_Magallanes':      { name: 'Magallanes',         count:   1, pct: '0.2'  },
      }
    },

    vinculacion: {
      eventosUVE:           12,
      participantes:      1500,
      centrosParticipantes: 50,
    },
  },

  // ── 2025 ─────────────────────────────────────────────────────
  // Ingresar datos reales cuando estén disponibles.
  // Copiar el bloque completo de 2024 arriba y actualizar valores.
  // ─────────────────────────────────────────────────────────────
  2025: null,

  // ── 2026 ─────────────────────────────────────────────────────
  2026: null,
};

"""

OLD_SCRIPT_OPEN = '<script>\n'
NEW_SCRIPT_OPEN = '<script>\n' + ANUARIO_JS

if OLD_SCRIPT_OPEN in html:
    html = html.replace(OLD_SCRIPT_OPEN, NEW_SCRIPT_OPEN, 1)
    changes.append('JS: ANUARIO multi-year data object + activeYear')
else:
    changes.append('SKIP <script> open tag not found')

# ════════════════════════════════════════════════════════════════
# 7. JS — Year switching + comparison functions (before </script>)
# ════════════════════════════════════════════════════════════════
YEAR_JS = r"""
// ══════════════════════════════════════════════════════════════
//  MULTI-YEAR SWITCHING
// ══════════════════════════════════════════════════════════════

function _showToast(msg, dur) {
  dur = dur || 3200;
  const t = document.getElementById('anuario-toast');
  if (!t) return;
  t.textContent = msg;
  t.classList.add('show');
  clearTimeout(t._tid);
  t._tid = setTimeout(function() { t.classList.remove('show'); }, dur);
}

function _showBanner(text) {
  const b = document.getElementById('year-banner');
  if (b) { b.textContent = text; b.classList.add('show'); }
}

function _hideBanner() {
  const b = document.getElementById('year-banner');
  if (b) b.classList.remove('show');
}

function setActiveYear(year) {
  const d = ANUARIO[year];
  activeYear = year;
  compareMode = false;

  // Remove all comparison delta badges
  document.querySelectorAll('.kpi-delta').forEach(function(el) { el.remove(); });

  // Remove comparison series from charts
  Object.keys(chartsInit).forEach(function(id) {
    const ch = chartsInit[id];
    if (!ch) return;
    const last = ch.data.datasets[ch.data.datasets.length - 1];
    if (last && last._cmp) { ch.data.datasets.pop(); ch.update('none'); }
  });

  // Update brand accent
  const accent = document.querySelector('.nav-brand .accent');
  if (accent) accent.textContent = year;

  // Update buttons
  document.querySelectorAll('.yr-btn').forEach(function(b) {
    b.classList.remove('yr-active');
    if (b.dataset.year == year) b.classList.add('yr-active');
    if (b.dataset.year !== 'compare') {
      const y = parseInt(b.dataset.year);
      if (!ANUARIO[y]) b.classList.add('yr-soon');
      else b.classList.remove('yr-soon');
    }
  });

  if (!d) {
    _showToast('Datos ' + year + ' aún no disponibles — próximamente');
    _showBanner('Anuario ' + year + ' · Datos en preparación');
    return;
  }

  _hideBanner();
  _updateKPIs(d);
  _updateCharts(d);
  if (year !== 2024) {
    _showBanner('Mostrando datos ' + year);
    setTimeout(_hideBanner, 4000);
  }
}

function enterCompare() {
  const yearsWithData = Object.keys(ANUARIO).filter(function(y) {
    return ANUARIO[y] !== null && parseInt(y) !== 2024;
  });
  if (yearsWithData.length === 0) {
    _showToast('Para comparar, ingrese los datos de 2025 en el objeto ANUARIO del HTML');
    return;
  }
  compareMode = true;
  document.querySelectorAll('.yr-btn').forEach(function(b) {
    b.classList.toggle('yr-active', b.dataset.year === 'compare');
  });
  _compareYears(2024, parseInt(yearsWithData[0]));
}

function _updateKPIs(d) {
  // Numeric counters
  document.querySelectorAll('[data-kpi]').forEach(function(el) {
    const path = el.dataset.kpi.split('.');
    let val = d;
    path.forEach(function(k) { val = val != null ? val[k] : null; });
    if (val == null) { el.textContent = '—'; return; }
    el.dataset.target = val;
    animCounter(el, parseInt(val), 1200);
  });
  // Currency
  document.querySelectorAll('[data-kpi-currency]').forEach(function(el) {
    const path = el.dataset.kpiCurrency.split('.');
    let val = d;
    path.forEach(function(k) { val = val != null ? val[k] : null; });
    if (val == null) { el.textContent = '—'; return; }
    const fmt = 'M$' + val.toLocaleString('es-CL');
    el.dataset.currency = fmt;
    animCurrency(el, fmt);
  });
}

function _updateCharts(d) {
  const ci = chartsInit;

  function upd(id, fn) {
    if (ci[id]) { fn(ci[id]); ci[id].update('active'); }
  }

  // Hero donut
  upd('chartHeroDonut', function(ch) {
    const ins = d.panorama.instrumentos;
    ch.data.datasets[0].data = [
      ins.equipamientoMediano.n,
      ins.anillosInvestigacion.n,
      ins.nucleosMilenio.n,
      ins.resto.n
    ];
  });

  // Postulación
  upd('chartPostulacion', function(ch) {
    ch.data.datasets[0].data = [d.postulacion.hombresPost, d.postulacion.hombresAdj];
    ch.data.datasets[1].data = [d.postulacion.mujeresPost, d.postulacion.mujeresAdj];
  });
  upd('chartTasas', function(ch) {
    ch.data.datasets[0].data = [d.postulacion.tasaHombres, d.postulacion.tasaMujeres];
  });

  // Gestión financiera
  upd('chartGestion', function(ch) {
    ch.data.datasets[0].data = d.financiera.porInstrumento.data;
  });

  // Publicaciones donuts — destroy + recreate (tienen plugin center-text inline)
  ['chartPubInstitutos','chartPubNucleos'].forEach(function(id) {
    if (ci[id]) { ci[id].destroy(); delete ci[id]; }
  });
  pubDonut('chartPubInstitutos',
    d.productividad.pub.institutosMilenio.total,
    d.productividad.pub.institutosMilenio.q1, C.blue, C.mid);
  pubDonut('chartPubNucleos',
    d.productividad.pub.nucleosMilenio.total,
    d.productividad.pub.nucleosMilenio.q1, C.purple, C.lav);

  // Productividad tabs
  upd('chartTesis', function(ch) {
    ch.data.datasets[0].data = d.productividad.tesis.pregrado;
    ch.data.datasets[1].data = d.productividad.tesis.magister;
    ch.data.datasets[2].data = d.productividad.tesis.doctorado;
  });
  upd('chartCongresos', function(ch) {
    ch.data.datasets[0].data = d.productividad.congresos.nacional;
    ch.data.datasets[1].data = d.productividad.congresos.internacional;
  });
  upd('chartDivulgacion', function(ch) {
    ch.data.datasets[0].data = d.productividad.divulgacion.medianaAsistentes;
  });
  upd('chartPatentes', function(ch) {
    ch.data.datasets[0].data = d.productividad.patentes.patentes;
    ch.data.datasets[1].data = d.productividad.patentes.derechoAutor;
    ch.data.datasets[2].data = d.productividad.patentes.marcas;
    ch.data.datasets[3].data = d.productividad.patentes.secretoInd;
    ch.data.datasets[4].data = d.productividad.patentes.servicioPi;
  });

  // Diversidad
  upd('chartDiversidad', function(ch) {
    ch.data.datasets[0].data = d.diversidad.partFemenina;
  });

  // Pirámide
  upd('pyramidChart', function(ch) {
    ch.data.datasets[0].data = d.capitalHumano.piramide.mujeres;
    ch.data.datasets[1].data = d.capitalHumano.piramide.hombres;
  });
}

function _compareYears(yearA, yearB) {
  const dA = ANUARIO[yearA];
  const dB = ANUARIO[yearB];
  if (!dA || !dB) return;

  const ci = chartsInit;

  // Add comparison dataset to key charts
  function addCmpSeries(id, dataB, colorB) {
    if (!ci[id]) return;
    const ch = ci[id];
    // Remove old comparison if present
    const last = ch.data.datasets[ch.data.datasets.length - 1];
    if (last && last._cmp) ch.data.datasets.pop();
    ch.data.datasets.push({
      label: String(yearB),
      data: dataB,
      backgroundColor: colorB || 'rgba(26,158,122,0.72)',
      borderRadius: 4,
      borderSkipped: 'bottom',
      _cmp: true,
    });
    ch.update('active');
  }

  // Make sure base year data is loaded first
  _updateCharts(dA);

  // Add comparison series
  addCmpSeries('chartGestion',    dB.financiera.porInstrumento.data, 'rgba(26,158,122,0.72)');
  addCmpSeries('chartTesis',      dB.productividad.tesis.pregrado,   'rgba(26,158,122,0.72)');
  addCmpSeries('chartCongresos',  dB.productividad.congresos.nacional,'rgba(26,158,122,0.72)');

  // Delta badges on KPI cards
  document.querySelectorAll('[data-kpi]').forEach(function(el) {
    const path = el.dataset.kpi.split('.');
    let vA = dA, vB = dB;
    path.forEach(function(k) {
      vA = vA != null ? vA[k] : null;
      vB = vB != null ? vB[k] : null;
    });
    if (typeof vA !== 'number' || typeof vB !== 'number') return;
    const delta = vB - vA;
    const pct = vA !== 0 ? (delta / vA * 100).toFixed(1) : 0;
    const cls = delta > 0 ? 'up' : delta < 0 ? 'down' : 'flat';
    const arrow = delta > 0 ? '▲' : delta < 0 ? '▼' : '=';
    const existing = el.nextElementSibling;
    if (existing && existing.classList.contains('kpi-delta')) existing.remove();
    const badge = document.createElement('div');
    badge.className = 'kpi-delta ' + cls;
    badge.textContent = arrow + ' ' + Math.abs(pct) + '% vs ' + yearA;
    el.after(badge);
  });

  _showToast('Comparando ' + yearA + ' vs ' + yearB);
}

// ── Init: mark years without data as coming-soon ──────────────
document.querySelectorAll('.yr-btn[data-year]').forEach(function(b) {
  const y = parseInt(b.dataset.year);
  if (y && !ANUARIO[y]) b.classList.add('yr-soon');
});
"""

OLD_SCRIPT_CLOSE = '</script>\n</body>'
NEW_SCRIPT_CLOSE = YEAR_JS + '\n</script>\n</body>'

if OLD_SCRIPT_CLOSE in html:
    html = html.replace(OLD_SCRIPT_CLOSE, NEW_SCRIPT_CLOSE, 1)
    changes.append('JS: setActiveYear/enterCompare/updateCharts/compare functions')
else:
    changes.append('SKIP </script></body> not found')

# Save
with open('c:/Users/acarcamo/Desktop/WEBS/Anuario SCIA/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'multi_year — {len(changes)} changes:')
for c in changes:
    print(f'  {"--" if "SKIP" in c else "OK"} {c}')

import os
size = os.path.getsize('c:/Users/acarcamo/Desktop/WEBS/Anuario SCIA/index.html')
content = open('c:/Users/acarcamo/Desktop/WEBS/Anuario SCIA/index.html', encoding='utf-8').read()
opens = content.count('<div')
closes = content.count('</div>')
print(f'\nBalance: {opens}/{closes} ({opens-closes}) | Size: {size//1024} KB')
