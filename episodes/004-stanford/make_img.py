"""Rasterize U.S. government filings (pdftoppm -r 220), crop, and compute gold-highlight boxes.
Sources: D = RECAP PDFs from archive.org (see sources.md); SHOTS = archived justice.gov releases rendered to PNG.
Writes img/<name>.jpg and hl.json {name: [[y0,y1],...]} with highlight y-ranges as fractions of the crop."""
import subprocess, os, json
from PIL import Image
from findy import find
D='/home/claude/research/d'; HI='/home/claude/research/hi'; SHOTS='/home/claude/research/shots'
HERE=os.path.dirname(os.path.abspath(__file__)); OUT=os.path.join(HERE,'img')
BR='gov.uscourts.ca5.12-20411.00502955799.0.pdf'   # Brief of the United States, 5th Cir. No. 12-20411, Mar 3, 2015
CMP='gov.uscourts.txnd.184049.48.0.pdf'            # SEC First Amended Complaint, N.D. Tex. 3:09-cv-298, Feb 27, 2009
RCV='gov.uscourts.txnd.184049.10.0.pdf'            # Order Appointing Receiver, Feb 16, 2009 (entered Feb 17)
jobs = {
 # name: (pdf, page, y0, y1, [(start, end) phrases to highlight])
 'brief_cover':   (BR, 1, 0.03, 0.60, [('BRIEF OF THE UNITED STATES', 'UNITED STATES')]),
 'brief_counts':  (BR, 22, 0.45, 0.93, [('A 14-count', 'following')]),
 'brief_case':    (BR, 23, 0.05, 0.50, [('After a 30-day', 'Order of Forfeiture')]),
 'brief_origin':  (BR, 24, 0.40, 0.93, [('SGC, headquartered', 'regulated')]),
 'brief_profits': (BR, 30, 0.30, 0.93, [('Stanford advised Davis', 'annual report')]),
 'brief_montserrat': (BR, 31, 0.20, 0.80, [('On November', 'revoke')]),
 'brief_piggy':   (BR, 33, 0.12, 0.80, [('By the end of 2008, over', 'renovating')]),
 'brief_tier':    (BR, 42, 0.05, 0.52, [('Stanford siphoned', 'lifestyle')]),
 'brief_hewlett': (BR, 44, 0.08, 0.76, [('Beginning on Montserrat,', 'GX 100-120).'), ('Stanford paid more', 'fees he paid him')]),
 'brief_king':    (BR, 45, 0.08, 0.72, [('Leroy King became', '7091).'), ('Stanford and King sealed', '7090).')]),
 'brief_sec2005': (BR, 46, 0.10, 0.80, [('In 2005, the SEC', '(GX 668).'), ('King immediately shared', '7125-7126).')]),
 'brief_burn':    (BR, 47, 0.05, 0.52, [('After the SEC investigation', '8139).')]),
 'brief_liquid':  (BR, 47, 0.48, 0.93, [('In October 2008,', 'than it')]),
 'brief_541':     (BR, 49, 0.05, 0.58, [('In December 2008, Stanford', '(GX 138).'), ('Stanford admitted to Davis', 'had occurred')]),
 'brief_hole':    (BR, 53, 0.05, 0.92, [('By the end of December 2008,', 'GX 1607).'), ('Although Stanford faced', '14014).')]),
 'cmp_cover':     (CMP, 1, 0.03, 0.86, [('1. For', 'fraudulent conduct.')]),
 'cmp_reverse':   (CMP, 8, 0.40, 0.80, [('37. SIB’s', 'actually earn.')]),
 'cmp_541':       (CMP, 9, 0.17, 0.52, [('40. In its', '2008.'), ('41. This', 'acquired.')]),
}
manual = {
 # scanned order (no text layer): highlight boxes measured on the page raster
 'rcv':        (RCV, 1, 0.03, 0.66, [(0.415, 0.440)]),
}
hl = {}
def raster(pdf, page):
    base = f'{HI}/{os.path.basename(pdf)}-{page}'
    if not os.path.exists(base + '.png'):
        subprocess.run(['pdftoppm','-r','220','-png','-singlefile','-f',str(page),'-l',str(page),f'{D}/{pdf}',base],check=True)
    return Image.open(base + '.png').convert('RGB')
def save(name, im, y0, y1, boxes):
    W, H = im.size
    c = im.crop((int(0.04*W), int(y0*H), int(0.96*W), int(y1*H)))
    c = c.resize((1480, int(c.height*1480/c.width)), Image.LANCZOS)
    c.save(f'{OUT}/{name}.jpg', quality=88)
    hl[name] = [[round((a-y0)/(y1-y0) - 0.008, 4), round((b-y0)/(y1-y0) + 0.008, 4)] for a, b in boxes]
    print(name, c.size, hl[name])
for name, (pdf, page, y0, y1, phrases) in jobs.items():
    boxes = []
    for s, e in phrases:
        r = find(f'{D}/{pdf}', page, s, e)
        if not r: raise SystemExit(f'phrase not found: {name} {s!r}')
        boxes.append(r)
    save(name, raster(pdf, page), y0, y1, boxes)
for name, (pdf, page, y0, y1, boxes) in manual.items():
    save(name, raster(pdf, page), y0, y1, boxes)
# archived justice.gov releases, rendered from the archive HTML (images disabled, so no seal)
for name, (src, y0, y1, boxes) in {
    'pr_conv':  ('pr_conv',  0.015, 0.392, [(0.3479, 0.3832)]),
    'pr_sent':  ('pr_sent',  0.004, 0.172, [(0.0560, 0.0816)]),
    'pr_judge': ('pr_sent',  0.284, 0.426, [(0.2905, 0.3068)]),
}.items():
    im = Image.open(f'{SHOTS}/{src}.png').convert('RGB'); W, H = im.size
    c = im.crop((0, int(y0*H), W, int(y1*H))); c = c.resize((1480, int(c.height*1480/c.width)), Image.LANCZOS)
    c.save(f'{OUT}/{name}.jpg', quality=88)
    hl[name] = [[round((a-y0)/(y1-y0) - 0.008, 4), round((b-y0)/(y1-y0) + 0.008, 4)] for a, b in boxes]
    print(name, c.size, hl[name])
json.dump(hl, open(os.path.join(HERE, 'hl.json'), 'w'), indent=1)
