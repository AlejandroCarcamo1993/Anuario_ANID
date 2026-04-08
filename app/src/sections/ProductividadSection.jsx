import { Doughnut, Bar } from 'react-chartjs-2'
import { C, tip, leg, xAxis, yAxis } from '../lib/chartConfig'

function sumPatents(row) {
  return (row.patentes || 0) + (row.derechoAutor || 0) + (row.marcas || 0) +
    (row.secretoIndustrial || 0) + (row.servicioPi || 0)
}

function pubDonutData(program) {
  const q1   = program.q1 ?? 0
  const rest = (program.total ?? 0) - q1
  const isIM = program.program.includes('Institutos')
  return {
    labels: ['Q1', 'Q2–Q4'],
    datasets: [{
      data: [q1, rest],
      backgroundColor: [isIM ? C.teal : C.copper, C.sand],
      borderColor: 'rgba(255,255,255,0.9)',
      borderWidth: 2,
      hoverOffset: 5,
    }],
  }
}

const donutOpts = (total) => ({
  responsive: true,
  maintainAspectRatio: true,
  cutout: '70%',
  plugins: {
    legend: leg,
    tooltip: {
      ...tip,
      callbacks: {
        label: (ctx) => ` ${ctx.label}: ${ctx.raw} (${((ctx.raw / total) * 100).toFixed(1)}%)`,
      },
    },
  },
})

