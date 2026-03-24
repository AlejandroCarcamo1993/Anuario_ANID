const modules = import.meta.glob('../../data/*.json', {
  eager: true,
  import: 'default'
})

const entries = Object.entries(modules)
  .map(([filePath, data]) => {
    const match = filePath.match(/(\d{4})\.json$/)
    if (!match) return null

    return {
      year: Number(match[1]),
      data
    }
  })
  .filter(Boolean)
  .sort((left, right) => left.year - right.year)

export const availableYears = entries.map((entry) => entry.year)

export function getYearData(year) {
  return entries.find((entry) => entry.year === Number(year))?.data ?? null
}
