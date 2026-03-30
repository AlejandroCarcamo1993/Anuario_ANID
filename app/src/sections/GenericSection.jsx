export function GenericSection({ section }) {
  if (section?._pending) {
    return (
      <div className="pending-section">
        <span className="material-symbols-outlined pending-section__icon">hourglass_empty</span>
        <p className="pending-section__label">Datos 2025 pendientes</p>
        <small className="pending-section__note">{section._pendingNote}</small>
      </div>
    )
  }
  return null
}
