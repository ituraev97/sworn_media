"""SWORN 009 — rasterized U.S. government documents for the Ponzi 50+ ranking. Crops exclude agency seals.
Sources (all public domain):
  Petters  D. Minn. 0:08-cr-00364 (RECAP gov.uscourts.mnd.103973): Dkt 26 criminal complaint + FBI affidavit; Dkt 388 gov't sentencing position; Dkt 400 judgment;
           USAO D. Minn. release Apr 8, 2010 (justice.gov/sites/default/files/usao-mn/legacy/2010/12/21/econ0413.pdf) — seal cropped out.
  Okun     E.D. Va. 3:08-cr-00132 (RECAP gov.uscourts.vaed.227739): Dkt 324 memorandum opinion (Judge Payne, Aug 27, 2009);
           USAO E.D. Va. release Nov 17, 2011 (justice.gov/archive/usao/vae/news/2011/11/20111117okunnr.html) — rendered text only, no images.
  Rothstein USAO S.D. Fla. releases Jan 27, 2010 and Jun 9, 2010 (justice.gov/archive/usao/fls/PressReleases/2010/100127-01.html, 100609-01.html) — rendered text only.
  Stanford, Madoff: images reused from episodes 004 and 001 (see their sources).
Writes img/<name>.jpg and hl.json {name: [[y0,y1],...]} (fractions of the crop)."""
import subprocess, os, json, csv, io, re, shutil
from PIL import Image
HI = '/home/claude/research/hi'
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, 'img')
def norm(t): return re.sub(r'[^a-z0-9]', '', t.lower())
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
    raise SystemExit(f'not found in {path}: {start!r} … {end!r}\n' + ' '.join(toks)[:3000])
# name: (image, y0, y1, x0, x1, [(start, end)])
jobs = {
 'rr_head':  ('100609-01.png', 0.0, 0.24, 0.0, 1.0, [('FORT LAUDERDALE ATTORNEY', 'PONZI SCHEME'), ('Cohn sentenced Rothstein', 'in prison,')]),
 'rr_never': ('100609-01.png', 0.30, 0.47, 0.0, 1.0, [('In both instances,', 'earlier investors.')]),
 'rr_order': ('100609-01.png', 0.50, 0.67, 0.0, 1.0, [('created a false federal court order,', 'U.S. District Judge,'), ('approximately $57 million', 'the bonds.')]),
 'pet_cw':   ('pet26-3.png', 0.03, 0.97, 0.04, 0.96, [('A Cooperating Witness', 'the fraud scheme.'), ('The purchase orders and other', 'entirely fabricated.')]),
 'pet_wm':   ('pet26-5.png', 0.03, 0.62, 0.04, 0.96, [('The Wal-Mart official reported', 'was fictitious.')]),
 'pet_rec':  ('pet26-6.png', 0.25, 0.97, 0.04, 0.96, [('PETTERS repeatedly admits', 'to investors.'), ('PETTERS talks about fleeing', 'is discovered.')]),
 'pet_pr':   ('petpr-2.png', 0.03, 0.97, 0.06, 0.94, [('Within the first few hours', 'so long.”')]),
 'pet_flow': ('petpr-4.png', 0.03, 0.60, 0.06, 0.94, [('approximately $35 billion', 'and EFBC.')]),
 'pet_gov':  ('pet388-02.png', 0.03, 0.97, 0.06, 0.94, [('maximum statutory sentence', '(335 years).')]),
 'pet_judg': ('pet400-2.png', 0.0, 0.40, 0.03, 0.97, [('total term of 600 months', '50 years.')]),
 'ok_ponzi': ('ok324-02.png', 0.03, 0.97, 0.04, 0.96, [('In sum, Okun was', 'Ponzi scheme.')]),
 'ok_rel':   ('20111117okunnr.png', 0.0, 0.30, 0.0, 1.0, [('Fourth Circuit Upholds', 'Okun Case')]),
 'ok_126':   ('20111117okunnr.png', 0.56, 0.80, 0.0, 1.0, [('misappropriated approximately $126 million', 'client funds')]),
 'ok_cash':  ('20111117okunnr.png', 0.74, 0.96, 0.0, 1.0, [('$15,000 in cash', 'reporting requirements.')]),
}
REUSE = {'st_sent': ('../004-stanford/img/pr_sent.jpg', '../004-stanford/hl.json', 'pr_sent'),
         'st_tier': ('../004-stanford/img/brief_tier.jpg', '../004-stanford/hl.json', 'brief_tier'),
         'st_cmp': ('../004-stanford/img/cmp_cover.jpg', '../004-stanford/hl.json', 'cmp_cover'),
         'md_lie': ('../001-madoff/img/arrest2.jpg', None, [[0.45, 0.84]]),
         'md_sent': ('../001-madoff/img/sentence.jpg', None, [[0.74, 1.0]])}
if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    if not os.path.exists(f'{HI}/pet388-02.png'):
        subprocess.run(['pdftoppm', '-r', '220', '-png', '-gray', '-f', '2', '-l', '2', '/home/claude/src/pet388.pdf', f'{HI}/pet388'], check=True)
    hl = {}
    for name, (img, y0, y1, x0, x1, phrases) in jobs.items():
        p = f'{HI}/{img}'
        im = Image.open(p).convert('L')
        boxes = [find(p, s, e) for s, e in phrases]
        for r in boxes:
            if not (y0 <= r[0] and r[1] <= y1): raise SystemExit(f'phrase outside crop: {name} {r}')
        W, H = im.size
        c = im.crop((int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H))).convert('RGB')
        if img.endswith('.png') and not img.startswith(('pet', 'ok', 'petpr')):  # rendered web pages: add margin
            m = Image.new('RGB', (c.width + 120, c.height + 40), 'white'); m.paste(c, (60, 20)); c = m
            boxes = [((a - y0) * H + 20, (b - y0) * H + 20) for a, b in boxes]; ch = c.height
            hl[name] = [[round(a / ch - 0.006, 4), round(b / ch + 0.006, 4)] for a, b in boxes]
        else:
            hl[name] = [[round((a - y0) / (y1 - y0) - 0.008, 4), round((b - y0) / (y1 - y0) + 0.008, 4)] for a, b in boxes]
        c = c.resize((1480, int(c.height * 1480 / c.width)), Image.LANCZOS)
        c.save(f'{OUT}/{name}.jpg', quality=88)
        print(name, c.size, hl[name])
    for name, (src, hj, key) in REUSE.items():
        shutil.copy(os.path.join(HERE, src), f'{OUT}/{name}.jpg')
        hl[name] = json.load(open(os.path.join(HERE, hj)))[key] if hj else key
    json.dump(hl, open(os.path.join(HERE, 'hl.json'), 'w'), indent=1)
