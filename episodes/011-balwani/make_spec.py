import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
def hl(name, i=0):
    a, b = HL[name][i]
    return [0.0, a, 1.0, round(b - a, 4)]
CASE = "UNITED STATES v. BALWANI"
SEC = "SEC v. BALWANI"
SRC_CA9 = "U.S. v. Holmes; U.S. v. Balwani, Order and Amended Opinion (9th Cir., Dec 22, 2025)"
SRC_TSI = "Third Superseding Indictment, U.S. v. Holmes & Balwani, No. 18-cr-258 (N.D. Cal., Jul 28, 2020)"
SRC_IND = "Indictment, U.S. v. Holmes & Balwani, No. 18-cr-258 (N.D. Cal., Jun 14, 2018)"
SRC_MEMO = "U.S. Sentencing Memorandum (re Holmes), No. 18-cr-258 (N.D. Cal., Nov 11, 2022)"
SRC_FIX = "U.S. Administrative Motion to Correct Judgments, No. 18-cr-258 (N.D. Cal.), ECF No. 1811"
SRC_SEC = "Complaint, SEC v. Ramesh \"Sunny\" Balwani, No. 18-cv-1603 (N.D. Cal., Mar 14, 2018) — allegations"
SRC_DOJ = "U.S. Attorney's Office, N.D. Cal., press release (Dec 7, 2022)"
SRC_AP = "Associated Press (Dec 7, 2022)"
SRC_ORD = "Order Granting Motion for Modification of Sentence, U.S. v. Holmes (N.D. Cal., Mar 26, 2026)"
SRC_SCOTUS = "Supreme Court of the United States, docket No. 25-1330, Balwani v. United States"
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
def doc(img, kicker, title, src, i=0, pan=None):
    return dict(type="doc", img=f"img/{img}.jpg", pan=pan or [0.0, 0.1], hl=hl(img, i), kicker=kicker, title=title, src=src)
