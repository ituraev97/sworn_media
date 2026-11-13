import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
def hl(name, i=0):
    a, b = HL[name][i]
    return [0.0, a, 1.0, round(b - a, 4)]
def doc(img, kicker, src, i=0):
    return dict(type="doc", img=f"img/{img}.jpg", pan=[0.0, 0.1], hl=hl(img, i), kicker=kicker, src=src)
CASE = "UNITED STATES v. MILTON"
SRC_GM = "Gov't Sentencing Memorandum, U.S. v. Milton (S.D.N.Y. 2023)"
SRC_SEC = "SEC v. Milton, Complaint (S.D.N.Y. 2021) — allegations"
SRC_REST = "Gov't restitution letter, U.S. v. Milton (Mar 14, 2025)"
SRC_PARD = "Executive Grant of Clemency (Mar 2025), U.S. v. Milton"
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
END = L("Real trials. Real evidence. The verdict.", dict(type="end"))
GUILTY = dict(type="verdict", kicker="S.D.N.Y. · OCTOBER 14, 2022", stamp="GUILTY", big="3 of 4 counts", sub="United States v. Trevor Milton")
shorts = [
 # S1 — verbatim quote
 {"title": "\"Behold, the Nikola One in Motion.\" It Rolled Downhill.", "template": "verbatim quote",
  "hook": "\"BEHOLD, THE NIKOLA|ONE IN MOTION.\"", "lines": [
  L("Behold, the Nikola One in motion. That was the caption in January twenty eighteen, on a video of Nikola's semi-truck cruising down a road.",
    dict(type="quote", q="Behold, the Nikola One in motion.", case=CASE, doc="NIKOLA TWEET · JAN 25, 2018", cite="As quoted in " + SRC_SEC, size=60),
    show="\"Behold, the Nikola One in motion.\" That was the caption in January 2018, on a video of Nikola's semi-truck cruising down a road."),
  L("According to the SEC, the truck could not run under its own power. It was towed to the top of an incline and filmed rolling down.",
    doc("sec_20", "SEC v. MILTON · COMPLAINT", SRC_SEC, 0)),
  L("Founder Trevor Milton had said it would be the first time anyone has seen the Nikola truck move. In twenty twenty-two, a jury convicted him of fraud.",
    GUILTY, show="Founder Trevor Milton had said it would be \"the first time anyone has seen the Nikola truck move.\" In 2022, a jury convicted him of fraud."),
  END]},
 # S2 — dollar-figure reveal
 {"title": "$660.8 Million Restitution Request. 13 Days Later, a Pardon.", "template": "dollar-figure reveal",
  "hook": "$660.8 MILLION|THEN A PARDON", "lines": [
  L("Six hundred sixty point eight million dollars. That is the restitution prosecutors asked Nikola founder Trevor Milton to pay shareholders, on March fourteenth, twenty twenty-five.",
    doc("rest", "U.S. ATTORNEY, S.D.N.Y. · MAR 14, 2025", SRC_REST, 1),
    show="$660.8 million. That is the restitution prosecutors asked Nikola founder Trevor Milton to pay shareholders, on March 14, 2025."),
  L("A jury had convicted him of fraud. A judge had given him four years. He was free on bail, appealing.",
    dict(type="verdict", kicker="DECEMBER 18, 2023", stamp="SENTENCED", big="4 years", sub="Free on bail pending appeal")),
  L("Thirteen days later came a full and unconditional pardon, covering any fines, forfeitures and restitution ordered by the court.",
    doc("pard", "EXECUTIVE GRANT OF CLEMENCY · MAR 2025", SRC_PARD, 1),
    show="13 days later came \"A Full and Unconditional Pardon,\" with \"remission of any and all fines, penalties, forfeitures, and restitution ordered by the court.\""),
  END]},
 # S3 — before -> after
 {"title": "\"Fully Functions and Works\" vs. \"Missing Critical Parts\"", "template": "before → after",
  "hook": "\"FULLY FUNCTIONS|AND WORKS\"", "lines": [
  L("Fully functions and works, which is really incredible. That is how, according to the SEC, Trevor Milton described Nikola's prototype semi-truck in twenty sixteen.",
    dict(type="quote", q="fully functions and works which is really incredible.", case=CASE, doc="TREVOR MILTON · DEC 1, 2016", cite="As quoted in " + SRC_SEC, size=56),
    show="\"Fully functions and works which is really incredible.\" That is how, according to the SEC, Trevor Milton described Nikola's prototype semi-truck in 2016."),
  L("What prosecutors told the court the trial showed: it was neither functioning nor designed to run on hydrogen, and it was missing critical parts.",
    doc("gm_6", "GOV'T SENTENCING MEMORANDUM", SRC_GM, 1),
    show="What prosecutors told the court the trial showed: it was \"neither functioning nor even designed to be hydrogen-powered and was missing critical parts.\""),
  L("The verdict: guilty on three of four fraud counts. Four years. Then, in twenty twenty-five, a presidential pardon.",
    GUILTY, show="The verdict: guilty on three of four fraud counts. Four years. Then, in 2025, a presidential pardon."),
  END]},
]
from panfix import fix
for s in shorts: fix(s["lines"], "short")
if __name__ == "__main__":
    for i, s in enumerate(shorts, 1):
        s["label"] = "SWORN"
        json.dump(s, open(os.path.join(HERE, f"short{i}.json"), "w"), indent=1, ensure_ascii=False)
        print(i, len(s["title"]), sum(len(l["say"].split()) for l in s["lines"]), "words", len(s["lines"]), "lines")
