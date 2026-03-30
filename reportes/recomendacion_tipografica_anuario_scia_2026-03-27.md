# Recomendacion Tipografica para el Anuario SCIA

Fecha: 2026-03-27

## Objetivo

Definir una direccion tipografica unica para el anuario web, alineada con tres necesidades:

1. lectura institucional y confiable
2. claridad de producto digital
3. momentos editoriales con personalidad

## Estado actual

### Legacy

- `Inter` para UI y cuerpo
- `Manrope` para titulares y cifras
- `Material Symbols` para iconografia

Evidencia:

- `index.html:9`
- `index.html:2698-2726`

### React

- `Inter` como sans principal
- `Manrope` como display
- `JetBrains Mono` como mono
- `IBM Plex Sans` en configuracion de charts

Evidencia:

- `app/src/styles.css:1`
- `app/src/styles.css:32-34`
- `app/src/lib/chartConfig.js:25`
- `app/src/sections/CapitalHumanoSection.jsx:42`

## Diagnostico

El problema no es que las fuentes actuales sean malas. El problema es que el sistema esta fragmentado.

Hoy hay tres voces simultaneas:

- una voz de producto generica (`Inter`)
- una voz de titulo fuerte (`Manrope`)
- una voz tecnica dispersa (`JetBrains Mono` / `IBM Plex Sans`)

Resultado:

- la UI es legible, pero no memorable
- los charts parecen de otro sistema
- la marca editorial del anuario no queda fijada

## Fuentes evaluadas

### Opcion A: Geist solo

Fortalezas:

- excelente para UI
- muy buena lectura en interfaces densas
- limpia, precisa, contemporanea
- resuelve bien producto y datos

Riesgos:

- puede dejar al anuario demasiado "software product"
- pierde un poco de espesor editorial en aperturas y titulares largos

Lectura:

- muy buena para shell, tablas, filtros, cards, deltas y metadata

### Opcion B: Geist + Sentient

Fortalezas:

- Geist ordena la interfaz
- Sentient aporta tono editorial en los momentos correctos
- permite que el anuario se sienta institucional y publicado, no solo dashboardizado

Riesgos:

- si Sentient se expande a KPIs, tablas o widgets, el producto pierde precision
- exige disciplina fuerte de roles

Lectura:

- mejor balance entre producto digital y publicacion institucional

### Opcion C: Sentient primero

Fortalezas:

- mucha personalidad
- tono editorial mas evidente

Riesgos:

- tension con dashboards, tooltips, labels y navegacion densa
- puede fatigar en UI frecuente
- aumenta el riesgo de que la web parezca mas revista que sistema anual

## Recomendacion final

Recomiendo `Geist Sans + Geist Mono + Sentient`, con esta regla:

- `Geist Sans` manda en toda la interfaz
- `Geist Mono` se reserva para metadata y microdato tecnico
- `Sentient` se usa solo como display editorial controlado

No recomiendo `Sentient` como fuente principal de interfaz ni como fuente numerica.

## Sistema propuesto por rol

### `display`

Fuente:

- `Sentient`

Usos:

- h1 de portada
- apertura de seccion
- quotes o titulares editoriales de maximo 2 lineas

Reglas:

- usar pocas veces por pagina
- evitar pesos muy extremos en pantallas chicas
- no usar en cuerpos largos

### `heading`

Fuente:

- `Geist Sans`

Usos:

- h2, h3, h4
- titulos de cards
- encabezados de bloques

Reglas:

- peso 600-700
- tracking contenido
- jerarquia por tamano y espaciado, no por artificio

### `body`

Fuente:

- `Geist Sans`

Usos:

- parrafos
- notas
- explicaciones metodologicas
- copy de apoyo

Reglas:

- 16px base minimo
- line-height generoso
- priorizar claridad sobre personalidad

### `label`

Fuente:

- `Geist Sans`

Usos:

- botones
- tabs
- labels de formularios
- nombres de controles

Reglas:

- evitar caps excesivo salvo micro-eyebrows
- usar pesos medios
- no competir con titulos

### `data`

Fuente:

- `Geist Sans` con tabular figures

Usos:

- KPIs grandes
- celdas de tabla
- comparaciones
- montos
- porcentajes

Reglas:

- usar `font-variant-numeric: tabular-nums`
- evitar serif en valores primarios
- mantener peso 600-700

### `caption`

Fuente:

- `Geist Sans`

Usos:

- pies de grafico
- ayudas cortas
- notas al pie
- copy secundario

Reglas:

- contraste suficiente
- no bajar de legibilidad movil

### `mono`

Fuente:

- `Geist Mono`

Usos:

- fechas de corte
- codigos
- fuentes maestras
- tooltips tecnicos
- labels de ejes, chips y metadata corta

Reglas:

- usarla como acento tecnico
- no convertirla en voz dominante del producto

## Donde NO usar Sentient

No usar `Sentient` en:

- sidebar
- navbar
- rail de secciones
- year switcher
- badges
- chips
- tablas
- leyendas
- ejes
- tooltips
- KPIs numericos
- labels de mapa
- botones
- formularios

Si Sentient entra en esas zonas, la interfaz se vuelve menos precisa y mas teatral de lo necesario.

## Donde SI usar Sentient

Si usar `Sentient` en:

- portada del anuario
- apertura de una seccion larga
- titulares editoriales de Panorama o Vinculacion
- piezas de "lectura editorial" donde el texto introduce, no donde mide

## Aplicacion recomendada al producto

### Sitio vigente

Aplicar la migracion tipografica en este orden:

1. reemplazar `Inter` por `Geist Sans`
2. reemplazar `Manrope` por una combinacion `Geist Sans` + `Sentient`
3. sustituir la mono actual por `Geist Mono`
4. normalizar charts, tooltips y leyendas al mismo sistema

### Base React

La app futura debe quedar asi:

- shell: `Geist Sans`
- metadata: `Geist Mono`
- apertura hero y editoriales clave: `Sentient`
- charts: `Geist Sans` + `Geist Mono`

## Reglas de implementacion futura

1. No mezclar mas de tres familias activas.
2. No introducir una fuente distinta solo para charts.
3. No usar Sentient por default en todos los titulos.
4. No convertir la mono en fuente de cuerpo.
5. Mantener tabular nums en data-heavy views.
6. Cerrar un token por rol antes de tocar seccion por seccion.

## Decision resumida

Si hubiera que decidir hoy:

- `Geist Sans` para interfaz y lectura base
- `Geist Mono` para precision tecnica
- `Sentient` solo para momentos editoriales puntuales

Esa combinacion le da al anuario lo mejor de ambos mundos:

- claridad de producto,
- tono institucional,
- y una firma editorial suficiente para que no se sienta como un dashboard generico.

## Referencias externas revisadas

- Geist, Vercel Design System: https://vercel.com/geist/introduction
- Sentient Typeface, Noopur Choksi / Fontshare: https://www.noopurchoksi.com/design/sentient-typeface
