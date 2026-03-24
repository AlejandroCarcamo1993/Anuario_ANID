# Arquitectura del Proyecto

## Capas

### 1. Sitio legado

Archivo principal:

- `index.html`

Uso:

- refleja el estado actual del sitio existente
- puede seguir recibiendo cambios puntuales, pero ya no debe ser la base de crecimiento

### 2. Nueva app

Directorio:

- `app/`

Uso:

- capa React/Vite para desacoplar datos, UI y validacion
- pensada para recibir 2024, 2025 y futuros anos via JSON

## Datos

Directorio:

- `data/`

Regla:

- un archivo JSON por ano
- mismo contrato entre anos

Ejemplos:

- `data/2024.json`
- `data/2025.json` cuando exista

## Validacion

Directorio:

- `scripts/`

Piezas clave:

- `validate.js`: chequeos de consistencia
- `scaffold-year.js`: base para nuevos anos

## Evidencia y trazabilidad

### Reportes

- `reportes/` guarda auditorias, comparaciones y hallazgos

### Handoff

- `handoff/` guarda estado para continuidad entre modelos o sesiones

### Screenshots

- `screenshots/` guarda evidencia visual de QA

## Referencias de diseno

Fuentes actuales:

- `stitch (3).zip`
- `stitch_extracted/`
- reportes de auditoria UX/UI

## Recomendacion Estructural

La evolucion correcta es:

1. `data/` como fuente de verdad
2. `app/` como interfaz principal
3. `index.html` solo como legacy hasta reemplazo controlado
