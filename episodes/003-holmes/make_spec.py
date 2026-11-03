import json
CASE = "U.S. v. HOLMES"
SRC_IND = "Indictment, Dkt. 1, N.D. Cal., Jun 14, 2018"
SRC_TSI = "Third Superseding Indictment, Dkt. 469, N.D. Cal., Jul 28, 2020"
SRC_VF = "Final verdict form, Dkt. 1235, N.D. Cal., Jan 3, 2022"
SRC_MEMO = "Gov't sentencing memorandum, Dkt. 1643, Nov 11, 2022"
SRC_MIN = "Criminal minutes, sentencing, Dkt. 1660, Nov 18, 2022"
SRC_SO = "Order on sentencing, Dkt. 1712, Jan 10, 2023"
SRC_JUDG = "Judgment, Dkt. 1716, N.D. Cal., Jan 11, 2023"
SRC_BAIL = "Order denying release pending appeal, Dkt. 1757, Apr 10, 2023"
SRC_REST = "Order on restitution, Dkt. 1760, May 16, 2023"
SRC_CA9 = "U.S. Court of Appeals, 9th Cir., No. 22-10312 (amended Dec 22, 2025)"
SRC_RS = "Order granting sentence modification, Dkt. 1816, Mar 26, 2026"
SRC_SEC = "SEC press release 2018-41, Mar 14, 2018"
SRC_DOJV = "U.S. Attorney, N.D. Cal. — release, Jan 4, 2022"
SRC_DOJC = "U.S. Attorney, N.D. Cal. — case page, U.S. v. Holmes et al."
SRC_FORBES = "Forbes, Sept 24, 2026"
MEMOQ = "As quoted in the gov't sentencing memorandum, Nov 11, 2022"
def L(say, scene=None, show=None, **kw):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    d.update(kw); return d
lines = [
 # COLD OPEN
 L("January third, two thousand twenty-two. San Jose, California. A federal jury returns its verdict on the founder of Theranos, Elizabeth Holmes.",
   dict(type="doc", img="img/verdict1.jpg", pan=[0.0, 0.1], hl=[0.0, 0.24, 1.0, 0.12], kicker="JANUARY 3, 2022 · FINAL VERDICT FORM", title="United States v. Elizabeth A. Holmes", src=SRC_VF),
   show="January 3, 2022. San Jose, California. A federal jury returns its verdict on the founder of Theranos, Elizabeth Holmes."),
 L("Count one. Conspiracy to commit wire fraud against Theranos investors. Guilty.",
   dict(type="doc", img="img/verdict1.jpg", pan=[0.28, 0.36], hl=[0.0, 0.50, 1.0, 0.115], kicker="COUNT ONE · INVESTORS", title="“Guilty”", src=SRC_VF)),
 L("Count two. Conspiracy to commit wire fraud against Theranos patients. Not guilty.",
   dict(type="doc", img="img/verdict1.jpg", pan=[0.36, 0.42], hl=[0.0, 0.615, 1.0, 0.105], kicker="COUNT TWO · PATIENTS", title="“Not Guilty”", src=SRC_VF)),
 L("Three more counts involving investors: guilty. The patient counts: not guilty. And on three counts, the jury could not agree.",
   dict(type="doc", img="img/verdict2.jpg", pan=[0.2, 0.3], hl=[0.0, 0.48, 1.0, 0.45], kicker="COUNTS SIX, SEVEN, EIGHT · INVESTORS", title="“Guilty”", src=SRC_VF + " · Minute order, Dkt. 1236")),
 L("A split verdict. The jury found that she had defrauded the people who invested in her company. This is the case prosecutors made, and what happened to her after.",
   dict(type="big", kicker="THE VERDICT", lines=["Investors: guilty.", "Patients: not guilty."], src=SRC_JUDG)),
 L("This is SWORN.",
   dict(type="title", kicker="SWORN · CASE 003", title="The Theranos|Verdict", sub="United States v. Elizabeth A. Holmes · Northern District of California · 2018–2026")),
 # I
 L("Chapter one. One tiny drop.", dict(type="chapter", n="I", title="One Tiny Drop")),
 L("Holmes founded Theranos in two thousand three, and served as its chief executive until two thousand eighteen, according to the federal appeals court.",
   dict(type="big", kicker="THERANOS", lines=["Founded 2003.", "Holmes: CEO|until 2018."], src=SRC_CA9),
   show="Holmes founded Theranos in 2003, and served as its chief executive until 2018, according to the federal appeals court."),
 L("The court opened its opinion with the vision she sold. One tiny drop changes everything.",
   dict(type="quote", q="[O]ne tiny drop changes everything.", case=CASE, doc="THE VISION · AS QUOTED BY THE COURT", cite="9th Cir. opinion, No. 22-10312", size=60)),
 L("Theranos claimed, the court wrote, that it could run fast, accurate and affordable tests with just a drop of blood drawn from the prick of a finger.",
   dict(type="doc", img="img/ca9.jpg", pan=[0.08, 0.16], hl=[0.0, 0.28, 1.0, 0.12], kicker="NINTH CIRCUIT · OPINION", title="“just a drop of blood”", src=SRC_CA9)),
 L("In two thousand ten, Theranos partnered with Walgreens. In the fall of two thousand thirteen, it launched its testing services in Walgreens stores, then raised new money from investors.",
   dict(type="timeline", kicker="THERANOS AND WALGREENS", events=[{"date": "2003", "text": "Holmes founds Theranos"}, {"date": "2010", "text": "Partnership with Walgreens"}, {"date": "FALL 2013", "text": "Testing launches at Walgreens"}], at=2, src=SRC_CA9),
   show="In 2010, Theranos partnered with Walgreens. In the fall of 2013, it launched its testing services in Walgreens stores, then raised new money from investors."),
 L("By the end of two thousand fourteen, prosecutors said, Holmes's own shares in Theranos were valued at more than four billion dollars.",
   dict(type="stat", kicker="END OF 2014 · PER PROSECUTORS", value="$4B+", label="the value of Holmes's own|Theranos shares", src=SRC_MEMO),
   show="By the end of 2014, prosecutors said, Holmes's own shares in Theranos were valued at more than $4 billion."),
 L("She was on the covers of Fortune and Forbes. Time named her one of the hundred most influential people in the world.",
   dict(type="big", kicker="PER PROSECUTORS", lines=["Fortune. Forbes. Inc.", "Time's 100 Most|Influential People."], src=SRC_MEMO),
   show="She was on the covers of Fortune and Forbes. Time named her one of the 100 most influential people in the world."),
 # II
 L("Chapter two. The pitch.", dict(type="chapter", n="II", title="The Pitch")),
 L("Prosecutors laid out what Holmes told investors. One Theranos device could run any blood test a conventional lab could, from a fingerstick. Major drug companies had validated it. The military was using it. And the business was profitable.",
   dict(type="list", kicker="THE PITCH · PER PROSECUTORS", items=[["1", "One device, any blood test"], ["2", "Validated by drug companies"], ["3", "Used by the military"], ["4", "A profitable business"]], size=42, src=SRC_MEMO)),
 L("In truth, the government said, the Theranos device could never complete more than twelve types of blood tests. To fill out its menu, the company quietly used modified and unmodified machines made by other companies.",
   dict(type="doc", img="img/memo_twelve.jpg", pan=[0.15, 0.25], hl=[0.0, 0.37, 1.0, 0.17], kicker="THE GOVERNMENT'S CASE", title="“never complete more than 12 types of blood tests”", src=SRC_MEMO),
   show="In truth, the government said, the Theranos device could never complete more than 12 types of blood tests. To fill out its menu, the company quietly used modified and unmodified machines made by other companies."),
 L("Theranos had zero revenue in two thousand twelve and two thousand thirteen. Yet investors were given projections of one hundred forty million dollars in revenue for two thousand fourteen, and nearly one billion for two thousand fifteen.",
   dict(type="bars", kicker="REVENUE · PER PROSECUTORS", title="Projected vs. actual", items=[{"label": "2015 PROJECTED", "value": 1000, "display": "~$1B"}, {"label": "2014 PROJECTED", "value": 140, "display": "$140M"}, {"label": "2012–13 ACTUAL", "value": 0, "display": "$0"}], src=SRC_MEMO),
   show="Theranos had zero revenue in 2012 and 2013. Yet investors were given projections of $140 million in revenue for 2014, and nearly $1 billion for 2015."),
 L("Behind the projections, the appeals court noted, Balwani told Holmes in November two thousand thirteen that Theranos was down to fifteen million dollars in cash, and spending up to two million dollars a week. In two thousand fifteen, it reported less than two million dollars in total income to the IRS.",
   dict(type="big", kicker="NOVEMBER 2013 · PER THE NINTH CIRCUIT", lines=["$15 million in cash.", "Spending up to|$2 million a week."], src=SRC_CA9),
   show="Behind the projections, the appeals court noted, Balwani told Holmes in November 2013 that Theranos was down to $15 million in cash, and spending up to $2 million a week. In 2015, it reported less than $2 million in total income to the IRS."),
 L("Investors were also told the device was being used on medevac helicopters and on the battlefield. According to the government, the Defense Department never used it to treat patients.",
   dict(type="doc", img="img/memo_rev.jpg", pan=[0.42, 0.5], hl=[0.0, 0.80, 1.0, 0.16], kicker="THE MILITARY CLAIM", title="“never used Theranos' device to clinically treat patients”", src=SRC_MEMO)),
 L("At technology demonstrations, the court wrote, VIP guests were led to believe the device was running a sample of their blood. In reality, it was running a null protocol, while some samples were secretly run on other companies' machines.",
   dict(type="quote", q="In reality, the device was running a “null protocol” while some of the VIP samples were surreptitiously run on third-party devices.", case=CASE, doc="NINTH CIRCUIT · ON THE DEMOS", cite="9th Cir. opinion, No. 22-10312", size=42)),
 L("Then there were the reports. In April two thousand ten, prosecutors said, Holmes emailed Walgreens executives reports with favorable conclusions about Theranos, bearing the logos of Pfizer, GlaxoSmithKline and Schering-Plough.",
   dict(type="doc", img="img/memo_logos.jpg", pan=[0.2, 0.3], hl=[0.0, 0.37, 1.0, 0.39], kicker="APRIL 2010", title="The logos", src=SRC_MEMO),
   show="Then there were the reports. In April 2010, prosecutors said, Holmes emailed Walgreens executives reports with favorable conclusions about Theranos, bearing the logos of Pfizer, GlaxoSmithKline and Schering-Plough."),
 L("At trial, Holmes admitted that she personally put those logos on the reports. Witnesses from the drug companies testified that they had not validated the technology, and had not authorized the use of their logos.",
   dict(type="big", kicker="AT TRIAL · PER THE NINTH CIRCUIT", lines=["She added the logos.", "The companies never|authorized them."], src=SRC_CA9)),
 # III
 L("Chapter three. The unraveling.", dict(type="chapter", n="III", title="The Unraveling")),
 L("Inside the company, prosecutors said, scientists warned Holmes in two thousand thirteen that the device could not reliably test patient samples. Some resigned shortly before the Walgreens launch.",
   dict(type="doc", img="img/memo_rev.jpg", pan=[0.15, 0.25], hl=[0.0, 0.31, 1.0, 0.33], kicker="2013 · PER PROSECUTORS", title="The warnings", src=SRC_MEMO),
   show="Inside the company, prosecutors said, scientists warned Holmes in 2013 that the device could not reliably test patient samples. Some resigned shortly before the Walgreens launch."),
 L("One scientist testified about Holmes's response: she has a promise to deliver to the customer.",
   dict(type="quote", q="she has a promise to deliver to the customer, she doesn't have much of a choice but to go ahead with the launch.", case=CASE, doc="TRIAL TESTIMONY", cite=MEMOQ, size=44)),
 L("In September two thousand fifteen, Balwani texted Holmes: Our validation reports are terrible. Her reply: Praying.",
   dict(type="doc", img="img/memo_texts.jpg", pan=[0.3, 0.4], hl=[0.0, 0.72, 1.0, 0.27], kicker="SEPT 22, 2015 · TEXT MESSAGES", title="“Our validation reports are terrible.”", src=SRC_MEMO),
   show="In September 2015, Balwani texted Holmes: \"Our validation reports are terrible.\" Her reply: \"Praying.\""),
 L("In late two thousand fifteen, news reporting revealed internal struggles inside the Theranos laboratory.",
   dict(type="big", kicker="LATE 2015", lines=["The reporting", "begins."], src=SRC_CA9),
   show="In late 2015, news reporting revealed internal struggles inside the Theranos laboratory."),
 L("According to prosecutors, when Holmes learned that a Wall Street Journal reporter was working on the story, she hired the lawyer David Boies to try to get him to drop it. Then she appealed to the newspaper's owner, who was also a significant Theranos investor.",
   dict(type="doc", img="img/memo_wsj.jpg", pan=[0.2, 0.3], hl=[0.0, 0.655, 1.0, 0.2], kicker="2015 · PER PROSECUTORS", title="Pressure on the story", src=SRC_MEMO)),
 L("Asked on television about it, Holmes said that every test that we offer in our laboratory can run on our proprietary devices. Prosecutors said that was false.",
   dict(type="quote", q="every test that we offer in our laboratory can run on our proprietary devices.", case=CASE, doc="OCT 15, 2015 · ON MAD MONEY", cite=MEMOQ, size=48)),
 L("Federal regulators inspected the lab. Faced with their findings, Theranos itself admitted a global and long-term failure of the quality control program for its device.",
   dict(type="doc", img="img/memo_cms.jpg", pan=[0.42, 0.5], hl=[0.0, 0.78, 1.0, 0.2], kicker="2015 · CMS INSPECTION", title="“a global and long-term failure”", src=SRC_MEMO)),
 L("Theranos voided every patient test result ever run on that device in its clinical lab.",
   dict(type="big", kicker="PER PROSECUTORS", lines=["Every Edison result:", "voided."], src=SRC_MEMO)),
 L("March fourteenth, two thousand eighteen. The Securities and Exchange Commission charged Theranos, Holmes and Balwani with what it called a massive fraud that raised more than seven hundred million dollars from investors.",
   dict(type="stat", kicker="MARCH 14, 2018 · SEC", value="$700M+", label="raised from investors,|according to the SEC", src=SRC_SEC),
   show="March 14, 2018. The Securities and Exchange Commission charged Theranos, Holmes and Balwani with what it called a \"massive fraud\" that raised more than $700 million from investors."),
 L("Holmes settled. She agreed to a five hundred thousand dollar penalty, a ten-year bar from serving as an officer or director of a public company, and to give up voting control of Theranos.",
   dict(type="list", kicker="HOLMES'S SEC SETTLEMENT", items=[["$500K", "Penalty"], ["10 YRS", "Barred as public-company officer or director"], ["18.9M", "Shares returned"], ["—", "Voting control given up"]], size=40, src=SRC_SEC),
   show="Holmes settled. She agreed to a $500,000 penalty, a ten-year bar from serving as an officer or director of a public company, and to give up voting control of Theranos."),
 L("Investors are entitled to nothing less than complete truth and candor, said the SEC's enforcement co-director.",
   dict(type="quote", q="Investors are entitled to nothing less than complete truth and candor from companies and their executives", case="SEC v. HOLMES", doc="SEC ENFORCEMENT · STEVEN PEIKIN", cite=SRC_SEC, size=46)),
 L("Three months later, on June fourteenth, a federal grand jury in California indicted Holmes and Balwani for wire fraud.",
   dict(type="doc", img="img/indictment.jpg", pan=[0.0, 0.1], hl=[0.0, 0.55, 1.0, 0.45], kicker="JUNE 14, 2018 · INDICTMENT", title="The United States of America v. Holmes & Balwani", src=SRC_IND),
   show="Three months later, on June 14, a federal grand jury in California indicted Holmes and Balwani for wire fraud."),
 # IV
 L("Chapter four. The trial.", dict(type="chapter", n="IV", title="The Trial")),
 L("The final indictment charged two conspiracies, one against investors and one against patients, and ten counts of wire fraud. The court tried Holmes and Balwani separately.",
   dict(type="doc", img="img/tsi_cover.jpg", pan=[0.0, 0.1], hl=[0.0, 0.755, 1.0, 0.075], kicker="JULY 28, 2020", title="Third Superseding Indictment", src=SRC_TSI + " · " + SRC_MEMO)),
 L("Holmes's trial began on August thirty-first, two thousand twenty-one. It lasted four months. Thirty-two witnesses testified, and more than nine hundred exhibits were admitted.",
   dict(type="doc", img="img/memo_trial.jpg", pan=[0.2, 0.3], hl=[0.0, 0.60, 1.0, 0.38], kicker="AUG 31, 2021 – JAN 3, 2022", title="Four months · 32 witnesses · 900+ exhibits", src=SRC_MEMO),
   show="Holmes's trial began on August 31, 2021. It lasted four months. 32 witnesses testified, and more than 900 exhibits were admitted."),
 L("At trial, prosecutors said, she blamed her chief operating officer, her board, her scientists, her business partners, her investors, the media. Everyone, that is, but herself.",
   dict(type="quote", q="At trial, she blamed her COO (and longtime boyfriend), her board, her scientists, her business partners, her investors, her marketing firm, her attorneys, the media—everyone, that is, but herself.", case=CASE, doc="THE GOVERNMENT'S VIEW", cite="Gov't sentencing memorandum, Nov 11, 2022", size=36)),
 L("The verdict: guilty of conspiracy to defraud investors, and of three counts of wire fraud. The wires behind those counts: thirty-eight million dollars in February two thousand fourteen, and nearly one hundred million and six million dollars on October thirty-first, two thousand fourteen.",
   dict(type="doc", img="img/tsi_counts.jpg", pan=[0.45, 0.55], hl=[0.0, 0.76, 1.0, 0.205], kicker="COUNTS SIX, SEVEN, EIGHT", title="$38,336,632 · $99,999,984 · $5,999,997", src=SRC_TSI),
   show="The verdict: guilty of conspiracy to defraud investors, and of three counts of wire fraud. The wires behind those counts: $38 million in February 2014, and nearly $100 million and $6 million on October 31, 2014."),
 L("Not guilty on four counts: the conspiracy against patients, and three related wire fraud counts. The court declared a mistrial on the three counts where the jury deadlocked. Prosecutors later dismissed them.",
   dict(type="doc", img="img/judgment.jpg", pan=[0.35, 0.45], hl=[0.0, 0.88, 1.0, 0.08], kicker="THE JUDGMENT", title="Not guilty · dismissed", src=SRC_JUDG + " · Minute order, Dkt. 1236")),
 L("The FBI's special agent in charge put it simply. Elizabeth Holmes chose fraud over business failure.",
   dict(type="quote", q="Elizabeth Holmes chose fraud over business failure.", case=CASE, doc="FBI · SPECIAL AGENT IN CHARGE CRAIG FAIR", cite=SRC_DOJV, size=56)),
 L("Months later, in a separate trial, another jury convicted Balwani on all twelve counts.",
   dict(type="big", kicker="JULY 2022 · RAMESH “SUNNY” BALWANI", lines=["Separate trial.", "Guilty on all 12."], src=SRC_MEMO),
   show="Months later, in a separate trial, another jury convicted Balwani on all 12 counts."),
 # V
 L("Chapter five. The sentence.", dict(type="chapter", n="V", title="The Sentence")),
 L("November eighteenth, two thousand twenty-two. Prosecutors asked for fifteen years. The probation office recommended nine. Her lawyers argued for eighteen months or less, and suggested home confinement.",
   dict(type="bars", kicker="WHAT EACH SIDE ASKED FOR", title="Months in prison", items=[{"label": "PROSECUTORS", "value": 180, "display": "180 mos"}, {"label": "PROBATION", "value": 108, "display": "108 mos"}, {"label": "DEFENSE", "value": 18, "display": "≤18 mos"}], src=SRC_MEMO + " · Defense memorandum, Dkt. 1642"),
   show="November 18, 2022. Prosecutors asked for 15 years. The probation office recommended nine. Her lawyers argued for 18 months or less, and suggested home confinement."),
 L("The probation office had put investor losses at more than seven hundred thirty million dollars. The judge found that too high. Theranos stock, he reasoned, was not practically worthless, and kept some value apart from the fraud.",
   dict(type="big", kicker="THE LOSS QUESTION", lines=["Probation: $730 million.", "The judge: lower."], src=SRC_SO),
   show="The probation office had put investor losses at more than $730 million. The judge found that too high. Theranos stock, he reasoned, was not \"practically worthless,\" and kept some value apart from the fraud."),
 L("Judge Edward Davila estimated the loss caused by her crimes at one hundred twenty million dollars. That put the guidelines range at one hundred thirty-five to one hundred sixty-eight months.",
   dict(type="stat", kicker="LOSS FOUND BY THE COURT", value="$120,146,247", label="guidelines range:|135–168 months", src=SRC_SO + " · " + SRC_RS),
   show="Judge Edward Davila estimated the loss caused by her crimes at $120 million. That put the guidelines range at 135 to 168 months."),
 L("At the hearing, the judge wrote, Holmes apologized for Theranos and its failings. But she did not accept responsibility for her own conduct.",
   dict(type="quote", q="Ms. Holmes apologized more generally for Theranos and its “failings,” but did not acknowledge nor accept responsibility for her conduct …", case=CASE, doc="JUDGE EDWARD J. DAVILA", cite=SRC_SO, size=42)),
 L("The sentence: one hundred thirty-five months. Eleven years and three months in federal prison, the low end of the range.",
   dict(type="verdict", kicker="THE SENTENCE · NOVEMBER 18, 2022", stamp="SENTENCED", big="135 months", sub="11 years, 3 months · then 3 years of supervised release"),
   show="The sentence: 135 months. 11 years and 3 months in federal prison, the low end of the range."),
 L("In May two thousand twenty-three, the judge ordered Holmes and Balwani to pay four hundred fifty-two million dollars in restitution to fourteen victims, including Walgreens and Safeway.",
   dict(type="doc", img="img/restitution.jpg", pan=[0.3, 0.4], hl=[0.0, 0.64, 1.0, 0.06], kicker="MAY 16, 2023 · RESTITUTION", title="$452,047,268", src=SRC_REST + " · " + SRC_CA9),
   show="In May 2023, the judge ordered Holmes and Balwani to pay $452 million in restitution to 14 victims, including Walgreens and Safeway."),
 L("He refused to let her stay free during her appeal. On May thirtieth, two thousand twenty-three, she reported to prison. Balwani, sentenced separately, got twelve years and eleven months.",
   dict(type="doc", img="img/bail.jpg", pan=[0.45, 0.55], hl=[0.0, 0.86, 1.0, 0.06], kicker="APRIL 10, 2023", title="Release pending appeal: denied", src=SRC_BAIL + " · " + SRC_DOJC),
   show="He refused to let her stay free during her appeal. On May 30, 2023, she reported to prison. Balwani, sentenced separately, got 12 years and 11 months."),
 # VI
 L("Chapter six. After the verdict.", dict(type="chapter", n="VI", title="After the Verdict")),
 L("In February two thousand twenty-five, the Ninth Circuit Court of Appeals affirmed her convictions, her sentence and the restitution order.",
   dict(type="doc", img="img/ca9.jpg", pan=[0.3, 0.4], hl=[0.0, 0.57, 1.0, 0.28], kicker="FEBRUARY 24, 2025 · AFFIRMED", title="“nothing more than a mirage”", src=SRC_CA9),
   show="In February 2025, the Ninth Circuit Court of Appeals affirmed her convictions, her sentence and the restitution order."),
 L("The vision Holmes and Balwani sold, the judges wrote, was nothing more than a mirage. The grandiose achievements they touted were half-truths and outright lies.",
   dict(type="quote", q="The grandiose achievements touted by Holmes and Balwani were half-truths and outright lies.", case=CASE, doc="NINTH CIRCUIT OPINION", cite="U.S. v. Holmes, No. 22-10312 (9th Cir.)", size=48)),
 L("In March two thousand twenty-six, a change in the sentencing guidelines for first-time offenders opened a door. Judge Davila cut her sentence from one hundred thirty-five months to one hundred twenty-three.",
   dict(type="doc", img="img/resent.jpg", pan=[0.2, 0.3], hl=[0.0, 0.44, 1.0, 0.24], kicker="MARCH 26, 2026 · SENTENCE REDUCED", title="135 → 123 months", src=SRC_RS),
   show="In March 2026, a change in the sentencing guidelines for first-time offenders opened a door. Judge Davila cut her sentence from 135 months to 123."),
 L("To be clear, he wrote, this sentence reduction does not diminish the enormity of Holmes's crimes.",
   dict(type="quote", q="To be clear, this sentence reduction does not diminish the enormity of Holmes’s crimes …", case=CASE, doc="JUDGE EDWARD J. DAVILA", cite=SRC_RS, size=48)),
 L("She has asked President Trump to commute her sentence. According to Forbes, as of late September, the Justice Department listed that request as pending.",
   dict(type="big", kicker="CLEMENCY · ACCORDING TO NEWS REPORTS", lines=["Commutation requested.", "Pending as of|Sept. 2026."], src=SRC_FORBES)),
 L("According to the same report, she has been approved for a halfway house in August two thousand twenty-seven, with her release scheduled for February two thousand thirty.",
   dict(type="timeline", kicker="ACCORDING TO NEWS REPORTS", events=[{"date": "MAY 2023", "text": "Reports to prison"}, {"date": "AUG 2027", "text": "Halfway house approved"}, {"date": "FEB 2030", "text": "Scheduled release"}], at=1, src=SRC_FORBES),
   show="According to the same report, she has been approved for a halfway house in August 2027, with her release scheduled for February 2030."),
 L("One tiny drop changes everything, the company promised.",
   dict(type="big", lines=["“One tiny drop", "changes everything.”"])),
 L("A jury, a judge and three appellate judges decided the case on something else. Not what the device could do, but what investors were told it could do.",
   dict(type="big", lines=["Not what it could do.", "What investors|were told."])),
 L("This is SWORN. Real trials. Real evidence. The verdict.", dict(type="end")),
]
from panfix import fix
fix(lines, "long")
spec = {"label": "SWORN · CASE 003", "lines": lines}
json.dump(spec, open("episode.json", "w"), indent=1, ensure_ascii=False)
print(len(lines), "lines,", sum(len(l["say"].split()) for l in lines), "words")
