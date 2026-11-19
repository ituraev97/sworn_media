import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
def hlb(key):
    img, a, b = HL[key]
    return img, [0.0, a, 1.0, round(b - a, 4)]
def doc(key, kicker, title, src, pan=None):
    img, box = hlb(key)
    if pan is None:
        c = box[1] + box[3] / 2
        pan = [max(0.0, round(c - 0.22, 3)), max(0.0, round(c - 0.16, 3))]
    return dict(type="doc", img=f"img/{img}.jpg", pan=pan, hl=box, kicker=kicker, title=title, src=src)
SRC_C = "Criminal complaint, U.S. v. Williams & Johnson (S.D.N.Y., sworn Nov 17, 2026) — allegations"
SRC_PR = "U.S. Attorney's Office, S.D.N.Y., press release (Nov 18, 2026)"
SRC_WRTV = "WRTV / WISH-TV (John Herrick, Nov 18, 2026)"
SRC_IBJ = "Indianapolis Business Journal via The Indiana Lawyer (Susan Orr, Nov 18, 2026)"
SRC_MINKOW = "Barry Minkow, \"One Minute On Fraud\" (Substack, Nov 18, 2026) — his own account"
C = "S.D.N.Y. COMPLAINT · "
PR = "U.S. ATTORNEY · S.D.N.Y. · NOV 18, 2026"
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
lines = [
 # COLD OPEN
 L("May fourteenth, twenty twenty-six. A text message arrives for the man who runs a six-hundred-million-dollar investment fund. Aggressive fund, ten point oh one percent. Does this sound right?",
   dict(type="quote", q="Aggressive fund 10.01% / Does this sound right?", case="A Backward Hat employee, May 14, 2026", doc="Text message quoted in the criminal complaint, ¶ 18", cite=SRC_C),
   show="May 14, 2026. A text message arrives for the man who runs a $600 million investment fund. \"Aggressive fund 10.01%. Does this sound right?\""),
 L("He asks what it was last month. Nine point five one, the employee says. And then, according to federal prosecutors, he answers: Let's do nine point nine one. Bumped it up a bit.",
   doc("may14", C + "¶ 18 · MAY 14, 2026", "“Let’s do 9.91 bumped it up a bit”", SRC_C),
   show="He asks what it was last month. 9.51%, the employee says. And then, according to federal prosecutors, he answers: \"Let's do 9.91. Bumped it up a bit.\""),
 L("Prosecutors say that is how Backward Hat Capital decided what its investors had earned. Not from trades. From a text.",
   dict(type="big", kicker="WHAT PROSECUTORS ALLEGE", lines=["Not from trades.", "From a text."], src=SRC_C)),
 L("More than two thousand investors put in more than six hundred million dollars. They were told the fund typically made more than six percent a month.",
   dict(type="stat", kicker="BACKWARD HAT CAPITAL · SINCE 2022", value="$600M+", label="from more than 2,000 investors", src=SRC_C),
   show="More than 2,000 investors put in more than $600 million. They were told the fund typically made more than 6% a month."),
 L("On the morning of November eighteenth, twenty twenty-six, federal agents arrested two of its founders. Phillip Patrick Williams in Kokomo, Indiana. Devin Allen Johnson in Gilbert, Arizona.",
   dict(type="verdict", kicker="NOVEMBER 18, 2026", stamp="CHARGED", big="Securities & wire fraud", sub="Phillip Patrick Williams · Devin Allen Johnson", neutral=True),
   show="On the morning of November 18, 2026, federal agents arrested two of its founders. Phillip Patrick Williams in Kokomo, Indiana. Devin Allen Johnson in Gilbert, Arizona."),
 L("They are charged, not convicted, and they are presumed innocent. Everything in the complaint is an allegation. This is what it says.",
   dict(type="title", kicker="SWORN · CASE 019 · BREAKING", title="Backward Hat|$600 Million", sub="United States v. Williams & Johnson · S.D.N.Y. · criminal complaint")),
 # I
 L("Chapter one. The promise.", dict(type="chapter", n="I", title="The Promise")),
 L("According to the complaint, Backward Hat Capital was founded in or about July twenty twenty-two by three people: Williams, Johnson, and a third co-founder the complaint does not name. Each held an equal share.",
   doc("cofounders", C + "¶ 11", "Three co-founders, equal shares", SRC_C),
   show="According to the complaint, Backward Hat Capital was founded in or about July 2022 by three people: Williams, Johnson, and a third co-founder the complaint does not name. Each held an equal share."),
 L("Williams was fifty-one, from Kokomo. Johnson was twenty-nine, from Zionsville, outside Indianapolis. The audit reports investors later received called Williams the Managing Partner and C.E.O., and Johnson the Managing Director of Algorithmic Strategy.",
   doc("titles", C + "¶ 14(a)", "“Managing Partner/CEO”", SRC_C),
   show="Williams was 51, from Kokomo. Johnson was 29, from Zionsville, outside Indianapolis. The audit reports investors later received called Williams the \"Managing Partner/CEO\", and Johnson the \"Managing Director, Algorithmic Strategy.\""),
 L("The pitch was forex. Foreign exchange: trading one currency against another, dollars against euros, yen against pounds, looking for tiny price gaps.",
   dict(type="big", kicker="THE PITCH", lines=["Forex.", "Currency against|currency."], src=SRC_C)),
 L("A marketing deck from late twenty twenty-three said Backward Hat started out of the desire to help friends and family navigate the complexities of the Forex arena, and had grown at a staggering rate.",
   doc("deck", C + "¶ 13 · 2023 MARKETING DECK", "“grown … at a staggering rate”", SRC_C),
   show="A marketing deck from late 2023 said Backward Hat \"started out of the desire to help friends and family navigate the complexities of the Forex arena\", and had grown \"at a staggering rate.\""),
 L("The website described forex pair arbitrage, using the firm's own proprietary automation and algorithms. By the complaint's count, there were more than twelve separate funds.",
   doc("twelve", C + "¶ 12–13", "More than twelve separate funds", SRC_C)),
 L("And the returns were the hook. The statements investors saw typically showed more than six percent a month.",
   doc("ov_6pct", C + "¶ 9", "“typically exceeded 6% per month”", SRC_C),
   show="And the returns were the hook. The statements investors saw typically showed more than 6% a month."),
 L("Do the math, and the complaint does: compounded, that is more than one hundred percent a year. An investor would more than double their money in twelve months.",
   dict(type="stat", kicker="6% A MONTH, COMPOUNDED", value="100%+", label="a year — money doubled in 12 months", src=SRC_C),
   show="Do the math, and the complaint does: compounded, that is more than 100% a year. An investor would more than double their money in 12 months."),
 L("Which raises a simple question. Who decided what that monthly number was?",
   dict(type="big", lines=["Who picked", "the number?"], src=SRC_C)),
 # II
 L("Chapter two. The number.", dict(type="chapter", n="II", title="The Number")),
 L("Investigators say they reviewed Backward Hat's own internal spreadsheets. Every fund, they say, earned the same percentage each month, except one more aggressive fund that earned more.",
   doc("same_rate", C + "¶ 16", "The same return, every fund, every month", SRC_C)),
 L("From January to August twenty twenty-six, according to those records, the regular funds never fell below six percent in a month. The aggressive fund never fell below nine and a half.",
   dict(type="bars", kicker="MONTHLY RETURN · JAN–AUG 2026 · PER BACKWARD HAT RECORDS", title="The lowest month", items=[{"label": "Regular funds", "value": 6, "display": "never below 6%"}, {"label": "\"Aggressive\" fund", "value": 9.5, "display": "never below 9.5%"}], src=SRC_C),
   show="From January to August 2026, according to those records, the regular funds never fell below 6% in a month. The aggressive fund never fell below 9.5%."),
 L("On the investor dashboard, from October twenty twenty-three to September twenty twenty-six, the monthly rate shown was always between six point oh one and seven point two one percent. Not one month below six.",
   doc("dashboard", C + "¶ 17 · THE DASHBOARD", "“between 6.01% and 7.21%”", SRC_C),
   show="On the investor dashboard, from October 2023 to September 2026, the monthly rate shown was always between 6.01% and 7.21%. Not one month below six."),
 L("So where did the rate come from? According to the complaint, each month Williams himself set the return rate used to value every investor's account.",
   doc("set_rate", C + "¶ 18", "“WILLIAMS set the return rate”", SRC_C)),
 L("August fifth, twenty twenty-six. An employee texts him a list of past returns: For returns tomorrow. Let me know if you need anything else. Williams replies with four characters. Six point six two.",
   doc("aug5", C + "¶ 18 · AUG 5, 2026", "WILLIAMS responded with “6.62”", SRC_C),
   show="August 5, 2026. An employee texts him a list of past returns: \"For returns tomorrow. Let me know if you need anything else.\" Williams replies with four characters. \"6.62.\""),
 L("The agent writes that six point six two percent was the rate Backward Hat then used for its regular funds for July.",
   dict(type="stat", kicker="JULY 2026 · REGULAR FUNDS", value="6.62%", label="the number in the text, per the agent", src=SRC_C),
   show="The agent writes that 6.62% was the rate Backward Hat then used for its regular funds for July."),
 L("And then the exchange from May. Ten point oh one, does this sound right. What was it last month. Nine point five one. Let's do nine point nine one, bumped it up a bit.",
   dict(type="quote", q="What was it last month? … Let’s do 9.91 bumped it up a bit", case="Phillip Patrick Williams, May 14, 2026", doc="Texts quoted in the criminal complaint, ¶ 18", cite=SRC_C),
   show="And then the exchange from May. \"10.01%, does this sound right?\" \"What was it last month?\" \"9.51%.\" \"Let's do 9.91, bumped it up a bit.\""),
 L("If the returns were set by text, what happened to the money itself? The bank records tell that part.",
   dict(type="big", lines=["Then where", "did the money|go?"], src=SRC_C)),
 # III
 L("Chapter three. The money.", dict(type="chapter", n="III", title="The Money")),
 L("Investigators say they traced Backward Hat's bank and cryptocurrency exchange records. More than two thousand investors, more than six hundred million dollars in.",
   doc("ov_600", C + "¶ 9", "“more than $600 million … over 2,000 investors”", SRC_C),
   show="Investigators say they traced Backward Hat's bank and cryptocurrency exchange records. More than 2,000 investors, more than $600 million in."),
 L("At least about two hundred million dollars, the complaint says, went back out to earlier investors, paid with new investors' money, in what it calls a Ponzi scheme-like fashion.",
   doc("ponzi200", C + "¶ 19(b)", "“in a Ponzi scheme-like fashion”", SRC_C),
   show="At least about $200 million, the complaint says, went back out to earlier investors, paid with new investors' money, in what it calls a \"Ponzi scheme-like fashion.\""),
 L("More than about two hundred million went to the founders, and to what Backward Hat called G.P.s: people enlisted to bring in more investors.",
   doc("gp200", C + "¶ 19(c)", "Founders and \"GPs\"", SRC_C),
   show="More than about $200 million went to the founders, and to what Backward Hat called \"GPs\": people enlisted to bring in more investors."),
 L("Of that, the complaint says, more than one hundred thirty million dollars went to accounts controlled by Phillip Williams. More than forty million to accounts controlled by Devin Johnson.",
   dict(type="bars", kicker="WHERE THE MONEY WENT · PER THE COMPLAINT", title="Out of $600M+ raised", items=[{"label": "Paid back to earlier investors", "value": 200, "display": "≈$200M+"}, {"label": "Founders & GPs (total)", "value": 200, "display": "$200M+"}, {"label": "…of which to Williams", "value": 130, "display": "$130M+"}, {"label": "…of which to Johnson", "value": 40, "display": "$40M+"}], src=SRC_C),
   show="Of that, the complaint says, more than $130 million went to accounts controlled by Phillip Williams. More than $40 million to accounts controlled by Devin Johnson."),
 L("And the trading, the forex algorithm at the heart of the pitch? Only minimal funds, the agent writes, appear to have been potentially used for forex trading.",
   doc("minimal", C + "¶ 19(d)", "“Only minimal funds”", SRC_C)),
 L("One more detail. On February twelfth, twenty twenty-six, an employee noticed that Johnson had moved about three hundred thousand dollars from a Backward Hat account into his personal account. Confronted, the complaint says, he put it back.",
   doc("k300", C + "¶ 20 · FEB 12, 2026", "About $300,000 — then returned", SRC_C),
   show="One more detail. On February 12, 2026, an employee noticed that Johnson had moved about $300,000 from a Backward Hat account into his personal account. Confronted, the complaint says, he put it back."),
 L("So how did a fund like this keep raising money for three years? Investors had a document that seemed to answer every doubt. An independent audit.",
   dict(type="big", lines=["Three years.", "One document:|“Independent.”"], src=SRC_C)),
 # IV
 L("Chapter four. The audit.", dict(type="chapter", n="IV", title="The Audit")),
 L("Backward Hat hired a firm to produce an Independent Financial Audit and Quality of Earnings reports, covering twenty twenty-three, twenty twenty-four and twenty twenty-five.",
   doc("auditor", C + "¶ 14", "“Independent Financial Audit”", SRC_C),
   show="Backward Hat hired a firm to produce an \"Independent Financial Audit\" and \"Quality of Earnings\" reports, covering 2023, 2024 and 2025."),
 L("The audit reported an average gross return of six point three percent a month and concluded that the fund exhibits strong financial integrity, sound governance, and consistent performance across all audited periods.",
   doc("integrity", C + "¶ 14(b)", "“strong financial integrity, sound governance”", SRC_C),
   show="The audit reported an average gross return of 6.3% and concluded that the fund \"exhibits strong financial integrity, sound governance, and consistent performance across all audited periods.\""),
 L("An opinion letter said the financial statements present fairly, in all material respects, the fund's financial position. And the reports called the audit and the auditor independent, again and again.",
   dict(type="quote", q="the financial statements present fairly, in all material respects, the financial position of [the fund]", case="\"Independent Auditor's Opinion Letter\"", doc="As quoted in the criminal complaint, ¶ 14(c)", cite=SRC_C)),
 L("On November fourteenth, twenty twenty-five, the complaint says, Johnson sent those reports to a prospective investor. That person invested.",
   doc("sent_audit", C + "¶ 15 · NOV 14, 2025", "Sent to a prospective investor", SRC_C),
   show="On November 14, 2025, the complaint says, Johnson sent those reports to a prospective investor. That person invested."),
 L("Now the other side of that audit. According to the complaint, Phillip Williams had co-founded a company with the auditor's own C.E.O.",
   doc("cofounded", C + "¶ 21(a)", "Williams “co-founded a company with the CEO of the Auditor”", SRC_C),
   show="Now the other side of that audit. According to the complaint, Phillip Williams had co-founded a company with the auditor's own CEO."),
 L("And on May twenty-ninth, twenty twenty-six, that C.E.O. emailed Johnson about the significant amount of work, value creation, introductions, and commitments that remain unresolved from the past several years.",
   doc("may29", C + "¶ 21(b) · MAY 29, 2026", "“commitments that remain unresolved”", SRC_C),
   show="And on May 29, 2026, that CEO emailed Johnson about \"the significant amount of work, value creation, introductions, and commitments that remain unresolved from the past several years.\""),
 L("He wrote that if those commitments had been honored, he would have accumulated no less than two million dollars in his personal Backward Hat account. The auditor, prosecutors say, had his own stake in the fund he was auditing.",
   doc("two_m", C + "¶ 21(b)(iii)", "“no less than $2,000,000”", SRC_C),
   show="He wrote that if those commitments had been honored, he would have \"accumulated no less than $2,000,000\" in his personal Backward Hat account. The auditor, prosecutors say, had his own stake in the fund he was auditing."),
 L("And while the audit was still being sent out, the complaint says Johnson was already building a second fund. With a name built for twenty twenty-five.",
   dict(type="big", lines=["A second fund.", "Its name:|AI Capital."], src=SRC_C)),
 # V
 L("Chapter five. AI Capital.", dict(type="chapter", n="V", title="AI Capital")),
 L("Since at least August twenty twenty-five, according to the complaint, Johnson, with Williams's knowledge, tried to expand the scheme through a related fund called A.I. Capital L.P.",
   doc("aicap", C + "¶ 22", "“AI Capital LP”", SRC_C),
   show="Since at least August 2025, according to the complaint, Johnson, with Williams's knowledge, tried to expand the scheme through a related fund called AI Capital LP."),
 L("Its pitch: the same supposed forex algorithm. Its marketing listed Williams as Investment Manager and Strategic Advisor.",
   doc("aicap_mgr", C + "¶ 23(b)", "“Investment Manager and Strategic Advisor”", SRC_C),
   show="Its pitch: the same supposed forex algorithm. Its marketing listed Williams as \"Investment Manager and Strategic Advisor.\""),
 L("A data room for prospective investors held a spreadsheet titled Trades, B.H., presented as an export of executed trades from the fund that supports A.I. Capital, showing profitable forex trading over about three weeks in the summer of twenty twenty-four.",
   doc("aicap_trades", C + "¶ 23(c)", "“Trades – BH (2025.09.04)”", SRC_C),
   show="A data room for prospective investors held a spreadsheet titled \"Trades – BH\", presented as an export of executed trades from \"the fund that supports AI Capital\", showing profitable forex trading over about three weeks in the summer of 2024."),
 L("And in one presentation, the complaint says, Johnson told a prospective investor that A.I. Capital had obtained seventy-five million dollars in funding. In fact, prosecutors say, it had not received any investor money at all.",
   doc("aicap_75", C + "¶ 23(d)", "$75 million claimed — $0 received, prosecutors say", SRC_C),
   show="And in one presentation, the complaint says, Johnson told a prospective investor that AI Capital had obtained $75 million in funding. In fact, prosecutors say, it had not received any investor money at all."),
 L("Then, in the summer of twenty twenty-six, investors started asking for their money back.",
   dict(type="big", lines=["Summer 2026.", "Investors asked|for their money."], src=SRC_C),
   show="Then, in the summer of 2026, investors started asking for their money back."),
 # VI
 L("Chapter six. The delays.", dict(type="chapter", n="VI", title="The Delays")),
 L("Beginning that summer, the complaint says, Backward Hat had difficulty meeting withdrawal requests. And the explanations kept changing.",
   doc("summer", C + "¶ 24", "Difficulty meeting withdrawal requests", SRC_C)),
 L("October twelfth. Williams sends a general partner a draft email for investors: the standard processing time for all distributions is now fifteen to twenty-five business days, citing recent changes in international requirements. The old window, the agent notes, was ten to fifteen.",
   doc("oct12", C + "¶ 25(a) · OCT 12, 2026", "“15-25 business days”", SRC_C),
   show="October 12. Williams sends a general partner a draft email for investors: the standard processing time for all distributions is now 15–25 business days, citing \"recent changes in international requirements.\" The old window, the agent notes, was 10–15."),
 L("October nineteenth. A general partner who stepped in to coordinate tells all the G.P.s the problem is a transition in prime-broker arrangements. Liquidity, the email says, continues to arrive in increments rather than through one larger release.",
   doc("oct19", C + "¶ 25(b) · OCT 19, 2026", "“Liquidity continues to arrive in increments”", SRC_C),
   show="October 19. A general partner who \"stepped in to coordinate\" tells all the GPs the problem is \"a transition\" in \"prime-broker arrangements.\" \"Liquidity continues to arrive in increments rather than through one larger release.\""),
 L("November thirteenth. Williams emails investors himself: higher-than-usual withdrawal volume, he writes, triggered additional verification checks by a third-party identity validator.",
   doc("nov13", C + "¶ 25(c) · NOV 13, 2026", "“a third-party identity validator”", SRC_C),
   show="November 13. Williams emails investors himself: higher-than-usual withdrawal volume, he writes, \"triggered additional verification checks by a third-party identity validator.\""),
 L("The agent's version is different. At the same time, he writes, Williams was trying to find an independent source of funding to cover the withdrawals, because by the summer of twenty twenty-six Backward Hat had dissipated most investor assets.",
   doc("dissipated", C + "¶ 26", "“dissipated most investor assets”", SRC_C),
   show="The agent's version is different. At the same time, he writes, Williams was trying to find an independent source of funding to cover the withdrawals, because by the summer of 2026 Backward Hat had \"dissipated most investor assets.\""),
 L("And the door was still open. On October sixth, an undercover I.R.S. employee emailed Backward Hat posing as a would-be investor. On October twentieth, the reply came back: We are accepting new investors at the moment.",
   doc("uc1", C + "¶ 27 · IRS UNDERCOVER", "“accepting new investors at the moment”", SRC_C),
   show="And the door was still open. On October 6, an undercover IRS employee emailed Backward Hat posing as a would-be investor. On October 20, the reply came back: \"[W]e are accepting new investors at the moment.\""),
 L("On November sixth, an email to an investor: If you sent a contribution recently and don't see it yet, please reply with the date, amount, and sending bank so we can match it quickly. Twelve days later, the agents came.",
   doc("nov6", C + "¶ 27 · NOV 6, 2026", "“If you sent a contribution recently …”", SRC_C),
   show="On November 6, an email to an investor: \"If you sent a contribution recently and don't see it yet, please reply with the date, amount, and sending bank so we can match it quickly.\" 12 days later, the agents came."),
 # VII
 L("Chapter seven. The arrests.", dict(type="chapter", n="VII", title="The Arrests")),
 L("On November seventeenth, Homeland Security Investigations Special Agent Robert Fanesi swore to the complaint before Magistrate Judge Gary Stein in Manhattan. It was filed under seal.",
   doc("caption", "S.D.N.Y. · SEALED COMPLAINT · SWORN NOV 17, 2026", "United States v. Williams and Johnson", SRC_C, pan=[0.0, 0.05]),
   show="On November 17, Homeland Security Investigations Special Agent Robert Fanesi swore to the complaint before Magistrate Judge Gary Stein in Manhattan. It was filed under seal."),
 L("The next morning, it was unsealed. Williams was arrested in Kokomo and brought before a federal court in the Southern District of Indiana. Johnson was arrested in Gilbert, Arizona, to appear in federal court there the next day.",
   doc("pr:arrest", PR, "Arrested “this morning”", SRC_PR),
   show="The next morning, it was unsealed. Williams was arrested in Kokomo and brought before a federal court in the Southern District of Indiana. Johnson was arrested in Gilbert, Arizona, to appear in federal court there the next day."),
 L("Each is charged with securities fraud and conspiracy to commit wire fraud, each carrying up to twenty years, and conspiracy to commit securities fraud, up to five. Any sentence, the release notes, would be up to a judge.",
   dict(type="list", kicker="THE CHARGES · EACH DEFENDANT", items=[["20 yrs max", "Securities fraud"], ["20 yrs max", "Conspiracy to commit wire fraud"], ["5 yrs max", "Conspiracy to commit securities fraud"]], src=SRC_PR),
   show="Each is charged with securities fraud and conspiracy to commit wire fraud, each carrying up to 20 years, and conspiracy to commit securities fraud, up to 5. Any sentence, the release notes, would be up to a judge."),
 L("U.S. Attorney Jamie McDonald called it, quote, alleging a six-hundred-million-dollar investment fraud scheme. The Homeland Security Investigations, F.B.I., and I.R.S. Criminal Investigation offices in New York, Indianapolis and Chicago worked the case.",
   doc("pr:mcdonald", PR, "“alleging a $600 million investment fraud scheme”", SRC_PR),
   show="U.S. Attorney Jamie McDonald called it, quote, \"alleging a $600 million investment fraud scheme.\" The HSI, FBI and IRS Criminal Investigation offices in New York, Indianapolis and Chicago worked the case."),
 L("Local station WRTV reported that the S.E.C. and the Commodity Futures Trading Commission have also filed civil actions against both men.",
   dict(type="big", kicker="ALSO REPORTED", lines=["SEC + CFTC:", "civil actions|filed too."], src=SRC_WRTV),
   show="Local station WRTV reported that the SEC and the Commodity Futures Trading Commission have also filed civil actions against both men."),
 L("And one fraud investigator, Barry Minkow, wrote the same day that he had filed a report on Backward Hat with regulators back in July, and had been asked not to discuss the case publicly. That is his account.",
   dict(type="quote", q="Do not discuss this case publicly.", case="Barry Minkow, describing a request relayed by his lawyers", doc="\"One Minute On Fraud\", Nov 18, 2026", cite=SRC_MINKOW),
   show="And one fraud investigator, Barry Minkow, wrote the same day that he had filed a report on Backward Hat with regulators back in July, and had been asked not to discuss the case publicly. That is his account."),
 L("What do the defendants say? So far, nothing public. A Justice Department spokesperson said both were using appointed counsel at their first appearances, and the Indianapolis Business Journal's calls to them got no immediate response.",
   dict(type="big", kicker="THEIR SIDE", lines=["No public", "statement|yet."], src=SRC_IBJ),
   show="What do the defendants say? So far, nothing public. A Justice Department spokesperson said both were using appointed counsel at their first appearances, and the Indianapolis Business Journal's calls to them got no immediate response."),
 L("The F.B.I. is asking anyone who invested to come forward through a page for Backward Hat investors.",
   doc("pr:victims", PR, "fbi.gov/backwardhatinvestors", SRC_PR),
   show="The FBI is asking anyone who invested to come forward through a page for Backward Hat investors: fbi.gov/backwardhatinvestors."),
 L("And the release ends where this video must too. The charges contained in the complaint are merely accusations, and the defendants are presumed innocent unless and until proven guilty.",
   doc("pr:presumed", PR, "“merely accusations”", SRC_PR)),
 L("But the head of the I.R.S. Criminal Investigation office in Chicago, Robert Kuszynski, left one line that works for anyone, anywhere. When someone promises extraordinary returns with little risk, ask hard questions. Easy money often comes at someone else's expense.",
   doc("pr:hardq", PR, "“ask hard questions”", SRC_PR),
   show="But the head of the IRS Criminal Investigation office in Chicago, Robert Kuszynski, left one line that works for anyone, anywhere. \"When someone promises extraordinary returns with little risk, ask hard questions. Easy money often comes at someone else's expense.\""),
 L("Six percent a month, every month, and an audit that said it was all real. Would you have asked the hard questions? Tell us in the comments.",
   dict(type="big", lines=["6% a month.", "Would you|have asked?"], src=SRC_C),
   show="6% a month, every month, and an audit that said it was all real. Would you have asked the hard questions? Tell us in the comments."),
 L("This is SWORN. Real trials. Real evidence. The verdict.", dict(type="end")),
]

