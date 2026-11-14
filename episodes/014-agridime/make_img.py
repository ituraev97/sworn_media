"""Rasterize public-domain U.S. government documents for SWORN 014 (United States v. Joshua Link & Jason Link — Agridime), crop, compute gold-highlight boxes (tesseract TSV).
Sources (local copies in /home/claude/dl):
  ssi    = Second Superseding Indictment, U.S. v. Link et al., No. 4:26-CR-051-P, Dkt. 168 (N.D. Tex. Sep 11, 2026) — attached to the USAO N.D. Tex. verdict release  [shown]
  wood   = Factual Resume, U.S. v. Jed Hansel Wood, Dkt. 63 (Mar 25, 2026) — USAO release attachment                                                                  [shown]
  tia    = Factual Resume, U.S. v. Tia Makenzie Link, Dkt. 116 (Jun 17, 2026)                                                                                          [shown]
  bang   = Factual Resume, U.S. v. Taylor Orris Bang (2026)                                                                                                             [shown]
  sec    = SEC v. Agridime LLC, Joshua Link and Jed Wood, No. 4:23-cv-01224-P, Complaint, Dkt. 1 (N.D. Tex. Dec 11, 2023) — allegations (RECAP gov.uscourts.txnd.384071) [shown]
  cftc   = CFTC v. Agridime LLC et al., No. 4:24-cv-0424-P, Final Judgment and Consent Order against Agridime, Dkt. 44 (Jun 10, 2025) (RECAP gov.uscourts.txnd.389685)  [shown]
  poster = FBI "Wanted by the FBI" poster, Joshua Robert Link (Feb 2026), attached to the USAO N.D. Tex. release of Feb 12, 2026 — FBI seal painted out              [shown]
Images from the USAO N.D. Tex. verdict release (Nov 11, 2026): gov't exhibit chart, salary table, feed table, barndominium photo — copied as published.
Victims are identified only as "Individual X" in the documents; no private names appear. Writes img/<name>.jpg and hl.json."""
import subprocess, os, json, csv, io, re, shutil
from PIL import Image, ImageDraw
D = '/home/claude/dl'; HI = '/home/claude/hi'
FILES = {'ssi': f'{D}/doj/ssi.pdf', 'wood': f'{D}/doj/fr_wood.pdf', 'tia': f'{D}/doj/fr_tia.pdf', 'bang': f'{D}/doj/fr_bang.pdf',
         'sec': f'{D}/recap/sec_1.pdf', 'cftc': f'{D}/recap/cftc_44.pdf', 'poster': f'{D}/doj/link_wanted.pdf'}
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, 'img')
def norm(t): return re.sub(r'[^a-z0-9]', '', t.lower())
def raster(src, page):
    base = f'{HI}/{src}-{page}'
    if not os.path.exists(base + '.png'):
        subprocess.run(['pdftoppm', '-r', '220', '-png', '-singlefile', '-f', str(page), '-l', str(page), FILES[src], base], check=True)
    return base + '.png'
def find(path, start, end):
    im = Image.open(path); H = im.size[1]
    tsv = path + '.tsv'
    if not os.path.exists(tsv):
        open(tsv, 'w').write(subprocess.run(['tesseract', path, '-', 'tsv'], capture_output=True, text=True).stdout)
    ws = [r for r in csv.DictReader(io.StringIO(open(tsv).read()), delimiter='\t', quoting=csv.QUOTE_NONE) if r['text'] and norm(r['text'])]
    nth = 1
    if start[:2] in ('2:', '3:'): nth, start = int(start[0]), start[2:]
    toks = [norm(w['text']) for w in ws]; s = [norm(x) for x in start.split() if norm(x)]; e = [norm(x) for x in end.split() if norm(x)]
    for i in range(len(toks)):
        if toks[i:i + len(s)] == s and (nth := nth - 1) == 0:
            for j in range(i, min(len(toks), i + 400)):
                if toks[j:j + len(e)] == e:
                    seg = ws[i:j + len(e)]
                    return round(min(int(w['top']) for w in seg) / H, 4), round(max(int(w['top']) + int(w['height']) for w in seg) / H, 4)
    raise SystemExit(f'not found in {path}: {start!r} … {end!r}\n' + ' '.join(toks)[:3000])
