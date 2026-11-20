// Thumbnail + Shorts-hook document panels: exact excerpts of the plea agreement (C.D. Cal. Dkt. 158, filed Nov 9, 2026)
// re-typeset large (text only, no seal). Run from the episode folder: NODE_PATH=$(npm root -g) node zoomcard.js
const { chromium } = require('playwright');
const HEAD = 'U.S. v. MESTANZA CERCADO · C.D. CAL.';
const T24 = `defendant and co-conspirators broke the locks on the Brinks truck and stole <mark>24 bags of jewelry</mark>, which the victims later valued at approximately <mark>$100,000,000</mark> . . .`;
const T10 = `certain victims declared in their transportation contracts with Brinks a total value of <mark>less than $10,000,000</mark> for the jewelry that Brinks was to transport, and the USAO disputes that those declarations limit the victims’ actual losses.`;
const TX = `defendant texted someone about his <mark>“stupidities from the past that I’m now paying for”</mark>`;
const C = {
  // name: [html, font px, width, height, sub-header, layout: 0 card / 1 vertical hook / 2 thumbnail panel]
  t_24: [`broke the locks on the Brinks truck and stole <mark>24 bags of jewelry</mark>, which the victims later valued at approximately <mark>$100,000,000</mark> . . .`, 56, 640, 720, 'Plea agreement ¶ 13 · July 11, 2022', 2],
  t_10m: [`Defendant contends that . . . ${T10}`, 44, 640, 720, 'Plea agreement ¶ 9 · his contention', 2],
  t_texts: [`<div class="who">JUNE 18–20, 2025:</div>${TX} . . .`, 60, 540, 720, 'Plea agreement ¶ 13', 2],
  h_24: [T24, 62, 1080, 1920, 'Plea agreement ¶ 13 · July 11, 2022', 1],
  h_10m: [`Defendant contends that . . . certain victims declared in their transportation contracts with Brinks a total value of <mark>less than $10,000,000</mark> for the jewelry that Brinks was to transport . . .`, 64, 1080, 1920, 'Plea agreement ¶ 9 · his contention', 1],
  h_texts: [`After the indictment . . . ${TX} . . .`, 66, 1080, 1920, 'Plea agreement ¶ 13 · June 2025', 1],
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
