// Thumbnail document panels: an exact excerpt of the U.S. Attorney's Nov 17, 2026 release, re-typeset large (text only, no seal).
const { chromium } = require('playwright');
const C = {
  zoom_total: ['…In total, THOMAS and THOMSPON <mark>stole between $1,500,000.00 and $3,000,000.00</mark> from the victim.', 70, 800],
  zoom_rolls: ['THOMPSON … <mark>arrived driving a Rolls Royce</mark> fraudulently obtained from the victim.', 68, 600],
};
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 800, height: 900 } });
  for (const [n, [t, fs, w]] of Object.entries(C)) {
    await p.setContent(`<html><body style="margin:0;background:#fff"><div id="d" style="width:${w}px;height:${w === 800 ? 900 : 800}px;box-sizing:border-box;padding:60px 44px;background:#fbfaf6">
<div style="font:700 22px Arial;letter-spacing:.08em;color:#444">U.S. ATTORNEY'S OFFICE · E.D. LOUISIANA</div><div style="font:22px Arial;color:#555;margin:8px 0 36px">Press release · November 17, 2026</div>
<div style="font-family:'Liberation Serif',Georgia,serif;font-size:${fs}px;line-height:1.22;color:#111">${t}</div></div>
<style>mark{background:#FFE81A;padding:0 4px}</style></body></html>`);
    await p.locator('#d').screenshot({ path: `img/${n}.jpg`, type: 'jpeg', quality: 92 }); console.log(n);
  }
  await b.close();
})();