lines = [
 # COLD OPEN
 L("Why did Sunny Balwani get more prison time than Elizabeth Holmes? Same company. Same fraud. Same judge. Even the same sentencing range.",
   dict(type="big", kicker="THERANOS · TWO DEFENDANTS", lines=["Same judge.", "Same|range."], src=SRC_CA9)),
 L("Holmes got one hundred thirty-five months. Balwani, the president and chief operating officer of Theranos, got one hundred fifty-five.",
   dict(type="bars", kicker="THE SENTENCES · 2022", title="Same range: 135 to 168 months", items=[{"label": "Elizabeth Holmes", "value": 135, "display": "135 months"}, {"label": "Sunny Balwani", "value": 155, "display": "155 months"}], src=SRC_CA9),
   show="Holmes got 135 months. Balwani, the president and chief operating officer of Theranos, got 155."),
 L("Her jury acquitted her of defrauding patients. His jury convicted him on every count: investors and patients. All twelve.",
   doc("ca9_all", "U.S. COURT OF APPEALS · NINTH CIRCUIT", "“convicted Balwani of all counts”", SRC_CA9, 0)),
 L("And on October fifth, twenty twenty-six, the Supreme Court declined to hear his case. This is the other Theranos verdict.",
   dict(type="title", kicker="SWORN · CASE 011 · THE VERDICT", title="The Other|Theranos Verdict", sub="United States v. Ramesh \"Sunny\" Balwani · San Jose · 2022"),
   show="And on October 5, 2026, the Supreme Court declined to hear his case. This is the other Theranos verdict."),
 # I
 L("Chapter one. The partner.", dict(type="chapter", n="I", title="The Partner")),
 L("The Ninth Circuit's opinion begins with a slogan. One tiny drop changes everything. That, the judges wrote, was the vision shared by Elizabeth Holmes and Ramesh Balwani, known as Sunny.",
   doc("ca9_drop", "NINTH CIRCUIT · OPINION · PAGE 8", "“[O]ne tiny drop changes everything.”", SRC_CA9, 0),
   show="The Ninth Circuit's opinion begins with a slogan: \"One tiny drop changes everything.\" That, the judges wrote, was the vision shared by Elizabeth Holmes and Ramesh Balwani, known as Sunny."),
 L("Holmes founded Theranos in two thousand three. The promise: fast, accurate, cheap blood tests from a drop of blood drawn from a fingertip.",
   doc("ca9_drop", "NINTH CIRCUIT · OPINION", "“nothing more than a mirage”", SRC_CA9, 1),
   show="Holmes founded Theranos in 2003. The promise: fast, accurate, cheap blood tests from a drop of blood drawn from a fingertip."),
 L("In two thousand nine, according to the Securities and Exchange Commission, Theranos was on the verge of running out of money. Holmes turned to Balwani, her boyfriend at the time, who guaranteed a line of credit for the company. He joined that same year, and became its president and chief operating officer.",
   doc("sec_2009", "SEC COMPLAINT · MARCH 2018 · AS ALLEGED", "“on the verge of running out of money”", SRC_SEC, 0),
   show="In 2009, according to the Securities and Exchange Commission, Theranos was on the verge of running out of money. Holmes turned to Balwani, her boyfriend at the time, who guaranteed a line of credit for the company. He joined that same year, and became its president and chief operating officer."),
 L("The appeals court wrote that the two were in a relationship from two thousand four to two thousand sixteen. And that evidence at both trials showed Balwani oversaw operations in the company's patient-testing lab, and was the main contact for its retail partners, Safeway and Walgreens.",
   doc("ca9_role", "NINTH CIRCUIT · FACTUAL BACKGROUND", "“Balwani oversaw operations”", SRC_CA9, 1),
   show="The appeals court wrote that the two were in a relationship from 2004 to 2016. And that evidence at both trials showed Balwani oversaw operations in the company's patient-testing lab, and was the main contact for its retail partners, Safeway and Walgreens."),
 L("Prosecutors said he owned nearly thirty million Theranos shares, more than six percent of the company.",
   dict(type="stat", kicker="RAMESH \"SUNNY\" BALWANI · 2009–2016", value="~30M", label="Theranos shares · more than 6%", src=SRC_DOJ),
   show="Prosecutors said he owned nearly 30 million Theranos shares, more than 6% of the company."),
 # II
 L("Chapter two. The model.", dict(type="chapter", n="II", title="The Model")),
 L("Theranos needed money. The appeals court noted testimony that the company had no revenue at all in twenty twelve and twenty thirteen, and lost fifty-seven million, then ninety-two million dollars.",
   doc("ca9_null", "NINTH CIRCUIT · FACTUAL BACKGROUND", "$57 million and $92 million in losses", SRC_CA9, 1),
   show="Theranos needed money. The appeals court noted testimony that the company had no revenue at all in 2012 and 2013, and lost $57 million, then $92 million."),
 L("In November twenty thirteen, Balwani told Holmes the company was down to fifteen million dollars in cash, while spending up to two million a week.",
   doc("ca9_null", "NINTH CIRCUIT · FACTUAL BACKGROUND", "“down to $15 million in cash”", SRC_CA9, 1),
   show="In November 2013, Balwani told Holmes the company was down to $15 million in cash, while spending up to $2 million a week."),
 L("From late twenty thirteen to twenty fifteen, the S.E.C. said, Theranos raised more than seven hundred million dollars from investors. Investors typically got a binder. And the SEC alleged that Balwani drafted the financial information inside it.",
   doc("sec_proj", "SEC COMPLAINT · AS ALLEGED", "“Balwani drafted the financial information”", SRC_SEC, 0),
   show="From late 2013 to 2015, the SEC said, Theranos raised more than $700 million from investors. Investors typically got a binder. And the SEC alleged that Balwani drafted the financial information inside it."),
 L("Those projections, the complaint says, showed more than one hundred million dollars in revenue for twenty fourteen, and about one billion dollars for twenty fifteen.",
   dict(type="bars", kicker="THERANOS · 2014 · AS ALLEGED BY THE SEC", title="Projected vs. recorded revenue", items=[{"label": "Projected to investors", "value": 100, "display": "$100M+"}, {"label": "Recorded", "value": 0.1, "display": "~$100,000"}], src=SRC_SEC),
   show="Those projections, the complaint says, showed more than $100 million in revenue for 2014, and about $1 billion for 2015."),
 L("The S.E.C. alleged that Theranos actually recorded little more than one hundred thousand dollars in revenue in twenty fourteen. And in October of that year, the same month he gave investors year-end figures of one hundred twenty to one hundred forty million, Balwani told potential insurers the company was losing eight to nine million dollars a month.",
   doc("sec_real", "SEC COMPLAINT · AS ALLEGED", "“little more than $100,000”", SRC_SEC, 0),
   show="The SEC alleged that Theranos actually recorded little more than $100,000 in revenue in 2014. And in October of that year, the same month he gave investors year-end figures of $120 to $140 million, Balwani told potential insurers the company was losing $8 to $9 million a month."),
 L("Questioned by the S.E.C., Balwani drew a line. He said he was responsible for the financial model. Not, the appeals court noted, for the financial projections.",
   doc("ca9_model", "NINTH CIRCUIT · OPINION · PAGE 40", "“financial model” vs. “financial projections”", SRC_CA9, 0),
   show="Questioned by the SEC, Balwani drew a line. He said he was responsible for the \"financial model.\" Not, the appeals court noted, for the \"financial projections.\""),
 L("At his sentencing, Judge Edward Davila addressed exactly that, the Associated Press reported. The projections, he said:",
   dict(type="big", kicker="DECEMBER 7, 2022 · SAN JOSE", lines=["The", "projections."], src=SRC_AP)),
 L("They weren't just projections. They were lies.",
   dict(type="quote", q="weren't just projections, they were lies.", case=CASE, doc="U.S. DISTRICT JUDGE EDWARD J. DAVILA · AT SENTENCING", cite="As quoted by " + SRC_AP, size=60),
   show="\"…weren't just projections, they were lies.\""),
 # III
 L("Chapter three. The pitch.", dict(type="chapter", n="III", title="The Pitch")),
 L("Investors were told Theranos ran its tests on its own machines. The S.E.C. alleged that in its clinical lab, the proprietary analyzer ran only about twelve of the more than two hundred tests on the menu. The rest ran on commercial analyzers bought from other companies, some modified for fingerstick samples.",
   doc("sec_cover", "SEC v. RAMESH \"SUNNY\" BALWANI · 2018", "The SEC's case", SRC_SEC, 1),
   show="Investors were told Theranos ran its tests on its own machines. The SEC alleged that in its clinical lab, the proprietary analyzer ran only about 12 of the more than 200 tests on the menu. The rest ran on commercial analyzers bought from other companies, some modified for fingerstick samples."),
 L("Visiting investors were shown the device. The court described what happened next: the machine was running a null protocol, while some of the visitors' samples were secretly run on third-party devices.",
   doc("ca9_null", "NINTH CIRCUIT · FACTUAL BACKGROUND", "“a ‘null protocol’”", SRC_CA9, 0),
   show="Visiting investors were shown the device. The court described what happened next: the machine was running a \"null protocol,\" while some of the visitors' samples were secretly run on third-party devices."),
 L("Investors also saw reports bearing the logos of drug companies like Pfizer. Holmes admitted she put those logos there herself. The companies testified they never independently validated the technology, and never authorized the use of their logos.",
   doc("ca9_drop", "NINTH CIRCUIT · OPINION", "“half-truths and outright lies”", SRC_CA9, 1)),
 L("Then the military. The S.E.C. alleged that Balwani told one potential investor in late twenty thirteen that seventy-five percent of Theranos's current revenue came from the military.",
   doc("sec_dod", "SEC COMPLAINT · AS ALLEGED", "“75 percent”", SRC_SEC, 0),
   show="Then the military. The SEC alleged that Balwani told one potential investor in late 2013 that 75% of Theranos's current revenue came from the military."),
 L("According to the complaint, Theranos made only about three hundred thousand dollars from three Defense Department contracts. At Holmes's trial, General James Mattis testified that the device was never put into the field, never installed on a military medevac, and never used to treat service members on the battlefield.",
   doc("sec_dod", "SEC COMPLAINT · AS ALLEGED", "“approximately $300,000”", SRC_SEC, 1),
   show="According to the complaint, Theranos made only about $300,000 from three Defense Department contracts. At Holmes's trial, General James Mattis testified that the device was never put into the field, never installed on a military medevac, and never used to treat service members on the battlefield."),
 L("And Walgreens? Balwani was the company's main contact there. A Walgreens representative testified that while Holmes and Balwani were telling investors the partnership was expanding, it was actually contracting.",
   dict(type="big", kicker="WALGREENS · AS TESTIFIED", lines=["Expanding?", "Contracting."], src=SRC_CA9)),
 # IV
 L("Chapter four. The lab.", dict(type="chapter", n="IV", title="The Lab")),
 L("Here is what set Balwani's case apart. He ran the operations of the lab. And the warnings went to him.",
   doc("ca9_role", "NINTH CIRCUIT · FACTUAL BACKGROUND", "the patient-testing lab", SRC_CA9, 1)),
 L("According to the government's sentencing memo, in late May twenty fourteen, lab director Dr. Adam Rosendorff halted all testing of h.C.G., a pregnancy hormone, on the Theranos analyzer because of inaccurate results. Balwani immediately passed that news to Holmes.",
   doc("memo_lab", "U.S. SENTENCING MEMORANDUM · 2022", "hCG testing halted", SRC_MEMO, 0),
   show="According to the government's sentencing memo, in late May 2014, lab director Dr. Adam Rosendorff halted all testing of hCG, a pregnancy hormone, on the Theranos analyzer because of inaccurate results. Balwani immediately passed that news to Holmes."),
 L("In August, Rosendorff emailed Balwani that the bicarbonate test had lost all diagnostic value. Balwani forwarded it to Holmes. When a scientist proposed a study of another test's low readings, Balwani wrote to Holmes:",
   doc("memo_lab", "U.S. SENTENCING MEMORANDUM · 2022", "“lost all diagnostic value”", SRC_MEMO, 1),
   show="In August, Rosendorff emailed Balwani that the bicarbonate test had \"lost all diagnostic value.\" Balwani forwarded it to Holmes. When a scientist proposed a study of another test's low readings, Balwani wrote to Holmes:"),
 L("Always another study after the fact.",
   dict(type="quote", q="Always another study after the fact.", case=CASE, doc="SUNNY BALWANI · EMAIL TO HOLMES · 2014", cite="As quoted in " + SRC_MEMO, size=64)),
 L("By late November twenty fourteen, the memo says, he texted Holmes that the lab where Theranos ran its own devices was a disaster zone.",
   doc("memo_zone", "U.S. SENTENCING MEMORANDUM · 2022", "“disaster zone”", SRC_MEMO, 1),
   show="By late November 2014, the memo says, he texted Holmes that the lab where Theranos ran its own devices was a \"disaster zone.\""),
 L("A lab associate, Erika Cheung, testified about the quality-control checks: something still going on that is causing one out of four failures of every single test.",
   doc("ca9_cheung", "NINTH CIRCUIT · ERIKA CHEUNG'S TESTIMONY", "“one out of four failures”", SRC_CA9, 0),
   show="A lab associate, Erika Cheung, testified about the quality-control checks: \"something still going on that is causing one out of four failures of every single test.\""),
 L("The indictment lists the tests Theranos could not consistently get right, from cholesterol and glucose to H.I.V., P.S.A. and h.C.G.",
   doc("tsi_tests", "THIRD SUPERSEDING INDICTMENT · ¶16", "The tests", SRC_TSI, 0),
   show="The indictment lists the tests Theranos could not consistently get right, from cholesterol and glucose to HIV, PSA and hCG."),
 L("The patients were real. One testified that a Theranos HIV test came back positive. Two later tests showed she was negative. Another received incorrect results on a pregnancy test. The court wrote that the evidence linked Balwani to the transmission of those results, and to buying advertisements for Theranos Wellness Centers in Arizona.",
   doc("ca9_pat", "NINTH CIRCUIT · SCHEME TO DEFRAUD PATIENTS", "“The evidence linked Balwani”", SRC_CA9, 1)),
 L("Count twelve of the indictment is one of those ad buys: on August third, twenty fifteen, one million, one hundred twenty-six thousand, six hundred sixty-one dollars wired to buy advertising for Theranos Wellness Centers.",
   doc("tsi_c12", "THIRD SUPERSEDING INDICTMENT · COUNT 12", "$1,126,661 for advertisements", SRC_TSI, 1),
   show="Count 12 of the indictment is one of those ad buys: on August 3, 2015, $1,126,661 wired to buy advertising for Theranos Wellness Centers."),
 L("After federal inspectors from C.M.S. found problems in the lab, Theranos voided every Edison test result.",
   doc("memo_zone", "U.S. SENTENCING MEMORANDUM · 2022", "“void every single Edison test”", SRC_MEMO, 2),
   show="After federal inspectors from CMS found problems in the lab, Theranos voided every Edison test result."),
 # V
 L("Chapter five. Twelve counts.", dict(type="chapter", n="V", title="Twelve Counts")),
 L("The grand jury indicted them both in June twenty eighteen. The final indictment charged two conspiracies, one against investors and one against patients, and ten counts of wire fraud.",
   doc("ind_cover", "U.S. DISTRICT COURT · N.D. CAL. · JUNE 2018", "The indictment", SRC_IND, 0),
   show="The grand jury indicted them both in June 2018. The final indictment charged two conspiracies, one against investors and one against patients, and ten counts of wire fraud."),
 L("The case was investigated by the F.B.I., the U.S. Postal Inspection Service, and the Food and Drug Administration's Office of Criminal Investigations.",
   doc("ind_cover", "U.S. DISTRICT COURT · N.D. CAL.", "United States v. Holmes & Balwani", SRC_IND + " · " + SRC_DOJ, 0),
   show="The case was investigated by the FBI, the U.S. Postal Inspection Service, and the Food and Drug Administration's Office of Criminal Investigations."),
 L("The court ordered separate trials. Holmes went first. On January third, twenty twenty-two, her jury convicted her on four investor counts, acquitted her of the patient charges, and could not agree on three others.",
   doc("ca9_all", "NINTH CIRCUIT · PROCEDURAL HISTORY", "Holmes: guilty on 4", SRC_CA9, 0, pan=[0.0, 0.05]),
   show="The court ordered separate trials. Holmes went first. On January 3, 2022, her jury convicted her on four investor counts, acquitted her of the patient charges, and could not agree on three others."),
 L("Balwani's trial began in March twenty twenty-two, on the same twelve counts. It lasted nearly four months. He did not testify.",
   dict(type="timeline", kicker="TWO TRIALS · ONE COURTROOM", events=[{"date": "2018", "text": "Indicted together"}, {"date": "Jan 2022", "text": "Holmes verdict"}, {"date": "Mar 2022", "text": "Balwani trial begins"}, {"date": "Jul 2022", "text": "Balwani verdict"}], at=2, src=SRC_MEMO + " · " + SRC_CA9 + " · " + SRC_AP),
   show="Balwani's trial began in March 2022, on the same twelve counts. It lasted nearly four months. He did not testify."),
 L("On July seventh, twenty twenty-two, the jury found him guilty of all counts alleged in the indictment.",
   doc("fix_dates", "U.S. ATTORNEY'S OFFICE · COURT FILING", "“guilty of all counts”", SRC_FIX, 0),
   show="On July 7, 2022, the jury found him guilty of all counts alleged in the indictment."),
 L("Seven counts involved investors. Five involved patients, the kind of charges Holmes's jury had rejected.",
   dict(type="verdict", kicker="JULY 7, 2022 · SAN JOSE", stamp="GUILTY", big="12 of 12 counts", sub="Ramesh \"Sunny\" Balwani · investors and patients")),
 # VI
 L("Chapter six. A hundred fifty-five months.", dict(type="chapter", n="VI", title="155 Months")),
 L("December seventh, twenty twenty-two. Prosecutors asked for fifteen years. His lawyers asked for four to ten months, and argued, the A.P. reported, that he never sought fame, and is not Ms. Holmes. Balwani declined the judge's invitation to speak.",
   dict(type="bars", kicker="SENTENCING · DECEMBER 7, 2022", title="What each side asked for", items=[{"label": "Prosecutors", "value": 180, "display": "15 years"}, {"label": "Defense", "value": 10, "display": "4–10 months"}], src=SRC_AP),
   show="December 7, 2022. Prosecutors asked for 15 years. His lawyers asked for four to ten months, and argued, the AP reported, that he never sought fame, and \"is not Ms. Holmes.\" Balwani declined the judge's invitation to speak."),
 L("The prosecutor answered that argument directly: that he did not seek fame or recognition is not something that Mr. Balwani should get credit for.",
   dict(type="quote", q="That he did not seek fame or recognition is not something that Mr. Balwani should get credit for.", case=CASE, doc="ASSISTANT U.S. ATTORNEY JEFFREY SCHENK", cite="As quoted by " + SRC_AP, size=44),
   show="The prosecutor answered that argument directly: \"That he did not seek fame or recognition is not something that Mr. Balwani should get credit for.\""),
 L("Judge Davila found the same number of victims and the same loss as in Holmes's case, so the guideline range was the same: one hundred thirty-five to one hundred sixty-eight months. Holmes had been sentenced at the bottom of that range. Balwani got one hundred fifty-five months, and a twenty-five-thousand-dollar fine.",
   doc("ca9_155", "NINTH CIRCUIT · OPINION · PAGE 17", "“155 months of imprisonment”", SRC_CA9, 1),
   show="Judge Davila found the same number of victims and the same loss as in Holmes's case, so the guideline range was the same: 135 to 168 months. Holmes had been sentenced at the bottom of that range. Balwani got 155 months, and a $25,000 fine."),
 L("The U.S. Attorney said Balwani valued business success and personal wealth far more than patient safety.",
   dict(type="quote", q="valued business success and personal wealth far more than patient safety.", case=CASE, doc="U.S. ATTORNEY STEPHANIE M. HINDS", cite=SRC_DOJ, size=50),
   show="The U.S. Attorney said Balwani \"valued business success and personal wealth far more than patient safety.\""),
 L("In May twenty twenty-three, the court ordered restitution: four hundred fifty-two million dollars, owed jointly by Holmes and Balwani, to investors and to Safeway and Walgreens.",
   doc("ca9_155", "NINTH CIRCUIT · RESTITUTION ORDER", "$452 million", SRC_CA9, 2),
   show="In May 2023, the court ordered restitution: $452 million, owed jointly by Holmes and Balwani, to investors and to Safeway and Walgreens."),
 # VII
 L("Chapter seven. The last appeal.", dict(type="chapter", n="VII", title="The Last Appeal")),
 L("On appeal, Balwani argued that former employees had been allowed to give expert opinions without being qualified as experts, and that he had been tried on facts the indictment never charged.",
   doc("ca9_cover", "U.S. COURT OF APPEALS · NINTH CIRCUIT", "Holmes · Balwani", SRC_CA9, 0)),
 L("In February twenty twenty-five, the Ninth Circuit agreed that some of that testimony veered into expert territory, but called the error harmless. And it held the indictment plainly gave him notice. Convictions and sentences, affirmed.",
   dict(type="verdict", kicker="NINTH CIRCUIT · FEB 24, 2025", stamp="AFFIRMED", big="Conviction stands", sub="Amended Dec 22, 2025 · rehearing denied"),
   show="In February 2025, the Ninth Circuit agreed that some of that testimony \"veered into expert territory,\" but called the error harmless. And it held the indictment \"plainly gave\" him notice. Convictions and sentences, affirmed."),
 L("He asked for rehearing. In December twenty twenty-five, the court denied it. In May twenty twenty-six, he petitioned the Supreme Court. The government waived its right to respond. On October fifth, the petition was denied. Justice Thomas took no part.",
   dict(type="timeline", kicker="BALWANI v. UNITED STATES · No. 25-1330", events=[{"date": "Dec 2025", "text": "Rehearing denied"}, {"date": "May 2026", "text": "Petition filed"}, {"date": "Jun 2026", "text": "U.S. waives response"}, {"date": "Oct 5, 2026", "text": "Petition denied"}], at=3, src=SRC_SCOTUS + " · " + SRC_CA9),
   show="He asked for rehearing. In December 2025, the court denied it. In May 2026, he petitioned the Supreme Court. The government waived its right to respond. On October 5, the petition was denied. Justice Thomas took no part."),
 L("Holmes, meanwhile, won a reduction. In March twenty twenty-six, under a change to the sentencing guidelines, her sentence was cut from one hundred thirty-five months to one hundred twenty-three.",
   dict(type="stat", kicker="ELIZABETH HOLMES · MARCH 26, 2026", value="135 → 123", label="months · guidelines amendment", src=SRC_ORD),
   show="Holmes, meanwhile, won a reduction. In March 2026, under a change to the sentencing guidelines, her sentence was cut from 135 months to 123."),
 L("So why more time for Balwani? The record gives the pieces. Every count against him ended in a guilty verdict, including defrauding patients. He drafted the numbers investors saw, according to the S.E.C. He oversaw the lab the warnings came from.",
   doc("tsi_tests", "THIRD SUPERSEDING INDICTMENT", "The tests", SRC_TSI, 0),
   show="So why more time for Balwani? The record gives the pieces. Every count against him ended in a guilty verdict, including defrauding patients. He drafted the numbers investors saw, according to the SEC. He oversaw the lab the warnings came from."),
 L("One tiny drop changes everything. In San Jose, it was twelve counts.",
   dict(type="big", lines=["One tiny drop.", "Twelve|counts."]),
   show="\"One tiny drop changes everything.\" In San Jose, it was twelve counts."),
 L("This is SWORN. Real trials. Real evidence. The verdict.", dict(type="end")),
]

