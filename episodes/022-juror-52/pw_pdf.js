// Save the innerText of justice.gov releases (Playwright, headless) to /home/claude/dl/doj/<name>.txt
const { chromium } = require('playwright'); const fs = require('fs');
const R = {
  pr24: 'https://www.justice.gov/usao-mn/pr/five-indicted-feeding-our-future-jury-bribery-scheme',
  prali: 'https://www.justice.gov/usao-mn/pr/seattle-woman-pleads-guilty-feeding-our-future-jury-bribery-scheme',
  prnur: 'https://www.justice.gov/usao-mn/pr/shakopee-man-pleads-guilty-feeding-our-future-jury-bribery-scheme',
};
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ userAgent: 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36' });
  for (const [n, u] of Object.entries(R)) {
    try { await p.goto(u, { waitUntil: 'domcontentloaded', timeout: 60000 }); await p.waitForTimeout(3000);
    fs.writeFileSync(`/home/claude/dl/doj/${n}.txt`, await p.evaluate(() => document.querySelector('main').innerText)); console.log(n); } catch (e) { console.log('ERR', n, e.message.slice(0, 80)); }
  }
  await b.close();
})();
