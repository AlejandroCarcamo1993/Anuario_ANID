import { useState } from 'react'
import { ParticleCard } from '../components/MagicBento/MagicBento'

const ChevronIcon = () => (
  <svg width="14" height="14" viewBox="0 0 14 14" fill="none" aria-hidden="true">
    <path d="M3 5l4 4 4-4" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"/>
  </svg>
)

function AgendaAccordion({ dimension }) {
  const [openIndex, setOpenIndex] = useState(null)
  const toggle = (i) => setOpenIndex(openIndex === i ? null : i)

  return (
    <section className={`agenda-track agenda-track--${dimension.id}`}>
      <header className="agenda-track__header">
        <div>
          <small>{dimension.colorLabel}</small>
          <h4>{dimension.title}</h4>
        </div>
        <span className="pill-soft">{dimension.count}</span>
      </header>

      <div className="agenda-accordion">
        {dimension.activities.map((activity, i) => {
          const isOpen = openIndex === i
          return (
            <div key={activity.title} className={`accord-item${isOpen ? ' accord-item--open' : ''}`}>
              <button
                type="button"
                className="accord-trigger"
                onClick={() => toggle(i)}
                aria-expanded={isOpen}
              >
                <span className={`accord-trigger__badge accord-trigger__badge--${dimension.id}`}>
                  {activity.date}
                </span>
                <span className="accord-trigger__title">{activity.title}</span>
                <span className="accord-trigger__chevron">
                  <ChevronIcon />
                </span>
              </button>

              <div className="accord-body-wrap">
                <div className="accord-body">
                  <p className="accord-body__objective">{activity.objective}</p>
                  <div className="accord-body__meta">
                    <span className="accord-body__place">{activity.place}</span>
                    <span className="accord-body__actors">{activity.actors}</span>
                  </div>
                </div>
              </div>
            </div>
          )
        })}
      </div>
    </section>
  )
}

export function VinculacionSection({ section, formatValue }) {
  const totalDimensions = section.dimensions.length
  const totalActivities = section.dimensions.reduce((acc, item) => acc + item.activities.length, 0)
  const agendaYear = section.agendaYear ?? '—'

  return (
    <div className="uve-shell">
      <div className="uve-hero-grid">
        <article className="lead-card uve-editorial">
          <span className="eyebrow">Resumen UVE</span>
          <h3>{section.summary.title}</h3>
          <p>{section.summary.lead}</p>

          <div className="uve-summary-strip">
            <div className="uve-summary-chip">
              <small>Dimensiones</small>
              <strong>{formatValue(totalDimensions, 'integer')}</strong>
            </div>
            <div className="uve-summary-chip">
              <small>Actividades</small>
              <strong>{formatValue(totalActivities, 'integer')}</strong>
            </div>
            <div className="uve-summary-chip">
              <small>Hallazgos</small>
              <strong>{formatValue(section.scientificHighlights.selectedCount, 'integer')}</strong>
            </div>
          </div>
        </article>

        <article className="panel-card uve-source-card">
          <span className="eyebrow">Criterio editorial</span>
          <p>{section.sourceNote}</p>
          <div className="source-cloud">
            {section.dimensions.map((dimension) => (
              <span key={dimension.id} className="source-pill source-pill--dark">
                {dimension.colorLabel} · {dimension.count}
              </span>
            ))}
          </div>
        </article>
      </div>

      <div className="uve-dimension-grid">
        {section.dimensions.map((dimension) => (
          <ParticleCard
            key={dimension.id}
            className={`dimension-card dimension-card--${dimension.id}`}
            glowColor="52, 79, 159"
            enableTilt={false}
            clickEffect={true}
            enableMagnetism={true}
          >
            <span className="eyebrow">{dimension.colorLabel}</span>
            <h4>{dimension.title}</h4>
            <p>{dimension.description}</p>
            <div className="dimension-meta">
              <span className="pill-soft">{dimension.badge}</span>
              <span className="pill-accent">{dimension.timeframe}</span>
            </div>
          </ParticleCard>
        ))}
      </div>

      <article className="panel-card agenda-card">
        <span className="eyebrow">Agenda {agendaYear}</span>
        <div className="agenda-grid">
          {section.dimensions.map((dimension) => (
            <AgendaAccordion key={dimension.id} dimension={dimension} />
          ))}
        </div>
      </article>

      <article className="panel-card highlight-wall">
        <span className="eyebrow">Hallazgos científicos destacados</span>
        <div className="mini-grid">
          {section.scientificHighlights.items.map((item) => (
            <article key={item.title} className="highlight-card">
              <div className="highlight-card__top">
                <small>{item.date}</small>
                <span className="pill-accent">{item.programs}</span>
              </div>
              <strong>{item.title}</strong>
              <p>{item.summary}</p>
              <div className="source-cloud">
                {item.tags.map((tag) => (
                  <span key={tag} className="source-pill">{tag}</span>
                ))}
              </div>
            </article>
          ))}
        </div>
      </article>
    </div>
  )
}
