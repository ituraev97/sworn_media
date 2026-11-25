import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
def doc(key, kicker, title, src, pan=None):
    img, a, b = HL[key]
    if pan is None:
        c = a + (b - a) / 2
        pan = [max(0.0, round(c - 0.22, 3)), max(0.0, round(c - 0.16, 3))]
    return dict(type="doc", img=f"img/{img}.jpg", pan=pan, hl=[0.0, a, 1.0, round(b - a, 4)], kicker=kicker, title=title, src=src)
def photo(img, caption, src, fit="contain"):
    return dict(type="photo", img=f"img/{img}.jpg", caption=caption, src=src, fit=fit)
CASE = "United States v. Huawei Technologies Co., Ltd., et al., E.D.N.Y. 18-cr-457 (AMD)"
S_S4 = f"Superseding Indictment S-4 ({CASE}, Dkt. 689, filed Apr 17, 2026)"
S_PR = "U.S. Department of Justice, Office of Public Affairs, press release 26-1413 (Nov 24, 2026)"
S_EX = "Trial exhibit released by the Justice Department with the verdict announcement (credit line: U.S. v. Huawei Technologies Co Ltd., Case No. 1:18-cr-00457)"
S_L823 = f"Government letter to Judge Donnelly, Aug 31, 2026 ({CASE}, Dkt. 823)"
S_L954 = f"Government letter to Judge Donnelly, Nov 14, 2026 ({CASE}, Dkt. 954)"
S_L959 = f"Government letter to Judge Donnelly, Nov 17, 2026 ({CASE}, Dkt. 959)"
S_AFP = "IBTimes (Merin Rebecca Thomas), citing AFP, Nov 24, 2026"
IK = "SUPERSEDING INDICTMENT · ALLEGATIONS · "
PK = "U.S. DEPARTMENT OF JUSTICE · NOV 24, 2026"
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
VERDICT = dict(type="verdict", kicker="NOVEMBER 24, 2026 · BROOKLYN, N.Y.", stamp="GUILTY", big="Huawei + 3 subsidiaries", sub="Federal jury, E.D.N.Y. · Judge Ann M. Donnelly presided · sentencing set Sept. 14, 2027")
lines = [
 # COLD OPEN
 L("A robot arm. The Justice Department says a Huawei employee carried part of one out of a laboratory in his backpack.",
   photo("tappy", "IMAGE RELEASED BY THE JUSTICE DEPARTMENT · T-MOBILE “TAPPY” TEST ROBOT", S_EX)),
 L("According to the announcement, it was a part of this T-Mobile testing robot, taken out of a controlled laboratory."),
 L("On November twenty-fourth, twenty twenty-six, a federal jury in Brooklyn found Huawei Technologies, and three of its subsidiaries, guilty.",
   VERDICT, show="On November 24, 2026, a federal jury in Brooklyn found Huawei Technologies, and three of its subsidiaries, guilty."),
 L("Bank fraud. Violating sanctions on Iran. Money laundering. And a conspiracy to steal trade secrets from American companies.",
   dict(type="big", kicker="CONVICTED OF · PER THE JUSTICE DEPARTMENT", lines=["Bank fraud.", "Iran sanctions.", "Money laundering.", "Trade-secret|theft conspiracy."], src=S_PR)),
 L("Two charges did not stick. According to AFP, the jury acquitted Huawei of racketeering conspiracy and of conspiracy to obstruct justice.",
   dict(type="big", kicker="ACQUITTED · AS REPORTED BY AFP", lines=["Acquitted:", "racketeering conspiracy,|conspiracy to|obstruct justice."], src=S_AFP),
   ),
 L("This is what the jury found, what the evidence shows, and what happens next. From the indictment, the government's letters to the judge, and the Justice Department's own announcement.",
   dict(type="title", kicker="SWORN · CASE 024 · BREAKING", title="Huawei|On Trial", sub="United States v. Huawei Technologies Co., Ltd. · E.D.N.Y. 18-cr-457 · verdict Nov 24, 2026")),
 # I
 L("Chapter one. The verdict.", dict(type="chapter", n="I", title="The Verdict")),
 L("The Justice Department's announcement lists what the jury convicted Huawei and three subsidiaries of. Conspiracy to steal trade secrets. Conspiracy to commit wire and bank fraud. Wire fraud. Bank fraud.",
   doc("p_verdict", PK, "What the jury convicted", S_PR)),
 L("Conspiracy to defraud the United States. Conspiracy to violate the International Emergency Economic Powers Act, and substantive violations of that law. And money laundering conspiracy."),
 L("Prosecutors said the defendants were Huawei Technologies, the Chinese parent company, plus Huawei Device, and two American subsidiaries, Futurewei Technologies and Huawei Device U.S.A.",
   doc("s_caption", IK + "CAPTION", "Four defendants", S_S4),
   show="Prosecutors said the defendants were Huawei Technologies, the Chinese parent company, plus Huawei Device, and two American subsidiaries, Futurewei Technologies and Huawei Device USA."),
 L("According to AFP, Huawei was convicted on ten of twelve criminal charges. The jury deliberated for five days, after more than sixty witnesses called by prosecutors, and fifteen called by the defense.",
   dict(type="stat", kicker="THE TRIAL · AS REPORTED BY AFP", value="10 of 12", label="criminal charges: guilty", src=S_AFP),
   show="According to AFP, Huawei was convicted on 10 of 12 criminal charges. The jury deliberated for five days, after more than 60 witnesses called by prosecutors, and 15 called by the defense."),
 L("Huawei was acquitted of racketeering conspiracy, and of conspiracy to obstruct justice. Racketeering is the charge that treats a company as a criminal enterprise. Before deliberations, the government had asked the judge for a modified instruction on how racketeering acts must be related to each other. The letters do not say whether the judge gave it.",
   doc("l_rico", "GOVERNMENT LETTER · NOV 17, 2026", "The racketeering instruction", S_L959)),
 L("The Attorney General, Todd Blanche, put it this way.",
   dict(type="quote", q="No person or company is above the law.", case="Attorney General Todd Blanche", doc="Justice Department announcement of the verdict", cite="DOJ press release 26-1413, Nov. 24, 2026")),
 L("The government told the judge this was not a trial of China, or of Iran. Before the jury was picked, the government wrote to the judge about prospective jurors who had answered questions on those topics.",
   doc("l_nottrial", "GOVERNMENT LETTER · AUG 31, 2026", "Who is on trial", S_L823)),
 L("The government said, quote, the government of the People's Republic of China, the Chinese Communist Party, the government of Iran, and the Islamic Revolutionary Guard Corps, are not on trial. The defendants were companies."),
 L("The case is older than most people realize. The indictment on the court docket today is the fourth superseding indictment, numbered S-4. An earlier one, the S-3, filed in February twenty twenty, named five companies and Huawei's chief financial officer. The one filed in April of this year names four companies.",
   dict(type="timeline", kicker="THE CASE · FROM THE COURT RECORD", events=[{"date":"Feb 13, 2020","text":"Superseding indictment (S-3): Huawei, four affiliates, and its CFO"},{"date":"Apr 17, 2026","text":"Superseding indictment (S-4): four companies"},{"date":"Aug 31, 2026","text":"Jury questionnaires: 130 prospective jurors in dispute"},{"date":"Nov 24, 2026","text":"Verdict"},{"date":"Sept 14, 2027","text":"Sentencing set"}], at=3, src=S_S4),
   show="The case is older than most people realize. The indictment on the court docket today is the fourth superseding indictment, numbered S-4. An earlier one, the S-3, filed in February 2020, named five companies and Huawei's chief financial officer. The one filed in April of this year names four companies."),
 L("Companies cannot go to prison. The Justice Department says that when sentenced, the defendants face financial penalties, including criminal fines, forfeiture, and restitution. Sentencing is set for September fourteenth, twenty twenty-seven.",
   doc("p_sent", PK, "Sentencing set for Sept. 14, 2027", S_PR),
   show="Companies cannot go to prison. The Justice Department says that when sentenced, the defendants face financial penalties, including criminal fines, forfeiture, and restitution. Sentencing is set for September 14, 2027."),
 L("So what did Huawei do? The Justice Department's answer starts with a robot.",
   dict(type="big", lines=["What does the Justice Department|say it proved?", "It starts|with a robot."], src=S_PR)),
 # II
 L("Chapter two. The robot.", dict(type="chapter", n="II", title="The Robot")),
 L("The robot belonged to T-Mobile. Its name was Tappy. It tests how a phone's touch screen responds, by mimicking a human touch. The Justice Department says Tappy was a T-Mobile trade secret.",
   doc("p_tappy", PK, "T-Mobile’s robot, “Tappy”", S_PR)),
 L("The indictment does not name the company and the announcement does not cite the paragraph, but both describe a phone-testing robot taken from a lab. In May twenty twelve, it says, Huawei Device USA asked a U.S. wireless network operator to sell or license its phone-testing robot. The company declined.",
   doc("s_robot_ask", IK + "¶ 33", "The robot was not for sale", S_S4),
   show="The indictment does not name the company and the announcement does not cite the paragraph, but both describe a phone-testing robot taken from a lab. In May 2012, it says, Huawei Device USA asked a U.S. wireless network operator to sell or license its phone-testing robot. The company declined."),
 L("Then, the indictment says, Huawei and Huawei Device began to build their own robot, and told Huawei's American employees to send them detailed information about the other company's technology."),
 L("The Justice Department says Huawei signed a nondisclosure agreement with T-Mobile, fully intending to violate it. And that Huawei employees in the United States sent photographs and technical details of the robot back to China."),
 L("In May twenty thirteen, the indictment says, Huawei sent an engineer to the United States. He described the trip in his own words. Quote: go to the laboratory for reconnaissance and obtain measurement data.",
   doc("s_recon", IK + "¶ 36", "“…for reconnaissance…”", S_S4),
   show="In May 2013, the indictment says, Huawei sent an engineer to the United States. He described the trip in his own words. Quote: \"go to the [Company 5] laboratory for reconnaissance and obtain measurement data.\""),
 L("Then came the arm. On May twenty-ninth, twenty thirteen, the indictment says, an employee surreptitiously placed a robot arm into a laptop bag, and removed it from the laboratory. The Justice Department's announcement says backpack. The photographs and measurements were emailed to engineers.",
   doc("s_arm", IK + "¶ 38", "The robot arm", S_S4),
   show="Then came the arm. On May 29, 2013, the indictment says, an employee surreptitiously placed a robot arm into a laptop bag, and removed it from the laboratory. The Justice Department's announcement says backpack. The photographs and measurements were emailed to engineers."),
 L("And when the other company noticed? The indictment says Huawei Device USA wrote an Investigation Report. It described the actions as isolated incidents, and one engineer's conduct as a moment of indiscretion.",
   doc("s_isolated", IK + "¶ 39", "“Isolated incidents”", S_S4)),
 L("According to Global Investigations Review, Huawei's defense closing described the case as ordinary business activity and isolated employee misconduct. The jury convicted Huawei of conspiracy to steal trade secrets.",
   dict(type="big", kicker="THE DEFENSE · AS REPORTED BY GIR", lines=["Ordinary business|and isolated|misconduct?", "Convicted:|conspiracy to steal|trade secrets."], src="Global Investigations Review, Nov 18, 2026")),
 # III
 L("Chapter three. The code and the circuit board.", dict(type="chapter", n="III", title="The Code and the Circuit Board")),
 L("Tappy was one example. The Justice Department listed others it says were proved at trial. The first is Cisco. Prosecutors say Huawei copied the source code used on Cisco routers, which the announcement calls the crown jewel of Cisco technology.",
   doc("p_cisco", PK, "Cisco’s “crown jewel”", S_PR)),
 L("And in a poorly conceived effort to hide the theft, the announcement says, Huawei engineers left Cisco's own notes in the code. They referred to Cisco by its name written backwards. O, C, S, I, C.",
   dict(type="big", kicker="DOJ ANNOUNCEMENT · TRIAL EVIDENCE", lines=["Cisco, spelled", "backwards:", "“ocsic”"], src=S_PR)),
 L("Then, the announcement says, Fujitsu. A Huawei employee was caught photographing proprietary Fujitsu equipment. His badge claimed he worked for a company called Weihua, not Huawei.",
   doc("p_weihua", PK, "A badge that said “Weihua”", S_PR)),
 L("The indictment describes a July 2004 trade-show incident in Chicago, involving a company it calls Company 3 and does not name. A badge reading Weihua appears there too, but the announcement does not say it is the same incident. According to the indictment, Huawei told Reuters the man was a junior engineer who had never traveled to the United States before, and a resume he gave the U.S. government around 2012 described him as a senior R&D engineer.",
   doc("s_junior", IK + "¶ 26 · COMPANY 3 (NOT NAMED)", "“A junior engineer…”", S_S4)),
 L("Then a circuit board. When CNEX, a U.S. technology company, would not collaborate with Huawei directly, the Justice Department says Huawei hired a university researcher to arrange it, without disclosing that he was acting for Huawei. He gave Huawei direct access to CNEX's proprietary hardware.",
   photo("cnex", "TRIAL EXHIBIT · CNEX SOLID-STATE DRIVE BOARD WITH WIRES ATTACHED BY HUAWEI ENGINEERS", S_EX)),
 L("And Quintel, a U.S. antenna maker. Huawei received confidential information under a nondisclosure agreement. Almost immediately, the announcement says, Huawei filed a patent application for technology that included Quintel's idea, and attached a confidential Quintel slide to it.",
   doc("p_quintel", PK, "A patent filing with someone else’s slide", S_PR)),
 L("The indictment puts one figure on a different, unnamed company. It says that between about two thousand nine and two thousand sixteen, Huawei received about twenty-two million dollars in income from products that incorporated intellectual property it alleges was misappropriated from an antenna-technology company it calls Company 4.",
   doc("s_22m", IK + "¶ 32 · COMPANY 4 (NOT NAMED)", "About $22 million", S_S4),
   show="The indictment puts one figure on a different, unnamed company. It says that between about 2009 and 2016, Huawei received about $22 million in income from products that incorporated intellectual property it alleges was misappropriated from an antenna-technology company it calls Company 4."),
 L("Prosecutors also alleged a policy. In twenty thirteen, the indictment says, Huawei launched a bonus program to reward employees who obtained confidential information from competitors. A group reviewed submissions and awarded monthly bonuses to the employees who provided the most valuable stolen information.",
   doc("s_bonus", IK + "¶ 11", "The bonus program", S_S4),
   show="Prosecutors also alleged a policy. In 2013, the indictment says, Huawei launched a bonus program to reward employees who obtained confidential information from competitors. A group reviewed submissions and awarded monthly bonuses to the employees who provided the most valuable stolen information."),
 L("Huawei's response, according to AFP: the trade-secret disputes had been resolved as civil matters. The jury also heard fifteen defense witnesses.",
   dict(type="big", kicker="HUAWEI'S RESPONSE · AS REPORTED BY AFP", lines=["Trade-secret disputes:", "civil matters."], src=S_AFP)),
 # IV
 L("Chapter four. Skycom.", dict(type="chapter", n="IV", title="Skycom")),
 L("The verdict also covers Iran. The Justice Department says Huawei conducted its business in Iran under the name Skycom.",
   doc("p_skycom", PK, "“Skycom”", S_PR)),
 L("According to the announcement, Huawei repeatedly lied about that business. To banks, to journalists, and to the U.S. government. It said that it did not assist Iran's government, military or intelligence community. That it began restricting its Iran business in twenty eleven. That Skycom was a business partner, rather than a wholly owned subsidiary. And that Huawei complied with all applicable sanctions.",
   show="According to the announcement, Huawei repeatedly lied about that business. To banks, to journalists, and to the U.S. government. It said that it did not assist Iran's government, military or intelligence community. That it began restricting its Iran business in 2011. That Skycom was a business partner, rather than a wholly owned subsidiary. And that Huawei complied with all applicable sanctions."),
 L("The announcement says Huawei knew every one of those statements was materially false and misleading.",
   dict(type="big", kicker="DOJ ANNOUNCEMENT · TRIAL EVIDENCE", lines=["Skycom: “a business", "partner”?", "Or a wholly owned|subsidiary.", "DOJ: the statements|were false."], src=S_PR)),
 L("The indictment describes the structure. It says Huawei operated Skycom as an unofficial subsidiary, to obtain otherwise prohibited American goods, technology and services, including banking services, while concealing the link to Huawei.",
   doc("s_unoff", IK + "¶ 67", "An “unofficial subsidiary”", S_S4)),
 L("Internal documents, the indictment says, used code names for sanctioned countries. A-two meant Iran. A-nine meant North Korea. The United States and Canada got no code names.",
   doc("s_a2", IK + "¶ 66", "“A2” = Iran", S_S4),
   show="Internal documents, the indictment says, used code names for sanctioned countries. A2 meant Iran. A9 meant North Korea. The United States and Canada got no code names."),
 L("And what was at stake? According to the Justice Department, Huawei lied to banks to obtain billions of U.S. dollars, and access to dollar clearing services.",
   doc("p_banks", PK, "“Billions of U.S. dollars”", S_PR)),
 L("The indictment gives one number. Between about twenty ten and twenty fourteen, it says, one bank and its American subsidiary cleared more than one hundred million dollars in transactions related to Skycom through the United States.",
   doc("s_100m", IK + "¶ 62", "$100 million cleared through the U.S.", S_S4),
   show="The indictment gives one number. Between about 2010 and 2014, it says, one bank and its American subsidiary cleared more than $100 million in transactions related to Skycom through the United States."),
 L("In two thousand thirteen, the indictment says, a Huawei executive presented a slide deck to a bank. It said Huawei operates in Iran in strict compliance with applicable laws, and that its engagement with Skycom is normal business cooperation. The indictment says: these statements were all false.",
   doc("s_ppt", IK + "¶¶ 73–74", "The bank presentation", S_S4),
   show="In 2013, the indictment says, a Huawei executive presented a slide deck to a bank. It said Huawei operates in Iran in strict compliance with applicable laws, and that its engagement with Skycom is normal business cooperation. The indictment says: these statements were all false."),
 L("The announcement adds the part that is not about money. Testimony established, it says, that Huawei helped Iran monitor and censor internet access, and provided surveillance cameras that let the regime monitor protest activity.",
   doc("p_cams", PK, "Surveillance and protest activity", S_PR)),
 L("The company also answered the press. The indictment says that in December twenty eleven, after a Wall Street Journal report, Huawei issued a press release saying it had, quote, no involvement in any type of monitoring and filtering activities.",
   doc("s_wsj", IK + "¶ 70", "Huawei’s December 2011 statement", S_S4),
   show="The company also answered the press. The indictment says that in December 2011, after a Wall Street Journal report, Huawei issued a press release saying it had, quote, \"no involvement in any type of monitoring and filtering activities.\""),
 L("The indictment says that when Reuters reported in twenty twelve and twenty thirteen that Skycom had sold embargoed American goods to Iran, and that Huawei owned it, banks relied on Huawei's denials to decide whether to keep doing business with it. They kept doing business with it.",
   show="The indictment says that when Reuters reported in 2012 and 2013 that Skycom had sold embargoed American goods to Iran, and that Huawei owned it, banks relied on Huawei's denials to decide whether to keep doing business with it. They kept doing business with it."),
 L("The indictment alleges that Huawei told Congress something different. In twenty twelve, it says, a Huawei senior vice president testified before the House Intelligence Committee: quote, we have never provided any equipment to the Iranian government.",
   doc("s_hpsci", IK + "¶ 60", "Testimony to Congress, 2012", S_S4),
   show="The indictment alleges that Huawei told Congress something different. In 2012, it says, a Huawei senior vice president testified before the House Intelligence Committee: quote, \"We have never provided any equipment to the Iranian government.\""),
 L("The indictment says that testimony was false, and that Huawei's Iran business included providing goods and services to the Iranian government. The jury convicted Huawei on the sanctions, bank fraud and money laundering charges."),
 # V
 L("Chapter five. The last weeks.", dict(type="chapter", n="V", title="The Last Weeks")),
 L("The government's November fourteenth letter concerned the rebuttal evidence it planned to offer. The government wrote to the judge about the rebuttal evidence it planned to offer.",
   doc("l_recorded", "GOVERNMENT LETTER · NOV 14, 2026", "Rebuttal evidence", S_L954),
   show="The government's November 14 letter concerned the rebuttal evidence it planned to offer. The government wrote to the judge about the rebuttal evidence it planned to offer."),
 L("The letter describes a recorded phone call in the government's case. In it, two Huawei employees, the letter says, discussed and coordinated a plan to send Chinese expatriate employees who worked in sensitive nations out of the jurisdiction of the United States."),
 L("The defense had told the jury another story, the letter says. That the expats were sent home because of headcount reductions and economic challenges at Huawei's American operations. The government said its rebuttal evidence would refute it."),
 L("The indictment also alleges that in April twenty eighteen, that Huawei made efforts to move an employee with knowledge of its Iran business to China, beyond the reach of the U.S. government.",
   doc("s_move", IK + "COUNT EIGHT · OVERT ACT (d)", "Moving an employee to China", S_S4),
   show="The indictment also alleges that in April 2018, that Huawei made efforts to move an employee with knowledge of its Iran business to China, beyond the reach of the U.S. government."),
 L("This was a trial of companies, not of people. An earlier version of the indictment, in twenty twenty, also named Huawei's chief financial officer, Meng Wanzhou. By this trial, she was no longer a defendant. According to IBTimes, she reached a deferred prosecution agreement in twenty twenty-one, and the charges against her were dismissed.",
   dict(type="big", kicker="AS REPORTED BY IBTIMES / AFP", lines=["Meng Wanzhou:", "not a defendant", "at this trial."], src=S_AFP),
   show="This was a trial of companies, not of people. An earlier version of the indictment, in 2020, also named Huawei's chief financial officer, Meng Wanzhou. By this trial, she was no longer a defendant. According to IBTimes, she reached a deferred prosecution agreement in 2021, and the charges against her were dismissed."),
 # VI
 L("Chapter six. What happens next.", dict(type="chapter", n="VI", title="What Happens Next")),
 L("Huawei has said it rejects the remaining allegations. According to AFP, it welcomed the acquittal on racketeering, said it would review the verdicts, and take legal action to defend its interests. Its attorney said the company was disappointed, and expects to appeal.",
   dict(type="big", kicker="HUAWEI'S RESPONSE · AS REPORTED BY AFP", lines=["Disappointed.", "Expected to|appeal."], src=S_AFP)),
 L("The sentencing is set for September fourteenth, twenty twenty-seven. The Justice Department says a federal district court judge will determine any sentence, and that the defendants face criminal fines, forfeiture, and restitution. AFP reports that the amounts have not been determined.",
   doc("p_sent", PK, "Penalties still to come", S_PR),
   show="The sentencing is set for September 14, 2027. The Justice Department says a federal district court judge will determine any sentence, and that the defendants face criminal fines, forfeiture, and restitution. AFP reports that the amounts have not been determined."),
 L("The jury convicted on the trade-secret conspiracy, the bank fraud, the sanctions violations and the money laundering. The Justice Department says the robot arm and the Skycom name are among the evidence it proved at trial. The bank presentation is an allegation from the indictment. Assistant Attorney General Tysen Duva of the Criminal Division said, quote, Huawei built its global empire on a foundation of fraud, theft, and deception. According to AFP, Huawei rejects the remaining allegations.",
   dict(type="verdict", kicker="NOVEMBER 24, 2026 · BROOKLYN, N.Y.", stamp="GUILTY", big="10 of 12 counts", sub="Racketeering conspiracy: acquitted · Huawei's attorney expects to appeal · as reported by AFP")),
 L("A company can't be sent to prison. So what should a punishment for a company look like? A fine so large it changes how it does business? Tell us in the comments.",
   dict(type="end")),
]
json.dump({"label": "SWORN · CASE 024", "lines": lines}, open(os.path.join(HERE, "episode.json"), "w"), indent=1, ensure_ascii=False)
print(len(lines), "lines,", sum(len(l["say"].split()) for l in lines), "words")
