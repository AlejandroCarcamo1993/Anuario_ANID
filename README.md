# Anuario ANID / SCIA

Repositorio de trabajo para la evolucion del Anuario SCIA hacia una base trazable, validable y mantenible. El proyecto convive hoy en dos capas:

1. `index.html`: sitio legado actualmente publicado.
2. `app/`: nueva base React/Vite orientada a datos estructurados por ano.

La prioridad del repositorio es **no perder decisiones, evidencia ni reconciliaciones de datos** mientras se avanza hacia 2025 y futuras ediciones.

## Objetivos

- Mantener trazabilidad de fuentes, auditorias y decisiones.
- Separar datos, presentacion y validacion.
- Tener una base profesional para trabajo continuo con varios modelos o colaboradores.
- Versionar tanto el sitio legado como la nueva capa React sin mezclar responsabilidades.

## Estado Actual

- Existe un dataset estructurado en `data/2024.json`.
- Hay validaciones automaticas en `scripts/validate.js`.
- La base React ya consume el contrato de datos y cubre las 8 secciones del anuario 2024.
- Se realizaron auditorias de contenido, datos, UVE y UX/UI en `reportes/`.

## Estructura Principal

```text
app/                  Shell React/Vite para la nueva experiencia
data/                 Datos estructurados por ano
scripts/              Validacion, scaffolds y utilidades operativas
reportes/             Auditorias, comparaciones, instructivos y extracciones
handoff/              Estado para relevo entre modelos o sesiones
tools/                Scripts puntuales de extraccion y revision
screenshots/          Evidencia visual generada durante QA
datos_2024/           Insumos de trabajo 2024
datos_2025/           Insumos preliminares 2025
stitch_extracted/     Referencias visuales extraidas desde stitch
index.html            Sitio legado actual
mapa-chile.svg        Mapa usado por legacy y shell React
```

## Comandos Principales

Instalacion:

```bash
npm install
```

Validacion de datos:

```bash
npm run validate:data
npm run validate:data:strict
```

Shell React:

```bash
npm run app:dev
npm run app:build
npm run app:preview
```

Scaffold de un nuevo ano:

```bash
npm run scaffold:year -- 2025
```

## Convenciones Operativas

- Toda nueva auditoria o decision relevante debe quedar en `reportes/` o `docs/`.
- No modificar `index.html` sin dejar evidencia y justificacion.
- Toda reconciliacion de datos debe pasar por `data/` y `scripts/validate.js`.
- Antes de commit:
  - correr `npm run validate:data`
  - correr `npm run app:build` si se tocaron archivos en `app/`

## Documentacion Base

- [Contributing](./CONTRIBUTING.md)
- [Changelog](./CHANGELOG.md)
- [Arquitectura](./docs/ARQUITECTURA.md)
- [Instructivo de uso](./docs/INSTRUCTIVO_USO.md)
- [Trazabilidad](./docs/TRAZABILIDAD.md)

## Riesgos Conocidos

- El bundle de la app React aun es grande y debe dividirse por seccion o por ano.
- Existen advertencias conocidas del dataset 2024 que no deben esconderse; deben seguir documentadas.
- El sitio legado y la nueva app conviven, por lo que hay que evitar mezclar cambios de una capa con la otra.
- Hay archivos binarios grandes en el repo; para futuras cargas pesadas conviene migrar a Git LFS o a una estrategia de artefactos versionados.

## Regla General

Si una decision no queda versionada en codigo, datos o markdown, esa decision se pierde.

## Politica de Binarios

Ver [docs/POLITICA_BINARIOS.md](./docs/POLITICA_BINARIOS.md).
