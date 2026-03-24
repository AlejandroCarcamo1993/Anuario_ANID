# Instructivo de Uso del Repositorio

## 1. Instalar dependencias

```bash
npm install
```

## 2. Revisar datos

Validacion base:

```bash
npm run validate:data
```

Validacion estricta:

```bash
npm run validate:data:strict
```

## 3. Trabajar en la nueva app

Desarrollo:

```bash
npm run app:dev
```

Build:

```bash
npm run app:build
```

Preview:

```bash
npm run app:preview
```

## 4. Agregar un nuevo ano

Generar base:

```bash
npm run scaffold:year -- 2025
```

Luego:

1. poblar `data/2025.json`
2. documentar fuentes
3. correr validacion
4. registrar el cambio en `CHANGELOG.md`

## 5. Crear una auditoria o reporte

Ubicacion:

- `reportes/`

Nombre recomendado:

```text
tema_descripcion_YYYY-MM-DD.md
```

Ejemplos:

- `auditoria_ux_ui_anuario_institucional_2026-03-24.md`
- `comparacion_pdf_vs_sitio_2026-03-24.md`

## 6. Registrar relevo o continuidad

Ubicacion:

- `handoff/`

Usar cuando:

- cambia el modelo
- se corta una sesion
- se deja una linea de trabajo abierta

## 7. Antes de cada commit

Checklist minima:

1. `npm run validate:data`
2. `npm run app:build` si cambiaste `app/`
3. revisar `git status`
4. resumir el avance en `CHANGELOG.md` si corresponde