# ---- fact-check fixes (factcheck.md, 43 items) ----
def F(i, say=None, show=None, **sc):
    l = lines[i]
    if say is not None: l["say"] = say
    if show is not None: l["show"] = show
    elif say is not None: l.pop("show", None)
    for k, v in sc.items(): l["scene"][k] = v
F(0, "May fourteenth, twenty twenty-six. According to federal prosecutors, a text message arrives for the man running an investment firm that raised more than six hundred million dollars. Aggressive fund, ten point oh one percent. Does this sound right?",
  "May 14, 2026. According to federal prosecutors, a text message arrives for the man running an investment firm that raised more than $600 million. \"Aggressive fund 10.01% / Does this sound right?\"")
F(1, "He asks what it was last month. Nine point five one, the employee says. Later in the exchange, according to federal prosecutors, he writes: Let's do nine point nine one, bumped it up a bit.",
  "He asks what it was last month. \"9.51% last month,\" the employee says. Later in the exchange, according to federal prosecutors, he writes: \"… Let's do 9.91 bumped it up a bit.\"")
F(3, "According to prosecutors, more than two thousand investors put in more than six hundred million dollars. They were told the fund typically made more than six percent a month.",
  "According to prosecutors, more than 2,000 investors put in more than $600 million. They were told the fund typically made more than 6% a month.")
