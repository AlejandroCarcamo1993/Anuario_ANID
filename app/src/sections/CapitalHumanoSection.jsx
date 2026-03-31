import { Bar } from 'react-chartjs-2'
import { C, tip, xAxis, yAxis } from '../lib/chartConfig'

const YOUNG_RANGES = new Set(['20-24', '25-29', '30-34'])

export function CapitalHumanoSection({ section, formatValue }) {
  const total = section.kpis.find((k) => k.id === 'total')?.value  ?? 0
  const women = section.kpis.find((k) => k.id === 'mujeres')?.value ?? 0

  // Calcular participación femenina por grupo etario
  const youngRows = section.agePyramid.filter((r) => YOUNG_RANGES.has(r.ageRange))
  const youngWomen = youngRows.reduce((a, r) => a + r.women, 0)
  const youngTotal = youngRows.reduce((a, r) => a + r.women + r.men, 0)
  const youngWomenPct = youngTotal > 0 ? Math.round((youngWomen / youngTotal) * 100) : 0

  const womenPct = total > 0 ? Math.round((women / total) * 100) : 0
  const menPct   = 100 - womenPct

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
        </article>

        <article className="panel-card capital-sidecard">
          <span className="eyebrow">Perspectiva de género</span>

          <div className="capital-gender-total">
            <span className="capital-gender-total__num">{formatValue(total, 'integer')}</span>
            <span className="capital-gender-total__label">personas en el ecosistema</span>
          </div>

          <div className="capital-gender-bars">
            <div className="capital-gender-bar">
              <div className="capital-gender-bar__header">
                <span>Mujeres</span>
                <strong style={{ color: '#E75D50' }}>{womenPct}%</strong>
              </div>
              <div className="capital-gender-bar__track">
                <div className="capital-gender-bar__fill capital-gender-bar__fill--women" style={{ width: `${womenPct}%` }} />
              </div>
            </div>
            <div className="capital-gender-bar">
              <div className="capital-gender-bar__header">
                <span>Hombres</span>
                <strong style={{ color: '#344F9F' }}>{menPct}%</strong>
              </div>
              <div className="capital-gender-bar__track">
                <div className="capital-gender-bar__fill capital-gender-bar__fill--men" style={{ width: `${menPct}%` }} />
              </div>
            </div>
          </div>

          <div className="capital-gender-highlight">
            <small>Mujeres menores de 35</small>
            <strong>{youngWomenPct}%</strong>
            <p>La generación de relevo es más paritaria</p>
          </div>
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
