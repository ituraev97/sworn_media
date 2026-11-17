"""SWORN 017 — United States v. Jordan Ross Belfort, E.D.N.Y. CR-98-0859 (restitution collection, 2017–2022).
Documents shown (all U.S. government works — DOJ filings — public domain), from the RECAP mirror on archive.org,
rasterized with pdftoppm -r 220:
  mtc  = Motion to Compel Non-Party Witnesses to Comply With Subpoenas, filed by the U.S. in D. Nev. 3:18-ms-00001
         (Mar 29, 2018), transferred to E.D.N.Y. 1:18-cv-03016, ECF 1 (gov.uscourts.nyed.417522)   scanned -> tesseract TSV
  gil  = Declaration of William Gilsen (forensic accountant, USAO EDNY), D. Nev. 3:18-cv-00139 ECF 4-1 (Mar 31, 2018)
         (gov.uscourts.nvd.129776)                                                                  text layer
  las  = Declaration of AUSA Peter A. Laserna, E.D.N.Y. 1:18-mc-01033 ECF 1-1 (Mar 27, 2018) (gov.uscourts.nyed.415574)
  l9   = USAO EDNY letter to Judge Donnelly, May 23, 2018, 1:18-cv-03016 ECF 9                    DOJ seal painted out
  l12  = USAO EDNY letter to Judge Kovner, Apr 8, 2022, 1:18-mc-01033 ECF 12                       DOJ seal painted out
  l16  = USAO EDNY letter to Judge Kovner, Oct 15, 2021, 1:18-cv-03016 ECF 16                      DOJ seal painted out
  cald = DOJ Office of Public Affairs, remarks of AAG Leslie R. Caldwell, July 20, 2016 (justice.gov), re-typeset as
         text only by txt2pdf.js (no seal/logo/images).
Private individuals named in the filings (Belfort's business partner, his children, the bookkeeper) are covered with
black bars on every image. Exhibits (QuickBooks printouts, deposition transcripts) are never shown.
Face: Wikimedia Commons "JordanBelfort2017.png", Tai Lopez, CC BY 3.0 (frame from a 2017 YouTube interview).
Writes img/<name>.jpg and hl.json ([top, bottom] fractions of each crop for each phrase)."""
import subprocess, os, json, re, csv, io, html
from PIL import Image, ImageDraw, ImageFilter
D = '/home/claude/dl17'; HI = '/home/claude/hi17'
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, 'img')
def norm(t): return re.sub(r'[^a-z0-9]', '', t.lower())
REDACT = {'koppe', 'anne', 'chandler', 'carter', 'grebe', 'marc', 'mark', 'koppes'}
# name: (pdf, page, scanned, crop_top_frac, crop_bottom_frac, seal, redact, phrases)
P = {
 'mtc_1': ('mtc', 1, True, 0.0, 0.95, False, False, [('UNITED STATES OF AMERICA, Misc.', 'Subpoenas'), ('Movant, the United States', 'served upon them.')]),
 'mtc_2': ('mtc', 2, True, 0.0, 1.0, False, False, [('As part of his conviction', '135 in CR-98-0859'),
                                                    ('In November 2017, the government', 'JB Global, Inc.'),
                                                    ('The non- party witnesses failed to produce', 'December 1, 2017.')]),
 'mtc_6': ('mtc', 6, True, 0.0, 1.0, False, True, [('investigation of the defendant because', 'Gilsen Decl. at'),
                                                   ('The financial investigation further indicated', 'respectively.'),
                                                   ('At least a portion', 'restitution liability.'),
                                                   ('The United States has initiated garnishment', 'nominee')]),
 'mtc_7': ('mtc', 7, True, 0.0, 0.55, False, False, [('The United States has substantial cause', 'principals.'),
                                                    ('millions of dollars’ worth', 'see id. at')]),
 'gil_1': ('gil', 1, False, 0.0, 1.0, False, True, [('I am a forensic accountant', 'Civil Division.'),
                                                   ('personal expenditures incurred by Jordan', 'by the company.'),
                                                   ('As of August 5, 2017', '9,188,876.06'),
                                                   ('I have not found any', 'reimburse the')]),
 'gil_2': ('gil', 2, False, 0.0, 1.0, False, True, [('Belfort was asked if he signed', 'Not to my knowledge.'),
                                                   ('together, Belfort and', 'respectively.'),
                                                   ('reported income from the aforementioned', 'for 2015.'),
                                                   ('were not reported as income', 'accounting principles.')]),
 'las_3': ('las', 3, False, 0.0, 1.0, False, False, [('The non-party witnesses’ deadline', 'in any manner.'),
                                                    ('As of the signing of this Declaration, the non-party witnesses have not responded to my December', 'letter.')]),
 'l9_2':  ('l9', 2, False, 0.0, 0.75, False, False, [('The non-party respondents have failed to fully comply', 'best efforts to be cooperative.'),
                                                    ('The non-party respondents’ delay', 'seemingly willful.')]),
 'l12_1': ('l12', 1, False, 0.0, 0.92, True, False, [('to inform the Court that the Defendant and Respondents have complied', 'subject to dismissal.'),
                                                    ('the United States respectfully requests that this case be dismissed', '41(a)(2).')]),
 'l16_1': ('l16', 1, False, 0.0, 0.9, True, False, [('there are no outstanding disputes', '41(a)(2).')]),
 'cald':  ('cald', 1, False, 0.0, 1.0, False, False, [('Remarks as prepared for delivery', 'Malaysian Sovereign Wealth Fund'),
                                                     ('That individual used the stolen funds', 'Red Granite Pictures.'),
                                                     ('Red Granite Pictures, in turn', 'The Wolf of Wall Street.'),
                                                     ('According to the allegations in the complaint, this is a case where life imitated art.', 'perceived foreign safe haven.')]),
}
# optional: crop a long page to a word range (start phrase top, end phrase bottom)
RANGE = {'cald': ('U.S. Department of Justice', 'no safe haven.')}
def words_text(pdf, page):
    xml = subprocess.run(['pdftotext', '-bbox', '-f', str(page), '-l', str(page), pdf, '-'], capture_output=True, text=True).stdout
    W, H = map(float, re.search(r'<page width="([\d.]+)" height="([\d.]+)"', xml).groups())
    ws = [(float(a) / W, float(b) / H, float(c) / W, float(d) / H, html.unescape(t)) for a, b, c, d, t in
          re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>', xml)]
    return [w for w in ws if norm(w[4])]
def words_ocr(png):
    tsv = subprocess.run(['tesseract', png, '-', 'tsv'], capture_output=True, text=True).stdout
    im = Image.open(png); W, H = im.size; ws = []
    for r in csv.DictReader(io.StringIO(tsv), delimiter='\t', quoting=csv.QUOTE_NONE):
        t = r.get('text') or ''
        if r['level'] == '5' and norm(t):
            x, y, w, h = (int(r[k]) for k in ('left', 'top', 'width', 'height'))
            ws.append((x / W, y / H, (x + w) / W, (y + h) / H, t))
    return ws
def find(ws, start, end):
    toks = [norm(w[4]) for w in ws]; s = [norm(x) for x in start.split() if norm(x)]; e = [norm(x) for x in end.split() if norm(x)]
    sj = ''.join(s); ej = ''.join(e)
    # match on the joined token stream (robust to OCR word splits / hyphenation)
    joined = ''; idx = []
    for k, t in enumerate(toks):
        idx += [k] * len(t); joined += t
    a = joined.find(sj)
    if a < 0: raise SystemExit(f'not found start: {start!r}\n' + joined[:3000])
    b = joined.find(ej, a + len(sj) - len(ej) if ej in sj else a)
    if b < 0: raise SystemExit(f'not found end: {end!r} after {start!r}')
    seg = ws[idx[a]: idx[b + len(ej) - 1] + 1]
    return min(w[1] for w in seg), max(w[3] for w in seg)
if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True); os.makedirs(HI, exist_ok=True); hl = {}
    for name, (pdf, page, scanned, ct, cb, seal, red, phrases) in P.items():
        base = f'{HI}/{pdf}_{page}'
        if not os.path.exists(base + '.png'):
            subprocess.run(['pdftoppm', '-r', '220', '-gray', '-png', '-singlefile', '-f', str(page), '-l', str(page), f'{D}/{pdf}.pdf', base], check=True)
        ws = words_ocr(base + '.png') if scanned else words_text(f'{D}/{pdf}.pdf', page)
        im = Image.open(base + '.png').convert('RGB'); W, H = im.size; dr = ImageDraw.Draw(im)
        if seal:  # DOJ seal at the top-left of the letterhead
            dr.rectangle([int(0.06 * W), int(0.02 * H), int(0.27 * W), int(0.135 * H)], fill='white')
        if red:
            for x0, y0, x1, y1, t in ws:
                if norm(t) in REDACT:
                    dr.rectangle([int(x0 * W) - 4, int(y0 * H) - 3, int(x1 * W) + 4, int(y1 * H) + 3], fill='black')
        if name in RANGE:
            ct = find(ws, *[RANGE[name][0]] * 2)[0] - 0.01; cb = find(ws, *[RANGE[name][1]] * 2)[1] + 0.012
        body = [w for w in ws if ct <= w[1] <= cb]
        top = max(0.0, max(ct, min(w[1] for w in body) - 0.02)); bot = min(1.0, cb, max(w[3] for w in body) + 0.02)
        c = im.crop((int(0.04 * W), int(top * H), int(0.96 * W), int(bot * H)))
        c = c.resize((1480, int(c.height * 1480 / c.width)), Image.LANCZOS)
        c.save(f'{OUT}/{name}.jpg', quality=88)
        hl[name] = [[round((a - top) / (bot - top) - 0.004, 4), round((b - top) / (bot - top) + 0.004, 4)] for a, b in (find(ws, s, e) for s, e in phrases)]
        print(name, c.size, hl[name])
    json.dump(hl, open(os.path.join(HERE, 'hl.json'), 'w'), indent=1)
    # face (Commons, CC BY 3.0, Tai Lopez, 2017)
    f = Image.open(f'{D}/belfort2017.png').convert('RGB')
    f.save(f'{OUT}/belfort_face.jpg', quality=92); print('belfort_face', f.size)
    # 1080x1920 hook image for Shorts: face at full width, eyes around y~430, blurred fill
    bg = f.resize((1080, 1920), Image.LANCZOS).filter(ImageFilter.GaussianBlur(30))
    fr = f.resize((1080, int(f.height * 1080 / f.width)), Image.LANCZOS)
    bg.paste(fr, (0, -60)); bg.save(f'{OUT}/belfort_hook.jpg', quality=92); print('belfort_hook', bg.size)
