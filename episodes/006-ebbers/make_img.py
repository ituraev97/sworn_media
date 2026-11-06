"""Rasterize U.S. government documents and court opinions in U.S. v. Ebbers (S.D.N.Y. 02 Cr. 1144) with pdftoppm -r 220, crop, and compute gold-highlight boxes.
Sources (see sources.md):
  opp.pdf  = Brief for the United States in Opposition, Ebbers v. United States, No. 06-590 (Solicitor General, Jan 2007) — archive.org micro_IA40386016_1666
  pet.pdf  = Petition for certiorari, same item; ONLY its Appendix A (2d Cir. opinion, Jul 28, 2006) and Appendix B (S.D.N.Y. order, Jul 9, 2005) pages are shown (court opinions)
  cftf_first_year_report.pdf = DOJ Corporate Fraud Task Force, First Year Report to the President (Jul 2003) — justice.gov/archive/dag/cftf/
  sdny_1216821.pdf = Government letter opposing compassionate release, Oct 4, 2019 (Dkt. 354) — justice.gov/usao-sdny/page/file/1216821/dl
Writes img/<name>.jpg and hl.json {name: [[y0,y1],...]}."""
import subprocess, os, json
from PIL import Image
from findy import find
D = '/home/claude/research/eb/pdf'; HI = '/home/claude/research/hi'
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, 'img')
OPP, PET, CF, GL = 'opp.pdf', 'pet.pdf', 'cftf_first_year_report.pdf', 'sdny_1216821.pdf'
# name: (pdf, page, y0, y1, x0, x1, [(start, end)])
jobs = {
 'opp_line':    (OPP, 11, 0.20, 0.82, 0.13, 0.90, [('The fees that', 'largest'), ('To hide', 'were almost $1 billion higher than expected.')]),
 'opp_38':      (OPP, 12, 0.06, 0.62, 0.10, 0.87, [('From the first', 'capital-expenditure accounts.')]),
 'opp_numbers': (OPP, 13, 0.20, 0.80, 0.13, 0.90, [('Throughout the fraud,', 'expectations,'), ('At trial,', '300 exhib-')]),
 'opp_trash':   (OPP, 14, 0.06, 0.60, 0.11, 0.87, [('he received it', 'reading it.')]),
 'opp_instr':   (OPP, 15, 0.06, 0.62, 0.15, 0.92, [('whether [petitioner] deliberately', 'obvious.')]),
 'ca2_loans':   (PET, 51, 0.42, 0.93, 0.10, 0.86, [('had borrowed over', 'collateral.')]),
 'ca2_hit':     (PET, 52, 0.40, 0.93, 0.10, 0.86, [('Ebbers refused.', 'numbers.”')]),
 'ca2_resign':  (PET, 53, 0.10, 0.62, 0.10, 0.86, [('Vinson and Normand', 'resigning.')]),
 'ca2_right':   (PET, 55, 0.10, 0.62, 0.10, 0.86, [('Sullivan told Ebbers', 'right.”')]),
 'ca2_storms':  (PET, 55, 0.40, 0.93, 0.10, 0.86, [('Instead, he said', 'stock.”')]),
 'ca2_fluff':   (PET, 56, 0.10, 0.62, 0.10, 0.86, [('“accounting fluff,”', '“junk.”')]),
 'ca2_stand':   (PET, 58, 0.10, 0.62, 0.10, 0.86, [('Ebbers assured', 'accounting,”')]),
 'ca2_audit':   (PET, 59, 0.10, 0.62, 0.10, 0.86, [('A month after', '2002.')]),
 'ca2_trash':   (PET, 77, 0.06, 0.55, 0.10, 0.86, [('tossing', 'reading it.')]),
 'ca2_codef':   (PET, 85, 0.40, 0.93, 0.14, 0.88, [('CFO Scott Sullivan,', 'years;')]),
 'ca2_why':     (PET, 86, 0.25, 0.80, 0.10, 0.86, [('All of those', 'Ebbers.')]),
 'ca2_harsh':   (PET, 88, 0.06, 0.50, 0.10, 0.86, [('the sentence is harsh', 'unreasonable')]),
 'cf_24h':      (CF, 45, 0.18, 0.62, 0.53, 0.90, [('Within 24 hours', 'billion.')]),
 'cf_5wk':      (CF, 15, 0.45, 0.96, 0.10, 0.48, [('prosecutors filed', 'fraud.')]),
 'gl_open':     (GL, 1, 0.20, 0.66, 0.08, 0.92, [('The Government writes', 'First Step Act.')]),
 'gl_90':       (GL, 2, 0.08, 0.56, 0.08, 0.92, [('After the fraud was disclosed', 'billion.')]),
 'gl_jones':    (GL, 3, 0.52, 0.93, 0.08, 0.92, [('(“The jury heard', 'numbers'), ('Judge Jones “recognize[d]', 'life sentence')]),
 'gl_2028':     (GL, 4, 0.08, 0.50, 0.08, 0.92, [('Ebbers surrendered', '2028.')]),
 'gl_enough':   (GL, 5, 0.40, 0.80, 0.08, 0.92, [('Ebbers also relies', 'enough.”')]),
}
hl = {}
def raster(pdf, page):
    base = f'{HI}/{pdf}-{page}'
    if not os.path.exists(base + '.png'):
        subprocess.run(['pdftoppm', '-r', '220', '-png', '-singlefile', '-f', str(page), '-l', str(page), f'{D}/{pdf}', base], check=True)
    return Image.open(base + '.png').convert('RGB')
def save(name, im, y0, y1, x0, x1, boxes):
    W, H = im.size
    c = im.crop((int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H)))
    c = c.resize((1480, int(c.height * 1480 / c.width)), Image.LANCZOS)
    c.save(f'{OUT}/{name}.jpg', quality=88)
    hl[name] = [[round((a - y0) / (y1 - y0) - 0.008, 4), round((b - y0) / (y1 - y0) + 0.008, 4)] for a, b in boxes]
    print(name, c.size, hl[name])
if __name__ == '__main__':
    for name, (pdf, page, y0, y1, x0, x1, phrases) in jobs.items():
        boxes = []
        for s, e in phrases:
            r = find(f'{D}/{pdf}', page, s, e)
            if not r: raise SystemExit(f'phrase not found: {name} {s!r}')
            if not (y0 <= r[0] and r[1] <= y1): raise SystemExit(f'phrase outside crop: {name} {r}')
            boxes.append(r)
        save(name, raster(pdf, page), y0, y1, x0, x1, boxes)
    json.dump(hl, open(os.path.join(HERE, 'hl.json'), 'w'), indent=1)
