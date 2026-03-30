# Matriz de Hallazgos UX/UI y Tipografia

Fecha: 2026-03-27

## Criterio

- `P0`: afecta comprension, accesibilidad base, trazabilidad o direccion de producto.
- `P1`: no bloquea lectura completa, pero deteriora confianza, consistencia o escalabilidad.
- `P2`: deuda de polish, mantenimiento o refinamiento.

## Hallazgos

| Severidad | Capa | Frente | Seccion / patron | Hallazgo | Evidencia |
| --- | --- | --- | --- | --- | --- |
| P0 | Compartida | Producto | Canon de experiencia | No existe una version canonica unica entre sitio publicado y shell React. | `index.html`, `app/index.html:6`, `docs/ARQUITECTURA.md` |
| P0 | React | Navegacion | Cambio de ano / seccion | `activeYear` y `activeSection` viven en estado local y no se reflejan en URL. | `app/src/App.jsx:18-27`, `app/src/components/YearSwitcher.jsx:7-17`, `app/src/components/SectionRail.jsx:7-20` |
| P0 | Legacy | Navegacion | Cambio de ano / comparar | El selector anual y `compare` no generan enlaces compartibles ni rutas estables. | `index.html:1290-1293`, `index.html:3727-3779` |
| P0 | Compartida | Accesibilidad | Mapa territorial | El mapa depende de `mouseenter/mousemove/mouseleave/click`; no ofrece equivalente por teclado. | `index.html:3487-3511`, `app/src/components/ChileMap.jsx:127-150` |
| P0 | Compartida | Tipografia | Sistema global | El producto usa stacks distintos entre shell, charts y microcopy; no hay sistema cerrado. | `index.html:9`, `app/src/styles.css:1`, `app/src/lib/chartConfig.js:25`, `app/src/sections/CapitalHumanoSection.jsx:42` |
| P1 | Legacy | Contenido | Marco editorial | La web no traduce en experiencia clara el prologo, introduccion y metodologia del anuario. | `reportes/anuario_2024_chequeo_y_comparacion.md`, `index.html` |
| P1 | Compartida | Comparacion anual | Patron de comparacion | La comparacion anual existe como intencion, pero no como patron UX estable y explicito. | `index.html:3773-3779`, `data/2025.json:1-120`, `app/src/App.jsx:18-27` |
| P1 | React | Producto | 2025 | El shell deja explorar 2025 completo, pero 7 de 8 secciones siguen pendientes. | `data/2025.json:1-120` |
| P1 | Legacy | Accesibilidad | Toast / banner | Hay feedback dinamico sin `aria-live`. | `index.html:1297`, `index.html:1299` |
| P1 | Legacy | Dataviz | Charts | Los `canvas` del legacy no muestran alternativa textual ni etiquetado accesible por grafico. | `index.html:1361`, `1516`, `1525`, `1623`, `1681`, `1690`, `1719`, `1739`, `1769`, `1796`, `1859`, `1911` |
| P1 | Compartida | IA | Requisitos de publicacion | Falta una entrada visible a descarga, impresion, versionado y metodologia como parte del producto. | `index.html`, `app/src/App.jsx:61-76`, `app/src/styles.css:2040-2099` |
| P1 | Compartida | Sistema visual | Continuidad | Legacy y React comparten ADN cromatico, pero no una misma voz de producto. | `verify_03_fullpage.png`, `react_app.png` |
| P1 | React | Chrome | Topbar | Los tabs del topbar son decorativos, no funcionales. | `app/src/App.jsx:67-70` |
| P1 | Compartida | Confianza del dato | Mensajeria metodologica | Las advertencias de alcance viven en JSON y reportes, pero no se integran de forma sistemica en la UX. | `data/2024.json:1-18`, `reportes/anuario_2024_chequeo_y_comparacion.md` |
| P2 | Legacy | Mantenimiento | CSS / JS | Hay mucho inline style y `transition: all`, lo que aumenta deuda y rigidez. | `index.html:219`, `427`, `475` |
| P2 | Legacy | Iconografia | Estilo | `Material Symbols` resuelve funcion, pero suma un tono mas generico que institucional. | `index.html:9`, multiples usos desde `index.html:1274` en adelante |
| P2 | React | Tipografia | Charts | Los charts usan IBM Plex Sans, mientras el shell usa Inter/Manrope/JetBrains. | `app/src/lib/chartConfig.js:25`, `app/src/styles.css:1`, `app/src/sections/CapitalHumanoSection.jsx:42` |
| P2 | React | Producto | Etiqueta del documento | El titulo `SCIA Data Lab` deja una sensacion de prototipo, no de anuario publicado. | `app/index.html:6` |
| P2 | Compartida | Visual | Efectos | El proyecto debe decidir cuanto glass, blur y sombra quiere sostener sin verse transicional. | `verify_03_fullpage.png`, `react_app.png`, `app/src/styles.css:151-165`, `253-266`, `629-638` |

## Lectura sintetica por seccion

| Seccion | Legacy | React | Nota |
| --- | --- | --- | --- |
| Panorama | Fuerte visualmente, pero sin contexto metodologico suficiente. | Bien estructurada y mas mantenible. | Necesita una narrativa inicial mas editorial y trazable. |
| Postulacion | Clara y legible. | Correcta. | Conviene preparar deltas anuales reutilizables. |
| Financiera | Buena lectura visual, pero compare aun inmaduro. | Mejor preparada para comparacion por ano. | Debe explicitar perimetros y diferencias de alcance. |
| Productividad | Alta densidad y muchas piezas. | Mejor separacion, aun sin patron anual estable. | Es la seccion mas sensible a tipografia y scannability. |
| Capital Humano | Fuerte como relato y grafico. | Correcta, pero con fuga tipografica en chart. | Mantener claridad numerica es critico. |
| Diversidad | Narrativamente clara. | Correcta. | Debe reforzar lectura comparativa y semantica de color. |
| Territorio | Mapa atractivo, pero dependiente de mouse. | Mejor shell, mismo problema de mapa. | Esta es la deuda de accesibilidad mas visible. |
| Vinculacion | Uno de los bloques mejor resueltos del legacy. | Todavia correcto como lectura editorial. | Puede convertirse en patron para capas metodologicas y editoriales. |

## Acciones sugeridas por severidad

### P0

1. Definir experiencia canonica.
2. Persistir estado en URL.
3. Redisenar el mapa para teclado y screen reader.
4. Cerrar el sistema tipografico.

### P1

1. Incorporar metodologia, descarga e impresion como parte visible del producto.
2. Convertir compare en patron UX real.
3. Disenar estados parciales para 2025 y futuros anos.
4. Dar alternativa textual y accesible a visualizaciones del legacy.

### P2

1. Reducir deuda de inline style y hover ad hoc.
2. Consolidar iconografia e intensidad visual.
3. Limpiar naming y labels de prototipo en la app.
