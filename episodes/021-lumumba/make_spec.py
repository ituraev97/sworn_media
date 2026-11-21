import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
def doc(key, kicker, title, src, pan=None):
    img, a, b = HL[key]
    box = [0.0, a, 1.0, round(b - a, 4)]
    if pan is None:
        c = a + (b - a) / 2
        pan = [max(0.0, round(c - 0.22, 3)), max(0.0, round(c - 0.16, 3))]
    return dict(type="doc", img=f"img/{img}.jpg", pan=pan, hl=box, kicker=kicker, title=title, src=src)
def photo(img, caption, src):
    return dict(type="photo", img=f"img/{img}.jpg", caption=caption, src=src, fit="cover")
SRC_I = "Indictment, U.S. v. Owens, Lumumba & Banks (S.D. Miss. 3:24-cr-103, filed Oct 23, 2024; unsealed Nov 7, 2024)"
SRC_IPH = "Image printed in the indictment (S.D. Miss. 3:24-cr-103) — FBI recording"
SRC_N = "Notice of maximum penalties, Dkt. 3-1 (S.D. Miss. 3:24-cr-103)"
SRC_PR = "U.S. Attorney's Office, S.D. Miss., press release (Nov 7, 2024)"
SRC_WLBT = "WLBT (Anthony Warren, Quentin Smith), Nov 20, 2026 — sentencing hearing"
SRC_WLBT7 = "WLBT/WLOX (July 6, 2026) — plea hearing"
SRC_MFP = "Mississippi Free Press (July 6, 2026) — plea hearing"
SRC_MT = "Mississippi Today (Nov 5, 2026) — Owens sentencing hearing"
SRC_WAPT = "WAPT (Nov 20, 2026)"
SRC_ST = "SuperTalk Mississippi (Nov 20, 2026)"
SRC_MAG = "Magnolia Tribune (Nov 20, 2026)"
SRC_HILL = "The Hill (Nov 20, 2026)"
I = "INDICTMENT · "
AL = "ALLEGATION · "
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
SENT = dict(type="verdict", kicker="NOVEMBER 20, 2026 · JACKSON, MISS.", stamp="SENTENCED", big="37 Months", sub="Chokwe Antar Lumumba · ex-mayor of Jackson · U.S. District Judge Daniel Jordan")
lines = [
 # COLD OPEN
 L("April second, twenty twenty-four. A yacht in Fort Lauderdale, Florida. In a private room on board, the mayor of Mississippi's capital city picks up his phone.",
   photo("ph_call", "INDICTMENT ¶ 56 · APRIL 2, 2024 · FBI RECORDING", SRC_IPH),
   show="April 2, 2024. A yacht in Fort Lauderdale, Florida. In a private room on board, the mayor of Mississippi's capital city picks up his phone."),
 L("He calls a city employee back home in Jackson, and says to move a deadline. The deadline for developers to compete for a project downtown. From April thirtieth, to April fifteenth.",
   doc("i_call", I + "¶ 56 · APRIL 2, 2024", "April 30 → April 15", SRC_I),
   show="He calls a city employee back home in Jackson, and says to move a deadline. The deadline for developers to compete for a project downtown. From April 30, to April 15."),
 L("Later in the meeting, he is handed an envelope. Inside, five checks of ten thousand dollars each.",
   doc("i_checks", I + "¶ 57", "Five $10,000 checks", SRC_I),
   show="Later in the meeting, he is handed an envelope. Inside, five checks of $10,000 each."),
 L("The men across the table say they are real estate developers from Nashville. They are not. They are working for the F.B.I. And the meeting is being recorded, on audio and video.",
   doc("i_yacht2", I + "¶ 55", "“audio and video recorded”", SRC_I),
   show="The men across the table say they are real estate developers from Nashville. They are not. They are working for the FBI. And the meeting is being recorded, on audio and video."),
 L("On November twentieth, twenty twenty-six, that mayor, Chokwe Antar Lumumba, stood before a federal judge in Jackson. He had already pleaded guilty. The sentence: thirty-seven months in prison.",
   SENT, show="On November 20, 2026, that mayor, Chokwe Antar Lumumba, stood before a federal judge in Jackson. He had already pleaded guilty. The sentence: 37 months in prison."),
 L("He was not alone. The county's district attorney, and the president of the city council, went down too. This is how the F.B.I.'s fake developers bought a city's leaders, from the court records.",
   dict(type="title", kicker="SWORN · CASE 021 · BREAKING", title="The Mayor and|the Fake Developers", sub="United States v. Owens, Lumumba & Banks · S.D. Miss. · sentenced Nov 20, 2026"),
   show="He was not alone. The county's district attorney, and the president of the city council, went down too. This is how the FBI's fake developers bought a city's leaders, from the court records."),
 # I
 L("Chapter one. The developers.", dict(type="chapter", n="I", title="The Developers")),
 L("Jackson, Mississippi. The state capital. Since around two thousand eight, the city has been trying to develop a seven point seven five acre plot downtown, near the convention center.",
   doc("i_hud", I + "¶ 16 · DOWNTOWN JACKSON", "A 7.75-acre plot since 2008", SRC_I),
   show="Jackson, Mississippi. The state capital. Since around 2008, the city has been trying to develop a 7.75-acre plot downtown, near the convention center."),
 L("To pay for it, the city took out a multi-million-dollar federal loan. The plan was a hotel, a parking garage and green space on what was then a parking lot. In July twenty twenty-three, the city asked for proposals. According to the indictment, not one qualified developer responded.",
   doc("i_rfp", I + "¶ 18 · JULY 2023", "“no responses from qualified developers”", SRC_I),
   show="To pay for it, the city took out a multi-million-dollar federal loan. The plan was a hotel, a parking garage and green space on what was then a parking lot. In July 2023, the city asked for proposals. According to the indictment, not one qualified developer responded."),
 L("That same summer, two men started showing up in Jackson. They said they were developers from Nashville, Tennessee. One was a confidential source employed by the F.B.I. The other was an undercover F.B.I. employee.",
   doc("i_fbi", I + "¶ 1", "“working for the Federal Bureau of Investigation”", SRC_I),
   show="That same summer, two men started showing up in Jackson. They said they were developers from Nashville, Tennessee. One was a confidential source employed by the FBI. The other was an undercover FBI employee."),
 L("In August twenty twenty-three, a local man introduced them to the most powerful prosecutor in the county. Jody Owens, the district attorney of Hinds County, which includes Jackson.",
   doc("i_intro", I + "¶ 21 · AUGUST 14, 2023", "The introduction", SRC_I),
   show="In August 2023, a local man introduced them to the most powerful prosecutor in the county. Jody Owens, the district attorney of Hinds County, which includes Jackson."),
 L("In October, the F.B.I. flew Owens and his associates to Nashville on a private jet, on the developers' behalf.",
   doc("i_jet", I + "¶ 22 · OCTOBER 9–11, 2023", "A private jet, paid for by the FBI", SRC_I),
   show="In October, the FBI flew Owens and his associates to Nashville on a private jet, on the developers' behalf."),
 L("A week later, according to the indictment, Owens told them he and a relative owned enough of the city. And that he had a bag of information on every council member, with an expletive in the middle, that let him get votes approved.",
   dict(type="quote", q="own enough of the city … a bag of [expletive] information on all the city councilmen … get votes approved", case="Jody Owens, to the “developers” · Oct 16, 2023", doc="As quoted in the indictment, ¶ 23", cite=SRC_I),
   show="A week later, according to the indictment, Owens told them he and a relative \"own enough of the city.\" And that he had \"a bag of [expletive] information on all the city councilmen\" that let him \"get votes approved.\""),
 L("Three weeks after that, Owens won re-election as district attorney. At his victory party, when the developers congratulated him, the indictment says he told them: This is the part time job, to get the conversations and the access.",
   dict(type="quote", q="This is the part time job, to get leverage for the full-time job. This is the part time job to get the conversations and the access.", case="Jody Owens, election night · Nov 7, 2023", doc="As quoted in the indictment, ¶ 24", cite=SRC_I),
   show="Three weeks after that, Owens won re-election as district attorney. At his victory party, when the developers congratulated him, the indictment says he told them: \"This is the part time job to get the conversations and the access.\""),
 L("The next day, he and his relative negotiated their own fee for helping. Two hundred fifty thousand dollars up front. A hundred thousand each, and fifty thousand for the man who had introduced them.",
   doc("i_250k", I + "¶ 25 · NOVEMBER 8, 2023", "$250,000 up front", SRC_I),
   show="The next day, he and his relative negotiated their own fee for helping. $250,000 up front. $100,000 each, and $50,000 for the man who had introduced them."),
 L("Remember, the district attorney is the person who decides who gets prosecuted in Jackson. And he had just set a price.",
   dict(type="big", lines=["The prosecutor", "set a price."], src=SRC_I)),
 # II
 L("Chapter two. The war room.", dict(type="chapter", n="II", title="The War Room")),
 L("December thirteenth, twenty twenty-three. The F.B.I.'s jet takes Owens to Fort Lauderdale. That evening, on a yacht, the developers ask how he wants to be paid. Cash, he says. It's easier. He brought a bag.",
   doc("i_yacht1", I + "¶ 26 · DECEMBER 13, 2023", "“cash was ‘easier’”", SRC_I),
   show="December 13, 2023. The FBI's jet takes Owens to Fort Lauderdale. That evening, on a yacht, the developers ask how he wants to be paid. Cash, he says. It's \"easier.\" He brought a bag."),
 L("One of them hands him one hundred twenty-five thousand dollars in cash.",
   dict(type="stat", kicker="FORT LAUDERDALE · DEC 13, 2023", value="$125,000", label="cash to Owens, to be split three ways (indictment)", src=SRC_I),
   show="One of them hands him $125,000 in cash."),
 L("Then, the indictment says, Owens explained what they were paying for: Every police agency comes to us. Everybody needs something. Every file comes to us. Everybody needs something fixed.",
   dict(type="quote", q="So right now, every police agency comes to us. Everybody needs something. Every file comes to us. Everybody needs something fixed.", case="Jody Owens, district attorney · Dec 13, 2023", doc="As quoted in the indictment, ¶ 27", cite=SRC_I),
   show="Then, the indictment says, Owens explained what they were paying for: \"Every police agency comes to us. Everybody needs something. Every file comes to us. Everybody needs something fixed.\""),
 L("In January, they met in Owens's private office in Jackson. He called it his war room. There he gave them a tip: the city would soon ask developers for their qualifications for the downtown project.",
   doc("i_warroom", I + "¶ 28 · JANUARY 10, 2024", "The “War Room”", SRC_I)),
 L("The developers wanted it. And they wanted the city council on their side.",
   dict(type="big", lines=["They wanted the project.", "And the votes."], src=SRC_I)),
 L("The next night, in a back room, they met Aaron Banks, the president of the Jackson City Council. Asked what he would need to support them, Banks answered, according to the indictment: fifty grand as soon as possible would help.",
   doc("i_banks50", I + "¶ 30 · JANUARY 11, 2024", "“fifty grand as soon as possible would help”", SRC_I),
   show="The next night, in a back room, they met Aaron Banks, the president of the Jackson City Council. Asked what he would need to support them, Banks answered, according to the indictment: \"fifty grand as soon as possible would help.\""),
 L("Then, on February twelfth, twenty twenty-four, Owens brought the developers to dinner with the mayor.",
   dict(type="big", kicker="FEBRUARY 12, 2024", lines=["Dinner", "with the mayor."], src=SRC_I),
   show="Then, on February 12, 2024, Owens brought the developers to dinner with the mayor."),
 L("Chokwe Antar Lumumba had been mayor of Jackson since twenty seventeen. He was the son of a former mayor, and The Hill notes he became the city's youngest mayor, at thirty-four.",
   doc("i_mayor", I + "¶ 6", "Mayor since 2017", SRC_I + "; The Hill (Nov 20, 2026)"),
   show="Chokwe Antar Lumumba had been mayor of Jackson since 2017. He was the son of a former mayor, and The Hill notes he became the city's youngest mayor, at 34."),
 L("According to the indictment, Owens introduced the two men with this line: I've done background checks. They're not F.B.I., by the way.",
   doc("i_notfbi", I + "¶ 31 · FEBRUARY 12, 2024", "“They’re not FBI by the way.”", SRC_I),
   show="According to the indictment, Owens introduced the two men with this line: \"I've done background checks. They're not FBI by the way.\""),
 # re-hook
 L("They were. And from that dinner on, almost everything the mayor said and did with them would end up in an indictment.",
   dict(type="big", lines=["They were FBI.", "Everything was recorded."], src=SRC_I)),
 # III
 L("Chapter three. The pawns.", dict(type="chapter", n="III", title="The Pawns")),
 L("After the dinner, the developers worried they didn't have enough votes. Owens, according to the indictment, said they already had the leadership, the mayor and the council president. Next, he would get them the pawns.",
   doc("i_pawns", I + "¶ 32 · FEBRUARY 12, 2024", "“the pawns”", SRC_I),
   show="After the dinner, the developers worried they didn't have enough votes. Owens, according to the indictment, said they already had \"the leadership,\" the mayor and the council president. Next, he would get them \"the pawns.\""),
 L("And he explained how the money would move. Campaign contributions, from inside Mississippi. Cash in, clean checks out.",
   dict(type="quote", q="I don’t give a [expletive] where the money comes from … I’m a whole DA … I need to clean it and spread it.", case="Jody Owens, district attorney · Feb 12, 2024", doc="As quoted in the indictment, ¶ 33", cite=SRC_I)),
 L("The next day, February thirteenth, the developers handed Owens sixty thousand dollars. Twenty-five thousand for himself, twenty-five thousand for Banks, ten thousand for a second council member, Angelique Lee. Owens said he'd keep their shares in a safe, at the district attorney's office.",
   doc("i_60k", I + "¶ 34 · FEBRUARY 13, 2024", "$60,000 · “a safe at the Hinds County District Attorney’s Office”", SRC_I),
   show="The next day, February 13, the developers handed Owens $60,000. $25,000 for himself, $25,000 for Banks, $10,000 for a second council member, Angelique Lee. Owens said he'd keep their shares in a safe, at the district attorney's office."),
 L("That night Banks walked in, and Owens handed him an envelope with ten thousand dollars in cash.",
   doc("i_envelope", I + "¶ 35 · FEBRUARY 13, 2024", "An envelope: $10,000", SRC_I),
   show="That night Banks walked in, and Owens handed him an envelope with $10,000 in cash."),
 L("Lee, according to the indictment, got ten thousand dollars of her campaign debt paid off, three thousand in cash in a bag, and a shopping trip on one developer's credit card. More than six thousand dollars in luxury goods.",
   doc("i_lee", I + "¶ 52 · MARCH 27, 2024", "$3,000 in a bag · $6,000 shopping", SRC_I),
   show="Lee, according to the indictment, got $10,000 of her campaign debt paid off, $3,000 in cash in a bag, and a shopping trip on one developer's credit card. More than $6,000 in luxury goods."),
 L("Then came the question of the mayor. Why do we need him, one developer asked. Because, came the answer, he could make things a lot harder.",
   doc("i_why", I + "¶ 39 · FEBRUARY 28, 2024", "“could make things a lot harder”", SRC_I),
   show="Then came the question of the mayor. \"Why do we need [him]?\" one developer asked. Because, came the answer, he \"could make things a lot harder.\""),
 L("Owens had a warning, too. Stay away from the b-word, he said, according to the indictment. The b-word is a bad word. We don't even say it.",
   doc("i_bword", I + "¶ 40 · FEBRUARY 28, 2024", "“stay away from the ‘b-word’”", SRC_I),
   show="Owens had a warning, too. \"Stay away from the 'b-word,'\" he said, according to the indictment. \"The 'b-word' is a bad word. We don't even say it.\""),
 L("Meanwhile, the city had published its request for developers, with a deadline of March twelfth. Then the deadline was pushed back, to April thirtieth, so more developers could apply. For the developers, more time meant more competition.",
   doc("i_rfq", I + "¶ 19 · FEBRUARY 5, 2024", "Deadline: March 12, 2024", SRC_I),
   show="Meanwhile, the city had published its request for developers, with a deadline of March 12. Then the deadline was pushed back, to April 30, so more developers could apply. For the developers, more time meant more competition."),
 L("On March fifth, Owens texted the mayor. The developers had come to submit a proposal, he wrote, but the deadline had moved. And he needed to understand how to donate to the mayor's re-election campaign, quote, in a size able way.",
   doc("i_text", I + "¶ 46 · TEXT TO LUMUMBA · MARCH 5, 2024", "“in a size able way”", SRC_I),
   show="On March 5, Owens texted the mayor. The developers had come to submit a proposal, he wrote, but the deadline had moved. And he needed to understand how to donate to the mayor's re-election campaign \"in a size able way.\""),
 L("The plan, as Owens described it, was a fundraiser in Florida. Ten guys with ten checks, or ten checks in one envelope. What we used to do, he said, if people wanted to stay under the radar: a bunch of different checks from a bunch of different companies.",
   doc("i_tenchecks", I + "¶ 47 · MARCH 5, 2024", "“ten guys with ten checks”", SRC_I),
   show="The plan, as Owens described it, was a \"fundraiser\" in Florida. \"Ten guys with ten checks,\" or ten checks in one envelope. \"What we used to do, if people wanted to stay under the radar, you just give a bunch of different checks from a bunch of different companies.\""),
 L("On March ninth, Owens met the mayor at the mayor's house. The next day he told the developers everyone was on one accord. Fifty thousand dollars in Florida. And, he said, the mayor's final number was a hundred thousand.",
   doc("i_final", I + "¶ 49 · MARCH 10, 2024", "“final number” — $100,000", SRC_I),
   show="On March 9, Owens met the mayor at the mayor's house. The next day he told the developers everyone was \"on one accord.\" $50,000 in Florida. And, he said, the mayor's \"final number\" was $100,000."),
 L("In late March, the developers delivered fifty thousand dollars in cash to Owens, at the district attorney's office. He turned it into five ten-thousand-dollar campaign checks, from his relative, himself, one of his companies, and two other associates. Then he paid them all back.",
   doc("i_conv", I + "¶ 54 · MARCH 27–28, 2024", "Cash → five “campaign contribution” checks", SRC_I),
   show="In late March, the developers delivered $50,000 in cash to Owens, at the district attorney's office. He turned it into five $10,000 campaign checks, from his relative, himself, one of his companies, and two other associates. Then he paid them all back."),
 L("Five clean-looking Mississippi checks. Now all they needed was the mayor, on a boat.",
   dict(type="big", lines=["Five checks.", "One yacht."], src=SRC_I)),
 # IV
 L("Chapter four. The call.", dict(type="chapter", n="IV", title="The Call")),
 L("April second, twenty twenty-four. The mayor, Owens, his relative and the developers fly to Fort Lauderdale, on a private jet the F.B.I. paid for. They meet in a private room on a yacht. The F.B.I. records it all.",
   doc("i_yacht2", I + "¶ 55 · APRIL 2, 2024", "“audio and video recorded”", SRC_I),
   show="April 2, 2024. The mayor, Owens, his relative and the developers fly to Fort Lauderdale, on a private jet the FBI paid for. They meet in a private room on a yacht. The FBI records it all."),
 L("The indictment quotes the exchange. Owens: We want to be very mindful of out-of-state money. Lumumba: Yeah. Owens: So what this team did was give us the money, being me, and we just filtered it through several accounts. Lumumba: Yeah.",
   dict(type="quote", q="OWENS: We want to be very mindful of out-of-state money. LUMUMBA: Yeah. OWENS: So what this team did was give us the money, being me, and we just filtered it through several accounts in a way we comfortable doing. LUMUMBA: Yeah.", case="Yacht, Fort Lauderdale · April 2, 2024", doc="Recorded exchange, as quoted in the indictment, ¶ 55", cite=SRC_I, size=38)),
 L("Owens: So we did five ten-thousand-dollar checks to make it very simple. Lumumba: Yeah.",
   dict(type="quote", q="OWENS: So we did five $10,000 checks to make it very simple … LUMUMBA: Yeah.", case="Yacht, Fort Lauderdale · April 2, 2024", doc="As quoted in the indictment, ¶ 55", cite=SRC_I),
   show="Owens: \"So we did five $10,000 checks to make it very simple.\" Lumumba: \"Yeah.\""),
 L("Then one developer asked the mayor to move the deadline up, from April thirtieth to April tenth or fifteenth. The mayor picked up his phone, called a city employee, and told them: April fifteenth.",
   photo("ph_call", "INDICTMENT ¶ 56 · “LUMUMBA THEN PLACED A TELEPHONE CALL”", SRC_IPH),
   show="Then one developer asked the mayor to move the deadline up, from April 30 to April 10 or 15. The mayor picked up his phone, called a city employee, and told them: April 15."),
 L("Later, the envelope. Five ten-thousand-dollar checks. Owens told him: These checks are Mississippi checks, but they're from this group. And the mayor said: Okay.",
   dict(type="quote", q="OWENS: These checks are Mississippi checks but they’re from this group. LUMUMBA: Okay.", case="Yacht, Fort Lauderdale · April 2, 2024", doc="As quoted in the indictment, ¶ 57", cite=SRC_I),
   show="Later, the envelope. Five $10,000 checks. Owens told him: \"These checks are Mississippi checks but they're from this group.\" And the mayor said: \"Okay.\""),
 L("When a developer asked whether the deadline would really move, the mayor checked his text messages, and told them the city employee had confirmed it.",
   photo("ph_sofa", "INDICTMENT ¶¶ 57–59 · APRIL 2, 2024 · FBI RECORDING", SRC_IPH)),
 L("Why does a deadline matter? Because, as the indictment puts it, an earlier deadline made it likely that competition for the project would be eliminated. That was the official act that was for sale.",
   doc("i_worth", I + "¶ 58", "“elimination of competition”", SRC_I)),
 L("The same day, according to the indictment, Owens took another fifty thousand dollars in cash for himself, from a bag, and put it in his pockets. The F.B.I. camera was rolling.",
   photo("ph_bag", "INDICTMENT ¶ 60 · APRIL 2, 2024 · FBI RECORDING", SRC_IPH),
   show="The same day, according to the indictment, Owens took another $50,000 in cash for himself, from a bag, and put it in his pockets. The FBI camera was rolling."),
 L("That night, the group went to a local club. The indictment says the developers made five thousand dollars in cash available for the mayor and others there.",
   doc("i_club", I + "¶ 61 · APRIL 2, 2024", "$5,000 at the club", SRC_I),
   show="That night, the group went to a local club. The indictment says the developers made $5,000 in cash available for the mayor and others there."),
 L("Back in Jackson, on April fourth, the five checks went into the mayor's campaign account. The balance before the deposit, according to the indictment: four hundred sixty-five dollars and thirty cents.",
   doc("i_deposit", I + "¶ 62 · APRIL 4, 2024", "Balance before: $465.30", SRC_I),
   show="Back in Jackson, on April 4, the five checks went into the mayor's campaign account. The balance before the deposit, according to the indictment: $465.30."),
 L("The next day, a check for nine thousand five hundred dollars was made out to Lumumba from that account. Three days later, another for five thousand. Both were cashed.",
   doc("i_9500", I + "¶ 63 · APRIL 5 & 8, 2024", "$9,500 · $5,000 · cashed", SRC_I),
   show="The next day, a check for $9,500 was made out to Lumumba from that account. Three days later, another for $5,000. Both were cashed."),
 L("Fifty thousand dollars in. Fourteen thousand five hundred out, to the mayor himself. And the man who paid it all was an F.B.I. employee.",
   dict(type="bars", kicker="LUMUMBA'S CAMPAIGN ACCOUNT · APRIL 2024", title="Per the indictment", items=[{"label": "Balance before (Apr 4)", "value": 465.3, "display": "$465.30"}, {"label": "Five checks deposited", "value": 50000, "display": "$50,000"}, {"label": "Paid to Lumumba (Apr 5 & 8)", "value": 14500, "display": "$14,500"}], src=SRC_I),
   show="$50,000 in. $14,500 out, to the mayor himself. And the man who paid it all was an FBI employee."),
 # V
 L("Chapter five. The book.", dict(type="chapter", n="V", title="The Book")),
 L("Seven weeks later, on May twenty-second, twenty twenty-four, an F.B.I. agent approached the district attorney and identified himself. He asked Owens whether there were any safes or lockboxes in his office. According to the indictment, Owens answered: none exist.",
   doc("i_none", I + "COUNT 11 · MAY 22, 2024", "“none exist”", SRC_I),
   show="Seven weeks later, on May 22, 2024, an FBI agent approached the district attorney and identified himself. He asked Owens whether there were any safes or lockboxes in his office. According to the indictment, Owens answered: \"none exist.\""),
 L("That same day, the F.B.I. searched his office at the Hinds County District Attorney's Office. They found a small lockbox, made to look like a book. Its title: The Constitution of the United States of America.",
   photo("ph_book", "INDICTMENT ¶ 65 · FBI SEARCH · MAY 22, 2024", "Image printed in the indictment (S.D. Miss. 3:24-cr-103) — FBI search"),
   show="That same day, the FBI searched his office at the Hinds County District Attorney's Office. They found a small lockbox, made to look like a book. Its title: \"The Constitution of the United States of America.\""),
 L("Inside, about twenty thousand dollars in cash. About nine thousand nine hundred of it, the F.B.I. confirmed by serial numbers, was money the developers had paid Owens on the yacht in December.",
   doc("i_lockbox", I + "¶ 65", "$20,000 · $9,900 by serial number", SRC_I),
   show="Inside, about $20,000 in cash. About $9,900 of it, the FBI confirmed by serial numbers, was money the developers had paid Owens on the yacht in December."),
 L("A district attorney's cash, hidden inside the Constitution. You could not write it better. But the case was only beginning.",
   dict(type="big", lines=["Cash inside", "the Constitution."], src=SRC_I)),
 L("Angelique Lee resigned from the council and pleaded guilty in August twenty twenty-four, according to Magnolia Tribune. She was the first official charged.",
   dict(type="timeline", kicker="THE CASE · 2024", events=[{"date": "Apr 2", "text": "Yacht · five checks · the call"}, {"date": "May 22", "text": "FBI search · the book"}, {"date": "Aug", "text": "Lee pleads guilty, resigns"}, {"date": "Nov 7", "text": "Indictment unsealed"}], at=2, src=SRC_MAG + "; " + SRC_I)),
 L("On November seventh, twenty twenty-four, the indictment against Owens, Lumumba and Banks was unsealed. The mayor alone faced five counts, from bribery to honest services wire fraud and money laundering.",
   doc("pr:alleges", "U.S. ATTORNEY · S.D. MISS. · NOV 7, 2024", "Indictment unsealed", SRC_PR),
   show="On November 7, 2024, the indictment against Owens, Lumumba and Banks was unsealed. The mayor alone faced five counts, from bribery to honest services wire fraud and money laundering."),
 L("The U.S. Attorney, Todd Gee, said: Leaders who are awarded the public's trust should be focusing on the needs of the Jackson community, not looking to line their own pockets.",
   dict(type="quote", q="Leaders who are awarded the public’s trust should be focusing on the needs of the Jackson community, not looking to line their own pockets and benefit themselves", case="Todd Gee, U.S. Attorney, S.D. Miss. · Nov 7, 2024", doc="Press release", cite=SRC_PR)),
 L("And the release added the line every indictment carries: an indictment is merely an allegation. All three pleaded not guilty.",
   doc("pr:presumed", "U.S. ATTORNEY · S.D. MISS. · NOV 7, 2024", "“merely an allegation”", SRC_PR + "; Magnolia Tribune (Nov 20, 2026)")),
 L("In December twenty twenty-four, on his program Ask Antar, the mayor said he was not going to walk around as if he was guilty of something he was not, as WLBT recalled at his sentencing.",
   dict(type="quote", q="not going to walk around as if I’m guilty of something I am not.", case="Chokwe Antar Lumumba · “Ask Antar,” December 2024", doc="As quoted by WLBT", cite=SRC_WLBT)),
 L("Before trial, the three defendants asked the court to throw the case out, or to try them separately, citing entrapment, government misconduct and other grounds.",
   dict(type="big", kicker="DEFENSE MOTIONS · PER MAGNOLIA TRIBUNE", lines=["Entrapment?", "Misconduct?"], src=SRC_MAG)),
 L("And in twenty twenty-five, still under indictment, Lumumba lost his bid for a third term. John Horhn became mayor.",
   dict(type="big", kicker="2025 · JACKSON MAYOR'S RACE", lines=["Lumumba", "loses."], src=SRC_ST + "; " + SRC_HILL),
   show="And in 2025, still under indictment, Lumumba lost his bid for a third term. John Horhn became mayor."),
 # VI
 L("Chapter six. The sentence.", dict(type="chapter", n="VI", title="The Sentence")),
 L("Then, in the summer of twenty twenty-six, the case turned. About a week after Owens changed his plea, on July sixth, Lumumba pleaded guilty to a single conspiracy count. Banks did the same that afternoon.",
   dict(type="verdict", kicker="JULY 6, 2026 · JACKSON, MISS.", stamp="GUILTY PLEA", big="Lumumba", sub="One conspiracy count · Banks pleads the same day · Owens about a week earlier"),
   show="Then, in the summer of 2026, the case turned. About a week after Owens changed his plea, on July 6, Lumumba pleaded guilty to a single conspiracy count. Banks did the same that afternoon."),
 L("In court, a federal prosecutor read the facts. Fifty thousand dollars in five ten-thousand-dollar checks, from F.B.I. sources posing as developers, received in Fort Lauderdale on April second, twenty twenty-four. The call to change the deadline. The deposit. The withdrawals for personal use. Lumumba told the judge he accepted those facts.",
   doc("pr:lumumba", "U.S. ATTORNEY · S.D. MISS. · NOV 7, 2024", "$50,000 · five $10,000 checks", SRC_WLBT7 + "; " + SRC_PR),
   show="In court, a federal prosecutor read the facts. $50,000 in five $10,000 checks, from FBI sources posing as developers, received in Fort Lauderdale on April 2, 2024. The call to change the deadline. The deposit. The withdrawals for personal use. Lumumba told the judge he accepted those facts."),
 L("The conspiracy count carries up to five years in prison. In exchange for the pleas, the government dropped the other, more serious charges, according to the Mississippi Free Press.",
   doc("n_count1", "NOTICE OF MAXIMUM PENALTIES · COUNT 1", "Conspiracy: not more than 5 years", SRC_N + "; " + SRC_MFP)),
 L("On November fifth, twenty twenty-six, Owens was sentenced first. Forty-one months in prison, and a one hundred thousand dollar fine. Banks got forty-five months and a fifteen thousand dollar fine.",
   dict(type="bars", kicker="SENTENCES · JUDGE DANIEL JORDAN", title="Months in prison", items=[{"label": "Aaron Banks (ex-council president)", "value": 45, "display": "45 mo. · $15K fine"}, {"label": "Jody Owens (ex-district attorney)", "value": 41, "display": "41 mo. · $100K fine"}, {"label": "Chokwe Antar Lumumba (ex-mayor)", "value": 37, "display": "37 mo. · $50K forfeited"}], src=SRC_MT + "; " + SRC_WLBT + "; " + SRC_ST),
   show="On November 5, 2026, Owens was sentenced first. 41 months in prison, and a $100,000 fine. Banks got 45 months and a $15,000 fine."),
 L("At Owens's hearing, Lumumba's lawyers had argued about what exactly the mayor was paid to do. The lead prosecutor, Dave Fulcher, answered: The bribery scheme was not, we need him to move the R.F.Q. The bribery scheme was, we need him involved.",
   dict(type="quote", q="The bribery scheme was not, ‘We need him to move the RFQ.’ The bribery scheme was, ‘We need him involved.’", case="Dave Fulcher, federal prosecutor · Nov 5, 2026", doc="As quoted by Mississippi Today", cite=SRC_MT),
   show="At Owens's hearing, Lumumba's lawyers had argued about what exactly the mayor was paid to do. The lead prosecutor, Dave Fulcher, answered: \"The bribery scheme was not, 'We need him to move the RFQ.' The bribery scheme was, 'We need him involved.'\""),
 L("Then, on November twentieth, it was the mayor's turn. His lawyer, Gerald Evelyn, told the court: He has no prior record or arrest of any kind.",
   dict(type="quote", q="He has no prior record or arrest of any kind.", case="Gerald Evelyn, Lumumba’s attorney · Nov 20, 2026", doc="As quoted by WLBT", cite=SRC_WLBT)),
 L("Lumumba spoke about his family. I have levied an unbearable and unfair burden on my wife, he said, who I have known since I was in kindergarten.",
   dict(type="quote", q="I have levied an unbearable and unfair burden on my wife, who I have known since I was in kindergarten.", case="Chokwe Antar Lumumba · Nov 20, 2026", doc="As quoted by WLBT", cite=SRC_WLBT)),
 L("And: My effort at redemption starts right now.",
   dict(type="quote", q="My effort at redemption starts right now", case="Chokwe Antar Lumumba · Nov 20, 2026", doc="As quoted by WLBT", cite=SRC_WLBT)),
 L("Judge Daniel Jordan said he sensed, at the plea hearing and again that day, a true sense of remorse. But he also said: You were the top elected official in the city of Jackson.",
   dict(type="quote", q="You were the top elected official in the city of Jackson.", case="U.S. District Judge Daniel Jordan · Nov 20, 2026", doc="As quoted by WLBT", cite=SRC_WLBT)),
 L("It is still not enough, the judge said, to outweigh the nature and circumstances of the offense. A sentence below the guideline range, he said, would not be sufficient.",
   dict(type="quote", q="It is still not enough to outweigh the nature and circumstances of the offense.", case="U.S. District Judge Daniel Jordan · Nov 20, 2026", doc="As quoted by WLBT", cite=SRC_WLBT)),
 L("Thirty-seven months in federal prison. Earlier that month, according to Mississippi Today, the judge had signaled a range of thirty-seven to forty-six months. Lumumba also agreed to forfeit fifty thousand dollars, the amount of the checks on the yacht.",
   SENT, show="37 months in federal prison. Earlier that month, according to Mississippi Today, the judge had signaled a range of 37 to 46 months. Lumumba also agreed to forfeit $50,000, the amount of the checks on the yacht."),
 L("He has given up his law license. His lawyer told the court he can never hold elected office again. Lumumba, Owens and Banks are due to report to prison on January fourth.",
   dict(type="big", kicker="PER WLBT, MAGNOLIA TRIBUNE & WAPT", lines=["Disbarred.", "Prison: January 4."], src=SRC_WLBT + "; " + SRC_MAG + "; " + SRC_WAPT),
   show="He has given up his law license. His lawyer told the court he can never hold elected office again. Lumumba, Owens and Banks are due to report to prison on January 4."),
 L("Angelique Lee and Owens's relative, Sherik Marve Smith, who also pleaded guilty, had not been sentenced as of early November, according to Mississippi Today.",
   doc("i_overview", I + "¶ 1", "Five people. One scheme.", SRC_I + "; " + SRC_MT)),
 L("So here is the whole case. Two fake developers. A district attorney who sold access. A council president who asked for fifty grand. And a mayor who made one phone call from a yacht, for five checks.",
   photo("ph_sofa", "INDICTMENT ¶¶ 57–59 · APRIL 2, 2024 · FBI RECORDING", SRC_IPH),
   show="So here is the whole case. Two fake developers. A district attorney who sold access. A council president who asked for fifty grand. And a mayor who made one phone call from a yacht, for five checks."),
 L("Banks, forty-five months. Owens, forty-one. The mayor, thirty-seven. Was the man at the top punished enough? Tell us in the comments.",
   dict(type="end"),
   show="Banks, 45 months. Owens, 41. The mayor, 37. Was the man at the top punished enough? Tell us in the comments."),
]

