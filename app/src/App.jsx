import { useEffect, useMemo, useState } from 'react'
import { AnimatePresence, motion } from 'framer-motion'
import { availableYears, getYearData } from './dataRegistry'
import { YearSwitcher } from './components/YearSwitcher'
import { SectionRail } from './components/SectionRail'
import { MetricStrip } from './components/MetricStrip'
import { formatValue } from './lib/formatters'
import { getSectionComponent, getSectionMetrics } from './sectionRegistry'
import { GenericSection } from './sections/GenericSection'

function SectionContent({ sectionKey, section }) {
  if (section?._pending) return <GenericSection section={section} />
  const Component = getSectionComponent(sectionKey)
  return <Component sectionKey={sectionKey} section={section} formatValue={formatValue} />
}

export default function App() {
  const [activeYear, setActiveYear] = useState(availableYears.at(-1) ?? 2024)
  const currentData = useMemo(() => getYearData(activeYear), [activeYear])
  const [activeSection, setActiveSection] = useState(currentData?.sectionOrder?.[0] ?? '')

  useEffect(() => {
    if (!currentData) return
    setActiveSection((current) => (
      currentData.sectionOrder.includes(current) ? current : currentData.sectionOrder[0]
    ))
  }, [currentData])

  if (!currentData) {
    return (
      <main className="app-shell">
        <div className="empty-state">
          <h1>No hay datos cargados.</h1>
          <p>Agrega un archivo JSON en /data para activar el shell de migracion.</p>
        </div>
      </main>
    )
  }

  const sectionList = currentData.sectionOrder.map((key) => ({
    key,
    number: currentData.sections[key].sectionNumber,
    title: currentData.sections[key].title,
    label: currentData.sections[key].tagLabel || currentData.sections[key].navLabel
  }))

  const activeData = currentData.sections[activeSection]
  const metrics = getSectionMetrics(activeSection, activeData)
  const shellStats = [
    { label: 'Secciones', value: currentData.sectionOrder.length },
    { label: 'Fuentes', value: currentData.footer.sources.length },
    { label: 'Corte', value: currentData.footer.lastDataCut },
  ]

  return (
    <main className="app-shell">
      <a className="skip-link" href="#main-content">Saltar al contenido</a>
      <div className="ambient ambient--top" />
      <div className="ambient ambient--bottom" />

      <header className="app-topbar">
        <div className="app-topbar__brand">
          <span className="brand-mark__kicker">ANID / SCIA</span>
          <strong className="brand-mark__label">Anuario Institucional</strong>
        </div>

        <div className="app-topbar__tabs" aria-label="Contexto de lectura">
          <span className="app-topbar__tab is-active">Exploración Anual</span>
          <span className="app-topbar__tab">Arquitectura React</span>
          <span className="app-topbar__tab">Esquema de Datos</span>
        </div>

        <div className="app-topbar__meta">
          <span className="app-topbar__chip">Corte {currentData.footer.lastDataCut}</span>
          <span className="app-topbar__chip app-topbar__chip--accent">{activeYear}</span>
        </div>
      </header>

      <aside className="sidebar">
        <div className="brand-block">
          <span className="brand-block__eyebrow">Archivo Institucional</span>
          <h1>Anuario Institucional SCIA</h1>
          <p>
            Plataforma interactiva de datos científicos institucionales de Chile.
            Productividad, financiamiento e impacto del ecosistema SCIA año a año.
          </p>
        </div>

        <YearSwitcher
          years={availableYears}
          activeYear={activeYear}
          onChange={setActiveYear}
        />

        <div className="sidebar-panel">
          <span className="eyebrow">Cobertura</span>
          <div className="ratio-grid">
            {shellStats.map((item) => (
              <div key={item.label}>
                <small>{item.label}</small>
                <strong>{item.value}</strong>
              </div>
            ))}
          </div>
        </div>

        <div className="sidebar-note">
          <span className="eyebrow">Corte de datos</span>
          <div className="sidebar-note__date">
            <span className="sidebar-note__chip">{currentData.footer.lastDataCut}</span>
          </div>
          <p>Bases de proyectos, investigadores y ejecución presupuestaria SCIA.</p>
        </div>

        <SectionRail
          sections={sectionList}
          activeSection={activeSection}
          onSelect={setActiveSection}
        />

        <div className="sidebar-panel sidebar-panel--sources">
          <span className="eyebrow">Fuentes maestras</span>
          <ul className="source-list">
            {currentData.footer.sources.map((item) => (
              <li key={item} className="source-list__item">
                <span className="source-list__dot" />
                <span>{item}</span>
              </li>
            ))}
          </ul>
        </div>
      </aside>

      <section className="workspace" id="main-content">
        <header className="workspace-hero">
          <div className="workspace-hero__copy">
            <span className="eyebrow">Anuario {activeYear}</span>
            <h2>{currentData.hero.title}</h2>
            <p>{currentData.hero.subtitle}</p>
          </div>
          <div className="hero-badges">
            {currentData.hero.statPills.map((item) => (
              <div key={item.label} className="hero-badge">
                <small>{item.label}</small>
                <strong>{typeof item.value === 'number' ? item.value.toLocaleString('es-CL') : item.value}</strong>
              </div>
            ))}
          </div>
        </header>

        <div className="workspace-meta">
          <span className="workspace-meta__item">
            <small>Organización</small>
            <strong>{currentData.footer.organization}</strong>
          </span>
          <span className="workspace-meta__item">
            <small>División</small>
            <strong>{currentData.footer.division}</strong>
          </span>
          <span className="workspace-meta__item">
            <small>Unidad</small>
            <strong>{currentData.footer.unit}</strong>
          </span>
        </div>

        <AnimatePresence mode="wait">
          <motion.article
            key={`${activeYear}-${activeSection}`}
            className="detail-shell"
            initial={{ opacity: 0, y: 18 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -14 }}
            transition={{ duration: 0.28, ease: 'easeOut' }}
          >
            <header className="detail-header">
              <div>
                <span className="eyebrow">{activeData.tagLabel || activeData.navLabel}</span>
                <h3>{activeData.title}</h3>
                <p>{activeData.subtitle}</p>
              </div>
              <div className="source-cloud">
                {activeData.sources.map((item) => (
                  <span key={item} className="source-pill source-pill--dark">{item}</span>
                ))}
              </div>
            </header>

            <MetricStrip items={metrics} formatter={formatValue} />

            <SectionContent sectionKey={activeSection} section={activeData} />

            {activeData.insights?.length > 1 && (
              <section className="insight-stack">
                {activeData.insights.slice(1).map((item) => (
                  <article key={item.title} className="insight-card">
                    <span className="eyebrow">{item.title}</span>
                    <p>{item.body}</p>
                  </article>
                ))}
              </section>
            )}
          </motion.article>
        </AnimatePresence>
      </section>
    </main>
  )
}
