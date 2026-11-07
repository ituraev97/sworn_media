import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
def hl(name, i=0):
    a, b = HL[name][i]
    return [0.0, a, 1.0, round(b - a, 4)]
CASE = "GIDEON v. WAINWRIGHT"
SRC_OP = "Gideon v. Wainwright, 372 U.S. 335 (Mar 18, 1963)"
SRC_REC = "Transcript of Record, Gideon v. Cochran, U.S. Supreme Court No. 155, Oct. Term 1962"
SRC_INFO = "Information, Circuit Court of Bay County, Fla., filed Jun 19, 1961 (in the Transcript of Record)"
SRC_MIN = "Bay County Circuit Court minute book, Aug 4 & Aug 25, 1961 (in the Transcript of Record)"
SRC_TRIAL = "Reporter's transcript of trial, Bay County, Aug 4, 1961 (in the Transcript of Record)"
SRC_HAB = "Gideon's petition for habeas corpus, Fla. Sup. Ct., Oct 1961 (in the Transcript of Record)"
SRC_FLO = "Florida Supreme Court, order of Oct 30, 1961 (in the Transcript of Record)"
SRC_CERT = "U.S. Supreme Court, order of Jun 4, 1962 (in the Transcript of Record)"
SRC_FLB = "Brief for the Respondent, Attorney General of Florida, No. 155 (filed Jan 1963)"
SRC_USC = "U.S. Courts, Facts and Case Summary — Gideon v. Wainwright"
SRC_JACOB = "Bruce R. Jacob, “The Gideon Trials,” 99 Iowa Law Review 2059 (2014)"
SRC_FPB = "Brief for the Petitioner, No. 155 (Arnold, Fortas & Porter, Washington, D.C.; Nov 21, 1962)"
SRC_ENC = "Encyclopedia.com, Clarence Earl Gideon Trials: 1961 & 1963"
def L(say, scene=None, show=None, **kw):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    d.update(kw); return d
def doc(img, kicker, title, src, i=0, pan=None):
    return dict(type="doc", img=f"img/{img}.jpg", pan=pan or [0.0, 0.1], hl=hl(img, i), kicker=kicker, title=title, src=src)
