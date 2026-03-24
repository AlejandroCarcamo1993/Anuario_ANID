#!/usr/bin/env node

const fs = require('node:fs');
const path = require('node:path');

const args = process.argv.slice(2);
const strict = args.includes('--strict');
const inputPaths = args.filter((arg) => arg !== '--strict');

function issue(issues, severity, at, message) {
  issues.push({ severity, at, message });
}

function isNumber(value) {
  return typeof value === 'number' && Number.isFinite(value);
}

function approxEqual(left, right, tolerance = 0.11) {
  return Math.abs(left - right) <= tolerance;
}

function sumBy(items, key) {
  return items.reduce((acc, item) => acc + (Number(item?.[key]) || 0), 0);
}

function getKpiMap(section) {
  const map = new Map();
  for (const item of section?.kpis || []) {
    if (item?.id) {
      map.set(item.id, item.value);
    }
  }
  return map;
}

function ensureArray(issues, value, at) {
  if (!Array.isArray(value)) {
    issue(issues, 'error', at, 'Debe ser un arreglo.');
    return false;
  }
  return true;
}

function ensureString(issues, value, at) {
  if (typeof value !== 'string' || !value.trim()) {
    issue(issues, 'error', at, 'Debe ser un texto no vacio.');
    return false;
  }
  return true;
}

function ensureSectionBasics(section, sectionKey, issues, options = {}) {
  const { requireKpis = true } = options;
  ensureString(issues, section?.title, `sections.${sectionKey}.title`);
  ensureString(issues, section?.subtitle, `sections.${sectionKey}.subtitle`);
  ensureArray(issues, section?.sources, `sections.${sectionKey}.sources`);
  if (requireKpis) {
    ensureArray(issues, section?.kpis, `sections.${sectionKey}.kpis`);
  }
}

function validatePanorama(section, issues) {
  const kpis = getKpiMap(section);
  const iniciativas = kpis.get('iniciativas');
  const rows = section.instrumentDistribution || [];
  if (!ensureArray(issues, rows, 'sections.panorama.instrumentDistribution')) return;
  const totalCount = sumBy(rows, 'count');
  const totalPct = sumBy(rows, 'sharePct');
  if (isNumber(iniciativas) && totalCount !== iniciativas) {
    issue(issues, 'warn', 'sections.panorama.instrumentDistribution', `La suma por instrumento es ${totalCount} y no coincide con iniciativas (${iniciativas}).`);
  }
  if (!approxEqual(totalPct, 100)) {
    issue(issues, 'warn', 'sections.panorama.instrumentDistribution', `La suma de porcentajes es ${totalPct.toFixed(1)} y no cierra en 100.0.`);
  }
}

function validatePostulacion(section, issues) {
  const kpis = getKpiMap(section);
  const post = section.genderBreakdown?.postulaciones || {};
  const adj = section.genderBreakdown?.adjudicaciones || {};
  const rates = section.genderBreakdown?.tasaAdjudicacionPct || {};
  const totalPost = (post.hombres || 0) + (post.mujeres || 0);
  const totalAdj = (adj.hombres || 0) + (adj.mujeres || 0);
  const femaleShare = totalAdj ? (adj.mujeres / totalAdj) * 100 : 0;
  const maleRate = post.hombres ? (adj.hombres / post.hombres) * 100 : 0;
  const femaleRate = post.mujeres ? (adj.mujeres / post.mujeres) * 100 : 0;

  if (isNumber(kpis.get('totalPostulaciones')) && totalPost !== kpis.get('totalPostulaciones')) {
    issue(issues, 'warn', 'sections.postulacion.genderBreakdown.postulaciones', `Hombres + mujeres suma ${totalPost} y no coincide con totalPostulaciones (${kpis.get('totalPostulaciones')}).`);
  }
  if (isNumber(kpis.get('totalAdjudicaciones')) && totalAdj !== kpis.get('totalAdjudicaciones')) {
    issue(issues, 'warn', 'sections.postulacion.genderBreakdown.adjudicaciones', `Hombres + mujeres suma ${totalAdj} y no coincide con totalAdjudicaciones (${kpis.get('totalAdjudicaciones')}).`);
  }
  if (isNumber(kpis.get('participacionFemeninaAdjudicada')) && !approxEqual(femaleShare, kpis.get('participacionFemeninaAdjudicada'))) {
    issue(issues, 'warn', 'sections.postulacion.kpis.participacionFemeninaAdjudicada', `La participacion femenina calculada es ${femaleShare.toFixed(1)}% y no coincide con ${kpis.get('participacionFemeninaAdjudicada')}%.`);
  }
  if (isNumber(rates.hombres) && !approxEqual(maleRate, rates.hombres)) {
    issue(issues, 'warn', 'sections.postulacion.genderBreakdown.tasaAdjudicacionPct.hombres', `La tasa masculina calculada es ${maleRate.toFixed(1)}% y no coincide con ${rates.hombres}%.`);
  }
  if (isNumber(rates.mujeres) && !approxEqual(femaleRate, rates.mujeres)) {
    issue(issues, 'warn', 'sections.postulacion.genderBreakdown.tasaAdjudicacionPct.mujeres', `La tasa femenina calculada es ${femaleRate.toFixed(1)}% y no coincide con ${rates.mujeres}%.`);
  }
}

