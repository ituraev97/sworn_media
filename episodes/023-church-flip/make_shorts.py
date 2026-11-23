import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
def doc(key, kicker, src, pan=None):
    img, a, b = HL[key]
    c = (a + b) / 2
    return dict(type="doc", img=f"img/{img}.jpg", pan=pan or [max(0.0, round(c - 0.2, 3)), max(0.0, round(c - 0.14, 3))],
                hl=[0.0, a, 1.0, round(b - a, 4)], kicker=kicker, src=src)
def photo(img, caption, src, fit="contain"):
    return dict(type="photo", img=f"img/{img}.jpg", caption=caption, src=src, fit=fit)
S_IND = "Superseding Indictment, U.S. v. Garcia (N.D. Tex. 4:26-cr-146, Dkt. 35)"
S_PR = "USAO N.D. Tex. press release, Nov 20, 2026"
S_EX = "Gov't trial exhibit (draft chart), released by USAO N.D. Tex."
XK = "GOV'T TRIAL CHART · NAMES REDACTED"
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
def hook(img, **kw):
    d = dict(type="hook", img=f"img/{img}.jpg", pos="50% 0%", zoom=1.3334); d.update(kw); return d
GUILTY = dict(type="verdict", kicker="NOV 19, 2026 · FORT WORTH, TEX.", stamp="GUILTY", big="4 Counts", sub="Richard Reinaldo Garcia · wire fraud", at=0.1)
shorts = [
 # S1 — number reveal (face + number)
 {"title": "$683,000 for 3 Churches. Gov't Chart: \"Never Purchased.\"", "template": "face + number reveal",
  "lines": [
   L("Six hundred eighty-three thousand dollars, for three church buildings. According to the government's chart, none was ever purchased.",
     hook("h_face", tag="GUILTY", number="$683,000", label="3 CHURCHES|NEVER PURCHASED"),
     show="$683,000, for three church buildings. According to the government's chart, none was ever purchased."),
   L("Pastor Richard Garcia sold church flipping deals: renovate a church, sell it, pay the investor a set return.",
     doc("i_flip", "SUPERSEDING INDICTMENT · ALLEGATIONS", S_IND),
     show="Pastor Richard Garcia sold \"Church Flipping\" deals: renovate a church, sell it, pay the investor a set return."),
   L("One investor was told his churches had sold at a profit, the indictment says. The chart: proceeds from sale, zero.",
     photo("f_never", XK, S_EX),
     show="One investor was told his churches had sold at a profit, the indictment says. The chart: proceeds from sale, $0."),
   L("On November nineteenth, a federal jury in Fort Worth found Garcia guilty. More than seventy victims. More than six million dollars lost.",
     GUILTY, show="On November 19, a federal jury in Fort Worth found Garcia guilty. More than 70 victims. More than $6 million lost."),
   L("Would you invest with your pastor?", dict(type="end", cta="FULL CASE ON THE CHANNEL")),
  ]},
 # S2 — trailer: the money trail (chart-led)
 {"title": "Church Account to Mercedes-Benz: A Pastor's Money Trail", "template": "money trail (chart-led) · trailer",
  "lines": [
   L("A hundred twenty-five thousand dollars from an investor, into a church bank account. Here is where it went, according to the government.",
     hook("h_face2", tag="GUILTY", number="$125,000", label="INTO THE|CHURCH ACCOUNT"),
     show="$125,000 from an investor, into a church bank account. Here is where it went, according to the government."),
   L("Thirteen thousand to the pastor's personal account, which had started the week overdrawn.",
     photo("f_rg1", XK, S_EX), show="$13,000 to the pastor's personal account, which had started the week overdrawn."),
   L("From there: Panama. Mercedes-Benz Financial Services. Later, the Texas Rangers, baseball and concessions.",
     photo("f_rg2", XK, S_EX), show="From there: Panama. Mercedes-Benz Financial Services. Later, the Texas Rangers, \"baseball & concessions.\""),
   L("The Texarkana church in his deal? According to the government's chart, never purchased. Pastor Richard Garcia was found guilty on November nineteenth.",
     GUILTY, show="The Texarkana church in his deal? According to the government's chart, never purchased. Pastor Richard Garcia was found guilty on November 19."),
   L("What sentence would you give him? Full story on the channel.", dict(type="end", cta="FULL STORY ON THE CHANNEL")),
  ]},
 # S3 — paradox question (document-led)
 {"title": "Why Did Investors Call Their Money a \"Donation\"?", "template": "paradox question (document-led)",
  "lines": [
   L("Why would an investor call his money a donation? Because, prosecutors say, the pastor told him to.",
     hook("h_face3", tag="GUILTY", number="$6M+", label="70+ VICTIMS|PASTOR GUILTY"),
     show="Why would an investor call his money a \"donation\"? Because, prosecutors say, the pastor told him to."),
   L("Richard Garcia sold church flipping and concert deals, and had victims label payments as donations to Gracia Church.",
     doc("p_accounts", "U.S. ATTORNEY · N.D. TEX.", S_PR),
     show="Richard Garcia sold church flipping and concert deals, and had victims label payments as \"donations\" to Gracia Church."),
   L("One investor even got a donation letter, the indictment says, for money meant for church deals.",
     doc("i_donletter", "SUPERSEDING INDICTMENT", S_IND),
     show="One investor even got a Donation Letter, the indictment says, for money meant for church deals."),
   L("More than seventy victims. More than six million dollars. A jury found Garcia guilty on November nineteenth.",
     GUILTY, show="More than 70 victims. More than $6 million. A jury found Garcia guilty on November 19."),
   L("Would you have noticed?", dict(type="end", cta="FULL CASE ON THE CHANNEL")),
  ]},
]
for i, s in enumerate(shorts, 1):
    json.dump(s, open(os.path.join(HERE, f"short{i}.json"), "w"), indent=1, ensure_ascii=False)
    print(i, len(s["title"]), s["title"], sum(len(l["say"].split()) for l in s["lines"]), "words")
