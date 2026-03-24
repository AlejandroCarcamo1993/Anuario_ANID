# Auditoria UX/UI Anuario SCIA

Fecha: 2026-03-24

## Alcance

Esta auditoria compara tres capas:

1. El shell React actual en `app/src`.
2. La referencia visual en `stitch (3).zip`, usando como base:
   - `stitch_extracted/stitch/andean_nexus/DESIGN.md`
   - `stitch_extracted/stitch/home_anuario_scia`
   - `stitch_extracted/stitch/dashboard_centros_de_investigaci_n`
   - `stitch_extracted/stitch/postulaciones_y_adjudicaciones`
   - `stitch_extracted/stitch/concentraci_n_regional_de_la_ciencia`
3. Las reglas recientes de Web Interface Guidelines de Vercel.

No se modifica el sitio legado `index.html`. El trabajo se concentra en la nueva base React.

## Resumen Ejecutivo

El shell previo estaba mejor estructurado que el HTML legado, pero visualmente se alejaba de una identidad institucional moderna:

- La paleta era calida y editorial, mas cercana a una memoria impresa que a una plataforma ANID.
- La tipografia mezclaba un sans corporativo con una serif literaria que restaba precision en datos.
- La jerarquia visual era inconsistente entre secciones: cada bloque parecia de una familia distinta.
- La navegacion funcionaba, pero no transmitia producto digital ni lectura institucional continua.

La referencia `stitch` resuelve mejor esos puntos porque unifica:

- una base azul institucional,
- superficies translucidas limpias,
- titulares de alto contraste,
- navegacion tipo dashboard,
- y una lectura de datos mas tecnica.

## Hallazgos Priorizados

### P0

1. La identidad visual no estaba alineada con ANID.
   - El shell usaba beige, cobre y rosa como base dominante.
   - Eso diluia el reconocimiento institucional.

2. La tipografia no apoyaba bien la lectura de datos.
   - La serif editorial en titulares aportaba caracter, pero no consistencia con un producto de informacion.
   - Faltaba una fuente monoespaciada para metadatos y cifras cortas.

3. La capa de chrome no parecia una plataforma.
   - Faltaba una barra superior clara y un sistema de navegacion que diera continuidad entre secciones.
   - La sidebar estaba bien funcionalmente, pero no suficientemente institucional.

4. Habia deuda de accesibilidad de interfaz.
   - Faltaban `focus-visible` globales coherentes.
   - Faltaba tratamiento para `prefers-reduced-motion`.
   - Las cifras no usaban `tabular-nums`.

### P1

5. Demasiada variacion cromatica por seccion.
   - El shell tenia varias atmosferas visuales correctas por separado, pero no una familia comun.
   - El sistema necesitaba usar el color como acento semantico, no como identidad independiente por capitulo.

6. La narrativa de hero y KPI no estaba suficientemente productizada.
   - Los indicadores principales estaban presentes, pero la envolvente visual no parecia un tablero institucional.

7. Las superficies y radios eran demasiado organicos para un anuario institucional.
   - Habia buen uso de tarjetas, pero faltaba mas rigor de ritmo, grosor y contraste tonal.

### P2

8. El shell aun no separa rendimiento por seccion.
   - El build actual sigue empaquetando toda la app en un chunk principal grande.
   - No es un problema de UX inmediato, pero si de escalabilidad.

9. Algunas piezas del chrome son informativas, no funcionales.
   - La barra superior nueva deja clara la direccion visual, pero todavia no expone estados complejos como comparacion 2024 vs 2025 o filtros persistentes.

## Direccion Visual Recomendada

### North Star

**Archivo Institucional Luminoso**

No buscamos un dashboard fintech ni un PDF vestido de web. La direccion correcta es:

- institucional,
- sobria,
- tecnica,
- contemporanea,
- con profundidad suave y no ornamental.

### Principios

1. El azul ANID manda.
2. El rojo se usa como acento de alerta o contraste, no como fondo dominante.
3. La interfaz debe sentirse precisa, no nostalgica.
4. El dato manda sobre el decorado.
5. El vidrio y el blur se usan como capa de profundidad, no como efecto protagonista.

## Sistema Visual Propuesto

### Color

Base adoptada:

- `primary`: `#00396b`
- `primary-strong`: `#005092`
- `secondary`: `#bc0004`
- `tertiary`: `#00566c`
- `sky`: `#59d5fe`
- `background`: `#f8f9ff`
- `background-soft`: `#eff4ff`
- `ink`: `#0b1c30`

Regla de uso:

- Los fondos mayores deben mantenerse en blancos frios y azules muy suaves.
- Los heroes pueden usar gradientes azules oscuros con halos celestes.
- El rojo queda reservado para alertas, warnings y contrastes puntuales.

### Tipografia

Sistema adoptado:

- Display y headings: `Manrope`
- Cuerpo y UI: `IBM Plex Sans`
- Metadatos y microcopy tecnico: `IBM Plex Mono`

Razon:

- `Manrope` conserva contundencia institucional.
- `IBM Plex Sans` mejora lectura de datos y tablas frente a una opcion mas editorial.
- `IBM Plex Mono` ordena cortes, codigos, fuentes y KPIs cortos.

### Superficies y Elevacion

Reglas:

- Fondo general claro con gradientes atmosfericos suaves.
- Tarjetas blancas semitransparentes con blur moderado.
- Bordes tenues y sombras difusas.
- Radios amplios, pero no blandos.

### Movimiento

Reglas:

- Transiciones cortas, limpias y opacas.
- Animaciones solo en `transform` y `opacity`.
- Variante reducida obligatoria para `prefers-reduced-motion`.

## Cambios Aplicados Ahora

Se aplico una base institucional nueva en el shell React:

### Chrome

- Se agrego una `topbar` fija con marca ANID / SCIA.
- La sidebar se rehizo como panel institucional translucido.
- Se reforzo la lectura de cobertura, fuentes y ano como parte del chrome.

### Tipografia

- Se reemplazo la mezcla editorial anterior por `Manrope + IBM Plex Sans + IBM Plex Mono`.
- Se normalizo el uso de mayusculas tecnicas para labels y metadata.

### Color

- Se elimino la base calida beige/cobre como identidad dominante.
- Se reemplazo por un sistema azul institucional con acentos celestes y rojos.
- Las secciones siguen teniendo matices propios, pero ahora dentro de una misma familia.

### Accesibilidad y consistencia

- Se agrego `skip-link`.
- Se agrego `focus-visible` global.
- Se agrego soporte `prefers-reduced-motion`.
- Se activaron `tabular-nums` en KPIs y cifras principales.

### Visualizacion de datos

- Se alineo la paleta de charts al nuevo sistema institucional.
- Se homogeneizaron leyendas, ejes y tooltips.

## Plan Completo de Mejora

### Fase 1. Fundacion visual

Objetivo: cerrar el sistema base.

- Consolidar tokens de color y tipografia.
- Homogeneizar cards, chips, pills, tablas y listas.
- Definir comportamiento de estados hover, active y focus.

Estado: iniciado y aplicado parcialmente.

### Fase 2. Consistencia por seccion

Objetivo: que las 8 secciones se sientan parte del mismo producto.

- Unificar reglas de hero.
- Estandarizar bloques de insight, KPI strip y panel secundario.
- Reducir variaciones innecesarias de layout.

Estado: pendiente de refinamiento fino.

### Fase 3. Narrativa y comparacion anual

Objetivo: preparar la experiencia para 2025.

- Agregar comparacion 2024 vs 2025 como patron de UI recurrente.
- Hacer persistente el selector de ano con contexto visual claro.
- Preparar estados de diferencia, warning y reconciliacion de datos.

Estado: pendiente.

### Fase 4. Rendimiento y polish

Objetivo: dejar la experiencia lista para publicacion.

- Dividir bundle por seccion o por ano.
- Revisar contraste final y accesibilidad de charts.
- Hacer QA visual responsive con capturas por seccion.

Estado: pendiente.

## Recomendaciones para el siguiente modelo

1. No volver a tocar `index.html` como base de diseno.
2. Trabajar sobre `app/src` como fuente de la nueva experiencia.
3. Mantener el sistema azul institucional como regla, no como sugerencia.
4. Antes de sumar 2025, cerrar estos tres frentes:
   - comparacion anual,
   - lazy loading por seccion,
   - QA visual responsive.

## Riesgos Abiertos

- El chunk principal sigue siendo grande y deberia dividirse.
- Las secciones aun dependen de bastante CSS compartido; conviene modularizar por bloques una vez estable la direccion visual.
- La nueva topbar todavia no expresa estados complejos de filtros o comparacion anual.

## Resultado Esperado

Si se sigue esta direccion, el anuario deberia pasar de ser una pagina de datos funcional a una plataforma institucional moderna:

- mas cercana a producto digital,
- mas coherente con ANID,
- mas clara para comparar anos,
- y mas defendible a nivel UX/UI cuando entren 2025 y futuras ediciones.
