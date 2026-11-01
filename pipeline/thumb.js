// usage: node thumb.js <thumb.json> <assetsdir> <outdir>
// thumb.json = {"A":{"words":"THE|CONFESSION","accent":1,"hook":"$65B ON PAPER","img":"img/arrest2.jpg","pos":"50% 40%","zoom":1.6}, "C":{...}}
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const [, , SPEC, ASSETS, OUT] = process.argv; const S = JSON.parse(fs.readFileSync(SPEC));
const F = path.join(__dirname, 'fonts'), seal = path.join(__dirname, 'brand/seal.svg');
const html = v => `<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:'DM Serif Display';src:url(file://${F}/dm-serif-display-latin-400-normal.woff2)}
@font-face{font-family:'Inter';font-weight:800;src:url(file://${F}/inter-latin-800-normal.woff2)}
*{margin:0;box-sizing:border-box}body{width:1280px;height:720px;background:#0b1020;overflow:hidden;position:relative}
.ph{position:absolute;right:0;top:0;width:660px;height:720px;background:#fff url(file://${path.resolve(ASSETS, v.img)}) ${v.pos || '50% 30%'}/${(v.zoom || 1.4) * 100}% auto no-repeat;filter:contrast(1.15)}
.fade{position:absolute;right:560px;top:0;width:160px;height:720px;background:linear-gradient(90deg,#0b1020,rgba(11,16,32,0))}
.w{position:absolute;left:44px;top:70px;width:640px;font:400 ${v.size || 150}px/.9 'DM Serif Display';color:#f3eee3;text-shadow:0 6px 30px rgba(0,0,0,.6)}
.w em{font-style:normal;color:#c9a227}
.hook{position:absolute;left:48px;top:${v.hookTop || 470}px;background:#f2c94c;color:#0b1020;font:800 38px/1 Inter;letter-spacing:.04em;padding:16px 20px;border-radius:4px}
.seal{position:absolute;left:44px;bottom:34px;width:84px}
${v.stamp ? `.st{position:absolute;right:120px;top:${v.stampTop || 70}px;border:8px solid #c8102e;color:#c8102e;font:400 64px/1 'DM Serif Display';padding:12px 26px 4px;transform:rotate(-6deg);background:rgba(255,255,255,.85)}` : ''}
</style></head><body><div class="ph"></div><div class="fade"></div>
<div class="w">${v.words.split('|').map((x, i) => i === v.accent ? `<em>${x}</em>` : x).join('<br>')}</div>
<div class="hook">${v.hook}</div><img class="seal" src="file://${seal}">${v.stamp ? `<div class="st">${v.stamp}</div>` : ''}</body></html>`;
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1280, height: 720 } });
  for (const k of Object.keys(S)) {
    const f = path.join(OUT, `thumb_${k}.html`); fs.writeFileSync(f, html(S[k]));
    await p.goto('file://' + f); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(200);
    await p.screenshot({ path: path.join(OUT, `thumb_${k}.jpg`), type: 'jpeg', quality: 90 }); fs.unlinkSync(f);
  }
  await b.close(); console.log('thumbs', Object.keys(S));
})();
