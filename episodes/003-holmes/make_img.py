import subprocess, os
from PIL import Image
D='/home/claude/research/d'; HI='/home/claude/research/hi'; OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'img')
P='gov.uscourts.cand.327949.%s.0.pdf'
jobs = {
 # name: (docket no, page, x0, x1, y0, y1)
 'indictment': ('1',1,0.04,0.96,0.03,0.40),
 'tsi_cover': ('469',1,0.04,0.96,0.03,0.62),
 'tsi_null': ('469',6,0.04,0.96,0.03,0.62),
 'tsi_counts': ('469',10,0.04,0.96,0.03,0.88),
 'verdict1': ('1235',1,0.04,0.96,0.20,0.93),
 'verdict2': ('1235',2,0.04,0.96,0.03,0.69),
 'memo_intro': ('1643',6,0.04,0.96,0.03,0.45),
 'memo_twelve': ('1643',8,0.04,0.96,0.03,0.45),
 'memo_logos': ('1643',8,0.04,0.96,0.40,0.86),
 'memo_rev': ('1643',9,0.04,0.96,0.03,0.70),
 'memo_texts': ('1643',12,0.04,0.96,0.03,0.34),
 'memo_cms': ('1643',17,0.04,0.96,0.40,0.97),
 'memo_wsj': ('1643',18,0.04,0.96,0.20,0.60),
 'memo_cover': ('1643',19,0.04,0.96,0.25,0.55),
 'memo_trial': ('1643',20,0.04,0.96,0.03,0.27),
 'minutes': ('1660',1,0.04,0.96,0.03,0.80),
 'sent_order': ('1712',22,0.04,0.96,0.40,0.96),
 'judgment': ('1716',1,0.03,0.97,0.03,0.66),
 'bail': ('1757',1,0.04,0.96,0.03,0.80),
 'restitution': ('1760',1,0.04,0.96,0.20,0.80),
 'resent': ('1816',10,0.04,0.96,0.03,0.60),
 'ca9': ('1802',8,0.04,0.96,0.03,0.96),
}
for name,(n,p,x0,x1,y0,y1) in jobs.items():
    base=f'{HI}/{n}-{p}'
    if not os.path.exists(base+'.png'):
        subprocess.run(['pdftoppm','-r','220','-png','-singlefile','-f',str(p),'-l',str(p),f'{D}/{P%n}',base],check=True)
    im=Image.open(base+'.png').convert('RGB'); W,H=im.size
    c=im.crop((int(x0*W),int(y0*H),int(x1*W),int(y1*H)))
    c=c.resize((1480,int(c.height*1480/c.width)),Image.LANCZOS)
    c.save(f'{OUT}/{name}.jpg',quality=88); print(name,c.size)