# ---- independent fact-check fixes (factcheck.md, 16) ----
def F(i, say=None, show=None, **sc):
    if say is not None: lines[i]["say"] = say
    if show is not None: lines[i]["show"] = show
    elif say is not None: lines[i].pop("show", None)
    for k, v in sc.items(): lines[i]["scene"][k] = v
F(10, "In August twenty twenty-three, a local man introduced one of them to the county's top prosecutor. Jody Owens, the district attorney of Hinds County, which includes Jackson.",
  "In August 2023, a local man introduced one of them to the county's top prosecutor. Jody Owens, the district attorney of Hinds County, which includes Jackson.")
F(15, "Remember, the district attorney is the county's chief prosecutor. And, according to the indictment, he had just negotiated his price.",
  lines=["The prosecutor", "named his price."], kicker="PER THE INDICTMENT")
F(17, "December thirteenth, twenty twenty-three. A private jet, paid for by the F.B.I., takes Owens to Fort Lauderdale. That evening, on a yacht, the developers ask how he wants to be paid. Cash, he says. It's easier. He brought a bag.",
  "December 13, 2023. A private jet, paid for by the FBI, takes Owens to Fort Lauderdale. That evening, on a yacht, the developers ask how he wants to be paid. Cash, he says. It's \"easier.\" He brought a bag.")
