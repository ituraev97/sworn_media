// usage: node render.js <workdir> <assetsdir> <out.mp4> [workers=2] [testTimes comma-separated]
// Renders <workdir>/timeline.json with stage.html at 30 fps (frame-exact, deterministic per t).
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path'); const { spawn, execFileSync } = require('child_process');
const [, , WD, ASSETS, OUT, WK = '2', TEST] = process.argv;
const T = JSON.parse(fs.readFileSync(path.join(WD, 'timeline.json')));
const fps = 30, N = Math.ceil(T.total * fps);
const size = T.mode === 'long' ? { width: 1920, height: 1080 } : { width: 1080, height: 1920 };
async function page(b) {
  const p = await b.newPage({ viewport: size });
  await p.goto('file://' + path.join(__dirname, 'stage.html'));
  await p.evaluate(([t, base]) => window.init(t, base), [T, path.resolve(ASSETS)]);
  await p.evaluate(() => document.fonts.ready);
  return p;
}
async function frame(p, t) {
  await p.evaluate(t => window.render(t), t);
  const pending = await p.evaluate(() => Promise.all([...document.images].filter(i => !i.complete).map(i => new Promise(r => { i.onload = i.onerror = r; }))).then(a => a.length));
  if (pending) await p.evaluate(t => window.render(t), t);
}
(async () => {
  const b = await chromium.launch();
  if (TEST) {
    const p = await page(b);
    for (const t of TEST.split(',').map(Number)) { await frame(p, t); await p.screenshot({ path: `${OUT}_${t}.jpg`, type: 'jpeg', quality: 85 }); }
    await b.close(); return;
  }
  const W = +WK, per = Math.ceil(N / W), parts = [];
  await Promise.all([...Array(W).keys()].map(async w => {
    const a = w * per, z = Math.min(N, a + per); if (a >= z) return;
    const p = await page(b); const part = path.join(WD, `part${w}.mp4`); parts[w] = part;
    const ff = spawn('ffmpeg', ['-v', 'error', '-y', '-f', 'image2pipe', '-framerate', '30', '-c:v', 'mjpeg', '-i', '-', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '17', '-pix_fmt', 'yuv420p', part]);
    for (let i = a; i < z; i++) {
      await frame(p, i / fps); const buf = await p.screenshot({ type: 'jpeg', quality: 92 });
      if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
      if ((i - a) % 600 === 0) console.log(`w${w} ${i - a}/${z - a}`);
    }
    ff.stdin.end(); await new Promise(r => ff.on('close', r));
  }));
  await b.close();
  const list = path.join(WD, 'parts.txt'); fs.writeFileSync(list, parts.filter(Boolean).map(p => `file '${p}'`).join('\n'));
  execFileSync('ffmpeg', ['-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', list, '-c', 'copy', OUT]);
  console.log('video done', OUT, N, 'frames');
})();
