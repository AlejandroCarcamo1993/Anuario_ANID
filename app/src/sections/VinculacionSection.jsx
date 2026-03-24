export function VinculacionSection({ section, formatValue }) {
  const totalDimensions = section.dimensions.length
  const totalActivities = section.dimensions.reduce((acc, item) => acc + item.activities.length, 0)

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
          <article key={dimension.id} className={`dimension-card dimension-card--${dimension.id}`}>
            <span className="eyebrow">{dimension.colorLabel}</span>
            <h4>{dimension.title}</h4>
            <p>{dimension.description}</p>
            <div className="dimension-meta">
              <span className="pill-soft">{dimension.badge}</span>
              <span className="pill-accent">{dimension.timeframe}</span>
            </div>
          </article>
        ))}
      </div>

      <article className="panel-card agenda-card">
        <span className="eyebrow">Agenda 2024</span>
        <div className="agenda-grid">
          {section.dimensions.map((dimension) => (
            <section key={dimension.id} className="agenda-track">
              <header className="agenda-track__header">
                <div>
                  <small>{dimension.colorLabel}</small>
                  <h4>{dimension.title}</h4>
                </div>
                <span className="pill-soft">{dimension.count}</span>
              </header>

              <div className="agenda-track__items">
                {dimension.activities.map((activity) => (
                  <article key={activity.title} className="activity-card">
                    <div className="activity-card__meta">
                      <span>{activity.date}</span>
                      <span>{activity.place}</span>
                    </div>
                    <strong>{activity.title}</strong>
                    <p>{activity.objective}</p>
                    <small>{activity.actors}</small>
                  </article>
                ))}
              </div>
            </section>
          ))}
        </div>
      </article>

      <article className="panel-card highlight-wall">
        <span className="eyebrow">Hallazgos cientificos destacados</span>
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
