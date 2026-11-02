import subprocess, sys, os
from PIL import Image
D='/home/claude/research/d'; HI='/home/claude/research/hi'; OUT='/home/claude/sworn_media/episodes/002-bankman-fried/img'
jobs = {
 # name: (pdf, page, x0, x1, y0, y1)
 'indictment': ('ind1.pdf',1,0.04,0.96,0.035,0.62),
 'memo_intro': ('gov.uscourts.nysd.590940.410.0.pdf',5,0.04,0.96,0.035,0.62),
 'allownegative': ('gov.uscourts.nysd.590940.410.0.pdf',10,0.04,0.96,0.33,0.93),
 'spreadsheet': ('gov.uscourts.nysd.590940.410.0.pdf',14,0.04,0.96,0.035,0.76),
 'tweets': ('gov.uscourts.nysd.590940.410.0.pdf',16,0.04,0.96,0.035,0.80),
 'letter': ('gov.uscourts.nysd.590940.388.0.pdf',1,0.04,0.96,0.40,0.80),
 'judgment': ('gov.uscourts.nysd.590940.424.0.pdf',1,0.03,0.97,0.03,0.66),
 'judgment3': ('gov.uscourts.nysd.590940.424.0.pdf',3,0.03,0.97,0.03,0.40),
 'forfeit': ('gov.uscourts.nysd.590940.424.0.pdf',7,0.03,0.97,0.70,0.96),
 'newtrial': ('gov.uscourts.nysd.590940.595.0.pdf',1,0.04,0.96,0.035,0.62),
 'newtrial3': ('gov.uscourts.nysd.590940.595.0.pdf',3,0.04,0.96,0.035,0.42),
 'mandate': ('gov.uscourts.nysd.590940.601.0.pdf',1,0.04,0.96,0.035,0.79),
}
for name,(pdf,p,x0,x1,y0,y1) in jobs.items():
    base=f'{HI}/{os.path.basename(pdf)}-{p}'
    if not os.path.exists(base+'.png'):
        subprocess.run(['pdftoppm','-r','220','-png','-singlefile','-f',str(p),'-l',str(p),f'{D}/{pdf}',base],check=True)
    im=Image.open(base+'.png').convert('RGB'); W,H=im.size
    c=im.crop((int(x0*W),int(y0*H),int(x1*W),int(y1*H)))
    c=c.resize((1480,int(c.height*1480/c.width)),Image.LANCZOS)
    c.save(f'{OUT}/{name}.jpg',quality=88); print(name,c.size)
