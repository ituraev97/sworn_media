// Re-typeset the DOJ speech text (innerText saved with Playwright from justice.gov) as a clean text-only PDF: no seal/logo/images.
const { chromium } = require('playwright'); const fs = require('fs');
(async () => {
  const t = fs.readFileSync('/home/claude/dl17/caldwell.txt', 'utf8').split('\n').map(s => s.trim()).filter(Boolean);
  const title = t[t.indexOf('SPEECH') + 1], date = t[t.indexOf('SPEECH') + 2];
  const i0 = t.indexOf('Remarks as prepared for delivery'), i1 = t.indexOf('* * *');
  const body = t.slice(i0 + 1, i1);
  const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;');
  const html = `<html><head><meta charset="utf-8"><style>body{margin:0;background:#fff} #d{width:720px;padding:40px 48px;font-family:'Liberation Serif',Georgia,serif;color:#111;font-size:20px;line-height:1.5}
 .k{font:700 15px Arial;letter-spacing:.08em;text-transform:uppercase;color:#333} .dt{font:16px Arial;color:#333;margin-top:8px} h1{font-size:28px;line-height:1.25;margin:14px 0 20px} p{margin:0 0 14px}</style></head>
 <body><div id="d"><div class="k">U.S. Department of Justice · Office of Public Affairs · Speech</div><div class="dt">${esc(date)} · Remarks as prepared for delivery</div><h1>${esc(title)}</h1>${body.map(s => `<p>${esc(s)}</p>`).join('')}</div></body></html>`;
  const b = await chromium.launch(); const p = await b.newPage();
  await p.setContent(html); const h = await p.evaluate(() => document.getElementById('d').offsetHeight);
  await p.pdf({ path: '/home/claude/dl17/cald.pdf', width: '816px', height: `${h + 20}px`, printBackground: true, pageRanges: '1' });
  console.log(title, date, h); await b.close();
})();
