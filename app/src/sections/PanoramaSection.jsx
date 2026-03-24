import { Doughnut } from 'react-chartjs-2'
import { C, tip, leg } from '../lib/chartConfig'

const COLORS = [C.teal, C.copper, C.rose, '#4a5cc7']

export function PanoramaSection({ section, formatValue }) {
  const topThreeShare = section.instrumentDistribution.slice(0, 3)
    .reduce((acc, item) => acc + item.sharePct, 0)

  const donutData = {
    labels: section.instrumentDistribution.map((i) => i.label),
    datasets: [{
      data: section.instrumentDistribution.map((i) => i.count),
      backgroundColor: COLORS,
      borderColor: 'rgba(255,255,255,0.9)',
      borderWidth: 2,
      hoverOffset: 6,
    }],
  }

  const donutOptions = {
    responsive: true,
    maintainAspectRatio: true,
    cutout: '68%',
    plugins: {
      legend: leg,
      tooltip: {
        ...tip,
        callbacks: {
          label: (ctx) => ` ${ctx.label}: ${ctx.raw} (${ctx.parsed.toFixed(1)}%)`,
        },
      },
    },
  }

  return (
    <div className="panorama-shell">
      <div className="panorama-grid">
        <article className="lead-card panorama-hero">
          <span className="eyebrow">Lectura editorial</span>
          <h3>Una cartera amplia, pero fuertemente dominada por instrumentos competitivos.</h3>
          <p>{section.insights?.[0]?.body}</p>
          <div className="panorama-ribbon">
            <div className="panorama-ribbon__item">
              <small>Top 3 instrumentos</small>
              <strong>{formatValue(topThreeShare, 'percentage')}</strong>
            </div>
            <div className="panorama-ribbon__item">
              <small>Total iniciativas</small>
              <strong>{formatValue(section.instrumentDistribution.reduce((a, i) => a + i.count, 0), 'integer')}</strong>
            </div>
            <div className="panorama-ribbon__item">
              <small>Instrumentos</small>
              <strong>{section.instrumentDistribution.length}</strong>
            </div>
          </div>
        </article>

        <article className="panel-card panorama-donut-card">
          <span className="eyebrow">Distribución por instrumento</span>
          <div className="chart-wrap chart-wrap--donut">
            <Doughnut data={donutData} options={donutOptions} />
          </div>
        </article>
      </div>

      <div className="panorama-stat-grid">
        {section.kpis.map((item) => (
          <article key={item.id} className="panorama-stat-card">
            <small>{item.label}</small>
            <strong>{formatValue(item.value, item.format)}</strong>
          </article>
        ))}
      </div>
    </div>
  )
}
