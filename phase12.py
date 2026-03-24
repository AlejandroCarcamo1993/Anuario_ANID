import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('c:/Users/acarcamo/Desktop/WEBS/Anuario SCIA/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

changes = []

# ═══════════════════════════════════════════════════════════════
# CSS — Insight callout component + simplificaciones
# ═══════════════════════════════════════════════════════════════
CSS_INSERT = """
/* ── INSIGHT CALLOUT ─────────────────────────────── */
.insight {
  position: relative;
  background: linear-gradient(135deg,
    rgba(46,49,146,.07) 0%,
    rgba(122,56,139,.05) 60%,
    rgba(74,127,193,.04) 100%);
  backdrop-filter: blur(16px) saturate(160%);
  -webkit-backdrop-filter: blur(16px) saturate(160%);
  border: 1px solid rgba(46,49,146,.12);
  border-left: 3px solid;
  border-image: linear-gradient(to bottom, var(--blue), var(--purple)) 1;
  border-radius: 0 1.1rem 1.1rem 0;
  padding: 1.1rem 1.35rem 1.1rem 1.5rem;
  margin: 1.75rem 0 .5rem;
  overflow: hidden;
}
.insight::before {
  content: '';
  position: absolute; inset: 0; border-radius: inherit; pointer-events: none;
  background: linear-gradient(135deg, rgba(255,255,255,.55) 0%, transparent 60%);
}
.insight-hdr {
  display: flex; align-items: center; gap: .5rem;
  margin-bottom: .55rem;
}
.insight-hdr .material-symbols-outlined {
  font-size: 1rem;
  background: linear-gradient(135deg, var(--blue), var(--purple));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
}
.insight-label {
  font-family: 'Manrope', sans-serif; font-weight: 800;
  font-size: .62rem; letter-spacing: .12em; text-transform: uppercase;
  background: linear-gradient(90deg, var(--blue), var(--purple));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
}
.insight p {
  font-size: .83rem; color: var(--text); line-height: 1.75;
  margin: 0; position: relative;
}
.insight strong { color: var(--navy); }
.insight-light {
  background: linear-gradient(135deg,
    rgba(255,255,255,.1) 0%,
    rgba(221,239,251,.07) 100%);
  border-color: rgba(221,239,251,.12);
}
.insight-light p { color: rgba(221,239,251,.78); }
.insight-light strong { color: white; }
.insight-light .insight-label {
  background: linear-gradient(90deg, var(--light), #b8def7);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
}

/* ── FINANCIAL KPI premium ───────────────────────── */
.kpi-fin {
  border-radius: var(--r-xl); padding: 1.5rem; position: relative; overflow: hidden;
  transition: transform .32s var(--spring), box-shadow .32s var(--smooth);
}
.kpi-fin::before {
  content: ''; position: absolute; inset: 0; border-radius: inherit;
  background: linear-gradient(135deg, rgba(255,255,255,.18) 0%, transparent 55%);
  pointer-events: none;
}
.kpi-fin:hover { transform: translateY(-6px) scale(1.01); }

/* ── TAB icons alignment ─────────────────────────── */
.tab-btn .material-symbols-outlined { font-size: .95em; vertical-align: middle; }
"""

html = html.replace(
    '@media (max-width: 768px) {',
    CSS_INSERT + '\n@media (max-width: 768px) {',
    1
)
changes.append('CSS: insight + kpi-fin + tab icon styles')

# ═══════════════════════════════════════════════════════════════
# FASE 2 — Tab emojis → Material Symbols
# ═══════════════════════════════════════════════════════════════
TAB_REPLACEMENTS = [
    ('📄 Publicaciones',  '<span class="material-symbols-outlined">article</span> Publicaciones'),
    ('🔬 Patentes & PI',  '<span class="material-symbols-outlined">labs</span> Patentes & PI'),
    ('🎓 Formación',      '<span class="material-symbols-outlined">school</span> Formación'),
    ('🌍 Congresos',      '<span class="material-symbols-outlined">public</span> Congresos'),
    ('📢 Divulgación',    '<span class="material-symbols-outlined">campaign</span> Divulgación'),
]
for old_t, new_t in TAB_REPLACEMENTS:
    if old_t in html:
        html = html.replace(old_t, new_t, 1)
        changes.append(f'Tab icon: {old_t[:20]}')

# ═══════════════════════════════════════════════════════════════
# FASE 3 — Simplificar section-divider redundante
#   Eliminar la línea section-divider que aparece después del sub
# ═══════════════════════════════════════════════════════════════
DIVIDER_BLOCK = '''    <div class="section-divider reveal">
      <div class="dot"></div>
      <div class="line"></div>
    </div>'''
# Reemplazar TODAS las ocurrencias con nada (es ruido visual)
count = html.count(DIVIDER_BLOCK)
html = html.replace(DIVIDER_BLOCK, '')
changes.append(f'Removed {count} redundant section-dividers')

DIVIDER_LIGHT = '''    <div class="section-divider section-divider-light reveal" style="margin-bottom:2rem;">
      <div class="dot"></div>
      <div class="line"></div>
    </div>'''
count2 = html.count(DIVIDER_LIGHT)
html = html.replace(DIVIDER_LIGHT, '')
changes.append(f'Removed {count2} light section-dividers')

# ═══════════════════════════════════════════════════════════════
# FASE 1 — INSIGHTS editoriales en cada sección
# ═══════════════════════════════════════════════════════════════

# ── Insight: Panorama ──
OLD_PAN = '''          <p class="data-cap" style="color:rgba(221,239,251,.5);">
            <span class="material-symbols-outlined" style="font-size:0.85em;">info</span>
            76.5% del total se concentra en 3 instrumentos
          </p>'''
NEW_PAN = '''          <div class="insight insight-light reveal">
            <div class="insight-hdr">
              <span class="material-symbols-outlined">emoji_objects</span>
              <span class="insight-label">Lectura clave</span>
            </div>
            <p>El <strong>76,5% del total</strong> se concentra en solo 3 instrumentos (Equipamiento Mediano, Anillos, Núcleos Milenio), lo que refleja una cartera dominada por proyectos de infraestructura y redes colaborativas de mediana escala. Esta concentración sugiere <strong>alta dependencia de concursos competitivos</strong> y menor participación de centros de largo aliento en el conteo total.</p>
          </div>
          <p class="data-cap" style="color:rgba(221,239,251,.5);">
            <span class="material-symbols-outlined" style="font-size:0.85em;">source</span>
            Fuente: DB Proyectos SCIA 26.06
          </p>'''
if OLD_PAN in html:
    html = html.replace(OLD_PAN, NEW_PAN, 1)
    changes.append('Insight: Panorama')

# ── Insight: Postulación ──
OLD_POST = '        <p class="data-cap"><span class="material-symbols-outlined" style="font-size:.85em;">source</span>Fuente: Estadísticas Concursos SCIA 2024</p>\n        </div>\n      </div>\n    </div>\n  </div>\n</section>'
NEW_POST = '''        <div class="insight reveal">
          <div class="insight-hdr">
            <span class="material-symbols-outlined">emoji_objects</span>
            <span class="insight-label">Lectura clave · Género y adjudicación</span>
          </div>
          <p>Contrario a la narrativa habitual, las mujeres alcanzan una <strong>tasa de adjudicación levemente superior (14,3%) frente a los hombres (13,3%)</strong>, señal de que la calidad de las postulaciones femeninas es alta. Sin embargo, la brecha persiste en volumen: solo el <strong>38% de las postulaciones son de mujeres</strong>, lo que limita el número total de adjudicaciones femeninas. En concursos temáticos como <strong>Litio y Salares</strong>, la paridad en adjudicaciones ya es un hecho.</p>
        </div>
        <p class="data-cap"><span class="material-symbols-outlined" style="font-size:.85em;">source</span>Fuente: Estadísticas Concursos SCIA 2024</p>
        </div>
      </div>
    </div>
  </div>
</section>'''
if OLD_POST in html:
    html = html.replace(OLD_POST, NEW_POST, 1)
    changes.append('Insight: Postulación')

# ── Insight: Gestión Financiera ──
OLD_FIN = '        <p class="data-cap"><span class="material-symbols-outlined" style="font-size:.85em;">source</span>Fuente: SCIA Programa de Caja 2024</p>\n      </div>\n    </div>\n  </div>\n</section>'
NEW_FIN = '''        <div class="insight reveal">
          <div class="insight-hdr">
            <span class="material-symbols-outlined">emoji_objects</span>
            <span class="insight-label">Lectura clave · Distribución presupuestaria</span>
          </div>
          <p>Los <strong>Centros Basales lideran con M$19.952.513</strong> (31% del presupuesto de centros), consolidando la apuesta por ciencia fundamental de largo plazo. Llama la atención que <strong>Equipamiento Mediano y Mayor suman M$13.341.804</strong>, evidenciando una inversión sostenida en capacidades de investigación de las universidades. El presupuesto de Proyectos (M$80.129.246) supera al de Centros (M$64.358.830), lo que refleja la <strong>predominancia de instrumentos competitivos de corto y mediano plazo</strong> en el ecosistema SCIA.</p>
        </div>
        <p class="data-cap"><span class="material-symbols-outlined" style="font-size:.85em;">source</span>Fuente: SCIA Programa de Caja 2024</p>
      </div>
    </div>
  </div>
</section>'''
if OLD_FIN in html:
    html = html.replace(OLD_FIN, NEW_FIN, 1)
    changes.append('Insight: Gestión Financiera')

# ── Insights: Productividad — al final de cada tab ──
# Publicaciones
OLD_PUB_DCAP = '      <p class="data-cap"><span class="material-symbols-outlined" style="font-size:.85em;">source</span>Fuente: DB Proyectos SCIA 26.06 · Base Investigadores SCIA 2024</p>\n    </div>'
NEW_PUB_DCAP = '''      <div class="insight reveal">
        <div class="insight-hdr">
          <span class="material-symbols-outlined">emoji_objects</span>
          <span class="insight-label">Lectura clave · Publicaciones</span>
        </div>
        <p>Los <strong>Institutos Milenio publican el 57,9% en Q1</strong> de Web of Science, el estándar de excelencia internacional más alto. Junto a los Núcleos Milenio (52,1% en Q1), el programa Milenio consolida su posición como el <strong>principal motor de ciencia de frontera</strong> en Chile. Con 1.232 publicaciones, los Institutos Milenio producen 1,6 veces más que FONDAP, pese a tener menos centros.</p>
      </div>
      <p class="data-cap"><span class="material-symbols-outlined" style="font-size:.85em;">source</span>Fuente: DB Proyectos SCIA 26.06 · Base Investigadores SCIA 2024</p>
    </div>'''
if OLD_PUB_DCAP in html:
    html = html.replace(OLD_PUB_DCAP, NEW_PUB_DCAP, 1)
    changes.append('Insight: Publicaciones')

# Patentes
OLD_PAT_DCAP = '      <p class="data-cap"><span class="material-symbols-outlined" style="font-size:.85em;">source</span>Fuente: DB Proyectos SCIA 26.06</p>\n    </div>\n\n    <!-- Tab: Formación'
NEW_PAT_DCAP = '''      <div class="insight reveal">
        <div class="insight-hdr">
          <span class="material-symbols-outlined">emoji_objects</span>
          <span class="insight-label">Lectura clave · Propiedad Intelectual</span>
        </div>
        <p>Los <strong>Centros Basales concentran el 71% de toda la propiedad intelectual</strong> registrada (40 de 56 títulos), liderando en patentes, derechos de autor y marcas. Este patrón revela que los centros de largo plazo tienen <strong>mayor madurez tecnológica</strong> y capacidad de proteger sus desarrollos. El total de 56 registros representa un portafolio modesto respecto a las publicaciones, señalando una oportunidad de mayor transferencia tecnológica en el sistema.</p>
      </div>
      <p class="data-cap"><span class="material-symbols-outlined" style="font-size:.85em;">source</span>Fuente: DB Proyectos SCIA 26.06</p>
    </div>

    <!-- Tab: Formación'''
if OLD_PAT_DCAP in html:
    html = html.replace(OLD_PAT_DCAP, NEW_PAT_DCAP, 1)
    changes.append('Insight: Patentes')

# Formación (Tesis)
OLD_TES_DCAP = '      <p class="data-cap"><span class="material-symbols-outlined" style="font-size:.85em;">source</span>Fuente: DB Proyectos SCIA 26.06</p>\n    </div>\n\n    <!-- Tab: Congresos'
NEW_TES_DCAP = '''      <div class="insight reveal">
        <div class="insight-hdr">
          <span class="material-symbols-outlined">emoji_objects</span>
          <span class="insight-label">Lectura clave · Formación de capital humano</span>
        </div>
        <p>Con <strong>1.701 tesis en 2024</strong>, el sistema SCIA es el principal formador de investigadores del país fuera del CONICYT clásico. La pirámide es sana: 52,3% pregrado, 32,7% magíster y 15% doctorado. Los <strong>Centros FONDAP destacan con 16% de doctorados</strong> (el más alto por instrumento), mientras que los Institutos Milenio forman el 17,1%. El 90,1% de la formación se concentra en solo <strong>4 instrumentos</strong>, evidenciando una oportunidad de expansión hacia instrumentos más pequeños.</p>
      </div>
      <p class="data-cap"><span class="material-symbols-outlined" style="font-size:.85em;">source</span>Fuente: DB Proyectos SCIA 26.06</p>
    </div>

    <!-- Tab: Congresos'''
if OLD_TES_DCAP in html:
    html = html.replace(OLD_TES_DCAP, NEW_TES_DCAP, 1)
    changes.append('Insight: Formación')

# Congresos
OLD_CON_DCAP = '      <p class="data-cap"><span class="material-symbols-outlined" style="font-size:.85em;">source</span>Fuente: DB Proyectos SCIA 26.06</p>\n    </div>\n\n    <!-- Tab: Divulgación'
NEW_CON_DCAP = '''      <div class="insight reveal">
        <div class="insight-hdr">
          <span class="material-symbols-outlined">emoji_objects</span>
          <span class="insight-label">Lectura clave · Presencia internacional</span>
        </div>
        <p>Con <strong>6.867 presentaciones en 52 países</strong>, la ciencia SCIA tiene huella global. El dato más llamativo: los <strong>Centros FONDAP lideran la internacionalización</strong> con 50,8% de sus presentaciones fuera de Chile, superando a todos los demás instrumentos. En contraste, los <strong>Centros de Educación muestran solo 27,5% de proyección internacional</strong>, coherente con su foco en impacto local. El 44% de internacionalización del sistema supera la media latinoamericana estimada.</p>
      </div>
      <p class="data-cap"><span class="material-symbols-outlined" style="font-size:.85em;">source</span>Fuente: DB Proyectos SCIA 26.06</p>
    </div>

    <!-- Tab: Divulgación'''
if OLD_CON_DCAP in html:
    html = html.replace(OLD_CON_DCAP, NEW_CON_DCAP, 1)
    changes.append('Insight: Congresos')

# Divulgación
OLD_DIV_DCAP = '      <p class="data-cap"><span class="material-symbols-outlined" style="font-size:.85em;">source</span>Fuente: DB Proyectos SCIA 26.06</p>\n    </div>\n  </div>\n</section>\n\n\n<!-- ═══════════════════════════════════════════\n     SECCIÓN 5 — CAPITAL HUMANO'
NEW_DIV_DCAP = '''      <div class="insight reveal">
        <div class="insight-hdr">
          <span class="material-symbols-outlined">emoji_objects</span>
          <span class="insight-label">Lectura clave · Divulgación científica</span>
        </div>
        <p>Con <strong>2.359.046 participantes en 1.130 actividades</strong>, el sistema SCIA alcanza un promedio de 2.087 personas por actividad, cifra excepcional para ciencia básica. Los <strong>Centros Basales lideran con mediana de 50 asistentes</strong> por evento, reflejando actividades presenciales de alta convocatoria. El contraste con Centros de Educación (mediana 4) revela distintos modelos de vinculación: masivos vs. especializados. La divulgación se consolida como <strong>puente entre la ciencia SCIA y la ciudadanía</strong>.</p>
      </div>
      <p class="data-cap"><span class="material-symbols-outlined" style="font-size:.85em;">source</span>Fuente: DB Proyectos SCIA 26.06</p>
    </div>
  </div>
</section>


<!-- ═══════════════════════════════════════════
     SECCIÓN 5 — CAPITAL HUMANO'''
if OLD_DIV_DCAP in html:
    html = html.replace(OLD_DIV_DCAP, NEW_DIV_DCAP, 1)
    changes.append('Insight: Divulgación')

# ── Insight: Capital Humano ──
OLD_CAP_DCAP = '        <p class="data-cap" style="justify-content:center;color:rgba(221,239,251,.4);">'
NEW_CAP_DCAP = '''        <div class="insight insight-light reveal" style="margin-top:1.5rem;">
          <div class="insight-hdr">
            <span class="material-symbols-outlined">emoji_objects</span>
            <span class="insight-label">Lectura clave · Capital humano</span>
          </div>
          <p>El <strong>72,7% del capital humano</strong> se concentra en el tramo 35–54 años, señal de un ecosistema maduro con investigadores en su etapa de mayor productividad. La <strong>presencia de mujeres es más alta en el tramo menor de 35 años (45,3%)</strong>, lo que anticipa una generación de relevo más equilibrada en género. El reto está en retener este talento emergente y asegurar continuidad en las trayectorias de investigación.</p>
        </div>
        <p class="data-cap" style="justify-content:center;color:rgba(221,239,251,.4);">'''
if OLD_CAP_DCAP in html:
    html = html.replace(OLD_CAP_DCAP, NEW_CAP_DCAP, 1)
    changes.append('Insight: Capital Humano')

# ── Insight: Diversidad ──
OLD_DIV2_DCAP = '        <p class="data-cap"><span class="material-symbols-outlined" style="font-size:.85em;">source</span>Fuente: Base Investigadores SCIA 2024</p>\n  </div>\n</section>'
NEW_DIV2_DCAP = '''        <div class="insight reveal">
          <div class="insight-hdr">
            <span class="material-symbols-outlined">emoji_objects</span>
            <span class="insight-label">Lectura clave · Equidad de género</span>
          </div>
          <p>La brecha de género persiste: <strong>1,78 hombres por cada mujer</strong> en el total del sistema. Sin embargo, los datos muestran señales positivas: los <strong>Centros de Servicios alcanzan 66,7% femenino</strong>, y los puestos de Investigadores Jóvenes/Formación llegan al <strong>45,5% de mujeres</strong>, la cifra más cercana a la paridad en posiciones académicas. La brecha más estructural está en Centros Basales (28,4%) y Equipamiento Mediano (26,9%), donde el perfil investigador sigue siendo mayoritariamente masculino.</p>
        </div>
        <p class="data-cap"><span class="material-symbols-outlined" style="font-size:.85em;">source</span>Fuente: Base Investigadores SCIA 2024</p>
  </div>
</section>'''
if OLD_DIV2_DCAP in html:
    html = html.replace(OLD_DIV2_DCAP, NEW_DIV2_DCAP, 1)
    changes.append('Insight: Diversidad')

# ── Insight: Territorio ──
OLD_TER_DCAP = '    <p class="data-cap" style="margin-top:1rem;">\n      <span class="material-symbols-outlined" style="font-size:.85em;">source</span>\n      Fuente: DB Proyectos SCIA 26.06\n    </p>'
NEW_TER_DCAP = '''    <div class="insight reveal">
      <div class="insight-hdr">
        <span class="material-symbols-outlined">emoji_objects</span>
        <span class="insight-label">Lectura clave · Concentración territorial</span>
      </div>
      <p>La <strong>Región Metropolitana concentra el 50,2% de las iniciativas</strong> (248 de 494), seguida por Valparaíso (11,5%) y Biobío (11,1%). Estas 3 regiones capturan el <strong>72,9% del total nacional</strong>, reflejando la alta concentración de universidades con capacidades de investigación en las grandes metrópolis. Las regiones del sur y norte extremo (Aysén, Magallanes, Arica) suman apenas 6 iniciativas, una oportunidad para políticas de <strong>descentralización científica</strong>. Los Macroterritorios Norte, Centro y Sur muestran distribuciones muy distintas según tipo de instrumento.</p>
    </div>
    <p class="data-cap" style="margin-top:1rem;">
      <span class="material-symbols-outlined" style="font-size:.85em;">source</span>
      Fuente: DB Proyectos SCIA 26.06
    </p>'''
if OLD_TER_DCAP in html:
    html = html.replace(OLD_TER_DCAP, NEW_TER_DCAP, 1)
    changes.append('Insight: Territorio')

# ── Upgrade: Gestión Financiera KPIs → glass con gradiente superpuesto ──
OLD_FIN_KPI1 = '      <div class="kpi reveal" style="background:linear-gradient(135deg,var(--blue),#1a1a80);color:white;box-shadow:0 8px 32px rgba(46,49,146,.3);">'
NEW_FIN_KPI1 = '      <div class="kpi kpi-fin reveal" style="background:linear-gradient(135deg,var(--blue),#1a1a80);color:white;box-shadow:0 1px 0 rgba(255,255,255,.2) inset,0 12px 40px rgba(46,49,146,.35);">'
if OLD_FIN_KPI1 in html: html = html.replace(OLD_FIN_KPI1, NEW_FIN_KPI1, 1); changes.append('FinKPI1 glass')

OLD_FIN_KPI2 = '      <div class="kpi reveal reveal-d1" style="background:linear-gradient(135deg,var(--purple),#4a1060);color:white;box-shadow:0 8px 32px rgba(122,56,139,.3);">'
NEW_FIN_KPI2 = '      <div class="kpi kpi-fin reveal reveal-d1" style="background:linear-gradient(135deg,var(--purple),#4a1060);color:white;box-shadow:0 1px 0 rgba(255,255,255,.2) inset,0 12px 40px rgba(122,56,139,.35);">'
if OLD_FIN_KPI2 in html: html = html.replace(OLD_FIN_KPI2, NEW_FIN_KPI2, 1); changes.append('FinKPI2 glass')

OLD_FIN_KPI3 = '      <div class="kpi reveal reveal-d2" style="background:linear-gradient(135deg,#11113A,#2E3192);color:white;box-shadow:0 8px 32px rgba(17,17,58,.3);border:1px solid rgba(221,239,251,.1);">'
NEW_FIN_KPI3 = '      <div class="kpi kpi-fin reveal reveal-d2" style="background:linear-gradient(135deg,#11113A,#2E3192);color:white;box-shadow:0 1px 0 rgba(255,255,255,.18) inset,0 12px 40px rgba(17,17,58,.4);border:1px solid rgba(221,239,251,.12);">'
if OLD_FIN_KPI3 in html: html = html.replace(OLD_FIN_KPI3, NEW_FIN_KPI3, 1); changes.append('FinKPI3 glass')

# ── Insight: Vinculación (after UVE section) ──
OLD_UVE = '    <!-- Hallazgos Científicos -->'
NEW_UVE = '''    <div class="insight reveal" style="margin-bottom:2rem;">
      <div class="insight-hdr">
        <span class="material-symbols-outlined">emoji_objects</span>
        <span class="insight-label">Lectura clave · Vinculación con el entorno</span>
      </div>
      <p>Los <strong>12 eventos UVE 2024 reunieron 1.500 participantes</strong> de 50 centros en sectores tan distintos como minería, construcción, transferencia regional y educación. Esta diversidad temática refleja que la ciencia SCIA <strong>cruza todas las industrias estratégicas de Chile</strong>. El formato de ferias y exposiciones sectoriales permite una conversación directa entre investigadores y tomadores de decisión, acortando el camino hacia la <strong>política pública basada en evidencia</strong>.</p>
    </div>

    <!-- Hallazgos Científicos -->'''
if OLD_UVE in html:
    html = html.replace(OLD_UVE, NEW_UVE, 1)
    changes.append('Insight: Vinculación UVE')

# ═══════════════════════════════════════════════════════════════
# Save
# ═══════════════════════════════════════════════════════════════
with open('c:/Users/acarcamo/Desktop/WEBS/Anuario SCIA/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('\n'.join(f'  {"OK" if not s.startswith("SKIP") else "SKIP"} {s}' for s in changes))
print(f'\nSize: {round(len(html)/1024)} KB | Lines: {html.count(chr(10))}')
