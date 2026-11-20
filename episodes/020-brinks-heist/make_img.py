"""SWORN 020 — United States v. Carlos Victor Mestanza Cercado et al. (C.D. Cal. 5:25-cr-00198-KK). Documents shown
(U.S. government works / court records, public domain), all from the RECAP mirror on archive.org (gov.uscourts.cacd.974654/974655):
  i1–i13  = grand-jury indictment, Dkt. 1 (filed June 11, 2025), text layer; page 14 (signatures) not used.
  p1–p19  = plea agreement for defendant Mestanza, Dkt. 158 (filed Nov 9, 2026; drafted and signed by the U.S. Attorney's Office),
            text layer; signature/certification pages 20–22 not used.
  s1–s4   = government/defense joint stipulation to continue trial, Dkt. 156 (filed Sep 10, 2026), text layer.
  pr26/pr25 = USAO C.D. Cal. press releases of Nov 19, 2026 and June 17, 2025, saved as innerText (pw_pdf.js) and
            re-typeset as text (txt2pdf.js: no seal, logo or images).
Rasterized with pdftoppm -r 220; highlight boxes from pdftotext -bbox. Writes img/<name>.jpg and hl.json:
  hl[key] = [img_name, y0, y1]  (fractions of the image height).
Private names: none of the documents used names a private victim; the jewelers/companies are not named in the excerpts."""
import subprocess, os, json, re
from PIL import Image
D = '/home/claude/dl/brinks/doj'; HI = '/home/claude/hi20'
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, 'img')
def norm(t): return re.sub(r'[^a-z0-9]', '', t.lower())
DOCS = {'i': ('indictment', range(1, 14)), 'p': ('plea', range(1, 20)), 's': ('stip156', range(1, 5))}
# key: (doc prefix, start phrase, end phrase)
P = {
 'i_caption': ('i', 'UNITED STATES OF AMERICA', 'I N D I C T M E N T'),
 'i_object': ('i', 'Beginning no later than on or about March 2, 2022', 'Section 659.'),
 'i_follow': ('i', 'would use multiple vehicles to follow victim truck', 'unlawfully carry away the merchandise from the victims.'),
 'i_lookouts': ('i', 'Some conspirators would act as lookouts', 'seemingly unattended.'),
 'i_fence': ('i', 'would return to Los Angeles County with the stolen merchandise', 'fence for profit.'),
 'i_oa14': ('i', 'Overt Act No. 14:', 'phone with a co-conspirator.'),
 'i_oa17': ('i', 'Overt Act No. 17:', 'traveled in interstate commerce.'),
 'i_oa18': ('i', 'Overt Act No. 18:', 'defendant VALENCIA.'),
 'i_oa19': ('i', 'Overt Act No. 19:', 'Lebec, California.'),
 'i_oa20': ('i', 'Overt Act No. 20:', 'Brinks semitruck.'),
 'i_oa21': ('i', 'Overt Act No. 21:', 'approximately $100,000,000.'),
 'i_oa22': ('i', 'Overt Act No. 22:', 'Brinks semitruck.'),
 'i_oa6': ('i', 'Overt Act No. 6:', 'small knife in his hand.'),
 'i_count6': ('i', 'that is, jewelry that the', 'freight, express, and property.'),
 'p_count3': ('p', 'appear and plead guilty to count three', 'U.S.C. § 1951(a).'),
 'p_dismiss': ('p', 'At the time of sentencing, move to dismiss the', 'the sentence to be imposed.'),
 'p_max': ('p', 'the statutory maximum sentence', 'special assessment of $100.'),
 'p_restit': ('p', 'restitution is at least $100,312,031.54', 'prior to sentencing.'),
 'p_declared': ('p', 'before the July 11, 2022 theft', 'victims’ actual losses.'),
 'p_guilty': ('p', 'Defendant admits that defendant is, in fact, guilty', 'agreeing to plead guilty.'),
 'p_series': ('p', 'Beginning no later than on or about March 2, 2022, and', 'divide up and sell for'),
 'p_711': ('p', 'On March 2, 2022, defendant and co-conspirators, using multiple', 'translating from Spanish into English'),
 'p_airtag': ('p', 'When the box truck driver caught defendant', 'did not intervene,'),
 'p_87': ('p', 'To facilitate the robbery, defendant also', 'before and during the'),
 'p_scout': ('p', 'On July 8, 9, and 10, 2022, a co-conspirator scouted', 'in transit following the show.'),
 'p_73': ('p', 'On July 10, 2022, defendant and co-', 'traveled in interstate commerce.'),
 'p_300': ('p', 'When the Brinks truck departed', 'in Buttonwillow and Lebec, California.'),
 'p_24': ('p', 'and co-conspirators broke the locks', 'traveled to East Hollywood with the stolen jewelry.'),
 'p_deact': ('p', 'In the days that followed', 'to try to conceal their identities.'),
 'p_search': ('p', 'After the indictment against defendant in this case was made', 'Interpol, and Ecuadorians'),
 'p_texts': ('p', 'Between June 18 and 20, 2025', '“still ha[s] to be careful.”'),
 'p_robo': ('p', 'On June 28, 2025, defendant messaged', '“robo grande.”'),
 'p_panama': ('p', 'On July 1, 2025, defendant was', 'from Guatemala to Ecuador.'),
 'p_base': ('p', 'Robbery Base Offense Level:', '§ 2B1.1(a)(2)'),
 's_discovery': ('s', 'photographs, license plate reader', '33,164 files.'),
 's_trial': ('s', 'CURRENT TRIAL DATE:', '03-22-27'),
 'pr26:plea': ('pr26', 'An Ecuadorian national pleaded guilty today', 'jewelry show in Northern California.'),
 'pr26:who': ('pr26', 'Carlos Victor Mestanza Cercado, 33', '(Hobbs Act).'),
 'pr26:notappeared': ('pr26', 'Co-defendants Victor Hugo Valencia Solorzano', 'removed from the United States.'),
 'i_oa2223': ('i', 'Overt Act No. 22:', 'LUGO and VALENCIA also deactivated their cellphone numbers that they had been using to steal the jewelry from the Brinks semitruck.'),
 'pr26:custody': ('pr26', 'Mestanza has been in federal custody', 'charges in this case.'),
 'pr26:fled': ('pr26', 'Mestanza fled the U.S. in June 2025', 'from Guatemala to Ecuador.'),
 'pr26:restit': ('pr26', 'Law enforcement believes', 'at least $100,312,031.'),
 'pr26:sentencing': ('pr26', 'United States District Judge Kenly Kiya Kato', '20 years in federal prison.'),
 'pr26:trial': ('pr26', 'The following defendants charged in this case', 'March 22, 2027:'),
 'pr26:atlarge': ('pr26', 'Co-defendants Victor Hugo Valencia Solorzano', 'charges against them.'),
 'pr26:removed': ('pr26', 'On February 12, the charges', 'removed from the United States.'),
 'pr25:largest': ('pr25', 'Two Southern California residents are expected', 'largest jewelry heist in U.S. history.'),
 'pr25:recovered': ('pr25', 'Some of that jewelry was recovered', 'on June 16.'),
 'pr25:presumed': ('pr25', 'An indictment contains allegations', 'proven guilty in court.'),
}
def words(pdf, page):
    xml = subprocess.run(['pdftotext', '-bbox', '-f', str(page), '-l', str(page), pdf, '-'], capture_output=True, text=True).stdout
    H = float(re.search(r'<page width="([\d.]+)" height="([\d.]+)"', xml).group(2))
    ws = [(float(a), float(b), float(c), float(d), t) for a, b, c, d, t in re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>', xml)]
    ws.sort(key=lambda w: (round(w[3] / 4), w[0]))  # reading order: line by line (pdftotext puts indented first words last)
    # drop pleading-paper line numbers in the left margin (they interrupt phrases)
    return H, [w for w in ws if norm(w[4]) and not (w[0] < 80 and re.fullmatch(r'\d{1,2}', w[4]))]
def find(ws, start, end):
    toks = [norm(w[4]) for w in ws]; s = [norm(x) for x in start.split() if norm(x)]; e = [norm(x) for x in end.split() if norm(x)]
    jt = ''.join(toks); js = ''.join(s); je = ''.join(e)
    # joined-token search (robust to hyphenation / split tokens)
    starts = [0]
    for t in toks: starts.append(starts[-1] + len(t))
    i0 = jt.find(js)
    while i0 >= 0:
        j0 = jt.find(je, i0)
        if j0 >= 0 and j0 - i0 < 6000:
            a = max(k for k in range(len(toks)) if starts[k] <= i0)
            b = max(k for k in range(len(toks)) if starts[k] < j0 + len(je))
            seg = ws[a:b + 1]
            return (min(w[1] for w in seg), max(w[3] for w in seg))
        i0 = jt.find(js, i0 + 1)
    return None
if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True); os.makedirs(HI, exist_ok=True)
    pages = {}
    for pre, (doc, rng) in DOCS.items():
        pdf = f'{D}/{doc}.pdf'
        for pg in rng:
            H, ws = words(pdf, pg)
            body = [w for w in ws if not (w[1] < 0.06 * H)]  # drop the ECF header line
            top = max(0, min(w[1] for w in body) - 20); bot = max(w[3] for w in body) + 16
            pages[f'{pre}{pg}'] = (pdf, pg, top, bot, ws, H)
    for n in ('pr26', 'pr25'):
        H, ws = words(f'{D}/{n}.pdf', 1)
        tk = [norm(w[4]) for w in ws]
        cut = [ws[i][1] for i in range(len(ws)) if tk[i] == 'contact']
        pages[n] = (f'{D}/{n}.pdf', 1, min(w[1] for w in ws) - 30, (min(cut) - 10) if cut else max(w[3] for w in ws) + 30, ws, H)
    for name, (pdf, pg, top, bot, ws, H) in pages.items():
        base = f'{HI}/{name}'
        subprocess.run(['pdftoppm', '-r', '220', '-png', '-singlefile', '-f', str(pg), '-l', str(pg), pdf, base], check=True)
        im = Image.open(base + '.png').convert('L').convert('RGB'); W, HH = im.size; k = HH / H
        x0, x1 = (0.05, 0.95) if not name.startswith('pr') else (0.03, 0.97)
        c = im.crop((int(x0 * W), max(0, int(top * k)), int(x1 * W), min(HH, int(bot * k))))
        c = c.resize((1480, int(c.height * 1480 / c.width)), Image.LANCZOS)
        c.save(f'{OUT}/{name}.jpg', quality=86)
    hl = {}
    for key, (pre, s, e) in P.items():
        cands = [pre] if pre.startswith('pr') else [n for n in pages if re.fullmatch(pre + r'\d+', n)]
        hit = None
        for name in sorted(cands, key=lambda n: int(re.sub(r'\D', '', n) or 0)):
            pdf, pg, top, bot, ws, H = pages[name]
            r = find(ws, s, e)
            if r:
                hit = [name, round((r[0] - top) / (bot - top) - 0.004, 4), round((r[1] - top) / (bot - top) + 0.004, 4)]; break
        if not hit:
            raise SystemExit(f'not found: {key}')
        hl[key] = hit
    used = sorted({v[0] for v in hl.values()})
    for f in os.listdir(OUT):  # keep only pages used
        if f.endswith('.jpg') and re.fullmatch(r'(i|p|s)\d+\.jpg|pr2[56]\.jpg', f) and f[:-4] not in used:
            os.remove(os.path.join(OUT, f))
    json.dump(hl, open(os.path.join(HERE, 'hl.json'), 'w'), indent=1)
    print(json.dumps(hl))
