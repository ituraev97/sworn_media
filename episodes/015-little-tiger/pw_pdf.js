const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36'});
  const jobs = JSON.parse(process.argv[2]);
  for (const [name, url] of jobs) {
    await p.goto(url, {waitUntil:'domcontentloaded', timeout:60000}); await p.waitForTimeout(2500);
    const txt = await p.evaluate(()=>document.body.innerText);
    require('fs').writeFileSync(`/home/claude/dl/doj/${name}.txt`, txt);
    await p.evaluate(() => {
      const main = document.querySelector('main') || document.body;
      const art = main.querySelector('article') || main;
      // keep only title, date, body
      const h1 = document.querySelector('h1');
      const keep = document.createElement('div'); keep.id='keep';
      keep.style.cssText='padding:40px 60px;font-family:Georgia,serif;color:#111;background:#fff';
      const date = [...document.querySelectorAll('time, .node-date, .date')][0];
      const comp = document.querySelector('.node-component, .field--name-field-component');
      const body = art.querySelector('.field--name-field-pr-body, .node-body, .field_body, .field--name-body') || art;
      keep.innerHTML = `<div style="font:600 18px Arial;letter-spacing:.06em;color:#333;text-transform:uppercase">U.S. Attorney's Office · Southern District of California · Press Release</div>` +
        (date?`<div style="font:18px Arial;color:#333;margin:10px 0 0">${date.innerText}</div>`:'') +
        (h1?`<h1 style="font:700 34px Georgia;line-height:1.25;margin:16px 0 22px">${h1.innerHTML}</h1>`:'') + body.innerHTML;
      document.body.innerHTML=''; document.body.appendChild(keep);
      document.querySelectorAll('#keep img, #keep svg, #keep iframe, #keep video, #keep button').forEach(e=>e.remove());
      const st=document.createElement('style'); st.textContent='#keep, #keep *{font-family:Georgia,serif !important;font-size:21px;line-height:1.5;color:#111 !important;background:none !important} #keep h1{font-size:34px !important;line-height:1.25 !important} #keep a{text-decoration:none} @page{size:8.5in 30in;margin:0}'; document.head.appendChild(st);
    });
    await p.pdf({path:`/home/claude/dl/doj/${name}.pdf`, width:'8.5in', height:'90in', printBackground:true, pageRanges:'1'});
    console.log('ok', name);
  }
  await b.close();
})();
