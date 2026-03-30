# Auditoria Integral UX/UI y Tipografia del Anuario SCIA

Fecha: 2026-03-27

## Artefactos asociados

- `reportes/matriz_hallazgos_ux_ui_tipografia_anuario_scia_2026-03-27.md`
- `reportes/requisitos_web_anuario_scia_2026-03-27.md`
- `reportes/recomendacion_tipografica_anuario_scia_2026-03-27.md`

## Alcance

Esta auditoria cubre ambas capas del producto:

1. Sitio vigente en `index.html`, tratado como el producto real que hoy comunica el anuario.
2. Base futura en `app/`, tratada como shell de migracion y consolidacion para 2024, 2025 y anos siguientes.

El objetivo no es revisar solo "como se ve", sino evaluar si la experiencia web resuelve bien el trabajo que un anuario institucional debe hacer:

- orientar,
- explicar,
- permitir comparar,
- dar confianza,
- dejar trazabilidad del dato,
- y sostener una lectura larga en escritorio y movil.

## Metodologia

La revision combina cuatro skills y seis roles funcionales.

### Skills usados

- `web-design-guidelines`: chequeo de semantica, focus, motion, navegacion, copy UI y patrones web.
- `ui-ux-pro-max`: lectura de jerarquia, narrativa, consistencia visual, responsive y calidad de producto.
- `web-accessibility`: foco, teclado, screen readers, semantica y riesgos WCAG AA.
- `frontend-design`: direccion visual futura y criterio para la recomendacion tipografica.

### Roles simulados

- UX Lead / Product Designer
- UI Designer / Design Systems Lead
- Typographer / Brand Designer
- Data Visualization Designer
- Accessibility Specialist
- Frontend Reviewer / Content Strategist

### Evidencia revisada

- `index.html`
- `app/index.html`
- `app/src/App.jsx`
- `app/src/styles.css`
- `app/src/components/*`
- `app/src/sections/*`
- `app/src/lib/chartConfig.js`
- `data/2024.json`
- `data/2025.json`
- `docs/ARQUITECTURA.md`
- `reportes/auditoria_ux_ui_anuario_institucional_2026-03-24.md`
- `reportes/auditoria_uve_diseno_presentacion.md`
- `reportes/anuario_2024_chequeo_y_comparacion.md`
- capturas `audit_home.png`, `audit_dashboard.png`, `react_app.png`, `verify_03_fullpage.png`
- lineamientos de Web Interface Guidelines de Vercel

## Inventario del producto

### Capa 1: sitio vigente

`index.html` es una experiencia one-page larga con ocho secciones:

1. Panorama
2. Postulacion y adjudicacion
3. Gestion financiera
4. Productividad
5. Capital humano
6. Diversidad
7. Territorio
8. Vinculacion

Patrones presentes:

- navbar fija con anclas
- switcher anual 2024/2025/2026
- boton de comparar
- KPIs animados
- multiples charts en `canvas`
- mapa coropletico interactivo
- footer de cierre
- variante `print`

### Capa 2: base futura React

`app/` ya desacopla datos y presentacion:

- shell con sidebar, hero, rail de secciones y vista principal
- `data/*.json` como fuente de verdad
- ocho secciones mapeadas desde `sectionRegistry`
- `2025.json` existente, pero solo con financiera realmente poblada; el resto sigue pendiente

Patrones presentes:

- `skip-link`
- `main`, `nav`, `header`, `section`, `article`
- charts con `aria-label`
- reduced motion global
- impresion razonable

## Resumen ejecutivo

El proyecto esta mejor que un micrositio improvisado: tiene estructura, fuentes visibles, ocho capitulos bien delimitados, narrativa institucional y una base React con contrato de datos. El problema no es falta de trabajo; el problema es falta de cierre entre producto actual, base futura y sistema visual.

Hoy conviven dos verdades:

- un sitio publicado largo, narrativo y bastante pulido visualmente;
- y una base React mas institucional y mantenible, pero todavia incompleta como producto.

Eso genera cuatro tensiones principales:

1. La experiencia no tiene una "version canonica" clara.
2. La comparacion anual existe en discurso, pero no como patron UX realmente defendible.
3. La tipografia esta fragmentada entre legacy, React y charts.
4. El mapa y varias piezas dinamicas aun dependen demasiado de mouse y de estados no compartibles.

## Lo que esta bien resuelto

### Arquitectura de contenido

- El anuario ya esta dividido en ocho bloques reconocibles y alineados con la lectura institucional.
- Hay trazabilidad visible de fuentes en casi todas las secciones del legacy y en la estructura del JSON de la app.
- La capa React ya ordena hero, metadata, KPIs, contenido principal e insights de forma consistente.

