"""Rasterize public-domain documents in Gideon v. Wainwright, crop, and compute gold-highlight boxes (tesseract TSV).
Sources (see sources.md):
  d1.pdf = Transcript of Record, Gideon v. Cochran, U.S. Supreme Court No. 155, Oct. Term 1962 (printed by the U.S. Government Printing Office):
           Florida circuit court information, minute-book entries, commitment (Bay County, Florida public records),
           Florida Supreme Court order of Oct 30, 1961, U.S. Supreme Court order of June 4, 1962.  archive.org micro_IA40385001_0301
           (the reporter's trial transcript and Gideon's own petition in this record are QUOTED, never shown)
  d7.pdf = Brief for the Respondent (Attorney General of Florida), same item
  usNNN.jpg = United States Reports vol. 372 (leaf NNN), Gideon v. Wainwright, 372 U.S. 335 (1963) — archive.org
           sim_united-states-supreme-court-cases-adjudged_february-18-april-26-1963_372
Writes img/<name>.jpg and hl.json {name: [[y0,y1],...]}."""
import subprocess, os, json, csv, io, re
from PIL import Image
S = '/home/claude/src'; HI = '/home/claude/research/hi'
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, 'img')
def norm(t): return re.sub(r'[^a-z0-9]', '', t.lower())
def raster(src, page):
    if src.endswith('.jpg'):
        return f'{S}/{src}'
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
    toks = [norm(w['text']) for w in ws]; s = [norm(x) for x in start.split()]; e = [norm(x) for x in end.split()]
    for i in range(len(toks)):
        if toks[i:i + len(s)] == s and (nth := nth - 1) == 0:
            for j in range(i, min(len(toks), i + 400)):
                if toks[j:j + len(e)] == e:
                    seg = ws[i:j + len(e)]
                    return round(min(int(w['top']) for w in seg) / H, 4), round(max(int(w['top']) + int(w['height']) for w in seg) / H, 4)
    raise SystemExit(f'not found in {path}: {start!r} … {end!r}\n' + ' '.join(toks)[:2500])
D1, D7 = 'd1.pdf', 'd7.pdf'
# name: (src, page, y0, y1, x0, x1, [(start, end)])
jobs = {
 'rec_cover':  (D1, 1, 0.03, 0.92, 0.03, 0.97, [('PETITION FOR CERTIORARI', 'JUNE 4, 1962')]),
 'info':       (D1, 4, 0.05, 0.66, 0.04, 0.96, [('Clarence Earl', 'lessee,')]),
 'verdict':    (D1, 7, 0.08, 0.98, 0.04, 0.96, [('2:We, the jury,', 'say we all.')]),
 'sentence':   (D1, 8, 0.05, 0.75, 0.04, 0.96, [('the sentence of the law that', 'five years')]),
 'fl_order':   (D1, 50, 0.03, 0.50, 0.04, 0.96, [('petitioner', 'denied')]),
 'cert':       (D1, 51, 0.03, 0.42, 0.04, 0.96, [('Should this', 'reconsider')]),
 'fl_5000':    (D7, 16, 0.45, 0.80, 0.06, 0.94, [('A decision reversing', 'set free.')]),
 'fl_survey':  (D7, 61, 0.28, 0.92, 0.06, 0.94, [('As of June 30, 1962, the Division', 'counsel.'), ('The above figures', 'resulting')]),
 'fl_exodus':  (D7, 62, 0.06, 0.70, 0.06, 0.94, [('as many as', 'exodus')]),
 'op_syl':     ('us398.jpg', 0, 0.05, 0.98, 0.06, 0.94, [('No. 155.', '1963.'), ('Held:', 'overruled.')]),
 'op_fortas':  ('us398.jpg', 0, 0.40, 0.98, 0.06, 0.94, [('Abe Fortas,', 'petitioner.'), ('Bruce R. Jacob,', 'respondent.')]),
 'op_coll':    ('us400.jpg', 0, 0.05, 0.75, 0.06, 0.94, [('The DEFENDANT:', 'Counsel.')]),
 'op_trial':   ('us400.jpg', 0, 0.30, 0.98, 0.06, 0.94, [('Put to trial', 'layman.'), ('The jury returned', 'state prison.')]),
 'op_q':       ('us401.jpg', 0, 0.05, 0.75, 0.06, 0.94, [('“Should', 'reconsidered')]),
 'op_betts':   ('us401.jpg', 0, 0.20, 0.98, 0.06, 0.94, [('Betts was indicted', 'Maryland state court.'), ('He was found guilty', 'eight years in prison.')]),
 'op_overrule':('us402.jpg', 0, 0.30, 0.98, 0.06, 0.94, [('Upon', 'overruled.')]),
 'op_truth':   ('us407.jpg', 0, 0.05, 0.98, 0.06, 0.94, [('any person haled', 'obvious truth.'), ('lawyers in criminal', 'luxuries.')]),
 'op_powell': ('us408.jpg', 0, 0.05, 0.70, 0.06, 0.94, [('Even the intelligent', 'perfect one.')]),
 'op_agree':   ('us408.jpg', 0, 0.05, 0.98, 0.06, 0.94, [('Twenty-two', 'We agree.'), ('The judgment', 'Reversed.')]),
}
def autocrop(path):
    im = Image.open(path).convert('L')
    if not path.endswith('.jpg'): return im
    # US Reports scans: drop black borders
    w, h = im.size; px = im.load()
    def colbright(x): return sum(px[x, y] for y in range(h // 4, 3 * h // 4, 20)) / len(range(h // 4, 3 * h // 4, 20))
    x0 = next(x for x in range(0, w // 3, 4) if colbright(x) > 180); x1 = next(x for x in range(w - 1, 2 * w // 3, -4) if colbright(x) > 180)
    return im.crop((x0 + 20, 0, x1 - 20, h))
hl = {}
if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for name, (src, page, y0, y1, x0, x1, phrases) in jobs.items():
        p = raster(src, page)
        im = autocrop(p)
        if src.endswith('.jpg'):
            cp = f'{HI}/{name}-page.png'; im.save(cp); p = cp
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
