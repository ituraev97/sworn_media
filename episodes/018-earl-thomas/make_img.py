"""SWORN 018 — United States v. Kevin J. Thompson and Nina Thomas, E.D. La. 2:24-cr-00058.
Documents shown (U.S. government works, public domain): the U.S. Attorney's Office, E.D. La. press releases
  plea = Nov 17, 2026  "New Orleans Man and Texas Woman Plead Guilty to Conspiracy to Commit Wire Fraud ..."
  ind  = Dec 23, 2024  "New Orleans Man and Texas Woman Indicted for Wire Fraud, Identity Theft, Money Laundering ..."
saved as innerText with Playwright (pw_pdf.js), re-typeset as text-only PDFs (txt2pdf.js: no seal, logo or images),
rasterized with pdftoppm -r 220. One clause about the victim's personal circumstances is blacked out (privacy).
Highlight boxes come from pdftotext -bbox. Writes img/<name>.jpg and hl.json."""
import subprocess, os, json, re
from PIL import Image, ImageDraw
D = '/home/claude/dl18/doj'; HI = '/home/claude/hi18'
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, 'img')
def norm(t): return re.sub(r'[^a-z0-9]', '', t.lower())
P = {
 'plea': [('KEVIN J. THOMPSON, age 41', 'David I. Courcelle.'), ('THOMPSON also pled', '841(b)(1)(B).'),
          ('Under the terms of a court order', 'in the other’s name.'), ('In 2021, THOMAS entered', 'by electronic wires.'),
          ('As part of their scheme, in 2022', 'signing the victim’s name.'), ('After the accounts were opened', 'totaled $885,419.00.'),
          ('On several occasions between 2022', 'without his authorization.'), ('Also, THOMAS and THOMPSON used', 'another individual.'),
          ('Proceeds from some of the other', 'THOMAS and THOMPSON.'), ('In total, THOMAS and THOMSPON', 'from the victim.'),
          ('In June 2023, the credit union', 'the victim’s account.'), ('THOMPSON, who was scheduled', 'fraudulently obtained from the victim.'),
          ('Credit union officials reviewed', 'was THOMPSON’s.'), ('Officers arrested THOMPSON', 'in the victim’s name.'),
          ('Officers obtained a search warrant', '$228,000.00 cash.'), ('On the wire fraud conspiracy count', 'fee of $100.00.'),
          ('On the drug count THOMPSON', 'fee of $100.00.'), ('The case was investigated', 'Narcotics Unit.')],
 'ind': [('were charged a superseding', 'Section 1957.'), ('THOMPSON alone was charged', '924(c)(1)(A).'),
         ('According to the indictment, in 2020', 'a romantic relationship.'), ('From on or about September 6, 2021', 'created by THOMAS and THOMPSON.'),
         ('To obtain these funds', 'which they controlled.'), ('After obtaining the funds', 'as much as $300,000.00,'),
         ('In addition to making cash', '$52,890.00.'), ('If convicted of the wire fraud counts', 'term of imprisonment.'),
         ('For the aggravated identity theft counts', 'term of imprisonment.'), ('reiterated that the superseding', 'reasonable doubt.'),
         ('Also according to court records, on or about June 9, 2023', 'cocaine.')],
}
REDACT = {'plea': [('who is under a guardianship', 'mental incapacity.')]}
def words(pdf):
    xml = subprocess.run(['pdftotext', '-bbox', '-f', '1', '-l', '1', pdf, '-'], capture_output=True, text=True).stdout
    H = float(re.search(r'<page width="([\d.]+)" height="([\d.]+)"', xml).group(2))
    ws = [(float(a), float(b), float(c), float(d), t) for a, b, c, d, t in re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>', xml)]
    return H, [w for w in ws if norm(w[4])]
def find(ws, start, end, seg_only=False):
    toks = [norm(w[4]) for w in ws]; s = [norm(x) for x in start.split() if norm(x)]; e = [norm(x) for x in end.split() if norm(x)]
    for i in range(len(toks)):
        if toks[i:i + len(s)] == s:
            for j in range(i, min(len(toks), i + 600)):
                if toks[j:j + len(e)] == e:
                    seg = ws[i:j + len(e)]
                    return seg if seg_only else (min(w[1] for w in seg), max(w[3] for w in seg))
    raise SystemExit(f'not found: {start!r} … {end!r}\n' + ' '.join(toks)[:3000])
hl = {}
if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True); os.makedirs(HI, exist_ok=True)
    for name, phrases in P.items():
        pdf = f'{D}/{name}.pdf'
        H, ws = words(pdf)
        tk = [norm(w[4]) for w in ws]
        top = min(w[1] for w in ws) - 30
        cut = [ws[i][1] for i in range(len(ws)) if tk[i] == 'contact']
        bot = (min(cut) - 10) if cut else max(w[3] for w in ws) + 30
        base = f'{HI}/{name}'
        subprocess.run(['pdftoppm', '-r', '220', '-png', '-singlefile', '-f', '1', '-l', '1', pdf, base], check=True)
        im = Image.open(base + '.png').convert('L').convert('RGB'); W, HH = im.size; k = HH / H
        d = ImageDraw.Draw(im)
        for s, e in REDACT.get(name, []):
            for w in find(ws, s, e, seg_only=True):
                d.rectangle([w[0] * k - 3, w[1] * k - 2, w[2] * k + 3, w[3] * k + 4], fill=(0, 0, 0))
        y0, y1 = max(0, int(top * k)), min(HH, int(bot * k))
        c = im.crop((int(0.03 * W), y0, int(0.97 * W), y1))
        c = c.resize((1480, int(c.height * 1480 / c.width)), Image.LANCZOS)
        c.save(f'{OUT}/{name}.jpg', quality=88)
        boxes = [find(ws, s, e) for s, e in phrases]
        hl[name] = [[round((a - top) / (bot - top) - 0.004, 4), round((b - top) / (bot - top) + 0.004, 4)] for a, b in boxes]
        print(name, c.size, len(hl[name]))
    json.dump(hl, open(os.path.join(HERE, 'hl.json'), 'w'), indent=1)
