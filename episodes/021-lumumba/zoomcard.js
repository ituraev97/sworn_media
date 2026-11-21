// Thumbnail document panel: exact excerpt of the indictment (S.D. Miss. 3:24-cr-103, Dkt. 3, ¶ 57)
// re-typeset large (text only, no seal). Run from the episode folder: NODE_PATH=$(npm root -g) node zoomcard.js
const { chromium } = require('playwright');
const HEAD = 'U.S. v. OWENS, LUMUMBA & BANKS · S.D. MISS.';
const C = {
  // name: [html, font px, width, height, sub-header, layout: 0 card / 1 vertical hook / 2 thumbnail panel]
  t_checks: [`<div class="who">ON THE YACHT · FBI RECORDING:</div>OWENS: “These checks are Mississippi checks but <mark>they’re from this group.</mark>” LUMUMBA: <mark>“Okay.”</mark>`, 50, 540, 720, 'Indictment ¶ 57 · April 2, 2024', 2],
};
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  for (const [n, [t, fs, w, h, sub, vert]] of Object.entries(C)) {
    const body = vert === 2
      ? `<div id="d" style="width:${w}px;height:${h}px;box-sizing:border-box;padding:112px 36px 0;background:#fbfaf6"><div style="font-family:'Liberation Serif',Georgia,serif;font-size:${fs}px;line-height:1.15;color:#111">${t}</div><div style="font:700 20px Arial;letter-spacing:.06em;color:#555;margin-top:18px">${HEAD} · ${sub}</div></div>`
      : `<div id="d" style="width:${w}px;height:${h}px;background:#0b1020;position:relative"><div style="position:absolute;left:40px;right:40px;top:330px;padding:22px 36px 18px;background:#fbfaf6;box-shadow:0 10px 0 #000"><div style="font-family:'Liberation Serif',Georgia,serif;font-size:${fs}px;line-height:1.14;color:#111">${t}</div><div style="font:700 22px Arial;letter-spacing:.05em;color:#555;margin-top:12px">${HEAD} · ${sub}</div></div></div>`;
    await p.setContent(`<html><body style="margin:0;background:#000">${body}<style>mark{background:#FFE81A;padding:0 4px}.who{font:700 .62em Arial;letter-spacing:.06em;color:#444;margin-bottom:6px}</style></body></html>`);
    await p.locator('#d').screenshot({ path: `img/${n}.jpg`, type: 'jpeg', quality: 92 }); console.log(n);
  }
  await b.close();
})();
