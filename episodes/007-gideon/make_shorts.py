import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
def hl(name, i=0):
    a, b = HL[name][i]
    return [0.0, a, 1.0, round(b - a, 4)]
def doc(img, kicker, src, i=0):
    return dict(type="doc", img=f"img/{img}.jpg", pan=[0.0, 0.1], hl=hl(img, i), kicker=kicker, src=src)
CASE = "GIDEON v. WAINWRIGHT"
SRC_OP = "Gideon v. Wainwright, 372 U.S. 335 (1963)"
SRC_MIN = "Bay County minute book, Aug 1961"
SRC_FLB = "Florida's brief, No. 155, 1963"
SRC_JACOB = "B. Jacob, 99 Iowa L. Rev. 2059 (2014)"
SRC_ENC = "Encyclopedia.com, Gideon Trials"
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
END = L("Real trials. Real evidence. The verdict.", dict(type="end"))
shorts = [
 # S1 — verbatim quote
 {"title": "\"I Am Entitled to Be Represented by Counsel\"", "template": "verbatim quote",
  "hook": "\"I am entitled to be|represented by Counsel\"", "lines": [
  L("The United States Supreme Court says I am entitled to be represented by Counsel.",
    dict(type="quote", q="The United States Supreme Court says I am entitled to be represented by Counsel.", case=CASE, doc="CLARENCE EARL GIDEON · AUG 4, 1961", cite="As quoted in " + SRC_OP, size=50)),
  L("Clarence Earl Gideon told a Florida judge that in nineteen sixty-one. Charged with breaking into a poolroom, too poor for a lawyer. The judge said no: Florida appointed counsel only in capital cases.",
    doc("op_coll", "BAY COUNTY, FLORIDA · 1961", SRC_OP),
    show="Clarence Earl Gideon told a Florida judge that in 1961. Charged with breaking into a poolroom, too poor for a lawyer. The judge said no: Florida appointed counsel only in capital cases."),
  L("He defended himself. Guilty. Five years.",
    dict(type="verdict", kicker="AUGUST 1961", stamp="GUILTY", big="5 years", sub="no lawyer"),
    show="He defended himself. Guilty. 5 years."),
  L("Nineteen sixty-three: the Supreme Court ruled for him, without a dissent. Retried with a lawyer, he was acquitted.",
    dict(type="verdict", kicker="1963", stamp="NOT GUILTY", neutral=True, big="Acquitted", sub="retried with a lawyer"),
    show="1963: the Supreme Court ruled for him, without a dissent. Retried with a lawyer, he was acquitted."),
  END]},
 # S2 — number reveal
 {"title": "\"Over 5,000 Hardened Criminals\": Florida's Warning", "template": "number reveal",
  "hook": "\"over 5,000|hardened criminals\"", "lines": [
  L("Over five thousand hardened criminals in Florida, set free, if the ruling reached old cases. That was Florida's warning to the Supreme Court.",
    dict(type="stat", kicker="FLORIDA'S BRIEF · 1963", value="5,000+", label="“hardened criminals”|to be set free", src=SRC_FLB),
    show="\"Over 5,000 hardened criminals in Florida,\" set free, if the ruling reached old cases. That was Florida's warning to the Supreme Court."),
  L("Its own survey: four thousand sixty-five prisoners had pleaded guilty with no lawyer.",
    doc("fl_survey", "FLORIDA'S PRISON SURVEY · 1962", SRC_FLB),
    show="Its own survey: 4,065 prisoners had pleaded guilty with no lawyer."),
  L("The case was Clarence Earl Gideon's. Five years for a poolroom break-in, tried without counsel. The Court sided with him anyway. Lawyers, it said, are necessities, not luxuries.",
    doc("op_truth", "MARCH 18, 1963", SRC_OP, 1),
    show="The case was Clarence Earl Gideon's. 5 years for a poolroom break-in, tried without counsel. The Court sided with him anyway. Lawyers, it said, are \"necessities, not luxuries.\""),
  L("Florida's own lawyer later wrote: about twelve hundred were set free.",
    dict(type="stat", kicker="PER FLORIDA'S LAWYER, BRUCE JACOB", value="~1,200", label="set free", src=SRC_JACOB),
    show="Florida's own lawyer later wrote: about 1,200 were set free."),
  END]},
 # S3 — before -> after
 {"title": "5-Year Sentence Without a Lawyer. Not Guilty With One.", "template": "before → after",
  "hook": "1961: GUILTY.|1963: NOT GUILTY.", "lines": [
  L("Nineteen sixty-one. No lawyer. Guilty. Five years.",
    dict(type="verdict", kicker="AUGUST 1961 · BAY COUNTY, FLORIDA", stamp="GUILTY", big="5 years", sub="Clarence Earl Gideon · no lawyer"),
    show="1961. No lawyer. Guilty. 5 years."),
  L("Clarence Earl Gideon was charged with breaking into a Florida poolroom. He asked for a lawyer. Florida appointed them only in capital cases.",
    doc("op_coll", "THE TRIAL · AUGUST 4, 1961", SRC_OP)),
  L("He took it to the Supreme Court, and won. A poor defendant, the Court said, cannot be assured a fair trial without one.",
    doc("op_truth", "MARCH 18, 1963", SRC_OP, 0)),
  L("Nineteen sixty-three. Retrial. Same charge, same judge. With a lawyer. Not guilty.",
    dict(type="verdict", kicker="THE RETRIAL · 1963", stamp="NOT GUILTY", neutral=True, big="Acquitted", sub="with a lawyer"),
    show="1963. Retrial. Same charge, same judge. With a lawyer. Not guilty."),
  END]},
]
from panfix import fix
for s in shorts: fix(s["lines"], "short")
for i, s in enumerate(shorts, 1):
    s["label"] = "SWORN"
    json.dump(s, open(os.path.join(HERE, f"short{i}.json"), "w"), indent=1, ensure_ascii=False)
    print(i, len(s["title"]), sum(len(l["say"].split()) for l in s["lines"]), "words", len(s["lines"]), "lines")
