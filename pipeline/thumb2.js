// SWORN thumbnails v2 (owner decision 2026-11-14: "максимально яркие").
// usage: node thumb2.js <thumb2.json> <assetsdir> <outdir>
// thumb2.json = { "A": {
//   "left":  {"img": "img/face.jpg", "pos": "50% 30%", "zoom": 1.2}            // defendant photo (federal/public-domain only)
//         or {"number": "$127M", "label": "GUILTY"},                          // no photo -> giant number panel
//   "right": {"img": "img/doc.jpg", "pos": "30% 10%", "zoom": 1.6},           // seized assets / press conference / document
//   "split": 0.5,                                                             // width of the left panel (0..1); 1 = single image
//   "breaking": true, "tag": "SENTENCED",   // breaking only <= 7 days old; otherwise an optional factual tag                                                         // only when the news is <= 7 days old
//   "line1": "30 YEARS IN PRISON", "line2": "$250M FOOD FRAUD", "line2color": "red"|"yellow",
//   "circle": {"x": 900, "y": 300, "r": 90},  "arrow": {"x": 780, "y": 420, "rot": -30},
//   "stamp": "GUILTY" } , "B": {...}, "C": {...} }
// Bottom-right 260x90 stays clear (YouTube duration badge).
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const [, , SPEC, ASSETS, OUT0] = process.argv; const OUT = path.resolve(OUT0); const S = JSON.parse(fs.readFileSync(SPEC));
const F = path.join(__dirname, 'fonts'), seal = path.join(__dirname, 'brand/seal.svg');
const src = p => 'file://' + path.resolve(ASSETS, p);
const COL = { red: '#FF2A2A', yellow: '#FFE81A', white: '#FFFFFF' };
function panel(p, x, w) {
  if (!p) return '';
  if (p.number) return `<div class="num" style="left:${x}px;width:${w}px"><div class="n" style="font-size:${Math.min(220, Math.round(w * 1.7 / Math.max(3, p.number.length)))}px">${p.number}</div>${p.label ? `<div class="lab">${p.label}</div>` : ''}</div>`;
  if (p.q) {  // v3 "question" panel: huge stacked words on dark navy (owner 2026-11-17, from winners like "WHERE'S THE $250M?")
    const n = Math.max(...p.q.map(t => t.length)); const fs = Math.min(190, Math.round(w * 1.75 / Math.max(4, n)), Math.round(540 / p.q.length));
    return `<div class="qp" style="left:${x}px;width:${w}px">${p.q.map((t, i) => `<div style="font-size:${fs}px;color:${i === p.q.length - 1 ? '#FFE81A' : '#fff'}">${t}</div>`).join('')}</div>`;
  }
  const st = p.stamp ? `<div class="pst" style="${p.stampPos || 'left:50%;top:44%'}">${p.stamp}</div>` : '';
  const ch = p.chip ? `<div class="chip">${p.chip}</div>` : '';
  return `<div class="ph" style="left:${x}px;width:${w}px;background-image:url('${src(p.img)}');background-position:${p.pos || '50% 30%'};background-color:#0a0a0a;background-size:${p.cover ? 'cover' : p.fitH ? 'auto ' + ((p.zoom || 1) * 100) + '%' : ((p.zoom || 1) * 100) + '% auto'}">${p.vignette === false ? '' : '<div class="vig"></div>'}${st}${ch}</div>`;
}
const html = v => {
  const sw = Math.round(1280 * (v.split ?? 0.5));
  const l2 = COL[v.line2color || 'red'];
  return `<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:Anton;src:url(file://${F}/anton-latin-400-normal.woff2)}
@font-face{font-family:Inter;font-weight:800;src:url(file://${F}/inter-latin-800-normal.woff2)}
*{margin:0;box-sizing:border-box}body{width:1280px;height:720px;background:#000;overflow:hidden;position:relative}
.ph{position:absolute;top:0;height:720px;background-color:#fff;background-repeat:no-repeat;filter:saturate(1.35) contrast(1.18) brightness(1.04)}
.num{position:absolute;top:0;height:720px;background:radial-gradient(circle at 50% 40%,#d1001c 0%,#7a0010 70%,#3a0008 100%);display:flex;flex-direction:column;align-items:center;justify-content:center;padding-bottom:150px}
.num .n{font:400 220px/0.9 Anton;color:#FFE81A;-webkit-text-stroke:8px #000;paint-order:stroke fill;text-shadow:0 10px 0 #000,0 0 40px rgba(0,0,0,.6)}
.num .lab{margin-top:18px;background:#fff;color:#c4001a;font:400 64px/1 Anton;padding:10px 26px 6px;transform:rotate(-3deg);border:6px solid #000}
.qp{position:absolute;top:0;height:720px;background:radial-gradient(circle at 40% 40%,#14234a 0%,#0a1230 70%,#050916 100%);display:flex;flex-direction:column;justify-content:flex-end;padding:0 0 70px 46px}
.qp div{font-family:Anton;line-height:1.0;-webkit-text-stroke:8px #000;paint-order:stroke fill;text-shadow:0 8px 0 #000}
.pst{position:absolute;transform:translate(-50%,-50%) rotate(-9deg);border:9px solid #FF1E1E;color:#FF1E1E;background:rgba(255,255,255,.92);font:400 78px/1 Anton;padding:8px 22px 2px;box-shadow:0 6px 0 rgba(0,0,0,.6);white-space:nowrap}
.chip{position:absolute;left:16px;bottom:250px;background:#000;color:#fff;font:800 30px/1 Inter;padding:9px 14px;border-left:8px solid #FF1E1E}
.vig{position:absolute;inset:0;background:radial-gradient(ellipse 60% 70% at 50% 40%,rgba(0,0,0,0) 45%,rgba(0,0,0,.75) 100%)}
.div{position:absolute;top:0;left:${sw - 5}px;width:10px;height:720px;background:#fff;box-shadow:0 0 0 4px #000}
.shade{position:absolute;left:0;right:0;bottom:0;height:330px;background:linear-gradient(0deg,rgba(0,0,0,.92) 0%,rgba(0,0,0,.65) 55%,rgba(0,0,0,0) 100%)}
.cap{position:absolute;left:0;right:0;bottom:${v.capBottom ?? 26}px;text-align:center}
.cap div{font:400 ${v.size1 || 104}px/1.0 Anton;letter-spacing:.5px;-webkit-text-stroke:10px #000;paint-order:stroke fill;text-shadow:0 8px 0 #000}
.cap .l1{color:#fff}.cap .l2{color:${l2};font-size:${v.size2 || 112}px}
.brk{position:absolute;left:0;top:26px;background:#E0001B;color:#fff;font:italic 800 46px/1 Inter;padding:14px 30px 14px 26px;clip-path:polygon(0 0,100% 0,94% 100%,0 100%);letter-spacing:.02em;box-shadow:0 4px 0 #000}
.circ{position:absolute;border:12px solid #FF1E1E;border-radius:50%;box-shadow:0 0 0 4px #000, inset 0 0 0 4px #000}
.arr{position:absolute;width:190px;height:70px;transform-origin:100% 50%}
.stamp{position:absolute;right:70px;top:${v.stampTop || 70}px;border:10px solid #FF1E1E;color:#FF1E1E;background:rgba(255,255,255,.9);font:400 92px/1 Anton;padding:8px 26px 2px;transform:rotate(-8deg)}
.seal{position:absolute;right:22px;top:20px;width:74px;filter:drop-shadow(0 0 6px #000)}
</style></head><body>
${(v.split ?? 0.5) >= 1 ? panel(v.left || v.right, 0, 1280) : panel(v.left, 0, sw) + panel(v.right, sw, 1280 - sw) + '<div class="div"></div>'}
${v.line1 || v.line2 ? '<div class="shade"></div>' : ''}
${v.circle ? `<div class="circ" style="left:${v.circle.x - v.circle.r}px;top:${v.circle.y - v.circle.r}px;width:${v.circle.r * 2}px;height:${v.circle.r * 2}px"></div>` : ''}
${v.arrow ? `<svg class="arr" style="left:${v.arrow.x - 190}px;top:${v.arrow.y - 35}px;transform:rotate(${v.arrow.rot || 0}deg)" viewBox="0 0 190 70"><path d="M4 26 H130 V6 L186 35 L130 64 V44 H4 Z" fill="#FF1E1E" stroke="#000" stroke-width="6" stroke-linejoin="round"/></svg>` : ''}
${v.stamp ? `<div class="stamp">${v.stamp}</div>` : ''}
${v.breaking || v.tag ? `<div class="brk">${v.breaking ? 'BREAKING' : v.tag}</div>` : ''}
${v.seal === false ? '' : `<img class="seal" src="file://${seal}">`}
<div class="cap">${v.line1 ? `<div class="l1">${v.line1}</div>` : ''}${v.line2 ? `<div class="l2">${v.line2}</div>` : ''}</div>
</body></html>`;
};
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1280, height: 720 } });
  for (const k of Object.keys(S)) {
    const f = path.join(OUT, `thumb_${k}.html`); fs.writeFileSync(f, html(S[k]));
    await p.goto('file://' + f); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(250);
    await p.screenshot({ path: path.join(OUT, `thumb_${k}.jpg`), type: 'jpeg', quality: 92 }); fs.unlinkSync(f);
  }
  await b.close(); console.log('thumbs v2', Object.keys(S));
})();