### Senales de producto serio

- El sitio vigente tiene `@media print`, reduced motion y una navegacion por anclas util.
- La app React introduce `skip-link`, focus visible global y semantica mucho mas limpia.
- `data/2024.json` conserva notas y advertencias metodologicas que ayudan a no maquillar inconsistencias reales del dato.

### Lenguaje visual

- El sitio vigente tiene una direccion visual reconocible: glassmorphism institucional, capas claras, azules profundos y narrativa de seccion.
- La app React ya ofrece una version mas sobria y escalable del mismo universo, especialmente en sidebar, hero y rail de secciones.

## Hallazgos prioritarios

### P0

1. No hay una experiencia canonica unica.
   - `index.html` es el producto vigente.
   - `app/` es la base futura.
   - `app/index.html:6` todavia titula la experiencia como `SCIA Data Lab`, lo que delata estado de laboratorio y no de producto institucional.

2. La navegacion y el contexto anual no son compartibles de forma robusta.
   - En React, `activeYear` y `activeSection` viven solo en estado local (`app/src/App.jsx:18-27`) y se consumen mediante botones (`app/src/components/YearSwitcher.jsx:7-17`, `app/src/components/SectionRail.jsx:7-20`).
   - En legacy, el selector anual y comparar operan via JS (`index.html:1290-1293`, `index.html:3727-3779`) sin estado reflejado en URL.
   - Resultado: no se puede compartir una vista exacta de ano + seccion + comparacion.

3. El mapa territorial sigue siendo principalmente una interaccion de mouse.
   - Legacy: `mouseenter`, `mousemove`, `mouseleave` y `click` sobre grupos SVG (`index.html:3487-3511`).
   - React: el mismo patron (`app/src/components/ChileMap.jsx:127-150`).
   - No hay soporte equivalente por teclado ni regiones SVG convertidas en elementos focusables y etiquetados.

4. El sistema tipografico no esta cerrado.
   - Legacy carga `Inter + Manrope + Material Symbols` (`index.html:9`).
   - React carga `Inter + Manrope + JetBrains Mono` (`app/src/styles.css:1`, `app/src/styles.css:32-34`).
   - Los charts React usan `IBM Plex Sans` (`app/src/lib/chartConfig.js:25`) y `CapitalHumanoSection` vuelve a fijar `Inter` (`app/src/sections/CapitalHumanoSection.jsx:42`).
   - La marca tipografica actual es funcional, pero no institucionalmente distintiva ni consistente.

### P1

5. La web del anuario aun no explicita bien su marco editorial.
   - Hay portada y secciones, pero falta una capa clara de "como leer esto", metodologia, advertencias, alcance del corte y cierre editorial fuera de la logica de cards y charts.
   - En el PDF existen prologo e introduccion; en web no existe un equivalente claro como experiencia.

6. La comparacion anual esta subdisenada.
   - En legacy, `compare` solo compara contra 2024 y depende del primer ano disponible (`index.html:3773-3779`).
   - En React, 2025 existe en `data/2025.json`, pero siete secciones siguen pendientes y aun asi el shell presenta una exploracion anual completa.

7. El legacy deja deuda seria de accesibilidad de datos.
   - Los charts son `canvas` sin alternativa textual equivalente visible ni etiquetado accesible por grafico (`index.html:1361`, `1516`, `1525`, `1623`, `1681`, `1690`, `1719`, `1739`, `1769`, `1796`, `1859`, `1911`).
   - `#anuario-toast` y `#year-banner` existen (`index.html:1297`, `1299`) pero no son live regions.

8. El lenguaje visual esta entre dos productos distintos.
   - Legacy: pagina narrativa con capas, blobs, gradients e iconografia Material Symbols.
   - React: dashboard/shell institucional, mas sobrio, pero aun con chrome experimental (`app/src/App.jsx:67-70`).
   - El usuario percibe mas "migracion" que "familia de producto".

9. La web comunica bien el dato, pero no termina de resolver la capa de confianza institucional.
   - Hay fuentes por seccion.
   - Sigue faltando una entrada visible a descarga, impresion, metodologia y versionado del anuario como publicacion.

### P2

10. El legacy usa demasiado inline style y `transition: all`.
    - Ejemplos: `index.html:219`, `427`, `475`.
    - No rompe la experiencia hoy, pero complica mantenimiento, performance fina y consistencia.

11. La app React tiene piezas de chrome mas demostrativas que funcionales.
    - `app/src/App.jsx:67-70` muestra tabs decorativos, no navegacion real.
    - Son utiles como direccion visual, pero hoy introducen una promesa de producto que aun no existe.

