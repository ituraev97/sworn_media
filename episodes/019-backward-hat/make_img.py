"""SWORN 019 — United States v. Phillip Patrick Williams and Devin Allen Johnson (S.D.N.Y., sealed complaint sworn Nov 17, 2026,
unsealed Nov 18, 2026). Documents shown (U.S. government works, public domain):
  complaint pages 1–9 = the criminal complaint (HSI Special Agent Robert Fanesi's affidavit), attached to the USAO S.D.N.Y. release
                        (justice.gov/usao-sdny/media/1472946/dl), text layer; page 9 is cropped above the signature block.
  pr                  = USAO S.D.N.Y. press release of Nov 18, 2026, saved as innerText (pw_pdf.js) and re-typeset as text (txt2pdf.js:
                        no seal, logo or images).
Rasterized with pdftoppm -r 220; highlight boxes from pdftotext -bbox. Writes img/<name>.jpg and hl.json:
  hl[key] = [img_name, y0, y1]  (fractions of the image height)."""
import subprocess, os, json, re
from PIL import Image
D = '/home/claude/dl/bh/doj'; HI = '/home/claude/hi19'
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, 'img')
def norm(t): return re.sub(r'[^a-z0-9]', '', t.lower())
# key: (start phrase, end phrase) — searched on every page of the complaint, then in the press release ("pr:" prefix)
P = {
 'caption': ('UNITED STATES OF AMERICA', 'Defendants.'),
 'ov_600': ('Since its founding in or about July 2022', 'over 2,000 investors.'),
 'ov_6pct': ('Backward Hat’s reported rate of return', 'their money in a year.'),
 'ov_illusory': ('Those outsized purported returns', 'DEVIN ALLEN JOHNSON, the defendant.'),
 'cofounders': ('Backward Hat was co-founded by', 'corporate entities they each controlled.'),
 'twelve': ('Backward Hat maintained more', 'placed investor money.'),
 'deck': ('Backward Hat marketed its funds', 'at a staggering rate.”'),
 'website': ('The Backward Hat website similarly', 'other arbitrage'),
 'auditor': ('Backward Hat hired', '“Quality of'),
 'titles': ('The audit report described', 'Strategy” of Backward Hat.'),
 'integrity': ('The audit report and accompanying', 'all audited'),
 'sent_audit': ('on or about November 14, 2025', 'later invested in Backward Hat.'),
 'same_rate': ('all of the funds operated by Backward Hat purportedly earned', 'never fell below 9.5%.'),
 'dashboard': ('between in or around October', 'between 6.01% and 7.21%.'),
 'set_rate': ('each month, WILLIAMS', 'investor’s investment into Backward Hat.'),
 'aug5': ('on or about August 5, 2026', 'WILLIAMS responded with “6.62,”'),
 'may14': ('May 14, 2026, the following exchange', 'bumped it up a bit'),
 'ponzi200': ('Of that money, at least approximately $200 million', 'legitimate investment profits.'),
 'gp200': ('More than approximately $200 million', 'JOHNSON, the defendant.'),
 'minimal': ('Only minimal funds', 'forex trading.'),
 'k300': ('on or about February 12, 2026', 'Backward Hat bank account.'),
 'cofounded': ('co-founded a company', 'CEO of the Auditor.'),
 'may29': ('On or about May 29, 2026, the CEO of the Auditor emailed', 'remain unresolved from the past several years.”'),
 'two_m': ('he would have “accumulated no less', 'personal BH'),
 'aicap': ('Since at least in or around August 2025', 'affiliated with Backward Hat.'),
 'aicap_mgr': ('In marketing materials created', 'Strategic Advisor.”'),
 'aicap_trades': ('a data room created to market AI Capital', 'August 4, 2024.'),
 'aicap_75': ('In a presentation to a prospective AI Capital investor', 'any investor money.'),
 'summer': ('In or around the summer of 2026, the Backward Hat Ponzi scheme', 'investor withdrawal requests.'),
 'oct12': ('On or about October 12, 2026', 'incoming transfers.”'),
 'oct19': ('On or about October 19, 2026', 'significant delays.”'),
 'nov13': ('On or about November 13, 2026', 'third-party identity validator.”'),
 'dissipated': ('he was, in actuality', 'dissipated most investor assets.'),
 'uc1': ('an undercover employee with the Internal Revenue', 'accepting new investors at the moment.”'),
 'nov6': ('In addition, based on my review of an email sent on or', 'match it quickly.”'),
 'count3': ('From at least in or about July 2022 up to and including the present, in the Southern', 'a person'),
 'p2_130': ('WILLIAMS transferred and caused to be transferred over $130 million', 'accounts under WILLIAMS’s control.'),
 'pr:arrest': ('WILLIAMS was arrested this morning', 'District of Arizona.'),
 'pr:mcdonald': ('“These charges—alleging', 'white collar fraud,”'),
 'pr:hardq': ('When someone promises extraordinary', 'someone else’s expense.”'),
 'pr:max': ('WILLIAMS, 51, of Kokomo', 'maximum sentence of five years in prison.'),
 'pr:presumed': ('The charges contained in the Complaint', 'proven guilty.'),
 'pr:victims': ('If you or someone you know is a victim', 'please visit:'),
}
def words(pdf, page):
    xml = subprocess.run(['pdftotext', '-bbox', '-f', str(page), '-l', str(page), pdf, '-'], capture_output=True, text=True).stdout
    H = float(re.search(r'<page width="([\d.]+)" height="([\d.]+)"', xml).group(2))
    ws = [(float(a), float(b), float(c), float(d), t) for a, b, c, d, t in re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>', xml)]
    return H, [w for w in ws if norm(w[4])]
def find(ws, start, end):
    toks = [norm(w[4]) for w in ws]; s = [norm(x) for x in start.split() if norm(x)]; e = [norm(x) for x in end.split() if norm(x)]
    for i in range(len(toks)):
        if toks[i:i + len(s)] == s:
            for j in range(i, min(len(toks), i + 700)):
                if toks[j:j + len(e)] == e:
                    seg = ws[i:j + len(e)]
                    return (min(w[1] for w in seg), max(w[3] for w in seg))
    return None
if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True); os.makedirs(HI, exist_ok=True)
    pages = {}  # img name -> (pdf, page, top, bot, ws, H)
    cpdf = f'{D}/complaint.pdf'
    for pg in range(1, 10):
        H, ws = words(cpdf, pg)
        top = max(0, min(w[1] for w in ws) - 24)
        bot = max(w[3] for w in ws) + 20
        if pg == 9:  # stop above the signature block
            sig = [w[1] for w in ws if norm(w[4]) == 's']
            bot = (min(sig) - 14) if sig else bot
        pages[f'c{pg}'] = (cpdf, pg, top, bot, ws, H)
    H, ws = words(f'{D}/pr.pdf', 1)
    tk = [norm(w[4]) for w in ws]
    cut = [ws[i][1] for i in range(len(ws)) if tk[i] == 'contact']
    pages['pr'] = (f'{D}/pr.pdf', 1, min(w[1] for w in ws) - 30, (min(cut) - 10) if cut else max(w[3] for w in ws) + 30, ws, H)
    for name, (pdf, pg, top, bot, ws, H) in pages.items():
        base = f'{HI}/{name}'
        subprocess.run(['pdftoppm', '-r', '220', '-png', '-singlefile', '-f', str(pg), '-l', str(pg), pdf, base], check=True)
        im = Image.open(base + '.png').convert('L').convert('RGB'); W, HH = im.size; k = HH / H
        x0, x1 = (0.07, 0.93) if name != 'pr' else (0.03, 0.97)
        c = im.crop((int(x0 * W), max(0, int(top * k)), int(x1 * W), min(HH, int(bot * k))))
        c = c.resize((1480, int(c.height * 1480 / c.width)), Image.LANCZOS)
        c.save(f'{OUT}/{name}.jpg', quality=88); print(name, c.size)
    hl = {}
    for key, (s, e) in P.items():
        cands = ['pr'] if key.startswith('pr:') else [f'c{i}' for i in range(1, 10)]
        hit = None
        for name in cands:
            pdf, pg, top, bot, ws, H = pages[name]
            r = find(ws, s, e)
            if r:
                hit = [name, round((r[0] - top) / (bot - top) - 0.004, 4), round((r[1] - top) / (bot - top) + 0.004, 4)]; break
        if not hit:
            raise SystemExit(f'not found: {key}')
        hl[key] = hit
    json.dump(hl, open(os.path.join(HERE, 'hl.json'), 'w'), indent=1)
    print(json.dumps(hl))
