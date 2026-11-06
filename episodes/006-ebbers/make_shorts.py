import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
def hl(name, i=0):
    a, b = HL[name][i]
    return [0.0, a, 1.0, round(b - a, 4)]
def doc(img, kicker, src, i=0):
    return dict(type="doc", img=f"img/{img}.jpg", pan=[0.0, 0.1], hl=hl(img, i), kicker=kicker, src=src)
CASE = "U.S. v. EBBERS"
SRC_OPP = "U.S. brief in opposition, No. 06-590, 2007"
SRC_CA2 = "U.S. v. Ebbers, 2d Cir., Jul 28, 2006"
SRC_DCT = "S.D.N.Y. order, Jul 9, 2005"
SRC_CFTF = "DOJ Corporate Fraud Task Force, 2003"
SRC_GL = "Gov't letter, S.D.N.Y., Oct 4, 2019"
SRC_TR = "Sentencing transcript, Jul 13, 2005"
SRC_SEC = "SEC complaint, Jun 26, 2002"
SRC_TIME = "TIME, Dec 2002"
SRC_AP05 = "Associated Press, Mar 16, 2005"
SRC_APS = "Associated Press, Aug 12, 2005"
SRC_OPN = "S.D.N.Y. opinion, Jan 8, 2020"
SRC_WLBT = "WLBT, Feb 3, 2020"
CA2Q = "As quoted in U.S. v. Ebbers, 2d Cir., 2006"
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
END = L("Real trials. Real evidence. The verdict.", dict(type="end"))
shorts = [
 {"title": "\"We Have to Hit Our Numbers\": The Order Behind the WorldCom Fraud", "hook": "\"We have to hit|our numbers.\"", "lines": [
  L("Third quarter, two thousand. WorldCom can't meet Wall Street's expectations, and its line costs come in almost one billion dollars higher than expected.",
    doc("opp_line", "THIRD QUARTER 2000", SRC_OPP, 1),
    show="Third quarter, 2000. WorldCom can't meet Wall Street's expectations, and its line costs come in almost $1 billion higher than expected."),
  L("The finance chief, Scott Sullivan, tells CEO Bernard Ebbers they should warn investors. According to the appeals court, Ebbers refuses.",
    doc("ca2_hit", "THE EARNINGS WARNING", SRC_CA2)),
  L("His answer, as the appeals court described the trial evidence: we have to hit our numbers.",
    dict(type="quote", q="[W]e have to hit our numbers.", case=CASE, doc="EBBERS TO HIS CFO", cite=CA2Q, size=56)),
  L("Ebbers had borrowed over four hundred million dollars against his WorldCom stock.",
    dict(type="stat", kicker="PER THE APPEALS COURT", value="$400M+", label="borrowed against|his shares", src=SRC_CA2),
    show="Ebbers had borrowed over $400 million against his WorldCom stock."),
  L("Over the next year and a half, about three point eight billion dollars in expenses were booked as capital.",
    doc("opp_38", "2001–2002", SRC_OPP),
    show="Over the next year and a half, about $3.8 billion in expenses were booked as capital."),
  L("In two thousand five, a jury convicted him on all nine counts. Twenty-five years.",
    dict(type="verdict", kicker="2005", stamp="SENTENCED", big="25 years", sub="Bernard J. Ebbers"),
    show="In 2005, a jury convicted him on all nine counts. 25 years."),
  END]},
 {"title": "The WorldCom CEO Said He Threw the Key Report in the Trash", "hook": "He said he threw|it in the trash.", "lines": [
  L("Bernard Ebbers ran WorldCom. Every month he got a report on the company's expenses.",
    dict(type="big", kicker="WORLDCOM", lines=["Every month,", "a|report."], src=SRC_DCT)),
  L("September two thousand: line costs of seven hundred thirty-two million dollars, against a budget of one point four billion.",
    dict(type="stat", kicker="SEPTEMBER 2000", value="$732M", label="vs. a $1.4 billion|budget", src=SRC_DCT),
    show="September 2000: line costs of $732 million, against a budget of $1.4 billion."),
  L("At his trial, he said he simply did not notice. And he said that in two thousand one, he began throwing the report in the trash without reading it.",
    doc("opp_trash", "HIS TESTIMONY · PER THE GOVERNMENT", SRC_OPP),
    show="At his trial, he said he simply \"did not notice.\" And he said that in 2001, he began throwing the report in the trash without reading it."),
  L("So the judge gave the jury an instruction on conscious avoidance.",
    doc("opp_instr", "THE JURY INSTRUCTION", SRC_OPP)),
  L("Whether he deliberately closed his eyes to what otherwise would have been obvious.",
    dict(type="quote", q="whether [petitioner] deliberately closed his eyes to what otherwise would have been obvious.", case=CASE, doc="THE JURY CHARGE", cite="As quoted in the U.S. brief in opposition, 2007", size=44)),
  L("Guilty on all nine counts. The appeals court upheld it.",
    dict(type="verdict", kicker="MARCH 15, 2005", stamp="GUILTY", big="9 of 9", sub="Bernard J. Ebbers")),
  END]},
 {"title": "How WorldCom Turned $3.8 Billion in Costs Into \"Investments\"", "hook": "Costs became|\"investments.\"", "lines": [
  L("WorldCom's biggest expense was line costs, the fees it paid to use other telephone networks.",
    doc("opp_line", "THE LARGEST EXPENSE", SRC_OPP, 0)),
  L("In two thousand one, prosecutors said, the company started booking part of them as capital expenditures, like new equipment.",
    dict(type="big", kicker="2001", lines=["Expenses?", "Now|capital."], src=SRC_OPP),
    show="In 2001, prosecutors said, the company started booking part of them as capital expenditures, like new equipment."),
  L("At a dinner, the CFO told CEO Bernard Ebbers the first move, over five hundred million dollars, wasn't right. Ebbers did not stop him.",
    doc("ca2_right", "MARCH 2001", SRC_CA2),
    show="At a dinner, the CFO told CEO Bernard Ebbers the first move, over $500 million, \"wasn't right.\" Ebbers did not stop him."),
  L("Quarter by quarter: seven hundred seventy-one million, more than six hundred ten million, more than seven hundred million, more than nine hundred forty-one million, eight hundred eighteen million.",
    dict(type="bars", kicker="CAPITALIZED", title="Line costs", items=[{"label": "Q1 01", "value": 771, "display": "771"}, {"label": "Q2", "value": 610, "display": "610+"}, {"label": "Q3", "value": 700, "display": "700+"}, {"label": "Q4", "value": 941, "display": "941+"}, {"label": "Q1 02", "value": 818, "display": "818"}], src=SRC_CA2 + " · $ millions"),
    show="Quarter by quarter: $771 million, more than $610 million, more than $700 million, more than $941 million, $818 million."),
  L("Ebbers told investors: we stand by our accounting.",
    doc("ca2_stand", "EARNINGS CALL", SRC_CA2),
    show="Ebbers told investors: \"We stand by our accounting.\""),
  L("Total: about three point eight billion dollars. He got twenty-five years.",
    dict(type="big", kicker="THE TOTAL", lines=["$3.8 billion.", "25|years."], src=SRC_OPP),
    show="Total: about $3.8 billion. He got 25 years."),
  END]},
 {"title": "The Internal Auditor Who Found WorldCom's Hidden Billions", "hook": "The auditor who|wouldn't wait.", "lines": [
  L("May two thousand two. WorldCom's CEO, Bernard Ebbers, has just resigned.",
    dict(type="big", kicker="MAY 2002", lines=["The CEO", "is|gone."], src=SRC_CA2),
    show="May 2002. WorldCom's CEO, Bernard Ebbers, has just resigned."),
  L("Inside the company, the internal audit department finds billions in expenses booked as capital.",
    doc("ca2_audit", "INTERNAL AUDIT", SRC_CA2)),
  L("TIME reported that its head, Cynthia Cooper, and her team worked late into the night, in secret.",
    dict(type="big", kicker="PER TIME", lines=["Late nights.", "In|secret."], src=SRC_TIME)),
  L("On June eleventh, according to TIME, the CFO asked her to delay the audit. She refused, and went to the board's audit committee.",
    dict(type="big", kicker="JUNE 11, 2002 · PER TIME", lines=["Delay it?", "Refused."], src=SRC_TIME),
    show="On June 11, according to TIME, the CFO asked her to delay the audit. She refused, and went to the board's audit committee."),
  L("June twenty-fifth, WorldCom disclosed the fraud. Within twenty-four hours, the S.E.C. sued.",
    doc("cf_24h", "WITHIN 24 HOURS", SRC_CFTF + " · " + SRC_SEC),
    show="June 25, WorldCom disclosed the fraud. Within 24 hours, the SEC sued."),
  L("The stock lost ninety percent. The CEO got twenty-five years.",
    dict(type="verdict", kicker="2005", stamp="SENTENCED", big="25 years", sub="Bernard J. Ebbers"),
    show="The stock lost 90%. The CEO got 25 years."),
  END]},
 {"title": "25 Years for the CEO, 5 for the CFO: The WorldCom Sentences", "hook": "25 years vs.|5 years.", "lines": [
  L("WorldCom's finance chief, Scott Sullivan, directed the accounting entries. Judge Barbara Jones called him the architect of the fraud.",
    dict(type="big", kicker="PER THE ASSOCIATED PRESS", lines=["“The architect", "of the|fraud.”"], src=SRC_APS),
    show="WorldCom's finance chief, Scott Sullivan, directed the accounting entries. Judge Barbara Jones called him \"the architect of the fraud.\""),
  L("He pleaded guilty and testified against his boss. He got five years. The controller, a year and a day.",
    doc("ca2_codef", "THE OTHER SENTENCES", SRC_CA2)),
  L("CEO Bernard Ebbers went to trial. The judge credited testimony that he was the instigator.",
    doc("gl_jones", "JUDGE BARBARA S. JONES", SRC_GL + " · " + SRC_TR, 0)),
  L("His guidelines range: thirty years to life. She gave him twenty-five.",
    dict(type="stat", kicker="JULY 13, 2005", value="25", label="years — below|30 years to life", src=SRC_GL)),
  L("The appeals court said the difference was cooperation, and rank. Each of the others was his subordinate.",
    dict(type="big", kicker="SECOND CIRCUIT", lines=["They pleaded.", "He|didn't."], src=SRC_CA2)),
  L("Its verdict on twenty-five years: harsh but not unreasonable.",
    doc("ca2_harsh", "JULY 28, 2006", SRC_CA2),
    show="Its verdict on 25 years: \"harsh but not unreasonable.\""),
  END]},
 {"title": "The Judge Who Gave Bernie Ebbers 25 Years Later Wrote: \"Punished Enough\"", "hook": "Likely a life sentence.|Then 2019.", "lines": [
  L("Two thousand five. Judge Barbara Jones sentences WorldCom's ex-CEO, Bernard Ebbers, to twenty-five years.",
    dict(type="verdict", kicker="JULY 13, 2005", stamp="SENTENCED", big="25 years", sub="Bernard J. Ebbers"),
    show="2005. Judge Barbara Jones sentences WorldCom's ex-CEO, Bernard Ebbers, to 25 years."),
  L("She said it was likely to be a life sentence, but that anything less would not sufficiently reflect the seriousness of the crime.",
    doc("gl_jones", "AT SENTENCING", SRC_GL, 1)),
  L("Two thousand nineteen. Ebbers, legally blind and in failing health, asks for compassionate release.",
    dict(type="big", kicker="SEPTEMBER 2019", lines=["Legally blind.", "Asks to|go home."], src=SRC_GL),
    show="2019. Ebbers, legally blind and in failing health, asks for compassionate release."),
  L("A letter of support comes from the retired judge who sentenced him. He has been punished enough, she writes.",
    doc("gl_enough", "JUDGE JONES' LETTER", SRC_GL)),
  L("Prosecutors object. In December, Judge Valerie Caproni grants the release.",
    dict(type="big", kicker="DECEMBER 18, 2019", lines=["Release:", "granted."], src=SRC_OPN)),
  L("He died on February second, two thousand twenty, at seventy-eight.",
    dict(type="big", kicker="FEBRUARY 2, 2020", lines=["Died at 78.", "After 13|years."], src=SRC_WLBT + " · " + SRC_GL),
    show="He died on February 2, 2020, at 78."),
  END]},
]
from panfix import fix
for s in shorts: fix(s["lines"], "short")
for i, s in enumerate(shorts, 1):
    s["label"] = "SWORN"
    json.dump(s, open(os.path.join(HERE, f"short{i}.json"), "w"), indent=1, ensure_ascii=False)
    print(i, len(s["title"]), sum(len(l["say"].split()) for l in s["lines"]), "words", len(s["lines"]), "lines")
