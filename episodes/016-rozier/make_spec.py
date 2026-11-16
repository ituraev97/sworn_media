import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
def hl(name, i=0):
    a, b = HL[name][i]
    return [0.0, a, 1.0, round(b - a, 4)]
CASE = "UNITED STATES v. ROZIER"
SRC_PR = "U.S. Attorney's Office, E.D.N.Y., press release (Oct 23, 2025)"
SRC_I = "Indictment, U.S. v. Earnest et al., E.D.N.Y. 25-cr-323, ECF 17 (Oct 16, 2025)"
SRC_S = "Superseding Indictment, E.D.N.Y. 25-cr-323, ECF 101 (May 28, 2026)"
SRC_G144 = "Gov't opposition to Rozier's motion to dismiss, ECF 144 (Aug 26, 2026)"
SRC_G166 = "Gov't letter opposing severance, ECF 166 (Nov 3, 2026)"
SRC_D169 = "Rozier's omnibus motion in limine, ECF 169 (Nov 12, 2026)"
SRC_MD = "Docket, U.S. v. Rozier, M.D. Fla. 6:25-mj-02183, filed as ECF 26 (Oct 27, 2025)"
SRC_ESPN = "ESPN, David Purdum (Nov 13, 2026)"
SRC_CBS = "CBS News / AP (Apr 28, 2026)"
SRC_COV = "Covers (May 28, 2026)"
SRC_COVM = "Covers (Jan 22, 2026)"
PHOTO = "PHOTO: KEITH ALLISON · CC BY-SA 2.0 · WIKIMEDIA COMMONS · 2017"
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
def doc(img, kicker, title, src, i=0, pan=None):
    return dict(type="doc", img=f"img/{img}.jpg", pan=pan or [0.0, 0.1], hl=hl(img, i), kicker=kicker, title=title, src=src)
def photo(caption):
    return dict(type="photo", img="img/rozier_face.jpg", caption=caption, src=PHOTO, fit="contain")
