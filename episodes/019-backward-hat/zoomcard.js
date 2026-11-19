// Thumbnail + Shorts-hook document panels: exact excerpts of the S.D.N.Y. criminal complaint (sworn Nov 17, 2026) re-typeset large
// (text only, no seal). Run from the episode folder: NODE_PATH=$(npm root -g) node zoomcard.js
const { chromium } = require('playwright');
const HEAD = 'U.S. v. WILLIAMS &amp; JOHNSON · S.D.N.Y.';
const C = {
  // name: [html, font px, width, height, sub-header, vertical (hook) layout]
  z_991: [`<div class="who">BACKWARD HAT EMPLOYEE:</div><div>Aggressive fund 10.01% Does this sound right?</div><div class="gap">[ . . . ]</div><div class="who">WILLIAMS:</div><div><mark>. . . Let’s do 9.91 bumped it up a bit</mark></div>`, 58, 640, 720, 'Criminal complaint ¶ 18 · texts of May 14, 2026'],
  z_130: [`Those payments included more than <mark>$130 million</mark> to accounts under the control of PHILLIP PATRICK WILLIAMS . . .`, 60, 640, 720, 'Criminal complaint ¶ 19(c) · allegation'],
  z_6pct: [`Backward Hat represented its monthly return rates to be <mark>between 6.01% and 7.21%</mark>.`, 64, 540, 720, 'Criminal complaint ¶ 17 · Oct 2023 – Sep 2026'],
  h_991: [`<div class="who">BACKWARD HAT EMPLOYEE:</div><div>Aggressive fund 10.01%<br>Does this sound right?</div><div class="gap">[ . . . ]</div><div class="who">WILLIAMS:</div><div><mark>. . . Let’s do 9.91<br>bumped it up a bit</mark></div>`, 46, 1080, 1920, 'Criminal complaint ¶ 18 · texts of May 14, 2026', 1],
  h_130: [`Those payments included more than <mark>$130 million</mark> to accounts under the control of PHILLIP PATRICK WILLIAMS, the defendant . . .`, 60, 1080, 1920, 'Criminal complaint ¶ 19(c) · allegation', 1],
  h_new: [`UC-1 received a response email on or about October 20, 2026, which stated that <mark>“[w]e are accepting new investors at the moment.”</mark>`, 62, 1080, 1920, 'Criminal complaint ¶ 27 · IRS undercover email', 1],
  t_991: [`<div class="who">WILLIAMS, MAY 14, 2026:</div><div><mark>“Let’s do 9.91 bumped it up a bit”</mark></div>`, 66, 640, 720, 'Criminal complaint ¶ 18', 2],
  t_130: [`more than <mark>$130 million</mark> to accounts under the control of PHILLIP PATRICK WILLIAMS . . .`, 58, 640, 720, 'Criminal complaint ¶ 19(c) · allegation', 2],
  t_6pct: [`<div class="who">MONTHLY RETURNS SHOWN:</div><mark>between 6.01% and 7.21%</mark>`, 76, 540, 720, 'Criminal complaint ¶ 17 · Oct 2023 – Sep 2026', 2],
};
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  for (const [n, [t, fs, w, h, sub, vert]] of Object.entries(C)) {
    const card = `<div style="font:700 ${vert ? 30 : 22}px Arial;letter-spacing:.08em;color:#444">${HEAD}</div><div style="font:${vert ? 28 : 21}px Arial;color:#555;margin:8px 0 ${vert ? 40 : 30}px">${sub}</div>
<div style="font-family:'Liberation Serif',Georgia,serif;font-size:${fs}px;line-height:1.2;color:#111">${t}</div>`;
    const body = vert === 2
      ? `<div id="d" style="width:${w}px;height:${h}px;box-sizing:border-box;padding:100px 36px 0;background:#fbfaf6"><div style="font-family:'Liberation Serif',Georgia,serif;font-size:${fs}px;line-height:1.15;color:#111">${t}</div><div style="font:700 20px Arial;letter-spacing:.06em;color:#555;margin-top:18px">${HEAD} · ${sub}</div></div>`
      : vert
      ? `<div id="d" style="width:${w}px;height:${h}px;background:#0b1020;position:relative"><div style="position:absolute;left:40px;right:40px;top:290px;padding:22px 36px 18px;background:#fbfaf6;box-shadow:0 10px 0 #000"><div style="font-family:'Liberation Serif',Georgia,serif;font-size:${fs}px;line-height:1.14;color:#111">${t}</div><div style="font:700 22px Arial;letter-spacing:.05em;color:#555;margin-top:12px">${HEAD} · ${sub}</div></div></div>`
      : `<div id="d" style="width:${w}px;height:${h}px;box-sizing:border-box;padding:54px 40px;background:#fbfaf6;display:flex;flex-direction:column;justify-content:center">${card}</div>`;
    await p.setContent(`<html><body style="margin:0;background:#000">${body}<style>mark{background:#FFE81A;padding:0 4px}.gap{font:700 .5em Arial;color:#777;margin:14px 0}.who{font:700 .62em Arial;letter-spacing:.06em;color:#444;margin-bottom:4px}</style></body></html>`);
    await p.locator('#d').screenshot({ path: `img/${n}.jpg`, type: 'jpeg', quality: 92 }); console.log(n);
  }
  await b.close();
})();
