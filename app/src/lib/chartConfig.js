import {
  Chart as ChartJS,
  ArcElement,
  BarElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend,
} from 'chart.js'

ChartJS.register(ArcElement, BarElement, CategoryScale, LinearScale, Tooltip, Legend)

export const C = {
  teal:       '#00566c',
  tealAlpha:  'rgba(0,86,108,0.22)',
  copper:     '#2160a2',
  copperAlpha:'rgba(33,96,162,0.22)',
  rose:       '#bc0004',
  roseAlpha:  'rgba(188,0,4,0.18)',
  night:      '#0b1c30',
  slate:      '#5f6f85',
  sand:       '#eff4ff',
}

const _font = { family: "'Inter','Segoe UI',sans-serif", size: 11, weight: '500' }

export const tip = {
  backgroundColor: 'rgba(11,28,48,0.94)',
  titleColor: '#f8fbff',
  bodyColor: 'rgba(248,251,255,0.84)',
  padding: 10,
  cornerRadius: 10,
  titleFont: { ..._font, weight: '700', size: 12 },
  bodyFont: _font,
  callbacks: {},
}

export const leg = {
  labels: {
    color: '#44556c',
    font: _font,
    boxWidth: 12,
    boxHeight: 12,
    borderRadius: 4,
    useBorderRadius: true,
  },
}

export const xAxis = (opts = {}) => ({
  grid: { color: 'rgba(33,96,162,0.09)' },
  border: { display: false },
  ticks: { color: '#5f6f85', font: _font, ...opts.ticks },
  ...opts,
})

export const yAxis = (opts = {}) => ({
  grid: { display: false },
  border: { display: false },
  ticks: { color: '#5f6f85', font: _font, ...opts.ticks },
  ...opts,
})
