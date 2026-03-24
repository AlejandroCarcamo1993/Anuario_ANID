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
          <div className="ratio-grid">
            <div><small>Razón H/M</small><strong>{section.leadership.razonHM.toFixed(2)}</strong></div>
            <div><small>Directivo</small><strong>{formatValue(section.leadership.directivoFemeninoPct, 'percentage')}</strong></div>
            <div><small>Investigación</small><strong>{formatValue(section.leadership.liderazgoInvestigadorasPct, 'percentage')}</strong></div>
            <div><small>Jóvenes</small><strong>{formatValue(section.leadership.liderazgoJovenesPct, 'percentage')}</strong></div>
          </div>
        </article>
      </div>

      <article className="panel-card">
        <span className="eyebrow">Participación femenina por instrumento</span>
        <div className="chart-wrap chart-wrap--hbar">
          <Bar data={barData} options={barOpts} />
        </div>
      </article>
    </div>
  )
}
