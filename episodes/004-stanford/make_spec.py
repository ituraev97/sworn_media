import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
def hl(name, i=0):
    a, b = HL[name][i]
    return [0.0, a, 1.0, round(b - a, 4)]
CASE = "U.S. v. STANFORD"
SRC_OIG = "SEC Office of Inspector General, Report OIG-526, Mar 31, 2010"
SRC_BR = "Brief of the United States, 5th Cir. No. 12-20411, Mar 3, 2015"
SRC_CMP = "SEC First Amended Complaint, N.D. Tex., Feb 27, 2009"
SRC_RCV = "Order Appointing Receiver, N.D. Tex., Feb 16, 2009"
SRC_PRC = "U.S. Attorney, S.D. Tex. — release, Mar 6, 2012"
SRC_PRS = "U.S. Attorney, S.D. Tex. — release, Jun 14, 2012"
SRC_CA5 = "U.S. Court of Appeals, 5th Cir., No. 12-20411, Oct 29, 2015"
SRC_DAVIS = "Justice Dept. release, Jan 22, 2013"
SRC_HLK = "Justice Dept. Fraud Section, U.S. v. Holt, Lopez, Kuhrt"
SRC_KING = "Justice Dept. release, Feb 24, 2021"
SRC_SEC25 = "SEC Litigation Release No. 26255, Feb 24, 2025"
SRC_IJ = "Insurance Journal, Nov 29, 2016"
SRC_BLK = "Bloomberg Law, Sept 19, 2025"
SRC_BLC = "Bloomberg Law, Sept 1, 2023"
SRC_BOP = "Federal Bureau of Prisons inmate locator, Nov 2026"
SRC_BANKS = "CNN, Feb 27, 2023 · Fishman Haygood, Aug 15, 2023"
BRQ = "As stated in the gov't appellate brief, 5th Cir., 2015"
def L(say, scene=None, show=None, **kw):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    d.update(kw); return d
def doc(img, kicker, title, src, i=0, pan=None):
    return dict(type="doc", img=f"img/{img}.jpg", pan=pan or [0.0, 0.1], hl=hl(img, i), kicker=kicker, title=title, src=src)
