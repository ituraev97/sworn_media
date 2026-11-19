import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
def doc(key, kicker, src, pan=None):
    img, a, b = HL[key]
    c = (a + b) / 2
    return dict(type="doc", img=f"img/{img}.jpg", pan=pan or [max(0.0, round(c - 0.2, 3)), max(0.0, round(c - 0.14, 3))],
                hl=[0.0, a, 1.0, round(b - a, 4)], kicker=kicker, src=src)
SRC_C = "Criminal complaint, U.S. v. Williams & Johnson (S.D.N.Y., Nov 17, 2026) — allegations"
SRC_PR = "U.S. Attorney's Office, S.D.N.Y. (Nov 18, 2026)"
C = "S.D.N.Y. COMPLAINT"
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
def hook(img, **kw):
    d = dict(type="hook", img=f"img/{img}.jpg", pos="50% 0%", zoom=1.3334); d.update(kw); return d
CHARGED = dict(type="verdict", kicker="NOV 18, 2026 · ARRESTED", stamp="CHARGED", big="Presumed innocent", sub="Williams · Johnson · 2 of 3 co-founders", neutral=True, at=0.1)
shorts = [
 # S1 — the text message (strongest, 10:00)
 {"title": "\"Let's Do 9.91\": How a $600M Fund Set Returns, Feds Say", "template": "verbatim quote + number reveal",
  "lines": [
  L("Six hundred million dollars from two thousand investors. And prosecutors say the monthly return was picked by text message.",
    hook("h_991", tag="BREAKING", number="$600M", label="RETURNS SET BY TEXT|PROSECUTORS ALLEGE"),
    show="$600 million from 2,000 investors. And prosecutors say the monthly return was picked by text message."),
  L("An employee asks: ten point oh one percent, does this sound right? The founder answers: let's do nine point nine one, bumped it up a bit.",
    doc("may14", C + " · MAY 14, 2026", SRC_C),
    show="An employee asks: \"10.01%, does this sound right?\" The founder answers: \"Let's do 9.91, bumped it up a bit.\""),
  L("On the dashboard, every month showed six to seven percent. Only minimal funds, the complaint says, went to trading.",
    doc("dashboard", C + " · ¶ 17", SRC_C),
    show="On the dashboard, every month showed 6% to 7%. Only minimal funds, the complaint says, went to trading."),
  L("On November eighteenth, both founders were arrested. They're presumed innocent.",
    CHARGED, show="On November 18, both founders were arrested. They're presumed innocent."),
  L("Would you have trusted six percent a month?",
    dict(type="end", cta="FULL CASE ON THE CHANNEL"), show="Would you have trusted 6% a month?"),
 ]},
 # S2 — where the money went (14:00)
 {"title": "$130M to One Founder: Where a $600M Fund's Money Went", "template": "number reveal + follow the money",
  "lines": [
  L("A hundred thirty million dollars. That's how much went to one founder's accounts, federal prosecutors allege, out of a six-hundred-million-dollar forex fund.",
    hook("h_130", tag="CHARGED", number="$130M+", label="TO ONE FOUNDER'S ACCOUNTS|PER THE COMPLAINT"),
    show="$130 million. That's how much went to one founder's accounts, federal prosecutors allege, out of a $600 million forex fund."),
  L("At least two hundred million, the complaint says, paid earlier investors with newer investors' money.",
    doc("ponzi200", C + " · ¶ 19(b)", SRC_C),
    show="At least $200 million, the complaint says, paid earlier investors with newer investors' money."),
  L("Over forty million went to the other founder. And the forex trading? Only minimal funds, the agent writes.",
    doc("minimal", C + " · ¶ 19(d)", SRC_C),
    show="Over $40 million went to the other founder. And the forex trading? \"Only minimal funds,\" the agent writes."),
  L("Phillip Williams and Devin Johnson were arrested November eighteenth. Both are presumed innocent.",
    CHARGED, show="Phillip Williams and Devin Johnson were arrested November 18. Both are presumed innocent."),
  L("Where do you think the rest went?",
    dict(type="end", cta="FULL CASE ON THE CHANNEL")),
 ]},
 # S3 — still taking money (18:00)
 {"title": "\"Accepting New Investors\": The Reply to an IRS Undercover", "template": "verbatim quote + how it ended",
  "lines": [
  L("We are accepting new investors at the moment. That was the reply an undercover I.R.S. employee got from a six-hundred-million-dollar fund, prosecutors say.",
    hook("h_new", tag="BREAKING", number="$600M", label="STILL TAKING MONEY|PROSECUTORS ALLEGE"),
    show="\"We are accepting new investors at the moment.\" That was the reply an undercover IRS employee got from a $600 million fund, prosecutors say."),
  L("By then, the complaint says, Backward Hat Capital had dissipated most investor assets, and withdrawals were stalling.",
    doc("dissipated", C + " · ¶ 26", SRC_C),
    show="By then, the complaint says, Backward Hat Capital had \"dissipated most investor assets\", and withdrawals were stalling."),
  L("Investors were told about longer processing times. Then about a third-party identity validator.",
    doc("nov13", C + " · NOV 13, 2026", SRC_C)),
  L("Five days later, on November eighteenth, both founders were arrested. They are presumed innocent.",
    CHARGED, show="5 days later, on November 18, both founders were arrested. They are presumed innocent."),
  L("What's the biggest red flag here?",
    dict(type="end", cta="FULL CASE ON THE CHANNEL")),
 ]},
]

