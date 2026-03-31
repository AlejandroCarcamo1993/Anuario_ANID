import { Doughnut } from 'react-chartjs-2'
import { C, tip, leg } from '../lib/chartConfig'

const COLORS = [C.teal, C.copper, C.rose, '#4a5cc7']
const INST_COLORS = ['#344F9F', '#293055', '#00566c', '#E75D50', '#4a5cc7', '#00869a', '#b36200', '#7c3aed']

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

  const maxCentros = section.centrosByInstrument
    ? Math.max(...section.centrosByInstrument.map((i) => i.count))
    : 0

  return (
    <div className="panorama-shell">
      {/* Hero: editorial + donut */}
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
              <small>Instrumentos distintos</small>
              <strong>{section.instrumentDistribution.length}</strong>
            </div>
          </div>
        </article>

        <article className="panel-card panorama-donut-card">
          <span className="eyebrow">Distribución por instrumento</span>
          <div className="chart-wrap chart-wrap--donut">
            <Doughnut data={donutData} options={donutOptions} aria-label="Gráfico donut: distribución por instrumento" role="img" />
          </div>
        </article>
      </div>

      {/* Centros por instrumento + Disciplinas — sólo años con datos ricos */}
      {(section.centrosByInstrument || section.disciplineDistribution) && (
        <div className="panorama-bottom-grid">

          {section.centrosByInstrument && (
            <article className="panel-card panorama-inst-card">
              <span className="eyebrow">Centros por instrumento</span>
              <p className="panorama-inst-card__sub">
                {section.centrosByInstrument.reduce((a, i) => a + i.count, 0)} centros en {section.centrosByInstrument.length} instrumentos
              </p>
              <div className="inst-bar-list">
                {section.centrosByInstrument.map((item, i) => (
                  <div key={item.instrument} className="inst-bar">
                    <div className="inst-bar__header">
                      <span>{item.instrument}</span>
                      <strong style={{ color: INST_COLORS[i % INST_COLORS.length] }}>{item.count}</strong>
                    </div>
                    <div className="inst-bar__track">
                      <div
                        className="inst-bar__fill"
                        style={{
                          width: `${(item.count / maxCentros) * 100}%`,
                          background: `linear-gradient(90deg, ${INST_COLORS[i % INST_COLORS.length]}, ${INST_COLORS[i % INST_COLORS.length]}bb)`,
                        }}
                      />
                    </div>
                  </div>
                ))}
              </div>
            </article>
          )}

          {section.disciplineDistribution && (
            <article className="panel-card panorama-disc-card">
              <span className="eyebrow">Distribución disciplinar</span>
              <p className="panorama-disc-card__sub">Por área OCDE — centros SCIA</p>
              <div className="disc-list">
                {section.disciplineDistribution.map((item, i) => (
                  <div key={item.discipline} className="disc-row">
                    <div className="disc-row__top">
                      <span>{item.discipline}</span>
                      <strong>{formatValue(item.pct, 'percentage')}</strong>
                    </div>
                    <div className="disc-row__track">
                      <div
                        className="disc-row__fill"
                        style={{
                          width: `${item.pct}%`,
                          background: `linear-gradient(90deg, ${INST_COLORS[i % INST_COLORS.length]}, ${INST_COLORS[(i + 2) % INST_COLORS.length]}90)`,
                        }}
                      />
                    </div>
                  </div>
                ))}
              </div>

              {section.leadershipGender && (
                <div className="gender-strip">
                  <div className="gender-strip__item gender-strip__item--female">
                    <small>Liderazgo femenino</small>
                    <strong>
                      {formatValue(
                        section.leadershipGender.mujeresPct
                          ?? section.leadershipGender.femalePct
                          ?? section.leadershipGender.directivoFemeninoPct,
                        'percentage'
                      )}
                    </strong>
                  </div>
                  <div className="gender-strip__item">
                    <small>Razón H/M directivos</small>
                    <strong>
                      {section.leadershipGender.razonHM
                        ?? (section.leadershipGender.mujeres > 0
                          ? (section.leadershipGender.hombres / section.leadershipGender.mujeres).toFixed(1)
                          : '—')}
                    </strong>
                  </div>
                </div>
              )}
            </article>
          )}

        </div>
      )}
    </div>
  )
}