function validateFinanciera(section, issues) {
  const kpis = getKpiMap(section);
  const rows = section.budgetByInstrument || [];
  if (!ensureArray(issues, rows, 'sections.financiera.budgetByInstrument')) return;
  const budgetSum = sumBy(rows, 'amount');
  const totalEjecutado = kpis.get('totalEjecutado');
  const centros = kpis.get('ejecutadoCentros');
  const proyectos = kpis.get('ejecutadoProyectos');

  if (isNumber(totalEjecutado) && budgetSum !== totalEjecutado) {
    issue(issues, 'warn', 'sections.financiera.budgetByInstrument', `La suma por instrumento es ${budgetSum} y no coincide con totalEjecutado (${totalEjecutado}).`);
  }
  if (isNumber(centros) && isNumber(proyectos) && isNumber(totalEjecutado)) {
    const combined = centros + proyectos;
    if (combined !== totalEjecutado) {
      issue(issues, 'warn', 'sections.financiera.kpis', `Ejecutado en centros + proyectos suma ${combined} y no coincide con totalEjecutado (${totalEjecutado}).`);
    }
  }
}

function validateProductividad(section, issues) {
  for (const item of section.publicaciones?.totalsByProgram || []) {
    if (isNumber(item.q1) && isNumber(item.total) && item.q1 > item.total) {
      issue(issues, 'warn', 'sections.productividad.publicaciones', `Q1 supera al total en ${item.program}.`);
    }
  }

  const tesisKpis = getKpiMap(section.tesis || {});
  const tesisLevels = section.tesis?.levels || {};
  const tesisTotal = (tesisLevels.pregrado || 0) + (tesisLevels.magister || 0) + (tesisLevels.doctorado || 0);
  if (isNumber(tesisKpis.get('totalTesis')) && tesisTotal !== tesisKpis.get('totalTesis')) {
    issue(issues, 'warn', 'sections.productividad.tesis.levels', `La suma de niveles es ${tesisTotal} y no coincide con totalTesis (${tesisKpis.get('totalTesis')}).`);
  }

  const tesisRows = section.tesis?.distributionByInstrument || [];
  if (Array.isArray(tesisRows)) {
    const pregrado = sumBy(tesisRows, 'pregrado');
    const magister = sumBy(tesisRows, 'magister');
    const doctorado = sumBy(tesisRows, 'doctorado');
    if (pregrado !== (tesisLevels.pregrado || 0)) {
      issue(issues, 'warn', 'sections.productividad.tesis.distributionByInstrument', `La suma de pregrado es ${pregrado} y no coincide con levels.pregrado (${tesisLevels.pregrado || 0}).`);
    }
    if (magister !== (tesisLevels.magister || 0)) {
      issue(issues, 'warn', 'sections.productividad.tesis.distributionByInstrument', `La suma de magister es ${magister} y no coincide con levels.magister (${tesisLevels.magister || 0}).`);
    }
    if (doctorado !== (tesisLevels.doctorado || 0)) {
      issue(issues, 'warn', 'sections.productividad.tesis.distributionByInstrument', `La suma de doctorado es ${doctorado} y no coincide con levels.doctorado (${tesisLevels.doctorado || 0}).`);
    }
  }

  const congresoKpis = getKpiMap(section.congresos || {});
  const congresoRows = section.congresos?.distributionByInstrument || [];
  if (Array.isArray(congresoRows)) {
    const congresosTotal = congresoRows.reduce((acc, item) => acc + (item.nacional || 0) + (item.internacional || 0), 0);
    if (isNumber(congresoKpis.get('presentaciones')) && congresosTotal !== congresoKpis.get('presentaciones')) {
      issue(issues, 'warn', 'sections.productividad.congresos.distributionByInstrument', `La suma de nacional + internacional es ${congresosTotal} y no coincide con presentaciones (${congresoKpis.get('presentaciones')}).`);
    }
  }
}

