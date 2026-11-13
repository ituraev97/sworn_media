"""Rasterize public-domain U.S. government documents for SWORN 013 (United States v. Trevor Milton, Nikola), crop, compute gold-highlight boxes (tesseract TSV).
Sources (RECAP mirror on archive.org; local copies in /home/claude/dl/milton):
  gm   = Government's Sentencing Memorandum, U.S. v. Milton, S1 21 Cr. 478 (ER), Dkt. 315 (Dec 12, 2023) — DOJ/USAO SDNY      [shown]
  op   = Opinion and Order denying new trial / acquittal, Dkt. 286 (Aug 30, 2023) — S.D.N.Y. (Ramos, J.)                    [shown]
  jdg  = Judgment in a Criminal Case, Dkt. 327 (Jan 17, 2024)                                                                 [shown]
  rest = Government letter seeking restitution, Dkt. 361 (Mar 14, 2025) — USAO SDNY (DOJ seal cropped)                     [shown]
  pard = Executive Grant of Clemency (pardon), Exhibit A to Dkt. 362 (filed Apr 1, 2025) — federal executive document      [shown]
  bail = Order Exonerating Defendant's Bail, Dkt. 365 (Apr 7, 2025)                                                         [shown]
  ind  = Sealed Indictment 21 Cr. 478, Dkt. 1 (Jul 28/29, 2021)                                                             [shown]
  sec  = SEC v. Milton, No. 1:21-cv-06445, Complaint, Dkt. 1 (Jul 29, 2021) — allegations                                   [shown]
  secd = SEC v. Milton, Joint Stipulation to Dismiss, Dkt. 53 (Sep 11, 2025)                                                [shown]
Not shown (quoted only): sentencing transcript Dkt. 322 (court reporter), trial exhibits, defense filings (the pardon text is shown from the government document itself).
Private persons (ranch seller, early investor) are blacked out on every image.
Writes img/<name>.jpg and hl.json {name: [[y0,y1],...]}."""
import subprocess, os, json, csv, io, re
from PIL import Image
S = '/home/claude/dl/milton'; HI = '/home/claude/hi'
FILES = {'gm': 'gov.uscourts.nysd.564175.315.0', 'op': 'gov.uscourts.nysd.564175.286.0', 'jdg': 'gov.uscourts.nysd.564175.327.0',
         'rest': 'gov.uscourts.nysd.564175.361.0', 'pard': 'gov.uscourts.nysd.564175.362.1', 'bail': 'gov.uscourts.nysd.564175.365.0',
         'ind': 'gov.uscourts.nysd.564175.1.0', 'sec': 'gov.uscourts.nysd.564121.1.0', 'secd': 'gov.uscourts.nysd.564121.53.0'}
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, 'img')
def norm(t): return re.sub(r'[^a-z0-9]', '', t.lower())
def raster(src, page):
    base = f'{HI}/{src}-{page}'
    if not os.path.exists(base + '.png'):
        subprocess.run(['pdftoppm', '-r', '220', '-png', '-singlefile', '-gray', '-f', str(page), '-l', str(page), f'{S}/{FILES[src]}.pdf', base], check=True)
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
 'gm_cover': ('gm', 1, 0.03, 0.62, 0.04, 0.96, [('TREVOR MILTON,', 'Defendant.'), ('THE GOVERNMENT’S SENTENCING MEMORANDUM', 'MEMORANDUM')]),
 'gm_pre':   ('gm', 3, *F, [('one time driving', 'for sale at'), ('Milton faces an advisory Guidelines sentence of', 'imprisonment.')]),
 'gm_6':     ('gm', 6, 0.03, 0.875, 0.04, 0.96, [('on December 1 and 2, 2016,', 'broadcast on the internet.'), ('These representations', 'missing critical parts.'), ('The infotainment screens that', 'laptop lock screens.'), ('The following year', 'rolled down a hill.')]),
 'gm_7':     ('gm', 7, *F, [('When Milton saw an initial version', 'used in the commercial.”'), ('[t]his will be the first time', 'youtube channel.”'), ('Milton then directed a Nikola employee', 'Facebook pages.'), ('rose from approximately $1.099 billion', '$7.303 billion'), ('one of [Milton’s] goal[s]', 'Nikola’s stock price.')]),
 'gm_8':     ('gm', 8, *F, [('Milton was able to sell, in May', 'approximately $100 million.'), ('By September 2020, Milton had already spent', 'Turks & Caicos.')]),
 'gm_9':     ('gm', 9, *F, [('Milton made similar misrepresentations about', 'Nikola branding.'), ('Milton claimed that Nikola was producing hydrogen', 'when it had not;'), ('Finally, Milton claimed that Nikola had firm contracts', 'That too was false.'), ('And Milton was', 'warned over and over')]),
 'gm_10':    ('gm', 10, *F, [('Ultimately,', '$8.5 million.')]),
 'gm_16':    ('gm', 16, *F, [('At those three brokerages alone', '$267.7 million.')]),
 'op_1':     ('op', 1, 0.03, 0.62, 0.04, 0.96, [('Milton proceeded to trial and was found guilty', 'with securities fraud'), ('Milton was found not guilty', 'Doc. 213.')]),
 'op_5':     ('op', 5, *F, [('The trial of this case began on September 13, 2022,', 'October 14, 2022.'), ('four big categories', 'from the ground up.”')]),
 'jdg_1':    ('jdg', 1, 0.03, 0.75, 0.04, 0.96, [('was found guilty on', 'indictment'), ('has been found not guilty on', 'Indictment')]),
 'jdg_2':    ('jdg', 2, 0.03, 0.40, 0.04, 0.96, [('The defendant is hereby committed', 'run concurrently.')]),
 'rest':     ('rest', 1, 0.115, 0.97, 0.04, 0.96, [('was sentenced to a term of forty-eight months', 'of imprisonment.'), ('to pay restitution in the amount of $660,800,000', 'shareholders of Nikola,')]),
 'pard':     ('pard', 2, 0.03, 0.97, 0.04, 0.96, [('A FULL AND UNCONDITIONAL PARDON', 'PARDON'), ('remission of', 'by the court:')]),
 'bail':     ('bail', 1, 0.03, 0.78, 0.04, 0.96, [('WHEREAS, on March 27, 2025,', 'in this action;'), ('IT IS HEREBY ORDERED', 'exonerated and released,')]),
 'ind_1':    ('ind', 1, 0.03, 0.97, 0.04, 0.96, [('From at least in or about November 2019', 'podcast interviews.')]),
 'sec_17':   ('sec', 17, *F, [('Nikola One “fully functions', 'really incredible.”')]),
 'sec_20':   ('sec', 20, *F, [('It was towed to the top of an inclined stretch', 'rolling down the incline.'), ('“Behold, the Nikola One in motion.', 'in motion.')]),
 'secd':     ('secd', 1, 0.03, 0.80, 0.04, 0.96, [('WHEREAS, in the exercise of its discretion,', 'is appropriate.')]),
}
# Private individuals (investors, private witnesses) are never named on screen: black bars over their names.
PRIVATE = re.compile(r"^(hicks|hickss|hickses|lackey|peter)$")
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
