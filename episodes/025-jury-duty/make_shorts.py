import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
SRC_PR = "U.S. Dept. of Justice press release, Nov 24, 2026"
SRC_SG = "DOJ Criminal Division anti-scam surge page"
SRC_AF = "Affidavit, D.N.J. Mag. No. 26-8230, Doc. 1 (Nov 5, 2026)"
def doc(key, kicker, src=SRC_AF, pan=None):
    img, a, b = HL[key]; c = (a + b) / 2
    return dict(type="doc", img=f"img/{img}.jpg", pan=pan or [max(0.0, round(c - 0.2, 3)), max(0.0, round(c - 0.14, 3))], hl=[0.0, a, 1.0, round(b - a, 4)], kicker=kicker, src=src)
def fig(img, kicker, pan=(0.0, 0.2), src=SRC_AF): return dict(type="doc", img=f"img/{img}.jpg", pan=list(pan), kicker=kicker, src=src)
def clip(n, frm, label): return dict(type="clip", file=f"footage/{n}.mp4", **{"from": frm}, label=label)
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
def hook(img, **kw):
    d = dict(type="hook", img=f"img/{img}.jpg", pos="50% 0%", zoom=1.3334); d.update(kw); return d
LB_DOJ = "Source: U.S. Department of Justice · press conference · Nov 24, 2026"
shorts = [
 {"title": "DOJ's 800+ Defendant Crackdown Singles Out Prison Calls", "template": "number reveal (footage hook)",
  "lines": [
   L("More than eight hundred defendants. More than four hundred cases. The Justice Department calls it its largest-ever crackdown on scammers.", hook("h_doj", tag="DOJ SAYS", number="800+", label="DEFENDANTS|SCAM CRACKDOWN"), show="More than 800 defendants. More than 400 cases. The Justice Department calls it its largest-ever crackdown on scammers."),
   L("It singled out one scheme. Fake jury duty calls. In these cases, prosecutors say the callers were Georgia prison gang members.", clip("doj_p01", 6.0, LB_DOJ)),
   L("A federal affidavit reproduces part of a handwritten script. It says Georgia officials found it in an inmate's cell.", fig("aff_p08", "AFFIDAVIT · ALLEGATIONS · FIGURE 1", (0.0, 0.1))),
   L("The F.T.C. counts more than thirty thousand jury duty impostor complaints since twenty twenty-one, with losses above forty million dollars.", dict(type="stat", kicker="FTC DATA, AS CITED IN THE AFFIDAVIT", value="$40M+", label="reported losses · 30,000+ complaints · 2021–2026", src=SRC_AF), show="The FTC counts more than 30,000 jury duty impostor complaints since 2021, with losses above $40 million."),
   L("Would you have hung up?", dict(type="end", cta="FULL CASE ON THE CHANNEL")),
  ]},
 {"title": "Affidavit Details Fake Court Sites: “.gov or .org”", "template": "document-led · trailer",
  "lines": [
   L("Only dot gov is official. The postal inspector says three court-imitating sites changed the banner to say dot gov or dot org.", hook("h_banner", tag="AFFIDAVIT SAYS", number=".GOV or .ORG", label="FAKE COURT|WEBSITE BANNER"), show="Only .gov is official. The postal inspector says three court-imitating sites changed the banner to say .gov or .org."),
   L("The real banner says a dot gov website belongs to an official government organization. The affidavit says the imitation sites added dot org.", doc("banner", "AFFIDAVIT · ALLEGATIONS · ¶ 46")),
   L("The affidavit says three sites copied the U.S. Courts website. The courts' administrative office says they are not official.", fig("aff_p45", "AFFIDAVIT · FIGURES 22–25", (0.0, 0.1))),
   L("A chat window opened with this greeting.", dict(type="quote", q="Hi I'm the duty officer today. How can I assist you?", case="Chat window on all three sites", doc="Affidavit ¶ 48", cite="D.N.J. Mag. No. 26-8230", size="lg")),
   L("Full story on the channel.", dict(type="end", cta="FULL STORY ON THE CHANNEL")),
  ]},
 {"title": "Over $19M Reported Lost to Jury Duty Fraud at One ATM Firm", "template": "number reveal (document-led)",
  "lines": [
   L("Over nineteen million dollars. Victims reported losing that to jury duty fraud at one crypto A.T.M. company, a federal affidavit says.", hook("h_atm", tag="AFFIDAVIT SAYS", number="$19M+", label="REPORTED LOST|AT ONE CRYPTO ATM FIRM"), show="Over $19 million. Victims reported losing that to jury duty fraud at one crypto ATM company, a federal affidavit says."),
   L("Between September twenty twenty-two and May twenty twenty-six, over forty percent of those victims paid money mules in Georgia.", doc("btc", "AFFIDAVIT · ALLEGATIONS · ¶ 29"), show="Between September 2022 and May 2026, over 40 percent of those victims paid money mules in Georgia."),
   L("The scheme, the affidavit says: a fake warrant, a gag order, then cash into a crypto machine.", clip("abc7_atm_b", 4.0, "Source: Eyewitness News ABC7NY · FBI warning on bitcoin ATM scams (file footage) · Dec 2025")),
   L("One victim report in the affidavit: an elderly Texas woman paid ten thousand dollars at a crypto A.T.M. after more than six hours on the phone.", dict(type="stat", kicker="VICTIM REPORT · AFFIDAVIT ¶ 50 · UNNAMED", value="$10,000", label="paid at a crypto ATM · on the phone 6+ hours", src=SRC_AF), show="One victim report in the affidavit: an elderly Texas woman paid $10,000 at a crypto ATM after more than 6 hours on the phone."),
   L("Would a bank teller stop you?", dict(type="end", cta="FULL CASE ON THE CHANNEL")),
  ]},
 {"title": "Postal Inspectors Warn 1,300+ Alleged Money Mules", "template": "footage-led · timeline",
  "lines": [
   L("More than thirteen hundred warning letters. On November thirteenth, postal inspectors mailed them to people they say were money mules for Georgia inmates.", hook("h_doj2", tag="DOJ SAYS", number="1,300+", label="WARNING LETTERS|MONEY MULES"), show="More than 1,300 warning letters. On November 13, postal inspectors mailed them to people they say were money mules for Georgia inmates."),
   L("The letters warn they could face criminal charges if they keep moving the money.", clip("doj_p14", 6.0, LB_DOJ)),
   L("Six days later, the F.C.C. approved a rule letting state prisons jam contraband cell phone signals.", clip("thv_jam", 3.0, "Source: THV11 · FCC approves contraband phone jamming · Nov 2026"), show="Six days later, the FCC approved a rule letting state prisons jam contraband cell phone signals."),
   L("The department also lists charges in Illinois and Texas, a Georgia state indictment of seventeen people for smuggling phones into prisons, and seized websites.", dict(type="big", kicker="DOJ SURGE PAGE · NOV 2026", lines=["Charges in|Illinois, Texas.", "17 charged in Georgia|for phone smuggling.", "3 fake court|sites seized."], src=SRC_SG), show="The department also lists charges in Illinois and Texas, a Georgia state indictment of 17 people for smuggling phones into prisons, and seized websites."),
   L("Should prisons be allowed to jam phones?", dict(type="end", cta="FULL CASE ON THE CHANNEL")),
  ]},
]
for i, s in enumerate(shorts, 1):
    json.dump(s, open(os.path.join(HERE, f"short{i}.json"), "w"), indent=1, ensure_ascii=False)
    print(i, len(s["title"]), s["title"], sum(len(l["say"].split()) for l in s["lines"]), "words")