F(4, big="Securities fraud & conspiracy")
F(8, "Today Williams is fifty-one, of Kokomo. Johnson is twenty-nine, of Zionsville, outside Indianapolis. The audit reports investors later received called Williams the Managing Partner and C.E.O., and Johnson the Managing Director of Algorithmic Strategy.",
  "Today Williams is 51, of Kokomo. Johnson is 29, of Zionsville, outside Indianapolis. The audit reports investors later received called Williams the \"Managing Partner/CEO\", and Johnson the \"Managing Director, Algorithmic Strategy.\"")
F(13, label="a year, on paper: money would more than double")
F(16, title="The same return, every fund but one")
F(22, "And then the exchange from May. Aggressive fund, ten point oh one percent, does this sound right. What was it last month. Nine point five one last month. Let's do nine point nine one, bumped it up a bit.",
  "And then the exchange from May. \"Aggressive fund 10.01% / Does this sound right?\" \"What was it last month?\" \"9.51% last month …\" \"… Let's do 9.91 bumped it up a bit\"")
F(23, "If the returns were set by text, what happened to the money itself? The complaint points to bank records.")
F(27, "More than about two hundred million went to the founders and to general partners, or G.P.s, whom the complaint describes as people Backward Hat enlisted to bring in more investors.",
  "More than about $200 million went to the founders and to general partners, or \"GPs\", whom the complaint describes as people Backward Hat enlisted to bring in more investors.")