F = (0.03, 0.97, 0.04, 0.96)
jobs = {
 'ssi_1':  ('ssi', 1, 0.03, 0.60, 0.04, 0.96, [('JOSHUA ROBERT LINK', 'LINK'), ('SECOND SUPERSEDING INDICTMENT', 'INDICTMENT')]),
 'ssi_4':  ('ssi', 4, 0.03, 0.40, 0.04, 0.96, [('purchase” a steer or heifer', 'yearly profits.”')]),
 'ssi_6':  ('ssi', 6, *F, [('Executed cattle contracts with individual', 'their cattle contracts;')]),
 'ssi_10': ('ssi', 10, *F, [('I could offer you', 'a $1,000”'), ('where we really make the money', 'of the yield.”')]),
 'ssi_13': ('ssi', 13, *F, [('customer purchases cattle from us for $2,000 per head.', 'sell the beef”')]),
 'ssi_20': ('ssi', 20, *F, [('$2,728,000 of combined', 'jointly;'), ('$6,987,000 of commission', 'Bang;'), ('provided duplicative Electronic Identification', 'for each victim.')]),
 'ssi_22': ('ssi', 22, 0.03, 0.55, 0.04, 0.96, [('over 2,200 individual victims', 'earlier cattle purchasers')]),
 'ssi_35': ('ssi', 35, *F, [('124 head x $750 per head', 'only $93,000.')]),
 'ssi_36': ('ssi', 36, *F, [('Since we have a bred cow/pair', 'per head.'), ('Can you send us the lease', 'per month')]),
 'ssi_37': ('ssi', 37, *F, [('will have no choice', 'cover those bills.'), ('2:feed that grows out of the ground', 'of the ground'), ('$1,498,275.22', 'H2 Hummer;')]),
 'wood_5': ('wood', 5, *F, [('obtained over $220 million', 'United States')]),
 'tia_3':  ('tia', 3, *F, [('Agridime is regulated by the USDA', 'with the USDA.”'), ('Yes, that is correct', 'pay me 5500')]),
 'bang_4': ('bang', 4, 0.03, 0.62, 0.04, 0.96, [('$240,000 purchase price', 'within 9 months;')]),
 'sec_1':  ('sec', 1, 0.03, 0.97, 0.04, 0.96, [('active Ponzi scheme', 'perpetrated'), ('We know it sounds too good to be true.', 'be true.”')]),
 'sec_3':  ('sec', 3, *F, [('Joshua Link, age 30,', 'Gilbert, Arizona.')]),
 'sec_7':  ('sec', 7, *F, [('Have you ever wanted to make money', 'be true')]),
 'sec_9':  ('sec', 9, *F, [('In short, Agridime is operating a Ponzi scheme.', 'scheme.'), ('more than $123 million in principal', '$1.5 million')]),
 'cftc_5': ('cftc', 5, *F, [('Defendant Agridime shall pay restitution', '($102,936,904)')]),
 'poster': ('poster', 1, 0.0, 0.83, 0.0, 1.0, [('In reality, Agridime purchased only a fraction', 'of the cattle.')]),
}
hl = {}
if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True); os.makedirs(HI, exist_ok=True)
    only = os.environ.get('ONLY')
    if os.path.exists(os.path.join(HERE, 'hl.json')): hl = json.load(open(os.path.join(HERE, 'hl.json')))
    for name, (src, page, y0, y1, x0, x1, phrases) in jobs.items():
        if only and name not in only.split(','): continue
        p = raster(src, page)
        im = Image.open(p).convert('RGB')
        boxes = [find(p, s, e) for s, e in phrases]
        for r in boxes:
            if not (y0 <= r[0] and r[1] <= y1): raise SystemExit(f'phrase outside crop: {name} {r}')
        W, H = im.size
        if src == 'poster':  # paint the FBI seal out with the banner red
            d = ImageDraw.Draw(im); col = im.getpixel((int(0.95 * W), int(0.03 * H)))
            d.rectangle([0, 0, int(0.185 * W), int(0.137 * H)], fill=col)
        c = im.crop((int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H)))
        if src != 'poster': c = c.convert('L').convert('RGB')
        c = c.resize((1480, int(c.height * 1480 / c.width)), Image.LANCZOS)
        c.save(f'{OUT}/{name}.jpg', quality=88)
        hl[name] = [[round((a - y0) / (y1 - y0) - 0.008, 4), round((b - y0) / (y1 - y0) + 0.008, 4)] for a, b in boxes]
        print(name, c.size, hl[name])
    json.dump(hl, open(os.path.join(HERE, 'hl.json'), 'w'), indent=1)
    # face from the FBI poster (photo embedded in the PDF) and release images
    if not only:
        subprocess.run(['pdfimages', '-j', '-f', '1', '-l', '1', FILES['poster'], f'{HI}/fbi'], check=True)
        Image.open(f'{HI}/fbi-002.jpg').convert('RGB').save(f'{OUT}/link_face.jpg', quality=92)
        for a, b in [('pr_img1', 'rel_salary'), ('pr_img2', 'rel_chart'), ('pr_img3', 'rel_feed'), ('pr_img4', 'rel_barndo')]:
            Image.open(f'{D}/doj/{a}.png').convert('RGB').save(f'{OUT}/{b}.jpg', quality=92)
