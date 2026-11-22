import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
def doc(key, kicker, title, src, pan=None):
    img, a, b = HL[key]
    if pan is None:
        c = a + (b - a) / 2
        pan = [max(0.0, round(c - 0.22, 3)), max(0.0, round(c - 0.16, 3))]
    return dict(type="doc", img=f"img/{img}.jpg", pan=pan, hl=[0.0, a, 1.0, round(b - a, 4)], kicker=kicker, title=title, src=src)
def photo(img, caption, src, fit="cover"):
    return dict(type="photo", img=f"img/{img}.jpg", caption=caption, src=src, fit=fit)
CASE = "U.S. v. Farah et al., D. Minn. 24-cr-173"
S_ALI = f"Government's position regarding sentencing, Ladan Mohamed Ali ({CASE}, Dkt. 277, Nov 6, 2026)"
S_AZ = f"Government's position regarding sentencing, Abdiaziz Shafii Farah ({CASE}, Dkt. 216, Jul 3, 2026)"
S_SF = f"Government's position regarding sentencing, Said Shafii Farah ({CASE}, Dkt. 251, Sep 14, 2026)"
S_NUR = f"Government's position regarding sentencing, Abdimajid Nur ({CASE}, Dkt. 243, Sep 4, 2026)"
S_J = f"Judgment, Abdiaziz Shafii Farah ({CASE}, Dkt. 231, Jul 24, 2026)"
S_M207 = f"Sentencing minutes, Abdulkarim Shafii Farah ({CASE}, Dkt. 207, Mar 4, 2026)"
S_ACQ = "Judgment of acquittal, Said Shafii Farah (D. Minn. 22-cr-124, Dkt. 579, Jun 12, 2024)"
S_N929 = "Government's position regarding sentencing, Abdimajid Nur (D. Minn. 22-cr-124, Dkt. 929, Nov 6, 2025)"
S_EX = "Government trial exhibit, reproduced in D. Minn. 22-cr-124, Dkt. 929"
S_PR24 = "U.S. Attorney's Office, D. Minn., press release (Jun 26, 2024)"
S_PRALI = "U.S. Attorney's Office, D. Minn., press release (Sep 5, 2024) — Ali guilty plea"
S_PRNUR = "U.S. Attorney's Office, D. Minn., press release (Jul 23, 2024) — Nur guilty plea"
S_MPR = "MPR News (Matt Sepic), Nov 20, 2026 — Ali sentencing hearing"
S_MPR7 = "MPR News (Estelle Timar-Wilcox), Jul 22, 2026 — Abdiaziz Farah sentencing hearing"
S_KSTP = "KSTP, Jul 22, 2026 — Abdiaziz Farah sentencing hearing"
S_CBS = "CBS Minnesota / WCCO, Nov 19–20, 2026"
S_MPRB = "MPR News (Matt Sepic), May 21, 2026 — Aimee Bock sentencing"
S_AP = "AP (Steve Karnowski), Jun 4, 2024"
G = "GOV'T SENTENCING MEMO · "
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
SENT = dict(type="verdict", kicker="NOVEMBER 20, 2026 · ST. PAUL, MINN.", stamp="SENTENCED", big="4 Years", sub="Ladan Mohamed Ali · the courier · Judge Eric C. Tostrud")
lines = [
 # COLD OPEN
 L("June second, twenty twenty-four. Eight fifty P.M. A woman walks up to a house in Minnesota and rings the bell. She is carrying a Hallmark gift bag.",
   doc("p_hallmark", "U.S. ATTORNEY · D. MINN. · SEP 5, 2024", "Two Hallmark gift bags", S_PRALI),
   show="June 2, 2024. 8:50 PM. A woman walks up to a house in Minnesota and rings the bell. She is carrying a Hallmark gift bag."),
 L("She hands the bag to the man who answers, and says it is a present, for his stepdaughter. And that there will be more, if she votes not guilty.",
   doc("a_present", G + "ABDIAZIZ FARAH", "“a present for Juror 52”", S_AZ),
   show="She hands the bag to the man who answers, and says it is a \"present,\" for his stepdaughter. And that there will be more, if she votes not guilty."),
 L("His stepdaughter is Juror fifty-two, in the biggest pandemic fraud trial in Minnesota. Inside the bag: one hundred twenty thousand dollars in cash.",
   doc("p_80k", "U.S. ATTORNEY · D. MINN. · SEP 5, 2024", "$120,000 delivered", S_PRALI),
   show="His stepdaughter is Juror 52, in the biggest pandemic fraud trial in Minnesota. Inside the bag: $120,000 in cash."),
 L("It should have been two hundred thousand. The woman with the bag had already taken eighty thousand for herself.",
   doc("a_stole", G + "LADAN ALI", "$80,000 “for herself”", S_ALI),
   show="It should have been $200,000. The woman with the bag had already taken $80,000 for herself."),
 L("And Juror fifty-two did not take the deal. She called the police.",
   dict(type="big", lines=["Juror 52", "called the police."], src=S_AZ)),
 L("On November twentieth, twenty twenty-six, the woman who carried that bag became the last of five people sentenced for the plot. All five had pleaded guilty. Hers: four years in federal prison.",
   SENT, show="On November 20, 2026, the woman who carried that bag became the last of five people sentenced for the plot. All five had pleaded guilty. Hers: four years in federal prison."),
 L("This is how they tried to buy a verdict in the Feeding Our Future case. And how a con inside the con fell apart in one night, from the court records.",
   dict(type="title", kicker="SWORN · CASE 022 · BREAKING", title="The Bribe|for Juror 52", sub="United States v. Farah et al. · D. Minn. 24-cr-173 · sentenced Nov 18–20, 2026"),
   show="This is how they tried to buy a verdict in the Feeding Our Future case. And how a con inside the con fell apart in one night, from the court records."),
 # I
 L("Chapter one. The trial.", dict(type="chapter", n="I", title="The Trial")),
 L("To understand the bribe, you need to know what was at stake. Feeding Our Future was a Minnesota nonprofit, in a federal program that pays for meals for children.",
   doc("n_largest", G + "NUR · 22-CR-124", "“the largest Covid-19 fraud scheme”", S_N929),
   show="To understand the bribe, you need to know what was at stake. Feeding Our Future was a Minnesota nonprofit, in a federal program that pays for meals for children."),
 L("During the pandemic, prosecutors say, people across its network claimed meals that were never served. Overall, more than two hundred fifty million dollars in federal funds were taken, according to the Associated Press. Prosecutors call it the largest Covid nineteen fraud scheme in the United States.",
   dict(type="stat", kicker="FEEDING OUR FUTURE · PER AP", value="$250M+", label="in federal child-nutrition funds taken", src=S_AP + "; " + S_N929),
   show="During the pandemic, prosecutors say, people across its network claimed meals that were never served. Overall, more than $250 million in federal funds were taken, according to the Associated Press. Prosecutors call it \"the largest Covid-19 fraud scheme in the United States.\""),
 L("One of the sites was a small halal market in Shakopee, called Empire Cuisine and Market. It enrolled in the program in April twenty twenty.",
   photo("ex_store", "GOV'T TRIAL EXHIBITS A-1 / H-119 · EMPIRE CUISINE & MARKET, SHAKOPEE", S_EX),
   show="One of the sites was a small halal market in Shakopee, called Empire Cuisine & Market. It enrolled in the program in April 2020."),
 L("According to prosecutors, at the peak, Empire Cuisine and its partners claimed to serve two point seven million meals to children, in the month of March twenty twenty-one alone. Many of the sites, prosecutors wrote, were nothing more than parking lots or vacant commercial spaces.",
   doc("n_meals", G + "NUR · 22-CR-124", "2.7 million meals in one month", S_N929),
   show="According to prosecutors, at the peak, Empire Cuisine and its partners claimed to serve 2.7 million meals to children, in the month of March 2021 alone. Many of the sites, prosecutors wrote, were \"nothing more than parking lots or vacant commercial spaces.\""),
 L("Seventy-nine people were eventually charged in the Feeding Our Future case, according to M.P.R. News. On April twenty-second, twenty twenty-four, the first seven went on trial, before U.S. District Judge Nancy Brasel.",
   doc("a_jury", G + "LADAN ALI", "April 22, 2024: jury selection", S_ALI + "; " + S_MPRB),
   show="79 people were eventually charged in the Feeding Our Future case, according to MPR News. On April 22, 2024, the first seven went on trial, before U.S. District Judge Nancy Brasel."),
 L("Among them: Abdiaziz Farah. His brother, Said Farah. And Abdimajid Nur, who, prosecutors say, created the bulk of the fake meal counts and invoices, including at Abdiaziz Farah's direction.",
   photo("ex_texts", "GOV'T TRIAL EXHIBIT H-51b · MESSAGES BETWEEN ABDIAZIZ FARAH AND ABDIMAJID NUR", S_EX, fit="contain"),
   show="Among them: Abdiaziz Farah. His brother, Said Farah. And Abdimajid Nur, who, prosecutors say, created the bulk of the fake meal counts and invoices, including at Abdiaziz Farah's direction."),
 L("Nur's own company, Nur Consulting, took in more than nine hundred thousand dollars, according to a government chart. Prosecutors say he even paid a website twelve thousand dollars to take his college classes for him.",
   photo("ex_nurcons", "GOV'T SUMMARY CHART · NUR CONSULTING LLC · APR 2021 – JAN 2022", S_N929, fit="contain"),
   show="Nur's own company, Nur Consulting, took in more than $900,000, according to a government chart. Prosecutors say he even paid a website $12,000 to take his college classes for him."),
 L("Their trial would last six weeks. And soon after the jury was picked, prosecutors say, the defendants started looking at the jurors.",
   dict(type="big", lines=["Six weeks.", "Twelve jurors.", "One target."], src=S_ALI + "; " + S_KSTP)),
 # II
 L("Chapter two. Juror fifty-two.", dict(type="chapter", n="II", title="Juror 52")),
 L("According to the government, Abdiaziz Farah quickly picked his candidate. Juror fifty-two. Because, prosecutors wrote, they believed she was the youngest, and the only person of color on the jury.",
   doc("a_target", G + "ABDIAZIZ FARAH", "“the best candidate to bribe”", S_AZ),
   show="According to the government, Abdiaziz Farah quickly picked his candidate. Juror 52. Because, prosecutors wrote, they believed she was \"the youngest and only person of color on the jury.\""),
 L("He told his co-defendants, according to the government: That juror, we can get to her. I'm serious, for real.",
   dict(type="quote", q="that juror . . . we can get to her . . . I’m serious for real.", case="Abdiaziz Farah, to his co-defendants · 2024", doc="As quoted in the government's sentencing memo", cite=S_AZ),
   show="He told his co-defendants, according to the government: \"that juror . . . we can get to her . . . I'm serious for real.\""),
 L("They researched her online, and found her home address. Their younger brother, Abdulkarim Farah, watched her house, and found out where she parked her car during jury service.",
   doc("a_target", G + "ABDIAZIZ FARAH", "Surveillance of Juror 52", S_AZ, pan=[0.25, 0.4]),
   show="They researched her online, and found her home address. Their younger brother, Abdulkarim Farah, watched her house, and found out where she parked her car during jury service."),
 L("Then Nur recruited a courier. Ladan Ali, from Seattle. According to the plea records, she was promised a hundred and fifty thousand dollars to deliver the bribe.",
   doc("a_recruit", G + "LADAN ALI", "Promised $150,000", S_ALI),
   show="Then Nur recruited a courier. Ladan Ali, from Seattle. According to the plea records, she was promised $150,000 to deliver the bribe."),
 L("On May thirtieth, she flew to Minneapolis. The next day, the first day of closing arguments, she followed Juror fifty-two from a downtown parking ramp, all the way home.",
   doc("a_follow", G + "LADAN ALI", "May 31, 2024: followed home", S_ALI),
   show="On May 30, she flew to Minneapolis. The next day, the first day of closing arguments, she followed Juror 52 from a downtown parking ramp, all the way home."),
 L("Abdiaziz Farah, prosecutors say, ordered a magnetic G.P.S. tracker, to put on the juror's car.",
   doc("a_gps", G + "ABDIAZIZ FARAH", "A magnetic GPS tracker", S_AZ),
   show="Abdiaziz Farah, prosecutors say, ordered a magnetic GPS tracker, to put on the juror's car."),
 L("And they wrote her a script. A list of instructions, telling her to vote not guilty on all counts for all defendants. And to convince the other jurors to do the same.",
   doc("p_list", "U.S. ATTORNEY · D. MINN. · JUN 26, 2024", "“NOT GUILTY ON ALL COUNTS”", S_PR24),
   show="And they wrote her a script. A list of instructions, telling her to vote \"NOT GUILTY ON ALL COUNTS FOR ALL DEFENDANTS.\" And to \"convince all the remaining jurors\" to do the same."),
 L("So far, it sounds like a plan. But the woman they had hired had a plan of her own.",
   dict(type="big", lines=["They had a plan.", "So did the courier."], src=S_ALI)),
 # III
 L("Chapter three. The con inside the con.", dict(type="chapter", n="III", title="The Con Inside the Con")),
 L("On June first, Ali told Nur she had approached Juror fifty-two in a bar. The juror, she said, wanted five hundred thousand dollars to vote not guilty. And she wanted the money delivered to her home, the next day.",
   doc("a_bar", G + "LADAN ALI", "“$500,000 in exchange for a not-guilty vote”", S_ALI),
   show="On June 1, Ali told Nur she had approached Juror 52 in a bar. The juror, she said, wanted $500,000 to vote not guilty. And she wanted the money delivered to her home, the next day."),
 L("None of it was true. In the government's words: Ms. Ali fabricated this entire interaction. She never met Juror fifty-two. It was her intention to steal the bribe money, and go back to Seattle.",
   dict(type="quote", q="Ms. Ali fabricated this entire interaction. She never met Juror 52. It was Ms. Ali’s intention to steal the bribe money and return to Seattle.", case="Government's position regarding sentencing · Nov 6, 2026", doc="Dkt. 277, U.S. v. Ali", cite=S_ALI),
   show="None of it was true. In the government's words: \"Ms. Ali fabricated this entire interaction. She never met Juror 52. It was Ms. Ali's intention to steal the bribe money and return to Seattle.\""),
 L("Nur believed her. He passed it on. And the morning of June second, Abdiaziz Farah sent his brother Said an encrypted Signal message. Have the money ready, by ten.",
   doc("a_ready", G + "ABDIAZIZ FARAH", "“have the money ready”", S_AZ),
   show="Nur believed her. He passed it on. And the morning of June 2, Abdiaziz Farah sent his brother Said an encrypted Signal message: \"have the money ready\" by 10:00."),
 L("Said Farah collected two hundred thousand dollars in cash, according to prosecutors, from multiple people, and from a hawala, an informal money-transfer business, at a Minneapolis mall.",
   doc("a_hawala", G + "SAID FARAH", "$200,000 in cash", S_SF),
   show="Said Farah collected $200,000 in cash, according to prosecutors, from multiple people, and from a hawala, an informal money-transfer business, at a Minneapolis mall."),
 L("At his business, Bushra Wholesalers, the cash went to Nur, in a cardboard box. Nur drove it to a parking lot in Bloomington, and handed the box to Ali. She moved the cash into a Hallmark gift bag.",
   doc("p_hallmark", "U.S. ATTORNEY · D. MINN. · SEP 5, 2024", "A cardboard box, $200,000", S_PRALI),
   show="At his business, Bushra Wholesalers, the cash went to Nur, in a cardboard box. Nur drove it to a parking lot in Bloomington, and handed the box to Ali. She moved the cash into a Hallmark gift bag."),
 L("But the brothers did not trust her. So their younger brother Abdulkarim was told to meet her, drive her to the juror's house, and film the delivery.",
   doc("a_stole", G + "LADAN ALI", "“did not trust Ms. Ali”", S_ALI, pan=[0.05, 0.12]),
   show="But the brothers did not trust her. So their younger brother Abdulkarim was told to meet her, drive her to the juror's house, and film the delivery."),
 L("According to the government, on her way to meet him, Ali stole eighty thousand dollars of the bribe money. Prosecutors say his insisting on driving is what stopped her from taking all of it.",
   doc("p_insisted", "U.S. ATTORNEY · D. MINN. · SEP 5, 2024", "“prevented Ali from stealing all of the bribe money”", S_PRALI),
   show="According to the government, on her way to meet him, Ali stole $80,000 of the bribe money. Prosecutors say his insisting on driving is what stopped her from taking all of it."),
 L("They stopped at a Target. Abdulkarim bought a screwdriver, and took the license plate off her rental car.",
   doc("a_target2", G + "ABDIAZIZ FARAH", "A screwdriver from Target", S_AZ),
   show="They stopped at a Target. Abdulkarim bought a screwdriver, and took the license plate off her rental car."),
 L("Eight fifty P.M. While he filmed from the car, Ali walked to the door, and handed the bag to Juror fifty-two's stepfather. A present, she said. More if she voted not guilty.",
   doc("a_present", G + "ABDIAZIZ FARAH", "The video", S_AZ),
   show="8:50 PM. While he filmed from the car, Ali walked to the door, and handed the bag to Juror 52's stepfather. A \"present,\" she said. More if she voted not guilty."),
 L("Then she texted Nur: It's done, babe.",
   dict(type="quote", q="It’s done babe.", case="Ladan Ali, text to Abdimajid Nur · June 2, 2024", doc="As quoted in the government's sentencing memo", cite=S_NUR),
   show="Then she texted Nur: \"It's done babe.\""),
 L("The video went out over Signal. Abdiaziz Farah forwarded it to his brother Said, with three words: watch and delete. And he texted another co-conspirator that he had a good feeling. That's a lot of money for her family.",
   doc("a_delete", G + "ABDIAZIZ FARAH", "“watch and delete”", S_AZ),
   show="The video went out over Signal. Abdiaziz Farah forwarded it to his brother Said, with three words: \"watch and delete.\" And he texted another co-conspirator that he had \"a good feeling\" — \"that's a lot of money for her family.\""),
 L("Two hundred thousand collected. Eighty thousand skimmed by their own courier. One hundred twenty thousand at the juror's door. And one thing they never planned for.",
   dict(type="bars", kicker="JUNE 2, 2024 · PER THE GOVERNMENT", title="Where the $200,000 went", items=[
     {"label": "Collected", "value": 200000, "display": "$200,000"},
     {"label": "Kept by the courier", "value": 80000, "display": "$80,000"},
     {"label": "Delivered to the door", "value": 120000, "display": "$120,000"}], src=S_PRALI + "; " + S_ALI),
   show="$200,000 collected. $80,000 skimmed by their own courier. $120,000 at the juror's door. And one thing they never planned for."),
 # IV
 L("Chapter four. The call.", dict(type="chapter", n="IV", title="The Call")),
 L("Juror fifty-two did not keep the bag. According to the government, she immediately reported the bribery attempt to the police. The A.P. reported that she called them right after she got home, and gave them the bag of cash.",
   doc("a_reported", G + "ABDIAZIZ FARAH", "“immediately reported”", S_AZ + "; " + S_AP),
   show="Juror 52 did not keep the bag. According to the government, she \"immediately reported the bribery attempt to the police.\" The AP reported that she called them right after she got home, and gave them the bag of cash."),
 L("The next morning, before closing arguments resumed, prosecutors told the judge. Judge Brasel ordered the defendants to surrender their phones to the F.B.I.",
   doc("a_reported", G + "ABDIAZIZ FARAH", "Phones surrendered", S_AZ + "; " + S_ALI, pan=[0.35, 0.5]),
   show="The next morning, before closing arguments resumed, prosecutors told the judge. Judge Brasel ordered the defendants to surrender their phones to the FBI."),
 L("Then the race to destroy the evidence began. Abdiaziz Farah did a factory reset of his phone, before agents could take it.",
   doc("a_reset", G + "ABDIAZIZ FARAH", "A factory reset", S_AZ),
   show="Then the race to destroy the evidence began. Abdiaziz Farah did a factory reset of his phone, before agents could take it."),
 L("Nur deleted Signal. But investigators recovered a deleted note from his phone. Thirty talking points, for Ali to give Juror fifty-two, to help her convince the other jurors.",
   doc("a_note", G + "ABDIMAJID NUR", "30 talking points", S_NUR),
   show="Nur deleted Signal. But investigators recovered a deleted note from his phone. 30 talking points, for Ali to give Juror 52, to help her \"convince other jurors.\""),
 L("Nur warned Ali to leave Minnesota. She moved her flight up two days. Before she left, prosecutors say, she packed the clothes she wore that night, together with the cash she had stolen, and shipped the box home to Seattle by U.P.S.",
   doc("a_ups", G + "LADAN ALI", "Shipped by UPS", S_ALI),
   show="Nur warned Ali to leave Minnesota. She moved her flight up two days. Before she left, prosecutors say, she packed the clothes she wore that night, together with the cash she had stolen, and shipped the box home to Seattle by UPS."),
 L("It did not help. Her fingerprints were found on the gift bag. The G.P.S. trackers she had ordered were found in her hotel.",
   doc("a_prints", G + "LADAN ALI", "Fingerprints on the gift bag", S_ALI),
   show="It did not help. Her fingerprints were found on the gift bag. The GPS trackers she had ordered were found in her hotel."),
 L("Juror fifty-two was dismissed from the jury. The trial went on without her. Prosecutor Joe Thompson told the court, as quoted by the Star Tribune: This is stuff that happens in mob movies.",
   dict(type="quote", q="This is completely beyond the pale. This is outrageous behavior. This is stuff that happens in mob movies.", case="AUSA Joseph Thompson, in court · June 2024", doc="As quoted by the Star Tribune, via AP", cite=S_AP + "; " + S_KSTP),
   show="Juror 52 was dismissed from the jury. The trial went on without her. Prosecutor Joe Thompson told the court, as quoted by the Star Tribune: \"This is stuff that happens in mob movies.\""),
 L("Four days later, on June seventh, the remaining jurors returned their verdict. Abdiaziz Farah: guilty. Abdimajid Nur: guilty.",
   doc("a_verdict", G + "ABDIAZIZ FARAH", "June 7, 2024: the verdict", S_AZ),
   show="Four days later, on June 7, the remaining jurors returned their verdict. Abdiaziz Farah: guilty. Abdimajid Nur: guilty."),
 L("And Said Farah, the brother who had gathered the two hundred thousand dollars, was acquitted on every count. The government's own word for it, later: ironically.",
   doc("a_ironic", G + "SAID FARAH", "“ironically acquitting the defendant”", S_SF),
   show="And Said Farah, the brother who had gathered the $200,000, was acquitted on every count. The government's own word for it, later: \"ironically.\""),
 L("The judgment is one line. The defendant was found not guilty. But the bribery case was just beginning.",
   doc("q_acq", "JUDGMENT OF ACQUITTAL · 22-CR-124 · JUNE 12, 2024", "“found not guilty”", S_ACQ),
   show="The judgment is one line. \"The Defendant was found not guilty.\" But the bribery case was just beginning."),
 # V
 L("Chapter five. The pleas.", dict(type="chapter", n="V", title="The Pleas")),
 L("On June twenty-fifth, twenty twenty-four, a federal grand jury indicted all five. Abdiaziz Farah, Said Farah, Abdulkarim Farah, Abdimajid Nur, and Ladan Ali. Then U.S. Attorney Andrew Luger called it a chilling attack on our justice system.",
   doc("p_youngest", "U.S. ATTORNEY · D. MINN. · JUN 26, 2024", "Five indicted", S_PR24 + "; " + S_AP),
   show="On June 25, 2024, a federal grand jury indicted all five. Abdiaziz Farah, Said Farah, Abdulkarim Farah, Abdimajid Nur, and Ladan Ali. Then-U.S. Attorney Andrew Luger called it a \"chilling attack on our justice system.\""),
 L("Nobody went to trial. Nur pleaded guilty first, in July twenty twenty-four. Ali, in September. Abdulkarim Farah, in April twenty twenty-five. Abdiaziz Farah, in June. And Said Farah, the acquitted brother, in August twenty twenty-five. Each to one count: bribery of a juror.",
   dict(type="timeline", kicker="GUILTY PLEAS · BRIBERY OF A JUROR", events=[
     {"date": "Jul 23, 2024", "text": "Abdimajid Nur"},
     {"date": "Sep 5, 2024", "text": "Ladan Ali"},
     {"date": "Apr 2, 2025", "text": "Abdulkarim Farah"},
     {"date": "Jun 18, 2025", "text": "Abdiaziz Farah"},
     {"date": "Aug 21, 2025", "text": "Said Farah"}], src=S_PRNUR + "; " + S_PRALI + "; " + S_AZ + "; " + S_SF + "; plea agreement Dkt. 155"),
   show="Nobody went to trial. Nur pleaded guilty first, in July 2024. Ali, in September. Abdulkarim Farah, in April 2025. Abdiaziz Farah, in June. And Said Farah, the acquitted brother, in August 2025. Each to one count: bribery of a juror."),
 L("Meanwhile, the fraud case had its own reckoning. In August twenty twenty-five, Abdiaziz Farah was sentenced to three hundred thirty-six months. Twenty-eight years.",
   doc("a_verdict", G + "ABDIAZIZ FARAH", "336 months for the fraud", S_AZ),
   show="Meanwhile, the fraud case had its own reckoning. In August 2025, Abdiaziz Farah was sentenced to 336 months. 28 years."),
 L("In November twenty twenty-five, Nur got ten years for the fraud. And in May twenty twenty-six, the founder of Feeding Our Future, Aimee Bock, convicted in a separate trial, was sentenced to five hundred months. Nearly forty-two years.",
   dict(type="bars", kicker="FEEDING OUR FUTURE · FRAUD SENTENCES", title="Before the bribery sentences", items=[
     {"label": "Aimee Bock (founder)", "value": 500, "display": "500 months"},
     {"label": "Abdiaziz Farah", "value": 336, "display": "336 months"},
     {"label": "Abdimajid Nur", "value": 120, "display": "120 months"}], src=S_MPRB + "; " + S_AZ + "; " + S_NUR),
   show="In November 2025, Nur got ten years for the fraud. And in May 2026, the founder of Feeding Our Future, Aimee Bock, convicted in a separate trial, was sentenced to 500 months. Nearly 42 years."),
 L("But the bribe was a separate crime. And for that, each of them would stand in front of a different judge, Eric Tostrud.",
   dict(type="big", lines=["A second case.", "A second judge."], src=S_J + "; " + S_MPR)),
 # VI
 L("Chapter six. The sentences.", dict(type="chapter", n="VI", title="The Sentences")),
 L("March fourth, twenty twenty-six. Abdulkarim Farah, the brother who drove and filmed. Fifty-seven months, the top of his guidelines range.",
   doc("m_57", "SENTENCING MINUTES · MARCH 4, 2026", "57 months", S_M207),
   show="March 4, 2026. Abdulkarim Farah, the brother who drove and filmed. 57 months, the top of his guidelines range."),
 L("July twenty-second. Abdiaziz Farah, the man prosecutors called the organizer and leader of the scheme. Prosecutor Matt Murphy called the bribe an unprecedented attack on the justice system, and on our democracy itself.",
   dict(type="quote", q="an unprecedented attack on the justice system and on our democracy itself.", case="AUSA Matthew Murphy · July 22, 2026", doc="As quoted by MPR News", cite=S_MPR7),
   show="July 22. Abdiaziz Farah, the man prosecutors called the organizer and leader of the scheme. Prosecutor Matt Murphy called the bribe \"an unprecedented attack on the justice system and on our democracy itself.\""),
 L("Farah told the court: I completely denied her civic responsibility to be an independent, fair and impartial juror.",
   dict(type="quote", q="I completely denied her civic responsibility to be an independent, fair and impartial juror.", case="Abdiaziz Farah · July 22, 2026", doc="As quoted by MPR News", cite=S_MPR7),
   show="Farah told the court: \"I completely denied her civic responsibility to be an independent, fair and impartial juror.\""),
 L("Judge Tostrud: It is hard to imagine a more serious case of bribery. This was a coordinated assault on our system of justice.",
   dict(type="quote", q="It is hard to imagine a more serious case of bribery. … This was a coordinated assault on our system of justice.", case="U.S. District Judge Eric C. Tostrud · July 22, 2026", doc="As quoted by MPR News", cite=S_MPR7),
   show="Judge Tostrud: \"It is hard to imagine a more serious case of bribery.\" \"This was a coordinated assault on our system of justice.\""),
 L("The sentence: one hundred twenty months. Ten years, to be served after his twenty-eight years for the fraud. According to KSTP, the judge called Juror fifty-two's actions heroic.",
   doc("j_120", "JUDGMENT · ABDIAZIZ FARAH · JULY 24, 2026", "120 months, consecutive", S_J + "; " + S_KSTP),
   show="The sentence: 120 months. Ten years, to be served after his 28 years for the fraud. According to KSTP, the judge called Juror 52's actions \"heroic.\""),
 L("October thirtieth. Said Farah, the acquitted brother. Six and a half years, according to M.P.R. News.",
   dict(type="verdict", kicker="OCTOBER 30, 2026 · PER MPR NEWS", stamp="SENTENCED", big="6½ Years", sub="Said Shafii Farah · acquitted of the fraud in 2024"),
   show="October 30. Said Farah, the acquitted brother. Six and a half years, according to MPR News."),
 L("November eighteenth. Abdimajid Nur. Five years, according to WCCO, on top of the ten he is already serving for the fraud.",
   dict(type="verdict", kicker="NOVEMBER 18, 2026 · PER WCCO / CBS MINNESOTA", stamp="SENTENCED", big="5 Years", sub="Abdimajid Mohamed Nur · on top of 10 years for the fraud"),
   show="November 18. Abdimajid Nur. Five years, according to WCCO, on top of the ten he is already serving for the fraud."),
 L("And two days later, November twentieth. Ladan Ali, the courier who took eighty thousand dollars for herself. Prosecutors had asked for fifty-seven months.",
   doc("a_forsale", G + "LADAN ALI", "“justice is not, and never will be for sale”", S_ALI),
   show="And two days later, November 20. Ladan Ali, the courier who took $80,000 for herself. Prosecutors had asked for 57 months."),
 L("Her lawyer, Eric Newmark, told the judge: Her interest here was not to subvert justice. It was purely financial.",
   dict(type="quote", q="Her interest here was not to subvert justice, it was purely financial.", case="Eric Newmark, Ali's attorney · Nov 20, 2026", doc="As quoted by MPR News", cite=S_MPR),
   show="Her lawyer, Eric Newmark, told the judge: \"Her interest here was not to subvert justice, it was purely financial.\""),
 L("Ali said: I'm a mother, a wife, and a woman who's committed to lead an honest life going forward.",
   dict(type="quote", q="I’m a mother, a wife, and a woman who’s committed to lead an honest life going forward.", case="Ladan Mohamed Ali · Nov 20, 2026", doc="As quoted by MPR News", cite=S_MPR),
   show="Ali said: \"I'm a mother, a wife, and a woman who's committed to lead an honest life going forward.\""),
 L("Judge Tostrud gave her four years in prison. She is due to report on January nineteenth.",
   SENT, show="Judge Tostrud gave her four years in prison. She is due to report on January 19."),
 L("So here is the final count. Five people. Two hundred thousand dollars. One juror. Fifty-seven months. Ten years. Six and a half. Five. Four.",
   dict(type="bars", kicker="BRIBERY OF A JUROR · D. MINN. 24-CR-173", title="All five sentenced", items=[
     {"label": "Abdiaziz Farah", "value": 120, "display": "120 mo."},
     {"label": "Said Farah", "value": 78, "display": "6½ yrs"},
     {"label": "Abdimajid Nur", "value": 60, "display": "5 yrs"},
     {"label": "Abdulkarim Farah", "value": 57, "display": "57 mo."},
     {"label": "Ladan Ali", "value": 48, "display": "4 yrs"}], src=S_J + "; " + S_M207 + "; " + S_MPR + "; " + S_CBS),
   show="So here is the final count. Five people. $200,000. One juror. 57 months. Ten years. Six and a half. Five. Four."),
 L("They picked her because they thought she was the easiest juror to buy. She was the one who picked up the phone. Was four years enough for the courier who skimmed the bribe? Tell us in the comments.",
   dict(type="end"),
   show="They picked her because they thought she was the easiest juror to buy. She was the one who picked up the phone. Was four years enough for the courier who skimmed the bribe? Tell us in the comments."),
]

