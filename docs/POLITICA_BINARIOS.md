# Politica de Binarios

## Contexto

El repositorio ya contiene fuentes y evidencias binarias importantes:

- PDF oficial del anuario
- DOCX de insumos UVE
- XLSX de productividad y presupuesto
- screenshots de QA
- referencias visuales en PNG y ZIP

GitHub acepto el primer push, pero ya advirtio que el PDF principal supera el maximo recomendado de 50 MB.

## Regla Operativa

### Se pueden versionar directamente

- PNG y JPG de evidencia visual
- XLSX y DOCX de trabajo si son insumos oficiales
- ZIPs de referencia pequenos

### Deben evaluarse antes de subir

- cualquier archivo sobre 25 MB
- series grandes de screenshots repetitivos
- artefactos generados que puedan reconstruirse

### Deben preferir Git LFS o alternativa externa

- PDFs o binarios sobre 50 MB
- lotes grandes de imagenes
- salidas compiladas o exportadas que no sean fuente primaria

## Recomendacion Inmediata

En una segunda iteracion conviene mover al menos estos tipos a Git LFS:

- PDF fuente principal
- futuras versiones pesadas del anuario
- screenshots masivos de QA historico

## Criterio de Trazabilidad

Un binario debe quedarse en el repo solo si cumple al menos una de estas condiciones:

1. es fuente primaria del proyecto
2. no puede regenerarse facilmente
3. es evidencia necesaria de auditoria o decision
