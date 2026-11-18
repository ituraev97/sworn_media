// Save the innerText of justice.gov press releases (Playwright, headless) to /home/claude/dl18/doj/<name>.txt
const { chromium } = require('playwright'); const fs = require('fs');
const R = {
  plea: 'https://www.justice.gov/usao-edla/pr/new-orleans-man-and-texas-woman-plead-guilty-conspiracy-commit-wire-fraud-and',
  ind: 'https://www.justice.gov/usao-edla/pr/new-orleans-man-and-texas-woman-indicted-wire-fraud-identity-theft-money-laundering',
};
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ userAgent: 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36' });
  for (const [n, u] of Object.entries(R)) {
    await p.goto(u, { waitUntil: 'domcontentloaded', timeout: 60000 }); await p.waitForTimeout(3000);
    fs.writeFileSync(`/home/claude/dl18/doj/${n}.txt`, await p.evaluate(() => document.querySelector('main').innerText)); console.log(n);
  }
  await b.close();
})();
