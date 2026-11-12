import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
def hl(name, i=0):
    a, b = HL[name][i]
    return [0.0, a, 1.0, round(b - a, 4)]
CASE = "KELLY v. UNITED STATES"
SRC_OP = "Kelly v. United States, No. 18-1059, opinion of the Court (Kagan, J.) (U.S. May 7, 2020)"
SRC_USB = "Brief for the United States, Kelly v. United States, No. 18-1059 (U.S. Nov 22, 2019)"
SRC_JA = "Joint Appendix, Kelly v. United States, No. 18-1059"
SRC_JI = "Final jury instructions, U.S. v. Baroni & Kelly, No. 2:15-cr-193 (D.N.J.), J.A. 863"
SRC_Q4 = "Jury Communication #4 and court response, U.S. v. Baroni & Kelly (D.N.J., Nov 1, 2016), J.A. 905"
SRC_SENT = "Sentencing transcript, U.S. v. Baroni & Kelly (D.N.J., Mar 29, 2017), J.A. 906–916"
SRC_GX = "Gov't Exhibit 145, U.S. v. Baroni & Kelly (D.N.J.), J.A. 917"
SRC_DOJV = "U.S. Attorney's Office, D.N.J., press release (Nov 4, 2016)"
SRC_DOJS = "U.S. Attorney's Office, D.N.J., press release (Mar 29, 2017)"
SRC_DOJW = "U.S. Attorney's Office, D.N.J., press release (Jul 12, 2017)"
SRC_DOJK = "U.S. Attorney's Office, D.N.J., press release (Apr 24, 2019)"
SRC_CRS1 = "Congressional Research Service, LSB10326 (May 8, 2020)"
SRC_CRS2 = "Congressional Research Service, LSB11025 (Jan 9, 2026)"
SRC_DKT = "Supreme Court docket No. 18-1059"
SRC_AP = "Associated Press (May 7, 2020)"
SRC_AP2 = "Associated Press (Jun 13, 2020)"
SRC_CNBC = "CNBC (May 7, 2020)"
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
def doc(img, kicker, title, src, i=0, pan=None):
    return dict(type="doc", img=f"img/{img}.jpg", pan=pan or [0.0, 0.1], hl=hl(img, i), kicker=kicker, title=title, src=src)
