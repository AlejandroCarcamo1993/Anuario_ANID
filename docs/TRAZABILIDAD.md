# Trazabilidad del Trabajo

## Objetivo

Este repositorio debe permitir reconstruir:

- que se hizo,
- por que se hizo,
- con que fuente,
- y cual fue el resultado.

## Donde registrar cada cosa

### Datos

- `data/`

Guardar:

- JSON por ano
- reconciliaciones definitivas

### Decisiones

- `reportes/`
- `docs/`
- `CHANGELOG.md`

Guardar:

- criterios de diseño
- hallazgos
- decisiones de arquitectura
- comparaciones y auditorias

### Continuidad operativa

- `handoff/`

Guardar:

- estado del trabajo
- proximos pasos
- riesgos pendientes

### Evidencia visual

- `screenshots/`

Guardar:

- capturas de QA
- pruebas visuales antes/despues

## Reglas Practicas

1. Cada cambio importante debe dejar evidencia escrita.
2. Cada reconciliacion numerica debe citar fuente.
3. Cada cambio de diseño mayor debe quedar en un reporte o changelog.
4. Si una tarea queda incompleta, debe dejar handoff.

## Nombre de Archivos

### Reportes

```text
tema_descripcion_YYYY-MM-DD.md
```

### Handoff

```text
HANDOFF_YYYY-MM-DD.md
state.json
```

### Screenshots

```text
seccion_contexto_timestamp.png
```

## Minimo para no perder progreso

Antes de cerrar una sesion importante, dejar:

- un commit local
- un `CHANGELOG.md` actualizado
- y si aplica, un archivo en `handoff/`
