"""Rasterize U.S. government filings in U.S. v. McFarland (S.D.N.Y. 17-cr-600) with pdftoppm -r 220, crop, and compute gold-highlight boxes.
Sources = RECAP PDFs from archive.org (gov.uscourts.nysd.481447 / .496262; see sources.md). Only government-authored filings and court orders are shown.
Writes img/<name>.jpg and hl.json {name: [[y0,y1],...]} with highlight y-ranges as fractions of the crop."""
import subprocess, os, json
from PIL import Image
from findy import find
D = '/home/claude/research/mcf/pdf'; HI = '/home/claude/research/hi'
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, 'img')
P = 'gov.uscourts.nysd.481447.'
CMP = P + '1.0.pdf'    # Sealed complaint, FBI SA Brandon Racz, Jun 30, 2017
MEMO = P + '63.0.pdf'  # Government's sentencing memorandum, Oct 3, 2018
BAIL = P + '42.0.pdf'  # Government letter re bail revocation, Jun 18, 2018
INF = P + '30.0.pdf'   # S1 Superseding Information, Mar 6, 2018 (scan)
JDG = P + '68.0.pdf'   # Judgment, Oct 16, 2018 (scan)
SUB = P + '79.0.pdf'   # Declaration of SA Racz re substitute assets, Jan 10, 2019 (scan)
LTR = P + '98.0.pdf'   # Letter of Judge Buchwald, May 11, 2020 (scan)
jobs = {
 'cmp_cover':  (CMP, 1, 0.03, 0.62, [('BRANDON', 'charges')]),
 'cmp_44':     (CMP, 4, 0.08, 0.62, [('replied,', '$50')]),
 'cmp_60':     (CMP, 5, 0.40, 0.93, [('shows that from', '$57,443.')]),
 'memo_160':   (MEMO, 4, 0.40, 0.93, [('This investor presentation', '2017.”'), ('to triple', '1,200.')]),
 'memo_60':    (MEMO, 5, 0.06, 0.62, [('Between May 2016', '$57,443.'), ('(as well', '(Id.)')]),
 'memo_sprinkle': (MEMO, 5, 0.50, 0.93, [('“Make sure', 'January')]),
 'memo_1459':  (MEMO, 6, 0.05, 0.50, [('included just', 'period.')]),
 'memo_stock': (MEMO, 8, 0.10, 0.62, [('Specifically,', 'shares,')]),
 'memo_smythe': (MEMO, 9, 0.30, 0.86, [('McFarland also created a fake', 'exist.')]),
 'memo_vendor': (MEMO, 10, 0.40, 0.90, [('In or about April 2017,', 'years.')]),
 'memo_victims': (MEMO, 10, 0.05, 0.42, [('Through this scheme,', 'dollars.')]),
 'memo_gala':  (MEMO, 13, 0.08, 0.62, [('You asked,', 'Tickets')]),
 'memo_con':   (MEMO, 24, 0.20, 0.72, [('For the past five years,', 'artist.'), ('Whenever he needed', 'newer and more elaborate one.')]),
 'memo_pent':  (MEMO, 28, 0.05, 0.50, [('In early 2017', 'rent.')]),
 'bail':       (BAIL, 1, 0.15, 0.70, [('the Court should revoke', 'bail.')]),
}
manual = {
 # scanned filings (no usable text layer): highlight y-ranges measured on the page raster; filled by measure step
}
hl = {}
def raster(pdf, page):
    base = f'{HI}/{os.path.basename(pdf)}-{page}'
    if not os.path.exists(base + '.png'):
        subprocess.run(['pdftoppm', '-r', '220', '-png', '-singlefile', '-f', str(page), '-l', str(page), f'{D}/{pdf}', base], check=True)
    return Image.open(base + '.png').convert('RGB')
def save(name, im, y0, y1, boxes):
    W, H = im.size
    c = im.crop((int(0.04 * W), int(y0 * H), int(0.96 * W), int(y1 * H)))
    c = c.resize((1480, int(c.height * 1480 / c.width)), Image.LANCZOS)
    c.save(f'{OUT}/{name}.jpg', quality=88)
    hl[name] = [[round((a - y0) / (y1 - y0) - 0.008, 4), round((b - y0) / (y1 - y0) + 0.008, 4)] for a, b in boxes]
    print(name, c.size, hl[name])
if __name__ == '__main__':
    import manual_boxes
    manual.update(manual_boxes.M)
    for name, (pdf, page, y0, y1, phrases) in jobs.items():
        boxes = []
        for s, e in phrases:
            r = find(f'{D}/{pdf}', page, s, e)
            if not r: raise SystemExit(f'phrase not found: {name} {s!r}')
            boxes.append(r)
        save(name, raster(pdf, page), y0, y1, boxes)
    for name, (pdf, page, y0, y1, boxes) in manual.items():
        save(name, raster(pdf, page), y0, y1, boxes)
    json.dump(hl, open(os.path.join(HERE, 'hl.json'), 'w'), indent=1)