IND = "THE INDICTMENT · OCT 2025 · "
SUP = "SUPERSEDING INDICTMENT · MAY 2026 · "
G144 = "GOVERNMENT FILING · AUG 26, 2026"
lines = [
 # COLD OPEN
 L("March twenty-third, twenty twenty-three. New Orleans. Terry Rozier, the Hornets' starting guard, walks off the court in the first quarter, and does not come back. He played nine minutes and thirty-four seconds.",
   photo("TERRY ROZIER · 2017"),
   show="March 23, 2023. New Orleans. Terry Rozier, the Hornets' starting guard, walks off the court in the first quarter, and does not come back. He played 9 minutes and 34 seconds."),
 L("Federal prosecutors say those nine minutes were sold in advance. They allege he agreed to an approximately one hundred thousand dollar bribe to leave that game early, so that people around him could bet against his numbers.",
   doc("sup_9", SUP + "PARAGRAPH 37", "“an approximately $100,000 bribe”", SRC_S, 1),
   show="Federal prosecutors say those nine minutes were sold in advance. They allege he agreed to an approximately $100,000 bribe to leave that game early, so that people around him could bet against his numbers."),
 L("Rozier says he was hurt, and that he is innocent. His lawyers wrote it in a court filing on November twelfth: Terry Rozier is innocent. The objective evidence proves it.",
   dict(type="quote", q="Terry Rozier is innocent. The objective evidence proves it.", case=CASE, doc="DEFENSE FILING · NOV 12, 2026", cite=SRC_D169),
   show="Rozier says he was hurt, and that he is innocent. His lawyers wrote it in a court filing on November 12: \"Terry Rozier is innocent. The objective evidence proves it.\""),
 L("One day later, according to ESPN, prosecutors filed new papers, describing a text about another plan, involving a Hornets teammate.",
   dict(type="big", kicker="NOVEMBER 13, 2026", lines=["A new filing.", "Another|teammate?"], src=SRC_ESPN),
   show="One day later, according to ESPN, prosecutors filed new papers, describing a text about another plan, involving a Hornets teammate."),
 L("Rozier has pleaded not guilty. Every charge in this story is an allegation, and he is presumed innocent unless and until proven guilty. His trial is set for February eighth, twenty twenty-seven, in Brooklyn.",
   dict(type="verdict", kicker="BROOKLYN · TRIAL SET FOR FEB 8, 2027", stamp="CHARGED", big="Not guilty plea", sub="Terry Rozier · presumed innocent", neutral=True),
   show="Rozier has pleaded not guilty. Every charge in this story is an allegation, and he is presumed innocent unless and until proven guilty. His trial is set for February 8, 2027, in Brooklyn."),
 L("This is what the government says happened, what Rozier says happened, and what the documents show so far.",
   dict(type="title", kicker="SWORN · CASE 016 · BREAKING", title="Nine Minutes|in New Orleans", sub="United States v. Terry Rozier · E.D.N.Y. · 25-cr-323"),),
 # I
 L("Chapter one. Nine minutes.", dict(type="chapter", n="I", title="Nine Minutes")),
 L("Start with the game. The Hornets were on the road, in New Orleans, against the Pelicans. According to the indictment, Rozier was not on the team's injury report, and Hornets officials did not know he planned to leave early.",
   doc("ind_9", IND + "PARAGRAPH 36", "Not on the injury report", SRC_I, 0)),
 L("But the grand jury alleges one person did know. Before the game, Rozier told his longtime friend, Deniro Laster, that he would remove himself in the first quarter, due to a supposed injury, and not return.",
   doc("ind_8", IND + "PARAGRAPH 36", "“a supposed injury”", SRC_I, 0)),
 L("Prosecutors say Laster then sold that information. Two of the buyers, Marves Fairley and an unnamed co-conspirator, agreed to pay him about one hundred thousand dollars out of their expected winnings. In this first indictment, that money is a payment to Laster for the tip. The word bribe comes later.",
   doc("ind_9", IND + "PARAGRAPH 37", "Approximately $100,000", SRC_I, 1),
   show="Prosecutors say Laster then sold that information. Two of the buyers, Marves Fairley and an unnamed co-conspirator, agreed to pay him about $100,000 out of their expected winnings. In this first indictment, that money is a payment to Laster for the tip. The word bribe comes later."),
 L("Then the money moved. According to the indictment, a bettor named Shane Hennen put about sixty-one thousand two hundred dollars on Rozier's unders at one retail sportsbook. One associate alone placed about one hundred seven thousand.",
   doc("ind_10", IND + "PARAGRAPH 39", "$61,200 on the unders", SRC_I, 0),
   show="Then the money moved. According to the indictment, a bettor named Shane Hennen put about $61,200 on Rozier's unders at one retail sportsbook. One associate alone placed about $107,000."),
 L("An under bet is simple. You win if the player does less than the sportsbook expects. Fewer points. Fewer assists. Fewer minutes.",
   dict(type="big", kicker="THE BET", lines=["The under.", "You win|when he fails."], src=SRC_I)),
 L("In all, the Justice Department says, the group placed and directed more than two hundred thousand dollars in wagers on Rozier's unders.",
   dict(type="stat", kicker="MARCH 23, 2023 · ROZIER'S UNDERS", value="$200K+", label="in wagers placed and directed, prosecutors say", src=SRC_PR),
   show="In all, the Justice Department says, the group placed and directed more than $200,000 in wagers on Rozier's unders."),
 L("And on the court, it played out the way the bettors needed. Rozier scored five points, with two assists and one three-pointer. His season averages were twenty-one point one points, five point one assists and two point six threes.",
   doc("ind_12", IND + "PARAGRAPH 41", "5 points. 2 assists. 1 three.", SRC_I, 1),
   show="And on the court, it played out the way the bettors needed. Rozier scored 5 points, with 2 assists and 1 three-pointer. His season averages were 21.1 points, 5.1 assists and 2.6 threes."),
 L("Nine minutes and thirty-four seconds, against a season average of about thirty-five point three minutes a game.",
   dict(type="bars", kicker="MINUTES PLAYED", title="March 23 vs. his season average", items=[{"label": "SEASON AVERAGE", "value": 35.3, "display": "35.3"}, {"label": "MARCH 23, 2023", "value": 9.57, "display": "9:34"}], src=SRC_I),
   show="9 minutes and 34 seconds, against a season average of about 35.3 minutes a game."),
 L("The Hornets lost the game. And the government says many of the bets paid off.",
   doc("g144_7", G144, "“His team, the Hornets, lost the game.”", SRC_G144, 1)),
 L("But one number did not cooperate. Four rebounds. Hold on to that number. Both sides now use it to make their case.",
   dict(type="big", kicker="THE ONE STAT THAT DIDN'T FIT", lines=["4 rebounds.", "Both sides|cite it."], src=SRC_I + " · " + SRC_D169)),
 # II
 L("Chapter two. The cash.", dict(type="chapter", n="II", title="The Cash")),
 L("Five days after the game, according to the indictment, Laster traveled to Philadelphia. The grand jury alleges Rozier arranged and paid for that trip.",
   doc("ind_12", IND + "PARAGRAPH 42", "“arranged and paid for”", SRC_I, 3)),
 L("In Philadelphia, between the late night of March twenty-eighth and the early morning of the twenty-ninth, Fairley allegedly handed Laster tens of thousands of dollars in cash, as payment for the information about Rozier's exit.",
   show="In Philadelphia, between the late night of March 28 and the early morning of the 29th, Fairley allegedly handed Laster tens of thousands of dollars in cash, as payment for the information about Rozier's exit."),
 L("Then, the government says, Laster drove hundreds of miles through the night to Rozier's house in Charlotte.",
   doc("g144_8", G144, "“through the night”", SRC_G144, 0)),
 L("And in the early morning hours of April first, twenty twenty-three, according to the superseding indictment, Laster and Rozier counted the money together.",
   doc("sup_14", SUP + "PARAGRAPH 46", "Counting the money", SRC_S, 0),
   show="And in the early morning hours of April 1, 2023, according to the superseding indictment, Laster and Rozier counted the money together."),
 L("Prosecutors go further. In an August filing, they wrote that Laster and Rozier photographed themselves counting the cash.",
   doc("g144_8", G144, "“photographed themselves counting the cash”", SRC_G144, 0)),
 L("Remember: Rozier denies knowing about any bets. A photo of money does not tell a jury where the money came from. That question is what the trial is for.",
   dict(type="big", kicker="HIS ANSWER", lines=["Cash is not", "a confession."], src=SRC_G166 + " · " + SRC_D169)),
 # III
 L("Chapter three. The arrest.", dict(type="chapter", n="III", title="The Arrest")),
 L("For two and a half years, Rozier was not charged. A defense filing says the NBA looked into the game, and in January twenty twenty-five said it had found no rule violation, and was cooperating with a federal investigation. Then, on October twenty-third, twenty twenty-five, the FBI made arrests across the country.",
   dict(type="timeline", kicker="FROM THE GAME TO THE ARREST", at=3, events=[{"date": "MAR 23, 2023", "text": "the game"}, {"date": "APR 1, 2023", "text": "the count"}, {"date": "OCT 16, 2025", "text": "grand jury indictment"}, {"date": "OCT 23, 2025", "text": "arrests"}], src=SRC_I + " · " + SRC_PR + " · " + SRC_D169),
   show="For two and a half years, Rozier was not charged. A defense filing says the NBA looked into the game, and in January 2025 said it had found no rule violation, and was cooperating with a federal investigation. Then, on October 23, 2025, the FBI made arrests across the country."),
 L("Rozier was arrested in Orlando, Florida. A federal court docket there lists the case as United States versus Rozier.",
   dict(type="big", kicker="ORLANDO · OCTOBER 23, 2025", lines=["USA v.", "Rozier."], src=SRC_MD)),
 L("In Brooklyn, the indictment was unsealed. Six defendants, charged with wire fraud conspiracy and money laundering conspiracy. Rozier's listed nicknames: Scary Terry, and Chum.",
   doc("ind_1", IND + "UNSEALED OCT 23, 2025", "Six defendants", SRC_I, 0),
   show="In Brooklyn, the indictment was unsealed. Six defendants, charged with wire fraud conspiracy and money laundering conspiracy. Rozier's listed nicknames: \"Scary Terry,\" and \"Chum.\""),
 L("Remember that second nickname. It comes back.",
   dict(type="big", lines=["\"Chum.\"", "Remember it."], src=SRC_PR)),
 L("The U.S. Attorney, Joseph Nocella, said: As alleged, the defendants turned professional basketball into a criminal betting operation.",
   dict(type="quote", q="As alleged, the defendants turned professional basketball into a criminal betting operation …", case="E.D.N.Y. · OCTOBER 23, 2025", doc="U.S. ATTORNEY JOSEPH NOCELLA JR.", cite=SRC_PR)),
 L("The New York police commissioner, Jessica Tisch, went further: Rigging a professional basketball game for personal profit is as immoral as it is illegal.",
   dict(type="quote", q="Rigging a professional basketball game for personal profit is as immoral as it is illegal.", case="E.D.N.Y. · OCTOBER 23, 2025", doc="NYPD COMMISSIONER JESSICA TISCH", cite=SRC_PR)),
 L("The same indictment named a former NBA player and coach, Damon Jones, and described tips about other games: a Trail Blazers game, a Magic game, and Lakers games. It also described games involving Jontay Porter, the former Raptors player, who had already pleaded guilty.",
   dict(type="list", kicker="THE SAME INDICTMENT · OCT 2025", items=[["MAR 23, 2023", "Hornets — Rozier's early exit (alleged)"], ["MAR 24, 2023", "Trail Blazers — lineup tip (alleged)"], ["APR 6, 2023", "Magic — lineup tip (alleged)"], ["2023–2024", "Lakers — medical tips (alleged)"], ["2024", "Raptors — Jontay Porter (pleaded guilty)"]], src=SRC_PR)),
 L("Rozier pleaded not guilty. The judge is LaShann DeArcy Hall, in the Eastern District of New York.",
   dict(type="big", kicker="E.D.N.Y. · JUDGE LASHANN DEARCY HALL", lines=["His plea:", "not guilty."], src="Minute entry, arraignment, ECF 69 (Dec 8, 2025)")),
 # IV
 L("Chapter four. The bribe.", dict(type="chapter", n="IV", title="The Bribe")),
 L("In May twenty twenty-six, the case got heavier. A grand jury returned a superseding indictment, with two new counts against Rozier: bribery in sporting contests, and honest services wire fraud conspiracy.",
   doc("sup_8", SUP + "PARAGRAPH 35", "Honest services", SRC_S, 0),
   show="In May 2026, the case got heavier. A grand jury returned a superseding indictment, with two new counts against Rozier: bribery in sporting contests, and honest services wire fraud conspiracy."),
 L("Honest services means this. Prosecutors allege he schemed to deprive the Hornets and the NBA of his honest and faithful services, through a bribe.",
   doc("sup_8", SUP + "PARAGRAPH 35", "“honest and faithful services”", SRC_S, 0)),
 L("The new version tells a different story about the injury. It says Rozier really had a lower leg injury near the end of that season. He kept playing on it. But, it alleges, he planned to use that injury as the reason to leave a game early.",
   doc("sup_9", SUP + "PARAGRAPH 37", "“a lower leg injury”", SRC_S, 0)),
 L("In exchange for an approximately one hundred thousand dollar bribe, the grand jury says, Rozier agreed to withdraw early from a game still to be chosen, and to give Laster a portion.",
   doc("sup_9", SUP + "PARAGRAPH 37", "“an approximately $100,000 bribe”", SRC_S, 1),
   show="In exchange for an approximately $100,000 bribe, the grand jury says, Rozier agreed to withdraw early from a game still to be chosen, and to give Laster a portion."),
 L("And while the game was being chosen, Laster allegedly kept the buyers updated, using encrypted apps.",
   doc("sup_9", SUP + "PARAGRAPH 37", "Encrypted applications", SRC_S, 2)),
 L("Now, the four rebounds. Of the four stats the indictment lists, rebounds were the only one where he went over his betting line. According to the superseding indictment, because of those four rebounds, not all of the bets won. So after the game, they negotiated the bribe down to about seventy thousand dollars.",
   doc("sup_13", SUP + "PARAGRAPH 44", "Down to approximately $70,000", SRC_S, 0),
   show="Now, the four rebounds. Of the four stats the indictment lists, rebounds were the only one where he went over his betting line. According to the superseding indictment, because of those four rebounds, not all of the bets won. So after the game, they negotiated the bribe down to about $70,000."),
 L("One hundred thousand promised. Seventy thousand, the government says, delivered. A thirty thousand dollar discount, for four rebounds.",
   dict(type="bars", kicker="THE ALLEGED BRIBE", title="Before and after the four rebounds", items=[{"label": "AGREED (ALLEGED)", "value": 100, "display": "$100K"}, {"label": "AFTER THE GAME (ALLEGED)", "value": 70, "display": "$70K"}], src=SRC_S),
   show="$100,000 promised. $70,000, the government says, delivered. A $30,000 discount, for four rebounds."),
 L("In its August filing, the government put it in one sentence. For taking a bribe in exchange for removing himself early from a professional basketball game so that others could bet on, and profit from, his underperformance, Rozier is charged with four distinct but related crimes.",
   doc("g144_6", G144, "Four counts", SRC_G144, 0)),
 # V
 L("Chapter five. The others.", dict(type="chapter", n="V", title="The Others")),
 L("While Rozier fights the charges, people around this case have been pleading guilty.",
   dict(type="big", lines=["He fights.", "Others|plead."], src=SRC_CBS + " · " + SRC_COV)),
 L("In January twenty twenty-six, a bettor named Timothy McCormack was sentenced to two years in prison by Judge DeArcy Hall. The indictment says he and another man bet about forty-one thousand dollars on Rozier's unders that night.",
   dict(type="stat", kicker="JANUARY 2026 · FIRST SENTENCE", value="2 years", label="Timothy McCormack, a bettor in the related schemes", src=SRC_COVM + " · " + SRC_I),
   show="In January 2026, a bettor named Timothy McCormack was sentenced to two years in prison by Judge DeArcy Hall. The indictment says he and another man bet about $41,000 on Rozier's unders that night."),
 L("In April, Damon Jones pleaded guilty to two counts of wire fraud conspiracy, covering this case and a separate rigged-poker case. According to AP, he acknowledged using insider information from relationships he made as a player. His sentencing is set for January sixth.",
   dict(type="verdict", kicker="BROOKLYN · APRIL 28, 2026", stamp="GUILTY PLEA", big="Damon Jones", sub="two counts of wire fraud conspiracy · sentencing Jan 6, 2027"),
   show="In April, Damon Jones pleaded guilty to two counts of wire fraud conspiracy, covering this case and a separate rigged-poker case. According to AP, he acknowledged using insider information from relationships he made as a player. His sentencing is set for January 6."),
 L("Then, on May twenty-eighth, Marves Fairley, one of the alleged buyers of Rozier's information, pleaded guilty to seven felony counts across two cases. In court he said: I agreed to pay a player to change their game performance.",
   dict(type="quote", q="I agreed to pay a player to change their game performance", case="BROOKLYN · MAY 28, 2026", doc="MARVES FAIRLEY, AT HIS PLEA", cite="As quoted by " + SRC_COV),
   show="Then, on May 28, Marves Fairley, one of the alleged buyers of Rozier's information, pleaded guilty to seven felony counts across two cases. In court he said: \"I agreed to pay a player to change their game performance.\""),
 L("He did not say the name. A prosecutor did. According to Covers, a lawyer for the U.S. Attorney's Office told the court the player Fairley referenced was Rozier. Rozier's attorney disputed that his client was paid to alter his play.",
   dict(type="big", kicker="MAY 28, 2026 · IN COURT", lines=["A prosecutor:", "the player|was Rozier."], src="As reported by " + SRC_COV)),
 L("Fairley's own sentencing is expected in February. Under his plea, he faces up to twenty years on six of the counts, and he agreed to a six hundred seventy-six thousand seven hundred dollar penalty, according to Covers.",
   dict(type="stat", kicker="FAIRLEY'S PLEA", value="$676,700", label="agreed penalty · up to 20 years on 6 counts", src=SRC_COV),
   show="Fairley's own sentencing is expected in February. Under his plea, he faces up to 20 years on six of the counts, and he agreed to a $676,700 penalty, according to Covers."),
 L("So some of the people accused of buying the information, or betting on it, have pleaded guilty. Rozier has not. He says he never knew about any bets.",
   dict(type="big", lines=["Some plead guilty.", "He pleads|not guilty."], src=SRC_COV + " · " + SRC_D169)),
 # VI
 L("Chapter six. His side.", dict(type="chapter", n="VI", title="His Side")),
 L("Rozier's defense, as the government itself summarizes it, is simple. He did not know about any bets. He left the game because he was hurt.",
   doc("g166_2", "GOVERNMENT LETTER · NOV 3, 2026", "“He did not know about any bets.”", SRC_G166, 0)),
 L("His lawyers say the objective evidence backs him. Unlike every other individual charged in this sweeping conspiracy, they wrote, he never placed a bet on an NBA game or player prop, and he had no knowledge that anyone else was betting on his performance.",
   dict(type="quote", q="he never placed a bet on an NBA game or player prop, and he had no knowledge that anyone else was betting on his performance.", case=CASE, doc="DEFENSE FILING · NOV 12, 2026", cite=SRC_D169)),
 L("They point to three things. Medical evidence that he was genuinely injured. The rebounds: he beat that line, the opposite of what the bettors wanted. And one text message.",
   dict(type="list", kicker="THE DEFENSE'S THREE POINTS", items=[["1", "medical evidence of a genuine injury"], ["2", "he exceeded his rebounding prop"], ["3", "the \"don't tell chum\" text"]], src=SRC_D169)),
 L("Remember the nickname. Chum. While in Philadelphia, Laster texted a third person: Dont tell Chum bout the bet.",
   doc("g144_8", G144 + " · FOOTNOTE 2", "“Dont [sic] tell Chum bout the bet.”", SRC_G144, 1),
   show="Remember the nickname. \"Chum.\" While in Philadelphia, Laster texted a third person: \"Dont tell Chum bout the bet.\""),
 L("The defense says that text guts the case. Why hide a bet from the man who supposedly sold it?",
   dict(type="big", kicker="THE DEFENSE", lines=["Why hide the bet", "from Chum?"], src=SRC_D169)),
 L("The government says its investigation developed evidence from multiple sources that this text chain does not relate to sports gambling. According to the defense, prosecutors now say it was about table games at a casino.",
   doc("g144_8", G144 + " · FOOTNOTE 2", "“does not relate to sports gambling”", SRC_G144, 1)),
 L("A jury may decide which reading is right. If the text is admitted at all.",
   dict(type="big", lines=["Casino talk", "or a cover-up?"], src=SRC_G144 + " · " + SRC_D169)),
 L("Rozier and Laster also asked to be tried separately. The government opposed it, calling Rozier's defense, in effect, an argument that no crime occurred, and asked to keep the joint trial, about three weeks long, starting February eighth, twenty twenty-seven.",
   doc("g166_1", "GOVERNMENT LETTER · NOV 3, 2026", "Joint trial on February 8, 2027", SRC_G166, 1),
   show="Rozier and Laster also asked to be tried separately. The government opposed it, calling Rozier's defense, in effect, an argument that no crime occurred, and asked to keep the joint trial, about three weeks long, starting February 8, 2027."),
 # VII
 L("Chapter seven. The new filing.", dict(type="chapter", n="VII", title="The New Filing")),
 L("Which brings us to last week. On November thirteenth, ESPN reported on a new government filing, asking the judge to admit more evidence at trial.",
   dict(type="big", kicker="ESPN · NOVEMBER 13, 2026", lines=["New evidence,", "prosecutors say."], src=SRC_ESPN),
   show="Which brings us to last week. On November 13, ESPN reported on a new government filing, asking the judge to admit more evidence at trial."),
 L("The headline claim: in April twenty twenty-three, about two weeks after the Pelicans game, Laster allegedly texted Fairley that he and Rozier were setting up another under bet, this one involving one of Rozier's then-teammates.",
   dict(type="big", kicker="APRIL 2023 · ALLEGED · AS DESCRIBED BY ESPN", lines=["Another under bet?", "A teammate,|prosecutors say."], src=SRC_ESPN),
   show="The headline claim: in April 2023, about two weeks after the Pelicans game, Laster allegedly texted Fairley that he and Rozier were setting up another under bet, this one involving one of Rozier's then-teammates."),
 L("Be careful with this one. ESPN reports it is unclear whether Rozier knew about that text, whether the teammate knew of any plan, or whether any bet was ever placed. The government has not charged Laster or Rozier over it.",
   dict(type="list", kicker="WHAT IS NOT KNOWN", items=[["?", "whether Rozier knew of the text"], ["?", "whether the teammate knew of any plan"], ["?", "whether any bet was placed"], ["0", "charges against Laster or Rozier over it"]], src=SRC_ESPN)),
 L("The filing also accuses Rozier of lying to the NBA during its investigation, and of not turning over all of his phones. And it asks the judge to let the jury hear that Rozier is paying the legal fees of Laster and Laster's siblings.",
   dict(type="list", kicker="THE GOVERNMENT'S NEW CLAIMS · NOV 2026", items=[["1", "lied to the NBA's investigators (alleged)"], ["2", "did not turn over all his phones (alleged)"], ["3", "pays legal fees for Laster and his siblings (alleged)"], ["4", "told people March 23 would be his last game of the season (alleged)"]], src=SRC_ESPN)),
 L("His lawyer, David Markus, told ESPN they deny the new allegations in the strongest possible way.",
   dict(type="big", kicker="DAVID MARKUS · ROZIER'S LAWYER", lines=["\"In the strongest", "possible way.\""], src=SRC_ESPN)),
 L("And the NBA? A league spokesperson said the league understands no player other than Rozier is alleged to have engaged in misconduct in this scheme. We continue to cooperate with the government's investigation.",
   dict(type="quote", q="We continue to cooperate with the government's investigation.", case="NBA SPOKESPERSON", doc="TO ESPN · NOV 2026", cite=SRC_ESPN)),
 # CLOSE
 L("So here is where it stands. Rozier faces four counts, including conspiracy to launder money. The original charges each carried a maximum of twenty years. He says he was injured, and never knew about a single bet.",
   dict(type="list", kicker="THE CHARGES AGAINST ROZIER", items=[["1", "wire fraud conspiracy"], ["2", "money laundering conspiracy"], ["3", "bribery in sporting contests"], ["4", "honest services wire fraud conspiracy"]], src=SRC_G144 + " · " + SRC_PR)),
 L("The government says the nine minutes were planned, the information was sold, and the cash was counted at his house.",
   dict(type="big", kicker="THE GOVERNMENT'S CASE · ALLEGED", lines=["Planned. Sold.", "Counted."], src=SRC_S + " · " + SRC_G144)),
 L("In February, a Brooklyn jury will be asked one question. Was Terry Rozier hurt, or was he paid?",
   dict(type="big", kicker="FEBRUARY 8, 2027 · BROOKLYN", lines=["Hurt", "or paid?"], src=SRC_G166)),
 L("Until then, he is presumed innocent. What do you think the four rebounds prove? Tell us in the comments. This is SWORN.",
   dict(type="end", cta="WHAT DO THE FOUR REBOUNDS PROVE?")),
]
from panfix import fix
fix(lines, "long")
spec = {"label": "SWORN · CASE 016", "lines": lines}
if __name__ == "__main__":
    json.dump(spec, open(os.path.join(HERE, "episode.json"), "w"), indent=1, ensure_ascii=False)
    print(len(lines), "lines,", sum(len(l["say"].split()) for l in lines), "words")