F(30, "One more detail. On February twelfth, twenty twenty-six, according to the complaint, an employee learned that Johnson had moved about three hundred thousand dollars from a Backward Hat account into his personal account. Confronted, the complaint says, he put it back.",
  "One more detail. On February 12, 2026, according to the complaint, an employee learned that Johnson had moved about $300,000 from a Backward Hat account into his personal account. Confronted, the complaint says, he put it back.")
F(31, "So how did Backward Hat keep raising money for more than four years? Investors had a document that seemed to answer every doubt. An independent audit.",
  lines=["Four-plus years.", "One document:|“Independent.”"])
F(34, "The audit reported an average gross return of six point three percent from twenty twenty-three through mid twenty twenty-five, and concluded that the fund exhibits strong financial integrity, sound governance, and consistent performance across all audited periods.",
  "The audit reported an average gross return of 6.3% from 2023 through mid-2025, and concluded that the fund \"exhibits strong financial integrity, sound governance, and consistent performance across all audited periods.\"")
F(39, "He wrote that if those commitments had been honored as represented, he would have accumulated no less than two million dollars in his personal Backward Hat account. They had not yet materialized, he wrote. Prosecutors say the auditor's C.E.O. had personal interests in Backward Hat that investors were never told about. The complaint does not name the auditor or its C.E.O., and neither is charged.",
  "He wrote that if those commitments had been honored as represented, he would have \"accumulated no less than $2,000,000\" in his personal Backward Hat account. They had \"not yet materialized,\" he wrote. Prosecutors say the auditor's CEO had personal interests in Backward Hat that investors were never told about. The complaint does not name the auditor or its CEO, and neither is charged.")