lines = [
 # COLD OPEN
 L("In August nineteen sixty-one, a Florida man too poor to hire a lawyer stood in front of a judge and asked for one. The judge said no.",
   doc("op_coll", "BAY COUNTY, FLORIDA · AUGUST 4, 1961", "Too poor for a lawyer", SRC_OP),
   show="In August 1961, a Florida man too poor to hire a lawyer stood in front of a judge and asked for one. The judge said no."),
 L("Under Florida law, the judge explained, he could appoint a lawyer only for a defendant charged with a capital offense. The man answered:",
   dict(type="quote", q="I am sorry, but I will have to deny your request to appoint Counsel to defend you in this case.", case=CASE, doc="JUDGE ROBERT L. McCRARY, JR.", cite="As quoted in " + SRC_OP, size=46)),
 L("The United States Supreme Court says I am entitled to be represented by Counsel.",
   dict(type="quote", q="The United States Supreme Court says I am entitled to be represented by Counsel.", case=CASE, doc="CLARENCE EARL GIDEON · AUGUST 4, 1961", cite="As quoted in " + SRC_OP, size=52)),
 L("At the time, he was wrong. The Supreme Court had never said that, not for a case like his. Nineteen months later, it did.",
   dict(type="big", kicker="MARCH 18, 1963", lines=["At the time,|he was wrong.", "Then the Court|agreed."], src=SRC_OP),
   show="At the time, he was wrong. The Supreme Court had never said that, not for a case like his. 19 months later, it did."),
 L("This is SWORN.",
   dict(type="title", kicker="SWORN · CASE 007 · THE ARGUMENT", title="Too Poor for|a Lawyer", sub="Gideon v. Wainwright · Supreme Court of the United States · 1963")),
 # I
 L("Chapter one. The poolroom.", dict(type="chapter", n="I", title="The Poolroom")),
 L("Panama City, Florida. Early on the morning of June third, nineteen sixty-one, someone broke into the Bay Harbor Poolroom. A cigarette machine and a jukebox had been broken into. Some beer and wine was gone.",
   dict(type="big", kicker="JUNE 3, 1961 · PANAMA CITY, FLORIDA", lines=["The Bay Harbor", "Poolroom."], src=SRC_TRIAL),
   show="Panama City, Florida. Early on the morning of June 3, 1961, someone broke into the Bay Harbor Poolroom. A cigarette machine and a jukebox had been broken into. Some beer and wine was gone."),
 L("That same day, Clarence Earl Gideon was arrested. He was fifty years old, with an eighth-grade education and a long criminal record, according to Bruce Jacob, the lawyer who would later argue against him.",
   dict(type="stat", kicker="CLARENCE EARL GIDEON · 1961", value="50", label="years old —|an eighth-grade education", src=SRC_JACOB),
   show="That same day, Clarence Earl Gideon was arrested. He was 50 years old, with an eighth-grade education and a long criminal record, according to Bruce Jacob, the lawyer who would later argue against him."),
 L("On June nineteenth, the state attorney filed the charge. Gideon, it said, did unlawfully and feloniously break and enter the poolroom, with intent to commit a misdemeanor: petit larceny.",
   doc("info", "THE INFORMATION · JUNE 19, 1961", "Breaking and entering", SRC_INFO),
   show="On June 19, the state attorney filed the charge. Gideon, it said, \"did unlawfully and feloniously break and enter\" the poolroom, with intent to commit a misdemeanor: petit larceny."),
 L("Breaking and entering with that intent was a felony under Florida law. It carried up to five years in prison. And under Florida practice, a man charged with it got no lawyer unless he could pay for one.",
   doc("op_syl", "THE SUPREME COURT'S SUMMARY", "A noncapital felony", SRC_OP + " · " + SRC_JACOB, 1),
   show="Breaking and entering with that intent was a felony under Florida law. It carried up to 5 years in prison. And under Florida practice, a man charged with it got no lawyer unless he could pay for one."),
 L("Gideon could not.",
   dict(type="big", lines=["Gideon", "could not."])),
 # II
 L("Chapter two. The trial.", dict(type="chapter", n="II", title="The Trial")),
 L("August fourth, nineteen sixty-one. Bay County Circuit Court, Judge Robert McCrary presiding. The judge asked whether the defendant was ready. Gideon said he was not. He had no counsel.",
   dict(type="quote", q="Your Honor, I said: I request this Court to appoint Counsel to represent me in this trial.", case=CASE, doc="CLARENCE EARL GIDEON · AUGUST 4, 1961", cite=SRC_TRIAL, size=46),
   show="August 4, 1961. Bay County Circuit Court, Judge Robert McCrary presiding. The judge asked whether the defendant was ready. Gideon said he was not. He had no counsel."),
 L("The judge denied the request, and had the reporter put it on the record: the defendant had asked for counsel, and the defendant said the Supreme Court said he was entitled to it.",
   doc("op_coll", "THE TRIAL RECORD", "“entitled to be represented”", SRC_OP)),
 L("Then the judge asked him again if he was ready. He said yes, sir. Six jurors were seated. Since the defendant had no lawyer, the judge asked them some questions on his behalf: would they give him the same fair trial they would if he had one? They said yes.",
   dict(type="big", kicker="JURY SELECTION · PER THE TRIAL TRANSCRIPT", lines=["Six jurors.", "No lawyer."], src=SRC_TRIAL)),
 L("The state's key witness was a man named Henry Cook. He testified he saw Gideon inside the poolroom at about five-thirty that morning, standing by the cigarette machine, then saw him leave by the back door, with some wine, and call a cab.",
   dict(type="big", kicker="THE STATE'S WITNESS · PER THE TRIAL TRANSCRIPT", lines=["5:30 a.m.", "By the cigarette|machine."], src=SRC_TRIAL),
   show="The state's key witness was a man named Henry Cook. He testified he saw Gideon inside the poolroom at about 5:30 that morning, standing by the cigarette machine, then saw him leave by the back door, with some wine, and call a cab."),
 L("Gideon did what he could. The Supreme Court later summed it up: he conducted his defense about as well as could be expected from a layman. He gave an opening statement, cross-examined the state's witnesses, called his own, and argued his innocence.",
   doc("op_trial", "AS THE SUPREME COURT DESCRIBED IT", "“about as well as could be expected”", SRC_OP, 0)),
 L("The jury came back the same day.",
   doc("verdict", "THE JURY'S VERDICT · AUGUST 4, 1961", "“guilty as charged”", SRC_MIN)),
 L("We, the jury, find the defendant, Clarence Earl Gideon, guilty as charged.",
   dict(type="quote", q="We, the jury, find the defendant, Clarence Earl Gideon, guilty as charged. So say we all.", case=CASE, doc="THE VERDICT · AUGUST 4, 1961", cite=SRC_MIN, size=50)),
 L("On August twenty-fifth, Judge McCrary pronounced sentence: the state prison, for a period of five years. Bruce Jacob later wrote that it was the maximum.",
   doc("sentence", "BAY COUNTY · AUGUST 25, 1961", "“a period of Five Years”", SRC_MIN + " · " + SRC_JACOB),
   show="On August 25, Judge McCrary pronounced sentence: the state prison, \"for a period of Five Years.\" Bruce Jacob later wrote that it was the maximum."),
 L("Five years in prison, for a poolroom break-in. With no lawyer.",
   dict(type="verdict", kicker="THE SENTENCE · AUGUST 25, 1961", stamp="GUILTY", big="5 years", sub="Clarence Earl Gideon · no lawyer"),
   show="5 years in prison, for a poolroom break-in. With no lawyer."),
 # III
 L("Chapter three. The petition.", dict(type="chapter", n="III", title="The Petition")),
 L("From the state prison at Raiford, Gideon petitioned the Florida Supreme Court for a writ of habeas corpus. He had apparently prepared it himself, the Supreme Court later noted.",
   dict(type="big", kicker="OCTOBER 1961 · FLORIDA STATE PRISON", lines=["No lawyer.", "His own|petition."], src=SRC_HAB + " · " + SRC_FLB + " · " + SRC_OP)),
 L("I was without funds and without an attorney. I asked this court to appoint me an attorney but they denied me that right.",
   dict(type="quote", q="I was without funds and without an attorney. I asked this court to appoint me an attorney but they denied me that right.", case=CASE, doc="GIDEON'S PETITION · OCTOBER 1961", cite=SRC_HAB, size=44)),
 L("On October thirtieth, nineteen sixty-one, the Florida Supreme Court denied it, in a single sentence, without an opinion.",
   doc("fl_order", "SUPREME COURT OF FLORIDA · OCTOBER 30, 1961", "“hereby denied”", SRC_FLO),
   show="On October 30, 1961, the Florida Supreme Court denied it, in a single sentence, without an opinion."),
 L("So he went higher. In January nineteen sixty-two, a petition from Clarence Earl Gideon reached the Supreme Court of the United States. He asked to proceed as a pauper, without paying the fees.",
   doc("rec_cover", "SUPREME COURT OF THE UNITED STATES", "Petition filed January 8, 1962", SRC_REC),
   show="So he went higher. In January 1962, a petition from Clarence Earl Gideon reached the Supreme Court of the United States. He asked to proceed as a pauper, without paying the fees."),
 L("He had a problem. Twenty years earlier, the Court had already decided this question, and decided it against him.",
   dict(type="big", kicker="THE PROBLEM", lines=["Already decided.", "In 1942."], src=SRC_OP)),
 L("The case was Betts versus Brady. Smith Betts was indicted for robbery in a Maryland state court. He told the judge he had no money for a lawyer and asked for one. He was told the county appointed lawyers for poor defendants only in murder and rape cases.",
   doc("op_betts", "BETTS v. BRADY · 1942", "Robbery, in Maryland", SRC_OP, 0),
   show="The case was Betts v. Brady. Smith Betts was indicted for robbery in a Maryland state court. He told the judge he had no money for a lawyer and asked for one. He was told the county appointed lawyers for poor defendants only in murder and rape cases."),
 L("Betts defended himself. A judge found him guilty, and sentenced him to eight years in prison.",
   doc("op_betts", "BETTS v. BRADY · 1942", "Eight years", SRC_OP, 1)),
 L("A divided Supreme Court upheld it. Appointing counsel, the majority said, is not a fundamental right, essential to a fair trial. Whether a trial without a lawyer was unfair would depend on the totality of facts in each case.",
   dict(type="quote", q="appointment of counsel is not a fundamental right, essential to a fair trial.", case="BETTS v. BRADY", doc="THE COURT · 1942", cite="As quoted in " + SRC_OP, size=54)),
 L("For twenty years, that was the rule. Then, on June fourth, nineteen sixty-two, the Court granted Gideon's petition, and added a question of its own.",
   doc("cert", "SUPREME COURT · JUNE 4, 1962", "The Court's own question", SRC_CERT),
   show="For 20 years, that was the rule. Then, on June 4, 1962, the Court granted Gideon's petition, and added a question of its own."),
 L("Should this Court's holding in Betts versus Brady be reconsidered?",
   dict(type="quote", q="Should this Court's holding in Betts v. Brady, 316 U.S. 455, be reconsidered?", case=CASE, doc="ORDER OF JUNE 4, 1962", cite=SRC_CERT, size=52),
   show="\"Should this Court's holding in Betts v. Brady, 316 U.S. 455, be reconsidered?\""),
 L("Gideon could not pay a lawyer to argue that question. So the Court appointed one: Abe Fortas, a Washington lawyer.",
   doc("op_fortas", "COUNSEL FOR THE PETITIONER", "“by appointment of the Court”", SRC_OP + " · " + SRC_FPB, 0)),
 # IV
 L("Chapter four. The argument.", dict(type="chapter", n="IV", title="The Argument")),
 L("Florida's case was argued by Bruce Jacob, an assistant attorney general. His brief asked the Court to keep Betts. If the rule changed and applied to old cases, the brief warned, it could reach prisoners already convicted.",
   doc("op_fortas", "COUNSEL FOR FLORIDA", "Bruce R. Jacob", SRC_OP, 1)),
 L("Florida's prison system had surveyed its own files. As of June thirtieth, nineteen sixty-two, it held eight thousand prisoners. Four thousand sixty-five of them had pleaded guilty with no counsel.",
   doc("fl_survey", "BRIEF FOR THE RESPONDENT · FLORIDA", "The prison survey", SRC_FLB, 0),
   show="Florida's prison system had surveyed its own files. As of June 30, 1962, it held 8,000 prisoners. 4,065 of them had pleaded guilty with no counsel."),
 L("By the brief's estimate, about sixty-five percent of the prisoners whose records were available had no lawyer in the proceedings that convicted them.",
   dict(type="stat", kicker="PER FLORIDA'S BRIEF", value="65%", label="had no lawyer, by|the state's own estimate", src=SRC_FLB),
   show="By the brief's estimate, about 65% of the prisoners whose records were available had no lawyer in the proceedings that convicted them."),
 L("The brief's warning: a decision reversing the case, if retroactive, would allow over five thousand hardened criminals in Florida to be set free.",
   doc("fl_5000", "BRIEF FOR THE RESPONDENT · FLORIDA", "“over 5,000 hardened criminals”", SRC_FLB),
   show="The brief's warning: a decision reversing the case, if retroactive, \"will allow over 5,000 hardened criminals in Florida to be set free.\""),
 L("As many as five thousand ninety-three, it said, may be eligible to be released in one mass exodus.",
   dict(type="quote", q="as many as 5,093 hardened criminals may be eligible to be released in one mass exodus in Florida alone", case=CASE, doc="FLORIDA'S BRIEF · 1963", cite=SRC_FLB, size=46),
   show="As many as 5,093, it said, \"may be eligible to be released in one mass exodus.\""),
 L("Two other states, Alabama and North Carolina, filed a brief supporting Florida. But twenty-two states filed a brief on Gideon's side, asking the Court to overrule Betts.",
   dict(type="bars", kicker="THE STATES · AS FRIENDS OF THE COURT", title="States filing briefs", items=[{"label": "FOR GIDEON", "value": 22, "display": "22"}, {"label": "FOR FLORIDA", "value": 2, "display": "2"}], src=SRC_OP),
   show="Two other states, Alabama and North Carolina, filed a brief supporting Florida. But 22 states filed a brief on Gideon's side, asking the Court to overrule Betts."),
 L("Betts, they argued, was an anachronism when handed down.",
   dict(type="quote", q="an anachronism when handed down", case=CASE, doc="22 STATES, AS FRIENDS OF THE COURT", cite="As quoted in " + SRC_OP, size=64)),
 L("On January fifteenth, nineteen sixty-three, the case was argued. Fortas for Gideon. Jacob for Florida. Lawyers for the American Civil Liberties Union and for the State of Alabama argued too.",
   doc("op_syl", "SUPREME COURT · JANUARY 15, 1963", "Argued", SRC_OP, 0),
   show="On January 15, 1963, the case was argued. Fortas for Gideon. Jacob for Florida. Lawyers for the American Civil Liberties Union and for the State of Alabama argued too."),
 # V
 L("Chapter five. The decision.", dict(type="chapter", n="V", title="The Decision")),
 L("On March eighteenth, nineteen sixty-three, the Court ruled. The opinion was written by Justice Hugo Black, who had dissented in Betts versus Brady twenty-one years before. No justice dissented this time.",
   dict(type="big", kicker="MARCH 18, 1963", lines=["Justice Hugo Black.", "No dissent."], src=SRC_OP + " · " + SRC_USC),
   show="On March 18, 1963, the Court ruled. The opinion was written by Justice Hugo Black, who had dissented in Betts v. Brady 21 years before. No justice dissented this time."),
 L("The facts of Betts and Gideon, the Court said, were so nearly indistinguishable that if Betts stood, Gideon would lose. Upon full reconsideration, we conclude that Betts versus Brady should be overruled.",
   doc("op_overrule", "THE OPINION OF THE COURT", "“should be overruled”", SRC_OP),
   show="The facts of Betts and Gideon, the Court said, were so nearly indistinguishable that if Betts stood, Gideon would lose. \"Upon full reconsideration we conclude that Betts v. Brady should be overruled.\""),
 L("In our adversary system of criminal justice, the Court wrote, any person haled into court, who is too poor to hire a lawyer, cannot be assured a fair trial unless counsel is provided for him.",
   doc("op_truth", "THE OPINION OF THE COURT", "“too poor to hire a lawyer”", SRC_OP, 0)),
 L("This seems to us to be an obvious truth.",
   dict(type="quote", q="This seems to us to be an obvious truth.", case=CASE, doc="JUSTICE HUGO BLACK · FOR THE COURT", cite=SRC_OP, size=64)),
 L("The Court went back to words written in nineteen thirty-two, in Powell versus Alabama, about what a defendant without a lawyer faces. Even an intelligent and educated layman, Justice George Sutherland had written, lacks both the skill and knowledge to prepare his defense, even though he have a perfect one.",
   doc("op_powell", "QUOTING POWELL v. ALABAMA · 1932", "“a perfect one”", SRC_OP, 0),
   show="The Court went back to words written in 1932, in Powell v. Alabama, about what a defendant without a lawyer faces. Even an intelligent and educated layman, Justice George Sutherland had written, \"lacks both the skill and knowledge adequately to prepare his defense, even though he have a perfect one.\""),
 L("He requires the guiding hand of counsel at every step in the proceedings against him.",
   dict(type="quote", q="He requires the guiding hand of counsel at every step in the proceedings against him.", case="POWELL v. ALABAMA", doc="JUSTICE GEORGE SUTHERLAND · 1932", cite="As quoted in " + SRC_OP, size=50)),
 L("Governments hire lawyers to prosecute. Defendants who have money hire lawyers to defend. Those facts, the Court said, are the strongest indications of a widespread belief: lawyers in criminal courts are necessities, not luxuries.",
   doc("op_truth", "THE OPINION OF THE COURT", "“necessities, not luxuries”", SRC_OP, 1)),
 L("And on the states' briefs: twenty-two states argue that Betts was an anachronism when handed down, and that it should now be overruled. We agree.",
   doc("op_agree", "THE OPINION OF THE COURT", "“We agree.”", SRC_OP, 0),
   show="And on the states' briefs: \"Twenty-two States, as friends of the Court, argue that Betts was 'an anachronism when handed down' and that it should now be overruled. We agree.\""),
 L("Justice John Marshall Harlan agreed Betts should go, but wrote that it deserved a more respectful burial.",
   dict(type="quote", q="I agree that Betts v. Brady should be overruled, but consider it entitled to a more respectful burial than has been accorded", case=CASE, doc="JUSTICE JOHN M. HARLAN · CONCURRING", cite=SRC_OP, size=42)),
 L("Justice Tom Clark, concurring, put it more simply. The Constitution, he wrote, makes no distinction between capital and noncapital cases.",
   dict(type="quote", q="the Constitution makes no distinction between capital and noncapital cases.", case=CASE, doc="JUSTICE TOM C. CLARK · CONCURRING IN THE RESULT", cite=SRC_OP, size=52)),
 L("The judgment against Gideon was reversed. The case went back to Florida.",
   dict(type="verdict", kicker="THE SUPREME COURT · MARCH 18, 1963", stamp="REVERSED", neutral=True, big="Betts overruled", sub="Gideon v. Wainwright, 372 U.S. 335")),
 # VI
 L("Chapter six. After the verdict.", dict(type="chapter", n="VI", title="After the Verdict")),
 L("Reversal did not set Gideon free. It meant a new trial. He was moved to the Bay County jail to be tried again, before the same judge, on the same charge.",
   dict(type="big", kicker="1963 · BAY COUNTY", lines=["Same judge.", "Same charge."], src=SRC_JACOB)),
 L("This time he had a lawyer. Gideon asked for a local lawyer named Fred Turner, and the judge appointed him.",
   dict(type="big", kicker="THE SECOND TRIAL", lines=["This time:", "a lawyer."], src=SRC_JACOB + " · " + SRC_ENC)),
 L("The retrial took place on August fifth, nineteen sixty-three. Henry Cook testified again. At the first trial, he had denied ever being convicted of a felony. Now he said he had once stolen a car and been put on probation. Turner used that prior inconsistent statement to impeach and discredit him, Jacob later wrote, though Jacob noted the earlier offense was a juvenile matter.",
   dict(type="timeline", kicker="THE RETRIAL", events=[{"date": "AUG 4, 1961", "text": "No lawyer. Guilty."}, {"date": "MAR 18, 1963", "text": "Reversed"}, {"date": "AUG 5, 1963", "text": "Retrial, with a lawyer"}], at=2, src=SRC_JACOB),
   show="The retrial took place on August 5, 1963. Henry Cook testified again. At the first trial, he had denied ever being convicted of a felony. Now he said he had once stolen a car and been put on probation. Turner used that prior inconsistent statement to \"impeach and discredit\" him, Jacob later wrote, though Jacob noted the earlier offense was a juvenile matter."),
 L("Same man. Same charge. This time, with a lawyer at his side, the jury acquitted him.",
   dict(type="verdict", kicker="THE RETRIAL · 1963 · BAY COUNTY", stamp="NOT GUILTY", neutral=True, big="Acquitted", sub="Clarence Earl Gideon · with a lawyer")),
 L("And Florida's warning? Bruce Jacob, the lawyer who had argued it, later wrote that approximately twelve hundred prisoners in Florida were set free as a result of Gideon, because witnesses had died or moved away.",
   dict(type="stat", kicker="PER BRUCE JACOB, FLORIDA'S LAWYER", value="~1,200", label="Florida prisoners set free,|he later wrote", src=SRC_JACOB),
   show="And Florida's warning? Bruce Jacob, the lawyer who had argued it, later wrote that \"approximately 1200 prisoners in Florida were set free as a result of Gideon,\" because witnesses had died or moved away."),
 L("Clarence Earl Gideon died in nineteen seventy-two. He was sixty-one.",
   dict(type="big", kicker="1972", lines=["Died at 61.", "The rule|stayed."], src=SRC_ENC),
   show="Clarence Earl Gideon died in 1972. He was 61."),
 L("Nineteen sixty-one: no lawyer, guilty, five years. Nineteen sixty-three: a lawyer, not guilty.",
   dict(type="big", lines=["1961: no lawyer.", "1963: not|guilty."]),
   show="1961: no lawyer, guilty, 5 years. 1963: a lawyer, not guilty."),
 L("Necessities. Not luxuries.",
   dict(type="big", lines=["Necessities.", "Not|luxuries."])),
 L("This is SWORN. Real trials. Real evidence. The verdict.", dict(type="end")),
]
from panfix import fix
fix(lines, "long")
spec = {"label": "SWORN · CASE 007", "lines": lines}
json.dump(spec, open(os.path.join(HERE, "episode.json"), "w"), indent=1, ensure_ascii=False)
print(len(lines), "lines,", sum(len(l["say"].split()) for l in lines), "words")