function validateCapitalHumano(section, issues) {
  const kpis = getKpiMap(section);
  const women = kpis.get('mujeres');
  const men = kpis.get('hombres');
  const total = kpis.get('total');

  if (isNumber(women) && isNumber(men) && isNumber(total) && women + men !== total) {
    issue(issues, 'warn', 'sections.capitalHumano.kpis', `Mujeres + hombres suma ${women + men} y no coincide con total (${total}).`);
  }

  const ageRows = section.agePyramid || [];
  if (Array.isArray(ageRows)) {
    const ageWomen = sumBy(ageRows, 'women');
    const ageMen = sumBy(ageRows, 'men');
    if (isNumber(women) && ageWomen !== women) {
      issue(issues, 'warn', 'sections.capitalHumano.agePyramid', `La suma de mujeres por tramo es ${ageWomen} y no coincide con el KPI (${women}).`);
    }
    if (isNumber(men) && ageMen !== men) {
      issue(issues, 'warn', 'sections.capitalHumano.agePyramid', `La suma de hombres por tramo es ${ageMen} y no coincide con el KPI (${men}).`);
    }
  }
}

function validateDiversidad(section, issues) {
  const kpis = getKpiMap(section);
  const women = kpis.get('mujeres');
  const men = kpis.get('hombres');
  const total = kpis.get('total');

  if (isNumber(women) && isNumber(men) && isNumber(total) && women + men !== total) {
    issue(issues, 'warn', 'sections.diversidad.kpis', `Mujeres + hombres suma ${women + men} y no coincide con total (${total}).`);
  }
  if (isNumber(women) && isNumber(total) && isNumber(kpis.get('mujeresPct'))) {
    const womenPct = (women / total) * 100;
    if (!approxEqual(womenPct, kpis.get('mujeresPct'))) {
      issue(issues, 'warn', 'sections.diversidad.kpis.mujeresPct', `El porcentaje femenino calculado es ${womenPct.toFixed(1)}% y no coincide con ${kpis.get('mujeresPct')}%.`);
    }
  }
  if (isNumber(men) && isNumber(total) && isNumber(kpis.get('hombresPct'))) {
    const menPct = (men / total) * 100;
    if (!approxEqual(menPct, kpis.get('hombresPct'))) {
      issue(issues, 'warn', 'sections.diversidad.kpis.hombresPct', `El porcentaje masculino calculado es ${menPct.toFixed(1)}% y no coincide con ${kpis.get('hombresPct')}%.`);
    }
  }
}

function validateTerritorio(section, issues) {
  const kpis = getKpiMap(section);
  const rows = section.regions || [];
  if (!ensureArray(issues, rows, 'sections.territorio.regions')) return;
  const totalRegions = sumBy(rows, 'count');
  const iniciativas = kpis.get('iniciativas');
  if (isNumber(iniciativas) && totalRegions !== iniciativas) {
    issue(issues, 'warn', 'sections.territorio.regions', `La suma regional es ${totalRegions} y no coincide con iniciativas (${iniciativas}).`);
  }

  const sorted = [...rows].sort((left, right) => (right.count || 0) - (left.count || 0));
  const top3Count = sumBy(sorted.slice(0, 3), 'count');
  const top3Pct = iniciativas ? (top3Count / iniciativas) * 100 : 0;
  if (isNumber(kpis.get('regionesPrincipalesPct')) && !approxEqual(top3Pct, kpis.get('regionesPrincipalesPct'))) {
    issue(issues, 'warn', 'sections.territorio.kpis.regionesPrincipalesPct', `El top 3 regional calcula ${top3Pct.toFixed(1)}% y no coincide con ${kpis.get('regionesPrincipalesPct')}%.`);
  }
}

