"""SWORN 021 — United States v. Jody E. Owens II, Chokwe Antar Lumumba and Aaron B. Banks (S.D. Miss. 3:24-cr-00103-DPJ-LGI).
Documents shown (U.S. government works / federal court records, public domain):
  i1–i32 = grand-jury indictment, Dkt. 3 (filed under seal Oct 23, 2024; unsealed Nov 7, 2024), as attached to the
           U.S. Attorney's Office (S.D. Miss.) press release of Nov 7, 2024 (justice.gov/usao-sdms/media/1376361/dl).
           Scanned → rasterized at 220 dpi (pdftoppm), word boxes from tesseract TSV. The ECF header line is cropped off.
  n33    = Notice of maximum penalties, Dkt. 3-1 (same attachment).
  pr24   = USAO S.D. Miss. press release of Nov 7, 2024, saved as innerText (pw_pdf.js) and re-typeset as text (txt2pdf.js:
           no seal, logo or images).
  Photos  = still images printed INSIDE the indictment (FBI recordings / FBI search photo): ph_call (¶56, p.16),
           ph_sofa (¶57–58, p.17), ph_bag (¶60, p.18), ph_book (¶65, p.19). Captions say only what the indictment says.
Profanity: paragraphs whose text contains profanity are not used as document images (quoted in quote cards with [expletive]).
Private persons: Witness 1 / Company A / the city employee are not named in the indictment excerpts; nothing to redact.
Writes img/<name>.jpg and hl.json: hl[key] = [img_name, y0, y1] (fractions of the image height)."""
import subprocess, os, json, re
from PIL import Image, ImageFilter
SRC = '/home/claude/dl/ind'          # p-01.jpg … p-38.jpg (pdftoppm -r 220 of indictment.pdf)
PR = '/home/claude/dl/doj/pr24.pdf'
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, 'img')
def norm(t): return re.sub(r'[^a-z0-9$]', '', t.lower().replace('’', "'"))
def tsv(path):
    cache = path[:-4] + '.tsv'
    if not os.path.exists(cache):
        subprocess.run(['tesseract', path, path[:-4], 'tsv'], capture_output=True)
    ws = []
    for line in open(cache, encoding='utf8').read().splitlines()[1:]:
        f = line.split('\t')
        if len(f) == 12 and f[11].strip() and f[10] != '-1':
            x, y, w, h = map(int, f[6:10]); ws.append((x, y, x + w, y + h, f[11]))
    return ws
def find(ws, start, end):
    toks = [norm(w[4]) for w in ws]; js = norm(start.replace(' ', '')); je = norm(end.replace(' ', ''))
    jt = ''.join(toks); starts = [0]
    for t in toks: starts.append(starts[-1] + len(t))
    i0 = jt.find(js)
    while i0 >= 0:
        j0 = jt.find(je, i0)
        if j0 >= 0 and j0 - i0 < 4000:
            a = max(k for k in range(len(toks)) if starts[k] <= i0)
            b = max(k for k in range(len(toks)) if starts[k] < j0 + len(je))
            seg = ws[a:b + 1]
            return (min(w[1] for w in seg), max(w[3] for w in seg))
        i0 = jt.find(js, i0 + 1)
    return None