def F(si, i, say=None, show=None):
    l = shorts[si]["lines"][i]
    if say is not None: l["say"] = say
    if show is not None: l["show"] = show
    elif say is not None: l.pop("show", None)
F(0, 0, "More than six hundred million dollars from more than two thousand investors. And prosecutors say the monthly return was picked by text message.",
  "$600M+ from more than 2,000 investors. And prosecutors say the monthly return was picked by text message.")
F(0, 1, "An employee texts: aggressive fund, ten point oh one percent, does this sound right? Later, prosecutors say, co-founder Phillip Williams replies: let's do nine point nine one, bumped it up a bit.",
  "An employee texts: \"Aggressive fund 10.01% / Does this sound right?\" Later, prosecutors say, co-founder Phillip Williams replies: \"… Let's do 9.91 bumped it up a bit\"")
F(0, 2, "On the dashboard, the complaint says, the monthly rate stayed between six point oh one and seven point two one percent. Only minimal funds, it says, went to forex trading.",
  "On the dashboard, the complaint says, the monthly rate stayed between 6.01% and 7.21%. \"Only minimal funds,\" it says, \"appear to have been potentially used for forex trading.\"")
F(0, 3, "On November eighteenth, two of its co-founders were arrested. They're charged, not convicted.",
  "On November 18, two of its co-founders were arrested. They're charged, not convicted.")
shorts[1]["title"] = "$130M+ to One Founder, Feds Allege: Where $600M Went"
F(1, 0, "More than a hundred thirty million dollars. That's how much went to one founder's accounts, federal prosecutors allege, from a forex firm that raised six hundred million.",
  "More than $130 million. That's how much went to one founder's accounts, federal prosecutors allege, from a forex firm that raised $600 million.")
F(1, 1, "At least about two hundred million, the complaint says, paid earlier investors with newer investors' money.",
  "At least about $200 million, the complaint says, paid earlier investors with newer investors' money.")
F(1, 2, "More than forty million, it says, went to accounts controlled by co-founder Devin Johnson. And the forex trading? Only minimal funds appear to have been potentially used for it, the agent writes.",
  "More than $40 million, it says, went to accounts controlled by co-founder Devin Johnson. And the forex trading? \"Only minimal funds appear to have been potentially used\" for it, the agent writes.")
F(2, 2, "Williams drafted an investor email about longer processing times, the complaint says. Then, on November thirteenth, he told investors about a third-party identity validator.",
  "Williams drafted an investor email about longer processing times, the complaint says. Then, on November 13, he told investors about \"a third-party identity validator.\"")
F(2, 3, "Five days later, on November eighteenth, two of its co-founders were arrested. They are charged, not convicted, and presumed innocent.",
  "5 days later, on November 18, two of its co-founders were arrested. They are charged, not convicted, and presumed innocent.")

F(0, 0, "More than six hundred million dollars from over two thousand investors. Prosecutors say the monthly return was picked by text.",
  "$600M+ from over 2,000 investors. Prosecutors say the monthly return was picked by text.")
F(0, 1, "An employee texts: aggressive fund, ten point oh one percent, does this sound right? Later, prosecutors say, co-founder Phillip Williams replies: let's do nine point nine one, bumped it up a bit.",
  "An employee texts: \"Aggressive fund 10.01% / Does this sound right?\" Later, prosecutors say, co-founder Phillip Williams replies: \"… Let's do 9.91 bumped it up a bit\"")
F(0, 2, "The dashboard, the complaint says, always showed six point oh one to seven point two one percent a month.",
  "The dashboard, the complaint says, always showed 6.01% to 7.21% a month.")
F(1, 0, "More than a hundred thirty million dollars went to one founder's accounts, prosecutors allege, from a forex firm that raised six hundred million.",
  "More than $130 million went to one founder's accounts, prosecutors allege, from a forex firm that raised $600 million.")
F(1, 2, "More than forty million, it says, went to co-founder Devin Johnson's accounts. The forex trading? Only minimal funds, the agent writes.",
  "More than $40 million, it says, went to co-founder Devin Johnson's accounts. The forex trading? \"Only minimal funds,\" the agent writes.")
F(2, 0, "We are accepting new investors at the moment. That's the reply an undercover I.R.S. employee got from a six-hundred-million-dollar fund, prosecutors say.",
  "\"We are accepting new investors at the moment.\" That's the reply an undercover IRS employee got from a $600 million fund, prosecutors say.")
F(2, 1, "By then, the complaint says, the fund had dissipated most investor assets.",
  "By then, the complaint says, the fund had \"dissipated most investor assets.\"")
F(2, 3, "Five days later, two of its co-founders were arrested. Charged, not convicted.",
  "5 days later, two of its co-founders were arrested. Charged, not convicted.")

del shorts[0]["lines"][2]

F(2, 0, "We are accepting new investors at the moment. That's the reply an undercover I.R.S. employee got, prosecutors say.",
  "\"We are accepting new investors at the moment.\" That's the reply an undercover IRS employee got, prosecutors say.")
for i, s in enumerate(shorts, 1):
    json.dump(s, open(os.path.join(HERE, f"short{i}.json"), "w"), indent=1, ensure_ascii=False)
    print(i, len(s["title"]), s["title"], sum(len(l["say"].split()) for l in s["lines"]), "words")
