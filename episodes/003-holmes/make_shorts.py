import json
CASE = "U.S. v. HOLMES"
SRC_VF = "Final verdict form, Jan 3, 2022"
SRC_MEMO = "Gov't sentencing memorandum, Nov 11, 2022"
SRC_CA9 = "9th Cir., No. 22-10312"
SRC_SO = "Order on sentencing, Jan 10, 2023"
SRC_RS = "Order, N.D. Cal., Mar 26, 2026"
SRC_REST = "Order on restitution, May 16, 2023"
SRC_JUDG = "Judgment, N.D. Cal., Jan 11, 2023"
SRC_TSI = "Third Superseding Indictment, Jul 28, 2020"
SRC_FORBES = "Forbes, Sept 24, 2026"
MEMOQ = "As quoted in the gov't sentencing memorandum"
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
END = L("Real trials. Real evidence. The verdict.", dict(type="end"))
shorts = [
 {"title": "Guilty on Investors, Not Guilty on Patients: The Elizabeth Holmes Verdict", "hook": "Guilty. Not guilty.|Same defendant.", "lines": [
  L("January third, two thousand twenty-two. The jury in the Elizabeth Holmes trial fills out its verdict form.",
    dict(type="doc", img="img/verdict1.jpg", pan=[0.1, 0.2], hl=[0.0, 0.24, 1.0, 0.12], kicker="JANUARY 3, 2022", src=SRC_VF),
    show="January 3, 2022. The jury in the Elizabeth Holmes trial fills out its verdict form."),
  L("Count one, conspiracy to defraud Theranos investors. Guilty.",
    dict(type="doc", img="img/verdict1.jpg", pan=[0.3, 0.38], hl=[0.0, 0.50, 1.0, 0.115], kicker="COUNT ONE · INVESTORS", src=SRC_VF)),
  L("Count two, conspiracy to defraud Theranos patients. Not guilty.",
    dict(type="doc", img="img/verdict1.jpg", pan=[0.38, 0.44], hl=[0.0, 0.615, 1.0, 0.105], kicker="COUNT TWO · PATIENTS", src=SRC_VF)),
  L("Three more investor counts: guilty. Every patient count that reached the jury: not guilty. On three counts, it could not agree.",
    dict(type="doc", img="img/verdict2.jpg", pan=[0.22, 0.32], hl=[0.0, 0.48, 1.0, 0.45], kicker="COUNTS 6–8 · INVESTORS", src=SRC_VF)),
  L("So her convictions are about one thing: what she told the people who funded Theranos.",
    dict(type="big", kicker="THE CONVICTIONS", lines=["Not the patients.", "The investors."], src=SRC_JUDG)),
  L("The sentence: eleven years and three months, later cut to one hundred twenty-three months.",
    dict(type="verdict", kicker="NOV 18, 2022 · CUT MARCH 2026", stamp="SENTENCED", big="135 → 123 mos", sub="Elizabeth A. Holmes"),
    show="The sentence: 11 years and 3 months, later cut to 123 months."),
  END]},
 {"title": "She Put Pfizer's Logo on Her Own Report — Elizabeth Holmes at Trial", "hook": "Whose logo|was that?", "lines": [
  L("April two thousand ten. Theranos is courting Walgreens.",
    dict(type="big", kicker="APRIL 2010", lines=["Theranos courts", "Walgreens."], src=SRC_MEMO),
    show="April 2010. Theranos is courting Walgreens."),
  L("Prosecutors said Elizabeth Holmes emailed Walgreens executives reports with favorable conclusions about Theranos, bearing the logos of Pfizer, GlaxoSmithKline and Schering-Plough.",
    dict(type="doc", img="img/memo_logos.jpg", pan=[0.22, 0.32], hl=[0.0, 0.37, 1.0, 0.39], kicker="PER PROSECUTORS", src=SRC_MEMO)),
  L("She described them as three independent due diligence reports from those companies.",
    dict(type="quote", q="three independent due diligence reports on Theranos systems", case=CASE, doc="HOLMES'S EMAIL · 2010", cite=MEMOQ, size=50)),
  L("At trial, she admitted that she put the logos on herself.",
    dict(type="big", kicker="AT TRIAL · PER THE NINTH CIRCUIT", lines=["She added", "the logos."], src=SRC_CA9)),
  L("Witnesses from the drug companies testified they never validated the technology, and never authorized their logos.",
    dict(type="big", kicker="PER THE NINTH CIRCUIT", lines=["Not validated.", "Not authorized."], src=SRC_CA9)),
  L("Prosecutors said she kept sending the Pfizer report to investors in two thousand fourteen and two thousand fifteen. She was convicted of defrauding investors.",
    dict(type="verdict", kicker="JANUARY 3, 2022", stamp="GUILTY", big="4 counts", sub="Investor fraud · United States v. Holmes"),
    show="Prosecutors said she kept sending the Pfizer report to investors in 2014 and 2015. She was convicted of defrauding investors."),
  END]},
 {"title": "$0 Revenue, a $1 Billion Projection: Inside the Theranos Pitch", "hook": "$0 revenue.|$1B projected.", "lines": [
  L("According to prosecutors, Theranos had zero revenue in two thousand twelve and two thousand thirteen.",
    dict(type="doc", img="img/memo_twelve.jpg", pan=[0.35, 0.42], hl=[0.0, 0.78, 1.0, 0.14], kicker="PER PROSECUTORS", src=SRC_MEMO),
    show="According to prosecutors, Theranos had zero revenue in 2012 and 2013."),
  L("Investors were shown projections of one hundred forty million dollars for two thousand fourteen, and nearly one billion for two thousand fifteen.",
    dict(type="bars", kicker="PER PROSECUTORS", items=[{"label": "2015 PROJ.", "value": 1000, "display": "~$1B"}, {"label": "2014 PROJ.", "value": 140, "display": "$140M"}, {"label": "2012–13", "value": 0, "display": "$0"}], src=SRC_MEMO),
    show="Investors were shown projections of $140 million for 2014, and nearly $1 billion for 2015."),
  L("In November two thousand thirteen, the appeals court noted, Theranos was down to fifteen million dollars in cash, spending up to two million a week.",
    dict(type="big", kicker="NOVEMBER 2013", lines=["$15 million in cash.", "Up to $2M a week|going out."], src=SRC_CA9),
    show="In November 2013, the appeals court noted, Theranos was down to $15 million in cash, spending up to $2 million a week."),
  L("One investor was told Theranos had earned over two hundred million dollars from the military and drug companies. Prosecutors said it never earned more than ten million from both.",
    dict(type="bars", kicker="PER PROSECUTORS", items=[{"label": "CLAIMED", "value": 200, "display": "$200M+"}, {"label": "ACTUAL", "value": 10, "display": "≤$10M"}], src=SRC_MEMO),
    show="One investor was told Theranos had earned over $200 million from the military and drug companies. Prosecutors said it never earned more than $10 million from both."),
  L("The judge later ordered four hundred fifty-two million dollars in restitution to investors.",
    dict(type="doc", img="img/restitution.jpg", pan=[0.32, 0.42], hl=[0.0, 0.64, 1.0, 0.06], kicker="MAY 16, 2023", src=SRC_REST),
    show="The judge later ordered $452 million in restitution to investors."),
  END]},
 {"title": "The Theranos Demo That Ran a \"Null Protocol\"", "hook": "The demo|that tested nothing.", "lines": [
  L("Theranos promised a full range of blood tests from a single drop of blood.",
    dict(type="quote", q="[O]ne tiny drop changes everything.", case=CASE, doc="THE VISION · AS QUOTED BY THE COURT", cite="9th Cir. opinion", size=54)),
  L("At demonstrations, the appeals court wrote, VIP guests were led to believe the device was running their blood.",
    dict(type="big", kicker="THE DEMOS · PER THE NINTH CIRCUIT", lines=["VIP guests.", "Their blood."], src=SRC_CA9)),
  L("In reality, it was running a null protocol, while some samples were secretly run on other companies' machines.",
    dict(type="quote", q="In reality, the device was running a “null protocol” while some of the VIP samples were surreptitiously run on third-party devices.", case=CASE, doc="NINTH CIRCUIT", cite="U.S. v. Holmes, No. 22-10312", size=38)),
  L("The indictment said the null protocol was meant to make the analyzer appear to be operating.",
    dict(type="doc", img="img/tsi_null.jpg", pan=[0.0, 0.05], hl=[0.0, 0.10, 1.0, 0.18], kicker="THE INDICTMENT", src=SRC_TSI)),
  L("According to prosecutors, the device itself could never run more than twelve types of tests.",
    dict(type="doc", img="img/memo_twelve.jpg", pan=[0.15, 0.25], hl=[0.0, 0.37, 1.0, 0.17], kicker="PER PROSECUTORS", src=SRC_MEMO),
    show="According to prosecutors, the device itself could never run more than 12 types of tests."),
  L("Elizabeth Holmes was convicted of defrauding investors.",
    dict(type="verdict", kicker="JANUARY 3, 2022", stamp="GUILTY", big="Investor fraud", sub="United States v. Elizabeth A. Holmes")),
  END]},
 {"title": "Prosecutors Wanted 15 Years. Here's What Elizabeth Holmes Got", "hook": "15 years asked.|Here's the math.", "lines": [
  L("November eighteenth, two thousand twenty-two. Elizabeth Holmes is sentenced for defrauding Theranos investors.",
    dict(type="doc", img="img/minutes.jpg", pan=[0.0, 0.1], hl=[0.0, 0.03, 1.0, 0.12], kicker="NOVEMBER 18, 2022", src="Criminal minutes, Nov 18, 2022"),
    show="November 18, 2022. Elizabeth Holmes is sentenced for defrauding Theranos investors."),
  L("Prosecutors asked for fifteen years. Probation suggested nine. Her lawyers argued for eighteen months or less.",
    dict(type="bars", kicker="THE ASKS", items=[{"label": "PROSECUTION", "value": 180, "display": "180 mos"}, {"label": "PROBATION", "value": 108, "display": "108 mos"}, {"label": "DEFENSE", "value": 18, "display": "≤18 mos"}], src="Sentencing memoranda, Nov 2022"),
    show="Prosecutors asked for 15 years. Probation suggested nine. Her lawyers argued for 18 months or less."),
  L("The judge put the loss at one hundred twenty million dollars, for a guidelines range of one hundred thirty-five to one hundred sixty-eight months.",
    dict(type="stat", kicker="LOSS FOUND BY THE COURT", value="$120.1M", label="range: 135–168 months", src=SRC_SO),
    show="The judge put the loss at $120 million, for a guidelines range of 135 to 168 months."),
  L("He chose the bottom. One hundred thirty-five months.",
    dict(type="verdict", kicker="THE SENTENCE", stamp="SENTENCED", big="135 months", sub="11 years, 3 months"),
    show="He chose the bottom. 135 months."),
  L("In March two thousand twenty-six, a guidelines change for first-time offenders let him cut it to one hundred twenty-three months.",
    dict(type="doc", img="img/resent.jpg", pan=[0.22, 0.32], hl=[0.0, 0.44, 1.0, 0.24], kicker="MARCH 26, 2026", src=SRC_RS),
    show="In March 2026, a guidelines change for first-time offenders let him cut it to 123 months."),
  END]},
 {"title": "Where Elizabeth Holmes Is Now (2026)", "hook": "Where Holmes|is now.", "lines": [
  L("Elizabeth Holmes reported to federal prison on May thirtieth, two thousand twenty-three.",
    dict(type="big", kicker="MAY 30, 2023", lines=["She reports", "to prison."], src=SRC_RS),
    show="Elizabeth Holmes reported to federal prison on May 30, 2023."),
  L("In February two thousand twenty-five, the Ninth Circuit affirmed her conviction. The vision she sold, it wrote, was nothing more than a mirage.",
    dict(type="doc", img="img/ca9.jpg", pan=[0.32, 0.42], hl=[0.0, 0.57, 1.0, 0.28], kicker="9TH CIRCUIT · AFFIRMED", src=SRC_CA9),
    show="In February 2025, the Ninth Circuit affirmed her conviction. The vision she sold, it wrote, was \"nothing more than a mirage.\""),
  L("In March two thousand twenty-six, her sentence was cut from one hundred thirty-five to one hundred twenty-three months.",
    dict(type="doc", img="img/resent.jpg", pan=[0.22, 0.32], hl=[0.0, 0.44, 1.0, 0.24], kicker="MARCH 26, 2026", src=SRC_RS),
    show="In March 2026, her sentence was cut from 135 to 123 months."),
  L("She has asked President Trump to commute her sentence. According to Forbes, as of late September the request was listed as pending.",
    dict(type="big", kicker="ACCORDING TO NEWS REPORTS", lines=["Commutation:", "pending as of|Sept. 2026."], src=SRC_FORBES)),
  L("The same report says she has been approved for a halfway house in August two thousand twenty-seven, with release scheduled for February two thousand thirty.",
    dict(type="timeline", kicker="ACCORDING TO NEWS REPORTS", events=[{"date": "AUG 2027", "text": "Halfway house"}, {"date": "FEB 2030", "text": "Scheduled release"}], at=1, src=SRC_FORBES),
    show="The same report says she has been approved for a halfway house in August 2027, with release scheduled for February 2030."),
  END]},
]
from panfix import fix
for s in shorts: fix(s["lines"], "short")
for i, s in enumerate(shorts, 1):
    s["label"] = "SWORN"
    json.dump(s, open(f"short{i}.json", "w"), indent=1, ensure_ascii=False)
    print(i, len(s["title"]), sum(len(l["say"].split()) for l in s["lines"]), "words", len(s["lines"]), "lines")
