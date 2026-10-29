import opentype from 'opentype.js';
import fs from 'fs';

const F='/tmp/claude-0/-home-claude/d9d83a47-141c-5b8c-9d4f-150b09114da6/scratchpad/fontwork/node_modules/@fontsource/';
const serif=opentype.parse(fs.readFileSync(F+'dm-serif-display/files/dm-serif-display-latin-400-normal.woff').buffer.slice(0));
const sans=opentype.parse(fs.readFileSync(F+'inter/files/inter-latin-800-normal.woff').buffer.slice(0));
const out=process.argv[2];
// text path with tracking, returns {d,width,bbox}
function txt(font,s,size,track=0){ let x=0, d=''; const parts=[];
  for(const ch of s){ const g=font.charToGlyph(ch); const p=g.getPath(x,0,size); parts.push(p); x+=g.advanceWidth*size/font.unitsPerEm+track; }
  const all=new opentype.Path(); parts.forEach(p=>all.extend(p)); const b=all.getBoundingBox();
  return {d:all.toPathData(2), w:b.x2-b.x1, h:b.y2-b.y1, b}; }
const GOLD='#C9A227', NIGHT='#0B1020', PAPER='#F3EEE3', RED='#C8102E', PANEL='#161D33';
function mark(cx,cy,R){ // seal
  const S=txt(serif,'S',R*1.25); const sx=cx-(S.b.x1+S.w/2), sy=cy-(S.b.y1+S.h/2);
  let ticks=''; for(let i=0;i<48;i++){const a=i/48*2*Math.PI; const r1=R*0.80,r2=R*0.88;
    ticks+=`<line x1="${(cx+r1*Math.cos(a)).toFixed(1)}" y1="${(cy+r1*Math.sin(a)).toFixed(1)}" x2="${(cx+r2*Math.cos(a)).toFixed(1)}" y2="${(cy+r2*Math.sin(a)).toFixed(1)}"/>`;}
  return `<circle cx="${cx}" cy="${cy}" r="${R*0.95}" fill="none" stroke="${GOLD}" stroke-width="${(R*0.06).toFixed(1)}"/>
<circle cx="${cx}" cy="${cy}" r="${R*0.74}" fill="none" stroke="${GOLD}" stroke-width="${(R*0.02).toFixed(1)}"/>
<g stroke="${GOLD}" stroke-width="${(R*0.022).toFixed(1)}" stroke-linecap="round">${ticks}</g>
<path transform="translate(${sx.toFixed(1)} ${sy.toFixed(1)})" fill="${GOLD}" d="${S.d}"/>`; }
// 1 mark
fs.writeFileSync(out+'/sworn-mark.svg',`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
<rect width="512" height="512" rx="96" fill="${NIGHT}"/>${mark(256,256,200)}</svg>`);
// 2 mark transparent (for overlays)
fs.writeFileSync(out+'/sworn-seal-gold.svg',`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">${mark(256,256,240)}</svg>`);
// 3 wordmark horizontal
const W=txt(serif,'SWORN',190,6); const K=txt(sans,'REAL TRIALS · REAL EVIDENCE',30,7);
const H=320, mx=160, tx=330;
const wy=H/2+10; 
const wordW = Math.max(W.w,K.w);
const total=tx+Math.max(W.w,K.w+84)+70;
fs.writeFileSync(out+'/sworn-wordmark.svg',`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${Math.ceil(total)} ${H}" width="${Math.ceil(total)}" height="${H}">
<rect width="100%" height="100%" rx="40" fill="${NIGHT}"/><g transform="translate(${mx-256*0.575} ${H/2-256*0.575}) scale(0.575)">${mark(256,256,200)}</g>
<path transform="translate(${(tx-W.b.x1).toFixed(1)} ${(wy-W.b.y2+W.b.y2).toFixed(1)})" fill="${PAPER}" d="${W.d}"/>
<rect x="${tx}" y="${wy+28}" width="64" height="6" fill="${RED}"/>
<path transform="translate(${(tx+84-K.b.x1).toFixed(1)} ${(wy+46).toFixed(1)})" fill="${GOLD}" d="${K.d}"/></svg>`);
// 4 YouTube banner 2560x1440, safe area 1546x423 centered
const BW=txt(serif,'SWORN',220,8); const tag=txt(sans,'REAL TRIALS.  REAL EVIDENCE.  THE VERDICT.',34,6);
const cx=1280, cy=720;
let rules=''; for(let i=0;i<5;i++){ rules+=`<line x1="0" y1="${560+i*80}" x2="2560" y2="${560+i*80}"/>`; }
fs.writeFileSync(out+'/sworn-banner.svg',`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2560 1440" width="2560" height="1440">
<rect width="2560" height="1440" fill="${NIGHT}"/>
<g stroke="${PANEL}" stroke-width="2">${rules}</g>
<rect x="2020" y="0" width="540" height="1440" fill="${PANEL}"/>
<rect x="2020" y="0" width="12" height="1440" fill="${GOLD}"/>
<g transform="translate(${cx-520-256*0.75} ${cy-256*0.75}) scale(0.75)">${mark(256,256,200)}</g>
<path transform="translate(${(cx-320-BW.b.x1).toFixed(1)} ${(cy+60).toFixed(1)})" fill="${PAPER}" d="${BW.d}"/>
<rect x="${cx-320}" y="${cy+96}" width="90" height="8" fill="${RED}"/>
<path transform="translate(${(cx-320-tag.b.x1).toFixed(1)} ${(cy+168).toFixed(1)})" fill="${GOLD}" d="${tag.d}"/>
</svg>`);
console.log('ok', W.w, K.w);