F(26, "They were. And much of what the mayor said and did with them would end up in a federal indictment.",
  lines=["They worked for the FBI.", "The yacht was recorded."])
F(33, "Back on February twenty-eighth, the question of the mayor had come up. Why do we need him, one developer asked. Because, Owens's relative answered, according to the indictment, he could make things a lot harder.",
  "Back on February 28, the question of the mayor had come up. \"Why do we need [him]?\" one developer asked. Because, Owens's relative answered, according to the indictment, he \"could make things a lot harder.\"")
F(38, "On the evening of March ninth, Owens texted the mayor that he was outside. The next day, according to the indictment, he told the developers he had met the mayor at his house, and that everyone was on one accord. Fifty thousand dollars in Florida. And, he said, the mayor's final number was a hundred thousand.",
  "On the evening of March 9, Owens texted the mayor that he was \"outside.\" The next day, according to the indictment, he told the developers he had met the mayor at his house, and that everyone was \"on one accord.\" $50,000 in Florida. And, he said, the mayor's \"final number\" was $100,000.")
F(39, lines[39]["say"].replace("Then he paid them all back.", "Then he reimbursed his relative and the two associates in full."),
  lines[39]["show"].replace("Then he paid them all back.", "Then he reimbursed his relative and the two associates in full."))
