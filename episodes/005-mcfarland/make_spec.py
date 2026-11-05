import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
def hl(name, i=0):
    a, b = HL[name][i]
    return [0.0, a, 1.0, round(b - a, 4)]
CASE = "U.S. v. McFARLAND"
SRC_CMP = "Sealed Complaint, S.D.N.Y., Jun 30, 2017 (FBI SA affidavit)"
SRC_MEMO = "Government's Sentencing Memorandum, S.D.N.Y. 17 Cr. 600, Oct 3, 2018"
SRC_INF = "S1 Superseding Information, S.D.N.Y., Mar 6, 2018"
SRC_PLEA = "Plea hearing transcript, S.D.N.Y., Mar 6, 2018"
SRC_BAIL = "Government letter re bail revocation, Jun 18, 2018"
SRC_SENT = "Sentencing transcript, S.D.N.Y., Oct 11, 2018"
SRC_JDG = "Judgment in a Criminal Case, S.D.N.Y., Oct 16, 2018"
SRC_PR = "U.S. Attorney, S.D.N.Y. — release, Oct 11, 2018"
SRC_PRJ = "U.S. Attorney, S.D.N.Y. — release, Jun 12, 2018"
SRC_SEC = "SEC press release 2018-141, Jul 24, 2018"
SRC_SUB = "Declaration of FBI SA Brandon Racz, Jan 10, 2019"
SRC_CR = "Government's opposition to compassionate release, Apr 28, 2020"
SRC_LTR = "Letter of Judge Naomi Reice Buchwald, May 11, 2020"
SRC_WPLG = "WPLG Local 10 / KSAT, Apr 28, 2017"
SRC_NPR = "NPR, Apr 24, 2025"
SRC_FORT = "Fortune, Jul 16, 2025"
MEMOQ = "As quoted in the Government's Sentencing Memorandum, Oct 3, 2018"
def L(say, scene=None, show=None, **kw):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    d.update(kw); return d
def doc(img, kicker, title, src, i=0, pan=None):
    return dict(type="doc", img=f"img/{img}.jpg", pan=pan or [0.0, 0.1], hl=hl(img, i), kicker=kicker, title=title, src=src)
