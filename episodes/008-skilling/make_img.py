"""Rasterize public-domain court/DOJ documents for SWORN 008 (Skilling / Enron), crop, and compute gold-highlight boxes (tesseract TSV).
Source: sk.pdf = archive.org micro_IA43085015_0478, "Skilling v. United States (No. 08-1394)" — U.S. Supreme Court case file:
  Pet. App. A = U.S. Court of Appeals for the Fifth Circuit opinion, No. 06-20885 (Jan 2009)  [court opinion — shown]
  Joint Appendix A = S.D. Tex. docket entries, No. 4:04-cr-00025 (jury verdict entry)       [court record — shown]
  Joint Appendix C = Superseding Indictment, U.S. v. Causey, Skilling & Lay, Cr. No. H-04-25 [DOJ/grand jury — shown]
  Brief for the United States (Solicitor General, merits, 2010)                              [DOJ — shown]
  (the defense petition, defense briefs, juror materials and press clippings in the same file are NOT shown)
Writes img/<name>.jpg and hl.json {name: [[y0,y1],...]}."""
import subprocess, os, json, csv, io, re
from PIL import Image
S = '/home/claude/src'; HI = '/home/claude/research/hi'
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, 'img')
def norm(t): return re.sub(r'[^a-z0-9]', '', t.lower())
def raster(src, page):
    base = f'{HI}/{src}-{page}'
    if not os.path.exists(base + '.png'):
        subprocess.run(['pdftoppm', '-r', '220', '-png', '-singlefile', '-gray', '-f', str(page), '-l', str(page), f'{S}/{src}', base], check=True)
    return base + '.png'
def find(path, start, end):
    im = Image.open(path); H = im.size[1]
    tsv = path + '.tsv'
    if not os.path.exists(tsv):
        open(tsv, 'w').write(subprocess.run(['tesseract', path, '-', 'tsv'], capture_output=True, text=True).stdout)
    ws = [r for r in csv.DictReader(io.StringIO(open(tsv).read()), delimiter='\t', quoting=csv.QUOTE_NONE) if r['text'] and norm(r['text'])]
    nth = 1
    if start[:2] in ('2:', '3:'): nth, start = int(start[0]), start[2:]
    toks = [norm(w['text']) for w in ws]; s = [norm(x) for x in start.split() if norm(x)]; e = [norm(x) for x in end.split() if norm(x)]
    for i in range(len(toks)):
        if toks[i:i + len(s)] == s and (nth := nth - 1) == 0:
            for j in range(i, min(len(toks), i + 400)):
                if toks[j:j + len(e)] == e:
                    seg = ws[i:j + len(e)]
                    return round(min(int(w['top']) for w in seg) / H, 4), round(max(int(w['top']) + int(w['height']) for w in seg) / H, 4)
    raise SystemExit(f'not found in {path}: {start!r} … {end!r}\n' + ' '.join(toks)[:2500])
P = 'sk.pdf'
# name: (page, y0, y1, x0, x1, [(start, end)])
jobs = {
 'ca5_cap':   (55, 0.03, 0.97, 0.04, 0.96, [('A jury convicted', 'auditors,')]),
 'ca5_bk':    (56, 0.03, 0.97, 0.04, 0.96, [('About four months', 'sudden bankruptcy.'), ('According to the government,', 'expectations.')]),
 'ca5_crack': (60, 0.03, 0.97, 0.04, 0.96, [('Rice likened', 'earnings.”')]),
 'ca5_calls': (61, 0.03, 0.97, 0.04, 0.96, [('Let me repeat', 'quarter results.”'), ('“not a trading', 'pany.”')]),
 'ca5_end':   (189, 0.03, 0.97, 0.04, 0.96, [('The court therefore erred', 'enhancement.'), ('we AFFIRM', 'resentencing.')]),
 'verdict':   (523, 0.03, 0.97, 0.04, 0.96, [('Redacted JURY VERDICT', 'filed.')]),
 'ind_cover': (580, 0.03, 0.97, 0.04, 0.96, [('SUPERSEDING', 'INDICTMENT')]),
 'ind_big':   (581, 0.03, 0.97, 0.04, 0.96, [('Before it filed', 'States.')]),
 'ind_call':  (612, 0.03, 0.97, 0.04, 0.96, [('On January 22, 2001,', 'quarter results.”')]),
 'ind_c42':   (661, 0.03, 0.97, 0.04, 0.96, [('COUNTS FORTY-TWO', 'Trading)'), ('SKILLING sold', 'shares of')]),
 'ind_c51':   (663, 0.03, 0.62, 0.04, 0.96, [('September 17,', '$31.0822')]),
 'sg_cover':  (2706, 0.03, 0.97, 0.04, 0.96, [('BRIEF FOR THE UNITED STATES', 'STATES')]),
 'sg_e':      (2707, 0.03, 0.97, 0.04, 0.96, [('as he told his managers,', 'earnings.”')]),
 'sg_ees':    (2708, 0.03, 0.97, 0.04, 0.96, [('first quarter earnings for EES', 'million loss.')]),
 'sg_opp':    (2709, 0.03, 0.97, 0.04, 0.96, [('According to the trial', 'truth.')]),
 'sg_sale':   (2710, 0.03, 0.97, 0.04, 0.96, [('That is not a gray', 'white.”'), ('on September 17,', 'transaction;')]),
 'sg_scared': (2711, 0.03, 0.97, 0.04, 0.96, [('by September 11,', 'the stock.”'), ('Less than three months', 'bankruptcy.')]),
}
hl = {}
if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for name, (page, y0, y1, x0, x1, phrases) in jobs.items():
        p = raster(P, page)
        im = Image.open(p).convert('L')
        boxes = [find(p, s, e) for s, e in phrases]
        for r in boxes:
            if not (y0 <= r[0] and r[1] <= y1): raise SystemExit(f'phrase outside crop: {name} {r}')
        W, H = im.size
        c = im.crop((int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H))).convert('RGB')
        c = c.resize((1480, int(c.height * 1480 / c.width)), Image.LANCZOS)
        c.save(f'{OUT}/{name}.jpg', quality=88)
        hl[name] = [[round((a - y0) / (y1 - y0) - 0.008, 4), round((b - y0) / (y1 - y0) + 0.008, 4)] for a, b in boxes]
        print(name, c.size, hl[name])
    json.dump(hl, open(os.path.join(HERE, 'hl.json'), 'w'), indent=1)
