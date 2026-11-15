import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
def hl(name, i=0):
    a, b = HL[name][i]
    return [0.0, a, 1.0, round(b - a, 4)]
def doc(img, kicker, src, i=0, pan=None):
    return dict(type="doc", img=f"img/{img}.jpg", pan=pan or [0.0, 0.1], hl=hl(img, i), kicker=kicker, src=src)
CASE = "UNITED STATES v. CHEN"
SRC_S = "U.S. Attorney's Office, S.D. Cal. (Nov 13, 2026)"
SRC_I = "U.S. Attorney's Office, S.D. Cal. (Jul 31, 2024)"
SRC_CP = "U.S. Attorney's Office, S.D. Cal. (Apr 2, 2026)"
SRC_R = "U.S. Attorney's Office, S.D. Cal. (Aug 27, 2025)"
SRC_YT = "YouTube Data API (Nov 15, 2026)"
SRC_SL = "DOJ sentencing slide (Nov 13, 2026)"
PR = "U.S. ATTORNEY · S.D. CAL. · "
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
SENT = dict(type="verdict", kicker="SAN DIEGO · NOV 13, 2026", stamp="SENTENCED", big="78 months", sub="Jiandong Chen, aka \"Little Tiger\"")
shorts = [
 # S1 — number + the sting (strongest, 10:00)
 {"title": "78 Months: The Scam Courier YouTubers Caught on Camera", "template": "number reveal + sting",
  "lines": [
  L("Seventy-eight months in prison, for the cash courier YouTubers confronted on camera.",
    dict(type="hook", img="img/chen_face.jpg", pos="50% 0%", zoom=0.85, tag="SENTENCED", number="78 MONTHS", label="CAUGHT ON YOUTUBE|NOW SENTENCED"),
    show="78 months in prison, for the cash courier YouTubers confronted on camera."),
  L("In July twenty twenty-three, Jiandong Chen, called Little Tiger, came to collect cash he thought was from an elderly victim.",
    doc("chenplea", PR + "APRIL 2, 2026", SRC_CP, 1),
    show="In July 2023, Jiandong Chen, called \"Little Tiger,\" came to collect cash he thought was from an elderly victim."),
  L("Trilogy Media confronted him instead. One point four million views.",
    dict(type="big", kicker="TRILOGY MEDIA · 2023", lines=["1.4 million", "views.|Still collecting."], src=SRC_YT + " · " + SRC_S),
    show="Trilogy Media confronted him instead. 1.4 million views."),
  L("Prosecutors say he kept going until federal agents encountered him that December.",
    doc("sent", PR + "NOVEMBER 13, 2026", SRC_S, 3)),
  L("On November thirteenth, with both YouTubers in court, a San Diego judge sentenced him.", SENT,
    show="On November 13, with both YouTubers in court, a San Diego judge sentenced him."),
  L("Was six and a half years enough? Tell me below.", dict(type="end", cta="FULL CASE ON THE CHANNEL")),
 ]},
 # S2 — the refund trick (14:00)
 {"title": "$27 Million From 2,000 Seniors: The Fake Refund Trick", "template": "number + how it works",
  "lines": [
  L("More than twenty-seven million dollars from about two thousand seniors. One of the most frequent tricks: a refund that never existed.",
    dict(type="hook", img="img/cash_count.jpg", pos="50% 45%", zoom=1.8, tag="SENTENCED", number="$27M", label="THE FAKE REFUND|2,000 SENIORS"),
    show="More than $27 million from about 2,000 seniors. One of the most frequent tricks: a refund that never existed."),
  L("A call or pop-up says you're owed a small refund. Then the caller pretends to over-refund you by accident.",
    
    doc("chenplea", PR + "APRIL 2, 2026", SRC_CP, 0)),
  L("Send back the difference, they say. In cash, by express mail.",
    dict(type="big", kicker="THE REFUND SCAM", lines=["Send back", "the|difference."], src=SRC_CP)),
  L("There was no refund. Victims sent their own money, to couriers with fake IDs.",
    doc("ind", PR + "JULY 31, 2024", SRC_I, 2)),
  L("One courier, Jiandong Chen, just got seventy-eight months.", SENT,
    show="One courier, Jiandong Chen, just got 78 months."),
  L("Has your family gotten this call? Tell me below.", dict(type="end", cta="FULL CASE ON THE CHANNEL")),
 ]},
 # S3 — verbatim quote (18:00)
 {"title": "\"Not All Heroes Wear Capes. Some Have YouTube Channels.\"", "template": "verbatim quote",
  "lines": [
  L("Not all heroes wear capes. Some have YouTube channels. A U.S. Attorney said that in twenty twenty-five, about scambaiters.",
    dict(type="hook", img="img/chen_face.jpg", pos="50% 0%", zoom=0.85, tag="SENTENCED", number="78 MONTHS", label="\"SOME HAVE|YOUTUBE CHANNELS\""),
    show="\"Not all heroes wear capes. Some have YouTube channels.\" A U.S. Attorney said that in 2025, about scambaiters."),
  L("Scammer Payback and Trilogy Media baited fraudsters and confronted them on camera.",
    doc("ring65", PR + "AUGUST 27, 2025", SRC_R, 3)),
  L("Prosecutors say their videos helped identify three defendants in a sixty-five million dollar ring.",
    show="Prosecutors say their videos helped identify three defendants in a $65 million ring."),
  L("In twenty twenty-three, Trilogy Media confronted a courier known as Little Tiger.",
    dict(type="photo", img="img/slide_0222.jpg", caption="DOJ SENTENCING SLIDE · 2/22/2023", src=SRC_SL, fit="contain"),
    show="In 2023, Trilogy Media confronted a courier known as \"Little Tiger.\""),
  L("On November thirteenth, with them in court, he got seventy-eight months.", SENT,
    show="On November 13, with them in court, he got 78 months."),
  L("Should police team up with scambaiters more? Tell me below.", dict(type="end", cta="FULL CASE ON THE CHANNEL")),
 ]},
]
from panfix import fix
if __name__ == "__main__":
    for i, s in enumerate(shorts, 1):
        fix(s["lines"], "short")
        json.dump({"title": s["title"], "template": s["template"], "lines": s["lines"]}, open(os.path.join(HERE, f"short{i}.json"), "w"), indent=1, ensure_ascii=False)
        print(i, len(s["title"]), s["title"], sum(len(l["say"].split()) for l in s["lines"]), "words")