F(42, lines[42]["say"].replace("The F.B.I. records it all.", "The meeting is recorded, on audio and video."),
  lines[42]["show"].replace("The FBI records it all.", "The meeting is recorded, on audio and video."))
F(44, show="Owens: \"So we did five $10,000 checks to make it very simple …\" Lumumba: \"Yeah.\"")
F(48, lines[48]["say"].replace("That was the official act that was for sale.", "In the indictment, that was the official act the money bought."))
F(53, "Fifty thousand dollars in. Fourteen thousand five hundred out, to the mayor himself. And the money had come from the F.B.I.'s own undercover developers.",
  "$50,000 in. $14,500 out, to the mayor himself. And the money had come from the FBI's own undercover developers.")
F(63, q="… going to walk around as if I’m guilty of something I am not.")
F(69, "The conspiracy count carries up to five years in prison. In exchange for the pleas, the government agreed to drop the more substantive charges, according to the Mississippi Free Press.")
F(71, "On November fifth, the day Owens was sentenced, Lumumba's own sentencing hearing began. The judge noted that the ask had been to move the date of the R.F.Q. The lead prosecutor, Dave Fulcher, called that a strawman set up by Lumumba's lawyers. The bribery scheme, he said, was: we need him involved.",
  "On November 5, the day Owens was sentenced, Lumumba's own sentencing hearing began. The judge noted that \"the ask was to move the date of the RFQ.\" The lead prosecutor, Dave Fulcher, called that \"a strawman that has been set up by Lumumba's counsel.\" The bribery scheme, he said, was: \"We need him involved.\"",
  q="That is a strawman that has been set up by Lumumba’s counsel. … The bribery scheme was, ‘We need him involved.’",
  case="Dave Fulcher, federal prosecutor · Nov 5, 2026 · Lumumba presentence hearing")
F(72, "Then, on November twentieth, the mayor's hearing resumed. His lawyer, Gerald Evelyn, told the court: He has no prior record or arrest of any kind.",
  "Then, on November 20, the mayor's hearing resumed. His lawyer, Gerald Evelyn, told the court: \"He has no prior record or arrest of any kind.\"")

json.dump({"label": "SWORN · CASE 021", "lines": lines}, open(os.path.join(HERE, "episode.json"), "w"), indent=1, ensure_ascii=False)
print(len(lines), "lines,", sum(len(l["say"].split()) for l in lines), "words")