lines = [
 # COLD OPEN
 L("Nineteen ninety-seven. Fort Worth, Texas. Examiners at the Securities and Exchange Commission finish a look at a Houston brokerage that sells certificates of deposit from a bank in the Caribbean.",
   dict(type="big", kicker="1997 · SEC FORT WORTH OFFICE", lines=["A Houston brokerage.", "An offshore bank."], src=SRC_OIG),
   show="1997. Fort Worth, Texas. Examiners at the Securities and Exchange Commission finish a look at a Houston brokerage that sells certificates of deposit from a bank in the Caribbean."),
 L("In the agency's tracking system, they record their conclusion. Possible misrepresentations. Possible Ponzi scheme.",
   dict(type="quote", q="Possible misrepresentations. Possible Ponzi scheme.", case="SEC v. STANFORD", doc="1997 EXAMINATION · AS QUOTED BY THE SEC INSPECTOR GENERAL", cite=SRC_OIG, size=58)),
 L("The bank kept selling. For almost twelve more years. Until February two thousand nine, when the SEC finally went to court, and a federal judge handed the whole empire to a receiver.",
   doc("rcv", "FEBRUARY 16, 2009", "Order Appointing Receiver", SRC_RCV),
   show="The bank kept selling. For almost twelve more years. Until February 2009, when the SEC finally went to court, and a federal judge handed the whole empire to a receiver."),
 L("The man at the top was Robert Allen Stanford. A jury convicted him. A judge sentenced him to one hundred ten years. This is the paper trail of how it was built, how it was hidden, and how it fell.",
   dict(type="big", kicker="THE VERDICT", lines=["Convicted.", "110 years."], src=SRC_PRS),
   show="The man at the top was Robert Allen Stanford. A jury convicted him. A judge sentenced him to 110 years. This is the paper trail of how it was built, how it was hidden, and how it fell."),
 L("This is SWORN.",
   dict(type="title", kicker="SWORN · CASE 004 · THE PAPER TRAIL", title="The Bank|That Wasn't", sub="United States v. Robert Allen Stanford · Southern District of Texas · 2009–2025")),
 # I
 L("Chapter one. The bank on the island.", dict(type="chapter", n="I", title="The Bank on the Island")),
 L("According to the Justice Department, Stanford began operating the bank in nineteen eighty-five on Montserrat, in the British West Indies, under the name Guardian International Bank.",
   dict(type="timeline", kicker="PER THE JUSTICE DEPARTMENT", events=[{"date": "1985", "text": "Guardian International Bank, Montserrat"}, {"date": "1990", "text": "The bank moves to Antigua"}, {"date": "1994", "text": "Renamed Stanford International Bank"}], at=0, src=SRC_PRS),
   show="According to the Justice Department, Stanford began operating the bank in 1985 on Montserrat, in the British West Indies, under the name Guardian International Bank."),
 L("In November nineteen ninety, the government's brief says, Montserrat's finance ministry faxed him notice that it intended to revoke the bank's license.",
   doc("brief_montserrat", "NOVEMBER 28, 1990", "Notice of intent to revoke", SRC_BR),
   show="In November 1990, the government's brief says, Montserrat's finance ministry faxed him notice that it intended to revoke the bank's license."),
 L("He moved the bank to Antigua. In nineteen ninety-four it became Stanford International Bank. Antigua knighted him. Sir Allen Stanford, he said, was good marketing.",
   dict(type="big", kicker="ANTIGUA · PER PROSECUTORS", lines=["A new island.", "“Sir Allen Stanford.”"], src=SRC_PRS + " · " + SRC_BR),
   show="He moved the bank to Antigua. In 1994 it became Stanford International Bank. Antigua knighted him. \"Sir Allen Stanford,\" he said, was good marketing."),
 L("The product was simple. Certificates of deposit that paid more than CDs at American banks. From Houston, financial advisers at his firm, Stanford Group Company, sold them to American investors.",
   doc("brief_origin", "THE PRODUCT", "CDs from an offshore bank", SRC_BR)),
 L("There was no F.D.I.C. insurance. Prosecutors said Stanford joked that people were greedy, willing to take that risk for an extra two percent.",
   dict(type="big", kicker="PER PROSECUTORS", lines=["No FDIC insurance.", "An extra 2%."], src=SRC_BR),
   show="There was no FDIC insurance. Prosecutors said Stanford joked that people were greedy, willing to take that risk for an extra 2%."),
 L("By the end of two thousand eight, according to the S.E.C., the bank had sold about eight billion dollars of these CDs, and claimed fifty thousand clients in more than one hundred countries. The S.E.C. called it a massive Ponzi scheme.",
   doc("cmp_cover", "SEC · FIRST AMENDED COMPLAINT", "“a massive Ponzi scheme”", SRC_CMP),
   show="By the end of 2008, according to the SEC, the bank had sold about $8 billion of these CDs, and claimed 50,000 clients in more than 100 countries. The SEC called it a massive Ponzi scheme."),
 # II
 L("Chapter two. The paper trail.", dict(type="chapter", n="II", title="The Paper Trail")),
 L("Every year, the bank's annual report showed a profit. According to the chief financial officer, James Davis, Stanford told him the bank never had a profitable year after nineteen eighty-six. Each year, the two men made up the numbers.",
   doc("brief_profits", "THE ANNUAL REPORTS", "“fake profit numbers”", SRC_BR),
   show="Every year, the bank's annual report showed a profit. According to the chief financial officer, James Davis, Stanford told him the bank never had a profitable year after 1986. Each year, the two men made up the numbers."),
 L("The S.E.C. described the method. Each month, a predetermined return. Then the bank's accountants reverse-engineered the financial statements to match it.",
   doc("cmp_reverse", "SEC · FIRST AMENDED COMPLAINT", "“reverse-engineered”", SRC_CMP)),
 L("Investors were told their money sat in safe, liquid investments, watched by money managers and analysts. Prosecutors said the bank split its assets into tiers.",
   dict(type="bars", kicker="THE TIERS · PER PROSECUTORS", title="Share of the bank's portfolio", items=[{"label": "TIER 1 · CASH", "value": 10, "display": "10%"}, {"label": "TIER 2 · MANAGED", "value": 15, "display": "15%"}, {"label": "TIER 3 · STANFORD", "value": 75, "display": "75%"}], src=SRC_BR)),
 L("Tier one, cash, was ten percent. Tier two, the part the analysts actually managed, fifteen percent. Tier three, seventy-five percent of the bank's assets, went to Stanford's companies, real estate and lifestyle.",
   doc("brief_tier", "TIER 3", "“the remaining 75%”", SRC_BR),
   show="Tier one, cash, was 10%. Tier two, the part the analysts actually managed, 15%. Tier three, 75% of the bank's assets, went to Stanford's companies, real estate and lifestyle."),
 L("By the end of two thousand eight, more than two billion dollars in CD money had gone to over fifty of his businesses. Restaurants. Two airlines. A newspaper. A cricket tournament with a twenty million dollar prize. A one hundred twelve foot yacht.",
   doc("brief_piggy", "BY THE END OF 2008", "“over $2 billion in CD monies”", SRC_BR),
   show="By the end of 2008, more than $2 billion in CD money had gone to over 50 of his businesses. Restaurants. Two airlines. A newspaper. A cricket tournament with a $20 million prize. A 112-foot yacht."),
 L("By two thousand eight, the government said, about a million dollars a day of depositors' money was going to keep those businesses afloat.",
   dict(type="stat", kicker="BY 2008 · PER PROSECUTORS", value="$1M a day", label="of depositor money to keep|his businesses afloat", src=SRC_BR),
   show="By 2008, the government said, about $1 million a day of depositors' money was going to keep those businesses afloat."),
 L("And the auditor? A one-man firm in Antigua, C.A.S. Hewlett. According to the government, in sixteen years he never got the documents to verify the bank's assets. Every year he signed off anyway.",
   doc("brief_hewlett", "THE AUDITOR", "C.A.S. Hewlett", SRC_BR, 0),
   show="And the auditor? A one-man firm in Antigua, C.A.S. Hewlett. According to the government, in 16 years he never got the documents to verify the bank's assets. Every year he signed off anyway."),
 L("Prosecutors said Stanford paid him more than three point three million dollars from a Swiss account, on top of his audit fees. Stanford once told Davis: God led me to Hewlett.",
   doc("brief_hewlett", "THE SWISS ACCOUNT", "More than $3.3 million", SRC_BR, 1),
   show="Prosecutors said Stanford paid him more than $3.3 million from a Swiss account, on top of his audit fees. Stanford once told Davis: \"God led me to Hewlett.\""),
 # III
 L("Chapter three. The warnings.", dict(type="chapter", n="III", title="The Warnings")),
 L("In two thousand ten, the S.E.C.'s own inspector general investigated how the agency had handled Stanford. The report's finding was blunt.",
   dict(type="quote", q="the SEC's Fort Worth office was aware since 1997 that Robert Allen Stanford was likely operating a Ponzi scheme", case="SEC OIG", doc="INSPECTOR GENERAL · CASE NO. OIG-526", cite=SRC_OIG, size=46),
   show="In 2010, the SEC's own inspector general investigated how the agency had handled Stanford. The report's finding was blunt."),
 L("Examiners looked at Stanford's operations four times. In nineteen ninety-seven, nineteen ninety-eight, two thousand two and two thousand four. A branch chief called the CD returns absolutely ludicrous.",
   dict(type="timeline", kicker="SEC EXAMINATIONS · PER THE INSPECTOR GENERAL", events=[{"date": "1997", "text": "“Possible Ponzi scheme”"}, {"date": "1998", "text": "Second exam"}, {"date": "2002", "text": "Third exam"}, {"date": "2004", "text": "Fourth exam"}], at=3, src=SRC_OIG),
   show="Examiners looked at Stanford's operations four times. In 1997, 1998, 2002 and 2004. A branch chief called the CD returns \"absolutely ludicrous.\""),
 L("The enforcement division opened an inquiry in May nineteen ninety-eight, and closed it three months later. The reasons given, the report said, related to the lack of U.S. investors.",
   dict(type="big", kicker="1998 · PER THE INSPECTOR GENERAL", lines=["Opened in May.", "Closed in August."], src=SRC_OIG),
   show="The enforcement division opened an inquiry in May 1998, and closed it three months later. The reasons given, the report said, related to the lack of U.S. investors."),
 L("The inspector general pointed to a preference inside the agency for quick hit cases. No meaningful effort to stop the fraud, the report found, was made until late two thousand five.",
   dict(type="quote", q="the preference for “quick hit” cases as a result of internal SEC pressure", case="SEC OIG", doc="INSPECTOR GENERAL · WHY IT WAITED", cite=SRC_OIG, size=50),
   show="The inspector general pointed to a preference inside the agency for \"quick hit\" cases. No meaningful effort to stop the fraud, the report found, was made until late 2005."),
 L("When the S.E.C. did reach out, it went to Antigua's regulator. In two thousand five, it sent a confidential request about the bank to Leroy King, the head of Antigua's Financial Services Regulatory Commission.",
   doc("brief_sec2005", "2005 · “PRIVILEGED AND CONFIDENTIAL”", "The SEC writes to Antigua", SRC_BR, 0),
   show="When the SEC did reach out, it went to Antigua's regulator. In 2005, it sent a confidential request about the bank to Leroy King, the head of Antigua's Financial Services Regulatory Commission."),
 L("According to the government, King immediately shared it with Stanford, and Stanford helped draft the reply.",
   doc("brief_sec2005", "PER PROSECUTORS", "King shares the letter", SRC_BR, 1)),
 L("King later admitted that Stanford's cash payments to him totaled about five hundred twenty-one thousand dollars, along with Super Bowl tickets and private jet flights.",
   dict(type="stat", kicker="LEROY KING · PER THE JUSTICE DEPARTMENT", value="$520,963.87", label="in cash payments from Stanford,|by King's own admission", src=SRC_KING),
   show="King later admitted that Stanford's cash payments to him totaled about $521,000, along with Super Bowl tickets and private jet flights."),
 L("According to the government's account of the trial testimony, Stanford and King sealed their arrangement by cutting themselves in a blood oath ceremony.",
   doc("brief_king", "ANTIGUA · TRIAL TESTIMONY", "“a blood-oath ceremony”", SRC_BR, 1)),
 # IV
 L("Chapter four. The collapse.", dict(type="chapter", n="IV", title="The Collapse")),
 L("Then came the financial crisis of two thousand eight. Redemptions jumped. New sales flatlined.",
   dict(type="big", kicker="2008", lines=["Redemptions up.", "Sales flat."], src=SRC_BR),
   show="Then came the financial crisis of 2008. Redemptions jumped. New sales flatlined."),
 L("In October, prosecutors said, Stanford told his global executive team that the bank was five billion dollars more liquid than it should be.",
   doc("brief_liquid", "OCTOBER 2008", "“$5 billion more liquid than it should be”", SRC_BR),
   show="In October, prosecutors said, Stanford told his global executive team that the bank was \"$5 billion more liquid than it should be.\""),
 L("When a manager suggested he ask wealthy friends for money, according to trial testimony, Stanford answered: I'll go to the Libyans. They love me. His trip to Libya was unsuccessful.",
   dict(type="quote", q="I’ll go to the Libyans. They love me", case=CASE, doc="STANFORD · NOVEMBER 2008 · PER TRIAL TESTIMONY", cite="As quoted in the Brief of the United States, 5th Cir. No. 12-20411, Mar 3, 2015", size=60)),
 L("In its December two thousand eight report, according to the S.E.C., the bank told investors it had received a capital infusion of five hundred forty-one million dollars.",
   doc("cmp_541", "DECEMBER 2008 · MONTHLY REPORT", "“a capital infusion of $541 million”", SRC_CMP, 0),
   show="In its December 2008 report, according to the SEC, the bank told investors it had received a capital infusion of $541 million."),
 L("The S.E.C. said that was false. Stanford had contributed interests in two pieces of real estate the bank already owned, acquired for about eighty-eight and a half million dollars. According to Davis, Stanford admitted the infusion was merely a bookkeeping entry.",
   doc("cmp_541", "PER THE SEC'S COMPLAINT", "$541 million → about $88.5 million", SRC_CMP + " · " + SRC_BR, 1),
   show="The SEC said that was false. Stanford had contributed interests in two pieces of real estate the bank already owned, acquired for about $88.5 million. According to Davis, Stanford admitted the infusion was merely a bookkeeping entry."),
 L("To back it up, the Justice Department said, accountants marked up a piece of Antiguan land the bank had bought for sixty-three and a half million dollars, by five thousand percent, to more than three billion. On paper.",
   dict(type="bars", kicker="THE LAND · PER THE JUSTICE DEPARTMENT", title="Same land, on paper", items=[{"label": "MARKED UP TO", "value": 3100, "display": "$3.1B"}, {"label": "PURCHASE PRICE, 2008", "value": 63.5, "display": "$63.5M"}], src=SRC_PRS),
   show="To back it up, the Justice Department said, accountants marked up a piece of Antiguan land the bank had bought for $63.5 million, by 5,000 percent, to more than $3 billion. On paper."),
 L("As the S.E.C. investigation surged, the manager of Stanford's estate in Saint Croix testified to following his instructions: fill empty barrels with his bank records, and burn them.",
   doc("brief_burn", "ST. CROIX · TRIAL TESTIMONY", "Records burned in barrels", SRC_BR),
   show="As the SEC investigation surged, the manager of Stanford's estate in St. Croix testified to following his instructions: fill empty barrels with his bank records, and burn them."),
 L("On February sixteenth, two thousand nine, on the S.E.C.'s motion, a federal judge in Dallas appointed a receiver for the Stanford companies. The next day, the receiver took over.",
   doc("rcv", "FEBRUARY 16, 2009", "Order Appointing Receiver", SRC_RCV + " · " + SRC_BR),
   show="On February 16, 2009, on the SEC's motion, a federal judge in Dallas appointed a receiver for the Stanford companies. The next day, the receiver took over."),
 L("An FBI agent traced two billion dollars in loans to Stanford's businesses. The bank reported eight point five nine billion in assets. That left, the government said, a five billion dollar hole.",
   doc("brief_hole", "THE HOLE · PER PROSECUTORS", "“a $5 billion ‘hole’”", SRC_BR, 0),
   show="An FBI agent traced $2 billion in loans to Stanford's businesses. The bank reported $8.59 billion in assets. That left, the government said, a $5 billion hole."),
 # V
 L("Chapter five. The verdict.", dict(type="chapter", n="V", title="The Verdict")),
 L("A fourteen-count superseding indictment charged Stanford with conspiracy, wire fraud, mail fraud, obstructing the S.E.C., and conspiracy to launder money.",
   doc("brief_counts", "THE SUPERSEDING INDICTMENT", "14 counts", SRC_BR),
   show="A 14-count superseding indictment charged Stanford with conspiracy, wire fraud, mail fraud, obstructing the SEC, and conspiracy to launder money."),
 L("At trial, the government said, he did not dispute that he had moved more than two billion dollars to his businesses. His defense blamed Davis, and the receiver, and called the businesses legitimate investments.",
   dict(type="list", kicker="THE DEFENSE · PER PROSECUTORS", items=[["1", "Davis ran the fraud alone"], ["2", "The receiver caused the losses"], ["3", "The businesses were real investments"]], size=42, src=SRC_BR),
   show="At trial, the government said, he did not dispute that he had moved more than $2 billion to his businesses. His defense blamed Davis, and the receiver, and called the businesses legitimate investments."),
 L("March sixth, two thousand twelve. After a six-week trial and about three days of deliberation, the jury found Stanford guilty on thirteen of fourteen counts.",
   doc("pr_conv", "MARCH 6, 2012", "Guilty on 13 of 14 counts", SRC_PRC),
   show="March 6, 2012. After a six-week trial and about three days of deliberation, the jury found Stanford guilty on 13 of 14 counts."),
 L("The one acquittal: a wire fraud count over nine thousand dollars in Super Bowl tickets for Leroy King. Two days later, the jury found twenty-nine accounts abroad, worth about three hundred thirty million dollars, were proceeds of the fraud.",
   dict(type="big", kicker="THE VERDICT", lines=["13 counts: guilty.", "1 count: not guilty."], src=SRC_BR + " · " + SRC_PRC),
   show="The one acquittal: a wire fraud count over $9,000 in Super Bowl tickets for Leroy King. Two days later, the jury found 29 accounts abroad, worth about $330 million, were proceeds of the fraud."),
 L("June fourteenth, two thousand twelve. The court had received more than three hundred fifty victim impact letters. The founder of a victims' coalition spoke at the hearing.",
   dict(type="quote", q="This was not a bloodless financial crime carried out on paper.", case=CASE, doc="AT SENTENCING · FOUNDER, STANFORD VICTIMS COALITION", cite=SRC_PRS, size=52),
   show="June 14, 2012. The court had received more than 350 victim impact letters. The founder of a victims' coalition spoke at the hearing."),
 L("Judge David Hittner called it one of the most egregious frauds ever presented to a trial jury in federal court.",
   doc("pr_judge", "JUDGE DAVID HITTNER", "“one of the most egregious frauds”", SRC_PRS)),
 L("The math: twenty years for the fraud conspiracy, twenty on each of four wire fraud counts, and five on each of the two obstruction counts. All consecutive.",
   dict(type="list", kicker="THE SENTENCE MATH", items=[["20", "Fraud conspiracy"], ["4 × 20", "Wire fraud"], ["5 + 5", "Obstructing the SEC"], ["110", "Years, consecutive"]], size=40, src=SRC_PRS),
   show="The math: 20 years for the fraud conspiracy, 20 on each of four wire fraud counts, and five on each of the two obstruction counts. All consecutive."),
 L("The total: one hundred ten years. The maximum had been two hundred thirty. The court also imposed a five point nine billion dollar money judgment.",
   dict(type="verdict", kicker="THE SENTENCE · JUNE 14, 2012", stamp="SENTENCED", big="110 years", sub="Robert Allen Stanford · plus a $5.9 billion money judgment"),
   show="The total: 110 years. The maximum had been 230. The court also imposed a $5.9 billion money judgment."),
 # VI
 L("Chapter six. After the verdict.", dict(type="chapter", n="VI", title="After the Verdict")),
 L("James Davis, who cooperated and testified, got five years. Laura Pendergest-Holt, the chief investment officer, pleaded guilty to obstruction and got three. The controller and the chief accounting officer, Mark Kuhrt and Gilbert Lopez, were convicted at trial and sentenced to twenty years each.",
   dict(type="bars", kicker="THE INSIDERS", title="Prison sentences", items=[{"label": "GILBERT LOPEZ", "value": 20, "display": "20 yrs"}, {"label": "MARK KUHRT", "value": 20, "display": "20 yrs"}, {"label": "JAMES DAVIS", "value": 5, "display": "5 yrs"}, {"label": "LAURA PENDERGEST-HOLT", "value": 3, "display": "3 yrs"}], src=SRC_DAVIS + " · " + SRC_HLK),
   show="James Davis, who cooperated and testified, got five years. Laura Pendergest-Holt, the chief investment officer, pleaded guilty to obstruction and got three. The controller and the chief accounting officer, Mark Kuhrt and Gilbert Lopez, were convicted at trial and sentenced to 20 years each."),
 L("In December two thousand twenty-four, according to Bloomberg Law, President Biden shortened Kuhrt's prison term in a clemency action. The Bureau of Prisons lists Lopez as released that same month.",
   dict(type="big", kicker="DECEMBER 2024 · BLOOMBERG LAW · BUREAU OF PRISONS", lines=["Kuhrt: term shortened.", "Lopez: released,|Dec. 2024."], src=SRC_BLK + " · " + SRC_BOP),
   show="In December 2024, according to Bloomberg Law, President Biden shortened Kuhrt's prison term in a clemency action. The Bureau of Prisons lists Lopez as released that same month."),
 L("At the time of Stanford's trial, Leroy King was still in Antigua, awaiting extradition. He was brought to the United States in November two thousand nineteen, pleaded guilty to obstruction, and in February two thousand twenty-one was sentenced to ten years.",
   dict(type="timeline", kicker="LEROY KING · PER THE JUSTICE DEPARTMENT", events=[{"date": "NOV 2019", "text": "Extradited to the U.S."}, {"date": "JAN 2020", "text": "Pleads guilty"}, {"date": "FEB 2021", "text": "Sentenced to 10 years"}], at=2, src=SRC_KING),
   show="At the time of Stanford's trial, Leroy King was still in Antigua, awaiting extradition. He was brought to the United States in November 2019, pleaded guilty to obstruction, and in February 2021 was sentenced to ten years."),
 L("Stanford appealed. In October two thousand fifteen, the Fifth Circuit affirmed. Stanford, the judges wrote, sat atop a massive Ponzi scheme.",
   dict(type="quote", q="Stanford sat atop a massive Ponzi scheme", case=CASE, doc="FIFTH CIRCUIT · AFFIRMED", cite=SRC_CA5, size=58),
   show="Stanford appealed. In October 2015, the Fifth Circuit affirmed. Stanford, the judges wrote, \"sat atop a massive Ponzi scheme.\""),
 L("In November two thousand sixteen, the Supreme Court declined to hear his case. In two thousand twenty-three, Judge Hittner again denied his request for compassionate release. The Bureau of Prisons lists him at a federal penitentiary in Florida, with a projected release date in the year twenty-one oh three.",
   dict(type="timeline", kicker="AFTER THE APPEAL", events=[{"date": "OCT 2015", "text": "Fifth Circuit affirms"}, {"date": "NOV 2016", "text": "Supreme Court declines to hear it"}, {"date": "2023", "text": "Compassionate release denied again"}, {"date": "2103", "text": "Projected release, per BOP"}], at=3, src=SRC_CA5 + " · " + SRC_IJ + " · " + SRC_BLC + " · " + SRC_BOP),
   show="In November 2016, the Supreme Court declined to hear his case. In 2023, Judge Hittner again denied his request for compassionate release. The Bureau of Prisons lists him at a federal penitentiary in Florida, with a projected release date in 2103."),
 L("The receiver went after the banks that had handled Stanford's money. By two thousand twenty-three, settlements with five banks, including one point two billion dollars from TD Bank, had topped one point six billion dollars.",
   dict(type="stat", kicker="BANK SETTLEMENTS · BY 2023", value="$1.6B+", label="recovered from five banks,|per reports", src=SRC_BANKS),
   show="The receiver went after the banks that had handled Stanford's money. By 2023, settlements with five banks, including $1.2 billion from TD Bank, had topped $1.6 billion."),
 L("And in January two thousand twenty-five, sixteen years after it sued, the S.E.C. got its final judgment: a civil penalty of five point nine billion dollars.",
   dict(type="big", kicker="JANUARY 29, 2025 · SEC FINAL JUDGMENT", lines=["16 years later:", "$5.9 billion|penalty."], src=SRC_SEC25),
   show="And in January 2025, sixteen years after it sued, the SEC got its final judgment: a civil penalty of $5.9 billion."),
 L("The warning was written down in nineteen ninety-seven. Possible Ponzi scheme.",
   dict(type="big", lines=["1997:", "“Possible Ponzi|scheme.”"])),
 L("Four examinations. A regulator taking cash. A bank that reported a profit every year. In the end, the case was decided on the paper trail.",
   dict(type="big", lines=["Four examinations.", "Then the|paper trail."])),
 L("This is SWORN. Real trials. Real evidence. The verdict.", dict(type="end")),
]
from panfix import fix
fix(lines, "long")
spec = {"label": "SWORN · CASE 004", "lines": lines}
json.dump(spec, open(os.path.join(HERE, "episode.json"), "w"), indent=1, ensure_ascii=False)
print(len(lines), "lines,", sum(len(l["say"].split()) for l in lines), "words")
