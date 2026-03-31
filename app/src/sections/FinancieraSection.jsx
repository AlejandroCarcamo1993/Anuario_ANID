import { Bar } from 'react-chartjs-2'
import { C, tip, xAxis, yAxis } from '../lib/chartConfig'

const CENTRO_COLOR   = C.night
const PROYECTO_COLOR = C.teal

function makeBarData(items) {
  return {
    labels: items.map((i) => i.instrument),
    datasets: [{
      label: 'M$ ejecutado',
      data: items.map((i) => i.amount),
      backgroundColor: items.map((i) =>
        i.category === 'centro' ? CENTRO_COLOR : PROYECTO_COLOR
      ),
      borderRadius: 5,
      borderSkipped: false,
    }],
  }
}

function makeBarOptions(formatValue, total) {
  return {
    indexAxis: 'y',
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { display: false },
      tooltip: {
        ...tip,
        callbacks: {
          label: (ctx) => {
            const pct = total > 0 ? ((ctx.raw / total) * 100).toFixed(1) : '0.0'
            return ` ${formatValue(ctx.raw, 'currency_clp_thousands')} · ${pct}%`
          },
        },
      },
    },
    scales: {
      x: xAxis({ ticks: { callback: (v) => `M$${(v / 1000).toFixed(0)}M` } }),
      y: yAxis(),
    },
  }
}

