import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
def hl(name, i=0):
    a, b = HL[name][i]
    return [0.0, a, 1.0, round(b - a, 4)]
def doc(img, kicker, src, i=0):
    return dict(type="doc", img=f"img/{img}.jpg", pan=[0.0, 0.1], hl=hl(img, i), kicker=kicker, src=src)
CASE = "UNITED STATES v. SKILLING"
SRC_CA5 = "U.S. v. Skilling (5th Cir. 2009)"
SRC_IND = "Superseding Indictment, Cr. No. H-04-25"
SRC_SG = "Brief for the United States, No. 08-1394"
SRC_SC = "Skilling v. United States, 561 U.S. 358 (2010)"
SRC_DOJ = "U.S. Dept. of Justice"
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
END = L("Real trials. Real evidence. The verdict.", dict(type="end"))
shorts = [
 # S1 — verbatim quote
 {"title": "\"Let Me Repeat That.\" What Enron's President Told Investors", "template": "verbatim quote",
  "hook": "\"Let me|repeat that.\"", "lines": [
  L("For Enron, the situation in California had little impact on fourth quarter results. Let me repeat that.",
    dict(type="quote", q="[F]or Enron, the situation in California had little impact on fourth quarter results. Let me repeat that.", case=CASE, doc="JEFFREY SKILLING · JAN 22, 2001", cite="As quoted in " + SRC_IND, size=44)),
  L("Enron's president, Jeffrey Skilling, to analysts in January two thousand one. Prosecutors said he knew California's utilities likely couldn't pay what they owed.",
    doc("ca5_calls", "THE FIFTH CIRCUIT · 2009", SRC_CA5, 0),
    show="Enron's president, Jeffrey Skilling, to analysts in January 2001. Prosecutors said he knew California's utilities likely couldn't pay what they owed."),
  L("That December, Enron went bankrupt. In two thousand six, a jury convicted him on nineteen counts.",
    dict(type="verdict", kicker="MAY 25, 2006 · HOUSTON", stamp="GUILTY", big="19 counts", sub="Jeffrey K. Skilling"),
    show="That December, Enron went bankrupt. In 2006, a jury convicted him on 19 counts."),
  L("Sentence: twenty-four years. Later cut to fourteen.",
    dict(type="big", kicker="2006 → 2013", lines=["24 years.", "Then|14."], src=SRC_DOJ),
    show="Sentence: 24 years. Later cut to 14."),
  END]},
 # S2 — dollar-figure reveal
 {"title": "$15 Million. Sold 6 Days After 9/11.", "template": "dollar-figure reveal",
  "hook": "$15 MILLION|6 days after 9/11", "lines": [
  L("Fifteen million dollars. Enron's former CEO netted more than that from one stock sale, on September seventeenth, two thousand one, the day markets reopened after nine eleven.",
    dict(type="stat", kicker="SEPTEMBER 17, 2001", value="$15M+", label="from one sale", src=SRC_SG),
    show="$15 million. Enron's former CEO netted more than that from one stock sale, on September 17, 2001, the day markets reopened after 9/11."),
  L("He told his broker he didn't want people at Enron to know. Under oath, he said he sold because he was scared by September eleventh.",
    doc("sg_scared", "BRIEF FOR THE UNITED STATES", SRC_SG, 0),
    show="He told his broker he didn't want people at Enron to know. Under oath, he said he sold because he was \"scared\" by September 11."),
  L("Less than three months later, Enron was bankrupt. The jury acquitted him on nine insider-trading counts. This sale was the one it convicted him on.",
    dict(type="verdict", kicker="COUNT 51 · INSIDER TRADING", stamp="GUILTY", big="Sept 17 sale", sub="Jeffrey K. Skilling · 2006")),
  END]},
 # S3 — before -> after
 {"title": "24 Years for Enron's CEO. Then It Became 14.", "template": "before → after",
  "hook": "24 YEARS.|THEN 14.", "lines": [
  L("Twenty-four years and four months. Enron's former CEO, Jeffrey Skilling, sentenced in two thousand six.",
    dict(type="verdict", kicker="OCTOBER 23, 2006", stamp="SENTENCED", big="24 yrs 4 mos", sub="Jeffrey K. Skilling"),
    show="24 years and 4 months. Enron's former CEO, Jeffrey Skilling, sentenced in 2006."),
  L("An appeals court threw out the sentence. Then the Supreme Court limited honest-services fraud, one theory against him, to bribes and kickbacks.",
    dict(type="quote", q="We therefore hold that §1346 covers only bribery and kickback schemes.", case="SKILLING v. UNITED STATES", doc="THE SUPREME COURT · 2010", cite=SRC_SC, size=46)),
  L("His convictions stood. In two thousand thirteen, a new sentence: fourteen years. He was released in two thousand nineteen.",
    dict(type="verdict", kicker="JUNE 21, 2013 · RESENTENCED", stamp="REDUCED", neutral=True, big="14 years", sub="released 2019"),
    show="His convictions stood. In 2013, a new sentence: 14 years. He was released in 2019."),
  END]},
]
from panfix import fix
for s in shorts: fix(s["lines"], "short")
for i, s in enumerate(shorts, 1):
    s["label"] = "SWORN"
    json.dump(s, open(os.path.join(HERE, f"short{i}.json"), "w"), indent=1, ensure_ascii=False)
    print(i, len(s["title"]), sum(len(l["say"].split()) for l in s["lines"]), "words", len(s["lines"]), "lines")
