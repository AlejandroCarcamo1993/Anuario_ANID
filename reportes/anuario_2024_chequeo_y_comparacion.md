# Chequeo y comparación: PDF vs sitio

## Alcance

- PDF revisado: `Anuario 2024 - ANID 30.12 (5).pdf`
- Artefacto comparado del sitio: `index.html`
- Fecha de revisión: `2026-03-24`
- No se modificó contenido publicado ni el HTML del sitio.
- No fue posible identificar una URL pública canónica desde el repositorio; además, una búsqueda web por el título y textos distintivos del sitio no devolvió una página pública inequívoca. Por eso, la comparación se hizo contra el artefacto disponible en este workspace: `index.html`.

## Resumen ejecutivo

- El PDF tiene inconsistencias de versión: el archivo dice 2024, pero el contenido visible y los pies de página dicen `ANUARIO 2025`.
- El PDF presenta problemas editoriales evidentes: placeholders, texto residual en inglés y errores tipográficos en fuentes.
- Hay diferencias relevantes entre PDF y sitio en `Panorama`, `Gestión Financiera` y `Productividad`.
- `Postulación`, `Patentes`, `Capital Humano`, `Diversidad` y parte de `Territorio` sí muestran alta coincidencia entre PDF y sitio.
- El sitio también tiene inconsistencias internas en sus totales, incluso antes de compararlo con el PDF.
- El PDF no cubre la sección `Vinculación`, mientras que el sitio sí la publica.

## Chequeo del PDF

### Hallazgos críticos

1. El documento mezcla años y versiones.
   - Página 1: aparece `ANUARIO 2025`.
   - Página 2: el prólogo presenta “Anuario 2025”.
   - Página 2: además habla del período `2023-2025`.
   - Pies de página: continúan mostrando `ANUARIO 2025`.

2. El índice no corresponde al documento efectivamente entregado.
   - Página 1 lista `Redes e interdisciplinariedad`, `Vinculación, extensión e impacto`, `Conclusiones` y `Anexos`.
   - En las 22 páginas extraídas no aparece una sección formal de `Vinculación`, ni `Conclusiones`, ni `Anexos`.

3. Hay residuos editoriales que indican que el PDF no está cerrado.
   - Páginas 5 y 6: aparece `MARKET RESEARCH REPORT`.
   - Página 8: aparece el placeholder `[Mencionar Basales/FONDAP si tienes el dato específico, o dejar genérico]`.
   - Páginas 14 y 15: la fuente aparece como `PRESEMTACIONES`, con error ortográfico.

4. Hay cifras que no se reconcilian dentro del propio PDF.
   - Página 4: se declara un total de `473 iniciativas`.
   - Página 4: también se muestran `72` centros vigentes y `307` proyectos vigentes, que suman `379`, no `473`.
   - Página 4: los conteos por instrumento sí suman `473`, por lo que el problema está en el resumen centros/proyectos.
   - Páginas 8 y 9: se muestran `M$64.358.830` para centros y `M$80.129.246` para proyectos; ambos suman `M$144.488.076`, pero el documento no presenta un total consistente con esa suma.
   - Página 10: se mencionan `2.532` presentaciones a congresos.
   - Página 14: luego se reportan `6.867` presentaciones.
   - Página 15: luego se reportan `2.932` presentaciones realizadas por 55 centros.
   - Página 13: formación de capital humano = `1.701`.
   - Página 22: territorio = `494` proyectos/centros.
   - El documento cambia de universo estadístico entre secciones sin explicitarlo con suficiente claridad.

5. Hay problemas de fuente o etiquetado.
   - Página 11: la sección de publicaciones termina con la fuente `PATENTES - PROPIEDAD INTELECTUAL`, que no corresponde al tema mostrado.

### Observaciones por página

- Página 1: índice incompleto y con año incorrecto.
- Página 2: prólogo con `Anuario 2025` y período `2023-2025`.
- Página 3: introducción consistente en tono, pero sigue con pie `ANUARIO 2025`.
- Página 4: panorama útil, pero con inconsistencia fuerte entre total, centros y proyectos.
- Página 5: KPIs de postulación/adjudicación consistentes; queda texto residual en inglés.
- Página 6: análisis de brecha de género consistente; se mantiene el residual en inglés.
- Página 7: introducción financiera sin problemas mayores.
- Página 8: contiene placeholder editorial; subtotal de centros visible.
- Página 9: subtotal de proyectos visible; no cierra contra un total global claro.
- Página 10: buena introducción narrativa, pero cifra de congresos no coincide con páginas posteriores.
- Página 11: publicaciones con métricas claras, pero fuente mal etiquetada.
- Página 12: patentes y PI coherentes.
- Página 13: formación de capital humano clara, pero no coincide con el sitio.
- Página 14: total de congresos claro; fuente con typo.
- Página 15: divulgación consistente; convive con otra cifra distinta de presentaciones; fuente con typo.
- Página 16: introducción de diversidad correcta.
- Página 17: capital humano consistente y legible.
- Página 18: participación femenina por instrumento consistente a nivel de titulares.
- Página 19: liderazgos femeninos y nota metodológica correctos.
- Página 20: introducción territorial correcta.
- Página 21: gráfico territorial difícil de recomponer en texto lineal.
- Página 22: resumen territorial claro, pero queda en tensión con otros universos del documento.

