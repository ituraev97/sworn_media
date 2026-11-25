"""SWORN 024 — Huawei Technologies Co., Ltd. et al., E.D.N.Y. 18-cr-457 (AMD). Jury verdict Nov 24, 2026.
Documents shown (U.S. government works, public domain):
  prv  = DOJ Office of Public Affairs release 26-1413 (Nov 24, 2026), innerText re-typeset as text (no seal/logo)
  s4   = Superseding Indictment (S-4), filed Apr 17, 2026 (RECAP gov.uscourts.nyed.445034 Dkt 689; scanned, OCR for highlight boxes)
  l823 = gov't letter Aug 31, 2026 (jury questionnaires) Dkt 823;  l959 = gov't letter Nov 17, 2026 Dkt 959; l954 = Nov 14, 2026 Dkt 954
  tappy / cnex = trial exhibit photos published inside the DOJ release (credit line 'U.S. v. Huawei Technologies Co Ltd., Case No. 1:18-cr-00457')
Writes img/<name>.jpg and hl.json: hl[key] = [img_name, y0, y1] (fractions of image height)."""
import subprocess, os, json, re, csv, io
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, 'img'); W0 = '/home/claude/work/024'
SRC = W0 + '/src/'; RAS = W0 + '/ras/'; os.makedirs(RAS, exist_ok=True); os.makedirs(OUT, exist_ok=True)
def norm(t): return re.sub(r'[^a-z0-9$]', '', t.lower().replace('’', "'"))
def words_text(pdf):
    xml = subprocess.run(['pdftotext', '-bbox', pdf, '-'], capture_output=True, text=True).stdout; pages = []
    for pg in re.findall(r'<page width="([\d.]+)" height="([\d.]+)">(.*?)</page>', xml, re.S):
        W, H, body = float(pg[0]), float(pg[1]), pg[2]
        ws = [(float(b) / H, float(d) / H, t) for a, b, c, d, t in re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>', body)]
        pages.append(ws)
    return pages
def words_scan(pgm):
    out = subprocess.run(['tesseract', pgm, 'stdout', 'tsv'], capture_output=True, text=True).stdout
    im = Image.open(pgm); H = im.height; ws = []
    for r in csv.DictReader(io.StringIO(out), delimiter='\t', quoting=csv.QUOTE_NONE):
        if r['text'] and r['text'].strip() and float(r['conf']) > 0: ws.append((int(r['top']) / H, (int(r['top']) + int(r['height'])) / H, r['text']))
    return [ws]
def find(ws, start, end):
    toks = [norm(w[2]) for w in ws]; js = norm(start); je = norm(end); jt = ''.join(toks); starts = [0]
    for t in toks: starts.append(starts[-1] + len(t))
    i0 = jt.find(js)
    while i0 >= 0:
        j0 = jt.find(je, i0)
        if j0 >= 0 and j0 - i0 < 3500:
            a = max(k for k in range(len(toks)) if starts[k] <= i0); b = max(k for k in range(len(toks)) if starts[k] < j0 + len(je))
            seg = ws[a:b + 1]; return (min(w[0] for w in seg), max(w[1] for w in seg))
        i0 = jt.find(js, i0 + 1)
    return None
# key: (doc, page(1-based or 0 = search all), start phrase, end phrase)
P = {
 'p_verdict': ('prv', 0, 'The jury convicted Huawei and three subsidiaries', 'money laundering conspiracy.'),
 'p_sent': ('prv', 0, 'Sentencing has been set for', '2027.'),
 'p_skycom': ('prv', 0, 'Huawei conducted its business in Iran under the name', 'applicable sanctions.'),
 'p_banks': ('prv', 0, 'Huawei lied about its activities in Iran to banks', 'because of its lies.'),
 'p_cams': ('prv', 0, 'Testimony further established that Huawei provided surveillance', 'protest activity.'),
 'p_tappy': ('prv', 0, 'Huawei stole proprietary information relating to a testing robot', 'controlled laboratory.'),
 'p_cisco': ('prv', 0, 'Huawei copied the source code used on Cisco routers', 'ocsic'),
 'p_weihua': ('prv', 0, 'A Huawei employee caught photographing', 'rather than'),
 'p_cnex': ('prv', 0, 'When Huawei learned that CNEX', 'proprietary hardware.'),
 'p_quintel': ('prv', 0, 'Huawei obtained confidential information from Quintel', 'patent application.'),
 'p_ag': ('prv', 0, 'No person or company is above the law', 'theft.'),
 'p_iran': ('prv', 0, 'Huawei and its subsidiaries assisted the government of the Islamic', 'protest activity.'),
 's_caption': ('s4', 1, 'UNITED STATES OF AMERICA', 'FUTUREWEI TECHNOLOGIES, INC.,'),
 's_bonus': ('s4', 5, 'internal HUAWEI website, or', 'valuable stolen information.'),
 's_weihua': ('s4', 10, 'Individual-3 wore a badge listing', 'without Huawei'),
 's_junior': ('s4', 10, 'This is a junior engineer who had never', 'values of Huawei.'),
 's_22m': ('s4', 12, 'In or about and between approximately 2009 and 2016', 'from Company 4.'),
 's_robot_ask': ('s4', 12, 'In May 2012, HUAWEI DEVICE USA asked', 'to support that effort.'),
 's_arm': ('s4', 14, 'On or about May 29, 2013', 'HUAWEI DEVICE engineers.'),
 's_isolated': ('s4', 14, 'On or about August 13, 2013', 'moment of indiscretion'),
 's_hpsci': ('s4', 22, 'We have never provided any equipment', 'commercial civilian use'),
 's_100m': ('s4', 23, 'Between approximately 2010 and 2014', 'through the United States.'),
 's_a2': ('s4', 24, 'internal HUAWEI documents referred to such jurisdictions', 'by country name.'),
 's_unoff': ('s4', 24, 'HUAWEI operated Skycom as an unofficial subsidiary', 'link to HUAWEI.'),
 's_ppt': ('s4', 27, 'In relevant part, the PowerPoint presentation included', 'compliance with applicable U.S. law'),
 's_false': ('s4', 27, 'These statements were all false.', 'false.'),
 's_wire': ('s4', 37, 'COUNT SEVEN', '(Wire Fraud)'),
 's_ieepa': ('s4', 41, 'COUNT TEN', '(IEEPA Violations)'),
 's_move': ('s4', 39, 'HUAWEI made efforts to move an employee', 'jurisdiction of the U.S. government.'),
 's_wsj': ('s4', 26, 'In response to the claims in The Wall Street Journal', 'monitoring and filtering activities'),
 's_recon': ('s4', 13, 'describing his trip as follows', 'measurement data.'),
 's_protest': ('s4', 25, 'HUAWEI assisted the Government of Iran by installing', 'Tehran, Iran.'),
 'l_questions': ('l823', 0, 'it appears that a significant number answered', 'Chinese companies generally'),
 'l_nottrial': ('l823', 0, 'But as the Court is well aware', 'are not on trial.'),
 'l_expats': ('l954', 0, 'In the defense case, among other things', 'not to put them beyond'),
 'l_recorded': ('l954', 0, 'The government', 'sensitive nations'),
 'l_rico': ('l959', 0, 'Second, the racketeering acts must have a', 'must have the same or similar purposes'),
}
DOCS = {'prv': ('/home/claude/dl/doj/huawei.pdf', 'text'), 'l823': (SRC + 'l823.pdf', 'text'), 'l954': (SRC + 'l954.pdf', 'text'), 'l959': (SRC + 'l959.pdf', 'text'), 's4': (SRC + 's4.pdf', 'scan')}
if __name__ == '__main__':
    cache = {}
    for d, (path, kind) in DOCS.items():
        if kind == 'text': cache[d] = words_text(path)
        else:
            pgm = '/home/claude/work/024/pdf/s4/p-%02d.pgm'
            cache[d] = [words_scan(pgm % i)[0] for i in range(1, 50)]
    hl = {}; used = {}
    for key, (doc, pg, s, e) in P.items():
        r = None
        pages = [pg - 1] if pg else range(len(cache[doc]))
        for pi in pages:
            ws = cache[doc][pi]
            if doc in ('l823', 'l954', 'l959'): ws = [w for w in ws if 0.06 < w[0] and w[1] < 0.94]
            r = find(ws, s, e)
            if r: break
        if not r: print('NOT FOUND', key); continue
        name = f'{doc}_p{pi + 1}'; used.setdefault(name, (doc, pi, [])); used[name][2].append((key, r))
    for name, (doc, pi, keys) in used.items():
        png = RAS + name; path, kind = DOCS[doc]
        subprocess.run(['pdftoppm', '-r', '200', '-png', '-singlefile', '-f', str(pi + 1), '-l', str(pi + 1), path, png], check=True)
        im = Image.open(png + '.png').convert('L').convert('RGB')
        ws = cache[doc][pi]
        if doc != 'prv':
            ws = [w for w in ws if 0.05 < w[0] and w[1] < 0.95]
        top = max(0, int((min(w[0] for w in ws) - 0.01) * im.height)); bot = min(im.height, int((max(w[1] for w in ws) + 0.012) * im.height))
        if doc == 'prv':   # tall single page: cut into a window around the keys, keep width
            ymin = min(r[0] for k, r in keys); ymax = max(r[1] for k, r in keys)
            top = max(0, int((ymin - 0.03) * im.height)); bot = min(im.height, int((ymax + 0.03) * im.height))
            if bot - top < 700: bot = min(im.height, top + 700)
        x0, x1 = (0.08, 0.92) if doc != 'prv' else (0.0, 1.0)
        c = im.crop((int(x0 * im.width), top, int(x1 * im.width), bot)); c = c.resize((1480, int(c.height * 1480 / c.width)), Image.LANCZOS)
        c.save(f'{OUT}/{name}.jpg', quality=86)
        for key, r in keys:
            hl[key] = [name, round((r[0] * im.height - top) / (bot - top) - 0.006, 4), round((r[1] * im.height - top) / (bot - top) + 0.008, 4)]
    for nm, src in (('tappy', '16143_image_credit.png'), ('cnex', '15200_image_credit.png')):
        im = Image.open(f'/home/claude/work/024/rel/{src}').convert('RGB'); im.resize((1600, int(im.height * 1600 / im.width)), Image.LANCZOS).save(f'{OUT}/{nm}.jpg', quality=92)
    json.dump(hl, open(os.path.join(HERE, 'hl.json'), 'w'), indent=1); print(len(hl), 'keys')
