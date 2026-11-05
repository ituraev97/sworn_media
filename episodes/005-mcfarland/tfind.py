import subprocess,sys,csv,io,os
from PIL import Image
def find(pdf,page,start,end,hi='/home/claude/research/hi'):
    base=f'{hi}/{os.path.basename(pdf)}-{page}'
    if not os.path.exists(base+'.png'):
        subprocess.run(['pdftoppm','-r','220','-png','-singlefile','-f',str(page),'-l',str(page),pdf,base],check=True)
    H=Image.open(base+'.png').size[1]
    out=subprocess.run(['tesseract',base+'.png','-','tsv'],capture_output=True,text=True).stdout
    ws=[r for r in csv.DictReader(io.StringIO(out),delimiter='\t',quoting=csv.QUOTE_NONE) if r['text'] and r['text'].strip()]
    toks=[w['text'] for w in ws]; s=start.split(); e=end.split()
    for i in range(len(toks)):
        if toks[i:i+len(s)]==s:
            for j in range(i,len(toks)):
                if toks[j:j+len(e)]==e:
                    k=j+len(e)-1; seg=ws[i:k+1]
                    return round(min(int(w['top']) for w in seg)/H,4), round(max(int(w['top'])+int(w['height']) for w in seg)/H,4)
    return None, ' '.join(toks)[:3000]
if __name__=='__main__':
    print(find(sys.argv[1],int(sys.argv[2]),sys.argv[3],sys.argv[4]))
