import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
def hl(name, i=0):
    a, b = HL[name][i]
    return [0.0, a, 1.0, round(b - a, 4)]
def doc(img, kicker, src, i=0, pan=None):
    return dict(type="doc", img=f"img/{img}.jpg", pan=pan or [0.0, 0.1], hl=hl(img, i), kicker=kicker, src=src)
SRC_P = "U.S. Attorney's Office, E.D. La. (Nov 17, 2026)"
SRC_I = "U.S. Attorney's Office, E.D. La. (Dec 23, 2024)"
PLEA = "U.S. ATTORNEY · NOV 17, 2026"
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
HOOK = dict(type="hook", img="img/earl_hook.jpg", pos="50% 0%", zoom=1.0)
def hook(**kw):
    d = dict(HOOK); d.update(kw); return d
shorts = [
 # S1 — the number + the plea (strongest, 10:00)
 {"title": "$1.5M–$3M Stolen From Earl Thomas: Both Plead Guilty", "template": "number reveal + verdict",
  "lines": [
  L("Up to three million dollars stolen, prosecutors say, from the man news reports identify as Super Bowl champion Earl Thomas. His estranged wife and her boyfriend just pleaded guilty.",
    hook(tag="BREAKING", number="UP TO $3M", label="STOLEN FROM EARL THOMAS|BOTH PLEADED GUILTY"),
    show="Up to $3 million stolen, prosecutors say, from the man news reports identify as Super Bowl champion Earl Thomas. His estranged wife and her boyfriend just pleaded guilty."),
  L("They opened accounts in his name. Her boyfriend practiced signing it.",
    doc("plea", PLEA, SRC_P, 4)),
  L("His union payments were redirected. One check: eight hundred eighty-five thousand, four hundred nineteen dollars.",
    doc("plea", PLEA, SRC_P, 5),
    show="His union payments were redirected. One check: $885,419."),
  L("On November twelfth, both pleaded guilty to wire fraud conspiracy. Up to five years each on that count.",
    dict(type="verdict", kicker="NEW ORLEANS · NOV 12, 2026", stamp="PLEADED GUILTY", big="Up to 5 years", sub="wire fraud conspiracy · each", at=0.1),
    show="On November 12, both pleaded guilty to wire fraud conspiracy. Up to 5 years each on that count."),
  L("What sentence is fair? Tell me below.",
    dict(type="end", cta="FULL CASE ON THE CHANNEL")),
 ]},
 # S2 — the Rolls-Royce arrest (14:00)
 {"title": "\"Driving a Rolls Royce\": The Man Using Earl Thomas's Name", "template": "verbatim quote + how he got caught",
  "lines": [
  L("More than seven hundred thousand dollars, withdrawn in Earl Thomas's name, reports say. Then the man behind it drove a Rolls-Royce to the credit union.",
    hook(tag="BREAKING", number="$700K+", label="WITHDRAWN IN HIS NAME|THEN: THE ROLLS-ROYCE"),
    show="More than $700,000, withdrawn in Earl Thomas's name, reports say. Then the man behind it drove a Rolls-Royce to the credit union."),
  L("The credit union had already called the sheriff. Kevin Thompson arrived in a Rolls-Royce fraudulently obtained from the victim.",
    doc("plea", PLEA, SRC_P, 11)),
  L("The account was in the victim's name. The phone number was Thompson's.",
    doc("plea", PLEA, SRC_P, 12)),
  L("This month, he and Thomas's estranged wife pleaded guilty.",
    dict(type="verdict", kicker="NEW ORLEANS · NOV 12, 2026", stamp="PLEADED GUILTY", big="Wire fraud conspiracy", sub="Kevin J. Thompson · Nina Thomas", at=0.1)),
  L("Should the bank have caught it sooner? Tell me below.",
    dict(type="end", cta="FULL CASE ON THE CHANNEL")),
 ]},
 # S3 — the search warrant (18:00)
 {"title": "3,716 Grams and $228,000 Cash: Inside the Earl Thomas Case", "template": "number reveal (the search)",
  "lines": [
  L("Three thousand seven hundred sixteen grams of cocaine. Found in the home of the man who used Earl Thomas's identity.",
    hook(tag="BREAKING", number="3,716 G", label="SEIZED FROM THE HOME OF|THE MAN WHO USED HIS NAME"),
    show="3,716 grams of cocaine. Found in the home of the man who used Earl Thomas's identity."),
  L("Plus a pistol, and two hundred twenty-eight thousand dollars in cash.",
    doc("plea", PLEA, SRC_P, 14),
    show="Plus a pistol, and $228,000 in cash."),
  L("Kevin Thompson pleaded guilty to the cocaine count. Five years minimum, up to forty.",
    doc("plea", PLEA, SRC_P, 16),
    show="Kevin Thompson pleaded guilty to the cocaine count. 5 years minimum, up to 40."),
  L("And, with Thomas's estranged wife, to wire fraud conspiracy.",
    dict(type="verdict", kicker="NEW ORLEANS · NOV 12, 2026", stamp="PLEADED GUILTY", big="Wire fraud conspiracy", sub="+ cocaine count · Kevin J. Thompson", at=0.1)),
  L("What should his sentence be? Tell me below.",
    dict(type="end", cta="FULL CASE ON THE CHANNEL")),
 ]},
]
from panfix import fix
if __name__ == "__main__":
    for i, s in enumerate(shorts, 1):
        fix(s["lines"], "short")
        json.dump(s, open(os.path.join(HERE, f"short{i}.json"), "w"), indent=1, ensure_ascii=False)
        print(i, len(s["title"]), s["title"], sum(len(l["say"].split()) for l in s["lines"]), "words")
