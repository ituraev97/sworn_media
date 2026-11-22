// Re-typeset a justice.gov press release (innerText saved by pw_pdf.js) as a clean PDF: text only, no seal/logo/images.
const { chromium } = require('playwright'); const fs = require('fs');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  for (const name of process.argv.slice(2)) {
    const t = fs.readFileSync(`/home/claude/dl/doj/${name}.txt`, 'utf8').split('\n').map(s => s.trim());
    const i0 = t.findIndex(s => s === 'For Immediate Release');
    let dateIdx = i0 - 1; while (dateIdx > 0 && !/^(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday), /.test(t[dateIdx])) dateIdx--;
    let titleIdx = dateIdx - 1; while (titleIdx > 0 && !t[titleIdx]) titleIdx--;
    const title = t[titleIdx], date = t[dateIdx];
    let end = t.findIndex((s, k) => k > i0 && s === 'Contact'); if (end < 0) end = t.length;
    const body = t.slice(i0 + 2, end).filter(s => s && !/@usdoj\.gov$/.test(s) && s !== 'Share');
    const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;');
    const html = `<html><head><meta charset="utf-8"><style>body{margin:0;background:#fff} #d{width:720px;padding:40px 48px;font-family:'Liberation Serif',Georgia,serif;color:#111;font-size:20px;line-height:1.5}
 .k{font:700 15px Arial;letter-spacing:.08em;text-transform:uppercase;color:#333} .dt{font:16px Arial;color:#333;margin-top:8px} h1{font-size:30px;line-height:1.25;margin:14px 0 20px} p{margin:0 0 14px}</style></head>
 <body><div id="d"><div class="k">U.S. Attorney's Office · District of Minnesota · Press Release</div><div class="dt">${esc(date)}</div><h1>${esc(title)}</h1>${body.map(s => `<p>${esc(s)}</p>`).join('')}</div></body></html>`;
    await p.setContent(html); const h = await p.evaluate(() => document.getElementById('d').offsetHeight);
    await p.pdf({ path: `/home/claude/dl/doj/${name}.pdf`, width: '816px', height: `${h + 20}px`, printBackground: true, pageRanges: '1' });
    console.log(name, title, date, h);
  }
  await b.close();
})();
