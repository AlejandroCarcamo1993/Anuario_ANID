/**
 * screenshot.js — Captura secciones del Anuario SCIA
 * Uso: node screenshot.js [sección]
 * Ejemplos:
 *   node screenshot.js             → captura sección visible (top)
 *   node screenshot.js panorama    → hero section
 *   node screenshot.js postulacion → sección 2
 *   node screenshot.js full        → página completa (scroll)
 *   node screenshot.js all         → todas las secciones
 */

const { chromium } = require('playwright-core');
const path = require('path');
const fs = require('fs');

const CHROME_PATH = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const HTML_FILE = path.resolve(__dirname, 'index.html');
const OUT_DIR = path.resolve(__dirname, 'screenshots');

if (!fs.existsSync(OUT_DIR)) fs.mkdirSync(OUT_DIR);

const SECTIONS = {
  panorama:    { id: 'panorama',    label: '1-Panorama' },
  postulacion: { id: 'postulacion', label: '2-Postulacion' },
  financiera:  { id: 'financiera',  label: '3-Financiera' },
  productividad:{ id:'productividad',label:'4-Productividad' },
  capital:     { id: 'capital',     label: '5-CapitalHumano' },
  diversidad:  { id: 'diversidad',  label: '6-Diversidad' },
  territorio:  { id: 'territorio',  label: '7-Territorio' },
  vinculacion: { id: 'vinculacion', label: '8-Vinculacion' },
};

async function shot(page, sectionId, label) {
  const ts = Date.now();
  let file;

  if (sectionId === '_full') {
    file = path.join(OUT_DIR, `full_${ts}.png`);
    await page.screenshot({ path: file, fullPage: true });
  } else if (sectionId === '_viewport') {
    file = path.join(OUT_DIR, `viewport_${ts}.png`);
    await page.screenshot({ path: file });
  } else {
    // Scroll to section + wait for animations
    await page.evaluate((id) => {
      const el = document.getElementById(id);
      if (el) el.scrollIntoView({ behavior: 'instant' });
    }, sectionId);
    await page.waitForTimeout(3500); // let reveal + counters animate
    await page.evaluate(() => {
      document.querySelectorAll('.reveal').forEach((el) => el.classList.add('visible'));
    });
    const el = await page.$(`#${sectionId}`);
    file = path.join(OUT_DIR, `${label}_${ts}.png`);
    if (el) {
      await el.screenshot({ path: file });
    } else {
      await page.screenshot({ path: file });
    }
  }

  const size = Math.round(fs.statSync(file).size / 1024);
  console.log(`  saved → ${path.basename(file)} (${size} KB)`);
  return file;
}

(async () => {
  const arg = process.argv[2] || '_viewport';
  console.log(`\nLaunching Chrome → file://${HTML_FILE}\n`);

  const browser = await chromium.launch({
    executablePath: CHROME_PATH,
    headless: true,
    args: ['--no-sandbox', '--disable-web-security', '--allow-file-access-from-files'],
  });

  const page = await browser.newPage();
  await page.setViewportSize({ width: 1440, height: 900 });
  await page.goto(`file:///${HTML_FILE.replace(/\\/g, '/')}`);
  await page.waitForTimeout(2800); // wait for fonts + charts

  if (arg === 'all') {
    for (const [key, val] of Object.entries(SECTIONS)) {
      await shot(page, val.id, val.label);
    }
  } else if (arg === 'full') {
    await shot(page, '_full', 'full');
  } else if (SECTIONS[arg]) {
    await shot(page, SECTIONS[arg].id, SECTIONS[arg].label);
  } else {
    await shot(page, '_viewport', 'viewport');
  }

  await browser.close();
  console.log(`\nDone. Screenshots in: ${OUT_DIR}\n`);
})();
