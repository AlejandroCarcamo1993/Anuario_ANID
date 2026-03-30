import { motion } from 'framer-motion'
import { ParticleCard } from './MagicBento/MagicBento'

const ITEM_VARIANTS = {
  hidden: { opacity: 0, y: 10 },
  visible: (i) => ({
    opacity: 1,
    y: 0,
    transition: { delay: i * 0.06, duration: 0.28, ease: [0.22, 1, 0.36, 1] },
  }),
}

export function MetricStrip({ items, formatter }) {
  return (
    <div className="metric-strip">
      {items.map((item, i) => (
        <motion.div
          key={item.id || item.label}
          custom={i}
          variants={ITEM_VARIANTS}
          initial="hidden"
          animate="visible"
        >
          <ParticleCard
            className="metric-card"
            glowColor="52, 79, 159"
            enableTilt={false}
            clickEffect={true}
            enableMagnetism={false}
            particleCount={6}
          >
            <span className="metric-card__label">{item.label}</span>
            <strong className="metric-card__value">{formatter(item.value, item.format)}</strong>
          </ParticleCard>
        </motion.div>
      ))}
    </div>
  )
}
