import { useEffect, useRef, useState } from 'react'
import mapUrl from '../../../mapa-chile.svg'

// ── Escala coroplética (paleta ANID sobre fondo claro) ──────────────────────
export function choroFill(count) {
  if (count >= 200) return '#00396b'
  if (count >= 50)  return '#2160a2'
  if (count >= 15)  return '#4e7dc4'
  if (count >= 4)   return '#85a8d8'
  if (count >= 1)   return '#b6cce8'
  return 'rgba(200,215,240,.3)'
}
function choroHover(count) {
  if (count >= 200) return '#00568a'
  if (count >= 50)  return '#3872c0'
  if (count >= 15)  return '#5e8dd0'
  if (count >= 4)   return '#9ab4dc'
  return '#c4d8f0'
}

function getS1(el) {
  const list = []
  if (el.classList?.contains('s1')) list.push(el)
  el.querySelectorAll?.('.s1').forEach(p => list.push(p))
  return list
}

/**
 * ChileMap — mapa coroplético interactivo
 *
 * Props:
 *   regions    — array de { mapId, name, count, pct }
 *   total      — número total de iniciativas
 *   selectedId — mapId controlado desde el padre (null = sin selección)
 *   onSelect   — callback(mapId, data) al hacer clic en región
 *   onDeselect — callback() al deseleccionar
 */
export function ChileMap({ regions, total, selectedId, onSelect, onDeselect }) {
  const containerRef = useRef(null)
  const svgRef       = useRef(null)
  const [tooltip, setTooltip] = useState(null)

  // Lookup mapId → datos
  const byId = {}
  regions.forEach(r => { if (r.mapId) byId[r.mapId] = r })

  // ── Helpers de manipulación SVG ───────────────────────────────
  function applyHighlight(svgEl, activeId) {
    Object.entries(byId).forEach(([id, rd]) => {
      const g = svgEl.getElementById(id)
      if (!g) return
      const isActive = id === activeId
      getS1(g).forEach(p => {
        p.style.fill        = isActive ? choroHover(rd.count) : choroFill(rd.count)
        p.style.opacity     = activeId && !isActive ? '0.22' : '1'
        p.style.stroke      = isActive ? 'rgba(0,57,107,.75)' : 'rgba(255,255,255,.9)'
        p.style.strokeWidth = isActive ? '1.2' : '0.4'
      })
    })
  }

  function restoreAll(svgEl) {
    Object.entries(byId).forEach(([id, rd]) => {
      const g = svgEl.getElementById(id)
      if (!g) return
      getS1(g).forEach(p => {
        p.style.fill        = choroFill(rd.count)
        p.style.opacity     = '1'
        p.style.stroke      = 'rgba(255,255,255,.9)'
        p.style.strokeWidth = '0.4'
      })
    })
  }

  // ── Reaccionar al selectedId controlado desde el padre ────────
  useEffect(() => {
    const svgEl = svgRef.current
    if (!svgEl) return
    if (selectedId) applyHighlight(svgEl, selectedId)
    else restoreAll(svgEl)
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [selectedId])

  // ── Cargar SVG inline una sola vez ────────────────────────────
  useEffect(() => {
    const container = containerRef.current
    if (!container) return

    fetch(mapUrl)
      .then(r => r.text())
      .then(svgText => {
        container.innerHTML = svgText
        const svgEl = container.querySelector('svg')
        if (!svgEl) return
        svgRef.current = svgEl
        svgEl.style.cssText = 'width:100%;height:auto;display:block;'

        // Estilos base — inyectados al final para ganar en cascade
        const st = document.createElementNS('http://www.w3.org/2000/svg', 'style')
        st.textContent = `
          .map-chile.s1 {
            fill: rgba(200,215,240,.3);
            stroke: rgba(255,255,255,.9);
            stroke-width: 0.4;
            cursor: pointer;
            transition: fill .2s ease, opacity .2s ease,
                        stroke .2s ease, stroke-width .15s ease;
          }
          .map-chile.s2 { stroke: rgba(80,100,180,.1);  fill: none; }
          .map-chile.s3 { stroke: rgba(80,100,180,.07); fill: none; }
        `
        svgEl.appendChild(st)

        // Colorear y añadir interactividad
        Object.entries(byId).forEach(([id, data]) => {
          const group = svgEl.getElementById(id)
          if (!group) return

          // Color inicial
          getS1(group).forEach(p => {
            p.style.fill        = choroFill(data.count)
            p.style.stroke      = 'rgba(255,255,255,.9)'
            p.style.strokeWidth = '0.4'
          })
          group.style.cursor = 'pointer'

          group.addEventListener('mouseenter', () => {
            if (id === selectedId) return
            getS1(group).forEach(p => { p.style.fill = choroHover(data.count) })
          })
          group.addEventListener('mousemove', e => {
            const rect = container.getBoundingClientRect()
            setTooltip({
              x: e.clientX - rect.left + 14,
              y: e.clientY - rect.top  - 44,
              text: `${data.name}  ·  ${data.count} iniciativas (${Number(data.pct).toFixed(1)}%)`,
            })
          })
          group.addEventListener('mouseleave', () => {
            setTooltip(null)
            if (id === selectedId) return
            getS1(group).forEach(p => {
              p.style.fill    = choroFill(data.count)
              p.style.opacity = selectedId ? '0.22' : '1'
            })
          })
          group.addEventListener('click', () => {
            if (id === selectedId) { onDeselect?.(); return }
            onSelect?.(id, data)
          })
        })
      })
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  return (
    <div className="chile-map-shell">
      <div ref={containerRef} className="chile-map-svg-wrap" />
      {tooltip && (
        <div
          className="map-tooltip"
          style={{ left: tooltip.x, top: tooltip.y }}
          role="tooltip"
        >
          {tooltip.text}
        </div>
      )}
    </div>
  )
}
