"""SWORN 022 — Feeding Our Future juror-bribery plot, United States v. Abdiaziz Shafii Farah et al. (D. Minn. 24-cr-173-ECT-DLM).
Documents shown (federal court records / U.S. government works, public domain), all with a text layer (word boxes from pdftotext -bbox):
  a277 = Gov't position re sentencing, Ladan Mohamed Ali, Dkt. 277 (Nov 6, 2026)      RECAP gov.uscourts.mnd.216393.277.0
  a216 = Gov't position re sentencing, Abdiaziz Shafii Farah, Dkt. 216 (Jul 3, 2026)  RECAP gov.uscourts.mnd.216389.216.0
  a251 = Gov't position re sentencing, Said Shafii Farah, Dkt. 251 (Sep 14, 2026)     RECAP gov.uscourts.mnd.216389.251.0
  a243 = Gov't position re sentencing, Abdimajid Nur, Dkt. 243 (Sep 4, 2026)          RECAP gov.uscourts.mnd.216389.243.0
  j231 = Judgment, Abdiaziz Farah, Dkt. 231 (Jul 24, 2026);  m230 / m207 = sentencing minutes (Jul 22, 2026 / Mar 4, 2026)
  q579 = Judgment of acquittal, Said Shafii Farah, 22-cr-124 Dkt. 579 (Jun 12, 2024)   RECAP gov.uscourts.mnd.203011.579.0
  n929 = Gov't position re sentencing, Abdimajid Nur, 22-cr-124 Dkt. 929 (Nov 6, 2025) RECAP gov.uscourts.mnd.203010.929.0
  pr24 / prali / prnur = USAO D. Minn. releases (Jun 26, 2024; Sep 5, 2024; Jul 23, 2024) re-typeset as text (txt2pdf.js, no seal).
Exhibit photos (government trial exhibits reproduced inside n929): ex_store (Empire Cuisine & Market, Gov't Ex. A-1/H-119),
  ex_nurcons (Gov't summary chart: Nur Consulting LLC deposits), ex_texts (WhatsApp chart, Gov't Ex. H-51).
Writes img/<name>.jpg and hl.json: hl[key] = [img_name, y0, y1] (fractions of the image height)."""
import subprocess, os, json, re
from PIL import Image, ImageDraw, ImageFilter
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, 'img')
R = '/home/claude/work/fof/dl/r/'; R2 = '/home/claude/work/fof/dl/r2/'; D = '/home/claude/dl/doj/'
DOCS = {'a277': R + 'gov.uscourts.mnd.216393.277.0.pdf', 'a216': R + 'gov.uscourts.mnd.216389.216.0.pdf',
        'a251': R + 'gov.uscourts.mnd.216389.251.0.pdf', 'a243': R + 'gov.uscourts.mnd.216389.243.0.pdf',
        'j231': R + 'gov.uscourts.mnd.216389.231.0.pdf', 'm230': R + 'gov.uscourts.mnd.216389.230.0.pdf',
        'm207': R + 'gov.uscourts.mnd.216392.207.0.pdf', 'q579': R2 + 'gov.uscourts.mnd.203011.579.0.pdf',
        'n929': R2 + 'gov.uscourts.mnd.203010.929.0.pdf',
        'pr24': D + 'pr24.pdf', 'prali': D + 'prali.pdf', 'prnur': D + 'prnur.pdf'}
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
# key: (doc, start phrase, end phrase) — searched on every page of the doc; image = <doc>_p<n>
P = {
 'a_jury': ('a277', 'On April 22, 2024, jury selection began', 'plans to bribe her.'),
 'a_target': ('a216', 'The defendant quickly identified', 'only person of color on the jury'),
 'a_getto': ('a216', 'The defendant concluded', 'I’m serious for real.'),
 'a_recruit': ('a277', 'Soon thereafter, Mr. Nur recruited Ms. Ali', 'plan and deliver the bribe.'),
 'a_follow': ('a277', 'On May 31, 2024,', 'over the ensuing three days.'),
 'a_gps': ('a216', 'Ladan continued to', 'surveillance easier.'),
 'a_bar': ('a277', 'On June 1, 2024, Ms. Ali told Mr. Nur', 'return to Seattle.'),
 'a_fabricated': ('a277', 'Ms. Ali fabricated this entire interaction.', 'return to Seattle.'),
 'a_hawala': ('a251', 'The defendant collected a total', 'Karmel Mall, in Minneapolis.'),
 'a_ready': ('a216', 'On June 2, 2024, the defendant sent an encrypted', '$200,000 in cash.'),
 'a_stole': ('a277', 'On her way to meet with Abdulkarim', 'for herself.'),
 'a_target2': ('a216', 'Abdulkadir first drove Ladan', 'Juror 52’s house.'),
 'a_present': ('a216', 'The video shows Ladan approach', 'if she voted not'),
 'a_done': ('a243', 'Ladan texted Mr. Nur', '“It’s done babe.”'),
 'a_delete': ('a216', 'The defendant forwarded', 'money for her family.”'),
 'a_reported': ('a216', 'To her credit, Juror 52', 'surrender his phone to law'),
 'a_reset': ('a216', 'however, the defendant conducted a factory reset', 'evidence of the bribe.'),
 'a_note': ('a243', 'A deleted note was later recovered', '“convince other jurors.”'),
 'a_ups': ('a277', 'Before leaving, she put', 'home in Seattle.'),
 'a_prints': ('a277', 'Ms. Ali’s fingerprints were later found', 'hotel in Minneapolis.'),
 'a_verdict': ('a216', 'The jury returned its verdict on June 7, 2024', 'on August 6, 2025.'),
 'a_ironic': ('a251', 'The jury returned its verdict on June 7, 2024', 'on all counts.'),
 'a_saidplea': ('a251', 'One year later, on August 21, 2025', 'bribing a juror.'),
 'a_democracy': ('a277', 'It is not', 'democracy is threatened.'),
 'a_forsale': ('a277', 'the public that justice is not', 'very heavy price.'),
 'a_nurverdict': ('a243', 'The jury returned its verdict on June 7, 2024', 'on November'),
 'q_acq': ('q579', 'The Defendant was found not guilty', 'bond exonerated.'),
 'j_count': ('j231', '18:201 BRIBERY OF A JUROR', '06/02/2024'),
 'j_120': ('j231', '120 months as to count 2', 'imposed in 22-CR-124'),
 'm_57': ('m207', 'Count No.', '57 months'),
 'n_largest': ('n929', 'Defendant Abdimajid Nur participated in the largest', 'staggering nature of the fraud'),
 'n_meals': ('n929', 'At their fraudulent', 'March 2021 alone.'),
 'n_sites': ('n929', 'As the Court heard', 'vacant'),
 'n_homework': ('n929', 'Nur paid $12,000 to a company called', 'exams.'),
 'p_hallmark': ('prali', 'Prior to the meeting, Ali purchased two Hallmark', 'one of the Hallmark gift bags.'),
 'p_insisted': ('prali', 'Abdulkarim Farah insisted that he drive', 'all of the bribe money.'),
 'p_80k': ('prali', 'Ali received $200,000 in cash from Nur', 'for herself.'),
 'p_list': ('pr24', 'The conspirators drafted a list of instructions', 'motivated by racial animus.'),
 'p_youngest': ('pr24', 'As part of the scheme, the conspirators decided to target Juror 52', 'only juror of color.'),
 'p_presumed': ('pr24', 'An indictment is merely an allegation', 'court of law.'),
}
if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True); hl = {}; used = {}
    cache = {k: words(v) for k, v in DOCS.items()}
    for key, (doc, s, e) in P.items():
        r = None
        for pi, (W, H, ws) in enumerate(cache[doc]):
            if doc not in ('pr24', 'prali', 'prnur'): ws = [w for w in ws if w[1] > 0.06 * H]   # drop ECF header
            r = find(ws, s, e)
            if r: break
        if not r: print('NOT FOUND', key); continue
        name = f'{doc}_p{pi + 1}'; used[name] = (doc, pi, W, H, ws)
        hl[key] = [name, r]
    for name, (doc, pi, W, H, ws) in used.items():
        png = f'/home/claude/work/fof/ras/{name}'
        os.makedirs(os.path.dirname(png), exist_ok=True)
        subprocess.run(['pdftoppm', '-r', '200', '-png', '-singlefile', '-f', str(pi + 1), '-l', str(pi + 1), DOCS[doc], png], check=True)
        im = Image.open(png + '.png').convert('L').convert('RGB'); k = im.height / H
        top = max(0, min(w[1] for w in ws) * k - 30); bot = min(im.height, max(w[3] for w in ws) * k + 24)
        x0, x1 = (0.07, 0.93) if not doc.startswith('pr') else (0.02, 0.98)
        c = im.crop((int(x0 * im.width), int(top), int(x1 * im.width), int(bot)))
        c = c.resize((1480, int(c.height * 1480 / c.width)), Image.LANCZOS); c.save(f'{OUT}/{name}.jpg', quality=86)
        for key, v in hl.items():
            if v[0] == name and isinstance(v[1], tuple):
                y0, y1 = v[1]; hl[key] = [name, round((y0 * k - top) / (bot - top) - 0.006, 4), round((y1 * k - top) / (bot - top) + 0.008, 4)]
    # exhibit photos from n929 (pdfimages -png → /home/claude/work/fof/dl/r2/i929/x-NNN.png)
    X = R2 + 'i929/'
    Image.open(X + 'x-000.png').convert('RGB').save(f'{OUT}/ex_store.jpg', quality=90)
    ch = Image.open(X + 'x-012.png').convert('RGB'); print('checks', ch.size)
    ch.save(f'{OUT}/ex_nurcons.jpg', quality=90)
    Image.open(X + 'x-001.png').convert('RGB').save(f'{OUT}/ex_texts.jpg', quality=90)
    json.dump(hl, open(os.path.join(HERE, 'hl.json'), 'w'), indent=1)
    print(json.dumps(hl))
