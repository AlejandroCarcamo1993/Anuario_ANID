#!/usr/bin/env node

const fs = require('node:fs')
const path = require('node:path')

function usage() {
  console.log('Uso: node scripts/scaffold-year.js <targetYear> [sourceFile] [outputFile]')
  console.log('Ejemplo: npm run scaffold:year -- 2025')
}

function blankKpis(kpis = []) {
  return kpis.map((item) => ({ ...item, value: null }))
}

function replaceYearInText(value, targetYear) {
  if (typeof value !== 'string') return value
  return value.replace(/\b20\d{2}\b/g, String(targetYear))
}

function buildScaffold(source, targetYear, sourceFile) {
  return {
    meta: {
      year: targetYear,
      title: `Anuario SCIA ${targetYear}`,
      description: `Scaffold base para poblar el anuario ${targetYear} manteniendo el contrato de datos actual.`,
      generatedAt: new Date().toISOString().slice(0, 10),
      generatedFrom: [path.basename(sourceFile)],
      scaffoldFromYear: source.meta?.year ?? null,
      status: 'scaffold',
      notes: [
        'Archivo base generado automaticamente para poblar un nuevo año sin romper el contrato del shell React.',
        'Las etiquetas estructurales se conservan y los datos/editoriales dependientes del año se vacian para ser completados.'
      ]
    },
    sectionOrder: [...(source.sectionOrder || [])],
    hero: {
      title: `Anuario SCIA ${targetYear}`,
      subtitle: replaceYearInText(source.hero?.subtitle ?? '', targetYear),
      statPills: (source.hero?.statPills || []).map((item) => ({
        ...item,
        value: typeof item.value === 'string' ? replaceYearInText(item.value, targetYear) : null
      }))
    },
    footer: {
      organization: source.footer?.organization ?? '',
      division: source.footer?.division ?? '',
      unit: source.footer?.unit ?? '',
      lastDataCut: null,
      sources: []
    },
    sections: {
      panorama: {
        sectionNumber: source.sections.panorama.sectionNumber,
        navLabel: replaceYearInText(source.sections.panorama.navLabel, targetYear),
        tagLabel: replaceYearInText(source.sections.panorama.tagLabel, targetYear),
        title: replaceYearInText(source.sections.panorama.title, targetYear),
        subtitle: replaceYearInText(source.sections.panorama.subtitle, targetYear),
        sources: [],
        kpis: blankKpis(source.sections.panorama.kpis),
        instrumentDistribution: source.sections.panorama.instrumentDistribution.map((item) => ({
          ...item,
          count: null,
          sharePct: null
        })),
        insights: []
      },
      postulacion: {
        sectionNumber: source.sections.postulacion.sectionNumber,
        navLabel: source.sections.postulacion.navLabel,
        tagLabel: replaceYearInText(source.sections.postulacion.tagLabel, targetYear),
        title: source.sections.postulacion.title,
        subtitle: replaceYearInText(source.sections.postulacion.subtitle, targetYear),
        sources: [],
        kpis: blankKpis(source.sections.postulacion.kpis),
        genderBreakdown: {
          postulaciones: { hombres: null, mujeres: null },
          adjudicaciones: { hombres: null, mujeres: null },
          tasaAdjudicacionPct: { hombres: null, mujeres: null }
        },
        genderGapTable: [],
        insights: []
      },
      financiera: {
        sectionNumber: source.sections.financiera.sectionNumber,
        navLabel: source.sections.financiera.navLabel,
        tagLabel: source.sections.financiera.tagLabel,
        title: source.sections.financiera.title,
        subtitle: replaceYearInText(source.sections.financiera.subtitle, targetYear),
        sources: [],
        kpis: blankKpis(source.sections.financiera.kpis),
        budgetByInstrument: source.sections.financiera.budgetByInstrument.map((item) => ({
          ...item,
          amount: null
        })),
        insights: []
      },
      productividad: {
        sectionNumber: source.sections.productividad.sectionNumber,
        navLabel: source.sections.productividad.navLabel,
        tagLabel: source.sections.productividad.tagLabel,
        title: source.sections.productividad.title,
        subtitle: replaceYearInText(source.sections.productividad.subtitle, targetYear),
        sources: [],
        publicaciones: {
          totalsByProgram: source.sections.productividad.publicaciones.totalsByProgram.map((item) => ({
            ...item,
            total: null,
            q1: Object.prototype.hasOwnProperty.call(item, 'q1') ? null : undefined
          }))
        },
        patentes: {
          totalsByInstrument: source.sections.productividad.patentes.totalsByInstrument.map((item) => ({
            ...item,
            patentes: null,
            derechoAutor: null,
            marcas: null,
            secretoIndustrial: null,
            servicioPi: null
          }))
        },
        tesis: {
          kpis: blankKpis(source.sections.productividad.tesis.kpis),
          levels: {
            pregrado: null,
            magister: null,
            doctorado: null
          },
          distributionByInstrument: source.sections.productividad.tesis.distributionByInstrument.map((item) => ({
            ...item,
            pregrado: null,
            magister: null,
            doctorado: null
          }))
        },
        congresos: {
          kpis: blankKpis(source.sections.productividad.congresos.kpis),
          distributionByInstrument: source.sections.productividad.congresos.distributionByInstrument.map((item) => ({
            ...item,
            nacional: null,
            internacional: null
          }))
        },
        divulgacion: {
          kpis: blankKpis(source.sections.productividad.divulgacion.kpis),
          medianAttendanceByInstrument: source.sections.productividad.divulgacion.medianAttendanceByInstrument.map((item) => ({
            ...item,
            medianAttendance: null
          }))
        },
        insights: []
      },
      capitalHumano: {
        sectionNumber: source.sections.capitalHumano.sectionNumber,
        navLabel: source.sections.capitalHumano.navLabel,
        tagLabel: source.sections.capitalHumano.tagLabel,
        title: source.sections.capitalHumano.title,
        subtitle: replaceYearInText(source.sections.capitalHumano.subtitle, targetYear),
        sources: [],
        kpis: blankKpis(source.sections.capitalHumano.kpis),
        agePyramid: source.sections.capitalHumano.agePyramid.map((item) => ({
          ...item,
          women: null,
          men: null
        })),
        insights: []
      },
      diversidad: {
        sectionNumber: source.sections.diversidad.sectionNumber,
        navLabel: source.sections.diversidad.navLabel,
        tagLabel: source.sections.diversidad.tagLabel,
        title: source.sections.diversidad.title,
        subtitle: replaceYearInText(source.sections.diversidad.subtitle, targetYear),
        sources: [],
        kpis: blankKpis(source.sections.diversidad.kpis),
        leadership: {
          razonHM: null,
          directivoFemeninoPct: null,
          liderazgoInvestigadorasPct: null,
          liderazgoJovenesPct: null
        },
        femaleParticipationByInstrument: source.sections.diversidad.femaleParticipationByInstrument.map((item) => ({
          ...item,
          valuePct: null
        })),
        insights: []
      },
      territorio: {
        sectionNumber: source.sections.territorio.sectionNumber,
        navLabel: source.sections.territorio.navLabel,
        tagLabel: source.sections.territorio.tagLabel,
        title: source.sections.territorio.title,
        subtitle: replaceYearInText(source.sections.territorio.subtitle, targetYear),
        sources: [],
        kpis: blankKpis(source.sections.territorio.kpis),
        regions: source.sections.territorio.regions.map((item) => ({
          ...item,
          count: null,
          pct: null
        })),
        insights: []
      },
      vinculacion: {
        sectionNumber: source.sections.vinculacion.sectionNumber,
        navLabel: source.sections.vinculacion.navLabel,
        tagLabel: source.sections.vinculacion.tagLabel,
        title: source.sections.vinculacion.title,
        subtitle: replaceYearInText(source.sections.vinculacion.subtitle, targetYear),
        sources: [],
        kpis: blankKpis(source.sections.vinculacion.kpis),
        summary: {
          title: '',
          lead: ''
        },
        dimensions: source.sections.vinculacion.dimensions.map((item) => ({
          ...item,
          count: null,
          timeframe: '',
          activities: []
        })),
        sourceNote: '',
        insights: [],
        scientificHighlights: {
          selectedCount: null,
          items: []
        }
      }
    }
  }
}

function main() {
  const [targetYearRaw, sourceFileRaw, outputFileRaw] = process.argv.slice(2)
  const targetYear = Number(targetYearRaw)

  if (!targetYear || Number.isNaN(targetYear)) {
    usage()
    process.exit(1)
  }

  const sourceFile = path.resolve(process.cwd(), sourceFileRaw || 'data/2024.json')
  const outputFile = path.resolve(
    process.cwd(),
    outputFileRaw || path.join('handoff', 'scaffolds', `${targetYear}.scaffold.json`)
  )

  if (!fs.existsSync(sourceFile)) {
    console.error(`No existe el archivo fuente: ${sourceFile}`)
    process.exit(1)
  }

  const source = JSON.parse(fs.readFileSync(sourceFile, 'utf8'))
  const scaffold = buildScaffold(source, targetYear, sourceFile)

  fs.mkdirSync(path.dirname(outputFile), { recursive: true })
  fs.writeFileSync(outputFile, `${JSON.stringify(scaffold, null, 2)}\n`, 'utf8')

  console.log(`Scaffold generado: ${path.relative(process.cwd(), outputFile)}`)
}

main()
