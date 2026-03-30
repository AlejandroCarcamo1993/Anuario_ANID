# Requisitos de una Web para Presentar el Anuario

Fecha: 2026-03-27

## Escala de estado

- `Presente`: el requisito ya se resuelve de forma defendible.
- `Parcial`: existe, pero con huecos UX, editoriales o tecnicos.
- `Ausente`: no existe o no es visible para la persona usuaria.

## Checklist evaluada

| Requisito | Por que importa | Legacy `index.html` | React `app/` | Observacion |
| --- | --- | --- | --- | --- |
| Portada clara | Debe explicar que es el anuario y para quien es. | Presente | Presente | Ambos tienen hero fuerte. |
| Indice navegable | Un anuario digital necesita orientacion rapida. | Presente | Presente | Legacy por anclas; React por rail lateral. |
| Resumen ejecutivo | Ayuda a leer sin recorrer toda la pieza. | Parcial | Parcial | Hay KPIs y subtitulos, pero no un resumen ejecutivo como bloque formal. |
| Contexto metodologico | Sin metodologia, los datos pierden confianza. | Parcial | Parcial | La info existe dispersa en fuentes y JSON, no como experiencia dedicada. |
| Trazabilidad de fuentes | Imprescindible para uso institucional. | Presente | Presente | Buen avance en ambas capas. |
| Fecha de corte visible | Sin corte visible no hay confianza temporal. | Presente | Presente | Muy bien resuelto en React; legacy lo comunica por contexto y fuentes. |
| Narrativa por seccion | Debe sostener lectura larga y no solo dashboard. | Presente | Presente | Vinculacion y Panorama son buenos ejemplos. |
| Comparacion anual | Es una de las promesas mas importantes del producto. | Parcial | Parcial | Existe como intencion, no como patron maduro. |
| Estado compartible por URL | Permite mandar vistas exactas entre equipos. | Ausente | Ausente | Deuda critica para la app. |
| Charts accesibles | Sin alternativa textual y labels se pierde accesibilidad. | Parcial | Presente | React va mejor; legacy queda corto. |
| Mapa accesible sin mouse | Requisito basico de accesibilidad y uso real. | Ausente | Ausente | Mayor deuda compartida. |
| Version movil legible | El anuario debe sobrevivir en laptop y telefono. | Presente | Presente | Hay responsive en ambas capas. |
| Opcion de impresion | Util para institucionalidad y archivo. | Parcial | Parcial | Existe `print`, pero no una entrada visible al usuario. |
| Opcion de descarga | Mucha gente espera PDF o documento descargable. | Ausente | Ausente | Falta CTA y posicion editorial clara. |
| Cierre institucional | Debe cerrar con firma, alcance, fuentes y continuidad. | Presente | Parcial | Legacy cierra mejor hoy. |
| Estado de contenido pendiente | Necesario si 2025 o futuros anos no estan completos. | Parcial | Parcial | React tiene `_pending`, pero la experiencia aun no lo comunica con claridad suficiente. |
| Reglas para inconsistencias del dato | El producto debe explicar descuadres sin esconderlos. | Parcial | Presente | React ya muestra warnings en algunos bloques; falta sistematizar. |
| Sistema tipografico por roles | Un anuario digital necesita reglas, no familias sueltas. | Ausente | Ausente | La recomendacion vive en el artefacto tipografico, no en producto aun. |

## Marco minimo recomendado

### 1. Apertura

La web del anuario debe abrir con:

- portada clara
- subtitulo institucional
- corte de datos
- resumen ejecutivo corto
- acceso directo al indice
- acceso directo a descarga o impresion

### 2. Lectura

La experiencia debe permitir:

- navegar por secciones
- entender rapidamente que muestra cada bloque
- saber de donde sale el dato
- distinguir metricas, relato editorial y advertencias metodologicas
- compartir una vista concreta por URL

### 3. Confianza

La experiencia debe incluir:

- metodologia o nota editorial visible
- fuentes maestras
- fecha de corte
- advertencias de alcance
- version o edicion del anuario
- cierre institucional

### 4. Comparacion anual

La experiencia debe permitir:

- cambiar de ano sin perder contexto
- comparar anos con reglas claras
- identificar que se compara y que no
- mostrar estado `sin datos`, `parcial` o `pendiente`

### 5. Accesibilidad

La experiencia debe garantizar:

- `skip-link`
- foco visible
- reduced motion
- charts etiquetados
- mapas y filtros operables por teclado
- feedback dinamico con `aria-live`
- lectura movil sin friccion

### 6. Distribucion

La experiencia debe cubrir:

- lectura web
- impresion
- descarga
- referencias para ser citada o compartida

## Requisitos que hoy conviene priorizar

### Prioridad inmediata

1. Estado compartible por URL.
2. Metodologia y corte como capa visible.
3. Mapa accesible sin mouse.
4. Compare anual real o retirada temporal del patron.

### Prioridad siguiente

1. Descarga / impresion como feature visible.
2. Estados parciales por ano.
3. Alternativas textuales consistentes para charts del legacy.
4. Sistema tipografico unificado.

## Conclusiones

El proyecto ya cumple varias condiciones basicas de una web-anuario:

- tiene portada,
- indice,
- secciones,
- narrativa,
- trazabilidad parcial,
- y responsive.

Lo que todavia falta para quedar realmente "cerrado" como publicacion digital es la capa de confianza, comparacion y accesibilidad avanzada.
