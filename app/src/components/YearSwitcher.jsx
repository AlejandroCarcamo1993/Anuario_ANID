export function YearSwitcher({ years, activeYear, onChange }) {
  return (
    <div className="year-switcher" aria-label="Anuarios disponibles">
      {years.map((year) => {
        const active = year === activeYear
        return (
          <button
            key={year}
            type="button"
            className={active ? 'year-pill is-active' : 'year-pill'}
            onClick={() => onChange(year)}
            aria-pressed={active}
            aria-label={`Abrir anuario ${year}`}
          >
            <span className="year-pill__label">Anuario</span>
            <strong>{year}</strong>
          </button>
        )
      })}
    </div>
  )
}