# ---- independent fact-check fixes (factcheck.md) ----
def F(i, say=None, show=None, **sc):
    if say is not None: lines[i]["say"] = say
    if show is not None: lines[i]["show"] = show
    elif say is not None: lines[i].pop("show", None)
    for k, v in sc.items(): lines[i]["scene"][k] = v
def R(i, a, b):
    for k in ("say", "show"):
        if k in lines[i]: lines[i][k] = lines[i][k].replace(a, b)
R(2, "in the biggest pandemic fraud trial in Minnesota", "in the first Feeding Our Future fraud trial")
F(6, sub="United States v. Farah et al. · D. Minn. 24-cr-173 · sentenced Mar 4 – Nov 20, 2026")
F(10, "This trial's scheme, prosecutors say, started at a small halal market in Shakopee, called Empire Cuisine and Market. It enrolled in the program in April twenty twenty.",
  "This trial's scheme, prosecutors say, started at a small halal market in Shakopee, called Empire Cuisine & Market. It enrolled in the program in April 2020.", src=S_EX + "; " + S_N929)
R(11, "Empire Cuisine and its partners claimed", "Nur and his co-defendants claimed")
F(12, src=S_ALI + "; " + S_PR24 + "; " + S_MPRB)
F(15, lines=["Six weeks.", "One jury.", "One target."])
R(21, "she followed Juror fifty-two from a downtown parking ramp, all the way home.", "she followed Juror fifty-two from a downtown parking ramp, prosecutors say, all the way home.")
R(21, "she followed Juror 52 from a downtown parking ramp, all the way home.", "she followed Juror 52 from a downtown parking ramp, prosecutors say, all the way home.")
R(23, "And they wrote her a script.", "And, prosecutors say, they wrote her a script.")
F(36, "The video went out over Signal. Abdiaziz Farah forwarded it to his brother Said, with three words: watch and delete. And he texted another co-conspirator that he had a good feeling Juror fifty-two will come through, and that's a lot of money for her family.",
  "The video went out over Signal. Abdiaziz Farah forwarded it to his brother Said, with three words: \"watch and delete.\" And he texted another co-conspirator that he had \"a good feeling [Juror 52] will come through and that's a lot of money for her family.\"")
