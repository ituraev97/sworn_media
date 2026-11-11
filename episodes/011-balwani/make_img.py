"""Rasterize public-domain U.S. court / DOJ / SEC documents for SWORN 011 (Ramesh "Sunny" Balwani, Theranos), crop, compute gold-highlight boxes (tesseract TSV).
Sources (RECAP mirror on archive.org; all U.S. court records or U.S. government filings):
  ca9  = U.S. v. Holmes / U.S. v. Balwani, 9th Cir. Nos. 22-10312, 22-10338 et al., Order and Amended Opinion (Dec 22, 2025),
         filed in the district court as ECF No. 1802, archive.org gov.uscourts.cand.327949            [court opinion — shown]
  tsi  = Third Superseding Indictment, U.S. v. Holmes & Balwani, No. 5:18-cr-00258 (N.D. Cal., Jul 28, 2020), ECF No. 469 [shown]
  ind  = Indictment (grand jury, Jun 14, 2018), ECF No. 1                                               [shown]
  memo = United States' Sentencing Memorandum re Holmes (Nov 11, 2022), ECF No. 1643 (DOJ filing)       [shown]
  fix  = United States' Administrative Motion to Correct Judgments (filed Mar 26, 2026), ECF No. 1811 (DOJ filing; page 1 court stamp NOT shown) [shown p.3]
  sec  = Complaint, SEC v. Ramesh "Sunny" Balwani, No. 5:18-cv-01603 (N.D. Cal., Mar 14, 2018), ECF No. 1, archive.org gov.uscourts.cand.323856 [SEC filing — shown]
  Defense filings, trial transcripts, private exhibits: NOT shown.
Writes img/<name>.jpg and hl.json {name: [[y0,y1],...]}."""
import subprocess, os, json, csv, io, re
from PIL import Image
S = '/home/claude/docs'; HI = '/home/claude/hi'
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, 'img')
def norm(t): return re.sub(r'[^a-z0-9]', '', t.lower())
def raster(src, page):
    base = f'{HI}/{src}-{page}'
    if not os.path.exists(base + '.png'):
        subprocess.run(['pdftoppm', '-r', '220', '-png', '-singlefile', '-gray', '-f', str(page), '-l', str(page), f'{S}/{src}.pdf', base], check=True)
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
    raise SystemExit(f'not found in {path}: {start!r} … {end!r}\n' + ' '.join(toks)[:3000])