lines = [
 # COLD OPEN
 L("Why did the Supreme Court throw out the Bridgegate convictions? Because, a unanimous Court ruled, the scheme was not aimed at money or property. And federal fraud law requires that it is.",
   dict(type="big", kicker="KELLY v. UNITED STATES · MAY 7, 2020", lines=["Not money.", "Not|property."], src=SRC_OP)),
 L("It started with one line, sent in August twenty thirteen by a deputy chief of staff to New Jersey's governor: Time for some traffic problems in Fort Lee.",
   dict(type="quote", q="Time for some traffic problems in Fort Lee.", case=CASE, doc="E-MAIL · BRIDGET ANNE KELLY · AUG 13, 2013", cite="Quoted in " + SRC_OP + " · " + SRC_GX, size=60),
   show="It started with one line, sent in August 2013 by a deputy chief of staff to New Jersey's governor: \"Time for some traffic problems in Fort Lee.\""),
 L("Four days of gridlock followed. A jury convicted her and a Port Authority executive on every count. And then nine justices, without a single dissent, reversed it.",
   dict(type="title", kicker="SWORN · CASE 012 · THE ARGUMENT", title="Traffic Problems|in Fort Lee", sub="Kelly v. United States · Supreme Court · 2020")),
 # I
 L("Chapter one. The bridge.", dict(type="chapter", n="I", title="The Bridge")),
 L("The George Washington Bridge connects Fort Lee, New Jersey, to New York City. With up to three hundred thousand vehicles a day, the government's brief calls it the busiest motor-vehicle bridge in the world.",
   doc("usb_bridge", "BRIEF FOR THE UNITED STATES · PAGE 3", "“the busiest motor-vehicle bridge in the world”", SRC_USB, 0),
   show="The George Washington Bridge connects Fort Lee, New Jersey, to New York City. With up to 300,000 vehicles a day, the government's brief calls it \"the busiest motor-vehicle bridge in the world.\""),
 L("It is run by the Port Authority of New York and New Jersey. On the upper level, twelve lanes and toll booths. During the morning rush hour, Port Authority police set out cones to reserve three of them for traffic entering from the streets of Fort Lee.",
   doc("usb_bridge", "BRIEF FOR THE UNITED STATES", "Twelve lanes. Three for Fort Lee.", SRC_USB, 1),
   show="It is run by the Port Authority of New York and New Jersey. On the upper level, 12 lanes and toll booths. During the morning rush hour, Port Authority police set out cones to reserve three of them for traffic entering from the streets of Fort Lee."),
 L("Those three lanes carry not only Fort Lee commuters, but thousands of drivers from other towns who cut through Fort Lee to reach the bridge. Roughly a quarter of the upper-level traffic.",
   doc("usb_bridge", "BRIEF FOR THE UNITED STATES", "Three lanes, about 25% of the traffic", SRC_USB, 1),
   show="Those three lanes carry not only Fort Lee commuters, but thousands of drivers from other towns who \"cut through Fort Lee\" to reach the bridge. Roughly a quarter of the upper-level traffic."),
 L("Two officials are at the center of this case. Bridget Anne Kelly, deputy chief of staff to New Jersey Governor Chris Christie. And Bill Baroni, the Port Authority's deputy executive director.",
   doc("usb_stmt", "BRIEF FOR THE UNITED STATES · STATEMENT", "Kelly and Baroni", SRC_USB, 3),
   show="Two officials are at the center of this case. Bridget Anne Kelly, deputy chief of staff to New Jersey Governor Chris Christie. And Bill Baroni, the Port Authority's deputy executive director."),
 L("In twenty thirteen, the governor was running for re-election. Fort Lee's mayor, Mark Sokolich, told Kelly's office he would not back the governor's campaign.",
   dict(type="big", kicker="FORT LEE, NEW JERSEY · 2013", lines=["No", "endorsement."], src=SRC_OP),
   show="In 2013, the governor was running for re-election. Fort Lee's mayor, Mark Sokolich, told Kelly's office he would not back the governor's campaign."),
 L("According to the government, Kelly wanted to punish the mayor for that. And she, Baroni and a third Port Authority official, David Wildstein, settled on a way to do it.",
   doc("usb_lie", "BRIEF FOR THE UNITED STATES", "“Kelly wanted to punish Fort Lee's mayor”", SRC_USB, 0),
   show="According to the government, Kelly wanted to punish the mayor for that. And she, Baroni and a third Port Authority official, David Wildstein, settled on a way to do it."),
 L("The plan, in the government's words: create as big a traffic jam as possible in Fort Lee.",
   doc("usb_bridge", "BRIEF FOR THE UNITED STATES · PAGE 3", "“create as big a traffic jam as possible”", SRC_USB, 1),
   show="The plan, in the government's words: \"create as big a traffic jam as possible\" in Fort Lee."),
 # II
 L("Chapter two. The cover story.", dict(type="chapter", n="II", title="The Cover Story")),
 L("On August thirteenth, twenty thirteen, at seven thirty-four in the morning, Kelly e-mailed Wildstein from a personal account. Time for some traffic problems in Fort Lee.",
   dict(type="quote", q="Time for some traffic problems in Fort Lee.", case=CASE, doc="GOV'T EXHIBIT 145 · AUG 13, 2013 · 7:34 AM", cite=SRC_GX, size=60),
   show="On August 13, 2013, at 7:34 in the morning, Kelly e-mailed Wildstein from a personal account: \"Time for some traffic problems in Fort Lee.\""),
 L("One minute later, Wildstein answered. Two words. Got it.",
   dict(type="quote", q="Got it", case=CASE, doc="GOV'T EXHIBIT 145 · AUG 13, 2013 · 7:35 AM", cite=SRC_GX, size=72),
   show="One minute later, Wildstein answered. Two words: \"Got it.\""),
 L("There was a problem. As deputy executive director, the appeals court found, Baroni lacked the authority to realign the bridge's traffic on his own. And he could not give his real reason.",
   doc("usb_lie", "BRIEF FOR THE UNITED STATES · PAGE 4", "“Baroni lacked the authority”", SRC_USB, 0),
   show="There was a problem. As deputy executive director, the appeals court found, Baroni \"lacked the authority to realign the bridge's traffic patterns unilaterally.\" And he could not give his real reason."),
 L("So, the government says, they needed to lie. Wildstein suggested a cover: a traffic study.",
   doc("usb_lie", "BRIEF FOR THE UNITED STATES", "“needed to lie to realign the traffic patterns”", SRC_USB, 1),
   show="So, the government says, they \"needed to lie.\" Wildstein suggested a cover: a traffic study."),
 L("The courts called that study a sham. The Port Authority's executive director later testified: there was no study.",
   doc("usb_lie", "BRIEF FOR THE UNITED STATES", "“there was no study”", SRC_USB, 2),
   show="The courts called that study a \"sham.\" The Port Authority's executive director later testified: \"there was no study.\""),
 L("With only one Fort Lee lane open, the Port Authority needed an extra toll collector on relief duty, at overtime rates. According to the government, the three of them joked about it.",
   doc("usb_toll", "BRIEF FOR THE UNITED STATES · PAGE 6", "An extra toll collector, at overtime", SRC_USB, 0)),
 L("They joked, the brief says, that the Port Authority would have to pay a second toll collector to sit and wait in case the first toll collector had to go to the bathroom.",
   doc("usb_toll", "BRIEF FOR THE UNITED STATES · PAGE 6", "“they ‘joked about’ the fact”", SRC_USB, 1),
   show="They joked, the brief says, that the Port Authority would have to \"pay a second toll collector to sit and wait in case the first toll collector had to go to the bathroom.\""),
 # III
 L("Chapter three. Four days.", dict(type="chapter", n="III", title="Four Days")),
 L("They picked the date to maximize the impact, the government says. Monday, September ninth, twenty thirteen. The first day of school. And no warning to Fort Lee.",
   doc("usb_toll", "BRIEF FOR THE UNITED STATES · PAGE 6", "Monday, September 9, 2013 — “the first day of school”", SRC_USB, 2),
   show="They picked the date to \"maximize the impact,\" the government says. Monday, September 9, 2013. The first day of school. And no warning to Fort Lee."),
 L("Three local lanes became one. The result, a witness told the jury, was concrete gridlock.",
   doc("usb_grid", "BRIEF FOR THE UNITED STATES · PAGE 7", "“concrete gridlock”", SRC_USB, 0),
   show="Three local lanes became one. The result, a witness told the jury, was \"concrete gridlock.\""),
 L("Fort Lee's chief of police testified it was the worst traffic the town had dealt with, except for nine eleven.",
   doc("usb_grid", "BRIEF FOR THE UNITED STATES · PAGE 7", "“except for 9/11”", SRC_USB, 1),
   show="Fort Lee's chief of police testified it was \"the wors[t] traffic [Fort Lee] had to deal with, except for 9/11.\""),
 L("First responders were slowed on their way to two emergencies: a missing four-year-old child, and a cardiac arrest.",
   doc("usb_grid", "BRIEF FOR THE UNITED STATES · PAGE 7", "“a missing four-year old child” · “cardiac arrest”", SRC_USB, 2)),
 L("The mayor called Baroni about an urgent matter of public safety. The plan, the government says, was radio silence. Baroni did not call back.",
   dict(type="big", kicker="SEPTEMBER 9–12, 2013", lines=["Radio", "silence."], src=SRC_USB)),
 L("When Wildstein forwarded Kelly a text from the mayor about a problem getting kids to school, Kelly wrote back:",
   doc("usb_smile", "BRIEF FOR THE UNITED STATES · PAGE 8", "Kelly's reply", SRC_USB, 0)),
 L("Is it wrong that I'm smiling?",
   dict(type="quote", q="Is it wrong that I'm smiling?", case=CASE, doc="TEXT MESSAGE · BRIDGET ANNE KELLY · SEPT 2013", cite="As quoted in " + SRC_USB + ", J.A. 753", size=64),
   show="\"Is it wrong that I'm smiling?\""),
 L("At trial, Kelly explained that she was happy for Wildstein that his traffic study was going well. The judge would later say that did not make a lot of sense.",
   dict(type="quote", q="And that just really did not make a lot of sense, quite frankly.", case=CASE, doc="U.S. DISTRICT JUDGE SUSAN D. WIGENTON · AT SENTENCING", cite=SRC_SENT, size=46)),
 L("The jams lasted four days, until the Port Authority's executive director learned what was happening, through a question from the press, and reversed the lane closures.",
   doc("usb_smile", "BRIEF FOR THE UNITED STATES · PAGE 8", "“The traffic jams continued for four days.”", SRC_USB, 1),
   show="The jams lasted four days, until the Port Authority's executive director learned what was happening, through a question from the press, and reversed the lane closures."),
 # IV
 L("He vowed to get to the bottom of what he called an abuse. Baroni asked him twice to put the lane reductions back. The executive director refused.",
   doc("usb_smile", "BRIEF FOR THE UNITED STATES · PAGE 8", "Baroni asked twice. Refused.", SRC_USB, 1)),
 L("Two months later, in November twenty thirteen, Baroni told a New Jersey Assembly committee the lane changes were part of a traffic study. The judge would later find the committee was misled.",
   dict(type="quote", q="the Assembly Transportation Committee was also misled when Mr. Baroni asserted and maintained that the traffic study was legitimate, knowing that it was not.", case=CASE, doc="U.S. DISTRICT JUDGE SUSAN D. WIGENTON · AT SENTENCING", cite=SRC_SENT, size=40),
   show="Two months later, in November 2013, Baroni told a New Jersey Assembly committee the lane changes were part of a traffic study. The judge would later find the committee \"was also misled.\""),
 L("Chapter four. The verdict.", dict(type="chapter", n="IV", title="The Verdict")),
 L("In twenty fifteen, a federal grand jury in New Jersey indicted Baroni and Kelly. Wildstein pleaded guilty to two conspiracy counts and became the government's cooperating witness.",
   dict(type="timeline", kicker="UNITED STATES v. BARONI & KELLY", events=[{"date": "Sept 2013", "text": "Four days of gridlock"}, {"date": "2015", "text": "Indictment; Wildstein pleads guilty"}, {"date": "Sept 2016", "text": "Trial begins in Newark"}, {"date": "Nov 4, 2016", "text": "Verdict"}], at=1, src=SRC_DOJV + " · " + SRC_DOJW),
   show="In 2015, a federal grand jury in New Jersey indicted Baroni and Kelly. Wildstein pleaded guilty to two conspiracy counts and became the government's cooperating witness."),
 L("The charges: wire fraud, fraud involving property of an organization that receives federal funds, conspiracy, and civil-rights counts. Seven counts each.",
   doc("usb_stmt", "BRIEF FOR THE UNITED STATES · STATEMENT", "The counts", SRC_USB, 0)),
 L("The trial in Newark lasted six weeks. The judge told the jury that motive is not an element of the offense. Proof of bad motive is not required to convict.",
   doc("ja_motive", "FINAL JURY INSTRUCTIONS · J.A. 863", "“Motive is not an element of the offense”", SRC_JI, 0),
   show="The trial in Newark lasted six weeks. The judge told the jury that \"motive is not an element of the offense.\" \"Proof of bad motive is not required to convict.\""),
 L("The jury was also told that an honest belief that the study was legitimate would be a complete defense. The jury rejected that defense.",
   doc("usb_14", "BRIEF FOR THE UNITED STATES · PAGE 20", "“a complete defense”", SRC_USB, 0)),
 L("On November first, twenty sixteen, the jury sent out a question. Can you be guilty of conspiracy without the act being intentionally punitive toward Mayor Sokolich? The judge answered: Yes.",
   doc("ja_q4", "U.S. DISTRICT COURT · JURY COMMUNICATION #4", "The jury's question", SRC_Q4, 0),
   show="On November 1, 2016, the jury sent out a question: \"Can you be guilty of Conspiracy without the act being intentionally punitive toward Mayor Sokolich.\" The judge answered: \"Yes.\""),
 L("Three days later, on November fourth, after less than four days of deliberations, the verdict. Guilty, on all seven counts, for both.",
   dict(type="verdict", kicker="NEWARK · NOVEMBER 4, 2016", stamp="GUILTY", big="All 7 counts", sub="William E. Baroni Jr. · Bridget Anne Kelly"),
   show="Three days later, on November 4, after less than four days of deliberations, the verdict. Guilty, on all seven counts, for both."),
 L("At sentencing, in March twenty seventeen, Judge Susan Wigenton said: there never was a legitimate traffic study.",
   dict(type="quote", q="there never was a legitimate traffic study.", case=CASE, doc="U.S. DISTRICT JUDGE SUSAN D. WIGENTON · MARCH 29, 2017", cite=SRC_SENT, size=56),
   show="At sentencing, in March 2017, Judge Susan Wigenton said: \"there never was a legitimate traffic study.\""),
 L("People, she said, needlessly suffered because of political payback and misuse of the resources of the Port Authority.",
   dict(type="quote", q="needlessly suffered because of political payback and misuse of the resources of the Port Authority.", case=CASE, doc="U.S. DISTRICT JUDGE SUSAN D. WIGENTON · AT SENTENCING", cite=SRC_SENT, size=44),
   show="People, she said, \"needlessly suffered because of political payback and misuse of the resources of the Port Authority.\""),
 L("Baroni got twenty-four months in prison. Kelly got eighteen. Wildstein, who cooperated, got probation.",
   dict(type="bars", kicker="SENTENCES · 2017", title="Months in prison", items=[{"label": "Bill Baroni", "value": 24, "display": "24 months"}, {"label": "Bridget Kelly", "value": 18, "display": "18 months"}, {"label": "David Wildstein", "value": 0.4, "display": "Probation"}], src=SRC_DOJS + " · " + SRC_DOJW),
   show="Baroni got 24 months in prison. Kelly got 18. Wildstein, who cooperated, got probation."),
 L("For Kelly, the judge noted, the guidelines called for thirty-seven to forty-six months. She went below that range.",
   dict(type="bars", kicker="BRIDGET ANNE KELLY · MARCH 29, 2017", title="Guidelines vs. sentence", items=[{"label": "Guidelines, low end", "value": 37, "display": "37 months"}, {"label": "Guidelines, high end", "value": 46, "display": "46 months"}, {"label": "Sentence", "value": 18, "display": "18 months"}], src=SRC_SENT + " · " + SRC_DOJS),
   show="For Kelly, the judge noted, the guidelines called for 37 to 46 months. She went below that range."),
 L("On appeal, the Third Circuit threw out the civil-rights convictions, but upheld the fraud counts. Baroni was resentenced to eighteen months, and Kelly to thirteen.",
   doc("usb_stmt", "BRIEF FOR THE UNITED STATES · STATEMENT", "Resentenced: 13 and 18 months", SRC_USB, 2),
   show="On appeal, the Third Circuit threw out the civil-rights convictions, but upheld the fraud counts. Baroni was resentenced to 18 months, and Kelly to 13."),
 # V
 L("Chapter five. The argument.", dict(type="chapter", n="V", title="The Argument")),
 L("Baroni had begun serving his sentence. Kelly was weeks from starting hers when, in June twenty nineteen, the Supreme Court agreed to hear her case.",
   dict(type="big", kicker="SUPREME COURT · JUNE 28, 2019", lines=["Petition", "granted."], src=SRC_DKT + " · " + SRC_AP),
   show="Baroni had begun serving his sentence. Kelly was weeks from starting hers when, in June 2019, the Supreme Court agreed to hear her case."),
 L("The question was not whether the scheme happened. It was whether it was fraud. The federal fraud laws in this case cover schemes to obtain money or property. So what property did Kelly and Baroni take?",
   doc("crs1_top", "CONGRESSIONAL RESEARCH SERVICE · LEGAL SIDEBAR", "Money or property?", SRC_CRS1, 0),
   show="The question was not whether the scheme happened. It was whether it was fraud. The federal fraud laws in this case cover schemes to obtain money or property. So what property did Kelly and Baroni take?"),
 L("The government's answer: they lied about a traffic study that did not exist, to take control of Port Authority resources they could not otherwise have ordered.",
   doc("usb_soa", "BRIEF FOR THE UNITED STATES · SUMMARY OF ARGUMENT", "“to hijack Port Authority resources”", SRC_USB, 0)),
 L("Concretely, the work of fourteen public employees. Eleven toll collectors paid overtime, and three professional staff members.",
   doc("usb_14", "BRIEF FOR THE UNITED STATES · PAGE 20", "“fourteen public employees”", SRC_USB, 2)),
 L("Payroll records put the toll collectors' extra shifts at three thousand six hundred ninety-six dollars and nine cents.",
   doc("usb_cost", "BRIEF FOR THE UNITED STATES · PAGE 18", "$3,696.09", SRC_USB, 0),
   show="Payroll records put the toll collectors' extra shifts at $3,696.09."),
 L("Kelly's side answered with a snowplow. If her conviction stood, her petition argued, an official who decides which snow-closed streets to plow first for unannounced political reasons could be committing federal fraud.",
   doc("crs1_pet", "CONGRESSIONAL RESEARCH SERVICE · ON KELLY'S PETITION", "The snowplow argument", SRC_CRS1, 0)),
 L("The appeals court's theory, the petition said, was a playbook for how to prosecute political adversaries.",
   doc("crs1_pet", "CONGRESSIONAL RESEARCH SERVICE · QUOTING KELLY'S PETITION", "“a playbook for how to prosecute political adversaries”", SRC_CRS1, 1),
   show="The appeals court's theory, the petition said, was \"a playbook for how to prosecute political adversaries.\""),
 L("The government replied that this case was different: Kelly and Baroni were not convicted for hiding a political motive, but for lying about a study that did not exist.",
   doc("usb_14", "BRIEF FOR THE UNITED STATES", "“politically motivated” — the appeals court", SRC_USB, 1)),
 L("The justices heard the case on January fourteenth, twenty twenty.",
   dict(type="stat", kicker="SUPREME COURT · No. 18-1059", value="Jan 14, 2020", label="Argued", src=SRC_DKT),
   show="The justices heard the case on January 14, 2020."),
 # VI
 L("Chapter six. Nine to nothing.", dict(type="chapter", n="VI", title="Nine to Nothing")),
 L("On May seventh, twenty twenty, Justice Elena Kagan wrote for a unanimous Court. She did not excuse what happened.",
   dict(type="stat", kicker="MAY 7, 2020", value="9–0", label="Opinion by Justice Elena Kagan", src=SRC_DKT),
   show="On May 7, 2020, Justice Elena Kagan wrote for a unanimous Court. She did not excuse what happened."),
 L("The evidence the jury heard no doubt shows wrongdoing. Deception, corruption, abuse of power.",
   dict(type="quote", q="The evidence the jury heard no doubt shows wrongdoing—deception, corruption, abuse of power.", case=CASE, doc="OPINION OF THE COURT · PAGE 2", cite=SRC_OP, size=50),
   show="\"The evidence the jury heard no doubt shows wrongdoing—deception, corruption, abuse of power.\""),
 L("But the federal fraud statutes at issue do not criminalize all such conduct.",
   dict(type="quote", q="But the federal fraud statutes at issue do not criminalize all such conduct.", case=CASE, doc="OPINION OF THE COURT · PAGE 2", cite=SRC_OP, size=52),
   show="\"But the federal fraud statutes at issue do not criminalize all such conduct.\""),
 L("The lanes, the Court said, were not property taken from the Port Authority. Changing who gets which lanes was a quintessential exercise of regulatory power.",
   dict(type="quote", q="But that realignment was a quintessential exercise of regulatory power.", case=CASE, doc="OPINION OF THE COURT · PAGE 8", cite=SRC_OP, size=52),
   show="The lanes, the Court said, were not property taken from the Port Authority. Changing who gets which lanes was \"a quintessential exercise of regulatory power.\""),
 L("And the employees' time? The scheme was not aimed at it. The cost of those hours, Kagan wrote, was its incidental byproduct.",
   dict(type="quote", q="The cost of the employee hours spent on implementing that plan was its incidental byproduct.", case=CASE, doc="OPINION OF THE COURT · PAGE 12", cite=SRC_OP, size=48),
   show="And the employees' time? The scheme was not aimed at it. \"The cost of the employee hours spent on implementing that plan was its incidental byproduct,\" Kagan wrote."),
 L("For no reason other than political payback, the opinion says, Baroni and Kelly used deception to reduce Fort Lee's access lanes. But not every corrupt act by state or local officials is a federal crime.",
   dict(type="quote", q="But not every corrupt act by state or local officials is a federal crime.", case=CASE, doc="OPINION OF THE COURT · PAGE 13", cite=SRC_OP, size=52),
   show="\"For no reason other than political payback, Baroni and Kelly used deception to reduce Fort Lee's access lanes.\" \"But not every corrupt act by state or local officials is a federal crime.\""),
 L("Federal prosecutors, the Court said, may not use property fraud statutes to set standards of disclosure and good government for local and state officials.",
   dict(type="quote", q="Federal prosecutors may not use property fraud statutes to “set[] standards of disclosure and good government for local and state officials.”", case=CASE, doc="OPINION OF THE COURT · PAGE 12", cite=SRC_OP + " · as quoted in " + SRC_CRS1, size=42),
   show="Federal prosecutors, the Court said, \"may not use property fraud statutes to 'set[] standards of disclosure and good government for local and state officials.'\""),
 L("Judgment reversed.",
   dict(type="verdict", kicker="SUPREME COURT · MAY 7, 2020", stamp="REVERSED", big="9–0", sub="Kelly v. United States · No. 18-1059", neutral=True)),
 L("In June twenty twenty, a federal judge dismissed the indictments, and vacated Wildstein's conviction too. Wildstein wrote that the conduct by me and others was still wrong.",
   dict(type="quote", q="the conduct by me and others was still wrong.", case=CASE, doc="DAVID WILDSTEIN · JUNE 2020", cite="As quoted by " + SRC_AP2, size=54),
   show="In June 2020, a federal judge dismissed the indictments, and vacated Wildstein's conviction too. Wildstein wrote that \"the conduct by me and others was still wrong.\""),
 L("Kelly said the ruling gave me back my name. Governor Christie was never charged, and has denied knowing about the plan.",
   dict(type="quote", q="gave me back my name", case=CASE, doc="BRIDGET ANNE KELLY · MAY 7, 2020", cite="As quoted by " + SRC_CNBC + " · " + SRC_AP2, size=64),
   show="Kelly said the ruling \"gave me back my name.\" Governor Christie was never charged, and has denied knowing about the plan."),
 L("The line Kelly drew did not stay in Fort Lee. In twenty twenty-three, the Court reversed two more wire-fraud convictions, in Ciminelli and Percoco. In twenty twenty-five, in Kousisis, it upheld one.",
   doc("crs2_lim", "CONGRESSIONAL RESEARCH SERVICE · JANUARY 2026", "After Kelly: Ciminelli, Percoco, Kousisis", SRC_CRS2, 0),
   show="The line Kelly drew did not stay in Fort Lee. In 2023, the Court reversed two more wire-fraud convictions, in Ciminelli and Percoco. In 2025, in Kousisis, it upheld one."),
 L("So the answer to the question is simple, and uncomfortable. The jury was right about what happened. The Supreme Court ruled it still was not federal fraud.",
   dict(type="big", lines=["Wrongdoing.", "Not federal|fraud."], src=SRC_OP)),
 L("This is SWORN. Real trials. Real evidence. The verdict.", dict(type="end")),
]