export function ProductividadSection({ section, formatValue }) {
  const milenioPrograms = section.publicaciones.totalsByProgram.filter((p) => p.q1 != null)
  const totalCongresos  = section.congresos.distributionByInstrument
    .reduce((a, i) => a + i.nacional + i.internacional, 0)
  const kpiCongresos = section.congresos.kpis.find((k) => k.id === 'presentaciones')?.value ?? 0
  const mismatch = totalCongresos !== kpiCongresos

  // Tesis stacked bar
  const tesisInstruments = section.tesis.distributionByInstrument
  const tesisData = {
    labels: tesisInstruments.map((i) => i.instrument),
    datasets: [
      { label: 'Pregrado',  data: tesisInstruments.map((i) => i.pregrado),  backgroundColor: C.teal,   borderRadius: 4, borderSkipped: false },
      { label: 'Magíster',  data: tesisInstruments.map((i) => i.magister),  backgroundColor: C.copper, borderRadius: 4, borderSkipped: false },
      { label: 'Doctorado', data: tesisInstruments.map((i) => i.doctorado), backgroundColor: C.rose,   borderRadius: 4, borderSkipped: false },
    ],
  }
  const tesisOpts = {
    indexAxis: 'y',
    responsive: true,
    maintainAspectRatio: false,
    plugins: { legend: leg, tooltip: { ...tip } },
    scales: {
      x: xAxis({ stacked: true }),
      y: yAxis({ stacked: true }),
    },
  }

  // Congresos grouped bar
  const congInstr = section.congresos.distributionByInstrument
  const congData = {
    labels: congInstr.map((i) => i.instrument),
    datasets: [
      { label: 'Nacional',       data: congInstr.map((i) => i.nacional),       backgroundColor: C.teal,   borderRadius: 4, borderSkipped: false },
      { label: 'Internacional',  data: congInstr.map((i) => i.internacional),  backgroundColor: C.rose,   borderRadius: 4, borderSkipped: false },
    ],
  }
  const congOpts = {
    indexAxis: 'y',
    responsive: true,
    maintainAspectRatio: false,
    plugins: { legend: leg, tooltip: { ...tip } },
    scales: {
      x: xAxis({ stacked: true }),
      y: yAxis({ stacked: true }),
    },
  }

  return (
    <div className="prod-shell">
      <div className="prod-top-grid">
        <article className="lead-card prod-hero">
          <span className="eyebrow">Sistema de outputs</span>
          <h3>Publicaciones, formación y divulgación: el núcleo de tracción del Anuario.</h3>
          <p>{section.insights?.[0]?.body}</p>
        </article>

        {mismatch && (
          <article className="panel-card prod-quality-card">
            <span className="eyebrow">Advertencia de datos</span>
            <div className="quality-note quality-note--warn">
              <strong>Congresos: desglose suma {formatValue(totalCongresos, 'integer')}, KPI {formatValue(kpiCongresos, 'integer')}.</strong>
              <p>Revisar distribución por instrumento — el total Excel y el KPI no coinciden.</p>
            </div>
          </article>
        )}
      </div>

      {/* Publicaciones Milenio — donuts */}
      <div className="prod-pub-grid">
        {milenioPrograms.map((p) => (
          <article key={p.program} className="panel-card">
            <span className="eyebrow">{p.program}</span>
            <div className="chart-wrap chart-wrap--donut">
              <Doughnut data={pubDonutData(p)} options={donutOpts(p.total)} aria-label={`Gráfico donut: distribución de publicaciones ${p.program}`} role="img" />
            </div>
            <div className="ratio-grid" style={{ marginTop: '0.75rem' }}>
              <div><small>Total</small><strong>{formatValue(p.total, 'integer')}</strong></div>
              <div><small>Q1</small><strong>{formatValue(p.q1, 'integer')}</strong></div>
              <div><small>% Q1</small><strong>{formatValue((p.q1 / p.total) * 100, 'percentage')}</strong></div>
            </div>
          </article>
        ))}

        <article className="panel-card pub-restantes-card">
          <span className="eyebrow">Publicaciones restantes</span>
          <p className="pub-restantes-card__note">Sin desglose Q1 disponible</p>
          <div className="list-grid">
            {section.publicaciones.totalsByProgram.filter((p) => !p.q1).map((p) => (
              <div key={p.program} className="list-row list-row--boxed">
                <strong>{p.program}</strong>
                <span className="pill-soft">{formatValue(p.total, 'integer')}</span>
              </div>
            ))}
          </div>
          {(() => {
            const total = section.publicaciones.totalsByProgram
              .filter((p) => !p.q1)
              .reduce((acc, p) => acc + p.total, 0)
            return (
              <div className="pub-restantes-card__total">
                <small>Total</small>
                <strong>{formatValue(total, 'integer')}</strong>
              </div>
            )
          })()}
        </article>
      </div>

      {/* Tesis + Congresos — grid 2 columnas */}
      <div className="prod-charts-grid">
        <article className="panel-card">
          <span className="eyebrow">Formación — tesis por instrumento</span>
          <div className="chart-wrap chart-wrap--hbar">
            <Bar data={tesisData} options={tesisOpts} aria-label="Gráfico de barras horizontal: tesis por instrumento" role="img" />
          </div>
          <div className="ratio-grid" style={{ marginTop: '0.75rem' }}>
            {section.tesis.kpis.map((k) => (
              <div key={k.id}><small>{k.label}</small><strong>{formatValue(k.value, k.format)}</strong></div>
            ))}
          </div>
        </article>

        <article className="panel-card">
          <span className="eyebrow">Congresos — nacional vs internacional</span>
          <div className="chart-wrap chart-wrap--hbar">
            <Bar data={congData} options={congOpts} aria-label="Gráfico de barras horizontal: presentaciones a congresos nacional vs internacional" role="img" />
          </div>
          <div className="ratio-grid" style={{ marginTop: '0.75rem' }}>
            {section.congresos.kpis.slice(0, 3).map((k) => (
              <div key={k.id}><small>{k.label}</small><strong>{formatValue(k.value, k.format)}</strong></div>
            ))}
          </div>
        </article>
      </div>

      {/* Patentes */}
      <article className="panel-card prod-pi-card">
        <div className="prod-pi-header">
          <span className="eyebrow">Propiedad intelectual</span>
          <span className="prod-pi-header__sub">Patentes · Derechos de autor · Marcas</span>
        </div>
        <div className="pi-list">
          {(() => {
            const sorted = [...section.patentes.totalsByInstrument].sort((a, b) => sumPatents(b) - sumPatents(a))
            const max = sumPatents(sorted[0]) || 1
            return sorted.map((item, i) => (
              <div
                key={item.instrument}
                className="pi-row"
                style={{ '--pi-bar': `${(sumPatents(item) / max) * 100}%` }}
              >
                <span className="pi-row__rank">{i + 1}</span>
                <div className="pi-row__copy">
                  <strong>{item.instrument}</strong>
                  <small>{item.patentes} PAT · {item.derechoAutor} D.AUTOR</small>
                </div>
                <span className="pi-row__badge">{formatValue(sumPatents(item), 'integer')}</span>
              </div>
            ))
          })()}
        </div>
      </article>
    </div>
  )
}
