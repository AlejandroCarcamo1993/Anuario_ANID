# Auditoría de Diseño — Anuario Virtual SCIA
**Fecha:** 2026-03-30
**Versión auditada:** 2024 (datos corte 2024-06-26)
**Herramienta:** Playwright + revisión manual de código

---

## Resumen ejecutivo

Se auditaron las 8 secciones del anuario mediante capturas de pantalla en vivo. Se identificaron y corrigieron en esta sesión 5 problemas de alta prioridad. Se documentan a continuación todos los hallazgos restantes clasificados por prioridad, junto con el plan de acción específico para cada uno.

---

## Cambios aplicados en esta sesión

| # | Problema | Solución aplicada |
|---|----------|------------------|
| 1 | "Lectura clave" repetía textualmente el contenido del editorial card | `insights.slice(1)`: el primer insight ya vive en el card editorial; el stack inferior sólo muestra los adicionales |
| 2 | Sidebar decía "paquete stitch" (lenguaje de desarrollo interno) | Reemplazado por "Acerca del anuario" con texto institucional y fecha de corte dinámica |
| 3 | Capital Humano: "Chequeo de pirámide" era un artefacto de QA interno | Reemplazado por "Perspectiva de género" con barra H/M + highlight 45% mujeres <35 |
| 4 | Territorio: nota de mismatch con estilo `warn` (rojo) desorientaba al usuario | Convertida en `quality-note--info` (azul neutro) con título "Nota metodológica" |
| 5 | Panorama: `panorama-stat-grid` triplicaba los mismos 4 KPIs del MetricStrip | Eliminado; la sección termina limpiamente en editorial + donut ± grids de datos ricos |

---

## Hallazgos por sección

### S01 — Panorama

| Severidad | Hallazgo | Acción recomendada |
|-----------|----------|-------------------|
| ✅ Corregido | `panorama-stat-grid` duplicaba KPIs | Eliminado |
| 🟡 Pendiente | Para el año 2024 la sección es corta (solo editorial + donut), sin `centrosByInstrument` ni `disciplineDistribution` | Añadir esos campos al JSON 2024 para igualar la riqueza del 2025 |
| 🟢 OK | Ribbon editorial (2 chips: Top 3, Instrumentos distintos) — limpio y sin redundancia | — |

---

### S02 — Postulación & Adjudicación

| Severidad | Hallazgo | Acción recomendada |
|-----------|----------|-------------------|
| 🔵 Info | Año 2025 muestra placeholder `_pending` — comportamiento esperado | Cuando lleguen los datos 2025, reemplazar el flag |
| 🟡 Pendiente | Los dos gráficos de barras secuenciales (montos por instrumento + pct adjudicación) lucen monótonos | Convertir el segundo en un gráfico de puntos/dots o añadir un card de "ratio adjudicación" para contrastar visualmente |
| 🟡 Pendiente | `post-balance-card` (2 chips de balance) queda vacío cuando no hay datos de balance | Condicionar el render a la existencia de los datos |

---

### S03 — Gestión Financiera

| Severidad | Hallazgo | Acción recomendada |
|-----------|----------|-------------------|
| 🟡 Pendiente | Dos gráficos de barras horizontales en secuencia sin ruptura visual | Separar con un card editorial intermedio que destaque el insight financiero principal |
| 🟡 Pendiente | Los valores del gráfico "Ejecución por instrumento" son grandes (M$ miles de millones) y la escala del eje se corta en algunos instrumentos | Revisar si `suggestedMax` del eje x da margen suficiente para etiquetas de valor |

---

### S04 — Productividad Científica

| Severidad | Hallazgo | Acción recomendada |
|-----------|----------|-------------------|
| ✅ Parcialmente corregido | Había 4 "Lectura clave" al pie; ahora muestra 3 (insight[0] quedó en el editorial card) | Evaluar si los 3 restantes agregan valor o si se integran dentro de la sección como anotaciones de gráfico |
| 🟡 Pendiente | La sección es la más larga del anuario — 5 bloques de contenido más 3 insights — excede el scroll cómodo | Considerar tabs o un toggle "ver más" para publicaciones/tesis/congresos/divulgación |
| 🟡 Pendiente | `prod-quality-card` (círculos de publicaciones) usa `position: relative` + pseudo-elementos que en pantallas <900px se superponen | Revisar breakpoint del layout de la cuadrícula `prod-triple-grid` |

---

### S05 — Capital Humano

| Severidad | Hallazgo | Acción recomendada |
|-----------|----------|-------------------|
| ✅ Corregido | "Chequeo de pirámide" — debug card visible al usuario | Reemplazado por "Perspectiva de género" |
| 🟡 Pendiente | `capital-band` al fondo del editorial card repite los mismos valores que el MetricStrip superior | Eliminar la `capital-band` del editorial card (o cambiarla a insights cualitativos) |
| 🟢 OK | Pirámide etaria — buen contraste rojo/teal, legible | — |
| 🟢 OK | Nueva sidecard "Perspectiva de género" — total, barras H/M, highlight mujeres <35 | — |

---

### S06 — Diversidad & Equidad

