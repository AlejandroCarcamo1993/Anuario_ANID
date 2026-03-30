import { useState } from 'react'
import { Bar } from 'react-chartjs-2'
import { C, tip, xAxis, yAxis } from '../lib/chartConfig'
import { ChileMap, choroFill } from '../components/ChileMap'

const LEGEND = [
  { label: '200+',   color: '#00396b' },
  { label: '50–199', color: '#2160a2' },
  { label: '15–49',  color: '#4e7dc4' },
  { label: '4–14',   color: '#85a8d8' },
  { label: '1–3',    color: '#b6cce8' },
]

export function TerritorioSection({ section, formatValue }) {
  const total       = section.kpis.find((k) => k.id === 'iniciativas')?.value  ?? 0
  const topThreePct = section.kpis.find((k) => k.id === 'regionesPrincipalesPct')?.value ?? 0
  const rmCount     = section.kpis.find((k) => k.id === 'rmCount')?.value ?? 0
  const sumRegions  = section.regions.reduce((a, r) => a + r.count, 0)
  const mismatch    = total !== sumRegions

  const sortedRegions = [...section.regions].sort((a, b) => b.count - a.count)

  // ── Estado de selección controlado ───────────────────────────
  const [selectedId,   setSelectedId]   = useState(null)
  const [selectedData, setSelectedData] = useState(null)

  function handleSelect(id, data) {
    setSelectedId(id)
    setSelectedData(data)
  }
  function handleDeselect() {
    setSelectedId(null)
    setSelectedData(null)
  }
  function handleChipClick(r) {
    if (selectedId === r.mapId) { handleDeselect(); return }
    handleSelect(r.mapId, r)
  }

  // ── Bar chart (top 10) ────────────────────────────────────────
  const topRegions = sortedRegions.slice(0, 10)
  const barData = {
    labels: topRegions.map((r) => r.name),
    datasets: [{
      label: 'Iniciativas',
      data: topRegions.map((r) => r.count),
      backgroundColor: topRegions.map((_, i) =>
        i === 0 ? C.night : i < 3 ? C.teal : i < 6 ? C.copper : C.rose
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
          label: (ctx) => ` ${ctx.raw} iniciativas (${((ctx.raw / total) * 100).toFixed(1)}%)`,
        },
      },
    },
    scales: { x: xAxis(), y: yAxis() },
  }

  return (
    <div className="territory-shell">

      {/* ── Hero + KPIs ─────────────────────────────────────── */}
      <div className="territory-kpi-row">
        <div className="territory-hero-copy">
          <span className="eyebrow">Huella territorial</span>
          <h3 className="territory-hero-title">
            El ecosistema se concentra en el corredor central del sistema universitario.
          </h3>
          <p className="territory-hero-sub">{section.insights?.[0]?.body}</p>
        </div>
        <div className="territory-kpi-strip">
          <div className="territory-kpi-chip">
            <small>Total</small>
            <strong>{formatValue(total, 'integer')}</strong>
          </div>
          <div className="territory-kpi-chip territory-kpi-chip--accent">
            <small>Top 3</small>
            <strong>{formatValue(topThreePct, 'percentage')}</strong>
          </div>
          <div className="territory-kpi-chip">
            <small>RM</small>
            <strong>{formatValue(rmCount, 'integer')}</strong>
          </div>
        </div>
      </div>

      {/* ── Panel principal: mapa full-width ────────────────── */}
      <article className="panel-card territory-map-panel">

        {/* Cabecera */}
        <div className="territory-map-panel__header">
          <div>
            <span className="eyebrow">Distribución regional</span>
            <p className="territory-map-panel__hint">
              {total} iniciativas · haz clic en una región o en los botones
            </p>
          </div>
          <div className="territory-legend">
            {LEGEND.map((l) => (
              <span key={l.label} className="territory-legend__item">
                <span className="territory-legend__dot" style={{ background: l.color }} />
                {l.label}
              </span>
            ))}
          </div>
        </div>

        {/* Mapa */}
        <div className="territory-map-full">
          <ChileMap
            regions={section.regions}
            total={total}
            selectedId={selectedId}
            onSelect={handleSelect}
            onDeselect={handleDeselect}
          />
        </div>

        {/* Panel de info — visible al seleccionar */}
        {selectedData && (
          <div className="territory-info-panel">
            <div
              className="territory-info-badge"
              style={{ background: choroFill(selectedData.count) }}
            >
              {selectedData.count}
            </div>
            <div className="territory-info-copy">
              <strong>{selectedData.name}</strong>
              <span>{Number(selectedData.pct).toFixed(1)}% del total · {selectedData.count} de {total} iniciativas</span>
            </div>
            <div className="territory-info-bar-wrap">
              <div
                className="territory-info-bar"
                style={{
                  width: `${Math.max(2, (selectedData.count / 248) * 100).toFixed(1)}%`,
                  background: choroFill(selectedData.count),
                }}
              />
            </div>
            <button className="map-close-btn" onClick={handleDeselect} aria-label="Cerrar">✕</button>
          </div>
        )}

        {/* Chips de regiones */}
        <div className="territory-chips-wrap">
          {sortedRegions.map((r) => {
            const isActive = selectedId === r.mapId
            return (
              <button
                key={r.mapId ?? r.name}
                className={`territory-chip${isActive ? ' is-active' : ''}`}
                onClick={() => handleChipClick(r)}
                title={`${r.name}: ${r.count} iniciativas`}
              >
                <span
                  className="territory-chip__dot"
                  style={{ background: choroFill(r.count) }}
                />
                <span className="territory-chip__name">{r.name}</span>
                <span
                  className="territory-chip__count"
                  style={{ color: isActive ? '#fff' : choroFill(r.count) }}
                >
                  {r.count}
                </span>
              </button>
            )
          })}
        </div>

      </article>

      {/* ── Advertencia de datos ─────────────────────────────── */}
      {mismatch && (
        <article className="quality-note quality-note--warn">
          <strong>Detalle regional suma {formatValue(sumRegions, 'integer')}, KPI dice {formatValue(total, 'integer')}.</strong>
          <p>19 iniciativas tienen presencia multi-regional y se cuentan una sola vez en el KPI.</p>
        </article>
      )}

      {/* ── Gráfico top 10 ──────────────────────────────────── */}
      <article className="panel-card">
        <span className="eyebrow">Top 10 regiones por concentración</span>
        <div className="chart-wrap chart-wrap--hbar">
          <Bar data={barData} options={barOpts} aria-label="Gráfico de barras horizontal: top 10 regiones por concentración de iniciativas" role="img" />
        </div>
      </article>

    </div>
  )
}
