// Thumbnail + Shorts-hook document panels: exact excerpts of government filings / USAO releases (D. Minn. 24-cr-173),
// re-typeset large (text only, no seal). Run from the episode folder: NODE_PATH=$(npm root -g) node zoomcard.js
const { chromium } = require('playwright');
const HEAD = 'U.S. v. FARAH ET AL. · D. MINN.';
const BAG = `Ali approached the house with the gift bag containing the bribe money, handed it to a relative of <mark>Juror 52</mark> . . . Ali only delivered <mark>$120,000</mark> to Juror 52’s relative and kept the remaining <mark>$80,000</mark> cash for herself.`;
const CALL = `To her credit, <mark>Juror 52 immediately reported the bribery attempt to the police.</mark>`;
const STOLE = `On her way to meet with Abdulkarim Farah, Ms. Ali <mark>stole $80,000</mark> of the briber [sic] money for herself.`;
const IRONIC = `The jury returned its verdict on June 7, 2024, <mark>ironically acquitting</mark> the defendant on all counts.`;
const NOTE = `a list of instructions for Juror 52 that included directions for her to vote <mark>“NOT GUILTY ON ALL COUNTS FOR ALL DEFENDANTS”</mark>`;
const C = {
  // name: [html, font px, width, height, sub-header, layout: 1 vertical hook / 2 thumbnail panel]
  t_bag: [`handed it to a relative of <mark>Juror 52</mark> . . . delivered <mark>$120,000</mark> . . . and kept the remaining <mark>$80,000</mark> cash for herself.`, 54, 640, 720, 'USAO D. Minn. · Sep 5, 2024', 2],
  t_call: [`To her credit, <mark>Juror 52 immediately reported the bribery attempt to the police.</mark>`, 50, 540, 720, 'Gov’t sentencing memo · Dkt. 216', 2],
  t_note: [`directions for her to vote <mark>“NOT GUILTY ON ALL COUNTS FOR ALL DEFENDANTS”</mark>`, 62, 540, 720, 'USAO D. Minn. · Jun 26, 2024', 2],
  t_stole: [`Ms. Ali <mark>stole $80,000</mark> of the briber [sic] money for herself.`, 62, 640, 720, 'Gov’t sentencing memo · Dkt. 277', 2],
  t_bag120: [`Ali only delivered <mark>$120,000</mark> to <mark>Juror 52</mark>’s relative . . .`, 70, 640, 720, 'USAO D. Minn. · Sep 5, 2024', 2],
  t_note2: [`directions for her to vote <mark>“NOT GUILTY ON ALL COUNTS . . .”</mark>`, 66, 640, 720, 'USAO D. Minn. · Jun 26, 2024', 2],
  h_bag: [BAG, 60, 1080, 1920, 'USAO D. Minn. · Sep 5, 2024', 1],
  h_stole: [STOLE, 74, 1080, 1920, "Gov’t sentencing memo · Ladan Ali · Dkt. 277", 1],
  h_ironic: [`[Said Farah] collected a total of <mark>$200,000</mark> in cash . . . ${IRONIC}`, 66, 1080, 1920, 'Gov’t sentencing memo · Dkt. 251', 1],
};
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  for (const [n, [t, fs, w, h, sub, vert]] of Object.entries(C)) {
    const body = vert === 2
      ? `<div id="d" style="width:${w}px;height:${h}px;box-sizing:border-box;padding:112px 36px 0;background:#fbfaf6"><div style="font-family:'Liberation Serif',Georgia,serif;font-size:${fs}px;line-height:1.15;color:#111">${t}</div><div style="font:700 20px Arial;letter-spacing:.06em;color:#555;margin-top:18px">${sub.startsWith('USAO') ? 'U.S. ATTORNEY’S OFFICE · D. MINN.' : HEAD} · ${sub}</div></div>`
      : `<div id="d" style="width:${w}px;height:${h}px;background:#0b1020;position:relative"><div style="position:absolute;left:40px;right:40px;top:330px;padding:22px 36px 18px;background:#fbfaf6;box-shadow:0 10px 0 #000"><div style="font-family:'Liberation Serif',Georgia,serif;font-size:${fs}px;line-height:1.14;color:#111">${t}</div><div style="font:700 22px Arial;letter-spacing:.05em;color:#555;margin-top:12px">${sub.startsWith('USAO') ? 'U.S. ATTORNEY’S OFFICE · D. MINN.' : HEAD} · ${sub}</div></div></div>`;
    await p.setContent(`<html><body style="margin:0;background:#000">${body}<style>mark{background:#FFE81A;padding:0 4px}</style></body></html>`);
    await p.locator('#d').screenshot({ path: `img/${n}.jpg`, type: 'jpeg', quality: 92 }); console.log(n);
  }
  await b.close();
})();
