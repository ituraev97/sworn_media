import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
def hl(name, i=0):
    a, b = HL[name][i]
    return [0.0, a, 1.0, round(b - a, 4)]
def doc(img, kicker, src, i=0):
    return dict(type="doc", img=f"img/{img}.jpg", pan=[0.0, 0.1], hl=hl(img, i), kicker=kicker, src=src)
CASE = "KELLY v. UNITED STATES"
SRC_OP = "Kelly v. United States, opinion of the Court (U.S. May 7, 2020)"
SRC_USB = "Brief for the United States, Kelly v. United States (2019)"
SRC_GX = "Gov't Exhibit 145, U.S. v. Baroni & Kelly (D.N.J.)"
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
END = L("Real trials. Real evidence. The verdict.", dict(type="end"))
REV = dict(type="verdict", kicker="SUPREME COURT · MAY 7, 2020", stamp="REVERSED", big="9–0", sub="Kelly v. United States", neutral=True)
shorts = [
 # S1 — verbatim quote
 {"title": "\"Time for Some Traffic Problems in Fort Lee.\"", "template": "verbatim quote",
  "hook": "\"TIME FOR SOME|TRAFFIC PROBLEMS\"", "lines": [
  L("Time for some traffic problems in Fort Lee. That was the whole e-mail, sent in August twenty thirteen by a deputy chief of staff to New Jersey's governor. The reply: Got it.",
    dict(type="quote", q="Time for some traffic problems in Fort Lee.", case=CASE, doc="E-MAIL · AUG 13, 2013", cite="Quoted in " + SRC_OP, size=54),
    show="\"Time for some traffic problems in Fort Lee.\" That was the whole e-mail, sent in August 2013 by a deputy chief of staff to New Jersey's governor. The reply: \"Got it.\""),
  L("On the first day of school, Fort Lee's lanes onto the George Washington Bridge went from three to one. Four days of gridlock.",
    doc("usb_smile", "BRIEF FOR THE UNITED STATES", SRC_USB, 1)),
  L("A jury convicted her on every count. Then the Supreme Court threw it out, nine to nothing.",
    REV, show="A jury convicted her on every count. Then the Supreme Court threw it out, 9–0."),
  END]},
 # S2 — dollar-figure reveal
 {"title": "$3,696.09 in Overtime: The \"Property\" in the Bridgegate Case", "template": "dollar-figure reveal",
  "hook": "$3,696.09|IN OVERTIME", "lines": [
  L("Three thousand six hundred ninety-six dollars and nine cents. Payroll records put the Bridgegate toll collectors' extra shifts at that.",
    doc("usb_cost", "BRIEF FOR THE UNITED STATES", SRC_USB, 0),
    show="$3,696.09. Payroll records put the Bridgegate toll collectors' extra shifts at that."),
  L("Prosecutors said the employees' time was property, taken by fraud through a fake traffic study. The jury convicted.",
    doc("usb_14", "BRIEF FOR THE UNITED STATES", SRC_USB, 2)),
  L("The Supreme Court disagreed, nine to nothing. That cost, it said, was only an incidental byproduct of the scheme.",
    dict(type="quote", q="was its incidental byproduct.", case=CASE, doc="OPINION OF THE COURT", cite=SRC_OP, size=60),
    show="The Supreme Court disagreed, 9–0. That cost, it said, \"was its incidental byproduct.\""),
  END]},
 # S3 — before -> after
 {"title": "Guilty on All 7 Counts. Then the Supreme Court Said 9–0.", "template": "before → after",
  "hook": "GUILTY →|REVERSED 9–0", "lines": [
  L("What the jury found: guilty on all seven counts. Two officials had cut Fort Lee's bridge lanes to punish its mayor, prosecutors said, behind a fake traffic study.",
    dict(type="verdict", kicker="NEWARK · NOV 4, 2016", stamp="GUILTY", big="All 7 counts", sub="Baroni & Kelly"),
    show="What the jury found: guilty on all seven counts. Two officials had cut Fort Lee's bridge lanes to punish its mayor, prosecutors said, behind a fake traffic study."),
  L("What the Supreme Court found: the evidence no doubt shows wrongdoing. Deception, corruption, abuse of power.",
    dict(type="quote", q="deception, corruption, abuse of power.", case=CASE, doc="OPINION OF THE COURT · 2020", cite=SRC_OP, size=58),
    show="What the Supreme Court found: the evidence \"no doubt shows wrongdoing—deception, corruption, abuse of power.\""),
  L("But not every corrupt act by state or local officials is a federal crime. Reversed, nine to nothing.",
    REV, show="\"But not every corrupt act by state or local officials is a federal crime.\" Reversed, 9–0."),
  END]},
]
from panfix import fix
for s in shorts: fix(s["lines"], "short")
if __name__ == "__main__":
    for i, s in enumerate(shorts, 1):
        s["label"] = "SWORN"
        json.dump(s, open(os.path.join(HERE, f"short{i}.json"), "w"), indent=1, ensure_ascii=False)
        print(i, len(s["title"]), sum(len(l["say"].split()) for l in s["lines"]), "words", len(s["lines"]), "lines")
