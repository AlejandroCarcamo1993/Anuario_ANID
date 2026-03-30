import { Bar } from 'react-chartjs-2'
import { C, tip, xAxis, yAxis } from '../lib/chartConfig'

export function CapitalHumanoSection({ section, formatValue }) {
  const total  = section.kpis.find((k) => k.id === 'total')?.value  ?? 0
  const men    = section.kpis.find((k) => k.id === 'hombres')?.value ?? 0
  const women  = section.kpis.find((k) => k.id === 'mujeres')?.value ?? 0
  const pct35  = section.kpis.find((k) => k.id === 'tramo3554Pct')?.value ?? 0
  const ageWomen = section.agePyramid.reduce((a, r) => a + r.women, 0)
  const ageMen   = section.agePyramid.reduce((a, r) => a + r.men,   0)
  const ok = ageWomen === women && ageMen === men

  const labels = section.agePyramid.map((r) => r.ageRange)
  const pyramidData = {
    labels,
    datasets: [
      {
        label: 'Mujeres',
        data: section.agePyramid.map((r) => r.women),
        backgroundColor: C.rose,
        borderRadius: 3,
        borderSkipped: false,
      },
      {
        label: 'Hombres',
        data: section.agePyramid.map((r) => -r.men),
        backgroundColor: C.teal,
        borderRadius: 3,
        borderSkipped: false,
      },
    ],
  }

  const pyramidOpts = {
    indexAxis: 'y',
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        labels: {
          color: '#50525f',
          font: { family: 'Inter, sans-serif', size: 11 },
          boxWidth: 12, boxHeight: 12, borderRadius: 4, useBorderRadius: true,
        },
      },
      tooltip: {
        ...tip,
        callbacks: {
          label: (ctx) => ` ${ctx.dataset.label}: ${Math.abs(ctx.raw).toLocaleString('es-CL')}`,
        },
      },
    },
    scales: {
      x: xAxis({
        stacked: true,
        ticks: { callback: (v) => Math.abs(v).toLocaleString('es-CL') },
      }),
      y: yAxis({ stacked: true }),
    },
  }

  return (
    <div className="capital-shell">
      <div className="capital-grid">
        <article className="lead-card capital-hero">
          <span className="eyebrow">Composición del equipo</span>
          <h3>La masa crítica se concentra en edades de mayor productividad investigativa.</h3>
          <p>{section.insights?.[0]?.body}</p>
          <div className="capital-band">
            <div className="capital-band__item">
              <small>Total</small><strong>{formatValue(total, 'integer')}</strong>
            </div>
            <div className="capital-band__item">
              <small>Hombres</small><strong>{formatValue(men, 'integer')}</strong>
            </div>
            <div className="capital-band__item">
              <small>Mujeres</small><strong>{formatValue(women, 'integer')}</strong>
            </div>
            <div className="capital-band__item">
              <small>Tramo 35–54</small><strong>{formatValue(pct35, 'percentage')}</strong>
            </div>
          </div>
        </article>

        <article className="panel-card capital-sidecard">
          <span className="eyebrow">Chequeo de pirámide</span>
          {ok ? (
            <div className="quality-note quality-note--ok">
              <strong>La pirámide cierra con los KPIs.</strong>
              <p>Mujeres: {formatValue(ageWomen, 'integer')} · Hombres: {formatValue(ageMen, 'integer')}</p>
            </div>
          ) : (
            <div className="quality-note quality-note--warn">
              <strong>Descuadre en pirámide.</strong>
              <p>Tramos: {formatValue(ageWomen, 'integer')} M / {formatValue(ageMen, 'integer')} H ≠ KPIs: {formatValue(women, 'integer')} M / {formatValue(men, 'integer')} H</p>
            </div>
          )}
        </article>
      </div>

      <article className="panel-card">
        <span className="eyebrow">Pirámide etaria — hombres · mujeres</span>
        <div className="chart-wrap chart-wrap--pyramid">
          <Bar data={pyramidData} options={pyramidOpts} aria-label="Gráfico pirámide etaria: distribución de investigadores por edad y género" role="img" />
        </div>
      </article>
    </div>
  )
}
