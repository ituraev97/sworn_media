"""Rasterize public-domain U.S. court / DOJ documents for SWORN 010 (Martin Shkreli), crop, and compute gold-highlight boxes (tesseract TSV).
Sources (RECAP mirror on archive.org; all U.S. court records or U.S. government filings):
  nyed*  = United States v. Shkreli, No. 1:15-cr-00637 (E.D.N.Y.), archive.org gov.uscourts.nyed.379142
     1   Indictment (grand jury, Dec 2015)                         [shown]
     305 Jury verdict sheet (redacted, Aug 4, 2017)                [shown]
     362 Government letter motion to revoke bail (Sep 7, 2017)     [DOJ — shown, seal cropped out]
     535 Memorandum & Order denying Rule 29 motion (Feb 26, 2018)  [court opinion — shown]
     540 Preliminary Order of Forfeiture (Mar 5, 2018)             [court order — shown]
     561 Government sentencing submission (Mar 2018)               [DOJ — shown]
     566 Judgment (Mar 2018)                                       [court — shown]
     716 Second Circuit mandate / summary order (Aug 2019)         [court — shown]
     734 Memorandum & Order denying compassionate release (May 2020) [court — shown]
  nysd865 = FTC et al. v. Vyera Pharmaceuticals et al., No. 1:20-cv-00706 (S.D.N.Y.), Opinion & Order (Jan 14, 2022),
            archive.org gov.uscourts.nysd.530855                    [court opinion — shown]
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
 'ftc_open':  ('nysd865', 6, *F, [('In 2015, Martin Shkreli', 'by 4,000%'), ('Shkreli and his companies profited', 'this scheme.')]),
 'ftc_ban':   ('nysd865', 7, *F, [('for life from participating', 'his wrongdoing.')]),
 'ftc_fn9':   ('nysd865', 13, *F, [('serving a sentence on an unrelated', 'conviction.'), ('Shkreli was arrested in', 'seven years).')]),
 'ftc_turing':('nysd865', 27, *F, [('Shkreli highlighted to early Turing', 'pricing power.”'), ('Shkreli remained CEO of Turing', 'Retrophin.')]),
 'ftc_price': ('nysd865', 32, *F, [('raised the WAC from', 'August'), ('poster child', 'industry.”')]),
 'ftc_vol':   ('nysd865', 33, *F, [('Daraprim’s sales volume dropped by 66%.', 'by 66%.'), ('From 2016 through 2019, Vyera made', 'sales of Daraprim.')]),
 'ftc_call':  ('nysd865', 40, *F, [('On August 8, 2019, while incarcerated', 'carefully,'), ('“there has to be some way', 'supply chain a bit')]),
 'ftc_end':   ('nysd865', 134, *F, [('An injunction shall issue', 'any capacity.')]),
 'r29_verd':  ('nyed535', 6, *F, [('The jury returned its verdict', 'deliberations.'), ('Mr. Shkreli was', 'Seven.')]),
 'r29_aum':   ('nyed535', 14, *F, [('“had approximately $35 million under management”', 'year-to-date”.'), ('“returned', 'inception”.')]),
 'r29_orex':  ('nyed535', 16, *F, [('Merrill Lynch had to buy', 'over $7 million.')]),
 'r29_rep':   ('nyed535', 18, *F, [('the April 10, 2011 performance report', '$1,324,905.'), ('claimed to have', 'Columbia.”')]),
 'r29_col':   ('nyed535', 58, *F, [('had never', 'Columbia University.”'), ('The defendant stipulated', 'MSMB Capital.')]),
 'r29_113':   ('nyed535', 59, *F, [('The fund, however, never', 'total investments.')]),
 'r29_lost':  ('nyed535', 61, *F, [('had in fact lost almost all', 'Therapeutics.'), ('continued to provide his investors', 'returns.')]),
 'ind_cover': ('nyed1', 1, *F, [('UNITED STATES OF AMERICA', 'Defendants.')]),
 'ind_35':    ('nyed1', 5, *F, [('SHKRELI told Investor', 'respectively.'), ('In fact, as of November 30, 2010', '$700.')]),
 'verdict':   ('nyed305', 2, *F, [('AS TO COUNT SIX', 'Guilty')]),
 'bail':      ('nyed362', 1, 0.15, 0.97, 0.04, 0.96, [('Most recently, Shkreli threatened', 'book tour.')]),
 'sm_core':   ('nyed561', 3, *F, [('no less than 180', 'months.'), ('At its core, this case is about', 'trusted him.')]),
 'judg':      ('nyed566', 1, *F, [('was found guilty on count(s)', 'superseding indictment'), ('has been found not guilty', 'indictment.')]),
 'judg2':     ('nyed566', 2, *F, [('Eighty-four months, with credit', 'concurrently.')]),
 'forf':      ('nyed540', 2, *F, [('Seven Million', '($7,360,450.00)')]),
 'forf3':     ('nyed540', 3, *F, [('the album', 'Wu Tang Clan;'), ('a Picasso', 'painting.')]),
 'mandate':   ('nyed716', 2, *F, [('IT IS HEREBY ORDERED', 'AFFIRMED.')]),
 'covid':     ('nyed734', 8, *F, [('pharmaceuticals to help develop', 'COVID-19'), ('“delusional', 'convicted.')]),
}
# Private individuals (investors, private witnesses) are never named on screen: black bars over their names.
PRIVATE = re.compile(r"^(blanton|darren|hassan|sarah|rosenwald|lindsay|richardson|neill|marshall|schuyler|austin|josiah|stewart|caroline|dynagrow|yaffe|stitch|tillman|ward|kane|barry|fearnow|biestek|mulleady|kevin|stevens?)$")
def redact(path, c, ox, oy):
    from PIL import ImageDraw
    tsv = path + '.tsv'
    if not os.path.exists(tsv):
        open(tsv, 'w').write(subprocess.run(['tesseract', path, '-', 'tsv'], capture_output=True, text=True).stdout)
    d = ImageDraw.Draw(c)
    for r in csv.DictReader(io.StringIO(open(tsv).read()), delimiter='\t', quoting=csv.QUOTE_NONE):
        t = re.sub(r"(’s|'s)$", '', (r['text'] or '').strip()).lower()
        t = re.sub(r'[^a-z]', '', t)
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
