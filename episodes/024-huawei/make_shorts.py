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
S_S4 = "Superseding Indictment S-4, U.S. v. Huawei (E.D.N.Y. 18-cr-457, Dkt. 689)"
S_PR = "U.S. Dept. of Justice press release 26-1413, Nov 24, 2026"
S_EX = "Trial exhibit released by the Justice Department with the verdict"
S_AFP = "IBTimes, citing AFP, Nov 24, 2026"
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
def hook(img, **kw):
    d = dict(type="hook", img=f"img/{img}.jpg", pos="50% 0%", zoom=1.3334); d.update(kw); return d
GUILTY = dict(type="verdict", kicker="NOV 24, 2026 · BROOKLYN, N.Y.", stamp="GUILTY", big="Huawei", sub="+ 3 subsidiaries · E.D.N.Y. · sentencing Sept 14, 2027", at=0.1)
shorts = [
 # S1 — number reveal (evidence photo + number) — T 10:00
 {"title": "10 of 12 Charges: Huawei Found Guilty in Brooklyn", "template": "evidence photo + number reveal",
  "lines": [
   L("Ten of twelve, according to AFP. A federal jury in Brooklyn has found Huawei guilty.",
     hook("h_tappy", tag="GUILTY", number="10 OF 12", label="CHARGES|HUAWEI CONVICTED"),
     show="10 of 12, according to AFP. A federal jury in Brooklyn has found Huawei guilty."),
   L("Bank fraud. Violating sanctions on Iran. Money laundering. Conspiracy to steal trade secrets.",
     dict(type="big", kicker="CONVICTED OF · PER DOJ", lines=["Bank fraud.", "Iran sanctions.", "Money laundering.", "Trade-secret|conspiracy."], src=S_PR)),
   L("The Justice Department says a Huawei employee carried part of a T-Mobile testing robot out of a lab in his backpack.",
     photo("tappy", "IMAGE RELEASED BY THE JUSTICE DEPARTMENT · T-MOBILE “TAPPY” TEST ROBOT", S_EX)),
   L("According to AFP, the jury acquitted Huawei of racketeering conspiracy and conspiracy to obstruct justice. Sentencing is set for September twenty twenty-seven.",
     GUILTY, show="According to AFP, the jury acquitted Huawei of racketeering conspiracy and conspiracy to obstruct justice. Sentencing is set for September 2027."),
   L("What should a punishment for a company look like?", dict(type="end", cta="FULL CASE ON THE CHANNEL")),
  ]},
 # S2 — trailer: the robot arm (document-led) — T 18:00
 {"title": "Robot Arm in a Laptop Bag, Indictment Says: Huawei Verdict", "template": "document-led · trailer",
  "lines": [
   L("May twenty-ninth, twenty thirteen. According to the indictment, an employee put a robot arm into a laptop bag, and walked it out of a lab.",
     hook("h_arm", tag="INDICTMENT SAYS", number="MAY 29, 2013", label="ROBOT ARM|LAPTOP BAG"),
     show="May 29, 2013. According to the indictment, an employee put a robot arm into a laptop bag, and walked it out of a lab."),
   L("The Justice Department's announcement says backpack. It says the robot was T-Mobile's.",
     photo("tappy", "IMAGE RELEASED BY THE JUSTICE DEPARTMENT · T-MOBILE “TAPPY” TEST ROBOT", S_EX)),
   L("Photographs and measurements went to engineers, the indictment says.",
     doc("s_arm", "SUPERSEDING INDICTMENT · ALLEGATIONS · ¶ 38", S_S4)),
   L("The indictment says a Huawei Device USA report called it isolated incidents. On November twenty-fourth, a jury convicted Huawei of conspiring to steal trade secrets.",
     doc("s_isolated", "SUPERSEDING INDICTMENT · ALLEGATIONS · ¶ 39", S_S4),
     show="The indictment says a Huawei Device USA report called it \"isolated incidents.\" On November 24, a jury convicted Huawei of conspiring to steal trade secrets."),
   L("Isolated, or a scheme? Full story on the channel.", dict(type="end", cta="FULL STORY ON THE CHANNEL")),
  ]},
 # S3 — number reveal (document) — T+1 10:00
 {"title": "$100M Through U.S. Banks, Feds Say: Huawei's Skycom", "template": "number reveal (document-led)",
  "lines": [
   L("More than a hundred million dollars. That's what one bank cleared through the U.S. for a company called Skycom, the indictment says.",
     hook("h_100m", tag="INDICTMENT SAYS", number="$100M+", label="CLEARED THROUGH|U.S. BANKS"),
     show="More than $100 million. That's what one bank cleared through the U.S. for a company called Skycom, the indictment says."),
   L("Skycom, the indictment says, was Huawei's unofficial subsidiary in Iran.",
     doc("s_unoff", "SUPERSEDING INDICTMENT · ALLEGATIONS · ¶ 67", S_S4)),
   L("The Justice Department says Huawei lied to banks to obtain billions of U.S. dollars.",
     doc("p_banks", "U.S. DEPARTMENT OF JUSTICE · NOV 24, 2026", S_PR)),
   L("On November twenty-fourth, a jury convicted Huawei of bank fraud, sanctions violations and money laundering.",
     GUILTY, show="On November 24, a jury convicted Huawei of bank fraud, sanctions violations and money laundering."),
   L("Would a bank believe a denial? Full case on the channel.", dict(type="end", cta="FULL CASE ON THE CHANNEL")),
  ]},
 # S4 — paradox/paper-trail (text-led) — T+1 18:00
 {"title": "DOJ Says “ocsic” (Cisco Backwards) Was in Huawei's Code", "template": "paradox · text-led",
  "lines": [
   L("O, C, S, I, C. That is Cisco, spelled backwards. And the Justice Department says it was written in Huawei's code.",
     hook("h_cisco", tag="DOJ SAYS", number="“ocsic”", label="CISCO'S NAME|BACKWARDS"),
     show="O, C, S, I, C. That is Cisco, spelled backwards. And the Justice Department says it was written in Huawei's code."),
   L("Prosecutors say Huawei copied Cisco router source code, which the announcement calls Cisco's crown jewel.",
     doc("p_cisco", "U.S. DEPARTMENT OF JUSTICE · NOV 24, 2026", S_PR)),
   L("In an effort to hide it, the announcement says, engineers left Cisco's notes about the code behind, and called Cisco by its name backwards.",
     dict(type="big", kicker="DOJ ANNOUNCEMENT · TRIAL EVIDENCE", lines=["Cisco’s notes", "left in the code.", "Cisco, backwards:", "“ocsic”"], src=S_PR)),
   L("On November twenty-fourth, a federal jury in Brooklyn convicted Huawei of conspiracy to steal trade secrets.",
     GUILTY, show="On November 24, a federal jury in Brooklyn convicted Huawei of conspiracy to steal trade secrets."),
   L("Would you have caught it?", dict(type="end", cta="FULL CASE ON THE CHANNEL")),
  ]},
]
for i, s in enumerate(shorts, 1):
    json.dump(s, open(os.path.join(HERE, f"short{i}.json"), "w"), indent=1, ensure_ascii=False)
    print(i, len(s["title"]), s["title"], sum(len(l["say"].split()) for l in s["lines"]), "words")