# --- Fact-check FIXes (factcheck.md, independent agent, 13 fixes) ---
def setline(prefix, say=None, show=None, scene=None):
    m = [l for l in lines if l["say"].startswith(prefix)]
    assert len(m) == 1, prefix
    l = m[0]
    if say: l["say"] = say
    if show: l["show"] = show
    if scene: l["scene"].update(scene)
setline("Why did the Supreme Court throw out", say="Why did the Supreme Court throw out the Bridgegate convictions? Because, a unanimous Court ruled, the scheme was not aimed at money or property. And the federal fraud laws they were convicted under require that it is.")
setline("It is run by the Port Authority", scene={"hl": [0.0, 0.4228, 1.0, 0.1099], "pan": [0.179, 0.239]})
setline("Those three lanes carry", scene={"hl": [0.0, 0.5746, 1.0, 0.091], "pan": [0.321, 0.381]})
setline("The plan, in the government's words", say="The plan, according to the government: create as big a traffic jam as possible in Fort Lee.", show="The plan, according to the government: to \"create as big a traffic jam as possible\" in Fort Lee.")
setline("There was a problem.", scene={"hl": [0.0, 0.1958, 1.0, 0.0537], "pan": [0.0, 0.05]})
setline("The courts called that study a sham", say="The appeals court called that study a sham. The Port Authority's executive director later testified: there was no study.", show="The appeals court called that study a \"sham.\" The Port Authority's executive director later testified: \"there was no study.\"")
setline("He vowed", scene={"hl": [0.0, 0.6125, 1.0, 0.1099], "pan": [0.369, 0.429]})
setline("The jury was also told", scene={"hl": [0.0, 0.1391, 1.0, 0.072]})
setline("For no reason other than political payback", show="\"For no reason other than political payback, Baroni and Kelly used deception to reduce Fort Lee's access lanes . . . .\" \"But not every corrupt act by state or local officials is a federal crime.\"")
setline("The line Kelly drew", say="The line drawn in Kelly did not stay in Fort Lee. In twenty twenty-three, the Court reversed two more wire-fraud convictions, in Ciminelli and Percoco. In twenty twenty-five, in Kousisis, it upheld wire-fraud convictions.", show="The line drawn in Kelly did not stay in Fort Lee. In 2023, the Court reversed two more wire-fraud convictions, in Ciminelli and Percoco. In 2025, in Kousisis, it upheld wire-fraud convictions.")
setline("So the answer to the question", say="So the answer to the question is simple, and uncomfortable. The Court said the evidence no doubt showed wrongdoing. And it ruled that this still was not federal fraud.")
from panfix import fix
fix(lines, "long")
spec = {"label": "SWORN · CASE 012", "lines": lines}
if __name__ == "__main__":
    json.dump(spec, open(os.path.join(HERE, "episode.json"), "w"), indent=1, ensure_ascii=False)
    print(len(lines), "lines,", sum(len(l["say"].split()) for l in lines), "words")
