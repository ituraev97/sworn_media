// Thumbnail panel: the three "NEVER PURCHASED" boxes of the government's draft trial chart (media/1473651 p.2), re-typeset verbatim.
const { chromium } = require('playwright');
const box = (a, cc, m) => `<div style="background:#a9bfd8;border:3px solid #10202e;border-radius:14px;margin:0 0 14px;padding:8px 18px"><div style="font:700 25px Arial;color:#111">${a}, ${cc}</div><div style="display:flex;justify-content:space-between;align-items:baseline"><div style="font:400 38px Anton;color:#111"><span style="font-size:24px">INVESTMENT:</span> ${m}</div><div style="font:800 25px Arial;color:#C8102E">NEVER PURCHASED</div></div></div>`;
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 640, height: 720 } });
  const html = `<div id="d" style="width:640px;height:720px;background:#36414b;box-sizing:border-box;padding:22px 26px">
   <div style="font:700 18px Arial;letter-spacing:.05em;color:#cfd6de;margin-bottom:12px;margin-right:70px">RE-TYPESET FROM GOV'T TRIAL CHART (DRAFT)</div><div style="height:40px"></div>
   ${box('2401 HAZEL ST', 'TEXARKANA', '$225,000')}${box('701 EAST QUEENS ST', 'LUBBOCK', '$168,000')}${box('4041 RYAN AVE', 'FORT WORTH', '$290,000')}</div>`;
  await p.setContent(`<html><head><style>@font-face{font-family:Anton;src:url('file:///home/claude/sworn_media/pipeline/fonts/anton-latin-400-normal.woff2')}</style></head><body style="margin:0">${html}</body></html>`);
  await p.waitForTimeout(300);
  await p.locator('#d').screenshot({ path: 'img/t_never.jpg', type: 'jpeg', quality: 92 });
  const bx = (m, t) => `<div style="background:#46799d;border:3px solid #10202e;border-radius:16px;margin:0 0 16px;padding:14px 18px;text-align:center"><div style="font:400 58px Anton;color:#fff">${m}</div><div style="font:800 28px Arial;color:#fff;line-height:1.15">${t}</div></div>`;
  const html2 = `<div id="d" style="width:540px;height:720px;background:#36414b;box-sizing:border-box;padding:112px 26px 0">
   <div style="font:700 17px Arial;letter-spacing:.04em;color:#cfd6de;margin-bottom:10px">RE-TYPESET FROM GOV'T TRIAL CHART (DRAFT) · OCT 2023</div>
   <div style="font:800 26px Arial;color:#fff;margin-bottom:10px">RICHARD R GARCIA · BOA #4494 →</div>
   ${bx('$1,204.18', 'MERCEDES BENZ<br>FINANCIAL SERVICES')}</div>`;
  await p.setContent(`<html><head><style>@font-face{font-family:Anton;src:url('file:///home/claude/sworn_media/pipeline/fonts/anton-latin-400-normal.woff2')}</style></head><body style="margin:0">${html2}</body></html>`);
  await p.waitForTimeout(300);
  await p.locator('#d').screenshot({ path: 'img/t_merc.jpg', type: 'jpeg', quality: 92 }); await b.close();
})();
