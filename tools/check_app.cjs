const { chromium } = require('./node_modules/playwright-core');
(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  const errors = [];
  page.on('console', m => { if (m.type() === 'error') errors.push('[CONSOLE ERROR] ' + m.text()); });
  page.on('pageerror', e => errors.push('[PAGE ERROR] ' + e.toString()));
  await page.goto('http://localhost:8766', { waitUntil: 'domcontentloaded', timeout: 10000 });
  await page.waitForTimeout(4000);
  await page.screenshot({ path: './debug_screen.png' });
  console.log('TITLE:', await page.title());
  console.log('--- ERRORS ---');
  errors.forEach(e => console.log(e));
  if (!errors.length) console.log('ninguno');
  const rootHtml = await page.evaluate(() => document.getElementById('root')?.innerHTML?.substring(0, 800) ?? 'VACIO');
  console.log('--- ROOT HTML ---');
  console.log(rootHtml);
  await browser.close();
})().catch(e => console.error('FAIL:', e.message));
