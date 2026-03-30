import { chromium } from './node_modules/playwright-core/index.js';

const browser = await chromium.launch({ headless: true });
const page = await browser.newPage();
const errors = [];
page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
page.on('pageerror', e => errors.push(e.toString()));

await page.goto('http://localhost:8766', { waitUntil: 'networkidle', timeout: 12000 });
await page.screenshot({ path: './debug_screen.png' });

console.log('TITLE:', await page.title());
console.log('ERRORS:', errors.length ? errors.join('\n') : 'ninguno');
const rootHtml = await page.evaluate(() => document.getElementById('root')?.innerHTML?.substring(0,600) ?? 'VACÍO');
console.log('ROOT:', rootHtml);
await browser.close();
