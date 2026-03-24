export function formatValue(value, format) {
  if (format === 'percentage') {
    return `${Number(value).toLocaleString('es-CL', {
      minimumFractionDigits: Number(value) % 1 === 0 ? 0 : 1,
      maximumFractionDigits: 1
    })}%`
  }

  if (format === 'currency_clp_thousands') {
    return `M$${Number(value).toLocaleString('es-CL')}`
  }

  if (typeof value === 'number') {
    return value.toLocaleString('es-CL')
  }

  return String(value)
}
