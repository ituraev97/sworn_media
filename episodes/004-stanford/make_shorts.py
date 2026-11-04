import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
def hl(name, i=0):
    a, b = HL[name][i]
    return [0.0, a, 1.0, round(b - a, 4)]
def doc(img, kicker, src, i=0):
    return dict(type="doc", img=f"img/{img}.jpg", pan=[0.0, 0.1], hl=hl(img, i), kicker=kicker, src=src)
CASE = "U.S. v. STANFORD"
SRC_OIG = "SEC Inspector General, OIG-526, 2010"
SRC_BR = "Gov't brief, 5th Cir. No. 12-20411, 2015"
SRC_CMP = "SEC amended complaint, Feb 27, 2009"
SRC_RCV = "Order Appointing Receiver, Feb 16, 2009"
SRC_PRC = "U.S. Attorney, S.D. Tex., Mar 6, 2012"
SRC_PRS = "U.S. Attorney, S.D. Tex., Jun 14, 2012"
SRC_CA5 = "5th Cir., No. 12-20411, Oct 29, 2015"
SRC_KING = "Justice Dept., Feb 24, 2021"
SRC_DAVIS = "Justice Dept., Jan 22, 2013"
SRC_HLK = "Justice Dept. Fraud Section"
SRC_BLK = "Bloomberg Law, Sept 19, 2025"
SRC_SEC25 = "SEC Lit. Release 26255, 2025"
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
END = L("Real trials. Real evidence. The verdict.", dict(type="end"))
shorts = [
 {"title": "The SEC Wrote \"Possible Ponzi Scheme\" in 1997. It Ran Until 2009", "hook": "The SEC knew|in 1997.", "lines": [
  L("Nineteen ninety-seven. S.E.C. examiners in Fort Worth review a Houston firm selling CDs from Allen Stanford's offshore bank.",
    dict(type="big", kicker="1997 · FORT WORTH", lines=["SEC examiners", "look at|Stanford."], src=SRC_OIG),
    show="1997. SEC examiners in Fort Worth review a Houston firm selling CDs from Allen Stanford's offshore bank."),
  L("Their conclusion, as quoted by the agency's own inspector general: Possible misrepresentations. Possible Ponzi scheme.",
    dict(type="quote", q="Possible misrepresentations. Possible Ponzi scheme.", case="SEC v. STANFORD", doc="1997 EXAMINATION", cite=SRC_OIG, size=52)),
  L("Examiners came back in nineteen ninety-eight, two thousand two and two thousand four.",
    dict(type="timeline", kicker="FOUR EXAMINATIONS", events=[{"date": "1997", "text": "Exam one"}, {"date": "1998", "text": "Exam two"}, {"date": "2002", "text": "Exam three"}, {"date": "2004", "text": "Exam four"}], at=3, src=SRC_OIG),
    show="Examiners came back in 1998, 2002 and 2004."),
  L("An enforcement inquiry opened in nineteen ninety-eight was closed after three months. The report found no meaningful effort to stop the fraud until late two thousand five.",
    dict(type="big", kicker="PER THE INSPECTOR GENERAL", lines=["Closed.", "Nothing until|late 2005."], src=SRC_OIG),
    show="An enforcement inquiry opened in 1998 was closed after three months. The report found no meaningful effort to stop the fraud until late 2005."),
  L("The bank kept selling until February two thousand nine, when a federal judge put it in the hands of a receiver.",
    doc("rcv", "FEBRUARY 16, 2009", SRC_RCV),
    show="The bank kept selling until February 2009, when a federal judge put it in the hands of a receiver."),
  L("Stanford was convicted, and sentenced to one hundred ten years.",
    dict(type="verdict", kicker="JUNE 14, 2012", stamp="SENTENCED", big="110 years", sub="Robert Allen Stanford"),
    show="Stanford was convicted, and sentenced to 110 years."),
  END]},
 {"title": "Where Allen Stanford's Bank Really Put Its Money: Tier 3", "hook": "Where the money|really went.", "lines": [
  L("Stanford International Bank told investors their money sat in safe, liquid, globally diversified investments.",
    dict(type="big", kicker="THE PITCH", lines=["Safe.", "Liquid.|Diversified."], src=SRC_PRS)),
  L("Prosecutors said the truth was in three tiers. Tier one, cash: ten percent. Tier two, what the analysts actually managed: fifteen percent.",
    dict(type="bars", kicker="PER PROSECUTORS", title="The bank's portfolio", items=[{"label": "TIER 1", "value": 10, "display": "10%"}, {"label": "TIER 2", "value": 15, "display": "15%"}, {"label": "TIER 3", "value": 75, "display": "75%"}], src=SRC_BR),
    show="Prosecutors said the truth was in three tiers. Tier one, cash: 10%. Tier two, what the analysts actually managed: 15%."),
  L("Tier three, seventy-five percent, went to Stanford's own companies, real estate and lifestyle.",
    doc("brief_tier", "TIER 3", SRC_BR),
    show="Tier three, 75%, went to Stanford's own companies, real estate and lifestyle."),
  L("More than two billion dollars, to over fifty businesses. Restaurants, two airlines, a newspaper, a cricket tournament, a one hundred twelve foot yacht.",
    doc("brief_piggy", "BY THE END OF 2008", SRC_BR),
    show="More than $2 billion, to over 50 businesses. Restaurants, two airlines, a newspaper, a cricket tournament, a 112-foot yacht."),
  L("By two thousand eight, about a million dollars a day of depositor money was keeping them afloat.",
    dict(type="stat", kicker="PER PROSECUTORS", value="$1M/day", label="of depositor money", src=SRC_BR),
    show="By 2008, about $1 million a day of depositor money was keeping them afloat."),
  L("A jury convicted Stanford on thirteen of fourteen counts.",
    doc("pr_conv", "MARCH 6, 2012", SRC_PRC),
    show="A jury convicted Stanford on 13 of 14 counts."),
  END]},
 {"title": "\"God Led Me to Hewlett\": The Auditor and the Regulator Behind Allen Stanford", "hook": "Who was|checking?", "lines": [
  L("Every year, Allen Stanford's bank published audited reports. The auditor was a one-man firm in Antigua, C.A.S. Hewlett.",
    doc("brief_hewlett", "THE AUDITOR", SRC_BR, 0)),
  L("In sixteen years, prosecutors said, he never got the documents to verify the assets. He signed off anyway.",
    dict(type="big", kicker="PER PROSECUTORS", lines=["16 years.", "No proof.|Signed anyway."], src=SRC_BR),
    show="In 16 years, prosecutors said, he never got the documents to verify the assets. He signed off anyway."),
  L("Prosecutors said Stanford paid him more than three point three million dollars from a Swiss account. According to his finance chief, Stanford told him: God led me to Hewlett.",
    dict(type="quote", q="God led me to Hewlett", case=CASE, doc="STANFORD TO DAVIS · PER TRIAL TESTIMONY", cite="As quoted in the gov't brief, 5th Cir. No. 12-20411, 2015", size=58),
    show="Prosecutors said Stanford paid him more than $3.3 million from a Swiss account. According to his finance chief, Stanford told him: \"God led me to Hewlett.\""),
  L("The regulator was Leroy King, head of Antigua's financial watchdog. He admitted taking about five hundred twenty-one thousand dollars in cash from Stanford.",
    dict(type="stat", kicker="LEROY KING", value="$520,963.87", label="cash from Stanford,|by his own admission", src=SRC_KING),
    show="The regulator was Leroy King, head of Antigua's financial watchdog. He admitted taking about $521,000 in cash from Stanford."),
  L("When the S.E.C. sent King a confidential request in two thousand five, prosecutors said he passed it straight to Stanford.",
    doc("brief_sec2005", "2005", SRC_BR, 1),
    show="When the SEC sent King a confidential request in 2005, prosecutors said he passed it straight to Stanford."),
  L("King was sentenced to ten years. Stanford, to one hundred ten.",
    dict(type="verdict", kicker="THE SENTENCES", stamp="SENTENCED", big="10 · 110 yrs", sub="Leroy King · Allen Stanford"),
    show="King was sentenced to ten years. Stanford, to 110."),
  END]},
 {"title": "The $541 Million That Never Arrived — Allen Stanford's Last Bluff", "hook": "$541 million?|Not quite.", "lines": [
  L("Late two thousand eight. Investors are pulling money out of Allen Stanford's bank.",
    dict(type="big", kicker="2008", lines=["Money out.", "Sales flat."], src=SRC_BR),
    show="Late 2008. Investors are pulling money out of Allen Stanford's bank."),
  L("Its December report tells them it just received a capital infusion of five hundred forty-one million dollars.",
    doc("cmp_541", "DECEMBER 2008 REPORT", SRC_CMP, 0),
    show="Its December report tells them it just received a capital infusion of $541 million."),
  L("The S.E.C. said it was real estate the bank already owned, acquired for about eighty-eight and a half million.",
    doc("cmp_541", "PER THE SEC'S COMPLAINT", SRC_CMP, 1),
    show="The SEC said it was real estate the bank already owned, acquired for about $88.5 million."),
  L("Prosecutors said accountants marked up land bought for sixty-three and a half million dollars by five thousand percent, to three point one billion, on paper.",
    dict(type="bars", kicker="PER THE JUSTICE DEPT.", title="Same land", items=[{"label": "ON PAPER", "value": 3100, "display": "$3.1B"}, {"label": "PAID", "value": 63.5, "display": "$63.5M"}], src=SRC_PRS),
    show="Prosecutors said accountants marked up land bought for $63.5 million by 5,000 percent, to $3.1 billion, on paper."),
  L("At his estate in Saint Croix, an employee testified, records were burned in barrels.",
    doc("brief_burn", "ST. CROIX", SRC_BR),
    show="At his estate in St. Croix, an employee testified, records were burned in barrels."),
  L("In February two thousand nine, a receiver took over. Stanford got one hundred ten years.",
    dict(type="verdict", kicker="JUNE 14, 2012", stamp="SENTENCED", big="110 years", sub="Robert Allen Stanford"),
    show="In February 2009, a receiver took over. Stanford got 110 years."),
  END]},
 {"title": "How a Judge Got to 110 Years for Allen Stanford", "hook": "How you get|110 years.", "lines": [
  L("March sixth, two thousand twelve. A Houston jury convicts Allen Stanford on thirteen of fourteen counts.",
    doc("pr_conv", "MARCH 6, 2012", SRC_PRC),
    show="March 6, 2012. A Houston jury convicts Allen Stanford on 13 of 14 counts."),
  L("The one acquittal: nine thousand dollars in Super Bowl tickets for an Antiguan regulator.",
    dict(type="big", kicker="NOT GUILTY · ONE COUNT", lines=["$9,000 in", "Super Bowl|tickets."], src=SRC_BR),
    show="The one acquittal: $9,000 in Super Bowl tickets for an Antiguan regulator."),
  L("Judge David Hittner called it one of the most egregious frauds ever presented to a trial jury in federal court.",
    doc("pr_judge", "JUNE 14, 2012", SRC_PRS)),
  L("Twenty years for the fraud conspiracy. Twenty on each of four wire fraud counts. Five on each of two obstruction counts. All consecutive.",
    dict(type="list", kicker="THE MATH", items=[["20", "Conspiracy"], ["80", "Wire fraud"], ["10", "Obstruction"]], size=40, src=SRC_PRS),
    show="20 years for the fraud conspiracy. 20 on each of four wire fraud counts. Five on each of two obstruction counts. All consecutive."),
  L("One hundred ten years, out of a possible two hundred thirty. Plus a five point nine billion dollar money judgment.",
    dict(type="verdict", kicker="THE SENTENCE", stamp="SENTENCED", big="110 years", sub="Maximum: 230 · Money judgment: $5.9B"),
    show="110 years, out of a possible 230. Plus a $5.9 billion money judgment."),
  L("The Fifth Circuit affirmed. Stanford, it wrote, sat atop a massive Ponzi scheme.",
    dict(type="quote", q="Stanford sat atop a massive Ponzi scheme", case=CASE, doc="FIFTH CIRCUIT", cite=SRC_CA5, size=52),
    show="The Fifth Circuit affirmed. Stanford, it wrote, \"sat atop a massive Ponzi scheme.\""),
  END]},
 {"title": "Allen Stanford's Inner Circle: What Happened to Each of Them", "hook": "What happened|to his team?", "lines": [
  L("Allen Stanford got one hundred ten years. His inner circle went to prison too.",
    dict(type="big", kicker="AFTER THE VERDICT", lines=["Stanford:", "110 years."], src=SRC_PRS),
    show="Allen Stanford got 110 years. His inner circle went to prison too."),
  L("His finance chief, James Davis, cooperated and testified. Five years. Laura Pendergest-Holt pleaded guilty to obstruction. Three years.",
    dict(type="bars", kicker="THE INSIDERS", title="Prison sentences", items=[{"label": "LOPEZ", "value": 20, "display": "20 yrs"}, {"label": "KUHRT", "value": 20, "display": "20 yrs"}, {"label": "DAVIS", "value": 5, "display": "5 yrs"}, {"label": "HOLT", "value": 3, "display": "3 yrs"}], src=SRC_DAVIS + " · " + SRC_HLK),
    show="His finance chief, James Davis, cooperated and testified. Five years. Laura Pendergest-Holt pleaded guilty to obstruction. Three years."),
  L("Accountants Gilbert Lopez and Mark Kuhrt were convicted at trial. Twenty years each. Bloomberg Law reports President Biden shortened Kuhrt's term in December two thousand twenty-four. Prison records list Lopez as released that month.",
    dict(type="big", kicker="BLOOMBERG LAW · PRISON RECORDS", lines=["Dec. 2024:", "Kuhrt cut.|Lopez out."], src=SRC_BLK + " · Federal Bureau of Prisons"),
    show="Accountants Gilbert Lopez and Mark Kuhrt were convicted at trial. 20 years each. Bloomberg Law reports President Biden shortened Kuhrt's term in December 2024. Prison records list Lopez as released that month."),
  L("Antigua's regulator, Leroy King, was extradited in two thousand nineteen. Ten years.",
    dict(type="timeline", kicker="LEROY KING", events=[{"date": "2019", "text": "Extradited"}, {"date": "2021", "text": "10 years"}], at=1, src=SRC_KING),
    show="Antigua's regulator, Leroy King, was extradited in 2019. Ten years."),
  L("And in January two thousand twenty-five, the S.E.C. won a final judgment against Stanford, with a five point nine billion dollar penalty.",
    dict(type="stat", kicker="SEC · JAN 29, 2025", value="$5.9B", label="civil penalty", src=SRC_SEC25),
    show="And in January 2025, the SEC won a final judgment against Stanford, with a $5.9 billion penalty."),
  END]},
]
from panfix import fix
for s in shorts: fix(s["lines"], "short")
for i, s in enumerate(shorts, 1):
    s["label"] = "SWORN"
    json.dump(s, open(os.path.join(HERE, f"short{i}.json"), "w"), indent=1, ensure_ascii=False)
    print(i, len(s["title"]), sum(len(l["say"].split()) for l in s["lines"]), "words", len(s["lines"]), "lines")
