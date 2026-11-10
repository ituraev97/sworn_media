import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
def hl(name, i=0):
    a, b = HL[name][i]
    return [0.0, a, 1.0, round(b - a, 4)]
CASE = "UNITED STATES v. SHKRELI"
FTC = "FTC v. VYERA PHARMACEUTICALS & SHKRELI"
SRC_R29 = "Memorandum & Order denying Rule 29 motion, U.S. v. Shkreli, No. 15-cr-637 (E.D.N.Y., Feb 26, 2018)"
SRC_IND = "Indictment, U.S. v. Shkreli & Greebel, No. 15-cr-637 (E.D.N.Y., Dec 2015)"
SRC_VER = "Jury Verdict Sheet, U.S. v. Shkreli, No. 15-cr-637 (E.D.N.Y.), ECF No. 305"
SRC_BAIL = "Government letter motion to revoke bail, U.S. v. Shkreli (E.D.N.Y., Sep 7, 2017)"
SRC_SM = "Government sentencing submission, U.S. v. Shkreli (E.D.N.Y., Mar 2018)"
SRC_DEF = "Defense sentencing memorandum, U.S. v. Shkreli (E.D.N.Y., Feb 27, 2018)"
SRC_JDG = "Judgment, U.S. v. Shkreli, No. 15-cr-637 (E.D.N.Y., Mar 2018)"
SRC_FORF = "Preliminary Order of Forfeiture, U.S. v. Shkreli (E.D.N.Y., Mar 5, 2018)"
SRC_CA2 = "U.S. v. Shkreli, Summary Order (2d Cir. 2019), ECF No. 716"
SRC_CR = "Memorandum & Order denying compassionate release, U.S. v. Shkreli (E.D.N.Y., May 16, 2020)"
SRC_FTC = "Opinion & Order, FTC et al. v. Vyera Pharmaceuticals et al., No. 20-cv-706 (S.D.N.Y., Jan 14, 2022)"
SRC_DOJ15 = "U.S. Attorney's Office, E.D.N.Y., press release (Dec 17, 2015)"
SRC_DOJ17 = "U.S. Attorney's Office, E.D.N.Y., press release (Aug 4, 2017)"
SRC_DOJ18 = "U.S. Attorney's Office, E.D.N.Y., press release (Mar 9, 2018)"
SRC_DOJ21 = "U.S. Attorney's Office, E.D.N.Y., press release (Jul 27, 2021)"
SRC_FTC24 = "Federal Trade Commission, statement (Jan 23, 2024)"
SRC_FOX = "FOX Business / FOX 5 New York (May 18, 2022), confirmed by the Bureau of Prisons"
def L(say, scene=None, show=None, **kw):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    d.update(kw); return d
def doc(img, kicker, title, src, i=0, pan=None):
    return dict(type="doc", img=f"img/{img}.jpg", pan=pan or [0.0, 0.1], hl=hl(img, i), kicker=kicker, title=title, src=src)
