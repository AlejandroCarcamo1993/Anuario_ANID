import { Bar } from 'react-chartjs-2'
import { C, tip, leg, xAxis, yAxis } from '../lib/chartConfig'

export function FinancieraSection({ section, formatValue }) {
  const centers  = section.kpis.find((k) => k.id === 'ejecutadoCentros')?.value ?? 0
  const projects = section.kpis.find((k) => k.id === 'ejecutadoProyectos')?.value ?? 0
  const total    = section.kpis.find((k) => k.id === 'totalEjecutado')?.value ?? 0
  const mismatch = centers + projects !== total

  const topRows = section.budgetByInstrument.slice(0, 12)

  const barData = {
    labels: topRows.map((i) => i.instrument),
    datasets: [{
      label: 'M$ ejecutado',
      data: topRows.map((i) => i.amount),
      backgroundColor: topRows.map((_, idx) =>
        idx < 3 ? C.teal : idx < 6 ? C.copper : C.rose
      ),
      borderRadius: 6,
      borderSkipped: false,
    }],
  }

  const barOptions = {
    indexAxis: 'y',
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { display: false },
      tooltip: {
        ...tip,
        callbacks: {
          label: (ctx) => ` ${formatValue(ctx.raw, 'currency_clp_thousands')}`,
        },
      },
    },
    scales: {
      x: xAxis({ ticks: { callback: (v) => `M$${(v / 1000000).toFixed(0)}M` } }),
      y: yAxis({ ticks: { font: { family: "'Aptos','Segoe UI',sans-serif", size: 11 } } }),
    },
  }

  return (
    <div className="fin-shell">
      <div className="fin-grid">
        <article className="lead-card fin-hero">
          <span className="eyebrow">Lectura presupuestaria</span>
          <h3>{section.insights?.[0]?.title?.replace('Lectura clave · ', '') || 'Distribución presupuestaria'}</h3>
          <p>{section.insights?.[0]?.body}</p>
          <div className="fin-band">
            <div className="fin-band__item">
              <small>Centros</small>
              <strong>{formatValue(centers, 'currency_clp_thousands')}</strong>
            </div>
            <div className="fin-band__item">
              <small>Proyectos</small>
              <strong>{formatValue(projects, 'currency_clp_thousands')}</strong>
            </div>
            <div className="fin-band__item">
              <small>Total publicado</small>
              <strong>{formatValue(total, 'currency_clp_thousands')}</strong>
            </div>
          </div>
        </article>

        <article className="panel-card fin-sidecard">
          <span className="eyebrow">Estado de consistencia</span>
          {mismatch ? (
            <div className="quality-note quality-note--warn">
              <strong>Diferencia de alcance documentada.</strong>
              <p>
                Centros + proyectos suman {formatValue(centers + projects, 'currency_clp_thousands')}.
                El total publicado ({formatValue(total, 'currency_clp_thousands')}) excluye
                algunos instrumentos del perímetro oficial del Anuario.
              </p>
            </div>
          ) : (
            <div className="quality-note quality-note--ok">
              <strong>Los totales cierran correctamente.</strong>
            </div>
          )}
        </article>
      </div>

      <article className="panel-card">
        <span className="eyebrow">Ejecución por instrumento</span>
        <div className="chart-wrap chart-wrap--hbar-lg">
          <Bar data={barData} options={barOptions} />
        </div>
      </article>
    </div>
  )
}