lines = [
 # COLD OPEN
 L("Between May two thousand sixteen and April two thousand seventeen, Fyre Media's booking app confirmed sixty paid bookings. The fees came to fifty-seven thousand, four hundred forty-three dollars.",
   doc("memo_60", "PER PROSECUTORS", "60 bookings · $57,443", SRC_MEMO),
   show="Between May 2016 and April 2017, Fyre Media's booking app confirmed 60 paid bookings. The fees came to $57,443."),
 L("In January two thousand seventeen, the real report showed about one point four six million dollars in offers for the month. The version prepared for investors showed thirty-four point seven nine million.",
   dict(type="bars", kicker="JANUARY 2017 · OFFERS ON THE APP", title="Same month, two reports", items=[{"label": "FABRICATED REPORT", "value": 34.79, "display": "$34.79M"}, {"label": "THE APP'S OWN REPORT", "value": 1.459, "display": "$1.459M"}], src=SRC_MEMO),
   show="In January 2017, the real report showed about $1.46 million in offers for the month. The version prepared for investors showed $34.79 million."),
 L("Prosecutors said the founder told a contractor exactly how to build it. Sprinkle in a couple of higher offer amounts.",
   dict(type="quote", q="[S]prinkle in a couple of higher offer amounts", case=CASE, doc="INSTRUCTIONS TO A CONTRACTOR · FEBRUARY 2017", cite=MEMOQ, size=56)),
 L("The founder was William McFarland. Billy. Twenty-six years old when he pleaded guilty. And while he was out on bail, he started another scam.",
   dict(type="big", kicker="THE DEFENDANT", lines=["Billy McFarland.", "Out on bail."], src=SRC_PR + " · " + SRC_PLEA),
   show="The founder was William McFarland. Billy. 26 years old when he pleaded guilty. And while he was out on bail, he started another scam."),
 L("This is SWORN.",
   dict(type="title", kicker="SWORN · CASE 005 · THE VERDICT", title="The Fyre|Files", sub="United States v. William McFarland · Southern District of New York · 2017–2018")),
 # I
 L("Chapter one. The app.", dict(type="chapter", n="I", title="The App")),
 L("In two thousand thirteen, McFarland founded Magnises, a members' club for millennials with a black metal card. Prosecutors said he raised about three million dollars from at least twenty-four investors, and inflated its membership numbers.",
   dict(type="big", kicker="2013 · MAGNISES · PER PROSECUTORS", lines=["A club.", "A black metal card."], src=SRC_MEMO),
   show="In 2013, McFarland founded Magnises, a members' club for millennials with a black metal card. Prosecutors said he raised about $3 million from at least 24 investors, and inflated its membership numbers."),
 L("In two thousand sixteen came Fyre Media. An app where people organizing events, like concerts, could bid to book artists and celebrities.",
   doc("inf_s1", "S1 SUPERSEDING INFORMATION", "Count One: wire fraud", SRC_INF),
   show="In 2016 came Fyre Media. An app where people organizing events, like concerts, could bid to book artists and celebrities."),
 L("On August first, two thousand sixteen, he told investors Fyre represented four hundred of the biggest names in music, sports, and entertainment.",
   dict(type="quote", q="400 of the biggest names in music, sports, and entertainment.", case=CASE, doc="McFARLAND TO INVESTORS · AUGUST 1, 2016", cite=MEMOQ, size=52),
   show="On August 1, 2016, he told investors Fyre represented \"400 of the biggest names in music, sports, and entertainment.\""),
 L("That same day he told another investor: two point five million dollars in accepted offers. Prosecutors said the real figure was eleven thousand one hundred dollars.",
   dict(type="stat", kicker="AUGUST 1, 2016 · PER PROSECUTORS", value="$11,100", label="in accepted offers —|not “$2.5mm”", src="McFarland email, Aug 1, 2016, as quoted in the Government's Sentencing Memorandum, Oct 3, 2018"),
   show="That same day he told another investor: \"$2.5mm in accepted offers!\" Prosecutors said the real figure was $11,100."),
 L("A private placement memorandum sent to investors in early two thousand seventeen claimed thousands of offers, worth tens of millions of dollars, made and accepted. It also said Fyre had acquired land in the Bahamas worth about eight million dollars. Fyre never owned any land there.",
   doc("memo_60", "THE PRIVATE PLACEMENT MEMORANDUM", "“tens of millions of dollars”", SRC_MEMO, 1),
   show="A private placement memorandum sent to investors in early 2017 claimed thousands of offers, worth tens of millions of dollars, made and accepted. It also said Fyre had acquired land in the Bahamas worth about $8 million. Fyre never owned any land there."),
 # II
 L("Chapter two. The numbers.", dict(type="chapter", n="II", title="The Numbers")),
 L("In December two thousand sixteen, an investor deck said Fyre was on track to achieve one hundred sixty million dollars in completed bookings by the fourth quarter of two thousand seventeen.",
   doc("memo_160", "DECEMBER 2016 · INVESTOR PRESENTATION", "“on track to achieve $160M”", SRC_MEMO, 0),
   show="In December 2016, an investor deck said Fyre was on track to achieve $160 million in completed bookings by the fourth quarter of 2017."),
 L("A few days later, according to prosecutors, he edited an update drafted by his chief revenue officer. The bookings goal went from fifty million to one hundred fifty million. Talent represented went from two hundred to twelve hundred.",
   doc("memo_160", "THE BUSINESS UPDATE", "$50M → $150M · 200 → 1,200", SRC_MEMO, 1),
   show="A few days later, according to prosecutors, he edited an update drafted by his chief revenue officer. The bookings goal went from $50 million to $150 million. Talent represented went from 200 to 1,200."),
 L("Then came the offer reports. In February two thousand seventeen, prosecutors said, he handed the contractor the app's real report, with instructions. Make sure thirty-five percent are international cities. Show thirty point one million in total bookings for January.",
   doc("memo_sprinkle", "FEBRUARY 2017", "The instructions", SRC_MEMO),
   show="Then came the offer reports. In February 2017, prosecutors said, he handed the contractor the app's real report, with instructions. Make sure 35% are international cities. Show $30.1 million in total bookings for January."),
 L("The contractor invented offers from accounts that did not exist, for venues picked at random. In April, asked whether to continue the trend, McFarland answered: yes let's increase them.",
   doc("memo_1459", "PER PROSECUTORS", "$1.459 million → $34.79 million", SRC_MEMO),
   show="The contractor invented offers from accounts that did not exist, for venues picked at random. In April, asked whether to continue the trend, McFarland answered: \"yes let's increase them.\""),
 L("When one investor asked for the latest bookings in April two thousand seventeen, the FBI's complaint says, McFarland replied with numbers the investor understood to mean forty-four million and fifty million dollars.",
   doc("cmp_44", "SEALED COMPLAINT · APRIL 24, 2017", "“$44 for march”", SRC_CMP),
   show="When one investor asked for the latest bookings in April 2017, the FBI's complaint says, McFarland replied with numbers the investor understood to mean $44 million and $50 million."),
 L("To show he could personally guarantee investments, he sent an altered brokerage statement. It showed two point five six million dollars in stock. He actually owned one thousand four hundred ninety-nine dollars' worth. The S.E.C. said the shares were Facebook's.",
   doc("memo_stock", "THE BROKERAGE STATEMENT", "$2.56 million vs. $1,499", SRC_MEMO + " · " + SRC_SEC),
   show="To show he could personally guarantee investments, he sent an altered brokerage statement. It showed $2.56 million in stock. He actually owned $1,499 worth. The SEC said the shares were Facebook's."),
 L("He told investors Magnises had been sold for about forty million dollars, to a new company called Saddleback Media. There was no sale. He even created an agreement bearing the electronic signature of Saddleback's supposed president, a G. Smythe. Prosecutors said that person does not exist.",
   doc("memo_smythe", "THE SALE THAT WASN'T", "“G. Smythe”", SRC_MEMO),
   show="He told investors Magnises had been sold for about $40 million, to a new company called Saddleback Media. There was no sale. He even created an agreement bearing the electronic signature of Saddleback's supposed president, a \"G. Smythe.\" Prosecutors said that person does not exist."),
 # III
 L("Chapter three. The island.", dict(type="chapter", n="III", title="The Island")),
 L("Fyre Festival was announced on December twelfth, two thousand sixteen. A music festival over two weekends in the Bahamas. In court, he said it was meant to promote the app.",
   dict(type="timeline", kicker="FYRE FESTIVAL", events=[{"date": "DEC 12, 2016", "text": "Festival announced"}, {"date": "APR 28, 2017", "text": "First weekend set to begin, Exuma"}, {"date": "JUN 30, 2017", "text": "Criminal complaint"}], at=0, src=SRC_MEMO + " · " + SRC_PLEA + " · " + SRC_WPLG),
   show="Fyre Festival was announced on December 12, 2016. A music festival over two weekends in the Bahamas. In court, he said it was meant to promote the app."),
 L("To fund it, prosecutors said, he overstated the festival's receivables, told investors top musicians would perform when no deals were in place, and promised payouts from event cancellation insurance. No such policy had been executed.",
   dict(type="list", kicker="TO FESTIVAL INVESTORS · PER PROSECUTORS", items=[["1", "Inflated receivables"], ["2", "Stars who never signed"], ["3", "Insurance that didn't exist"]], size=42, src=SRC_MEMO)),
 L("In April, a ticket vendor paid two million dollars for advance tickets to future festivals, after he showed it a fraudulent income statement.",
   doc("memo_vendor", "APRIL 2017 · VENDOR-1", "$2 million for future tickets", SRC_MEMO),
   show="In April, a ticket vendor paid $2 million for advance tickets to future festivals, after he showed it a fraudulent income statement."),
 L("The first weekend was set to begin on Friday, April twenty-eighth, on Exuma. Patrons, some of whom had paid thousands of dollars, found that the luxury villas and gourmet meals were tents and prepackaged meals. The festival was canceled.",
   dict(type="big", kicker="EXUMA, THE BAHAMAS · APRIL 2017", lines=["Villas: tents.", "Canceled."], src=SRC_MEMO + " · " + SRC_WPLG),
   show="The first weekend was set to begin on Friday, April 28, on Exuma. Patrons, some of whom had paid thousands of dollars, found that the luxury villas and gourmet meals were tents and prepackaged meals. The festival was canceled."),
 L("Investors who had been promised insurance payouts lost their money in full. In all, prosecutors said, at least eighty investors lost more than twenty-four million dollars.",
   doc("memo_victims", "THE LOSSES", "At least 80 investors · $24M+", SRC_MEMO),
   show="Investors who had been promised insurance payouts lost their money in full. In all, prosecutors said, at least 80 investors lost more than $24 million."),
 L("On June thirtieth, two thousand seventeen, an FBI special agent swore out a criminal complaint. Wire fraud. McFarland was released on bail the next day.",
   doc("cmp_cover", "JUNE 30, 2017", "Sealed complaint", SRC_CMP + " · " + SRC_MEMO),
   show="On June 30, 2017, an FBI special agent swore out a criminal complaint. Wire fraud. McFarland was released on bail the next day."),
 # IV
 L("Chapter four. The second scheme.", dict(type="chapter", n="IV", title="The Second Scheme")),
 L("On March sixth, two thousand eighteen, he pleaded guilty to two counts of wire fraud. In court, he said this.",
   dict(type="quote", q="I lied to investors about various aspects of Fyre Media and my personal finances.", case=CASE, doc="McFARLAND · GUILTY PLEA · MARCH 6, 2018", cite=SRC_PLEA, size=48),
   show="On March 6, 2018, he pleaded guilty to two counts of wire fraud. In court, he said this."),
 L("He was still on bail. And since late two thousand seventeen, prosecutors said, he had been running a company called NYC VIP Access, selling tickets to the Met Gala, Burning Man, Coachella, the Grammys and the Super Bowl. Tickets that did not exist.",
   dict(type="list", kicker="NYC VIP ACCESS · LATE 2017 – MARCH 2018", items=[["1", "2018 Met Gala"], ["2", "Burning Man 2018"], ["3", "Coachella 2018"], ["4", "2018 Grammy Awards"], ["5", "Super Bowl LII"]], size=40, src=SRC_PR),
   show="He was still on bail. And since late 2017, prosecutors said, he had been running a company called NYC VIP Access, selling tickets to the Met Gala, Burning Man, Coachella, the Grammys and the Super Bowl. Tickets that did not exist."),
 L("In December, an email went out from an employee's account. We partnered with the sponsoring brands to get you a chance to buy tickets. The price, prosecutors said: two thousand five hundred dollars a ticket.",
   doc("memo_gala", "DECEMBER 17, 2017 · “2018 MET GALA”", "The email", SRC_MEMO),
   show="In December, an email went out from an employee's account. \"We partnered with the sponsoring brands to get you a chance to buy tickets.\" The price, prosecutors said: $2,500 a ticket."),
 L("When a buyer wanted confirmation, McFarland later admitted, he created a fake email from the gala's host. None of the buyers were on the guest list.",
   dict(type="big", kicker="THE MET GALA · PER PROSECUTORS", lines=["A fake confirmation.", "No one got in."], src=SRC_MEMO)),
 L("Prosecutors said he hid behind his staff. He wrote from an employee's email account and from a fake employee's. Payments went to employees' and his driver's accounts, and came back to him in cash. At least thirty customers lost about one hundred fifty thousand dollars. Some had been at Fyre Festival.",
   dict(type="stat", kicker="NYC VIP ACCESS · PER PROSECUTORS", value="$150,000", label="from at least 30 customers —|some of them Fyre Festival guests", src=SRC_PR),
   show="Prosecutors said he hid behind his staff. He wrote from an employee's email account and from a fake employee's. Payments went to employees' and his driver's accounts, and came back to him in cash. At least 30 customers lost about $150,000. Some had been at Fyre Festival."),
 L("In March two thousand eighteen, he also gave his driver a forged twenty-five thousand dollar check, written on an employee's bank account.",
   dict(type="big", kicker="MARCH 2018 · PER PROSECUTORS", lines=["A forged check.", "$25,000."], src=SRC_PR),
   show="In March 2018, he also gave his driver a forged $25,000 check, written on an employee's bank account."),
 L("On June twelfth, he was charged again, and his pretrial release ended. On June eighteenth, the judge revoked his bail.",
   doc("bail", "JUNE 18, 2018", "“the Court should revoke the defendant's bail”", SRC_BAIL + " · " + SRC_PRJ),
   show="On June 12, he was charged again, and his pretrial release ended. On June 18, the judge revoked his bail."),
 L("Two days later, he sat down voluntarily with a federal agent, with his lawyer present, and lied, including that the employee had authorized that check. On July twenty-sixth, he pleaded guilty to wire fraud and bank fraud on bail, and to making false statements.",
   dict(type="timeline", kicker="2018", events=[{"date": "MAR 6", "text": "Guilty plea: 2 counts"}, {"date": "JUN 12", "text": "Charged again"}, {"date": "JUN 20", "text": "Lies to a federal agent"}, {"date": "JUL 26", "text": "Guilty plea: 3 more counts"}], at=3, src=SRC_PR + " · " + SRC_MEMO),
   show="Two days later, he sat down voluntarily with a federal agent, with his lawyer present, and lied, including that the employee had authorized that check. On July 26, he pleaded guilty to wire fraud and bank fraud on bail, and to making false statements."),
 # V
 L("Chapter five. The sentence.", dict(type="chapter", n="V", title="The Sentence")),
 L("The government asked for a sentence within a guidelines range of one hundred eighty-eight to two hundred thirty-five months. Its memorandum put it bluntly.",
   doc("memo_con", "THE GOVERNMENT'S MEMORANDUM", "“the consummate con artist”", SRC_MEMO, 0),
   show="The government asked for a sentence within a guidelines range of 188 to 235 months. Its memorandum put it bluntly."),
 L("Whenever one scheme began to falter, prosecutors wrote, he hatched a newer and more elaborate one.",
   doc("memo_con", "PER PROSECUTORS", "“a newer and more elaborate one”", SRC_MEMO, 1)),
 L("The defense said McFarland had used investor money on a flawed business plan, and pointed to his youth and his mental health. October eleventh, two thousand eighteen. McFarland addressed the court.",
   dict(type="quote", q="I know that I betrayed the trust of my investors, customers, my family, and even the Court.", case=CASE, doc="McFARLAND · SENTENCING · OCTOBER 11, 2018", cite=SRC_SENT, size=46),
   show="The defense said McFarland had used investor money on a flawed business plan, and pointed to his youth and his mental health. October 11, 2018. McFarland addressed the court."),
 L("Judge Naomi Reice Buchwald rejected the picture of a good idea gone bad. While soliciting investments for the festival, she noted, he had upgraded from an eight thousand dollar a month apartment to a penthouse at twenty-one thousand a month.",
   doc("memo_pent", "EARLY 2017 · PER PROSECUTORS", "$8,000 → $21,000 a month", SRC_MEMO + " · " + SRC_SENT),
   show="Judge Naomi Reice Buchwald rejected the picture of a good idea gone bad. While soliciting investments for the festival, she noted, he had upgraded from an $8,000-a-month apartment to a penthouse at $21,000 a month."),
 L("On the lies to the FBI agent, she said this.",
   dict(type="quote", q="This is just white-collar obstruction.", case=CASE, doc="JUDGE NAOMI REICE BUCHWALD · OCTOBER 11, 2018", cite=SRC_SENT, size=60)),
 L("And her conclusion.",
   dict(type="quote", q="the defendant is a serial fraudster, and that to date his fraud, like a circle, has no end.", case=CASE, doc="JUDGE NAOMI REICE BUCHWALD · OCTOBER 11, 2018", cite=SRC_SENT, size=46)),
 L("The sentence: six years in prison. Five years, plus one consecutive year for crimes committed on bail. Three years of supervised release.",
   doc("jdg_72", "JUDGMENT · OCTOBER 2018", "72 months", SRC_JDG),
   show="The sentence: six years in prison. Five years, plus one consecutive year for crimes committed on bail. Three years of supervised release."),
 L("And a forfeiture of twenty-six point one nine million dollars.",
   dict(type="verdict", kicker="THE SENTENCE · OCTOBER 11, 2018", stamp="SENTENCED", big="6 years", sub="William McFarland · forfeiture of $26,191,306.28"),
   show="And a forfeiture of $26.19 million."),
 # VI
 L("Chapter six. After the verdict.", dict(type="chapter", n="VI", title="After the Verdict")),
 L("In July two thousand eighteen, in a civil case, the S.E.C. had charged him with fraud in offerings that raised at least twenty-seven point four million dollars from more than one hundred investors. He admitted the allegations and accepted a permanent officer-and-director bar.",
   dict(type="big", kicker="JULY 24, 2018 · SEC", lines=["$27.4 million.", "Permanent bar."], src=SRC_SEC),
   show="In July 2018, in a civil case, the SEC had charged him with fraud in offerings that raised at least $27.4 million from more than 100 investors. He admitted the allegations and accepted a permanent officer-and-director bar."),
 L("To collect on the forfeiture, the FBI listed what it could find. About two hundred forty thousand dollars held in his name at a law firm. Funds in a Fyre Festival bank account. And two large boxes of Fyre-branded t-shirts, sweatshirts and shorts, meant to be sold at the festival.",
   doc("sub_shirts", "JANUARY 2019 · SUBSTITUTE ASSETS", "Two boxes of Fyre clothing", SRC_SUB),
   show="To collect on the forfeiture, the FBI listed what it could find. About $240,000 held in his name at a law firm. Funds in a Fyre Festival bank account. And two large boxes of Fyre-branded t-shirts, sweatshirts and shorts, meant to be sold at the festival."),
 L("In prison, according to the government, he was caught with a pen that could record. He was segregated for forty days and lost forty days of good conduct time.",
   dict(type="big", kicker="IN PRISON · PER THE GOVERNMENT", lines=["A recording pen.", "40 days."], src=SRC_CR),
   show="In prison, according to the government, he was caught with a pen that could record. He was segregated for 40 days and lost 40 days of good conduct time."),
 L("In April two thousand twenty, he asked for compassionate release because of COVID-19. The government opposed it. With the motion ripe and a draft opinion ready, his lawyer withdrew the request. The judge wrote that this obvious effort to avoid a negative result could not go without comment.",
   doc("ltr_2020", "MAY 11, 2020 · JUDGE BUCHWALD", "“this obvious effort”", SRC_LTR + " · " + SRC_CR),
   show="In April 2020, he asked for compassionate release because of COVID-19. The government opposed it. With the motion ripe and a draft opinion ready, his lawyer withdrew the request. The judge wrote that this \"obvious effort to avoid a negative result\" could not go without comment."),
 L("According to NPR, he was released in two thousand twenty-two. Ticket holders' class action had settled in two thousand twenty-one for two million dollars.",
   dict(type="timeline", kicker="AFTER PRISON · PER REPORTS", events=[{"date": "2021", "text": "Class action settles: $2M"}, {"date": "2022", "text": "Released from prison"}, {"date": "2025", "text": "Fyre Festival 2 postponed"}, {"date": "JUL 2025", "text": "Brand sold on eBay"}], at=1, src=SRC_NPR + " · " + SRC_FORT),
   show="According to NPR, he was released in 2022. Ticket holders' class action had settled in 2021 for $2 million."),
 L("Then he announced Fyre Festival two. Tickets went on sale in February two thousand twenty-five, starting at fourteen hundred dollars, for an event in Mexico. Local officials denied it. In April it was postponed.",
   dict(type="big", kicker="2025 · PER NPR", lines=["Fyre Festival 2.", "Postponed."], src=SRC_NPR),
   show="Then he announced Fyre Festival 2. Tickets went on sale in February 2025, starting at $1,400, for an event in Mexico. Local officials denied it. In April it was postponed."),
 L("In July two thousand twenty-five, the Fyre Festival brand sold on eBay for two hundred forty-five thousand, three hundred dollars. According to NPR, he still owes twenty-six million dollars in restitution.",
   dict(type="stat", kicker="JULY 2025 · PER FORTUNE AND NPR", value="$245,300", label="for the brand —|against $26 million still owed", src=SRC_FORT + " · " + SRC_NPR),
   show="In July 2025, the Fyre Festival brand sold on eBay for $245,300. According to NPR, he still owes $26 million in restitution."),
 L("January two thousand seventeen. One point four six million dollars in real offers. Thirty-four point seven nine million on paper.",
   dict(type="big", lines=["$1.46M real.", "$34.79M|on paper."]),
   show="January 2017. $1.46 million in real offers. $34.79 million on paper."),
 L("In the end, the judge read the paper, not the pitch. Like a circle, she said. No end.",
   dict(type="big", lines=["Like a circle.", "No end."])),
 L("This is SWORN. Real trials. Real evidence. The verdict.", dict(type="end")),
]
from panfix import fix
fix(lines, "long")
spec = {"label": "SWORN · CASE 005", "lines": lines}
json.dump(spec, open(os.path.join(HERE, "episode.json"), "w"), indent=1, ensure_ascii=False)
print(len(lines), "lines,", sum(len(l["say"].split()) for l in lines), "words")