function validateVinculacion(section, issues) {
  const kpis = getKpiMap(section);
  const dims = section.dimensions || [];
  if (!ensureArray(issues, dims, 'sections.vinculacion.dimensions')) return;

  const dimTotal = sumBy(dims, 'count');
  if (isNumber(kpis.get('actividadesUve')) && dimTotal !== kpis.get('actividadesUve')) {
    issue(issues, 'warn', 'sections.vinculacion.dimensions', `La suma de dimensiones es ${dimTotal} y no coincide con actividadesUve (${kpis.get('actividadesUve')}).`);
  }

  for (const dim of dims) {
    const activities = dim.activities || [];
    if (!Array.isArray(activities)) {
      issue(issues, 'error', `sections.vinculacion.dimensions.${dim.id}.activities`, 'Debe ser un arreglo.');
      continue;
    }
    if (isNumber(dim.count) && activities.length !== dim.count) {
      issue(issues, 'warn', `sections.vinculacion.dimensions.${dim.id}.activities`, `Hay ${activities.length} actividades y el count declarado es ${dim.count}.`);
    }
  }

  const selectedCount = section.scientificHighlights?.selectedCount;
  const highlightItems = section.scientificHighlights?.items || [];
  if (isNumber(selectedCount) && selectedCount !== highlightItems.length) {
    issue(issues, 'warn', 'sections.vinculacion.scientificHighlights', `selectedCount es ${selectedCount} y hay ${highlightItems.length} items.`);
  }
}

function validateData(data, filePath) {
  const issues = [];

  if (!data || typeof data !== 'object' || Array.isArray(data)) {
    issue(issues, 'error', path.basename(filePath), 'El archivo debe contener un objeto JSON en la raiz.');
    return issues;
  }

  ensureString(issues, data.meta?.title, 'meta.title');
  if (!isNumber(data.meta?.year)) {
    issue(issues, 'error', 'meta.year', 'Debe ser numerico.');
  }

  if (!ensureArray(issues, data.sectionOrder, 'sectionOrder')) {
    return issues;
  }
  if (!data.sections || typeof data.sections !== 'object' || Array.isArray(data.sections)) {
    issue(issues, 'error', 'sections', 'Debe ser un objeto con las secciones del anuario.');
    return issues;
  }

  const sectionKeys = Object.keys(data.sections);
  for (const key of data.sectionOrder) {
    if (!data.sections[key]) {
      issue(issues, 'error', `sectionOrder.${key}`, 'La seccion declarada no existe en sections.');
    }
  }
  for (const key of sectionKeys) {
    if (!data.sectionOrder.includes(key)) {
      issue(issues, 'warn', `sections.${key}`, 'La seccion existe pero no esta incluida en sectionOrder.');
    }
    ensureSectionBasics(data.sections[key], key, issues, {
      requireKpis: key !== 'productividad'
    });
  }

  validatePanorama(data.sections.panorama, issues);
  validatePostulacion(data.sections.postulacion, issues);
  validateFinanciera(data.sections.financiera, issues);
  validateProductividad(data.sections.productividad, issues);
  validateCapitalHumano(data.sections.capitalHumano, issues);
  validateDiversidad(data.sections.diversidad, issues);
  validateTerritorio(data.sections.territorio, issues);
  validateVinculacion(data.sections.vinculacion, issues);

  return issues;
}

function resolveFiles() {
  if (inputPaths.length > 0) {
    return inputPaths.map((item) => path.resolve(process.cwd(), item));
  }

  const dataDir = path.join(process.cwd(), 'data');
  if (!fs.existsSync(dataDir)) {
    return [];
  }

  return fs.readdirSync(dataDir)
    .filter((file) => file.endsWith('.json'))
    .map((file) => path.join(dataDir, file))
    .sort();
}

function main() {
  const files = resolveFiles();
  if (files.length === 0) {
    console.error('No se encontraron archivos JSON para validar.');
    process.exit(1);
  }

  let totalErrors = 0;
  let totalWarnings = 0;

  for (const filePath of files) {
    let data;
    try {
      data = JSON.parse(fs.readFileSync(filePath, 'utf8'));
    } catch (error) {
      totalErrors += 1;
      console.error(`[ERROR] ${path.relative(process.cwd(), filePath)} -> JSON invalido: ${error.message}`);
      continue;
    }

    const issues = validateData(data, filePath);
    const errors = issues.filter((item) => item.severity === 'error');
    const warnings = issues.filter((item) => item.severity === 'warn');
    totalErrors += errors.length;
    totalWarnings += warnings.length;

    console.log(`\n${path.relative(process.cwd(), filePath)}`);
    if (issues.length === 0) {
      console.log('  OK - sin observaciones');
      continue;
    }

    for (const item of issues) {
      console.log(`  [${item.severity.toUpperCase()}] ${item.at} - ${item.message}`);
    }
  }

  console.log(`\nResumen: ${totalErrors} errores, ${totalWarnings} advertencias.`);
  if (totalErrors > 0 || (strict && totalWarnings > 0)) {
    process.exit(1);
  }
}

main();
