export function MetricStrip({ items, formatter }) {
  return (
    <div className="metric-strip">
      {items.map((item) => (
        <article key={item.id || item.label} className="metric-card">
          <span className="metric-card__label">{item.label}</span>
          <strong className="metric-card__value">{formatter(item.value, item.format)}</strong>
        </article>
      ))}
    </div>
  )
}
