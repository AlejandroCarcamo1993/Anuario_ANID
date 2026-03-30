import { PanoramaSection } from './sections/PanoramaSection'
import { PostulacionSection } from './sections/PostulacionSection'
import { FinancieraSection } from './sections/FinancieraSection'
import { ProductividadSection } from './sections/ProductividadSection'
import { CapitalHumanoSection } from './sections/CapitalHumanoSection'
import { DiversidadSection } from './sections/DiversidadSection'
import { TerritorioSection } from './sections/TerritorioSection'
import { VinculacionSection } from './sections/VinculacionSection'
import { GenericSection } from './sections/GenericSection'

const registry = {
  panorama: {
    Component: PanoramaSection,
    getMetrics: (section) => section.kpis.slice(0, 5)
  },
  postulacion: {
    Component: PostulacionSection,
    getMetrics: (section) => section.kpis.slice(0, 4)
  },
  financiera: {
    Component: FinancieraSection,
    getMetrics: (section) => section.kpis.slice(0, 3)
  },
  productividad: {
    Component: ProductividadSection,
    getMetrics: (section) => [
      {
        id: 'publicaciones',
        label: 'Inst. Milenio',
        value: section.publicaciones.totalsByProgram[0].total,
        format: 'integer'
      },
      {
        id: 'tesis',
        label: 'Tesis',
        value: section.tesis.kpis[0].value,
        format: 'integer'
      },
      {
        id: 'congresos',
        label: 'Presentaciones',
        value: section.congresos.kpis[0].value,
        format: 'integer'
      },
      {
        id: 'divulgacion',
        label: 'Actividades',
        value: section.divulgacion.kpis[0].value,
        format: 'integer'
      }
    ]
  },
  capitalHumano: {
    Component: CapitalHumanoSection,
    getMetrics: (section) => section.kpis.slice(0, 5)
  },
  diversidad: {
    Component: DiversidadSection,
    getMetrics: (section) => section.kpis.slice(0, 5)
  },
  territorio: {
    Component: TerritorioSection,
    getMetrics: (section) => section.kpis.slice(0, 5)
  },
  vinculacion: {
    Component: VinculacionSection,
    getMetrics: (section) => section.kpis.slice(0, 3)
  }
}

export function getSectionComponent(sectionKey) {
  return registry[sectionKey]?.Component ?? GenericSection
}

export function getSectionMetrics(sectionKey, section) {
  if (section?._pending) return []
  try {
    return registry[sectionKey]?.getMetrics?.(section) ?? []
  } catch {
    return []
  }
}

export function getRegisteredSectionKeys() {
  return Object.keys(registry)
}
