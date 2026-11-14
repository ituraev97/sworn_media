import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
def hl(name, i=0):
    a, b = HL[name][i]
    return [0.0, a, 1.0, round(b - a, 4)]
def doc(img, kicker, src, i=0, pan=None):
    return dict(type="doc", img=f"img/{img}.jpg", pan=pan or [0.0, 0.1], hl=hl(img, i), kicker=kicker, src=src)
CASE = "UNITED STATES v. LINK"
SRC_V = "U.S. Attorney's Office, N.D. Tex. (Nov 11, 2026)"
SRC_SSI = "Second Superseding Indictment, U.S. v. Link (N.D. Tex. 2026)"
SRC_SEC = "SEC v. Agridime, Complaint (N.D. Tex. 2023) — allegations"
SRC_FBI = "FBI wanted poster, Joshua Robert Link (2026)"
SRC_EX = "Gov't trial exhibit, published by USAO N.D. Tex. (Nov 2026)"
SRC_DTN = "DTN, citing FBI Dallas (Mar 2026)"
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
GUILTY = dict(type="verdict", kicker="FORT WORTH · NOV 10, 2026", stamp="GUILTY", big="Joshua & Jason Link", sub="wire fraud · money laundering")
shorts = [
 # S1 — number + fugitive (strongest, 10:00)
 {"title": "$240 Million Cattle Scheme. FBI Fugitive Caught at LAX.", "template": "number reveal + chase",
  "lines": [
  L("Guilty. Joshua Link's cattle company collected over two hundred forty million dollars. Then he landed on the FBI's wanted list.",
    dict(type="hook", img="img/link_face.jpg", pos="50% 0%", zoom=0.85, tag="GUILTY", number="$240M", label="FBI FUGITIVE|NOW CONVICTED"),
    show="Guilty. Joshua Link's cattle company collected over $240 million. Then he landed on the FBI's wanted list."),
  L("The FBI's poster said Agridime purchased only a fraction of the cattle.",
    doc("poster", "WANTED BY THE FBI · 2026", SRC_FBI, 0),
    show="The FBI's poster said \"Agridime purchased only a fraction of the cattle.\""),
  L("On March ninth, he was taken into custody at Los Angeles International Airport.",
    dict(type="big", kicker="LAX · MARCH 9, 2026", lines=["Taken into", "custody|at LAX."], src=SRC_DTN),
    show="On March 9, he was taken into custody at Los Angeles International Airport."),
  L("On November tenth, a Fort Worth jury convicted him and his brother Jason. Sentencing is set for March.",
    GUILTY, show="On November 10, a Fort Worth jury convicted him and his brother Jason. Sentencing is set for March."),
  L("How many years should he get? Tell me below.", dict(type="end", cta="FULL CASE ON THE CHANNEL")),
 ]},
 # S2 — the chart (14:00)
 {"title": "115,255 Cattle Sold on Contract. Only 51,704 Net Bought.", "template": "number vs number",
  "lines": [
  L("Contracts for one hundred fifteen thousand, two hundred fifty-five head of cattle sold. Only fifty-one thousand, seven hundred four net bought. That's the government's chart from the Agridime trial.",
    dict(type="hook", img="img/link_face.jpg", pos="50% 0%", zoom=0.85, tag="GUILTY", number="115,255", label="HEAD SOLD ON CONTRACT|ONLY 51,704 NET BOUGHT"),
    show="Contracts for 115,255 head of cattle sold. Only 51,704 net bought. That's the government's chart from the Agridime trial."),
  L("Buyers paid two thousand dollars a head, with guaranteed fifteen to twenty percent yearly profits.",
    doc("ssi_4", "SECOND SUPERSEDING INDICTMENT", SRC_SSI, 0),
    show="Buyers paid $2,000 a head, with \"guaranteed 15-20% yearly profits.\""),
  L("Prosecutors say new money paid earlier buyers. The U.S. Attorney called it a high-tech Ponzi scheme.",
    dict(type="quote", q="the Link brothers ran a high-tech Ponzi scheme", case=CASE, doc="U.S. ATTORNEY RYAN RAYBOULD", cite=SRC_V, size=50),
    show="Prosecutors say new money paid earlier buyers. The U.S. Attorney called it a \"high-tech Ponzi scheme.\""),
  L("On November tenth, the Link brothers were found guilty.", GUILTY, show="On November 10, the Link brothers were found guilty."),
  L("Would you have bought one? Comment below.", dict(type="end", cta="FULL CASE ON THE CHANNEL")),
 ]},
 # S3 — verbatim quote (18:00)
 {"title": "\"Too Good to Be True\" — Their Own Ad Said It", "template": "verbatim quote",
  "lines": [
  L("We know it sounds too good to be true. A real ad from a Texas cattle company promising fifteen to twenty percent a year.",
    dict(type="hook", img="img/sec_7.jpg", pos="50% 36%", zoom=1.6, tag="GUILTY", number="15–20%", label="\"WE KNOW IT SOUNDS|TOO GOOD TO BE TRUE\""),
    show="\"We know it sounds too good to be true.\" A real ad from a Texas cattle company promising 15-20% a year."),
  L("Make money raising cattle without having to do all the work, it said.",
    doc("sec_7", "SEC v. AGRIDIME · COMPLAINT", SRC_SEC, 0),
    show="\"Make money raising cattle without having to do all the work,\" it said."),
  L("Agridime collected over two hundred forty million dollars from more than twenty-two hundred people.",
    dict(type="stat", kicker="2021–2023", value="$240M", label="from 2,200+ victims", src=SRC_V),
    show="Agridime collected over $240 million from more than 2,200 people."),
  L("Prosecutors say scheme money built a nearly one point five million dollar barndominium in Kansas.",
    dict(type="photo", img="img/rel_barndo.jpg", caption="PHOTO RELEASED BY THE U.S. ATTORNEY", src=SRC_V, fit="cover"),
    show="Prosecutors say scheme money built a nearly $1.5 million \"barndominium\" in Kansas."),
  L("Then the jury said guilty.", GUILTY),
  L("Would that ad have fooled you? Tell me below.", dict(type="end", cta="FULL CASE ON THE CHANNEL")),
 ]},
]
from panfix import fix
if __name__ == "__main__":
    for i, s in enumerate(shorts, 1):
        fix(s["lines"], "short")
        json.dump({"title": s["title"], "template": s["template"], "lines": s["lines"]}, open(os.path.join(HERE, f"short{i}.json"), "w"), indent=1, ensure_ascii=False)
        print(i, len(s["title"]), s["title"], sum(len(l["say"].split()) for l in s["lines"]), "words")
