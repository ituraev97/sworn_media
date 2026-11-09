import sys, re
from playwright.sync_api import sync_playwright
src, out = sys.argv[1], sys.argv[2]
t = open(src, errors='ignore').read()
# keep only the main press-release content
m = re.search(r'(?is)(<h1.*?)(Return to Top|A copy of this press release)', t) or re.search(r'(?is)(FOR IMMEDIATE RELEASE.*?)(Return to Top|A copy of this press release)', t)
body = m.group(1) if m else t
title = re.search(r'(?is)<h1[^>]*>(.*?)</h1>', t)
h = re.findall(r'(?is)<(?:h1|h2|strong)[^>]*>(.*?)</(?:h1|h2|strong)>', t[:t.find('FOR IMMEDIATE RELEASE')+50])
html = f"""<html><head><style>*{{font-size:24px !important;line-height:1.5 !important;font-family:Georgia,serif !important;max-width:820px}} h1,h1 *{{font-size:38px !important;line-height:1.25 !important}} table,td,div{{width:auto !important}}</style></head><body style="margin:0;background:#fff"><div style="width:820px;padding:50px 60px;font-family:'Times New Roman',serif;font-size:21px;line-height:1.45;color:#111">{body}</div></body></html>"""
html = re.sub(r'(?is)<img[^>]*>', '', html)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 960, 'height': 1200}, device_scale_factor=2)
    pg.route('**/*', lambda r: r.abort() if r.request.url.startswith('http') else r.continue_())
    pg.set_content(html, wait_until='domcontentloaded'); pg.screenshot(path=out, full_page=True); b.close()
print(out)
