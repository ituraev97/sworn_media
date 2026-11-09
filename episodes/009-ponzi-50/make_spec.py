import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
def hl(name, i=0):
    a, b = HL[name][i]
    return [0.0, a, 1.0, round(b - a, 4)]
# sources
RR_SENT = "U.S. Attorney, S.D. Fla. — release, Jun 9, 2010"
RR_PLEA = "U.S. Attorney, S.D. Fla. — release, Jan 27, 2010"
RR_AP = "Associated Press, Apr 16, 2018"
PT_AFF = "Criminal complaint & FBI affidavit, U.S. v. Petters, D. Minn. 08-MJ-364 (Oct 2008)"
PT_PR = "U.S. Attorney, D. Minn. — release, Apr 8, 2010"
PT_GOV = "Gov't Position Regarding Sentencing, U.S. v. Petters, D. Minn. No. 08-364, Dkt. 388"
PT_JUD = "Judgment, U.S. v. Petters, D. Minn. No. 08-364, Dkt. 400 (Apr 8, 2010)"
PT_APP = "KARE 11 (8th Cir. ruling) · Star Tribune (Supreme Court)"
OK_REL = "U.S. Attorney, E.D. Va. — release, Nov 17, 2011"
OK_OP = "Memorandum Opinion, U.S. v. Okun, E.D. Va. No. 3:08cr132, Dkt. 324 (Aug 27, 2009)"
ST_SENT = "Justice Dept. — release, Jun 14, 2012"
ST_CMP = "SEC First Amended Complaint, N.D. Tex. 3:09-cv-0298, Feb 27, 2009"
ST_BR = "Brief of the United States, 5th Cir. No. 12-20411 (2015)"
ST_BOP = "Federal Bureau of Prisons inmate locator, Nov 2026"
MD_ARR = "U.S. Attorney, S.D.N.Y. — release, Dec 11, 2008"
MD_PLEA = "U.S. Attorney, S.D.N.Y. — release, Mar 12, 2009"
MD_SENT = "U.S. Attorney, S.D.N.Y. — release, Jun 29, 2009"
MD_AP = "Associated Press, Apr 14, 2021"
def L(say, scene=None, show=None, **kw):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    d.update(kw); return d
def doc(img, kicker, title, src, i=0, pan=None):
    return dict(type="doc", img=f"img/{img}.jpg", pan=pan or [0.0, 0.1], hl=hl(img, i), kicker=kicker, title=title, src=src)
BARS = dict(type="bars", kicker="FIVE PONZI SCHEMES · FIVE FEDERAL SENTENCES", title="Years in prison",
            items=[{"label": "Rothstein", "value": 50, "display": "50"}, {"label": "Petters", "value": 50, "display": "50"},
                   {"label": "Okun", "value": 100, "display": "100"}, {"label": "Stanford", "value": 110, "display": "110"},
                   {"label": "Madoff", "value": 150, "display": "150"}],
            src=RR_SENT + " · " + PT_PR + " · " + OK_REL + " · " + ST_SENT + " · " + MD_SENT)
