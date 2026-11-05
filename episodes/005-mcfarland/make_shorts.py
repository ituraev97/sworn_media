import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
def hl(name, i=0):
    a, b = HL[name][i]
    return [0.0, a, 1.0, round(b - a, 4)]
def doc(img, kicker, src, i=0):
    return dict(type="doc", img=f"img/{img}.jpg", pan=[0.0, 0.1], hl=hl(img, i), kicker=kicker, src=src)
CASE = "U.S. v. McFARLAND"
SRC_CMP = "Sealed complaint, S.D.N.Y., Jun 30, 2017"
SRC_MEMO = "Gov't sentencing memo, S.D.N.Y., Oct 3, 2018"
SRC_PLEA = "Plea transcript, S.D.N.Y., Mar 6, 2018"
SRC_SENT = "Sentencing transcript, Oct 11, 2018"
SRC_JDG = "Judgment, S.D.N.Y., Oct 16, 2018"
SRC_PR = "U.S. Attorney, S.D.N.Y., Oct 11, 2018"
SRC_SEC = "SEC press release 2018-141"
SRC_SUB = "FBI declaration, Jan 10, 2019"
SRC_CR = "Gov't filing, Apr 28, 2020"
SRC_WPLG = "WPLG / KSAT, Apr 28, 2017"
SRC_NPR = "NPR, Apr 24, 2025"
SRC_FORT = "Fortune, Jul 16, 2025"
MEMOQ = "As quoted in the gov't sentencing memo, 2018"
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
END = L("Real trials. Real evidence. The verdict.", dict(type="end"))
shorts = [
 {"title": "$1.46 Million Real, $34.79 Million on Paper: How Fyre's Numbers Were Built", "hook": "$1.46M real.|$34.79M on paper.", "lines": [
  L("Fyre Media sold itself as an app for booking artists. From May two thousand sixteen to April two thousand seventeen, it confirmed sixty paid bookings.",
    doc("memo_60", "PER PROSECUTORS", SRC_MEMO),
    show="Fyre Media sold itself as an app for booking artists. From May 2016 to April 2017, it confirmed 60 paid bookings."),
  L("Total fees: fifty-seven thousand, four hundred forty-three dollars.",
    dict(type="stat", kicker="MAY 2016 – APRIL 2017", value="$57,443", label="in booking fees", src=SRC_MEMO),
    show="Total fees: $57,443."),
  L("In February two thousand seventeen, prosecutors said, Billy McFarland gave a contractor instructions for the investor version.",
    doc("memo_sprinkle", "FEBRUARY 2017", SRC_MEMO),
    show="In February 2017, prosecutors said, Billy McFarland gave a contractor instructions for the investor version."),
  L("Sprinkle in a couple of higher offer amounts.",
    dict(type="quote", q="[S]prinkle in a couple of higher offer amounts", case=CASE, doc="McFARLAND'S INSTRUCTIONS", cite=MEMOQ, size=50)),
  L("January's real offers: about one point four six million dollars. The new report: thirty-four point seven nine million.",
    dict(type="bars", kicker="JANUARY 2017", title="Offers on the app", items=[{"label": "FAKE", "value": 34.79, "display": "$34.79M"}, {"label": "REAL", "value": 1.459, "display": "$1.459M"}], src=SRC_MEMO),
    show="January's real offers: about $1.46 million. The new report: $34.79 million."),
  L("He pleaded guilty to wire fraud, and was sentenced to six years.",
    dict(type="verdict", kicker="OCTOBER 11, 2018", stamp="SENTENCED", big="6 years", sub="William McFarland"),
    show="He pleaded guilty to wire fraud, and was sentenced to six years."),
  END]},
 {"title": "$2.56 Million in Stock — or $1,499? The Fake Proof Behind Fyre Festival", "hook": "$2.56 million?|Or $1,499?", "lines": [
  L("Investors wanted to know Billy McFarland could back his promises. Prosecutors said he showed them proof.",
    dict(type="big", kicker="THE GUARANTEE", lines=["He showed", "them|proof."], src=SRC_MEMO)),
  L("An altered brokerage statement showing two point five six million dollars in stock. He actually owned one thousand four hundred ninety-nine dollars' worth.",
    doc("memo_stock", "THE BROKERAGE STATEMENT", SRC_MEMO),
    show="An altered brokerage statement showing $2.56 million in stock. He actually owned $1,499 worth."),
  L("A banker's email approving a three million dollar loan. The banker never sent it.",
    dict(type="big", kicker="PER PROSECUTORS", lines=["A $3M loan.", "Never|sent."], src=SRC_MEMO),
    show="A banker's email approving a $3 million loan. The banker never sent it."),
  L("And the sale of his earlier company, Magnises, for about forty million dollars, to Saddleback Media. There was no sale.",
    dict(type="stat", kicker="MAGNISES · PER PROSECUTORS", value="$40M", label="a sale that|never happened", src=SRC_MEMO),
    show="And the sale of his earlier company, Magnises, for about $40 million, to Saddleback Media. There was no sale."),
  L("One document bore the electronic signature of Saddleback's president, a G. Smythe. Prosecutors said that person does not exist.",
    doc("memo_smythe", "“G. SMYTHE”", SRC_MEMO),
    show="One document bore the electronic signature of Saddleback's president, a \"G. Smythe.\" Prosecutors said that person does not exist."),
  L("In July two thousand eighteen, he admitted the S.E.C.'s allegations.",
    dict(type="big", kicker="JULY 2018 · SEC", lines=["Allegations:", "admitted."], src=SRC_SEC),
    show="In July 2018, he admitted the SEC's allegations."),
  END]},
 {"title": "Fyre Festival: What Investors Were Promised vs. What Was Real", "hook": "What investors|were promised.", "lines": [
  L("Fyre Festival was announced in December two thousand sixteen. Two weekends in the Bahamas.",
    dict(type="big", kicker="DECEMBER 12, 2016", lines=["Fyre Festival.", "The|Bahamas."], src=SRC_MEMO),
    show="Fyre Festival was announced in December 2016. Two weekends in the Bahamas."),
  L("Investors were told Fyre had acquired land there worth about eight million dollars. It never owned any.",
    doc("memo_60", "THE LAND", SRC_MEMO, 1),
    show="Investors were told Fyre had acquired land there worth about $8 million. It never owned any."),
  L("Some were promised payouts from event cancellation insurance. No such policy had been executed.",
    dict(type="big", kicker="PER PROSECUTORS", lines=["Insurance?", "None."], src=SRC_MEMO)),
  L("Others were told top musicians would perform. No such agreements were ever reached.",
    dict(type="big", kicker="PER PROSECUTORS", lines=["The stars?", "Never|signed."], src=SRC_MEMO)),
  L("On Exuma, in late April two thousand seventeen, the promised luxury villas and gourmet meals were tents and prepackaged meals. The festival was canceled.",
    dict(type="big", kicker="EXUMA · APRIL 2017", lines=["Villas?", "Tents."], src=SRC_MEMO + " · " + SRC_WPLG),
    show="On Exuma, in late April 2017, the promised luxury villas and gourmet meals were tents and prepackaged meals. The festival was canceled."),
  L("Prosecutors said at least eighty investors lost more than twenty-four million dollars.",
    doc("memo_victims", "THE LOSSES", SRC_MEMO),
    show="Prosecutors said at least 80 investors lost more than $24 million."),
  END]},
 {"title": "Out on Bail, He Sold Met Gala Tickets That Didn't Exist", "hook": "Out on bail.|Selling the Met Gala.", "lines": [
  L("July two thousand seventeen. Charged over Fyre Festival, Billy McFarland is released on bail.",
    doc("cmp_cover", "JUNE 30, 2017", SRC_CMP),
    show="July 2017. Charged over Fyre Festival, Billy McFarland is released on bail."),
  L("By late that year, prosecutors said, he ran NYC VIP Access, selling tickets to the Met Gala, Coachella, the Grammys, the Super Bowl.",
    dict(type="list", kicker="NYC VIP ACCESS", items=[["1", "Met Gala"], ["2", "Coachella"], ["3", "Grammys"], ["4", "Super Bowl"]], size=40, src=SRC_PR),
    show="By late that year, prosecutors said, he ran NYC VIP Access, selling tickets to the Met Gala, Coachella, the Grammys, the Super Bowl."),
  L("The Met Gala pitch went out from an employee's email account. Two thousand five hundred dollars a ticket.",
    doc("memo_gala", "DECEMBER 17, 2017", SRC_MEMO),
    show="The Met Gala pitch went out from an employee's email account. $2,500 a ticket."),
  L("When one buyer wanted proof, he admitted, he created a fake email from the gala's host. No buyer was on the guest list.",
    dict(type="big", kicker="PER PROSECUTORS", lines=["Fake proof.", "No one|got in."], src=SRC_MEMO)),
  L("Some were Fyre Festival guests. At least thirty customers lost about one hundred fifty thousand dollars.",
    dict(type="stat", kicker="PER PROSECUTORS", value="$150,000", label="from at least|30 customers", src=SRC_PR),
    show="Some were Fyre Festival guests. At least 30 customers lost about $150,000."),
  L("His bail was revoked. At sentencing, the judge called him unique in the court's memory.",
    dict(type="quote", q="Mr. McFarland is unique in this Court's memory.", case=CASE, doc="JUDGE NAOMI REICE BUCHWALD", cite=SRC_SENT, size=48)),
  END]},
 {"title": "\"Like a Circle, Has No End\": The Judge Who Sentenced Billy McFarland", "hook": "\"Like a circle,|has no end.\"", "lines": [
  L("October eleventh, two thousand eighteen. Billy McFarland stands for sentencing on five counts.",
    doc("jdg_72", "JUDGMENT", SRC_JDG),
    show="October 11, 2018. Billy McFarland stands for sentencing on five counts."),
  L("His defense described a young man with a flawed business plan. Judge Naomi Reice Buchwald disagreed.",
    dict(type="quote", q="Importantly, this was not a good idea gone bad.", case=CASE, doc="JUDGE NAOMI REICE BUCHWALD", cite=SRC_SENT, size=48)),
  L("While raising money for the festival, she noted, he moved from an eight thousand dollar a month apartment to a twenty-one thousand dollar a month penthouse.",
    doc("memo_pent", "EARLY 2017", SRC_MEMO + " · " + SRC_SENT),
    show="While raising money for the festival, she noted, he moved from an $8,000-a-month apartment to a $21,000-a-month penthouse."),
  L("After his second arrest, he had also lied to a federal agent. The judge's words: white-collar obstruction.",
    dict(type="quote", q="This is just white-collar obstruction.", case=CASE, doc="JUDGE NAOMI REICE BUCHWALD", cite=SRC_SENT, size=52)),
  L("Her conclusion.",
    dict(type="quote", q="the defendant is a serial fraudster, and that to date his fraud, like a circle, has no end.", case=CASE, doc="OCTOBER 11, 2018", cite=SRC_SENT, size=40)),
  L("Six years in prison, and a forfeiture of twenty-six point one nine million dollars.",
    dict(type="verdict", kicker="THE SENTENCE", stamp="SENTENCED", big="6 years", sub="Forfeiture: $26,191,306.28"),
    show="Six years in prison, and a forfeiture of $26.19 million."),
  END]},
 {"title": "Where Billy McFarland Is Now: Prison, Fyre Festival 2 and a $245,300 eBay Sale", "hook": "After Fyre:|where is he now?", "lines": [
  L("Billy McFarland got six years for the Fyre fraud and a ticket scam he ran on bail.",
    dict(type="big", kicker="OCTOBER 2018", lines=["6 years.", "$26.19M|forfeiture."], src=SRC_PR),
    show="Billy McFarland got six years for the Fyre fraud and a ticket scam he ran on bail."),
  L("Hunting for assets, the FBI listed two large boxes of Fyre-branded clothing.",
    doc("sub_shirts", "JANUARY 2019", SRC_SUB)),
  L("In prison, the government said, he was caught with a pen that could record, and spent forty days segregated.",
    dict(type="big", kicker="PER THE GOVERNMENT", lines=["A recording", "pen.|40 days."], src=SRC_CR),
    show="In prison, the government said, he was caught with a pen that could record, and spent 40 days segregated."),
  L("According to NPR, he was released in two thousand twenty-two. In two thousand twenty-five, Fyre Festival two was postponed.",
    dict(type="timeline", kicker="PER NPR", events=[{"date": "2022", "text": "Released"}, {"date": "2025", "text": "Fyre Festival 2 postponed"}], at=1, src=SRC_NPR),
    show="According to NPR, he was released in 2022. In 2025, Fyre Festival 2 was postponed."),
  L("In July two thousand twenty-five, the Fyre brand sold on eBay for two hundred forty-five thousand, three hundred dollars.",
    dict(type="stat", kicker="JULY 2025 · FORTUNE", value="$245,300", label="for the Fyre brand", src=SRC_FORT),
    show="In July 2025, the Fyre brand sold on eBay for $245,300."),
  L("NPR reports he still owes twenty-six million dollars in restitution.",
    dict(type="big", kicker="PER NPR", lines=["Still owed:", "$26|million."], src=SRC_NPR),
    show="NPR reports he still owes $26 million in restitution."),
  END]},
]
from panfix import fix
for s in shorts: fix(s["lines"], "short")
for i, s in enumerate(shorts, 1):
    s["label"] = "SWORN"
    json.dump(s, open(os.path.join(HERE, f"short{i}.json"), "w"), indent=1, ensure_ascii=False)
    print(i, len(s["title"]), sum(len(l["say"].split()) for l in s["lines"]), "words", len(s["lines"]), "lines")
