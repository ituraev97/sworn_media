"""SWORN 015 — United States v. Jiandong Chen ("Little Tiger"), S.D. Cal. 24-cr-1317-RSH.
Documents shown (all U.S. government works, public domain):
  U.S. Attorney's Office, S.D. Cal. press releases, printed from justice.gov to PDF with Playwright (text only:
  no seal, no logo, no third-party images) and rasterized with pdftoppm -r 220:
    ind      = Jul 31, 2024  "Five Chinese Nationals Indicted for Scamming Seniors Out of More Than $27 Million"
    wangplea = Jan 15, 2026  Zhao Wang pleads guilty
    chenplea = Apr 2, 2026   Jiandong Chen pleads guilty
    wangsent = May 8, 2026   Zhao Wang sentenced to 151 months
    sent     = Nov 13, 2026  Jiandong Chen sentenced to 6 1/2 years
    ring65   = Aug 27, 2025  "YouTube Scambaiters Help Dismantle $65 Million Multinational Fraud Ring"
    final65  = Oct 26, 2026  final defendants plead guilty in the $65M ring
  DOJ sentencing slides published in the Nov 13, 2026 release ("Package Videos", 2/22/2023, 2/23/2023, 5/19/2023):
  DOJ seal painted out. The Trilogy Media banner/thumbnail images in that release are third-party works: NOT used.
Highlight boxes come from pdftotext -bbox. Writes img/<name>.jpg and hl.json."""
import subprocess, os, json, re
from PIL import Image, ImageDraw, ImageFilter
D = '/home/claude/dl/doj'; C = '/home/claude/dl/chen'; HI = '/home/claude/hi15'
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, 'img')
def norm(t): return re.sub(r'[^a-z0-9]', '', t.lower())
P = {
 'sent': [('Jiandong Chen, aka', 'the United States.'), ('Chen was confronted in a viral', 'sentencing hearing.'),
          ('Chen, a Chinese national, moved', 'money laundering scheme'), ('despite being arrested by local', 'victim packages.'),
          ('his time during the conspiracy involved', 'evade law enforcement.'), ('These victims', 'even more.'),
          ('Before pronouncing the 78-month', 'United States.'), ('more than just money', 'thing to suffer.'),
          ('Chen also admitted that he and his', 'Las Vegas, Nevada.'), ('as evidenced by numerous videos', 'viral YouTube video.')],
 'ind': [('An indictment was unsealed today', '2,000 seniors.'), ('about 60 federal, state and local', 'searched their homes.'),
         ('The defendants provided fake names', 'using fake IDs.'), ('Jiandong Chen, aka', 'Pomona, CA'), ('We urge everyone to use caution', 'or a computer.')],
 'wangplea': [('Wang admitted that typically each day', 'his co-conspirators.'), ('In his plea agreement, Wang admitted', 'the fraud scheme.')],
 'chenplea': [('One of the most frequent scams', 'received any money.'), ('In one such instance captured', 'scam organization.'),
              ('Chen admitted that he used fraudulent', 'bulk cash.'), ('Victims received unsolicited', 'call centers.'),
              ('In many instances, the conspirators', 'carry on the scams.')],
 'wangsent': [('was sentenced in federal court today to 151 months', 'the United States.'), ('In sentencing papers, the government argued', 'Wang’s phone.'),
              ('Their vulnerability was not incidental.', 'came to be scammed.'), ('The wife and daughter of an', 'on this planet.'),
              ('called the scope of the fraud', 'reprehensible.')],
 'ring65': [('Twenty-eight alleged members', 'life savings.'), ('Not all heroes wear capes.', 'YouTube channels'),
            ('That memo says that the YouTubers', 'role in the scheme.'), ('Videos posted in 2020 and 2021 helped', 'named in the indictments.')],
 'final65': [('The last of 25 defendants', 'YouTube scambaiters.'), ('admitted to being in YouTube videos', 'criminal activity.'),
             ('The investigation started in December 2020', '$135,000 in cash.'), ('booked short-term rentals in a hub-and-spoke', 'shorter stays.')],
}
def words(pdf):
    xml = subprocess.run(['pdftotext', '-bbox', '-f', '1', '-l', '1', pdf, '-'], capture_output=True, text=True).stdout
    H = float(re.search(r'<page width="([\d.]+)" height="([\d.]+)"', xml).group(2))
    ws = [(float(a), float(b), float(c), float(d), t) for a, b, c, d, t in re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>', xml)]
    return H, [w for w in ws if norm(w[4])]
def find(ws, start, end):
    toks = [norm(w[4]) for w in ws]; s = [norm(x) for x in start.split() if norm(x)]; e = [norm(x) for x in end.split() if norm(x)]
    for i in range(len(toks)):
        if toks[i:i + len(s)] == s:
            for j in range(i, min(len(toks), i + 600)):
                if toks[j:j + len(e)] == e:
                    seg = ws[i:j + len(e)]
                    return min(w[1] for w in seg), max(w[3] for w in seg)
    raise SystemExit(f'not found: {start!r} … {end!r}\n' + ' '.join(toks)[:2500])
hl = {}
if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True); os.makedirs(HI, exist_ok=True)
    for name, phrases in P.items():
        pdf = f'{D}/{name}.pdf'
        H, ws = words(pdf)
        top = min(w[1] for w in ws) - 30; bot = max(w[3] for w in ws if not norm(w[4]).startswith('thechargesandallegations')) + 30
        # stop before the "Contact" block
        tk = [norm(w[4]) for w in ws]
        cut = [ws[i][1] for i in range(len(ws) - 1) if tk[i] == 'contact' and tk[i + 1] == 'kelly']
        if cut: bot = min(bot, min(cut) - 10)
        base = f'{HI}/{name}'
        if not os.path.exists(base + '.png'):
            subprocess.run(['pdftoppm', '-r', '220', '-png', '-singlefile', '-f', '1', '-l', '1', pdf, base], check=True)
        im = Image.open(base + '.png').convert('L').convert('RGB'); W, HH = im.size; k = HH / H
        y0, y1 = max(0, int(top * k)), min(HH, int(bot * k))
        c = im.crop((int(0.03 * W), y0, int(0.97 * W), y1))
        c = c.resize((1480, int(c.height * 1480 / c.width)), Image.LANCZOS)
        c.save(f'{OUT}/{name}.jpg', quality=88)
        boxes = [find(ws, s, e) for s, e in phrases]
        hl[name] = [[round((a - top) / (bot - top) - 0.004, 4), round((b - top) / (bot - top) + 0.004, 4)] for a, b in boxes]
        print(name, c.size, hl[name])
    json.dump(hl, open(os.path.join(HERE, 'hl.json'), 'w'), indent=1)
    # DOJ sentencing slides: paint the DOJ seal (top-left) with the banner navy
    for src, dst, wb in [('picture2_1_5.png', 'slide_0222', 0.195), ('picture3_1_2.png', 'slide_0223', 0.2), ('picture4_1.png', 'slide_0519', 0.228)]:
        im = Image.open(f'{C}/{src}').convert('RGB'); W, H = im.size; d = ImageDraw.Draw(im)
        col = im.getpixel((int(0.30 * W), 6))
        bh = next(y for y in range(5, H) if sum(im.getpixel((int(0.30 * W), y))) > 600)  # bottom of the navy banner
        d.rectangle([0, 0, int(0.135 * W), bh - 1], fill=col)
        d.rectangle([0, bh, int(0.135 * W), int(wb * H)], fill=im.getpixel((int(0.15 * W), int(0.19 * H))))
        im = im.resize((W * 3, H * 3), Image.LANCZOS)
        im.save(f'{OUT}/{dst}.jpg', quality=92); print(dst, im.size)
    # face: the ID-style photo of Chen on the DOJ slide (labelled "Jiandong CHEN aka 'Little Tiger'")
    im = Image.open(f'{C}/picture2_1_5.png').convert('RGB')
    f = im.crop((12, 56, 78, 134))
    f = f.resize((f.width * 9, f.height * 9), Image.LANCZOS).filter(ImageFilter.UnsharpMask(radius=4, percent=60, threshold=2))
    f.save(f'{OUT}/chen_face.jpg', quality=92); print('chen_face', f.size)
    # cash-counting frame (right-hand third of the 2/22/2023 slide) for B-roll / thumbnails
    im = Image.open(f'{C}/picture2_1_5.png').convert('RGB')
    cash = im.crop((226, 44, 362, 284)).resize((136 * 6, 240 * 6), Image.LANCZOS)
    cash.save(f'{OUT}/cash_count.jpg', quality=92); print('cash_count', cash.size)
    # thumbnail panel: whole face in the top ~2/3 (the caption covers the bottom), blurred fill around it
    face = Image.open(f'{OUT}/chen_face.jpg')
    bg = face.resize((720, 720), Image.LANCZOS).filter(ImageFilter.GaussianBlur(28))
    fh = 540; fw = int(face.width * fh / face.height)
    bg.paste(face.resize((fw, fh), Image.LANCZOS), ((720 - fw) // 2, 0))
    bg.save(f'{OUT}/chen_panel.jpg', quality=92); print('chen_panel', bg.size)
