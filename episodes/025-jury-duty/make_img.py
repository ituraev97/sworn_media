"""SWORN 025 — DOJ anti-scam surge (Nov 24, 2026) + the Georgia-prison "jury duty impostor" scheme.
Documents shown (U.S. government works, public domain):
  aff = Affidavit in Support of an Application for a Seizure Warrant, In re Seizure of Web-Hosting Accounts for ejurorcourts.org,
        judicialservices.org, civilservicesdivision.org, D.N.J. Mag. No. 26-8230 (JSA), Doc. 1, filed 11/05/2026 (64 pp; DOJ already
        blurred faces and blacked out names). https://www.justice.gov/criminal/media/1473906/dl?inline
Writes img/aff_pNN.jpg (150 dpi pages, DOJ seal not present on the chosen pages) and hl.json: hl[key] = [img_name, y0, y1] (fractions).
Run: python3 make_img.py /home/claude/work/025/affidavit.pdf"""
import subprocess, os, json, re, sys
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, 'img'); os.makedirs(OUT, exist_ok=True)
PDF = sys.argv[1]
def norm(t): return re.sub(r'[^a-z0-9$]', '', t.lower().replace('’', "'"))
xml = subprocess.run(['pdftotext', '-bbox', PDF, '-'], capture_output=True, text=True).stdout
pages = []
for pg in re.findall(r'<page width="([\d.]+)" height="([\d.]+)">(.*?)</page>', xml, re.S):
    H = float(pg[1])
    pages.append([(float(b) / H, float(d) / H, t) for a, b, c, d, t in re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>', pg[2])])
def find(pn, start, end):
    ws = pages[pn - 1]; toks = [norm(w[2]) for w in ws]; jt = ''.join(toks); starts = [0]
    for t in toks: starts.append(starts[-1] + len(t))
    js, je = norm(start), norm(end); i0 = jt.find(js)
    while i0 >= 0:
        j0 = jt.find(je, i0)
        if j0 >= 0:
            a = max(k for k in range(len(toks)) if starts[k] <= i0); b = max(k for k in range(len(toks)) if starts[k] < j0 + len(je))
            seg = ws[a:b + 1]; return (round(min(w[0] for w in seg) - 0.004, 4), round(max(w[1] for w in seg) + 0.004, 4))
        i0 = jt.find(js, i0 + 1)
    return None
USE = [7, 8, 10, 14, 21, 22, 24, 34, 45, 47, 53]
for p in USE:
    subprocess.run(['pdftoppm', '-r', '150', '-jpeg', '-f', str(p), '-l', str(p), PDF, f'/tmp/aff_{p}'], check=True)
    f = [x for x in os.listdir('/tmp') if x.startswith(f'aff_{p}-')][0]
    im = Image.open('/tmp/' + f).convert('RGB'); w, h = im.size
    im = im.crop((0, int(h * 0.05), w, int(h * 0.95)))   # drop ECF header/footer strip
    im.save(f'{OUT}/aff_p{p:02d}.jpg', quality=90)
# (page, start phrase, end phrase)
P = {
 'ftc': (7, 'Database, from January 2021', 'losses of around $13 million'),
 'call': (7, 'This scheme typically starts when a victim', 'will go to jail'),
 'pay': (14, 'typically pay the scammers thousands of dollars', 'hundreds of thousands of dollars'),
 'scammers': (22, 'I believe that the vast majority of jury duty fraud perpetrators', 'Georgia state prison system'),
 'btc': (24, 'between September 2022 and', 'Georgia'),
 'table': (34, 'ejurorcourts.org', '03/16/2026'),
 'v2': (53, 'The scammers directed victim-2 to drive to a crypto ATM', 'over 6 hours'),
 'banner': (47, 'The official wording is', 'Secure .gov websites use'),
}
hl = {}
for k, (pn, a, b) in P.items():
    r = find(pn, a, b)
    if r is None: print('NOT FOUND', k); continue
    # convert from page fractions to cropped-image fractions
    y0 = max(0.0, (r[0] - 0.05) / 0.90); y1 = min(1.0, (r[1] - 0.05) / 0.90)
    hl[k] = [f'aff_p{pn:02d}', round(y0, 4), round(y1, 4)]
json.dump(hl, open(os.path.join(HERE, 'hl.json'), 'w'), indent=1); print(hl)
# redact handwritten personal names in the script figure (p8): impersonated-deputy name and a named person
from PIL import ImageDraw
im = Image.open(f'{OUT}/aff_p08.jpg'); d = ImageDraw.Draw(im)
for box in [(298, 143, 548, 180), (250, 285, 398, 322)]: d.rectangle(box, fill=(0, 0, 0))
im.save(f'{OUT}/aff_p08.jpg', quality=90)