# --- Fact-check FIXes (factcheck.md, independent agent) ---
def setline(prefix, say=None, show=None, hlbox=None, title=None, kicker=None):
    m = [l for l in lines if l["say"].startswith(prefix)]
    assert len(m) == 1, prefix
    l = m[0]
    if say: l["say"] = say
    if show is not None:
        if show: l["show"] = show
        else: l.pop("show", None)
    if hlbox: l["scene"]["hl"] = hlbox
    if title: l["scene"]["title"] = title
    if kicker: l["scene"]["kicker"] = kicker
setline("Why did Sunny Balwani get more prison time", say="Why did Sunny Balwani get more prison time than Elizabeth Holmes? Same company. Same indictment. Same judge. Even the same sentencing range.")
setline("Holmes got one hundred thirty-five months.", say="Holmes got one hundred thirty-five months. Balwani, Theranos's former president and chief operating officer, got one hundred fifty-five.", show="Holmes got 135 months. Balwani, Theranos's former president and chief operating officer, got 155.")
setline("Theranos needed money.", hlbox=[0.0, 0.3495, 1.0, 0.0390])
setline("From late twenty thirteen", say="From late twenty thirteen to twenty fifteen, the S.E.C. said, Theranos raised more than seven hundred million dollars from investors. Investors typically got a binder, the complaint says. And the SEC alleged that Balwani drafted the financial information inside it.", show="From late 2013 to 2015, the SEC said, Theranos raised more than $700 million from investors. Investors typically got a binder, the complaint says. And the SEC alleged that Balwani drafted the financial information inside it.")
setline("The S.E.C. alleged that Theranos actually recorded", say="The S.E.C. alleged that Theranos actually recorded little more than one hundred thousand dollars in revenue in twenty fourteen. And it alleged that in October of that year, the same month he gave investors year-end revenue projections of one hundred twenty to one hundred forty million dollars, Balwani told potential insurers the company was losing eight to nine million dollars a month.", show="The SEC alleged that Theranos actually recorded little more than $100,000 in revenue in 2014. And it alleged that in October of that year, the same month he gave investors year-end revenue projections of $120 to $140 million, Balwani told potential insurers the company was losing $8 to $9 million a month.")
setline("At his sentencing, Judge Edward Davila", say="At his sentencing, Judge Edward Davila spoke about the projections Balwani drew up, the Associated Press reported. The projections, he said:")
setline("Investors were told Theranos ran", say="Investors testified they were led to believe Theranos ran its tests on its own machines. The S.E.C. alleged that in its clinical lab, the proprietary analyzer ran only about twelve of the more than two hundred tests on the menu. The rest ran on commercially available analyzers made by other companies, some modified for fingerstick samples.", show="Investors testified they were led to believe Theranos ran its tests on its own machines. The SEC alleged that in its clinical lab, the proprietary analyzer ran only about 12 of the more than 200 tests on the menu. The rest ran on commercially available analyzers made by other companies, some modified for fingerstick samples.")
setline("Here is what set Balwani's case apart.", say="Here is what set Balwani's case apart. He oversaw the operations of the lab. And the warnings went to him.")
setline("A lab associate, Erika Cheung", say="A lab associate, Erika Cheung, testified that there was something still going on that is causing one out of four failures of every single test that we do on this system.", show="A lab associate, Erika Cheung, testified there was \"something still going on that is causing one out of four failures of every single test that we do on this . . . system.\"", hlbox=[0.0, 0.8140, 1.0, 0.0560])
setline("The indictment lists the tests", say="The indictment lists tests it alleged Theranos could not consistently get right, from cholesterol and glucose to H.I.V., P.S.A. and h.C.G.", show="The indictment lists tests it alleged Theranos could not consistently get right, from cholesterol and glucose to HIV, PSA and hCG.")
setline("Count twelve of the indictment", say="Count twelve of the indictment is an ad buy: on August third, twenty fifteen, one million, one hundred twenty-six thousand, six hundred sixty-one dollars wired to buy advertising for Theranos Wellness Centers.", show="Count 12 of the indictment is an ad buy: on August 3, 2015, $1,126,661 wired to buy advertising for Theranos Wellness Centers.")
setline("The court ordered separate trials.", hlbox=[0.0, 0.0, 1.0, 0.155])
setline("Balwani's trial began in March", kicker="TWO TRIALS · ONE JUDGE")
setline("In May twenty twenty-three, the court ordered restitution", say="In May twenty twenty-three, the court ordered restitution: four hundred fifty-two million dollars, with Holmes and Balwani each liable for the full amount, to investors and to Safeway and Walgreens.", show="In May 2023, the court ordered restitution: $452 million, with Holmes and Balwani jointly and severally liable, to investors and to Safeway and Walgreens.")
setline("So why more time for Balwani?", say="So why more time for Balwani? The record gives the pieces. Every count against him ended in a guilty verdict, including defrauding patients. The S.E.C. alleged he drafted the numbers investors saw. And he oversaw the lab the warnings came from.", show="So why more time for Balwani? The record gives the pieces. Every count against him ended in a guilty verdict, including defrauding patients. The SEC alleged he drafted the numbers investors saw. And he oversaw the lab the warnings came from.")
from panfix import fix
fix(lines, "long")
spec = {"label": "SWORN · CASE 011", "lines": lines}
json.dump(spec, open(os.path.join(HERE, "episode.json"), "w"), indent=1, ensure_ascii=False)
print(len(lines), "lines,", sum(len(l["say"].split()) for l in lines), "words")
