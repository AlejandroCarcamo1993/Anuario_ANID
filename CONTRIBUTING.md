# Contributing

## Principios

1. Preservar trazabilidad.
2. No romper el sitio legado por accidente.
3. Separar claramente datos, presentacion y evidencia.
4. Documentar antes de olvidar.

## Tipos de Cambio

Usar prefijos simples en commits:

- `docs:` documentacion, auditorias, instructivos
- `data:` actualizaciones de JSON, conciliaciones, nuevas fuentes
- `app:` cambios en la base React/Vite
- `legacy:` cambios en `index.html` o recursos del sitio actual
- `scripts:` utilidades, validadores, scaffolds
- `qa:` capturas, chequeos visuales y verificaciones

## Flujo Recomendado

1. Crear o actualizar evidencia en `reportes/` o `docs/`.
2. Modificar codigo o datos.
3. Ejecutar validaciones:
   - `npm run validate:data`
   - `npm run app:build` si aplica
4. Revisar `git status`.
5. Commit corto y claro.

## Antes de Tocar `index.html`

Solo tocar el sitio legado si:

- el cambio es urgente para publicacion,
- no existe aun equivalente funcional en `app/`,
- y queda documentado en `reportes/` o `CHANGELOG.md`.

## Antes de Agregar un Nuevo Ano

1. Generar scaffold:
   - `npm run scaffold:year -- 2025`
2. Crear o poblar `data/2025.json`
3. Ejecutar validacion
4. Documentar fuentes y supuestos

## Evidencia Minima por Tarea Relevante

Cada tarea importante debe dejar al menos uno de estos artefactos:

- un `.md` en `reportes/`
- una actualizacion en `CHANGELOG.md`
- un archivo en `handoff/`

## Pull Requests

Usar el template definido en `.github/pull_request_template.md`.