## Chequeo de consistencia del sitio local

Base revisada: objeto `ANUARIO[2024]` y contenido visible de `index.html`.

1. `Panorama` no cierra internamente.
   - Total de iniciativas: `473`.
   - Centros: `72`.
   - Proyectos: `385`.
   - `72 + 385 = 457`, no `473`.

2. `Gestión Financiera` no cierra internamente.
   - Centros: `64.358.830`.
   - Proyectos: `80.129.246`.
   - Suma: `144.488.076`.
   - Total publicado en el sitio: `88.190.665`.

3. `Formación de Capital Humano` no cierra entre KPIs y series.
   - KPI publicado: `1.732` tesis.
   - Suma de las series del gráfico: `1.579`.

4. `Congresos` no cierra entre KPI y series.
   - KPI publicado: `6.867`.
   - Suma de series nacional + internacional: `6.842`.
   - La diferencia es `25`, que coincide con la categoría mencionada en el PDF como `Milenio (otros/apoyo)` y que el sitio no despliega en la serie.

5. `Territorio` no cierra entre titular y desglose regional.
   - KPI publicado: `494`.
   - Suma del diccionario regional del sitio: `475`.

## Comparación PDF vs sitio

| Sección | Estado | Observación |
| --- | --- | --- |
| Panorama | No coincide | El PDF usa `473` iniciativas, `72` centros y `307` proyectos; el sitio usa `473`, `72` y `385`. Ninguno de los dos resúmenes cierra contra sus propios subtotales. |
| Postulación y adjudicación | Coincide | Coinciden `1.985` postulaciones, `272` adjudicaciones, `1.230/755`, `164/108`, `13,7%`, `13,3%`, `14,3%` y la lectura de brecha de género. |
| Gestión Financiera | Coincide parcial | Coinciden los subtotales de centros (`64.358.830`) y proyectos (`80.129.246`). El sitio agrega `88.190.665` como total ejecutado, cifra que no aparece reconciliada en el PDF ni en el propio sitio. |
| Publicaciones | No coincide | PDF: Institutos `1.232 / 713 Q1`, Núcleos `774 / 403 Q1`. Sitio: Institutos `1.208 / 682 Q1`, Núcleos `777 / 370 Q1`. |
| Patentes y PI | Coincide | Coinciden los totales por instrumento: Basales `40`, Institutos `11`, Anillos `4`, FONDAP `4`, Núcleos `1`. |
| Formación de capital humano | No coincide | PDF: `1.701` casos, con `890/556/255`. Sitio: `1.732`, con `901/572/259`. |
| Congresos | Coincide parcial | Ambos usan `6.867` como titular principal, pero el PDF también usa `2.532` y `2.932` en otras páginas; el sitio, además, solo suma `6.842` en sus series. |
| Divulgación | Coincide | Coinciden `1.130` actividades, `2.359.046` participantes y `52` centros participantes. |
| Capital humano | Coincide | Coinciden `2.807` personas, `1.737` hombres, `1.070` mujeres, `38,1%` mujeres y `72,7%` entre 35 y 54 años. |
| Diversidad | Coincide parcial | Coinciden los titulares `3.547`, `36,0%`, `64,0%`, `1,78`, `34,9%`, `34,6%` y `45,5%`. La cobertura por instrumento no está igual de detallada entre ambos soportes. |
| Territorio | Coincide parcial | Coinciden `494`, `248` y `72,9%` en el relato general. El problema es que ni el PDF linealizado ni el sitio dejan un desglose regional completamente reconciliado. |
| Vinculación | Solo sitio | El sitio sí publica una sección completa de `Vinculación & Ciencia con Impacto`; el PDF entregado no la contiene. |
| Prólogo / Introducción | Solo PDF | El PDF contiene prólogo e introducción; el sitio no los publica como secciones equivalentes. |

## Conclusión operativa

- El PDF no está listo para usarse como fuente final sin una corrección editorial y una reconciliación de cifras.
- El sitio tampoco está completamente reconciliado a nivel de totales internos.
- La comparación muestra una base común clara en `Postulación`, `Patentes`, `Capital Humano`, `Diversidad` y parte de `Territorio`.
- Las diferencias más relevantes están en `Panorama`, `Financiera`, `Publicaciones`, `Formación` y `Congresos`.
- Para revisión detallada del texto por página, usar `reportes/anuario_2024_pdf_extraccion.md`.
