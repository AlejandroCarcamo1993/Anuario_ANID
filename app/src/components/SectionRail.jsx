export function SectionRail({ sections, activeSection, onSelect }) {
  return (
    <nav className="section-rail" aria-label="Secciones del anuario">
      {sections.map((item) => {
        const active = item.key === activeSection
        return (
          <button
            key={item.key}
            type="button"
            className={active ? 'section-rail__item is-active' : 'section-rail__item'}
            onClick={() => onSelect(item.key)}
            aria-pressed={active}
            aria-label={`Abrir seccion ${item.number} ${item.title}`}
          >
            <span className="section-rail__index">{item.number}</span>
            <span className="section-rail__copy">
              <strong>{item.title}</strong>
              <small>{item.label}</small>
            </span>
          </button>
        )
      })}
    </nav>
  )
}
