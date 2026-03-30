# Anuario SCIA - Contexto del Agente

## Proyecto

**Anuario Virtual Institucional SCIA** — Plataforma web interactiva de datos anuales de productividad científica para SCIA (Sistema de Centros e Institutos Asociados de ANID, Chile). Año de datos: 2024.

---

## Stack Tecnológico

- **HTML5** semántico con **Tailwind CSS** (vía CDN + configuración personalizada)
- **Fuentes**: Manrope (display/headlines) + Inter (body/títulos) + Material Symbols Outlined (iconos)
- **Charts**: A definir (preferir librerías ligeras compatibles con Tailwind)
- **Datos**: Excel (.xlsx) → procesados vía Python (`phase12.py`, `phase3.py`)
- **Prototipo base**: `stitch_extracted/stitch/` (4 pantallas HTML)

---

## Sistema de Diseño: "The Ethereal Archive"

### Filosofía
Transformar datos institucionales en una experiencia digital viva. **Luminous Depth** como norte creativo: glassmorphism + asimetría intencional + profundidad tonal. No es un documento estático; es un ecosistema traslúcido sofisticado.

### Paleta de Colores (Tailwind custom tokens)

```
primary:              #00396b   (azul institucional ANID)
primary-container:    #005092
secondary:            #bc0004   (rojo institucional)
on-surface:           #0b1c30   (NUNCA usar #000000 puro)
surface:              #f8f9ff   (canvas base)
surface-container:    #e5eeff
surface-container-low:#eff4ff
surface-container-lowest: #ffffff
tertiary:             #003d4e
tertiary-fixed-dim:   #59d5fe
outline-variant:      #c2c6d2
error:                #ba1a1a
```

### Reglas de Diseño Críticas

**HACER:**
- Glassmorphic cards: `background: rgba(255,255,255,0.7)`, `backdrop-filter: blur(16px)`, `border-radius: 1.5rem`
- Gradientes en hero/CTAs: `linear-gradient(135deg, #00396b, #005092)`
- Separar secciones por cambio de color, NO por líneas divisorias
- Superponer elementos para crear profundidad
- `font-mono` (peso 15%) para metadatos: fechas, códigos, etiquetas "SCIA-2024"
- Sombras ultra-difusas: `box-shadow: 0 20px 40px rgba(11,28,48,0.06)`
- Bordes fantasma para accesibilidad: `outline-variant` al 15% de opacidad

**NO HACER:**
- Bordes sólidos 1px de alto contraste
- Sombras estilo Material Design (demasiado pesadas)
- Líneas divisorias en listas (usar `gap-2` + hover sutil)
- Negro puro `#000000`
- Glassmorphism en texto pequeño (ilegible)

### Tipografía

| Rol | Familia | Tamaño | Peso | Tracking |
|-----|---------|--------|------|---------|
| Display/Hero | Manrope | 3.5rem | 800 | -0.02em |
| Título sección | Manrope | 1.75rem | 700 | -0.01em |
| Subtítulo | Inter | 1.375rem | 600 | normal |
| Body | Inter | 0.875rem | 400 | normal |
| Metadatos | Monospace | 0.75rem | 500 | 0.05em |

### Elevación (sin sombras convencionales)

1. **Base**: `surface` (#f8f9ff)
2. **Agrupación**: `surface-container` (#e5eeff)
3. **Cards flotantes**: `surface-container-lowest` blanco 70% + blur 16px
4. **Modales/dropdowns**: sombra difusa tintada en azul

---

## Pantallas Existentes (Prototipos en `stitch_extracted/`)

| Pantalla | Archivo |
|----------|---------|
| Home Anuario SCIA | `home_anuario_scia/code.html` |
| Dashboard Centros de Investigación | `dashboard_centros_de_investigacion/code.html` |
| Postulaciones y Adjudicaciones | `postulaciones_y_adjudicaciones/code.html` |
| Concentración Regional de la Ciencia | `concentracion_regional_de_la_ciencia/code.html` |

---

## Datos Disponibles (2024)

Todos en `datos_2024/Información de Productividad SCIA 2024/`:

- `Publicaciones Centros 2024.xlsx` / `Publicaciones Milenio 2024.xlsx`
- `Presentaciones a Congresos Centros 2024.xlsx` / `Milenio 2024.xlsx`
- `Formación de Capital Humano Centros 2024.xlsx` / `Milenio 2024.xlsx`
- `Patentes - Propiedad Intelectual Centros 2024.xlsx` / `Milenio 2024.xlsx`
- `Actividades de Divulgación Centros 2024.xlsx` / `Milenio 2024.xlsx`
- `Ejecución Presupuestaria 2024 y 2025/Caja 2024 - 2025.xlsx`

Dos categorías de centros: **Centros** (FONDAP/Basal) y **Milenio**.

---

## Skills UX/UI Instaladas

| Skill | Uso principal |
|-------|--------------|
| `ui-ux-pro-max` | Decisiones de diseño, estilos, paletas, tipografía, charts |
| `frontend-design` | Generación de interfaces HTML/CSS de alta calidad |
| `shadcn-ui` | Componentes React accesibles si se migra a React |
| `web-accessibility` | Cumplimiento WCAG 2.1, ARIA, teclado |
| `web-design-guidelines` | Revisión y auditoría de UI |

**Workflow recomendado para nuevas pantallas:**
1. `/ui-ux-pro-max` → planificar estructura y estilo
2. `/frontend-design` → generar código HTML/Tailwind
3. `/web-accessibility` → revisar accesibilidad
4. `/web-design-guidelines` → auditoría final

---

## Contexto Institucional

- **SCIA**: Sistema de Centros e Institutos Asociados — programa de ANID (Agencia Nacional de Investigación y Desarrollo, Chile)
- **Audiencia**: Directivos ANID, investigadores, público general interesado en ciencia chilena
- **Tono**: Institucional pero moderno, sofisticado, basado en datos
- **Idioma**: Español (Chile)
- **Mapa**: Incluye `mapa-chile.svg` para visualizaciones regionales