export function FinancieraSection({ section, formatValue }) {
  const kpis = section.kpis ?? []

  // Modo comparativo (2024.json): usa IDs centros2024 / centros2025
  const hasComparison = kpis.some((k) => k.id === 'centros2024')

  const c1   = kpis.find((k) => k.id === (hasComparison ? 'centros2024'   : 'ejecutadoCentros'))?.value   ?? 0
  const p1   = kpis.find((k) => k.id === (hasComparison ? 'proyectos2024' : 'ejecutadoProyectos'))?.value ?? 0
  const t1   = kpis.find((k) => k.id === (hasComparison ? 'total2024'     : 'totalEjecutado'))?.value     ?? 0
  const c2   = hasComparison ? (kpis.find((k) => k.id === 'centros2025')?.value   ?? 0) : null
  const p2   = hasComparison ? (kpis.find((k) => k.id === 'proyectos2025')?.value ?? 0) : null
  const t2   = hasComparison ? (kpis.find((k) => k.id === 'total2025')?.value     ?? 0) : null

  const label1 = hasComparison ? '2024' : kpis.find((k) => k.id === 'ejecutadoCentros')?.label?.replace('Centros ', '') ?? 'Año actual'
  const label2 = hasComparison ? '2025' : null

  const items1 = section.budgetByInstrument      ?? []
  const items2 = hasComparison ? (section.budgetByInstrument2025 ?? []) : []

  const barData1 = makeBarData(items1)
  const barData2 = makeBarData(items2)
  const barOpts1 = makeBarOptions(formatValue, t1)
  const barOpts2 = makeBarOptions(formatValue, t2 ?? 0)

  return (
    <div className="fin-shell">

      {/* ── Hero + resumen ── */}
      <div className="fin-grid">
        <article className="lead-card fin-hero">
          <span className="eyebrow">Lectura presupuestaria</span>
          <h3>Distribución presupuestaria</h3>
          <p>{section.insights?.[0]?.body}</p>

          <div className="fin-compare-table">
            <div className="fin-compare-table__head">
              <span />
              <span>{label1}</span>
              {label2 && <span>{label2}</span>}
            </div>
            <div className="fin-compare-table__row fin-compare-table__row--centro">
              <span>Centros</span>
              <strong>{formatValue(c1, 'currency_clp_thousands')}</strong>
              {c2 !== null && <strong>{formatValue(c2, 'currency_clp_thousands')}</strong>}
            </div>
            <div className="fin-compare-table__row fin-compare-table__row--proyecto">
              <span>Proyectos</span>
              <strong>{formatValue(p1, 'currency_clp_thousands')}</strong>
              {p2 !== null && <strong>{formatValue(p2, 'currency_clp_thousands')}</strong>}
            </div>
            <div className="fin-compare-table__row fin-compare-table__row--total">
              <span>Total</span>
              <strong>{formatValue(t1, 'currency_clp_thousands')}</strong>
              {t2 !== null && <strong>{formatValue(t2, 'currency_clp_thousands')}</strong>}
            </div>
          </div>
        </article>

        {/* Leyenda */}
        <article className="panel-card fin-sidecard">
          <span className="eyebrow">Categorías</span>
          <div className="fin-legend">
            <div className="fin-legend__item">
              <span className="fin-legend__dot" style={{ background: CENTRO_COLOR }} />
              <div>
                <strong>Centros</strong>
                <small>Basales · FONDAP · Milenio · Regionales · Internacionales · Tecnológicos · Educación · Servicios</small>
              </div>
            </div>
            <div className="fin-legend__item">
              <span className="fin-legend__dot" style={{ background: PROYECTO_COLOR }} />
              <div>
                <strong>Proyectos</strong>
                <small>Anillos · Equipamiento Mediano/Mayor · Núcleos Milenio · Buque</small>
              </div>
            </div>
          </div>
          <div className="fin-source-note">
            <small>Fuente: {section.sources?.[0]}</small>
            <small>Estados considerados: Vigente + Finalizado</small>
          </div>
        </article>
      </div>

      {/* ── Gráfico año principal ── */}
      {items1.length > 0 && (
        <article className="panel-card">
          <span className="eyebrow">Ejecución por instrumento · {label1}</span>
          <div className="chart-wrap chart-wrap--hbar-lg">
            <Bar
              data={barData1}
              options={barOpts1}
              aria-label={`Gráfico de barras: ejecución presupuestaria ${label1}`}
              role="img"
            />
          </div>
        </article>
      )}

      {/* ── Editorial bridge (solo en modo comparativo) ── */}
      {hasComparison && items2.length > 0 && (() => {
        const delta = t2 - t1
        const deltaPct = t1 > 0 ? ((delta / t1) * 100).toFixed(1) : '0.0'
        const isDown = delta < 0
        return (
          <div className="fin-bridge">
            <div className="fin-bridge__line" />
            <article className="fin-bridge__card">
              <span className="eyebrow">Variación interanual</span>
              <div className="fin-bridge__stats">
                <div className="fin-bridge__stat">
                  <small>Total {label1}</small>
                  <strong>{formatValue(t1, 'currency_clp_thousands')}</strong>
                </div>
                <div className={`fin-bridge__arrow ${isDown ? 'fin-bridge__arrow--down' : 'fin-bridge__arrow--up'}`}>
                  <span>{isDown ? '▼' : '▲'}</span>
                  <strong>{Math.abs(Number(deltaPct))}%</strong>
                </div>
                <div className="fin-bridge__stat">
                  <small>Total {label2}</small>
                  <strong>{formatValue(t2, 'currency_clp_thousands')}</strong>
                </div>
              </div>
              <p className="fin-bridge__note">
                {isDown
                  ? `Reducción de ${formatValue(Math.abs(delta), 'currency_clp_thousands')} respecto al año anterior, reflejando menor ejecución en proyectos competitivos.`
                  : `Incremento de ${formatValue(Math.abs(delta), 'currency_clp_thousands')} respecto al año anterior.`}
              </p>
            </article>
            <div className="fin-bridge__line" />
          </div>
        )
      })()}

      {/* ── Gráfico año 2 (solo en modo comparativo) ── */}
      {items2.length > 0 && (
        <article className="panel-card">
          <span className="eyebrow">Ejecución por instrumento · {label2}</span>
          <div className="chart-wrap chart-wrap--hbar">
            <Bar
              data={barData2}
              options={barOpts2}
              aria-label={`Gráfico de barras: ejecución presupuestaria ${label2}`}
              role="img"
            />
          </div>
        </article>
      )}

    </div>
  )
}
