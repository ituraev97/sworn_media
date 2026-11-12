"""Rasterize public-domain U.S. government documents for SWORN 012 (Kelly v. United States, "Bridgegate"), crop, compute gold-highlight boxes (tesseract TSV).
Sources:
  usb  = Brief for the United States (respondent), Kelly v. United States, No. 18-1059 (U.S. Nov 22, 2019) — DOJ / Solicitor General filing
         archive.org 6562201-Brief-of-respondent-United-States-filed                                   [shown]
  ja   = Joint Appendix Vol. II, Kelly v. United States, No. 18-1059 — only court-authored pages are shown:
         final jury instructions (JA 863) and Jury Communication #4 with the court's response (JA 905).
         Trial/sentencing transcripts and trial exhibits (e-mails, texts) are NOT shown — quoted only.
  crs1 = Congressional Research Service, Legal Sidebar LSB10326 "High Court Tosses Bridgegate Convictions" (May 8, 2020) [shown, logo cropped]
  crs2 = Congressional Research Service, Legal Sidebar LSB11025 "Public Corruption and the Limits of Federal Fraud Statutes" (Jan 9, 2026) [shown, logo cropped]
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
 'usb_cover': ('usb', 1, 0.03, 0.62, 0.04, 0.96, [('BRIDGET ANNE KELLY, PETITIONER', 'UNITED STATES OF AMERICA'), ('BRIEF FOR THE UNITED STATES', 'UNITED STATES')]),
 'usb_stmt':  ('usb', 8, *F, [('each convicted on one count of conspiracy', 'wire fraud, in violation of 18 U.S.C. 1349;'), ('The district court sentenced Kelly to 18 months', 'Baroni to 24 months'), ('The district court resentenced Kelly to 13 months', 'Baroni to 18 months'), ('Kelly is the former Deputy Chief of Staff', 'New York and New Jersey.')]),
 'usb_bridge':('usb', 9, *F, [('the George Washington Bridge is the busiest', 'in the world,'), ('In the late summer of 2013, Kelly and Baroni', 'in Fort Lee.')]),
 'usb_lie':   ('usb', 10, *F, [('namely, that Kelly wanted to punish', 'for reelection.'), ('Instead, Baroni and Kelly', 'the traffic patterns.”'), ('study, however, was a “sham.”', 'there was no study.”')]),
 'usb_toll':  ('usb', 12, *F, [('And because only one lane from Fort Lee', 'in that lane.'), ('Indeed, they “joked about”', 'go to the bathroom.”'), ('scheme on Monday, September', 'Pet. App. 8a.')]),
 'usb_grid':  ('usb', 13, *F, [('As the conspirators had intended, the result was', 'J.A. 107.'), ('The Fort Lee Chief of Police would later testify', 'except for 9/11,”'), ('First responders were impeded', '“cardiac arrest.”')]),
 'usb_smile': ('usb', 14, *F, [('Kelly responded “Is it wrong that I’m smiling?”', 'J.A. 753.'), ('The traffic jams continued for four days.', 'Pet. App. 10a-11a.')]),
 'usb_cost':  ('usb', 24, *F, [('The court observed that the fraudulent scheme', 'total cost of $3,696.09).')]),
 'usb_14':    ('usb', 26, *F, [('fourteen Port Authority employees to do sham work', 'Port Authority aim.”'), ('“That Defendants were politically motivated,”', 'federal criminal law.”'), ('the labor of fourteen public', 'three professional staff members,”')]),
 'usb_soa':   ('usb', 27, *F, [('The court of appeals correctly determined that Kelly', 'they could not')]),
 'ja_motive': ('ja', 363, *F, [('Motive is not an element', 'is charged.'), ('Proof of bad motive is not required', 'to convict.')]),
 'ja_q4':     ('ja', 405, 0.03, 0.80, 0.04, 0.96, [('Can you be guilty of Conspiracy', 'Mayor Sokolich.'), ('Yes. Please consider this', 'given to you.')]),
 'crs1_top':  ('crs1', 1, 0.20, 0.62, 0.04, 0.96, [('On May 7, 2020, a unanimous Supreme Court threw out', 'leading to gridlock.')]),
 'crs1_pet':  ('crs1', 3, *F, [('Her petition argued that', 'conflicting with announced reasons.'), ('Its opinion is', 'every public official in the nation.”')]),
 'crs2_lim':  ('crs2', 1, 0.20, 0.80, 0.04, 0.96, [('This trend continued in two cases', 'Kousisis v.')]),
}
# Private individuals (investors, private witnesses) are never named on screen: black bars over their names.
PRIVATE = re.compile(r"^(zzzznone)$")
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
