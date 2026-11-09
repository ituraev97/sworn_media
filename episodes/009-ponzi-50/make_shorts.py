import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
def hl(name, i=0):
    a, b = HL[name][i]
    return [0.0, a, 1.0, round(b - a, 4)]
def doc(img, kicker, src, i=0):
    return dict(type="doc", img=f"img/{img}.jpg", pan=[0.0, 0.1], hl=hl(img, i), kicker=kicker, src=src)
RR = "U.S. Attorney, S.D. Fla. (2010)"
PT = "U.S. Attorney, D. Minn. (Apr 8, 2010)"
PT_AFF = "FBI affidavit, D. Minn. 08-MJ-364"
PT_JUD = "Judgment, D. Minn. No. 08-364"
DOJ = "U.S. Dept. of Justice releases"
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
END = L("Real trials. Real evidence. The verdict.", dict(type="end"))
BARS = dict(type="bars", kicker="FEDERAL SENTENCES", title="Years in prison",
            items=[{"label": "Rothstein", "value": 50, "display": "50"}, {"label": "Petters", "value": 50, "display": "50"},
                   {"label": "Okun", "value": 100, "display": "100"}, {"label": "Stanford", "value": 110, "display": "110"},
                   {"label": "Madoff", "value": 150, "display": "150"}], src=DOJ)
shorts = [
 # S1 — countdown / ranking
 {"title": "50 to 150 Years: 5 Ponzi Schemes, Ranked", "template": "countdown / ranking",
  "hook": "50 → 150|YEARS", "lines": [
  L("Fifty years. Fifty. One hundred. One hundred ten. One hundred fifty. Five Ponzi schemes, five federal sentences.",
    BARS, show="50 years. 50. 100. 110. 150. Five Ponzi schemes, five federal sentences."),
  L("Fifty: Scott Rothstein, a lawyer whose firm sold settlements that never existed. Fifty: Tom Petters, and purchase orders for electronics never bought.",
    dict(type="list", kicker="#5 · #4", items=[["50", "Scott Rothstein"], ["50", "Tom Petters"]], src=DOJ),
    show="50: Scott Rothstein, a lawyer whose firm sold settlements that never existed. 50: Tom Petters, and purchase orders for electronics never bought."),
  L("One hundred: Edward Okun, who took clients' tax-exchange money. One hundred ten: Allen Stanford's offshore bank.",
    dict(type="list", kicker="#3 · #2", items=[["100", "Edward Okun"], ["110", "Allen Stanford"]], src=DOJ),
    show="100: Edward Okun, who took clients' tax-exchange money. 110: Allen Stanford's offshore bank."),
  L("And one hundred fifty years: Bernie Madoff.",
    dict(type="verdict", kicker="#1 · JUNE 29, 2009", stamp="SENTENCED", big="150 years", sub="Bernard L. Madoff"),
    show="And 150 years: Bernie Madoff."),
  END]},
 # S2 — verbatim quote
 {"title": "\"Divine Intervention\": How a $3.7B Ponzi Got Caught", "template": "verbatim quote",
  "hook": "“DIVINE|INTERVENTION”", "lines": [
  L("Divine intervention. That, the Justice Department said, is how Tom Petters explained getting away with it for so long, on tape, recorded by his own employee.",
    doc("pet_pr", "U.S. ATTORNEY · APRIL 8, 2010", PT),
    show="\"Divine intervention.\" That, the Justice Department said, is how Tom Petters explained getting away with it for so long, on tape, recorded by his own employee."),
  L("Investors lent his company money to buy electronics for Costco and Sam's Club. No such purchases were made. In an FBI affidavit, a cooperating witness called the purchase orders entirely fabricated.",
    doc("pet_cw", "FBI AFFIDAVIT · OCTOBER 2008", PT_AFF, 1),
    show="Investors lent his company money to buy electronics for Costco and Sam's Club. No such purchases were made. In an FBI affidavit, a cooperating witness called the purchase orders \"entirely fabricated.\""),
  L("A three point seven billion dollar Ponzi scheme. Guilty on all twenty counts. Fifty years.",
    dict(type="verdict", kicker="APRIL 8, 2010 · ST. PAUL", stamp="SENTENCED", big="50 years", sub="Tom Petters · $3.7 billion"),
    show="A $3.7 billion Ponzi scheme. Guilty on all 20 counts. 50 years."),
  END]},
 # S3 — dollar-figure reveal
 {"title": "$57 Million to Collect a Win. The Court Order Was Fake.", "template": "dollar-figure reveal",
  "hook": "$57 MILLION|FAKE COURT ORDER", "lines": [
  L("Fifty-seven million dollars. That's what one law firm's clients wired, prosecutors said, to collect a twenty-three million dollar judgment that did not exist.",
    dict(type="stat", kicker="PER PROSECUTORS", value="$57M", label="wired to post “bonds”", src=RR),
    show="$57 million. That's what one law firm's clients wired, prosecutors said, to collect a $23 million judgment that did not exist."),
  L("The firm had secretly settled their lawsuit, in the other side's favor. Then came a false federal court order, purportedly signed by a U.S. District Judge.",
    doc("rr_order", "PER PROSECUTORS", RR, 0)),
  L("Behind it, prosecutors said, was attorney Scott Rothstein. He ran a one point two billion dollar Ponzi scheme built on settlements and loans that never existed. Sentence: fifty years.",
    dict(type="verdict", kicker="JUNE 9, 2010 · FORT LAUDERDALE", stamp="SENTENCED", big="50 years", sub="Scott Rothstein · $1.2 billion"),
    show="Behind it, prosecutors said, was attorney Scott Rothstein. He ran a $1.2 billion Ponzi scheme built on settlements and loans that never existed. Sentence: 50 years."),
  END]},
]
from panfix import fix
for s in shorts: fix(s["lines"], "short")
for i, s in enumerate(shorts, 1):
    s["label"] = "SWORN"
    json.dump(s, open(os.path.join(HERE, f"short{i}.json"), "w"), indent=1, ensure_ascii=False)
    print(i, len(s["title"]), sum(len(l["say"].split()) for l in s["lines"]), "words", len(s["lines"]), "lines")