lines = [
 # COLD OPEN
 L("Martin Shkreli did not go to prison for the seven-hundred-fifty-dollar pill.",
   dict(type="big", kicker="WHY HE WENT TO PRISON", lines=["Not for", "the pill."], src=SRC_FTC),
   show="Martin Shkreli did not go to prison for the $750 pill."),
 L("In two thousand fifteen, a company he ran raised the price of a sixty-two-year-old drug, Daraprim, from seventeen dollars and sixty cents a tablet to seven hundred fifty dollars. A federal judge would later call it a four thousand percent increase.",
   doc("ftc_open", "FEDERAL COURT · S.D.N.Y. · 2022", "“by 4,000%”", SRC_FTC, 0),
   show="In 2015, a company he ran raised the price of a 62-year-old drug, Daraprim, from $17.60 a tablet to $750. A federal judge would later call it a 4,000% increase."),
 L("But none of the charges that sent him to prison were about Daraprim. They were about two hedge funds he ran years earlier, the drug company he founded after them, and the people who trusted him with their money.",
   doc("ftc_fn9", "THE SAME OPINION · PAGE 13", "“an unrelated federal conviction”", SRC_FTC, 0)),
 L("He told one of them his fund held about thirty-five million dollars. The fund, a federal judge wrote, never had more than about one point one three million at one time.",
   doc("r29_113", "U.S. DISTRICT COURT · E.D.N.Y. · 2018", "never more than ~$1.13 million", SRC_R29, 0),
   show="He told one of them his fund held about $35 million. The fund, a federal judge wrote, never had more than about $1.13 million at one time."),
 L("This is the paper trail.",
   dict(type="title", kicker="SWORN · CASE 010 · THE PAPER TRAIL", title="The Pharma Bro|Paper Trail", sub="United States v. Martin Shkreli · Brooklyn · 2017")),
 # I
 L("Chapter one. The pill.", dict(type="chapter", n="I", title="The Pill")),
 L("Daraprim treats toxoplasmosis, a parasitic infection that mainly strikes people with weakened immune systems, such as patients with HIV. The F.D.A. approved it in the nineteen-fifties. Until twenty twenty, it was the only F.D.A.-approved version of its active ingredient, pyrimethamine, on the U.S. market.",
   dict(type="big", kicker="DARAPRIM · PYRIMETHAMINE", lines=["Approved", "1953."], src=SRC_FTC),
   show="Daraprim treats toxoplasmosis, a parasitic infection that mainly strikes people with weakened immune systems, such as patients with HIV. The FDA approved it in the 1950s. Until 2020, it was the only FDA-approved version of its active ingredient, pyrimethamine, on the U.S. market."),
 L("In two thousand fourteen, Shkreli founded Turing Pharmaceuticals. The court found that from day one, his plan was to buy drugs that were the gold-standard treatment for rare, life-threatening diseases with only inferior alternatives, raise their prices, and block generic competition. He told early investors:",
   doc("ftc_turing", "FTC v. VYERA · FINDINGS OF FACT", "“pricing power”", SRC_FTC, 0),
   show="In 2014, Shkreli founded Turing Pharmaceuticals. The court found that from day one, his plan was to buy drugs that were the gold-standard treatment for rare, life-threatening diseases with only inferior alternatives, raise their prices, and block generic competition. He told early investors:"),
 L("Exclusivity, closed distribution, creates a barrier and pricing power.",
   dict(type="quote", q="[E]xclusivity (closed distribution) creates a barrier and pricing power.", case=FTC, doc="MARTIN SHKRELI · TO EARLY TURING INVESTORS", cite="As quoted in " + SRC_FTC, size=54)),
 L("In August two thousand fifteen, Turing paid fifty-five million dollars for Daraprim, more than eleven times its net revenue the year before. Within days, at Shkreli's direction, the list price went from seventeen sixty to seven hundred fifty dollars a tablet.",
   doc("ftc_price", "FTC v. VYERA · FINDINGS OF FACT", "$17.60 → $750", SRC_FTC, 0),
   show="In August 2015, Turing paid $55 million for Daraprim, more than 11 times its net revenue the year before. Within days, at Shkreli's direction, the list price went from $17.60 to $750 a tablet."),
 L("Years later, at the F.T.C.'s antitrust trial, even the company's own former head of research and development, Dr. Eliseo Salinas, called the price hike the poster child of everything that is considered wrong about the pharmaceutical industry.",
   dict(type="quote", q="poster child of everything that is considered wrong about the pharmaceutical industry.", case=FTC, doc="DR. ELISEO SALINAS · FORMER VYERA PRESIDENT OF R&D", cite="As quoted in " + SRC_FTC, size=50),
   show="Years later, at the FTC's antitrust trial, even the company's own former head of research and development, Dr. Eliseo Salinas, called the price hike the \"poster child of everything that is considered wrong about the pharmaceutical industry.\""),
 L("Sales volume fell by two thirds. But from twenty sixteen through twenty nineteen, the company made between fifty-five and seventy-four million dollars a year in gross profit on Daraprim, a drug whose revenue from twenty ten to twenty fourteen had been at most ten million dollars a year.",
   doc("ftc_vol", "FTC v. VYERA · FINDINGS OF FACT", "$55–74 million a year", SRC_FTC, 1),
   show="Sales volume fell by two thirds. But from 2016 through 2019, the company made between $55 and $74 million a year in gross profit on Daraprim, a drug whose revenue from 2010 to 2014 had been at most $10 million a year."),
 L("The price hike itself was never charged as a crime. What came with it, the blocking of generic competition, would land in court years later. But first, federal prosecutors came for him over something else entirely.",
   dict(type="big", kicker="DECEMBER 2015", lines=["A different", "case."], src=SRC_DOJ15)),
 # II
 L("Chapter two. Thirty-five million.", dict(type="chapter", n="II", title="$35 Million")),
 L("Rewind to two thousand nine. Shkreli, then in his twenties, launched a hedge fund in New York called MSMB Capital, focused on healthcare stocks. In two thousand eleven he started a second one, MSMB Healthcare.",
   doc("ind_cover", "THE INDICTMENT · DECEMBER 2015", "United States v. Martin Shkreli", SRC_IND, 0),
   show="Rewind to 2009. Shkreli, then in his twenties, launched a hedge fund in New York called MSMB Capital, focused on healthcare stocks. In 2011 he started a second one, MSMB Healthcare."),
 L("To raise money, he told people the fund was big and successful. At trial, a Merrill Lynch employee testified that in two thousand ten Shkreli told him MSMB Capital had approximately thirty-five million dollars under management, and was up fifty-three percent that year.",
   doc("r29_aum", "U.S. DISTRICT COURT · RULE 29 ORDER", "“approximately $35 million”", SRC_R29, 0),
   show="To raise money, he told people the fund was big and successful. At trial, a Merrill Lynch employee testified that in 2010 Shkreli told him MSMB Capital had \"approximately $35 million under management,\" and was \"up 53 percent\" that year."),
 L("Investors were told the fund used an outside auditor, Rothstein Kass, and an independent administrator, NAV Consulting. Shkreli later stipulated that neither firm ever provided services to MSMB Capital.",
   doc("r29_col", "U.S. DISTRICT COURT · RULE 29 ORDER", "The stipulation", SRC_R29, 1)),
 L("One investor testified Shkreli claimed to have graduated very young from Columbia. Columbia's registrar testified he had never enrolled at any school affiliated with the university. He had attended Baruch College.",
   doc("r29_col", "U.S. DISTRICT COURT · RULE 29 ORDER", "“never ‘enrolled’”", SRC_R29, 0),
   show="One investor testified Shkreli claimed to have \"graduated very young from Columbia.\" Columbia's registrar testified he had never enrolled at any school affiliated with the university. He had attended Baruch College."),
 L("In total, investors put about three point zero four million dollars into MSMB Capital, over its whole life. It never held more than about one point one three million at any one time.",
   dict(type="bars", kicker="MSMB CAPITAL · CLAIM vs. RECORD", title="Claimed vs. the bank records", items=[{"label": "What he claimed (AUM)", "value": 35, "display": "$35M"}, {"label": "Most it held at one time", "value": 1.13, "display": "$1.13M"}, {"label": "All money ever invested", "value": 3.04, "display": "$3.04M"}], src=SRC_R29),
   show="In total, investors put about $3.04 million into MSMB Capital, over its whole life. It never held more than about $1.13 million at any one time."),
 # III
 L("Chapter three. The fat finger.", dict(type="chapter", n="III", title="The Fat Finger")),
 L("February first, two thousand eleven. Shkreli bet against the stock of a drug company, Orexigen Therapeutics. The trade went wrong. The judge wrote that he lost almost all of the fund's capital.",
   doc("r29_lost", "U.S. DISTRICT COURT · RULE 29 ORDER", "“lost almost all of the fund's capital”", SRC_R29, 0),
   show="February 1, 2011. Shkreli bet against the stock of a drug company, Orexigen Therapeutics. The trade went wrong. The judge wrote that he lost almost all of the fund's capital."),
 L("Merrill Lynch, his broker, had to buy the stock to cover the position, and a Merrill witness testified the bank lost over seven million dollars.",
   doc("r29_orex", "U.S. DISTRICT COURT · RULE 29 ORDER", "“a loss of over $7 million”", SRC_R29, 0),
   show="Merrill Lynch, his broker, had to buy the stock to cover the position, and a Merrill witness testified the bank lost over $7 million."),
 L("He told the fund's biggest investor about the trade only in part, and called it a fat finger trading error: where you push sell but meant to push buy.",
   dict(type="quote", q="where you push sell but meant to push buy.", case=CASE, doc="SHKRELI'S EXPLANATION · AS AN INVESTOR TESTIFIED", cite="As quoted in " + SRC_R29, size=58),
   show="He told the fund's biggest investor about the trade only in part, and called it a \"fat finger\" trading error: \"where you push sell but meant to push buy.\""),
 L("Then the reports kept coming. Two months after the trade, the April tenth performance report told that investor MSMB had returned six point seven percent in March, and that his one point two five million dollar investment was now worth about one point three two million.",
   doc("r29_rep", "U.S. DISTRICT COURT · RULE 29 ORDER", "The April 10, 2011 report", SRC_R29, 0),
   show="Then the reports kept coming. Two months after the trade, the April 10 performance report told that investor MSMB had returned 6.7% in March, and that his $1.25 million investment was now worth $1,324,905."),
 L("The judge wrote that the fund had essentially no assets from the Orexigen trade through June two thousand twelve. Yet the statements he sent investors kept showing positive returns.",
   doc("r29_lost", "U.S. DISTRICT COURT · RULE 29 ORDER", "positive returns", SRC_R29, 1),
   show="The judge wrote that the fund had essentially no assets from the Orexigen trade through June 2012. Yet the statements he sent investors kept showing positive returns."),
 L("Meanwhile, prosecutors said, he raised more than five million dollars for his second fund without telling those investors what had happened to the first, and used its money to pay obligations that were not its own.",
   dict(type="stat", kicker="MSMB HEALTHCARE · 2011–2014", value="$5M+", label="raised from investors", src=SRC_DOJ17),
   show="Meanwhile, prosecutors said, he raised more than $5 million for his second fund without telling those investors what had happened to the first, and used its money to pay obligations that were not its own."),
 # IV
 L("Chapter four. Retrophin.", dict(type="chapter", n="IV", title="Retrophin")),
 L("In two thousand eleven Shkreli had also founded a drug company, Retrophin. By the end of two thousand twelve it was publicly traded, with him as chief executive. He wound the hedge funds down, and investors were paid, often in Retrophin shares and later through settlements and consulting agreements with Retrophin itself.",
   dict(type="timeline", kicker="MARTIN SHKRELI · 2009–2015", events=[{"date": "2009", "text": "MSMB Capital"}, {"date": "2011", "text": "MSMB Healthcare · Retrophin"}, {"date": "2012", "text": "Retrophin goes public"}, {"date": "2014", "text": "Out at Retrophin · Turing"}], at=2, src=SRC_IND),
   show="In 2011 Shkreli had also founded a drug company, Retrophin. By the end of 2012 it was publicly traded, with him as chief executive. He wound the hedge funds down, and investors were paid, often in Retrophin shares and later through settlements and consulting agreements with Retrophin itself."),
 L("Prosecutors charged that this was a third fraud: that he used Retrophin's money to pay off his fund investors. And a fourth: that he secretly controlled most of Retrophin's freely trading shares through people who held them in their names, to influence the stock's price and trading volume.",
   dict(type="list", kicker="AS CHARGED · SUPERSEDING INDICTMENT (2016)", items=[["1", "MSMB Capital investors"], ["2", "MSMB Healthcare investors"], ["3", "Retrophin's assets"], ["4", "Retrophin's stock"]], src="Superseding Indictment, U.S. v. Shkreli & Greebel (E.D.N.Y., June 2016), as described in Rule 29 Order (Feb 26, 2018) · " + SRC_DOJ17)),
 L("The indictment alleged that on December second, two thousand ten, he told an investor the fund had thirty-five million dollars under management. Two days earlier, its bank and brokerage accounts had held about seven hundred dollars.",
   doc("ind_35", "THE INDICTMENT · AS CHARGED", "“approximately $700”", SRC_IND, 1),
   show="The indictment alleged that on December 2, 2010, he told an investor the fund had $35 million under management. Two days earlier, its bank and brokerage accounts had held about $700."),
 L("On December seventeenth, two thousand fifteen, four months after the Daraprim price hike, the indictment was unsealed in Brooklyn. Shkreli was arrested and released on a five-million-dollar bond.",
   dict(type="big", kicker="DECEMBER 17, 2015 · BROOKLYN", lines=["Arrested.", "$5 million|bond."], src=SRC_DOJ15 + " · " + SRC_BAIL),
   show="On December 17, 2015, four months after the Daraprim price hike, the indictment was unsealed in Brooklyn. Shkreli was arrested and released on a $5 million bond."),
 L("Announcing the charges, the U.S. Attorney said: as alleged, Martin Shkreli engaged in multiple schemes to ensnare investors through a web of lies and deceit.",
   show="Announcing the charges, the U.S. Attorney said: \"As alleged, Martin Shkreli engaged in multiple schemes to ensnare investors through a web of lies and deceit.\"",
   scene=dict(type="quote", q="As alleged, Martin Shkreli engaged in multiple schemes to ensnare investors through a web of lies and deceit.", case=CASE, doc="U.S. ATTORNEY ROBERT L. CAPERS", cite=SRC_DOJ15, size=44)),
 # V
 L("Chapter five. The verdict.", dict(type="chapter", n="V", title="The Verdict")),
 L("The trial lasted six weeks. On August fourth, two thousand seventeen, after five days of deliberations, the jury came back with a split verdict on eight counts.",
   doc("r29_verd", "U.S. DISTRICT COURT · RULE 29 ORDER", "“The jury returned its verdict”", SRC_R29, 0),
   show="The trial lasted six weeks. On August 4, 2017, after five days of deliberations, the jury came back with a split verdict on eight counts."),
 L("Not guilty on five, including the charge that he conspired to use Retrophin's assets to pay off his fund investors.",
   doc("verdict", "THE JURY VERDICT SHEET", "Count by count", SRC_VER, 0)),
 L("Guilty on three: securities fraud involving MSMB Capital, securities fraud involving MSMB Healthcare, and conspiracy to commit securities fraud involving Retrophin's stock.",
   dict(type="verdict", kicker="AUGUST 4, 2017 · BROOKLYN", stamp="GUILTY", big="3 of 8 counts", sub="Martin Shkreli · securities fraud")),
 L("He stayed free on bail. Then, in September, he posted on Facebook offering five thousand dollars to anyone who would grab hair from former Secretary of State Hillary Clinton during her book tour. The Secret Service opened an investigation. Prosecutors asked the judge to jail him.",
   doc("bail", "U.S. ATTORNEY'S OFFICE · SEPT 7, 2017", "Motion to revoke bail", SRC_BAIL, 0),
   show="He stayed free on bail. Then, in September, he posted on Facebook offering $5,000 to anyone who would \"grab\" hair from former Secretary of State Hillary Clinton during her book tour. The Secret Service opened an investigation. Prosecutors asked the judge to jail him."),
 L("Shkreli added a line calling the post satire. On September thirteenth, two thousand seventeen, Judge Kiyo Matsumoto revoked his bail. He stayed in custody from that day.",
   dict(type="big", kicker="SEPTEMBER 13, 2017", lines=["Bail", "revoked."], src="Order of Detention, U.S. v. Shkreli (E.D.N.Y., Sep 13, 2017), ECF No. 367 · " + SRC_FTC),
   show="Shkreli added a line calling the post \"satire.\" On September 13, 2017, Judge Kiyo Matsumoto revoked his bail. He stayed in custody from that day."),
 # VI
 L("Chapter six. Seven years.", dict(type="chapter", n="VI", title="Seven Years")),
 L("At sentencing, his lawyers argued that none of his investors had actually lost money, and asked for twelve to eighteen months. The government asked for no less than one hundred eighty months: fifteen years.",
   doc("sm_core", "GOVERNMENT SENTENCING SUBMISSION · 2018", "“no less than 180 months”", SRC_SM, 0),
   show="At sentencing, his lawyers argued that none of his investors had actually lost money, and asked for 12 to 18 months. The government asked for no less than 180 months: 15 years."),
 L("Prosecutors wrote that the investors were repaid only because his frauds succeeded long enough to give his Retrophin shares some value. Their summary of the case:",
   doc("sm_core", "GOVERNMENT SENTENCING SUBMISSION · 2018", "“deception of people who trusted him”", SRC_SM, 1)),
 L("At its core, this case is about Shkreli's deception of people who trusted him.",
   dict(type="quote", q="At its core, this case is about Shkreli's deception of people who trusted him.", case=CASE, doc="ASSISTANT U.S. ATTORNEYS · E.D.N.Y.", cite=SRC_SM, size=52)),
 L("March ninth, two thousand eighteen. Judge Matsumoto sentenced him to eighty-four months in prison, seven years, and a seventy-five-thousand-dollar fine. She also found, by a preponderance of the evidence, that the Retrophin scheme the jury had acquitted him of had taken place.",
   dict(type="verdict", kicker="MARCH 9, 2018 · BROOKLYN", stamp="SENTENCED", big="7 years", sub="84 months · $75,000 fine"),
   show="March 9, 2018. Judge Matsumoto sentenced him to 84 months in prison, 7 years, and a $75,000 fine. She also found, by a preponderance of the evidence, that the Retrophin scheme the jury had acquitted him of had taken place."),
 L("He was ordered to forfeit seven million, three hundred sixty thousand, four hundred fifty dollars.",
   doc("forf", "PRELIMINARY ORDER OF FORFEITURE", "$7,360,450", SRC_FORF, 0),
   show="He was ordered to forfeit $7,360,450."),
 L("The order let the government take substitute assets: five million dollars in his bail account, his interest in Vyera, the former Turing, a Picasso painting, a Lil Wayne album, and the only copy of the Wu-Tang Clan album, Once Upon a Time in Shaolin.",
   doc("forf3", "PRELIMINARY ORDER OF FORFEITURE", "Substitute assets", SRC_FORF, 0),
   show="The order let the government take substitute assets: $5 million in his bail account, his interest in Vyera, the former Turing, a Picasso painting, a Lil Wayne album, and the only copy of the Wu-Tang Clan album, \"Once Upon a Time in Shaolin.\""),
 L("In two thousand nineteen, the Second Circuit affirmed. It rejected his argument that his investors' large returns should cut the forfeiture to zero. Forfeiture, the court said, is gain based.",
   doc("mandate", "U.S. COURT OF APPEALS · SECOND CIRCUIT", "AFFIRMED", SRC_CA2, 0),
   show="In 2019, the Second Circuit affirmed. It rejected his argument that his investors' large returns should cut the forfeiture to zero. Forfeiture, the court said, \"is gain based.\""),
 # VII
 L("Chapter seven. The pill, again.", dict(type="chapter", n="VII", title="The Pill, Again")),
 L("Prison did not end his interest in Daraprim. The court later found that he kept controlling the company from inside. In August two thousand nineteen, while incarcerated, he was recorded telling an employee:",
   doc("ftc_call", "FTC v. VYERA · FINDINGS OF FACT", "August 8, 2019", SRC_FTC, 0),
   show="Prison did not end his interest in Daraprim. The court later found that he kept controlling the company from inside. In August 2019, while incarcerated, he was recorded telling an employee:"),
 L("There has to be some way to tighten the supply chain a bit.",
   dict(type="quote", q="[T]here has to be some way to tighten the supply chain a bit . . .", case=FTC, doc="MARTIN SHKRELI · RECORDED FROM PRISON", cite="As quoted in " + SRC_FTC, size=56),
   show="\"There has to be some way to tighten the supply chain a bit . . .\""),
 L("In January twenty twenty, the Federal Trade Commission and seven states sued. They said his company had cut off generic makers from the samples and ingredients they needed. The first generic finally reached the market in March twenty twenty.",
   doc("ftc_open", "FEDERAL COURT · S.D.N.Y. · 2022", "“block the entry of generic drug competition”", SRC_FTC, 0),
   show="In January 2020, the Federal Trade Commission and seven states sued. They said his company had cut off generic makers from the samples and ingredients they needed. The first generic finally reached the market in March 2020."),
 L("That spring, Shkreli asked to be released early because of COVID. He said he could help develop a cure. Judge Matsumoto said no, noting probation's view that the claim was the type of delusional self-aggrandizing behavior that led to his crimes.",
   doc("covid", "U.S. DISTRICT COURT · MAY 16, 2020", "Compassionate release: denied", SRC_CR, 1),
   show="That spring, Shkreli asked to be released early because of COVID. He said he could help develop a cure. Judge Matsumoto said no, noting probation's view that the claim was the type of \"delusional self-aggrandizing behavior\" that led to his crimes."),
 L("In July twenty twenty-one, the government sold the Wu-Tang album. With that sale, the U.S. Attorney's Office said, his payment of the forfeiture was complete.",
   dict(type="quote", q="With today's sale of this one-of-a-kind album, his payment of the forfeiture is now complete.", case=CASE, doc="ACTING U.S. ATTORNEY JACQUELYN M. KASULIS", cite=SRC_DOJ21, size=46),
   show="In July 2021, the government sold the Wu-Tang album. \"With today's sale of this one-of-a-kind album,\" the U.S. Attorney's Office said, \"his payment of the forfeiture is now complete.\""),
 L("The F.T.C. case went to trial in December twenty twenty-one, without a jury. His company and its former chief executive settled on the eve of trial. Shkreli did not. Still in federal prison, he opted not to attend, the judge noted.",
   doc("ftc_fn9", "FTC v. VYERA · OPINION", "“He opted not to attend”", SRC_FTC, 0),
   show="The FTC case went to trial in December 2021, without a jury. His company and its former chief executive settled on the eve of trial. Shkreli did not. Still in federal prison, he \"opted not to attend,\" the judge noted."),
 L("January fourteenth, twenty twenty-two. Judge Denise Cote found he had delayed generic competition by at least eighteen months, and that he and his companies profited over sixty-four million dollars from the scheme.",
   doc("ftc_open", "OPINION & ORDER · JAN 14, 2022", "“profited over $64 million”", SRC_FTC, 1),
   show="January 14, 2022. Judge Denise Cote found he had delayed generic competition by at least eighteen months, and that he and his companies profited over $64 million from the scheme."),
 L("He was banned for life from the pharmaceutical industry, in any capacity, and ordered to disgorge sixty-four point six million dollars, reduced by whatever the settling defendants paid.",
   dict(type="verdict", kicker="JANUARY 14, 2022 · S.D.N.Y.", stamp="BANNED", big="For life", sub="Pharmaceutical industry · $64.6 million disgorgement"),
   show="He was banned for life from the pharmaceutical industry, in any capacity, and ordered to disgorge $64.6 million, reduced by whatever the settling defendants paid."),
 L("In May twenty twenty-two, the Bureau of Prisons moved him out of a low-security prison in Pennsylvania to a halfway house, months before his scheduled release. In January twenty twenty-four, the Second Circuit upheld the lifetime ban and the sixty-four point six million dollars.",
   dict(type="timeline", kicker="AFTER THE SENTENCE", events=[{"date": "2019", "text": "Conviction affirmed"}, {"date": "2021", "text": "Forfeiture complete"}, {"date": "2022", "text": "Lifetime ban · halfway house"}, {"date": "2024", "text": "Ban upheld on appeal"}], at=3, src=SRC_FOX + " · " + SRC_FTC24),
   show="In May 2022, the Bureau of Prisons moved him out of a low-security prison in Pennsylvania to a halfway house, months before his scheduled release. In January 2024, the Second Circuit upheld the lifetime ban and the $64.6 million."),
 L("Daraprim made him famous. The jury never heard a charge about it. What sent him to prison were his lies to investors, starting with a hedge fund he said held thirty-five million dollars, and that never held more than one point one three million.",
   doc("r29_113", "THE COURT RECORD", "never more than ~$1.13 million", SRC_R29, 0),
   show="Daraprim made him famous. The jury never heard a charge about it. What sent him to prison were his lies to investors, starting with a hedge fund he said held $35 million, and that never held more than $1.13 million."),
 L("Exclusivity created pricing power. The paper trail created the verdict.",
   dict(type="big", lines=["$35 million.", "$1.13|million."]),
   show="Exclusivity created pricing power. The paper trail created the verdict."),
 L("This is SWORN. Real trials. Real evidence. The verdict.", dict(type="end")),
]
from panfix import fix
fix(lines, "long")
spec = {"label": "SWORN · CASE 010", "lines": lines}
json.dump(spec, open(os.path.join(HERE, "episode.json"), "w"), indent=1, ensure_ascii=False)
print(len(lines), "lines,", sum(len(l["say"].split()) for l in lines), "words")