# name: (src, page, y0, y1, x0, x1, [(start, end)])
F = (0.03, 0.97, 0.04, 0.96)
jobs = {
 'ca9_drop':   ('ca9', 8, *F, [('“[O]ne tiny drop changes everything.”', 'everything.”'), ('But the vision sold by Holmes and Balwani', 'outright lies.')]),
 'ca9_role':   ('ca9', 9, *F, [('Balwani, who was in a romantic', 'Chief Operating Officer.'), ('Balwani oversaw', 'patient-testing lab')]),
 'ca9_null':   ('ca9', 13, *F, [('running a “null protocol”', 'third-party devices.'), ('In November 2013, Balwani told Holmes', 'up to $2 million weekly.')]),
 'ca9_pat':    ('ca9', 15, *F, [('One patient testified that an', 'in fact negative.'), ('The evidence linked Balwani', 'in Arizona.')]),
 'ca9_all':    ('ca9', 16, 0.40, 0.97, 0.04, 0.96, [('The jury convicted Balwani of all counts', '(Counts 9–12).')]),
 'ca9_155':    ('ca9', 17, *F, [('the same sentencing range of 135 to 168 months.', '2023 WL 2065045'), ('The district court sentenced him to 155 months', 'imprisonment.'), ('jointly and severally liable for', 'Safeway and Walgreens.')]),
 'ca9_cheung': ('ca9', 28, *F, [('“if you just extrapolate out', 'system.”')]),
 'ca9_model':  ('ca9', 40, *F, [('when the government asked if he was the person', 'financial model.”'), ('admitted to owning the financial model', 'financial projections,')]),
 'ca9_cover':  ('ca9', 2, *F, [('Argued and Submitted June 11, 2024', 'Amended December 22, 2025')]),
 'sec_cover':  ('sec', 1, 0.27, 0.97, 0.04, 0.96, [('SECURITIES AND EXCHANGE COMMISSION,', 'Defendant.'), ('This case involves the fraudulent offer', 'Chief Operating Officer, Ramesh “Sunny” Balwani.')]),
 'sec_2009':   ('sec', 4, *F, [('In 2009, as Theranos was on the verge', 'that same year.')]),
 'sec_dod':    ('sec', 14, *F, [('Balwani told one potential investor in late 2013 that 75 percent', 'from the military.'), ('Theranos generated only approximately $300,000', 'DOD contracts.')]),
 'sec_proj':   ('sec', 17, *F, [('Balwani drafted the financial information', 'revenues in 2015.')]),
 'sec_real':   ('sec', 18, *F, [('Theranos recorded little more than $100,000', 'end of 2014.'), ('In October 2014, the same month', '$9 million monthly net loss.')]),
 'tsi_tests':  ('tsi', 8, *F, [('but not limited to bicarbonate', 'vitamin B-12.'), ('used interstate electronic wires to purchase advertisements', 'California and Arizona.')]),
 'tsi_c12':    ('tsi', 11, *F, [('COUNTS NINE THROUGH TWELVE', '(Wire Fraud)'), ('8/3/2015', 'Wellness Centers')]),
 'ind_cover':  ('ind', 1, 0.03, 0.47, 0.04, 0.96, [('ELIZABETH A. HOLMES', 'BALWANI,')]),
 'memo_lab':   ('memo', 28, *F, [('In late May 2014, Dr. Rosendorff halted all testing', 'passed along'), ('In August of that year, Dr. Rosendorff emailed Balwani', 'forwarded that notice to Holmes.')]),
 'memo_zone':  ('memo', 29, *F, [('Balwani emailed Holmes complaining, “Always', 'after the fact.”'), ('with Balwani texting Holmes that the Normandy lab', 'disaster zone.”'), ('Ultimately, they had to void every single Edison test', 'possible patient impact.')]),
 'fix_dates':  ('fix', 3, *F, [('On July 7, 2022, a jury found Defendant Ramesh Balwani', 'Indictment. ECF No. 1507.'), ('On December 7, 2022, the Court imposed sentence on Defendant Balwani.', 'a $25,000 fine.')]),
}
# Private individuals (investors, private witnesses) are never named on screen: black bars over their names.
PRIVATE = re.compile(r"^(peterson|grossman|mosley|eisenman|tolbert|bb|et|me)$")
RAWOK = {'me'}  # the word "me" is only redacted when written as initials (M.E.)
def redact(path, c, ox, oy):
    from PIL import ImageDraw
    tsv = path + '.tsv'
    if not os.path.exists(tsv):
        open(tsv, 'w').write(subprocess.run(['tesseract', path, '-', 'tsv'], capture_output=True, text=True).stdout)
    d = ImageDraw.Draw(c)
    for r in csv.DictReader(io.StringIO(open(tsv).read()), delimiter='\t', quoting=csv.QUOTE_NONE):
        raw = re.sub(r"(’s|'s)$", '', (r['text'] or '').strip())
        t = re.sub(r'[^a-z]', '', raw.lower())
        if t in ('bb', 'et', 'me') and not re.match(r'^[A-Z]\.[A-Z]\.?,?$', raw): continue
        if t and PRIVATE.match(t):
            l, tp, w, h = (int(r[k]) for k in ('left', 'top', 'width', 'height'))
            d.rectangle([l - ox - 4, tp - oy - 3, l - ox + w + 4, tp - oy + h + 3], fill=(11, 16, 32))
hl = {}
if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for name, (src, page, y0, y1, x0, x1, phrases) in jobs.items():
        p = raster(src, page)
        im = Image.open(p).convert('L')
        boxes = [find(p, s, e) for s, e in phrases]
        for r in boxes:
            if not (y0 <= r[0] and r[1] <= y1): raise SystemExit(f'phrase outside crop: {name} {r}')
        W, H = im.size
        c = im.crop((int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H))).convert('RGB')
        redact(p, c, int(x0 * W), int(y0 * H))
        c = c.resize((1480, int(c.height * 1480 / c.width)), Image.LANCZOS)
        c.save(f'{OUT}/{name}.jpg', quality=88)
        hl[name] = [[round((a - y0) / (y1 - y0) - 0.008, 4), round((b - y0) / (y1 - y0) + 0.008, 4)] for a, b in boxes]
        print(name, c.size, hl[name])
    json.dump(hl, open(os.path.join(HERE, 'hl.json'), 'w'), indent=1)
