import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
def hl(name, i=0):
    a, b = HL[name][i]
    return [0.0, a, 1.0, round(b - a, 4)]
def doc(img, kicker, src, i=0):
    return dict(type="doc", img=f"img/{img}.jpg", pan=[0.0, 0.1], hl=hl(img, i), kicker=kicker, src=src)
CASE = "UNITED STATES v. BALWANI"
SRC_CA9 = "U.S. v. Balwani, Ninth Circuit opinion (amended Dec 2025)"
SRC_SEC = "SEC v. Balwani, Complaint (N.D. Cal. 2018) — allegations"
SRC_TSI = "Third Superseding Indictment, U.S. v. Holmes & Balwani (N.D. Cal. 2020)"
SRC_MEMO = "U.S. Sentencing Memorandum, U.S. v. Holmes (N.D. Cal. 2022)"
SRC_AP = "Associated Press (Dec 7, 2022)"
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
END = L("Real trials. Real evidence. The verdict.", dict(type="end"))
shorts = [
 # S1 — verbatim quote
 {"title": "\"[They] Weren't Just Projections, They Were Lies.\"", "template": "verbatim quote",
  "hook": "\"THEY WERE|LIES.\"", "lines": [
  L("They weren't just projections. They were lies. A federal judge said that at the sentencing of former Theranos president Sunny Balwani, the A.P. reported.",
    dict(type="quote", q="weren't just projections, they were lies.", case=CASE, doc="JUDGE EDWARD J. DAVILA · AT SENTENCING", cite="As quoted by " + SRC_AP, size=54),
    show="\"…weren't just projections, they were lies.\" A federal judge said that at the sentencing of former Theranos president Sunny Balwani, the AP reported."),
  L("The S.E.C. alleged he drafted investor projections of over one hundred million dollars in revenue for twenty fourteen. It alleged Theranos recorded little more than one hundred thousand.",
    doc("sec_real", "SEC COMPLAINT · AS ALLEGED", SRC_SEC, 0),
    show="The SEC alleged he drafted investor projections of over $100 million in revenue for 2014. It alleged Theranos recorded little more than $100,000."),
  L("A jury convicted him on all twelve counts. Sentence: one hundred fifty-five months.",
    dict(type="verdict", kicker="SAN JOSE · 2022", stamp="GUILTY", big="155 months", sub="Ramesh \"Sunny\" Balwani · 12 of 12 counts"),
    show="A jury convicted him on all twelve counts. Sentence: 155 months."),
  END]},
 # S2 — before -> after (Holmes vs. Balwani)
 {"title": "135 Months vs. 155 Months: The Two Theranos Verdicts", "template": "before → after",
  "hook": "135 vs. 155|MONTHS", "lines": [
  L("One hundred thirty-five months for Elizabeth Holmes. One hundred fifty-five for Sunny Balwani. Same indictment. Same judge. Same sentencing range.",
    dict(type="bars", kicker="THERANOS · THE SENTENCES", title="Same range: 135–168 months", items=[{"label": "Holmes", "value": 135, "display": "135"}, {"label": "Balwani", "value": 155, "display": "155"}], src=SRC_CA9),
    show="135 months for Elizabeth Holmes. 155 for Sunny Balwani. Same indictment. Same judge. Same sentencing range."),
  L("Her jury acquitted her of defrauding patients. His jury convicted him on all twelve counts, investors and patients.",
    doc("ca9_all", "NINTH CIRCUIT · OPINION", SRC_CA9, 0)),
  L("The appeals court wrote that the evidence linked him to inaccurate test results sent to patients. In October, the Supreme Court declined to hear his case.",
    dict(type="verdict", kicker="OCTOBER 5, 2026", stamp="DENIED", big="No review", sub="Balwani v. United States · No. 25-1330")),
  END]},
 # S3 — dollar-figure reveal
 {"title": "$1,126,661 on Ads. His Own Text: \"Disaster Zone.\"", "template": "dollar-figure reveal",
  "hook": "$1,126,661|ON ADS", "lines": [
  L("One million, one hundred twenty-six thousand, six hundred sixty-one dollars. Theranos wired that on August third, twenty fifteen, to buy ads for its blood-testing Wellness Centers.",
    doc("tsi_c12", "INDICTMENT · COUNT 12", SRC_TSI, 1),
    show="$1,126,661. Theranos wired that on August 3, 2015, to buy ads for its blood-testing Wellness Centers."),
  L("Months earlier, its president, Sunny Balwani, had texted Elizabeth Holmes that the lab running Theranos's own devices was a disaster zone.",
    doc("memo_zone", "U.S. SENTENCING MEMORANDUM", SRC_MEMO, 1),
    show="Months earlier, its president, Sunny Balwani, had texted Elizabeth Holmes that the lab running Theranos's own devices was a \"disaster zone.\""),
  L("That ad buy became count twelve. The jury convicted him on all twelve. One hundred fifty-five months.",
    dict(type="verdict", kicker="JULY 7, 2022 · SAN JOSE", stamp="GUILTY", big="Count 12", sub="and every other count · 155 months"),
    show="That ad buy became count twelve. The jury convicted him on all twelve. 155 months."),
  END]},
]
from panfix import fix
for s in shorts: fix(s["lines"], "short")
for i, s in enumerate(shorts, 1):
    s["label"] = "SWORN"
    json.dump(s, open(os.path.join(HERE, f"short{i}.json"), "w"), indent=1, ensure_ascii=False)
    print(i, len(s["title"]), sum(len(l["say"].split()) for l in s["lines"]), "words", len(s["lines"]), "lines")
