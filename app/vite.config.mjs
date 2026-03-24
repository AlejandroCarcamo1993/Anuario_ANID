import path from 'node:path'
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  root: path.resolve('app'),
  plugins: [react()],
  resolve: {
    alias: {
      '@': path.resolve('app/src'),
      '@data': path.resolve('data')
    }
  },
  server: {
    fs: {
      allow: [path.resolve('.')]
    }
  },
  build: {
    outDir: path.resolve('dist/app'),
    emptyOutDir: true
  }
})