lines = [
 # COLD OPEN
 L("How long can a Ponzi scheme put you in prison? For the five men in this countdown, federal judges said: fifty years, or more.",
   dict(type="big", kicker="PONZI SCHEMES · FEDERAL SENTENCES", lines=["50 years", "or|more."]),
   show="How long can a Ponzi scheme put you in prison? For the five men in this countdown, federal judges said: 50 years, or more."),
 L("A lawyer whose firm sold lawsuit settlements that never existed. A businessman recorded by his own employee. A tax-exchange company that spent its clients' money. An offshore bank. And the biggest name of all.",
   BARS),
 L("Two got fifty years. One got a hundred. One, a hundred and ten. And one, a hundred and fifty.",
   show="Two got 50 years. One got 100. One, 110. And one, 150."),
 L("Every fact in this countdown comes from court records, the Justice Department, the SEC, and the reporting that followed. This is SWORN.",
   dict(type="title", kicker="SWORN · CASE 009 · THE COUNTDOWN", title="Fifty Years|or More", sub="Five Ponzi schemes · five federal sentences")),
 # 5 — ROTHSTEIN
 L("Number five. Fifty years.", dict(type="chapter", n="#5", kicker="50 YEARS", title="Scott Rothstein")),
 L("Scott Rothstein was a lawyer in Fort Lauderdale, Florida. He ran his scheme, the Justice Department said, through his own law firm, Rothstein Rosenfeldt and Adler.",
   doc("rr_head", "U.S. ATTORNEY · SOUTHERN DISTRICT OF FLORIDA", "A billion-dollar Ponzi scheme", RR_SENT)),
 L("The pitch: confidential settlements of civil lawsuits, sold to investors at a discount and repaid over time at full face value. The money, investors were told, would be held in the firm's trust account.",
   dict(type="big", kicker="THE PITCH · PER PROSECUTORS", lines=["Buy a settlement", "at a|discount."], src=RR_SENT)),
 L("The Justice Department put it plainly: the purported investment vehicles never existed.",
   doc("rr_never", "U.S. ATTORNEY · JUNE 9, 2010", "“never existed”", RR_SENT)),
 L("To make them look real, prosecutors said, Rothstein and others created false bank documents, false online bank account information, and false settlement agreements and promissory notes.",
   dict(type="list", kicker="PER THE JUSTICE DEPARTMENT", items=[["1", "False bank documents"], ["2", "False online bank account information"], ["3", "False settlement agreements"], ["4", "False promissory notes"]], src=RR_SENT)),
 L("Then they went further. Without its clients' knowledge, his firm had settled a lawsuit it filed for them, in the other side's favor. To hide it, prosecutors said, they created a false federal court order, purportedly signed by a U.S. District Judge, saying the clients had won about twenty-three million dollars.",
   doc("rr_order", "PER PROSECUTORS", "A false federal court order", RR_SENT, 0),
   show="Then they went further. Without its clients' knowledge, his firm had settled a lawsuit it filed for them, in the other side's favor. To hide it, prosecutors said, they created a false federal court order, purportedly signed by a U.S. District Judge, saying the clients had won about $23 million."),
 L("To collect it, the clients were told to post bonds. They wired about fifty-seven million dollars to a trust account he controlled.",
   doc("rr_order", "PER PROSECUTORS", "About $57 million", RR_SENT, 1),
   show="To collect it, the clients were told to post bonds. They wired about $57 million to a trust account he controlled."),
 L("From around two thousand five through November two thousand nine, he and others took in about one point two billion dollars.",
   dict(type="stat", kicker="2005 – 2009 · PER THE JUSTICE DEPARTMENT", value="$1.2B", label="obtained from investors", src=RR_PLEA),
   show="From around 2005 through November 2009, he and others took in about $1.2 billion."),
 L("He pleaded guilty to five counts, including racketeering conspiracy. On June ninth, two thousand ten, Judge James Cohn sentenced him to fifty years.",
   dict(type="verdict", kicker="JUNE 9, 2010 · FORT LAUDERDALE", stamp="SENTENCED", big="50 years", sub="Scott Rothstein · pleaded guilty"),
   show="He pleaded guilty to five counts, including racketeering conspiracy. On June 9, 2010, Judge James Cohn sentenced him to 50 years."),
 L("He went on to cooperate with prosecutors. But in two thousand eighteen, after prosecutors said he had given them false information, the judge let them withdraw an earlier offer to reduce his sentence. The fifty years stood.",
   dict(type="big", kicker="APRIL 2018 · PER THE ASSOCIATED PRESS", lines=["No reduction.", "50|years."], src=RR_AP),
   show="He went on to cooperate with prosecutors. But in 2018, after prosecutors said he had given them false information, the judge let them withdraw an earlier offer to reduce his sentence. The 50 years stood."),
 # 4 — PETTERS
 L("Number four. Also fifty years.", dict(type="chapter", n="#4", kicker="50 YEARS", title="Tom Petters")),
 L("Tom Petters, of Wayzata, Minnesota, bought companies including Fingerhut, Polaroid and Sun Country Airlines. The Justice Department said he paid for them with proceeds of his fraud.",
   dict(type="big", kicker="PETTERS GROUP WORLDWIDE · PER THE JUSTICE DEPARTMENT", lines=["Polaroid.", "Fingerhut.|Sun Country."], src=PT_PR)),
 L("At the center was Petters Company, Inc. Investors lent it money to buy electronics that would be resold to big-box retailers, like Costco and Sam's Club, at a profit. However, the Justice Department said, no such purchases were made.",
   doc("pet_cw", "FBI AFFIDAVIT · OCTOBER 2008", "“entirely fabricated”", PT_AFF + " · " + PT_PR, 1)),
 L("A Walmart security official told agents that the vendor number on Petters' Sam's Club purchase orders was fictitious.",
   doc("pet_wm", "FBI AFFIDAVIT · OCTOBER 2008", "“fictitious”", PT_AFF)),
 L("From two thousand three to September two thousand eight, about thirty-five billion dollars was wired into one account that only Petters and one employee were authorized to use. None of the deposits came from retailers.",
   doc("pet_flow", "U.S. ATTORNEY · DISTRICT OF MINNESOTA", "About $35 billion", PT_PR),
   show="From 2003 to September 2008, about $35 billion was wired into one account that only Petters and one employee were authorized to use. None of the deposits came from retailers."),
 L("The money passed through two so-called vendors. One of them, the Justice Department said, was a sham company with its headquarters above a car wash, a few miles from Petters' headquarters. It did no real business. Money only flowed one way: to Petters' company.",
   dict(type="big", kicker="THE \"VENDORS\" · PER THE JUSTICE DEPARTMENT", lines=["Above a", "car|wash."], src=PT_PR)),
 L("The employee who shared that account was Deanna Coleman. On September eighth, two thousand eight, she and her attorney went to the authorities. She agreed to wear a recording device.",
   doc("pet_cw", "FBI AFFIDAVIT · THE COOPERATING WITNESS", "September 8, 2008", PT_AFF + " · " + PT_PR, 0),
   show="The employee who shared that account was Deanna Coleman. On September 8, 2008, she and her attorney went to the authorities. She agreed to wear a recording device."),
 L("Within the first few hours of her recordings, the Justice Department said, Petters was heard admitting that purchase orders were fake, and claiming divine intervention was the only explanation for how they could have got away with this for so long.",
   doc("pet_pr", "U.S. ATTORNEY · APRIL 8, 2010", "“divine intervention”", PT_PR),
   show="Within the first few hours of her recordings, the Justice Department said, Petters was heard admitting that purchase orders were \"fake,\" and claiming \"divine intervention\" was the only explanation for how they \"could of got away with this for so long.\""),
 L("On the recordings, the FBI agent wrote, Petters also talked about fleeing the country. On September twenty-fourth, agents searched his headquarters and his home. On October third, he was arrested.",
   doc("pet_rec", "FBI AFFIDAVIT · THE RECORDINGS", "Fleeing the country", PT_AFF, 1),
   show="On the recordings, the FBI agent wrote, Petters also talked about fleeing the country. On September 24, agents searched his headquarters and his home. On October 3, he was arrested."),
 L("Petters went to trial. On December second, two thousand nine, the jury convicted him on all twenty counts. Prosecutors argued for the maximum the counts allowed: three hundred thirty-five years.",
   doc("pet_gov", "THE GOVERNMENT'S SENTENCING POSITION", "335 years", PT_GOV + " · " + PT_JUD),
   show="Petters went to trial. On December 2, 2009, the jury convicted him on all 20 counts. Prosecutors argued for the maximum the counts allowed: 335 years."),
 L("On April eighth, two thousand ten, Judge Richard Kyle gave him six hundred months. Fifty years. The U.S. Attorney's office called it the longest prison term ever ordered in a financial fraud case in Minnesota history.",
   doc("pet_judg", "JUDGMENT · APRIL 8, 2010", "600 months · 50 years", PT_JUD + " · " + PT_PR),
   show="On April 8, 2010, Judge Richard Kyle gave him 600 months. 50 years. The U.S. Attorney's office called it the longest prison term ever ordered in a financial fraud case in Minnesota history."),
 L("On Petters' own testimony at trial, the judge said: It just didn't pass the smell test.",
   dict(type="quote", q="It just didn't pass the smell test.", case="UNITED STATES v. PETTERS", doc="JUDGE RICHARD H. KYLE · AT SENTENCING", cite="As quoted in " + PT_PR, size=60),
   show="On Petters' own testimony at trial, the judge said: \"It just didn't pass the smell test.\""),
 L("A federal appeals court upheld the conviction and the sentence. The Supreme Court declined to review it.",
   dict(type="verdict", kicker="DECEMBER 2, 2009 · ST. PAUL", stamp="GUILTY", big="50 years", sub="Tom Petters · 20 of 20 counts"),
   show="A federal appeals court upheld the conviction and the sentence. The Supreme Court declined to review it."),
 # 3 — OKUN
 L("Number three. One hundred years. And the smallest dollar figure on this list.", dict(type="chapter", n="#3", kicker="100 YEARS", title="Edward Okun")),
 L("Edward Okun owned The ten thirty-one Tax Group. The name comes from Section ten thirty-one of the tax code. Sell an investment property, leave the proceeds with a company called a qualified intermediary, buy a new property within a set time, and you can put off the capital gains tax.",
   dict(type="list", kicker="SECTION 1031 · AS THE JUSTICE DEPARTMENT EXPLAINED IT", items=[["1", "Sell an investment property"], ["2", "Deposit the proceeds with a qualified intermediary"], ["3", "Buy new property in time"], ["4", "Defer the capital gains tax"]], src=OK_REL),
   show="Edward Okun owned The 1031 Tax Group. The name comes from Section 1031 of the tax code. Sell an investment property, leave the proceeds with a company called a qualified intermediary, buy a new property within a set time, and you can put off the capital gains tax."),
 L("Clients were promised their money would be used solely for those exchanges. Instead, the evidence at trial showed, Okun and others misappropriated about one hundred twenty-six million dollars of client funds.",
   doc("ok_126", "U.S. ATTORNEY · EASTERN DISTRICT OF VIRGINIA", "About $126 million", OK_REL),
   show="Clients were promised their money would be used solely for those exchanges. Instead, the evidence at trial showed, Okun and others misappropriated about $126 million of client funds."),
 L("It paid for his lavish lifestyle, his companies' expenses and commercial real estate. It also bought more qualified intermediary companies, and with them, more client money to take.",
   dict(type="big", kicker="WHERE THE MONEY WENT · PER THE JUSTICE DEPARTMENT", lines=["Buy a company.", "Take its|clients' money."], src=OK_REL)),
 L("The trial judge, Robert Payne, put it this way.",
   doc("ok_ponzi", "MEMORANDUM OPINION · AUGUST 27, 2009", "“somewhat unconventional”", OK_OP)),
 L("In sum, Okun was running a large, somewhat unconventional Ponzi scheme.",
   dict(type="quote", q="In sum, Okun was running a large, somewhat unconventional Ponzi scheme.", case="UNITED STATES v. OKUN", doc="JUDGE ROBERT E. PAYNE · E.D. VA.", cite=OK_OP, size=54)),
 L("The evidence also showed he had employees withdraw fifteen thousand dollars in cash and smuggle it to his personal yacht in the Bahamas, to avoid federal currency reporting requirements.",
   doc("ok_cash", "U.S. ATTORNEY · NOVEMBER 17, 2011", "$15,000 to the yacht", OK_REL),
   show="The evidence also showed he had employees withdraw $15,000 in cash and smuggle it to his personal yacht in the Bahamas, to avoid federal currency reporting requirements."),
 L("On March nineteenth, two thousand nine, a jury in Richmond, Virginia, convicted him of fraud, money laundering, bulk cash smuggling and perjury, among other charges. On August fourth, Judge Payne sentenced him to one hundred years.",
   dict(type="verdict", kicker="AUGUST 4, 2009 · RICHMOND", stamp="SENTENCED", big="100 years", sub="Edward H. Okun · $126 million"),
   show="On March 19, 2009, a jury in Richmond, Virginia, convicted him of fraud, money laundering, bulk cash smuggling and perjury, among other charges. On August 4, Judge Payne sentenced him to 100 years."),
 L("In two thousand eleven, the Fourth Circuit upheld the conviction and the sentence. The U.S. Attorney said:",
   doc("ok_rel", "U.S. ATTORNEY · NOVEMBER 17, 2011", "Upheld", OK_REL),
   show="In 2011, the Fourth Circuit upheld the conviction and the sentence. The U.S. Attorney said:"),
 L("Financial fraudsters make calculated, rational decisions, and the threat of spending as much as one hundred years in prison can begin to change corporate culture and behavior.",
   dict(type="quote", q="Financial fraudsters make calculated, rational decisions, and the threat of spending as much as 100 years in prison can begin to change corporate culture and behavior.", case="UNITED STATES v. OKUN", doc="U.S. ATTORNEY NEIL H. MacBRIDE", cite=OK_REL, size=42),
   show="\"Financial fraudsters make calculated, rational decisions, and the threat of spending as much as 100 years in prison can begin to change corporate culture and behavior.\""),
 # 2 — STANFORD
 L("Number two. One hundred and ten years.", dict(type="chapter", n="#2", kicker="110 YEARS", title="Allen Stanford")),
 L("R. Allen Stanford was chairman of the board of Stanford International Bank, based on the Caribbean island of Antigua. It sold certificates of deposit. By the end of two thousand eight, the SEC said, about eight billion dollars of them.",
   dict(type="stat", kicker="STANFORD INTERNATIONAL BANK · PER THE SEC", value="$8B", label="in certificates of deposit|sold by the end of 2008", src=ST_CMP + " · " + ST_SENT),
   show="R. Allen Stanford was chairman of the board of Stanford International Bank, based on the Caribbean island of Antigua. It sold certificates of deposit. By the end of 2008, the SEC said, about $8 billion of them."),
 L("For at least a decade, the SEC alleged, Stanford and his chief financial officer executed a massive Ponzi scheme.",
   doc("st_cmp", "SEC · FIRST AMENDED COMPLAINT", "“a massive Ponzi scheme”", ST_CMP)),
 L("Where did the money go? According to the government's appeals brief, only about a quarter of the bank's reported assets were invested the way the bank described. Stanford siphoned the remaining seventy-five percent, known as Tier Three, to his companies, real estate purchases, and lifestyle.",
   doc("st_tier", "BRIEF OF THE UNITED STATES", "“Tier 3” · 75%", ST_BR),
   show="Where did the money go? According to the government's appeals brief, only about a quarter of the bank's reported assets were invested the way the bank described. Stanford siphoned the remaining 75%, \"Tier 3,\" to his companies, real estate purchases, and lifestyle."),
 L("In March two thousand twelve, a Houston jury convicted him on thirteen of fourteen counts. That June, Judge David Hittner sentenced him to one hundred ten years, for what the Justice Department called a twenty-year investment fraud scheme in which he misappropriated seven billion dollars.",
   doc("st_sent", "JUSTICE DEPARTMENT · JUNE 14, 2012", "110 years", ST_SENT),
   show="In March 2012, a Houston jury convicted him on 13 of 14 counts. That June, Judge David Hittner sentenced him to 110 years, for what the Justice Department called a 20-year investment fraud scheme in which he misappropriated $7 billion."),
 L("The judge called it one of the most egregious frauds ever presented to a trial jury in federal court.",
   dict(type="quote", q="this is one of the most egregious frauds ever presented to a trial jury in federal court.", case="UNITED STATES v. STANFORD", doc="JUDGE DAVID HITTNER · AT SENTENCING", cite="As quoted in U.S. Attorney, S.D. Tex. — release, Jun 14, 2012", size=50)),
 L("The Fifth Circuit affirmed. The Bureau of Prisons lists his projected release date in the year twenty-one oh three.",
   dict(type="stat", kicker="R. ALLEN STANFORD · FEDERAL BUREAU OF PRISONS", value="2103", label="projected release date", src=ST_BOP),
   show="The Fifth Circuit affirmed. The Bureau of Prisons lists his projected release date in the year 2103."),
 # 1 — MADOFF
 L("Number one. One hundred and fifty years.", dict(type="chapter", n="#1", kicker="150 YEARS", title="Bernard Madoff")),
 L("On December tenth, two thousand eight, according to federal prosecutors, Bernard Madoff told senior employees that his investment advisory business was a fraud. That it was all just one big lie. Basically, a giant Ponzi scheme.",
   doc("md_lie", "U.S. ATTORNEY · DECEMBER 11, 2008", "“one big lie”", MD_ARR),
   show="On December 10, 2008, according to federal prosecutors, Bernard Madoff told senior employees that his investment advisory business was a fraud. That \"it's all just one big lie.\" \"Basically, a giant Ponzi scheme.\""),
 L("Months earlier, in a January two thousand eight filing with the SEC, he had reported that this advisory business had about seventeen point one billion dollars under management, for between eleven and twenty-five clients.",
   dict(type="big", kicker="JANUARY 2008 · FILED WITH THE SEC", lines=["$17.1 billion", "11 to 25|clients."], src=MD_ARR),
   show="Months earlier, in a January 2008 filing with the SEC, he had reported that this advisory business had about $17.1 billion under management, for between 11 and 25 clients."),
 L("That December, he estimated the losses at approximately fifty billion dollars, at least.",
   dict(type="stat", kicker="DECEMBER 2008 · MADOFF'S OWN ESTIMATE", value="$50B", label="in losses, at least", src=MD_ARR),
   show="That December, he estimated the losses at approximately $50 billion, at least."),
 L("He was arrested the next day. In March two thousand nine, he pleaded guilty to all eleven counts. There was no trial.",
   dict(type="big", kicker="MARCH 12, 2009 · MANHATTAN", lines=["11 counts.", "Guilty."], src=MD_PLEA),
   show="He was arrested the next day. In March 2009, he pleaded guilty to all 11 counts. There was no trial."),
 L("On June twenty-ninth, two thousand nine, Judge Denny Chin sentenced him to one hundred fifty years. He called the crimes extraordinarily evil.",
   doc("md_sent", "U.S. ATTORNEY · JUNE 29, 2009", "150 years", MD_SENT),
   show="On June 29, 2009, Judge Denny Chin sentenced him to 150 years. He called the crimes \"extraordinarily evil.\""),
 L("And he said it was not merely a bloodless crime that takes place on paper, but one that takes a staggering human toll.",
   dict(type="quote", q="not merely a bloodless crime that takes place on paper but one that takes a staggering human toll.", case="UNITED STATES v. MADOFF", doc="JUDGE DENNY CHIN · AT SENTENCING", cite="As quoted in " + MD_SENT, size=48),
   show="And he said it was \"not merely a bloodless crime that takes place on paper but one that takes a staggering human toll.\""),
 L("Madoff died in federal prison in April two thousand twenty-one. He was eighty-two.",
   dict(type="verdict", kicker="JUNE 29, 2009 · MANHATTAN", stamp="SENTENCED", big="150 years", sub="Bernard L. Madoff · died in prison, 2021"),
   show="Madoff died in federal prison in April 2021. He was 82."),
 # CLOSE
 L("Five schemes. Look at what they ran on. Purchase orders for goods that were never bought. Settlements that never existed. A court order no judge signed. Promises to keep clients' money safe that were not kept. And statements, from Madoff and Stanford alike, that hid what the money was really doing.",
   dict(type="list", kicker="WHAT THEY RAN ON", items=[["#5", "Settlements that never existed"], ["#4", "Fabricated purchase orders"], ["#3", "Exchange money spent"], ["#2", "A bank's hidden “Tier 3”"], ["#1", "“One big lie”"]],
        src="Court records and Justice Department releases shown in this episode")),
 L("Two pleaded guilty. Three went to trial and lost. All five received fifty years or more.",
   BARS, show="Two pleaded guilty. Three went to trial and lost. All five received 50 years or more."),
 L("Madoff died in prison. Edward Okun died in prison, the Free Lance-Star of Virginia reported. Stanford is still in federal prison. Petters and Rothstein lost their bids for relief.",
   dict(type="big", kicker="WHERE THEY ARE", lines=["The sentences", "stood."], src=MD_AP + " · Free Lance-Star · " + ST_BOP + " · " + PT_APP + " · " + RR_AP),
   show="Madoff died in prison. Edward Okun died in prison, the Free Lance-Star of Virginia reported. Stanford is still in federal prison. Petters and Rothstein lost their bids for relief."),
 L("This is SWORN. Real trials. Real evidence. The verdict.", dict(type="end")),
]
from panfix import fix
fix(lines, "long")
spec = {"label": "SWORN · CASE 009", "lines": lines}
json.dump(spec, open(os.path.join(HERE, "episode.json"), "w"), indent=1, ensure_ascii=False)
print(len(lines), "lines,", sum(len(l["say"].split()) for l in lines), "words")