R(41, "Then the race to destroy the evidence began.", "Then, prosecutors say, the race to destroy the evidence began.")
R(42, "But investigators recovered", "But, according to prosecutors, investigators recovered")
R(48, "The judgment is one line.", "The judgment is short.")
F(50, src=S_PR24 + "; AP via ABC News, Jun 2024")
F(53, title="The fraud sentences")
F(54, "But the bribe was a separate crime, in a separate case. And that case went to a different judge, Eric Tostrud.")
F(56, src=S_M207 + "; Gov't position re sentencing, Abdulkarim Farah (Dkt. 203); " + S_AZ)
F(62, "November eighteenth. Abdimajid Nur. Five years, according to WCCO. M.P.R. News reports it runs on top of the ten he is already serving for the fraud.",
  "November 18. Abdimajid Nur. Five years, according to WCCO. MPR News reports it runs on top of the ten he is already serving for the fraud.",
  kicker="NOVEMBER 18, 2026 · PER WCCO / MPR NEWS")
R(64, "told the judge", "told the court")
R(68, "the easiest juror to buy", "the best candidate to bribe")
for i in (5, 66):
    lines[i]["scene"] = dict(lines[i]["scene"], kicker="NOVEMBER 20, 2026 · D. MINN.")

json.dump({"label": "SWORN · CASE 022", "lines": lines}, open(os.path.join(HERE, "episode.json"), "w"), indent=1, ensure_ascii=False)
print(len(lines), "lines,", sum(len(l["say"].split()) for l in lines), "words")
