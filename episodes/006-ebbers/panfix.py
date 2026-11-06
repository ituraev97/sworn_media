"""Keep each doc highlight inside the visible frame (stage.html geometry: long frame 1000x710, short 936x587)."""
from PIL import Image
import os
HERE = os.path.dirname(os.path.abspath(__file__))
def fix(lines, mode):
    fw, fh = (1000, 710) if mode == 'long' else (936, 587)
    for ln in lines:
        s = ln.get('scene')
        if not s or s.get('type') != 'doc' or not s.get('hl'): continue
        w, h = Image.open(os.path.join(HERE, s['img'])).size
        vis = fh / (h * fw / w)
        maxpan = max(0.0, 1 - vis)
        y, hh = s['hl'][1], s['hl'][3]
        p0, p1 = s.get('pan', [0, 0.12])
        ok = all(y >= p0 + (p1 - p0) * p - 1e-6 and y + hh <= p0 + (p1 - p0) * p + vis * 0.97 for p in (0.35, 0.6, 1.0))
        if ok: continue
        mid = y + hh / 2 - vis / 2 if hh < vis * 0.9 else y - 0.02
        a = min(max(0.0, mid - 0.03), maxpan); b = min(max(0.0, mid + 0.03), maxpan)
        if hh < vis * 0.9: b = min(b, y); a = min(a, b)
        s['pan'] = [round(a, 3), round(b, 3)]
    return lines
