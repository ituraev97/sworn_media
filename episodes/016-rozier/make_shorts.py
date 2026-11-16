import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
def hl(name, i=0):
    a, b = HL[name][i]
    return [0.0, a, 1.0, round(b - a, 4)]
def doc(img, kicker, src, i=0, pan=None):
    return dict(type="doc", img=f"img/{img}.jpg", pan=pan or [0.0, 0.1], hl=hl(img, i), kicker=kicker, src=src)
CASE = "UNITED STATES v. ROZIER"
SRC_PR = "U.S. Attorney's Office, E.D.N.Y. (Oct 23, 2025)"
SRC_I = "Indictment, E.D.N.Y. 25-cr-323, ECF 17"
SRC_S = "Superseding Indictment, ECF 101 (May 28, 2026)"
SRC_G144 = "Gov't filing, ECF 144 (Aug 26, 2026)"
SRC_G166 = "Gov't letter, ECF 166 (Nov 3, 2026)"
SRC_D169 = "Rozier motion in limine, ECF 169 (Nov 12, 2026)"
SRC_COV = "Covers (May 28, 2026)"
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
TRIAL = dict(type="verdict", kicker="BROOKLYN · TRIAL SET FOR FEB 8, 2027", stamp="CHARGED", big="Not guilty plea", sub="Terry Rozier · presumed innocent", neutral=True)
shorts = [
 # S1 — the number (strongest, 10:00)
 {"title": "$100,000 to Leave a Game Early? The Terry Rozier Case", "template": "number reveal (alleged bribe)",
  "lines": [
  L("A hundred thousand dollars to leave an NBA game early. That's what prosecutors say Terry Rozier agreed to.",
    dict(type="hook", img="img/rozier_hook.jpg", pos="50% 0%", zoom=1.3334, tag="CHARGED", number="$100K", label="ALLEGED BRIBE|TO LEAVE A GAME"),
    show="$100,000 to leave an NBA game early. That's what prosecutors say Terry Rozier agreed to."),
  L("March twenty-third, twenty twenty-three. He walked off after nine minutes and thirty-four seconds. He wasn't on the injury report.",
    doc("ind_12", "THE INDICTMENT · PARAGRAPH 41", SRC_I, 0),
    show="March 23, 2023. He walked off after 9 minutes and 34 seconds. He wasn't on the injury report."),
  L("The government says more than two hundred thousand dollars was bet on his unders.",
    dict(type="stat", kicker="ROZIER'S UNDERS", value="$200K+", label="IN BETS, PROSECUTORS SAY", src=SRC_PR),
    show="The government says more than $200,000 was bet on his unders."),
  L("Rozier says he was hurt, and never knew about any bets. Trial: February eighth.", TRIAL,
    show="Rozier says he was hurt, and never knew about any bets. Trial: February 8."),
  L("Injury, or a setup? Tell me below.", dict(type="end", cta="FULL CASE ON THE CHANNEL")),
 ]},
 # S2 — the four rebounds twist (14:00)
 {"title": "Four Rebounds Cut the Alleged Bribe to $70K, Feds Say", "template": "twist (one stat, two stories)",
  "lines": [
  L("Four rebounds. Prosecutors say that one stat cut Terry Rozier's alleged bribe from a hundred thousand to seventy thousand dollars.",
    dict(type="hook", img="img/sup_13.jpg", pos="50% 38%", zoom=1.9, tag="CHARGED", number="$70K", label="AFTER 4 REBOUNDS|PROSECUTORS SAY"),
    show="Four rebounds. Prosecutors say that one stat cut Terry Rozier's alleged bribe from $100,000 to $70,000."),
  L("He left the game after nine minutes. Points, assists, threes: all under the betting lines.",
    doc("ind_12", "THE INDICTMENT · PARAGRAPH 41", SRC_I, 1),
    show="He left the game after nine minutes. Points, assists, threes: all under the betting lines."),
  L("But four rebounds went over. Some bets lost. So, the superseding indictment alleges, the bribe was negotiated down.",
    doc("sup_13", "SUPERSEDING INDICTMENT · PARAGRAPH 44", SRC_S, 0)),
  L("His lawyers say the same stat shows he played hard, the opposite of what bettors wanted.",
    dict(type="big", kicker="THE DEFENSE · NOV 12, 2026", lines=["Same stat.", "Opposite|story."], src=SRC_D169)),
  L("He pleaded not guilty. So who's right? Tell me below.", dict(type="end", cta="FULL CASE ON THE CHANNEL")),
 ]},
 # S3 — the text (18:00)
 {"title": "\"Dont Tell Chum Bout the Bet\": The Disputed Text", "template": "verbatim quote (contested text)",
  "lines": [
  L("Dont tell Chum bout the bet. Chum is Terry Rozier's nickname. And this one text may decide his case.",
    dict(type="hook", img="img/g144_8.jpg", pos="50% 96%", zoom=1.9, tag="CHARGED", number="\"THE BET\"", label="\"DONT TELL CHUM|BOUT THE BET\""),
    show="\"Dont tell Chum bout the bet.\" \"Chum\" is Terry Rozier's nickname. And this one text may decide his case."),
  L("Prosecutors say his friend Deniro Laster sold word of Rozier's early exit from a March twenty twenty-three game.",
    doc("ind_8", "THE INDICTMENT · PARAGRAPH 36", SRC_I, 0),
    show="Prosecutors say his friend Deniro Laster sold word of Rozier's early exit from a March 2023 game."),
  L("Laster sent that text from Philadelphia. The defense says it proves Rozier never knew about the bets.",
    dict(type="big", kicker="THE DEFENSE", lines=["Why hide it", "from Chum?"], src=SRC_D169)),
  L("The government says the text has nothing to do with sports gambling.",
    doc("g144_8", "GOVERNMENT FILING · FOOTNOTE 2", SRC_G144, 1)),
  L("Trial is set for February. What do you think it means? Tell me below.", dict(type="end", cta="FULL CASE ON THE CHANNEL")),
 ]},
]
from panfix import fix
if __name__ == "__main__":
    for i, s in enumerate(shorts, 1):
        fix(s["lines"], "short")
        json.dump({"title": s["title"], "template": s["template"], "lines": s["lines"]}, open(os.path.join(HERE, f"short{i}.json"), "w"), indent=1, ensure_ascii=False)
        print(i, len(s["title"]), s["title"], sum(len(l["say"].split()) for l in s["lines"]), "words")
