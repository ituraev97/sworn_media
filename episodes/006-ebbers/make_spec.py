import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
def hl(name, i=0):
    a, b = HL[name][i]
    return [0.0, a, 1.0, round(b - a, 4)]
CASE = "U.S. v. EBBERS"
SRC_OPP = "Brief for the United States in Opposition, Ebbers v. United States, No. 06-590 (2007)"
SRC_CA2 = "U.S. v. Ebbers, 458 F.3d 110 (2d Cir. Jul 28, 2006)"
SRC_DCT = "U.S. v. Ebbers, S.D.N.Y., order of Jul 9, 2005"
SRC_CFTF = "DOJ Corporate Fraud Task Force, First Year Report to the President, Jul 2003"
SRC_GL = "Government letter, S.D.N.Y., Oct 4, 2019 (Dkt. 354)"
SRC_TR = "Sentencing transcript, S.D.N.Y., Jul 13, 2005 (Exhibit B to Dkt. 354)"
SRC_SEC = "SEC complaint, SEC v. WorldCom, S.D.N.Y., Jun 26, 2002"
SRC_SECPR = "SEC press release 2002-94, Jun 26, 2002"
SRC_HR = "House Financial Services Committee hearing, Jul 8, 2002 (Serial No. 107-74)"
SRC_AG = "Attorney General's prepared remarks, Mar 2, 2004"
SRC_TIME = "TIME, “The Night Detective,” Dec 2002"
SRC_AP02 = "Associated Press, Jul 22, 2002"
SRC_AP05 = "Associated Press, Mar 16, 2005"
SRC_APS = "Associated Press, Aug 12, 2005"
SRC_AP06 = "Associated Press, Sep 26, 2006"
SRC_AP07 = "Associated Press, Mar 5, 2007"
SRC_OPN = "U.S. v. Ebbers, 432 F. Supp. 3d 421 (S.D.N.Y. Jan 8, 2020)"
SRC_WLBT = "WLBT, Feb 3, 2020 (family statement)"
CA2Q = "As quoted in U.S. v. Ebbers, 2d Cir., Jul 28, 2006"
def L(say, scene=None, show=None, **kw):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    d.update(kw); return d
def doc(img, kicker, title, src, i=0, pan=None):
    return dict(type="doc", img=f"img/{img}.jpg", pan=pan or [0.0, 0.1], hl=hl(img, i), kicker=kicker, title=title, src=src)
