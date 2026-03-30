import { Bar } from 'react-chartjs-2'
import { C, tip, xAxis, yAxis } from '../lib/chartConfig'

export function DiversidadSection({ section, formatValue }) {
  const sorted = [...section.femaleParticipationByInstrument]
    .sort((a, b) => b.valuePct - a.valuePct)

  const barData = {
    labels: sorted.map((i) => i.instrument),
    datasets: [{
      label: 'Participación femenina %',
      data: sorted.map((i) => i.valuePct),
      backgroundColor: sorted.map((i) =>
        i.valuePct >= 48 ? C.teal : i.valuePct >= 36 ? C.copper : C.rose
      ),
      borderRadius: 5,
      borderSkipped: false,
    }],
  }

  const barOpts = {
    indexAxis: 'y',
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { display: false },
      tooltip: {
        ...tip,
        callbacks: {
          label: (ctx) => ` ${ctx.raw.toFixed(1).replace('.', ',')}% participación femenina`,
          afterBody: () => ['50% = paridad'],
        },
      },
    },
    scales: {
      x: xAxis({
        max: 100,
        ticks: { callback: (v) => `${v}%` },
      }),
      y: yAxis(),
    },
  }

  return (
    <div className="diversity-shell">
      <div className="diversity-grid">
        <article className="lead-card diversity-hero">
          <span className="eyebrow">Paridad e inclusión</span>
          <h3>La fotografía general sigue lejos de la paridad, pero algunos instrumentos ya muestran mejores señales.</h3>
          <p>
            La razón hombres/mujeres es {section.leadership.razonHM.toFixed(2)} y el liderazgo
            femenino mejora en equipos jóvenes ({formatValue(section.leadership.liderazgoJovenesPct, 'percentage')}).
          </p>
          <div className="diversity-band">
            <div className="diversity-band__item">
              <small>Part. femenina</small>
              <strong>{formatValue(section.kpis.find((k) => k.id === 'mujeresPct')?.value ?? 0, 'percentage')}</strong>
            </div>
            <div className="diversity-band__item">
              <small>Liderazgo directivo</small>
              <strong>{formatValue(section.leadership.directivoFemeninoPct, 'percentage')}</strong>
            </div>
            <div className="diversity-band__item">
              <small>Investigadoras jóvenes</small>
              <strong>{formatValue(section.leadership.liderazgoJovenesPct, 'percentage')}</strong>
            </div>
          </div>
        </article>

        <article className="panel-card diversity-sidecard">
          <span className="eyebrow">Indicadores de liderazgo</span>

          <div className="diversity-total-row">
            <span className="diversity-total-row__num">
              {section.kpis.find((k) => k.id === 'total')?.value ?? '—'}
            </span>
            <span className="diversity-total-row__label">Investigadoras e investigadores principales</span>
          </div>

          <div className="leader-stat-list">
            {[
              {
                label: 'Paridad global',
                note: 'Razón H/M · 1.0 = paridad',
                display: section.leadership.razonHM.toFixed(2),
                pct: Math.round((1 / (1 + section.leadership.razonHM)) * 100),
                color: '#344F9F',
              },
              {
                label: 'Liderazgo directivo',
                note: 'Cargos de dirección femeninos',
                display: formatValue(section.leadership.directivoFemeninoPct, 'percentage'),
                pct: section.leadership.directivoFemeninoPct,
                color: '#E75D50',
              },
              {
                label: 'Investigadoras',
                note: 'Participación en investigación',
                display: formatValue(section.leadership.liderazgoInvestigadorasPct, 'percentage'),
                pct: section.leadership.liderazgoInvestigadorasPct,
                color: '#00566c',
              },
              {
                label: 'Jóvenes científicas',
                note: 'Liderazgo en tramos menores de 35',
                display: formatValue(section.leadership.liderazgoJovenesPct, 'percentage'),
                pct: section.leadership.liderazgoJovenesPct,
                color: '#7c3aed',
              },
            ].map((stat) => (
              <div key={stat.label} className="leader-stat">
                <div className="leader-stat__header">
                  <span className="leader-stat__label">{stat.label}</span>
                  <strong className="leader-stat__value" style={{ color: stat.color }}>{stat.display}</strong>
                </div>
                <div className="leader-stat__track">
                  <div
                    className="leader-stat__fill"
                    style={{ width: `${Math.min(100, stat.pct)}%`, background: stat.color }}
                  />
                  <div className="leader-stat__parity" />
                </div>
                <small className="leader-stat__note">{stat.note}</small>
              </div>
            ))}
          </div>
        </article>
      </div>

      <article className="panel-card">
        <span className="eyebrow">Participación femenina por instrumento</span>
        <div className="chart-wrap chart-wrap--hbar">
          <Bar data={barData} options={barOpts} aria-label="Gráfico de barras horizontal: participación femenina por instrumento" role="img" />
        </div>
      </article>
    </div>
  )
}