F(40, "And while the audit was still being sent out, the complaint says Johnson was already building another fund. With a name built for twenty twenty-five.",
  "And while the audit was still being sent out, the complaint says Johnson was already building another fund. With a name built for 2025.",
  lines=["Another fund.", "Its name:|AI Capital."])
F(44, "A data room for prospective investors held a spreadsheet titled Trades, B.H., presented as an export of executed trades from the fund that supports A.I. Capital. It purported to show profitable forex trading over about three weeks in the summer of twenty twenty-four.",
  "A data room for prospective investors held a spreadsheet titled \"Trades – BH\", presented as an export of executed trades from \"the fund that supports AI Capital.\" It purported to show profitable forex trading over about three weeks in the summer of 2024.")
F(46, "Then, in the summer of twenty twenty-six, according to the complaint, Backward Hat began struggling to pay investors who asked for their money back.",
  "Then, in the summer of 2026, according to the complaint, Backward Hat began struggling to pay investors who asked for their money back.",
  lines=["Summer 2026.", "Withdrawals|delayed."])
F(50, title="“[l]iquidity continues to arrive in increments”")
F(56, "On November seventeenth, Homeland Security Investigations Special Agent Robert Fanesi swore to the complaint by telephone before Magistrate Judge Gary Stein of the Southern District of New York. It was filed under seal.",
  "On November 17, Homeland Security Investigations Special Agent Robert Fanesi swore to the complaint by telephone before Magistrate Judge Gary Stein of the Southern District of New York. It was filed under seal.")