| Severidad | Hallazgo | Acción recomendada |
|-----------|----------|-------------------|
| 🟢 OK | Sidecard "Indicadores de liderazgo" — contador total, 4 progress bars con línea de paridad al 50% | — |
| 🟢 OK | Gráfico horizontal de participación femenina por instrumento — colores semánticos (teal=paridad, copper=intermedio, rose=bajo) | — |
| 🟡 Pendiente | `diversity-band` al fondo del editorial card repite Part. femenina / Liderazgo directivo / Jóvenes — ya visibles en la sidecard | Eliminar la banda del editorial o convertirla en una frase destaque (ej. "36% de participación femenina en 2024") |

---

### S07 — Cobertura Territorial

| Severidad | Hallazgo | Acción recomendada |
|-----------|----------|-------------------|
| ✅ Corregido | Nota de mismatch con estilo rojo desorientaba | Convertida en "Nota metodológica" estilo azul neutro |
| 🟡 Pendiente | El mapa SVG de Chile está renderizado horizontalmente (isla de Pascua a la derecha) — estéticamente correcto pero inusual para audiencia chilena | Evaluar rotar/apilar verticalmente para lectura norte-sur más natural |
| 🟢 OK | Chips de región con hover/selected + panel de detalle al clic | — |
| 🟢 OK | Gráfico "Top 10 regiones" — colores gradient por posición | — |

---

### S08 — Vinculación & Ciencia con Impacto

| Severidad | Hallazgo | Acción recomendada |
|-----------|----------|-------------------|
| 🟢 OK | Acordeón de agenda — 3 columnas por dimensión, animación CSS grid-template-rows suave | — |
| 🟢 OK | `ParticleCard` en dimension cards — glow/spotlight on hover, magnetismo activado | — |
| 🟢 OK | "Hallazgos científicos destacados" — 4 cards con tags, programas, fecha | — |
| 🟡 Pendiente | `uve-dimension-grid` en pantallas <768px colapsa a 1 columna pero las `ParticleCard` pierden el glow (el efecto necesita hover de mouse) | Añadir fallback de color de borde estático en mobile |

---

## Hallazgos transversales (todas las secciones)

| Severidad | Hallazgo | Acción recomendada |
|-----------|----------|-------------------|
| 🟡 Pendiente | `workspace-meta` (Organización / División / Unidad) — fila de texto plano sin peso visual, consume espacio innecesario | Rediseñar como 3 pills compactas o reducir a una sola línea de metadatos |
| 🟡 Pendiente | El enlace "Saltar al contenido" aparece visible en el corner superior izquierdo al cargar (antes de que se focalice) | Añadir `opacity: 0; pointer-events: none` al `.skip-link` y mostrarlo sólo en `:focus` |
| 🟡 Pendiente | Tipografía `--mono` cae back a Inter (fuentes TT Interphases no provistas) | Instalar archivos `.woff2` en `app/public/fonts/TT-Interphases/` |
| 🟡 Pendiente | Hero header (`workspace-hero`) repite el título que ya está en el section header debajo — dos headings casi idénticos en pantalla | Considerar eliminar el `h2` del workspace-hero o usarlo como subtítulo del anuario, no del documento |
| 🟡 Pendiente | `editorial-band` / `capital-band` / `diversity-band` al fondo de los editorial cards repiten los KPIs del MetricStrip — triple aparición | Eliminar las bandas de los editorial cards; mantener sólo MetricStrip + contenido del card |

---

## Plan de acción priorizado

### Prioridad Alta (próxima sesión)

1. **Eliminar `capital-band`, `diversity-band`, `panorama-ribbon` de los editorial cards** — triple duplication con MetricStrip
2. **Fix `.skip-link` — ocultar cuando no está enfocado** — problema de accesibilidad visible en pantalla
3. **Compactar `workspace-meta`** — fila Organización/División/Unidad a pills o una línea

### Prioridad Media

4. **Panorama 2024**: poblar `centrosByInstrument` y `disciplineDistribution` en `data/2024.json`
5. **Financiera**: añadir un card editorial entre los dos gráficos de barras para ruptura visual
6. **Productividad**: evaluar acordeón o tabs para reducir longitud de sección

### Prioridad Baja / Opcional

7. **Territorio**: orientación vertical del mapa Chile
8. **Vinculación mobile**: fallback de borde para `ParticleCard` sin hover
9. **TT Interphases**: instalar los archivos de fuente licenciados

---

## Estado del anuario — visión global

| Sección | Datos 2024 | Datos 2025 | Estado visual |
|---------|-----------|-----------|--------------|
| 01 Panorama | ✅ | ✅ | 🟡 Corto sin datos ricos |
| 02 Postulación | ✅ | ⏳ pending | 🟡 Gráficos monótonos |
| 03 Financiera | ✅ | ⏳ pending | 🟡 Sin ruptura visual |
| 04 Productividad | ✅ | ⏳ pending | 🟡 Sección muy larga |
| 05 Capital Humano | ✅ | ✅ | ✅ Limpio |
| 06 Diversidad | ✅ | ✅ | ✅ Limpio |
| 07 Territorio | ✅ | ✅ | ✅ Limpio |
| 08 Vinculación | ✅ | ✅ | ✅ Limpio |
