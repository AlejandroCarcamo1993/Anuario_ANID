import { Bar } from 'react-chartjs-2'
import { C, tip, leg, xAxis, yAxis } from '../lib/chartConfig'

export function PostulacionSection({ section, formatValue }) {
  const { postulaciones, adjudicaciones, tasaAdjudicacionPct } = section.genderBreakdown
  const totalPost = postulaciones.hombres + postulaciones.mujeres
  const rateDelta = tasaAdjudicacionPct.mujeres - tasaAdjudicacionPct.hombres

  const barData = {
    labels: ['Postulaciones', 'Adjudicaciones'],
    datasets: [
      {
        label: 'Hombres',
        data: [postulaciones.hombres, adjudicaciones.hombres],
        backgroundColor: C.teal,
        borderRadius: 6,
        borderSkipped: false,
      },
      {
        label: 'Mujeres',
        data: [postulaciones.mujeres, adjudicaciones.mujeres],
        backgroundColor: C.rose,
        borderRadius: 6,
        borderSkipped: false,
      },
    ],
  }

  const barOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: leg,
      tooltip: {
        ...tip,
        callbacks: {
          label: (ctx) => ` ${ctx.dataset.label}: ${ctx.raw.toLocaleString('es-CL')}`,
        },
      },
    },
    scales: {
      x: xAxis(),
      y: yAxis({ ticks: { callback: (v) => v.toLocaleString('es-CL') } }),
    },
  }

  return (
    <div className="post-shell">
      <div className="post-grid">
        <article className="lead-card post-hero">
          <span className="eyebrow">Lectura de adjudicación</span>
          <h3>La brecha principal no está en la tasa, sino en el volumen de entrada al sistema.</h3>
          <p>{section.insights?.[0]?.body}</p>
          <div className="post-band">
            <div className="post-band__item">
              <small>Total postulaciones</small>
              <strong>{formatValue(totalPost, 'integer')}</strong>
            </div>
            <div className="post-band__item">
              <small>Tasa global</small>
              <strong>{formatValue(section.kpis.find((k) => k.id === 'tasaGlobal')?.value, 'percentage')}</strong>
            </div>
            <div className="post-band__item">
              <small>Delta tasa M vs H</small>
              <strong>{rateDelta > 0 ? '+' : ''}{formatValue(rateDelta, 'percentage')}</strong>
            </div>
          </div>
        </article>

        <article className="panel-card">
          <span className="eyebrow">Postulaciones y adjudicaciones por género</span>
          <div className="chart-wrap chart-wrap--bar">
            <Bar data={barData} options={barOptions} aria-label="Gráfico de barras: postulaciones y adjudicaciones por género" role="img" />
          </div>
        </article>
      </div>

      <div className="post-detail-grid">
        <article className="panel-card">
          <span className="eyebrow">Tasas de adjudicación</span>
          <div className="ratio-grid">
            <div>
              <small>Hombres</small>
              <strong>{formatValue(tasaAdjudicacionPct.hombres, 'percentage')}</strong>
            </div>
            <div>
              <small>Mujeres</small>
              <strong>{formatValue(tasaAdjudicacionPct.mujeres, 'percentage')}</strong>
            </div>
            <div>
              <small>Part. fem. adjudicada</small>
              <strong>{formatValue(section.kpis.find((k) => k.id === 'participacionFemeninaAdjudicada')?.value, 'percentage')}</strong>
            </div>
          </div>
        </article>

        <article className="panel-card">
          <span className="eyebrow">Brechas destacadas</span>
          <div className="list-grid">
            {section.genderGapTable.map((item) => (
              <article key={item.contest} className="list-row list-row--boxed">
                <div>
                  <strong>{item.contest}</strong>
                  <small>{item.femaleApplicationsPct}% postulaciones femeninas</small>
                </div>
                <span className={item.status === 'parity' ? 'pill-soft' : 'pill-accent'}>
                  {item.status === 'parity' ? 'Paridad' : `+${item.gapPp.toFixed(1).replace('.', ',')} pp`}
                </span>
              </article>
            ))}
          </div>
        </article>
      </div>
    </div>
  )
}