lines = [
 # COLD OPEN
 L("At his trial in two thousand five, the former chief executive of WorldCom was asked about a monthly report on the company's expenses. He admitted he received it. But in two thousand one, he said, he began throwing it in the trash without reading it.",
   doc("opp_trash", "HIS OWN TESTIMONY · PER THE GOVERNMENT", "“in the trash without reading it”", SRC_OPP),
   show="At his trial in 2005, the former chief executive of WorldCom was asked about a monthly report on the company's expenses. He admitted he received it. But in 2001, he said, he began throwing it in the trash without reading it."),
 L("So the judge told the jury it could consider whether he deliberately closed his eyes to what otherwise would have been obvious.",
   doc("opp_instr", "THE JURY INSTRUCTION", "Conscious avoidance", SRC_OPP)),
 L("The Justice Department called the case the largest accounting fraud in U.S. history. Billions of dollars in ordinary costs, recorded as if they were investments.",
   dict(type="big", kicker="PER THE JUSTICE DEPARTMENT", lines=["Ordinary costs.", "Booked as|investments."], src=SRC_CFTF + " · " + SRC_OPP)),
 L("His name was Bernard Ebbers. This is the paper trail.",
   dict(type="big", kicker="THE DEFENDANT", lines=["Bernard Ebbers.", "The paper trail."], src=SRC_CA2)),
 L("This is SWORN.",
   dict(type="title", kicker="SWORN · CASE 006 · THE PAPER TRAIL", title="The Line|Costs", sub="United States v. Bernard J. Ebbers · Southern District of New York · 2002–2005")),
 # I
 L("Chapter one. Hit the numbers.", dict(type="chapter", n="I", title="Hit the Numbers")),
 L("Before WorldCom, Ebbers had been a teacher, a coach and a motel operator. In nineteen eighty-three he invested in a small long-distance company in Mississippi. By two thousand, renamed WorldCom, it had about ninety thousand employees in sixty-five countries, and reported revenues of thirty-nine billion dollars.",
   dict(type="stat", kicker="WORLDCOM · 2000 · PER THE APPEALS COURT", value="$39B", label="in reported revenues —|90,000 employees in 65 countries", src=SRC_CA2),
   show="Before WorldCom, Ebbers had been a teacher, a coach and a motel operator. In 1983 he invested in a small long-distance company in Mississippi. By 2000, renamed WorldCom, it had about 90,000 employees in 65 countries, and reported revenues of $39 billion."),
 L("Its largest expense was something called line costs: the fees it paid to use other companies' telephone networks.",
   doc("opp_line", "THE LARGEST EXPENSE", "“line costs”", SRC_OPP, 0)),
 L("Then the dot-com bubble burst. Demand fell. In the third quarter of two thousand, line costs came in almost one billion dollars higher than expected.",
   doc("opp_line", "THIRD QUARTER 2000", "“almost $1 billion higher than expected”", SRC_OPP, 1),
   show="Then the dot-com bubble burst. Demand fell. In the third quarter of 2000, line costs came in almost $1 billion higher than expected."),
 L("Ebbers had his own reasons to watch the stock. He had borrowed over four hundred million dollars from banks, using his WorldCom shares as collateral. As the price fell, the margin calls came, and in October two thousand, WorldCom took on the liability for his bank debts. He now owed that money to WorldCom instead.",
   doc("ca2_loans", "EBBERS' PERSONAL FINANCES", "“over $400 million”", SRC_CA2),
   show="Ebbers had his own reasons to watch the stock. He had borrowed over $400 million from banks, using his WorldCom shares as collateral. As the price fell, the margin calls came, and in October 2000, WorldCom took on the liability for his bank debts. He now owed that money to WorldCom instead."),
 L("According to the trial evidence, as the appeals court described it, chief financial officer Scott Sullivan told Ebbers they should issue an earnings warning. Ebbers refused. When Sullivan said meeting expectations would take an improper adjustment, Ebbers replied:",
   doc("ca2_hit", "THIRD QUARTER 2000", "The earnings warning that wasn't", SRC_CA2)),
 L("We have to hit our numbers.",
   dict(type="quote", q="[W]e have to hit our numbers.", case=CASE, doc="EBBERS TO CFO SCOTT SULLIVAN · 2000", cite=CA2Q, size=64)),
 # II
 L("Chapter two. The line costs.", dict(type="chapter", n="II", title="The Line Costs")),
 L("The first line-cost fix came from reserves. On Sullivan's instructions, Controller David Myers and his staff reduced line-cost accounts and drew down reserves by the same amounts. Reported line costs fell by about eight hundred twenty-eight million dollars.",
   dict(type="big", kicker="THIRD QUARTER 2000 · PER THE APPEALS COURT", lines=["$828 million.", "From reserves."], src=SRC_CA2),
   show="The first line-cost fix came from reserves. On Sullivan's instructions, Controller David Myers and his staff reduced line-cost accounts and drew down reserves by the same amounts. Reported line costs fell by about $828 million."),
 L("Two accountants on that staff believed the entries were wrong and considered resigning. Told about it, Ebbers said they shouldn't be putting people in this position, and apologized to Myers.",
   doc("ca2_resign", "THE ACCOUNTING STAFF", "“considered resigning”", SRC_CA2)),
 L("The next quarter, the staff cut the income tax reserve by four hundred seven million dollars and altered other accounts, until reported line costs were seven hundred ninety-seven million dollars lower. The monthly reports sent to Ebbers carried the reduced line costs: an apparent gross margin of seventy-eight percent in September two thousand, and seventy-four percent in December. WorldCom had never achieved margins like that.",
   dict(type="stat", kicker="PER THE APPEALS COURT", value="78%", label="apparent gross margin, Sept. 2000 report —|never achieved by WorldCom before", src=SRC_CA2),
   show="The next quarter, the staff cut the income tax reserve by $407 million and altered other accounts, until reported line costs were $797 million lower. The monthly reports sent to Ebbers carried the reduced line costs: an apparent gross margin of 78% in September 2000, and 74% in December. WorldCom had never achieved margins like that."),
 L("By early two thousand one, the reserves were largely exhausted. Sullivan proposed something new. Line costs had always been operating expenses. Now part of them would be booked as capital expenditures, like investments in equipment.",
   doc("opp_38", "2001 · PER THE GOVERNMENT", "Line costs → capital expenditures", SRC_OPP),
   show="By early 2001, the reserves were largely exhausted. Sullivan proposed something new. Line costs had always been operating expenses. Now part of them would be booked as capital expenditures, like investments in equipment."),
 L("At a dinner in Washington in March two thousand one, Sullivan told Ebbers the planned move, over five hundred million dollars, wasn't right. Ebbers did not deter him.",
   doc("ca2_right", "MARCH 2001 · WASHINGTON", "“wasn't right”", SRC_CA2),
   show="At a dinner in Washington in March 2001, Sullivan told Ebbers the planned move, over $500 million, \"wasn't right.\" Ebbers did not deter him."),
 L("On the earnings call, the change went unmentioned. Ebbers said there were no storms on the horizon, and urged listeners to go out and buy stock.",
   doc("ca2_storms", "FIRST QUARTER 2001 · EARNINGS CALL", "“no storms on the horizon”", SRC_CA2)),
 L("At one line-cost meeting, he told employees his lifeblood was in the stock. If it fell below about twelve dollars a share, margin calls would wipe him out.",
   dict(type="big", kicker="2001 · PER THE APPEALS COURT", lines=["His lifeblood:", "the stock."], src=SRC_CA2),
   show="At one line-cost meeting, he told employees his \"lifeblood was in the stock.\" If it fell below about $12 a share, margin calls would wipe him out."),
 L("Revenue was the other problem. Executives created a program called Close the Gap, to find new items to count. In a voicemail to Ebbers, Sullivan described some of them as accounting fluff, one-time stuff, and junk.",
   doc("ca2_fluff", "“CLOSE THE GAP”", "“accounting fluff” · “junk”", SRC_CA2),
   show="Revenue was the other problem. Executives created a program called \"Close the Gap,\" to find new items to count. In a voicemail to Ebbers, Sullivan described some of them as \"accounting fluff,\" \"one-time stuff,\" and \"junk.\""),
 L("Quarter after quarter, the capitalized line costs grew. Seven hundred seventy-one million. Over six hundred ten million. Over seven hundred million. Over nine hundred forty-one million. Eight hundred eighteen million.",
   dict(type="bars", kicker="LINE COSTS CAPITALIZED · PER THE APPEALS COURT", title="Expenses moved to capital", items=[{"label": "Q1 2001", "value": 771, "display": "$771M"}, {"label": "Q2 2001", "value": 610, "display": "$610M+"}, {"label": "Q3 2001", "value": 700, "display": "$700M+"}, {"label": "Q4 2001", "value": 941, "display": "$941M+"}, {"label": "Q1 2002", "value": 818, "display": "$818M"}], src=SRC_CA2),
   show="Quarter after quarter, the capitalized line costs grew. $771 million. Over $610 million. Over $700 million. Over $941 million. $818 million."),
 L("After the fourth quarter, Ebbers assured investors: we stand by our accounting. In total, about three point eight billion dollars had been moved from expenses to capital.",
   doc("ca2_stand", "FOURTH QUARTER 2001 · EARNINGS CALL", "“[w]e stand by our accounting”", SRC_CA2 + " · " + SRC_OPP),
   show="After the fourth quarter, Ebbers assured investors: \"We stand by our accounting.\" In total, about $3.8 billion had been moved from expenses to capital."),
 # III
 L("Chapter three. The audit.", dict(type="chapter", n="III", title="The Audit")),
 L("In March two thousand two, the S.E.C. began to investigate WorldCom. At the end of April, the board asked Ebbers to resign. He did, on April twenty-ninth. In May, he bought three million more shares of WorldCom stock.",
   dict(type="timeline", kicker="2002 · PER THE APPEALS COURT", events=[{"date": "MARCH", "text": "SEC investigates"}, {"date": "APRIL 29", "text": "Ebbers resigns"}, {"date": "MAY", "text": "Buys 3 million shares"}, {"date": "JUNE 25", "text": "Fraud disclosed"}], at=2, src=SRC_CA2),
   show="In March 2002, the SEC began to investigate WorldCom. At the end of April, the board asked Ebbers to resign. He did, on April 29. In May, he bought three million more shares of WorldCom stock."),
 L("A month after he left, WorldCom's own internal audit department found the capitalized line costs. TIME magazine later reported that its head, Cynthia Cooper, and her team worked late into the night, keeping the project secret.",
   dict(type="big", kicker="MAY–JUNE 2002 · PER TIME", lines=["Internal audit.", "Late into|the night."], src=SRC_CA2 + " · " + SRC_TIME)),
 L("According to TIME, on June eleventh, Sullivan asked her to delay the audit. She refused. The next day she told the head of the board's audit committee.",
   dict(type="big", kicker="JUNE 11, 2002 · PER TIME", lines=["Delay the audit?", "Refused."], src=SRC_TIME),
   show="According to TIME, on June 11, Sullivan asked her to delay the audit. She refused. The next day she told the head of the board's audit committee."),
 L("Sullivan was soon fired. On June twenty-fifth, two thousand two, WorldCom disclosed the fraud. The stock lost ninety percent of its value.",
   doc("ca2_audit", "JUNE 25, 2002", "The disclosure", SRC_CA2),
   show="Sullivan was soon fired. On June 25, 2002, WorldCom disclosed the fraud. The stock lost 90% of its value."),
 L("Within twenty-four hours, the S.E.C. sued. Its complaint said WorldCom had overstated its income by about three point oh five five billion dollars in two thousand one, and seven hundred ninety-seven million in early two thousand two. For two thousand one, it said, the company had actually lost about six hundred sixty-two million dollars.",
   doc("cf_24h", "WITHIN 24 HOURS", "“more than $3.8 billion”", SRC_CFTF + " · " + SRC_SEC),
   show="Within 24 hours, the SEC sued. Its complaint said WorldCom had overstated its income by about $3.055 billion in 2001, and $797 million in early 2002. For 2001, it said, the company had actually lost about $662 million."),
 L("The S.E.C.'s statement that day called them accounting improprieties of unprecedented magnitude.",
   dict(type="quote", q="accounting improprieties of unprecedented magnitude", case="SEC v. WORLDCOM", doc="SEC STATEMENT · JUNE 26, 2002", cite=SRC_SECPR, size=58)),
 L("On July eighth, Ebbers appeared before a House committee. He read a statement, then declined to answer questions, citing his Fifth Amendment rights.",
   dict(type="quote", q="I believe that no one will conclude that I engaged in any criminal or fraudulent conduct during my tenure at WorldCom.", case="HOUSE FINANCIAL SERVICES COMMITTEE", doc="BERNARD EBBERS · JULY 8, 2002", cite=SRC_HR, size=44),
   show="On July 8, Ebbers appeared before a House committee. He read a statement, then declined to answer questions, citing his Fifth Amendment rights."),
 L("On July twenty-first, WorldCom filed for bankruptcy, reporting one hundred seven billion dollars in assets, the largest bankruptcy in U.S. history at the time, the Associated Press reported.",
   dict(type="big", kicker="JULY 21, 2002 · PER THE ASSOCIATED PRESS", lines=["$107 billion.", "Bankrupt."], src=SRC_AP02),
   show="On July 21, WorldCom filed for bankruptcy, reporting $107 billion in assets, the largest bankruptcy in U.S. history at the time, the Associated Press reported."),
 L("On August first, five weeks after the disclosure, prosecutors filed a criminal complaint against Sullivan and Myers.",
   doc("cf_5wk", "AUGUST 1, 2002", "“five weeks after”", SRC_CFTF),
   show="On August 1, five weeks after the disclosure, prosecutors filed a criminal complaint against Sullivan and Myers."),
 # IV
 L("Chapter four. The trial.", dict(type="chapter", n="IV", title="The Trial")),
 L("Myers and three former members of his department were convicted. On March second, two thousand four, Sullivan pleaded guilty and agreed to cooperate. That same day, an indictment against Ebbers was unsealed. That September, a superseding indictment charged him with nine counts.",
   dict(type="timeline", kicker="THE CHARGES", events=[{"date": "AUG 1, 2002", "text": "Sullivan, Myers charged"}, {"date": "MAR 2, 2004", "text": "Sullivan pleads guilty"}, {"date": "SEP 15, 2004", "text": "Ebbers: 9 counts"}, {"date": "JAN 2005", "text": "Trial begins"}], at=2, src=SRC_CFTF + " · " + SRC_AG + " · " + SRC_GL),
   show="Myers and three former members of his department were convicted. On March 2, 2004, Sullivan pleaded guilty and agreed to cooperate. That same day, an indictment against Ebbers was unsealed. That September, a superseding indictment charged him with nine counts."),
 L("The government called fourteen witnesses and introduced more than three hundred exhibits. Five witnesses, including Sullivan, had cooperation agreements. According to the Associated Press, only Sullivan directly implicated Ebbers.",
   doc("opp_numbers", "THE TRIAL · 2005", "14 witnesses · 300+ exhibits", SRC_OPP + " · " + SRC_AP05, 1),
   show="The government called 14 witnesses and introduced more than 300 exhibits. Five witnesses, including Sullivan, had cooperation agreements. According to the Associated Press, only Sullivan directly implicated Ebbers."),
 L("Ebbers testified in his own defense. He denied speaking with Sullivan about improper adjustments to line costs, and said he never noticed them on the reports he reviewed.",
   dict(type="big", kicker="THE DEFENSE · PER THE GOVERNMENT", lines=["He testified.", "He never|noticed."], src=SRC_OPP)),
 L("The trial judge, Barbara Jones, pointed to one of those reports. September two thousand: line costs of seven hundred thirty-two million dollars, against a budget of one point four billion. Shown it at trial, Ebbers said he simply did not notice.",
   dict(type="stat", kicker="SEPTEMBER 2000 REPORT · PER JUDGE JONES", value="$732M", label="in line costs —|against a $1.4 billion budget", src=SRC_DCT),
   show="The trial judge, Barbara Jones, pointed to one of those reports. September 2000: line costs of $732 million, against a budget of $1.4 billion. Shown it at trial, Ebbers said he simply \"did not notice.\""),
 L("The appeals court later summed up his own testimony: using a procedure for signing documents he didn't bother to read in full, including the ten-Ks, and tossing the management budget variance report in the trash without reading it.",
   doc("ca2_trash", "THE APPEALS COURT", "“tossing … in the trash”", SRC_CA2),
   show="The appeals court later summed up his own testimony: \"using a procedure for signing documents he didn't bother to read in full, including the 10-Ks, and tossing the management budget variance report in the trash without reading it.\""),
 L("That was why the jury heard the instruction on conscious avoidance.",
   doc("opp_instr", "THE JURY INSTRUCTION", "“deliberately closed his eyes”", SRC_OPP)),
 L("On March fifteenth, two thousand five, after eight days of deliberation, the jury found Bernard Ebbers guilty on all nine counts.",
   dict(type="verdict", kicker="THE VERDICT · MARCH 15, 2005", stamp="GUILTY", big="All 9 counts", sub="Bernard J. Ebbers · conspiracy, securities fraud, false filings"),
   show="On March 15, 2005, after eight days of deliberation, the jury found Bernard Ebbers guilty on all nine counts."),
 # V
 L("Chapter five. The sentence.", dict(type="chapter", n="V", title="The Sentence")),
 L("July thirteenth, two thousand five. Judge Jones found that the probation office's loss figure, over two billion dollars, was a reasonable estimate. The guidelines range: thirty years to life.",
   dict(type="stat", kicker="JULY 13, 2005 · PER THE GOVERNMENT", value="$2B+", label="in losses — “a reasonable estimate”|guidelines: 30 years to life", src=SRC_GL),
   show="July 13, 2005. Judge Jones found that the probation office's loss figure, over $2 billion, was \"a reasonable estimate.\" The guidelines range: 30 years to life."),
 L("She credited testimony that Ebbers was the instigator of the fraud.",
   doc("gl_jones", "JUDGE BARBARA S. JONES", "“the instigator of the fraud”", SRC_GL + " · " + SRC_TR, 0)),
 L("Then she addressed his age and his heart condition.",
   dict(type="quote", q="Although I recognize, as the defense has pointed out, that this sentence is likely to be a life sentence for Mr. Ebbers, I find that a sentence of anything less would not sufficiently reflect the seriousness of this crime.", case=CASE, doc="JUDGE BARBARA S. JONES · JULY 13, 2005", cite=SRC_TR, size=36)),
 L("Twenty-five years in prison. He was sixty-three. There was no fine and no restitution order. Under a settlement with shareholders, he had to give up substantially all of his remaining assets.",
   dict(type="verdict", kicker="THE SENTENCE · JULY 13, 2005", stamp="SENTENCED", big="25 years", sub="Bernard J. Ebbers · assets to the shareholders' settlement"),
   show="25 years in prison. He was 63. There was no fine and no restitution order. Under a settlement with shareholders, he had to give up substantially all of his remaining assets."),
 L("The people who made the entries had pleaded guilty and cooperated. Sullivan, whom the judge called the architect of the fraud, got five years. Myers, a year and a day. So did accounting director Buford Yates. One accountant got five months. Another, probation.",
   dict(type="bars", kicker="THE SENTENCES · PER THE APPEALS COURT", title="Prison, in months", items=[{"label": "CFO SULLIVAN", "value": 60, "display": "60"}, {"label": "MYERS", "value": 12, "display": "12+"}, {"label": "YATES", "value": 12, "display": "12+"}, {"label": "VINSON", "value": 5, "display": "5"}, {"label": "NORMAND", "value": 0, "display": "0"}, {"label": "EBBERS", "value": 300, "display": "300"}], src=SRC_CA2 + " · " + SRC_APS),
   show="The people who made the entries had pleaded guilty and cooperated. Sullivan, whom the judge called \"the architect of the fraud,\" got five years. Myers, a year and a day. So did accounting director Buford Yates. One accountant got five months. Another, probation."),
 L("The appeals court explained the gap. All of them cooperated and pleaded guilty. Ebbers did not. And each was his subordinate.",
   doc("ca2_why", "THE APPEALS COURT", "“Ebbers did not.”", SRC_CA2)),
 # VI
 L("Chapter six. After the verdict.", dict(type="chapter", n="VI", title="After the Verdict")),
 L("In July two thousand six, the Second Circuit affirmed. Twenty-five years, it wrote, is a long sentence for a white collar crime. But given Congress' policy decisions on sentences for fraud, the sentence is harsh but not unreasonable.",
   doc("ca2_harsh", "JULY 28, 2006 · SECOND CIRCUIT", "“harsh but not unreasonable”", SRC_CA2),
   show="In July 2006, the Second Circuit affirmed. \"Twenty-five years is a long sentence for a white collar crime,\" it wrote. But given Congress' policy decisions on sentences for fraud, \"the sentence is harsh but not unreasonable.\""),
 L("On September twenty-sixth, two thousand six, he reported to federal prison in Oakdale, driving himself there, the Associated Press reported. In March two thousand seven, the Supreme Court declined to hear his case. His projected release date was July fourth, two thousand twenty-eight.",
   doc("gl_2028", "BUREAU OF PRISONS · PER THE GOVERNMENT", "Release date: July 4, 2028", SRC_GL + " · " + SRC_AP06 + " · " + SRC_AP07),
   show="On September 26, 2006, he reported to federal prison in Oakdale, driving himself there, the Associated Press reported. In March 2007, the Supreme Court declined to hear his case. His projected release date was July 4, 2028."),
 L("WorldCom itself had settled with the S.E.C.: a civil penalty of two point two five billion dollars, to be satisfied in bankruptcy with seven hundred fifty million dollars in cash and stock for defrauded investors.",
   dict(type="stat", kicker="SEC v. WORLDCOM · PER THE JUSTICE DEPARTMENT", value="$750M", label="to investors, to satisfy|a $2.25 billion penalty", src=SRC_CFTF),
   show="WorldCom itself had settled with the SEC: a civil penalty of $2.25 billion, to be satisfied in bankruptcy with $750 million in cash and stock for defrauded investors."),
 L("In September two thousand nineteen, after almost thirteen years in prison, Ebbers asked to be released on medical grounds. He was legally blind, with a heart condition and significant weight loss. One letter of support came from the judge who had sentenced him, Barbara Jones, now retired. Given his serious health problems, she wrote, he has been punished enough.",
   doc("gl_enough", "THE SENTENCING JUDGE'S LETTER · PER THE GOVERNMENT", "“punished enough”", SRC_GL),
   show="In September 2019, after almost 13 years in prison, Ebbers asked to be released on medical grounds. He was legally blind, with a heart condition and significant weight loss. One letter of support came from the judge who had sentenced him, Barbara Jones, now retired. \"Given [his] serious health problems,\" she wrote, he \"has been punished enough.\""),
 L("The government opposed, pointing to the size of the fraud and to her own words at sentencing: likely a life sentence.",
   doc("gl_open", "OCTOBER 4, 2019 · U.S. ATTORNEY, S.D.N.Y.", "The government opposes", SRC_GL)),
 L("On December eighteenth, two thousand nineteen, Judge Valerie Caproni granted the motion. He left federal custody on December twenty-first. Bernard Ebbers died on February second, two thousand twenty. He was seventy-eight.",
   dict(type="timeline", kicker="2019–2020", events=[{"date": "SEP 5, 2019", "text": "Motion filed"}, {"date": "DEC 18, 2019", "text": "Release granted"}, {"date": "DEC 21, 2019", "text": "Leaves custody"}, {"date": "FEB 2, 2020", "text": "Dies at 78"}], at=1, src=SRC_OPN + " · " + SRC_WLBT),
   show="On December 18, 2019, Judge Valerie Caproni granted the motion. He left federal custody on December 21. Bernard Ebbers died on February 2, 2020. He was 78."),
 L("September two thousand. Seven hundred thirty-two million dollars in line costs, against a budget of one point four billion.",
   dict(type="big", lines=["$732M reported.", "$1.4B|budgeted."]),
   show="September 2000. $732 million in line costs, against a budget of $1.4 billion."),
 L("He said he never noticed. The paper trail did.",
   dict(type="big", lines=["He never noticed.", "The paper|trail did."])),
 L("This is SWORN. Real trials. Real evidence. The verdict.", dict(type="end")),
]
from panfix import fix
fix(lines, "long")
spec = {"label": "SWORN · CASE 006", "lines": lines}
json.dump(spec, open(os.path.join(HERE, "episode.json"), "w"), indent=1, ensure_ascii=False)
print(len(lines), "lines,", sum(len(l["say"].split()) for l in lines), "words")
