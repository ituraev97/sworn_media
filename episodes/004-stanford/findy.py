import subprocess, sys, re, html
def words(pdf, page):
    x = subprocess.run(['pdftotext','-bbox','-f',str(page),'-l',str(page),pdf,'-'],capture_output=True,text=True).stdout
    H = float(re.search(r'<page width="([\d.]+)" height="([\d.]+)"',x).group(2))
    ws = [(html.unescape(m.group(5)), float(m.group(2))/H, float(m.group(4))/H) for m in re.finditer(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', x)]
    return ws
def find(pdf, page, start, end):
    ws = words(pdf, page); toks=[w[0] for w in ws]
    s = start.split(); e = end.split()
    for i in range(len(toks)):
        if toks[i:i+len(s)] == s:
            for j in range(i, len(toks)):
                if toks[j:j+len(e)] == e:
                    k = j+len(e)-1
                    return round(min(w[1] for w in ws[i:k+1]),4), round(max(w[2] for w in ws[i:k+1]),4)
    return None
if __name__ == '__main__':
    pdf, page = sys.argv[1], int(sys.argv[2])
    for a in sys.argv[3:]:
        st, en = a.split('|')
        print(a, find(pdf, page, st, en))
