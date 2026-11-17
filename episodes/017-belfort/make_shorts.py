import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
def hl(name, i=0):
    a, b = HL[name][i]
    return [0.0, a, 1.0, round(b - a, 4)]
def doc(img, kicker, src, i=0, pan=None):
    return dict(type="doc", img=f"img/{img}.jpg", pan=pan or [0.0, 0.1], hl=hl(img, i), kicker=kicker, src=src)
SRC_MTC = "U.S. motion to compel, ECF 1 (Mar 29, 2018)"
SRC_GIL = "Gilsen declaration, D. Nev. ECF 4-1 (Mar 31, 2018)"
SRC_CALD = "DOJ, AAG Caldwell remarks (Jul 20, 2016)"
SRC_BBG18 = "Bloomberg (May 16, 2018)"
SRC_TMZ = "TMZ (Jul 13, 2026)"
SRC_CNBC = "CNBC (Mar 7, 2018)"
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
shorts = [
 # S1 — the number (strongest, 10:00)
 {"title": "$12.8M of $110M by 2018, Feds Said: The Wolf's Restitution", "template": "number reveal (ordered vs. paid)",
  "lines": [
  L("Twelve point eight million dollars. That's what prosecutors said Jordan Belfort, the Wolf of Wall Street, had paid by twenty eighteen, of one hundred ten million.",
    dict(type="hook", img="img/belfort_hook.jpg", pos="50% 0%", zoom=1.3334, tag="GUILTY", number="$12.8M", label="PAID OF $110M|BY 2018, FEDS SAID"),
    show="$12.8 million. That's what prosecutors said Jordan Belfort, the Wolf of Wall Street, had paid by 2018, of $110 million."),
  L("In two thousand three, a judge ordered it, for fifteen hundred thirteen investors.",
    doc("mtc_2", "U.S. MOTION TO COMPEL · 2018", SRC_MTC, 0),
    show="In 2003, a judge ordered it, for 1,513 investors."),
  L("He was supposed to pay half his income. Prosecutors said he kept at least nine million from speeches.",
    dict(type="stat", kicker="SPEAKING FEES · 2013–2015", value="$9M+", label="KEPT, PROSECUTORS SAID", src=SRC_BBG18),
    show="He was supposed to pay half his income. Prosecutors said he kept at least $9 million from speeches."),
  L("TMZ reported his obligation expired this year, under a twenty-year federal limit. Belfort says he completed it.",
    dict(type="quote", q="…I completed my court-ordered restitution.", case="JORDAN BELFORT", doc="TO TMZ · JULY 2026", cite=SRC_TMZ),
    show="TMZ reported his obligation expired this year, under a 20-year federal limit. Belfort says he completed it."),
  L("Should restitution ever expire? Tell me below.", dict(type="end", cta="FULL CASE ON THE CHANNEL")),
 ]},
 # S2 — the movie money (14:00)
 {"title": "\"Life Imitated Art\": What DOJ Alleged About the Wolf Movie", "template": "verbatim quote (DOJ) + twist",
  "lines": [
  L("More than a hundred million dollars from a theft. That's what the Justice Department alleged went into The Wolf of Wall Street.",
    dict(type="hook", img="img/cald.jpg", pos="50% 74%", zoom=1.9, tag="DOJ ALLEGED", number="$100M+", label="TO FINANCE THE FILM|DOJ ALLEGED IN 2016"),
    show="More than $100 million from a theft. That's what the Justice Department alleged went into The Wolf of Wall Street."),
  L("It said Red Granite Pictures financed the film with that money, from Malaysia's one M.D.B. fund.",
    doc("cald", "DOJ · JULY 20, 2016", SRC_CALD, 2),
    show="It said Red Granite Pictures financed the film with that money, from Malaysia's 1MDB fund."),
  L("Its words: according to the allegations in the complaint, this is a case where life imitated art.",
    dict(type="quote", q="According to the allegations in the complaint, this is a case where life imitated art.", case="AAG LESLIE R. CALDWELL", doc="DOJ · JULY 20, 2016", cite=SRC_CALD)),
  L("In twenty eighteen, Red Granite agreed to pay sixty million dollars, admitting no wrongdoing. Belfort wasn't accused.",
    dict(type="stat", kicker="RED GRANITE · 2018", value="$60M", label="SETTLEMENT · NO ADMISSION", src=SRC_CNBC),
    show="In 2018, Red Granite agreed to pay $60 million, admitting no wrongdoing. Belfort wasn't accused."),
  L("A fraud movie, funded by theft, the DOJ alleged. Did you know?", dict(type="end", cta="FULL CASE ON THE CHANNEL")),
 ]},
 # S3 — the company books (18:00)
 {"title": "$9,188,876.06 in \"Distributions\": The Wolf's Company Books", "template": "document reveal (forensic accounting)",
  "lines": [
  L("Nine point one nine million dollars. A government accountant found that much in personal expenses of Jordan Belfort and his partner, paid by his company.",
    dict(type="hook", img="img/gil_1.jpg", pos="50% 84%", zoom=1.9, tag="COURT FILING", number="$9.19M", label="\"DISTRIBUTIONS\"|PAID BY HIS COMPANY"),
    show="$9.19 million. A government accountant found that much in personal expenses of Jordan Belfort and his partner, paid by his company."),
  L("It sat in an account called Distributions. He found no agreement to pay it back.",
    doc("gil_1", "FORENSIC ACCOUNTANT · MARCH 2018", SRC_GIL, 2)),
  L("Asked under oath if he signed any loan agreements with the company, Belfort said: No.",
    doc("gil_2", "FORENSIC ACCOUNTANT · MARCH 2018", SRC_GIL, 0)),
  L("Prosecutors said some of that money could have gone to his victims, who were owed about ninety-seven million.",
    doc("mtc_6", "U.S. MOTION TO COMPEL · 2018", SRC_MTC, 2),
    show="Prosecutors said some of that money could have gone to his victims, who were owed about $97 million."),
  L("Loan or income? Tell me below.", dict(type="end", cta="FULL CASE ON THE CHANNEL")),
 ]},
]
from panfix import fix
if __name__ == "__main__":
    for i, s in enumerate(shorts, 1):
        fix(s["lines"], "short")
        json.dump({"title": s["title"], "template": s["template"], "lines": s["lines"]}, open(os.path.join(HERE, f"short{i}.json"), "w"), indent=1, ensure_ascii=False)
        print(i, len(s["title"]), s["title"], sum(len(l["say"].split()) for l in s["lines"]), "words")
