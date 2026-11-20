// Save the innerText of the justice.gov press releases (Playwright, headless) to /home/claude/dl/brinks/doj/<name>.txt
const { chromium } = require('playwright'); const fs = require('fs');
const R = { pr26: 'https://www.justice.gov/usao-cdca/pr/ecuadorian-national-pleads-guilty-committing-several-truck-thefts-including-stealing',
            pr25: 'https://www.justice.gov/usao-cdca/pr/two-southern-california-men-arrested-charges-alleging-they-committed-largest-jewelry' };
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ userAgent: 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36' });
  for (const [n, u] of Object.entries(R)) {
    await p.goto(u, { waitUntil: 'domcontentloaded', timeout: 60000 }); await p.waitForTimeout(3000);
    fs.writeFileSync(`/home/claude/dl/brinks/doj/${n}.txt`, await p.evaluate(() => document.querySelector('main').innerText)); console.log(n);
  }
  await b.close();
})();
