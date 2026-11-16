"""SWORN 016 — United States v. Earnest et al. / United States v. Rozier, E.D.N.Y. 25-cr-323 (LDH).
Documents shown (all U.S. government works: grand-jury indictments and DOJ filings, public domain), from the
RECAP mirror on archive.org (gov.uscourts.nyed.537695 / 537701), rasterized with pdftoppm -r 220:
  ind  = ECF 17   Indictment (returned Oct 16, 2025; unsealed Oct 23, 2025)           text layer -> pdftotext -bbox
  sup  = ECF 101  Superseding Indictment (filed May 28, 2026)                         scanned -> tesseract TSV
  g144 = ECF 144  Gov't opposition to Rozier's motion to dismiss the superseding indictment (Aug 26, 2026)
  g166 = ECF 166  Gov't letter opposing severance (Nov 3, 2026) — DOJ letterhead/seal cropped off the top
Defense filings (ECF 124/128/169) are quoted only, never shown.
Face: Wikimedia Commons "Terry Rozier (33650529273).jpg", Keith Allison, CC BY-SA 2.0 (cropped to Rozier).
Writes img/<name>.jpg and hl.json ([top, bottom] fractions of each crop for each phrase)."""
import subprocess, os, json, re, csv, io, html
from PIL import Image, ImageFilter
D = '/home/claude/dl16'; HI = '/home/claude/hi16'
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, 'img')
def norm(t): return re.sub(r'[^a-z0-9]', '', t.lower())
# name: (pdf, page, scanned, crop_top_frac, crop_bottom_frac, phrases)
P = {
 'ind_1':  ('ind', 1, False, 0.0, 0.75, [('TERRY ROZIER', 'Chum')]),
 'ind_8':  ('ind', 8, False, 0.0, 1.0, [('informed the defendant DENIRO LASTER', 'information to')]),
 'ind_9':  ('ind', 9, False, 0.0, 1.0, [('ROZIER was not on the Hornets', 'exit the March 23 Game'),
                                        ('agreed to pay LASTER approximately', 'gambling winnings.')]),
 'ind_12': ('ind', 12, False, 0.0, 1.0, [('removed himself from the game in the first quarter', 'per game.'),
                                         ('ROZIER scored five points', 'in the March 23 Game.'),
                                         ('ROZIER collected four rebounds', 'rebounds in the March 23 Game.'),
                                         ('ROZIER arranged and paid for', 'travel to Philadelphia.')]),
 'ind_10': ('ind', 10, False, 0.0, 1.0, [('Company 3 totaling approximately', 'ROZIER\'s unders.'),
                                         ('Co-Conspirator 2 placed multiple', 'approximately $107,000.')]),
 'sup_8':  ('sup', 8, True, 0.0, 1.0, [('engaged in a scheme to defraud the Charlotte Hornets', 'anticipated underperformance.')]),
 'sup_9':  ('sup', 9, True, 0.0, 1.0, [('suffered a lower leg injury', 'during an upcoming game.'),
                                       ('In exchange for an approximately', 'portion of the bribe.'),
                                       ('using encrypted applications', 'grew closer.')]),
 'sup_13': ('sup', 13, True, 0.0, 1.0, [('Not all of the bets', 'approximately $70,000.'),
                                        ('ROZIER arranged and paid for', 'flight to Philadelphia.')]),
 'sup_14': ('sup', 14, True, 0.0, 1.0, [('During the early morning hours of April 1', 'from Fairley in Philadelphia.')]),
 'g144_6': ('g144', 6, False, 0.0, 1.0, [('For taking a bribe in exchange', 'his underperformance,'),
                                         ('After developing additional evidence', 'Counts Three and Four.')]),
 'g144_7': ('g144', 7, False, 0.0, 1.0, [('he solicited an approximately', 'to do so.'),
                                         ('Rozier removed himself during the first quarter', 'lost the game.'),
                                         ('Rozier collected four rebounds', 'approximately $70,000.')]),
 'g144_8': ('g144', 8, False, 0.0, 1.0, [('drove hundreds of miles through the', 'counting the cash.'),
                                         ('Dont [sic] tell Chum bout the bet', 'relate to sports gambling.')]),
 'g166_1': ('g166', 1, False, 0.17, 1.0, [('defense theory', 'predetermined plan'),
                                           ('trial for both defendants should commence', 'as scheduled.')]),
 'g166_2': ('g166', 2, False, 0.0, 1.0, [('defense is simple', 'about any bets.')]),
}
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
    for i in range(len(toks)):
        if toks[i:i + len(s)] == s:
            for j in range(i, min(len(toks), i + 400)):
                if toks[j:j + len(e)] == e:
                    seg = ws[i:j + len(e)]
                    return min(w[1] for w in seg), max(w[3] for w in seg)
    raise SystemExit(f'not found: {start!r} … {end!r}\n' + ' '.join(toks)[:3000])
if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True); os.makedirs(HI, exist_ok=True); hl = {}
    for name, (pdf, page, scanned, ct, cb, phrases) in P.items():
        base = f'{HI}/{pdf}_{page}'
        if not os.path.exists(base + '.png'):
            subprocess.run(['pdftoppm', '-r', '220', '-gray', '-png', '-singlefile', '-f', str(page), '-l', str(page), f'{D}/{pdf}.pdf', base], check=True)
        ws = words_ocr(base + '.png') if scanned else words_text(f'{D}/{pdf}.pdf', page)
        im = Image.open(base + '.png').convert('RGB'); W, H = im.size
        body = [w for w in ws if w[1] >= ct]
        top = max(ct, min(w[1] for w in body) - 0.02); bot = min(cb, max(w[3] for w in body) + 0.02)
        c = im.crop((int(0.06 * W), int(top * H), int(0.94 * W), int(bot * H)))
        c = c.resize((1480, int(c.height * 1480 / c.width)), Image.LANCZOS)
        c.save(f'{OUT}/{name}.jpg', quality=88)
        hl[name] = [[round((a - top) / (bot - top) - 0.004, 4), round((b - top) / (bot - top) + 0.004, 4)] for a, b in (find(ws, s, e) for s, e in phrases)]
        print(name, c.size, hl[name])
    json.dump(hl, open(os.path.join(HERE, 'hl.json'), 'w'), indent=1)
    # face (Commons, CC BY-SA 2.0, Keith Allison): crop Rozier only (the other player and the rim are cut out)
    src = '/home/claude/dl16/rozier_commons.jpg'
    if os.path.exists(src):
        im = Image.open(src).convert('RGB'); W, H = im.size
        box = [float(x) for x in open('/home/claude/dl16/face_box.txt').read().split()]  # fractions x0 y0 x1 y1
        f = im.crop((int(box[0] * W), int(box[1] * H), int(box[2] * W), int(box[3] * H)))
        if f.width < 900:
            f = f.resize((900, int(f.height * 900 / f.width)), Image.LANCZOS).filter(ImageFilter.UnsharpMask(radius=3, percent=50, threshold=2))
        f.save(f'{OUT}/rozier_face.jpg', quality=92); print('rozier_face', f.size)