# key: (page prefix 'i' = any indictment page | exact page name, start phrase, end phrase)
P = {
 'i_caption': ('i1', 'UNITED STATES OF AMERICA', 'AARON B. BANKS'),
 'i_overview': ('i1', 'Beginning on or about October 16, 2023', 'downtown Jackson development project.'),
 'i_fbi': ('i2', 'aware that, in reality', 'Investigation'),
 'i_p2banks': ('i2', 'As part of the scheme, on or about January 11, 2024', 'protective detail service.'),
 'i_p4': ('i2', 'As part of the scheme, in or about March and April of 2024', 'including OWENS and SMITH.'),
 'i_mayor': ('i3', 'was first elected the Mayor', 'City Council for a vote.'),
 'i_hud': ('i4', 'Since approximately 2008', 'complete its downtown development project.'),
 'i_rfp': ('i5', 'The DPD last issued an RFP', 'from qualified developers.'),
 'i_rfq': ('i5', 'On February 5, 2024', 'March 12, 2024.'),
 'i_intro': ('i5', 'On or about August 14, 2023', 'Developer'),
 'i_jet': ('i6', 'On October 9, 2023, through October 11, 2023', 'business opportunities in Jackson.'),
 'i_250k': ('i6', 'The following day, on November 8, 2023', 'Witness 1 was to be paid $50,000.'),
 'i_yacht1': ('i7', 'On or about December 13, 2023', 'himself, SMITH, and Witness'),
 'i_fixed': ('i7', 'After receiving the $125,000', 'needs something fixed.'),
 'i_warroom': ('i7', 'On or about January 10, 2024', 'for the downtown development project.'),
 'i_banks50': ('i8', 'When BANKS rejoined the meeting', 'would help.'),
 'i_notfbi': ('i8', 'On February 12, 2024, OWENS arranged a dinner', 'related to the convention area hotels.'),
 'i_pawns': ('i9', 'three more votes', 'the pawns.'),
 'i_60k': ('i9', 'On February 13, 2024, OWENS and the Developers met', 'Hinds County District Attorney'),
 'i_envelope': ('i9', 'When BANKS arrived in the back room', 'development project.'),
 'i_leedebt': ('i10', 'Two days later, on or about February 15, 2024', 'proposed development project.'),
 'i_why': ('i10', 'At another point in the meeting', 'could make things a lot harder.'),
 'i_bword': ('i11', 'Here', 'the b-word is, right?'),
 'i_text': ('i13', 'After the meeting, OWENS texted LUMUMBA', 'private fundraiser.'),
 'i_tenchecks': ('i13', 'OWENS said that they would hold a', 'a bunch of different companies.'),
 'i_accord': ('i13', 'On March 10, 2024, OWENS called Developer 1', 'at a “fundraiser” in Florida.'),
 'i_final': ('i14', 'OWENS also said that he had assured LUMUMBA', 'final number” was $100,000.'),
 'i_lee': ('i14', 'On or about March 27, 2024, OWENS planned', 'Developer 2’s credit card.'),
 'i_conv': ('i15', 'On or about March 27 and 28, 2024', 'two associates in full.'),
 'i_yacht2': ('i15', 'On April 2, 2024, OWENS, LUMUMBA, SMITH', 'The following exchange was captured:'),
 'i_dialog': ('i15', 'We want to be very mindful', 'something similar.'),
 'i_call': ('i16', 'Developer 1 then asked LUMUMBA', 'April 15, 2024:'),
 'i_checks': ('i16', 'Later in the discussion, Developer 2 handed', 'stated: “Okay.”'),
 'i_worth': ('i17', 'OWENS and LUMUMBA understood that the money', 'additional $50,000 in the future.'),
 'i_confirm': ('i17', 'Developer 2 then directly asked', 'deadline would be moved.'),
 'i_owens50': ('i17', 'Later that same day, OWENS had a separate', 'put it in his pockets:'),
 'i_club': ('i18', 'During the evening of April 2, 2024', 'benefit.'),
 'i_deposit': ('i18', 'Following LUMUMBA', 'approximately $465.30.'),
 'i_9500': ('i18', 'On or about April 5, 2024, a check', 'Both checks were ultimately cashed.'),
 'i_serial': ('i19', 'Between February and April 2024, OWENS made', 'via serial numbers.'),
 'i_lockbox': ('i19', 'On May 22, 2024, pursuant to', 'December 13, 2023.'),
 'i_none': ('i31', 'he was asked whether there were any safes', 'none exist'),
 'i_count5': ('i27', 'the defendant, CHOKWE ANTAR LUMUMBA', 'to benefit the Developers.'),
 'i_shorten': ('i23', 'LUMUMBA solicited and accepted the aforementioned bribes', 'would be selected.'),
 'n_count1': ('n33', 'OWENS, BANKS, and LUMUMBA', 'special assessment'),
 'pr:alleges': ('pr24', 'As alleged in the indictment, between approximately October 2023', 'when to bribe those officials.'),
 'pr:lumumba': ('pr24', 'As part of the scheme, Mayor Lumumba accepted', 'portion of the payment.'),
 'pr:gee': ('pr24', 'Leaders who are awarded', 'benefit themselves'),
 'pr:presumed': ('pr24', 'An indictment is merely an allegation', 'court of law.'),
}
PHOTOS = {  # name: (page, box in original page pixels 1865 x ~2428)
 'ph_call': (16, (311, 728, 1556, 1482)),
 'ph_sofa': (17, (333, 213, 1582, 1024)),
 'ph_bag': (18, (387, 219, 1480, 1019)),
 'ph_book': (19, (410, 1156, 1462, 1862)),
}
if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    pages = {}
    for pg in list(range(1, 33)) + [33]:
        path = f'{SRC}/p-{pg:02d}.jpg'; im = Image.open(path); W, H = im.size
        ws = [w for w in tsv(path) if w[1] > 0.045 * H]          # drop ECF header line
        for ppg, (bx0, by0, bx1, by1) in PHOTOS.values():      # OCR noise inside the printed photos
            if ppg == pg: ws = [w for w in ws if not (w[0] > bx0 - 10 and w[2] < bx1 + 10 and w[1] > by0 - 10 and w[3] < by1 + 10)]
        top = max(0, min(w[1] for w in ws) - 24); bot = min(H, max(w[3] for w in ws) + 20)
        name = f'i{pg}' if pg <= 32 else f'n{pg}'
        pages[name] = (path, top, bot, ws, W)
    # press release: text PDF → raster + pdftotext boxes
    xml = subprocess.run(['pdftotext', '-bbox', PR, '-'], capture_output=True, text=True).stdout
    Hp = float(re.search(r'<page width="([\d.]+)" height="([\d.]+)"', xml).group(2))
    wsp = [(float(a), float(b), float(c), float(d), t) for a, b, c, d, t in re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>', xml)]
    subprocess.run(['pdftoppm', '-r', '220', '-png', '-singlefile', PR, '/home/claude/dl/doj/pr24'], check=True)
    imp = Image.open('/home/claude/dl/doj/pr24.png'); k = imp.height / Hp
    wsp = [(a * k, b * k, c * k, d * k, t) for a, b, c, d, t in wsp]
    imp.convert('RGB').save('/home/claude/dl/doj/pr24_r.jpg', quality=92)
    pages['pr24'] = ('/home/claude/dl/doj/pr24_r.jpg', max(0, min(w[1] for w in wsp) - 30), imp.height, wsp, imp.width)
    hl = {}
    for key, (pre, s, e) in P.items():
        path, top, bot, ws, W = pages[pre]
        r = find(ws, s, e)
        if not r: raise SystemExit(f'not found: {key}')
        hl[key] = [pre, round((r[0] - top) / (bot - top) - 0.004, 4), round((r[1] - top) / (bot - top) + 0.006, 4)]
    for name in sorted({v[0] for v in hl.values()}):
        path, top, bot, ws, W = pages[name]
        im = Image.open(path).convert('L').convert('RGB')
        x0, x1 = (0.06, 0.94) if name != 'pr24' else (0.03, 0.97)
        c = im.crop((int(x0 * W), int(top), int(x1 * W), int(bot)))
        c = c.resize((1480, int(c.height * 1480 / c.width)), Image.LANCZOS)
        c.save(f'{OUT}/{name}.jpg', quality=86)
    for name, (pg, box) in PHOTOS.items():
        im = Image.open(f'{SRC}/p-{pg:02d}.jpg').convert('RGB').crop(box)
        im = im.resize((1920, int(im.height * 1920 / im.width)), Image.LANCZOS).filter(ImageFilter.UnsharpMask(2, 60, 2))
        im.save(f'{OUT}/{name}.jpg', quality=90)
    json.dump(hl, open(os.path.join(HERE, 'hl.json'), 'w'), indent=1)
    print(json.dumps(hl))
