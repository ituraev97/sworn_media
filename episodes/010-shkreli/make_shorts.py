import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
def hl(name, i=0):
    a, b = HL[name][i]
    return [0.0, a, 1.0, round(b - a, 4)]
def doc(img, kicker, src, i=0):
    return dict(type="doc", img=f"img/{img}.jpg", pan=[0.0, 0.1], hl=hl(img, i), kicker=kicker, src=src)
CASE = "UNITED STATES v. SHKRELI"
FTC = "FTC v. VYERA & SHKRELI"
SRC_R29 = "U.S. v. Shkreli, Rule 29 Order (E.D.N.Y. 2018)"
SRC_FTC = "FTC v. Vyera, Opinion & Order (S.D.N.Y. 2022)"
SRC_DOJ = "U.S. Attorney's Office, E.D.N.Y."
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
END = L("Real trials. Real evidence. The verdict.", dict(type="end"))
shorts = [
 # S1 — verbatim quote
 {"title": "\"Tighten the Supply Chain a Bit.\" He Said It From Prison", "template": "verbatim quote",
  "hook": "\"TIGHTEN THE|SUPPLY CHAIN\"", "lines": [
  L("There has to be some way to tighten the supply chain a bit. Martin Shkreli said that in August twenty nineteen, recorded from federal prison.",
    dict(type="quote", q="[T]here has to be some way to tighten the supply chain a bit . . .", case=FTC, doc="MARTIN SHKRELI · FROM PRISON · 2019", cite="As quoted in " + SRC_FTC, size=46),
    show="\"There has to be some way to tighten the supply chain a bit.\" Martin Shkreli said that in August 2019, recorded from federal prison."),
  L("He meant Daraprim, the drug his company raised from seventeen sixty to seven hundred fifty dollars a tablet. A judge found he kept directing the company from inside.",
    doc("ftc_price", "FTC v. VYERA · FINDINGS OF FACT", SRC_FTC, 0),
    show="He meant Daraprim, the drug his company raised from $17.60 to $750 a tablet. A judge found he kept directing the company from inside."),
  L("In twenty twenty-two, the court banned him from the drug industry for life, and ordered sixty-four point six million dollars disgorged.",
    dict(type="verdict", kicker="JANUARY 14, 2022", stamp="BANNED", big="For life", sub="$64.6 million disgorgement"),
    show="In 2022, the court banned him from the drug industry for life, and ordered $64.6 million disgorged."),
  END]},
 # S2 — dollar-figure reveal
 {"title": "$35 Million on Paper. $1.13 Million in Reality.", "template": "dollar-figure reveal",
  "hook": "$35 MILLION?|NOT EVEN CLOSE", "lines": [
  L("Thirty-five million dollars. That's how much Martin Shkreli told people his hedge fund managed.",
    dict(type="stat", kicker="MSMB CAPITAL · WHAT HE CLAIMED", value="$35M", label="under management", src=SRC_R29),
    show="$35 million. That's how much Martin Shkreli told people his hedge fund managed."),
  L("A federal judge wrote that the fund never had more than about one point one three million at one time.",
    doc("r29_113", "U.S. DISTRICT COURT · 2018", SRC_R29, 0),
    show="A federal judge wrote that the fund never had more than about $1.13 million at one time."),
  L("One bad trade in twenty eleven cost Merrill Lynch more than seven million dollars. His reports to investors kept showing positive returns.",
    doc("r29_orex", "U.S. DISTRICT COURT · 2018", SRC_R29, 0),
    show="One bad trade in 2011 cost Merrill Lynch more than $7 million. His reports to investors kept showing positive returns."),
  L("In twenty seventeen, a jury convicted him of securities fraud. Sentence: seven years. Not for the seven-hundred-fifty-dollar pill.",
    dict(type="verdict", kicker="BROOKLYN · 2017–2018", stamp="GUILTY", big="7 years", sub="Martin Shkreli · securities fraud"),
    show="In 2017, a jury convicted him of securities fraud. Sentence: 7 years. Not for the $750 pill."),
  END]},
 # S3 — before -> after (what he claimed vs. what the court record shows)
 {"title": "\"Graduated Very Young From Columbia.\" The Record Says No", "template": "before → after",
  "hook": "\"VERY YOUNG FROM|COLUMBIA\"", "lines": [
  L("Graduated very young from Columbia. That's what Martin Shkreli claimed, an investor testified. Columbia's registrar testified he never enrolled.",
    dict(type="big", kicker="CLAIM → COURT RECORD", lines=["“Columbia.”", "Never|enrolled."], src=SRC_R29),
    show="\"Graduated very young from Columbia.\" That's what Martin Shkreli claimed, an investor testified. Columbia's registrar testified he never enrolled."),
  L("The auditor he named for his fund? He stipulated the firm never provided it any services.",
    doc("r29_col", "U.S. DISTRICT COURT · 2018", SRC_R29, 1)),
  L("His report after a trade wiped out almost all the fund's capital? It said up six point seven percent in March.",
    doc("r29_rep", "U.S. DISTRICT COURT · 2018", SRC_R29, 0),
    show="His report after a trade wiped out almost all the fund's capital? It said up 6.7% in March."),
  L("The jury convicted him of securities fraud. Seven years in federal prison.",
    dict(type="verdict", kicker="AUGUST 4, 2017 · BROOKLYN", stamp="GUILTY", big="Securities fraud", sub="sentenced to 7 years")),
  END]},
]
from panfix import fix
for s in shorts: fix(s["lines"], "short")
for i, s in enumerate(shorts, 1):
    s["label"] = "SWORN"
    json.dump(s, open(os.path.join(HERE, f"short{i}.json"), "w"), indent=1, ensure_ascii=False)
    print(i, len(s["title"]), sum(len(l["say"].split()) for l in s["lines"]), "words", len(s["lines"]), "lines")
