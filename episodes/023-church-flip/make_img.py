"""SWORN 023 — Richard Reinaldo Garcia, Arlington pastor, "church flipping" fraud. United States v. Garcia, N.D. Tex. 4:26-cr-146-P.
Documents shown (U.S. government works, public domain):
  ind = Superseding Indictment, Dkt. 35 (filed Oct 7, 2026) — attached to the USAO N.D. Tex. release (justice.gov/usao-ndtx/media/1473611)
  prv = USAO N.D. Tex. release, Nov 20, 2026 (updated Nov 22) — innerText re-typeset as text (txt2pdf.js), no seal/logo/images
  foa = government trial exhibits (summary charts marked "DRAFT") attached to the release (media/1473651); private investors' names,
        their companies and uncharged family signers are blacked out.
  house_1..3 = photos published inside the USAO release (justice.gov/sites/default/files/2026-11/house_N.png), uncaptioned there.
Writes img/<name>.jpg and hl.json: hl[key] = [img_name, y0, y1] (fractions of image height)."""
import subprocess, os, json, re
from PIL import Image, ImageDraw, ImageFilter
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, 'img')
S = '/home/claude/work/023/src/'
DOCS = {'ind': S + 'indictment.pdf', 'prv': '/home/claude/dl/doj/prv.pdf'}
def norm(t): return re.sub(r'[^a-z0-9$]', '', t.lower().replace('’', "'"))
def words(pdf):
    xml = subprocess.run(['pdftotext', '-bbox', pdf, '-'], capture_output=True, text=True).stdout
    pages = []
    for pg in re.findall(r'<page width="([\d.]+)" height="([\d.]+)">(.*?)</page>', xml, re.S):
        W, H, body = float(pg[0]), float(pg[1]), pg[2]
        ws = [(float(a), float(b), float(c), float(d), t) for a, b, c, d, t in re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>', body)]
        pages.append((W, H, ws))
    return pages
def find(ws, start, end):
    toks = [norm(w[4]) for w in ws]; js = norm(start); je = norm(end)
    jt = ''.join(toks); starts = [0]
    for t in toks: starts.append(starts[-1] + len(t))
    i0 = jt.find(js)
    while i0 >= 0:
        j0 = jt.find(je, i0)
        if j0 >= 0 and j0 - i0 < 3000:
            a = max(k for k in range(len(toks)) if starts[k] <= i0)
            b = max(k for k in range(len(toks)) if starts[k] < j0 + len(je))
            seg = ws[a:b + 1]; return (min(w[1] for w in seg), max(w[3] for w in seg))
        i0 = jt.find(js, i0 + 1)
    return None
P = {
 'i_caption': ('ind', 'UNITED STATES OF AMERICA', 'SUPERSEDING INDICTMENT'),
 'i_entities': ('ind', 'Richard Reinaldo Garcia, defendant, is a current', 'MG Kingdom, Inc.'),
 'i_names': ('ind', 'Iglesia Gracia de Texas is an entity', 'Richard Garcia Ministries.'),
 'i_flip': ('ind', 'Executed Partnership Agreements, or', 'a third-party buyer.'),
 'i_roi': ('ind', 'misrepresented to victims that the profits', 'own personal expenses;'),
 'i_concert': ('ind', 'Executed Investment Contracts, or', 'share with victims.'),
 'i_notintend': ('ind', 'did not intend to i) host concerts', 'own personal expenses;'),
 'i_donation': ('ind', 'Directed many victims who executed', 'personal expenses;'),
 'i_dup': ('ind', 'Entered into duplicative Partnership', 'by other individual victims;'),
 'i_kenya': ('ind', 'Made fraudulent representations to solicit funds', 'used to pay for unrelated'),
 'i_check': ('ind', 'In or about August 2021, defendant Garcia and Co-Defendant A entered', 'ARLINGTON xxxx.'),
 'i_55k': ('ind', 'After in or about August 2021', 'invest in a new project.'),
 'i_hazel': ('ind', 'On or about October 6, 2023', 'respectively.'),
 'i_hazellie': ('ind', 'Defendant Garcia falsely represented to Individual C that he had secured', 'Hazel Street project.'),
 'i_lubbock': ('ind', 'On or about November 6, 2023', 'account no. x2450.'),
 'i_donletter': ('ind', 'In 2024, Defendant Garcia directed', 'listed donations to the Church.'),
 'i_may2025': ('ind', 'May 2025, Defendant solicited funds', 'executed an agreement to sell'),
 'i_24m': ('ind', 'Ave, Arlington, Texas to a buyer for the amount of $2,400,000', 'Commercial Contract.'),
 'i_lulling': ('ind', 'Garcia made lulling payments', 'specific agreements.'),
 'i_70': ('ind', 'over approximately 70 victims', 'personal enrichment.'),
 'p_verdict': ('prv', 'Following a four-day trial', 'three counts of wire fraud.'),
 'p_70': ('prv', 'for orchestrating a real estate', 'Dominican Republic.'),
 'p_quote': ('prv', 'This defendant didn', 'fraud scheme.'),
 'p_quick': ('prv', 'The jury saw through those lies', 'very quick decision by the jury'),
 'p_scheme': ('prv', 'from at least August 2021 through April 2025', 'business operating costs.'),
 'p_reinvest': ('prv', 'When victims questioned missing profits', 'other projects.'),
 'p_church': ('prv', 'Trial evidence showed that Garcia served as a pastor', 'additional investments from victims.'),
 'p_accounts': ('prv', 'Evidence further showed that Garcia controlled', 'tied to the fraudulent scheme.'),
 'p_personal': ('prv', 'Between approximately 2023 and October 2025', 'more than $1.6 million.'),
 'p_6m': ('prv', 'victims collectively lost', 'scheme.'),
 'p_sent': ('prv', 'Garcia faces up to 20 years', 'March 4, 2027.'),
 'p_fbi': ('prv', 'The FBI requests', 'Questionnaire'),
 'p_fbiq': ('prv', 'The defendant\'s scheme betrayed', 'financial security'),
}
# names of private investors / their companies / uncharged relatives on the government charts -> blacked out
REDACT = [['CARLOS', 'LOPEZ'], ['JOHN', 'MONCADA'], ['LOPEZ'], ['MONCADA'], ['COSTAL', 'COIN', 'INVESTMENTS', 'LLC'],
          ['JDI', 'BETHEL', 'GROUP', 'INC.'], ['Jessica', 'E', 'Garcia'], ['Rey', 'E', 'Garcia'], ['Jessica'], ['Rey', 'E'], ['INGRID', 'ROSARIO'], ['INGRID'], ['ROSARIO']]
FOA = {'f_never': 2, 'f_tx1': 4, 'f_rg1': 6, 'f_rg2': 9, 'f_lub': 11}
def foa_chart(name, page):
    W, H, ws = words(S + 'foa_exhibits.pdf')[page - 1]
    png = f'/home/claude/work/023/ras/{name}'
    os.makedirs(os.path.dirname(png), exist_ok=True)
    subprocess.run(['pdftoppm', '-r', '200', '-png', '-singlefile', '-f', str(page), '-l', str(page), S + 'foa_exhibits.pdf', png], check=True)
    im = Image.open(png + '.png').convert('RGB'); k = im.width / W; d = ImageDraw.Draw(im)
    toks = [w[4] for w in ws]; n = 0
    for pat in REDACT:
        for i in range(len(toks) - len(pat) + 1):
            if [t.strip(',').upper() for t in toks[i:i + len(pat)]] == [p.upper() for p in pat]:
                seg = ws[i:i + len(pat)]
                if len(pat) > 1 and max(w[1] for w in seg) - min(w[1] for w in seg) > 30: continue
                for w in seg:
                    d.rectangle([w[0] * k - 4, w[1] * k - 3, w[2] * k + 4, w[3] * k + 3], fill=(0, 0, 0)); n += 1
    # crop to the dark slide band
    g = im.convert('L'); px = g.load(); col = im.width // 2
    ys = [y for y in range(im.height) if px[col, y] < 120]
    im = im.crop((0, max(0, ys[0]), im.width, min(im.height, ys[-1] + 1)))
    im = im.resize((1920, int(im.height * 1920 / im.width)), Image.LANCZOS)
    im.save(f'{OUT}/{name}.jpg', quality=90); print(name, 'redacted words', n, im.size)
def house(n):
    im = Image.open(f'{S}house_{n}.png').convert('RGB')
    big = im.resize((1600, int(im.height * 1600 / im.width)), Image.LANCZOS)
    big.save(f'{OUT}/house{n}.jpg', quality=90)
if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True); hl = {}; used = {}
    cache = {k: words(v) for k, v in DOCS.items()}
    for key, (doc, s, e) in P.items():
        r = None
        for pi, (W, H, ws) in enumerate(cache[doc]):
            if doc == 'ind': ws = [w for w in ws if w[1] > 0.05 * H and w[3] < 0.93 * H]   # drop ECF header + page footer
            r = find(ws, s, e)
            if r: break
        if not r: print('NOT FOUND', key); continue
        name = f'{doc}_p{pi + 1}'; used[name] = (doc, pi, W, H, ws)
        hl[key] = [name, r]
    for name, (doc, pi, W, H, ws) in used.items():
        png = f'/home/claude/work/023/ras/{name}'
        os.makedirs(os.path.dirname(png), exist_ok=True)
        subprocess.run(['pdftoppm', '-r', '200', '-png', '-singlefile', '-f', str(pi + 1), '-l', str(pi + 1), DOCS[doc], png], check=True)
        im = Image.open(png + '.png').convert('L').convert('RGB'); k = im.height / H
        top = max(0, min(w[1] for w in ws) * k - 30); bot = min(im.height, max(w[3] for w in ws) * k + 24)
        x0, x1 = (0.08, 0.92) if doc == 'ind' else (0.02, 0.98)
        c = im.crop((int(x0 * im.width), int(top), int(x1 * im.width), int(bot)))
        c = c.resize((1480, int(c.height * 1480 / c.width)), Image.LANCZOS); c.save(f'{OUT}/{name}.jpg', quality=86)
        for key, v in hl.items():
            if v[0] == name and isinstance(v[1], tuple):
                y0, y1 = v[1]; hl[key] = [name, round((y0 * k - top) / (bot - top) - 0.006, 4), round((y1 * k - top) / (bot - top) + 0.008, 4)]
    for nm, pg in FOA.items(): foa_chart(nm, pg)
    for n in (1, 2, 3): house(n)
    json.dump(hl, open(os.path.join(HERE, 'hl.json'), 'w'), indent=1)
    print(json.dumps(hl))