F(57, "The next day, it was unsealed. Williams was arrested that morning in Kokomo and brought before a federal court in the Southern District of Indiana. Johnson was arrested in Gilbert, Arizona, to appear in federal court there the next day.")
F(59, "U.S. Attorney Jamie McDonald said the charges are, quote, alleging a six-hundred-million-dollar investment fraud scheme. The Homeland Security Investigations, F.B.I., and I.R.S. Criminal Investigation offices in New York, Indianapolis and Chicago worked the case.",
  "U.S. Attorney Jamie McDonald said the charges are \"alleging a $600 million investment fraud scheme.\" The HSI, FBI and IRS Criminal Investigation offices in New York, Indianapolis and Chicago worked the case.")
F(61, "And Barry Minkow, who writes a fraud newsletter, wrote the same day that he and his lawyer had filed a detailed report on Backward Hat back in July, and that a request then came through his lawyers: do not discuss this case publicly. That is his account.",
  case="Barry Minkow, describing a request that came through his lawyers")
F(62, "What do the defendants say? We found no public statement from either man. A Justice Department spokesperson said both were using appointed counsel for their initial court appearances, and the Indianapolis Business Journal said phone messages it left at numbers it believes are theirs got no immediate response.",
  lines=["No public", "statement|found."])
F(65, "But the acting head of the I.R.S. Criminal Investigation office in Chicago, Robert Kuszynski, left one line that works for anyone, anywhere. When someone promises extraordinary returns with little risk, ask hard questions. Easy money often comes at someone else's expense.",
  "But the acting head of the IRS Criminal Investigation office in Chicago, Robert Kuszynski, left one line that works for anyone, anywhere. \"When someone promises extraordinary returns with little risk, ask hard questions. Easy money often comes at someone else's expense.\"")
F(66, "More than six percent a month on paper, month after month, and an audit that called it sound. Would you have asked the hard questions? Tell us in the comments.",
  "6%+ a month on paper, month after month, and an audit that called it sound. Would you have asked the hard questions? Tell us in the comments.")
json.dump({"label": "SWORN · CASE 019", "lines": lines}, open(os.path.join(HERE, "episode.json"), "w"), indent=1, ensure_ascii=False)
print(len(lines), "lines,", sum(len(l["say"].split()) for l in lines), "words")