12. El sistema visual todavia no decide cuanto editorial quiere ser.
    - El shell React es correcto y sobrio.
    - El sitio vigente tiene una atmosfera mas rica.
    - La futura mejora necesita una jerarquia tipografica mas definida para que el tono editorial no dependa solo de gradientes, blur y cajas.

## Lectura por frentes

### 1. Arquitectura de informacion

Estado:

- Bueno en division de secciones.
- Parcial en contexto, lectura guiada y comparacion anual.

Problemas:

- falta resumen ejecutivo web
- falta metodologia explicita
- falta un estado shareable por seccion/ano
- 2025 no tiene una estrategia visual clara para "en construccion" o "parcial"

### 2. Sistema visual

Estado:

- Bueno en identidad institucional azul y superficies claras.
- Parcial en coherencia entre legacy y React.

Problemas:

- dos gramaticas cercanas, pero no unificadas
- iconografia legacy mas generica
- exceso de efectos en legacy frente a una app futura mas contenida

### 3. Tipografia

Estado:

- Correcta en legibilidad base.
- Debil en diferenciacion, consistencia y jerarquia editorial.

Problemas:

- demasiadas familias para un mismo producto
- charts con stack distinto al shell
- el sistema actual no separa bien display, heading, body, label y mono

### 4. Interaccion y navegacion

Estado:

- Bueno en anclas y railes.
- Debil en deep linking y mapa.

Problemas:

- falta persistencia en URL
- comparar no esta productizado
- mapa no resuelve teclado

### 5. Visualizacion de datos

Estado:

- Bueno en variedad de formatos y uso de KPIs.
- Parcial en accesibilidad y consistencia comparativa.

Problemas:

- canvas legacy sin alternativa textual equivalente
- reglas de comparacion anual aun no estabilizadas
- faltan patrones recurrentes para deltas, advertencias y cambios de alcance

### 6. Accesibilidad y performance perceptual

Estado:

- React va mejor encaminado.
- Legacy resuelve parte del focus y reduced motion, pero no todo el modelo interactivo.

Problemas:

- live regions ausentes
- mapa dependiente de mouse
- sin estado URL
- demasiado codigo inline en legacy

## Panorama del producto segun capturas

### Sitio vigente

Lo que se observa en `verify_03_fullpage.png` confirma un producto largo, claro y ya defendible ante stakeholders:

- hero fuerte,
- sidebar contextual,
- tarjetas limpias,
- estructura de lectura consistente.

Pero tambien confirma la tension principal:

- visualmente parece listo,
- estructuralmente aun no esta resuelto como sistema anual, comparable y mantenible.

### Base React

`react_app.png` muestra una capa mas institucional y mas cercana a dashboard documental:

- mejor shell,
- mejor control de fuentes y corte,
- mejor separacion de datos y UI.

A la vez, se percibe mas como "workspace interno del anuario" que como edicion final publicada.

## Recomendacion de direccion

La decision correcta no es elegir entre el legacy y la app, sino consolidar una sola experiencia final con esta regla:

- el producto publicado debe heredar la trazabilidad, semantica y escalabilidad de `app/`
- y solo debe conservar del legacy lo que realmente mejora lectura editorial, no lo que agrega ruido o deuda

En tipografia, la mejor hipotesis no es `Geist solo`, sino `Geist + Sentient` con un uso muy controlado de Sentient.

## Hoja de ruta sin codigo

### Quick wins del sitio vigente

1. Definir una capa visible de metodologia, corte y alcance.
2. Hacer visible una entrada de descarga/impresion/version.
3. Redisenar compare como patron real o desactivarlo hasta tenerlo cerrado.
4. Resolver accesibilidad del mapa y alternativas textuales de charts.

### Decisiones fundacionales para `app/`

1. Persistir estado de ano y seccion en URL.
2. Definir estados `pendiente`, `parcial`, `sin datos` y `comparativo`.
3. Cerrar un sistema tipografico unico para shell, cards, charts y metadata.
4. Sustituir el chrome demostrativo por chrome funcional.

### Decisiones a postergar hasta cerrar 2025

1. Motion de alto detalle.
2. Pulido visual fino por seccion.
3. Variantes comparativas complejas entre anos.
4. Microajustes de iconografia y ornamentacion.

## Conclusion

El sitio ya tiene valor institucional y no parte de cero. El problema central es de cierre de producto:

- una sola experiencia canonica,
- una sola logica anual,
- una sola gramatica tipografica,
- y una sola manera de compartir, comparar y leer el anuario.

La mejora mas importante no es agregar mas componentes. Es decidir que el anuario deje de ser una suma de buenas pantallas y pase a ser una publicacion digital con reglas propias.
