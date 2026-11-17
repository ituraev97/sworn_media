import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
def hl(name, i=0):
    a, b = HL[name][i]
    return [0.0, a, 1.0, round(b - a, 4)]
CASE = "UNITED STATES v. BELFORT"
SRC_MTC = "U.S. motion to compel, U.S. v. Belfort, D. Nev. 3:18-ms-00001 / E.D.N.Y. 18-cv-3016, ECF 1 (Mar 29, 2018)"
SRC_GIL = "Declaration of William Gilsen, D. Nev. 3:18-cv-00139, ECF 4-1 (Mar 31, 2018)"
SRC_LAS = "Declaration of AUSA Peter A. Laserna, E.D.N.Y. 18-mc-1033, ECF 1-1 (Mar 27, 2018)"
SRC_L9 = "U.S. Attorney's Office E.D.N.Y., letter, 18-cv-3016, ECF 9 (May 23, 2018)"
SRC_L16 = "U.S. Attorney's Office E.D.N.Y., letter, 18-cv-3016, ECF 16 (Oct 15, 2021)"
SRC_L12 = "U.S. Attorney's Office E.D.N.Y., letter, 18-mc-1033, ECF 12 (Apr 8, 2022)"
SRC_CALD = "U.S. Department of Justice, remarks of AAG Leslie R. Caldwell (Jul 20, 2016)"
SRC_AP13 = "Associated Press, Tom Hays (Nov 11, 2013)"
SRC_BBG13 = "Bloomberg (Nov 7, 2013)"
SRC_BBG18 = "Bloomberg, via Fortune and BNN Bloomberg (May 16, 2018)"
SRC_CNBC = "CNBC (Mar 7, 2018)"
SRC_TMZ = "TMZ (Jul 13, 2026)"
SRC_CNW = "Celebrity Net Worth (Jul 14, 2026) — estimate"
SRC_LAW = "18 U.S.C. § 3613(b)"
SRC_TONE = "Startup Fortune / Analytics Insight (Nov 17, 2026), citing TechCrunch"
PHOTO = "PHOTO: TAI LOPEZ · CC BY 3.0 · WIKIMEDIA COMMONS · 2017"
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
def doc(img, kicker, title, src, i=0, pan=None):
    return dict(type="doc", img=f"img/{img}.jpg", pan=pan or [0.0, 0.1], hl=hl(img, i), kicker=kicker, title=title, src=src)
def photo(caption):
    return dict(type="photo", img="img/belfort_face.jpg", caption=caption, src=PHOTO, fit="contain")
MTC = "U.S. MOTION TO COMPEL · MARCH 2018"
GIL = "FORENSIC ACCOUNTANT'S DECLARATION · MARCH 2018"
lines = [
 # COLD OPEN
 L("One hundred ten million, three hundred sixty-two thousand, nine hundred ninety-three dollars and eighty-seven cents. That is what a federal judge ordered Jordan Belfort, the real Wolf of Wall Street, to pay back to his victims in two thousand three.",
   photo("JORDAN BELFORT · 2017"),
   show="$110,362,993.87. That is what a federal judge ordered Jordan Belfort, the real Wolf of Wall Street, to pay back to his victims in 2003."),
 L("Here is that number, in a Justice Department filing.",
   doc("mtc_2", MTC, "Restitution: $110,362,993.87", SRC_MTC, 0)),
 L("By twenty eighteen, prosecutors said, he had paid about twelve point eight million dollars, most of it from property he gave up at his sentencing. They said he still owed about ninety-seven million.",
   dict(type="bars", kicker="PROSECUTORS' FIGURES · MAY 2018", title="Ordered vs. paid", items=[{"label": "ORDERED (2003)", "value": 110.4, "display": "$110.4M"}, {"label": "PAID BY 2018", "value": 12.8, "display": "$12.8M"}], src=SRC_BBG18),
   show="By 2018, prosecutors said, he had paid about $12.8 million, most of it from property he gave up at his sentencing. They said he still owed about $97 million."),
 L("And then, this year, came this statement, given to TMZ. Today, I can finally say that I completed my court-ordered restitution.",
   dict(type="quote", q="Today, I can finally say that I completed my court-ordered restitution.", case="JORDAN BELFORT", doc="STATEMENT TO TMZ · JULY 2026", cite=SRC_TMZ),
   show="And then, this year, came this statement, given to TMZ: \"Today, I can finally say that I completed my court-ordered restitution.\""),
 L("TMZ reported, citing sources, that his obligation to keep paying expired on April twenty-eighth, twenty twenty-six. And on Monday, November sixteenth, according to tech press reports, he launched a new company: an A.I. that makes sales calls, trained on his sales methods.",
   dict(type="big", kicker="APRIL 28, 2026 → NOVEMBER 16, 2026", lines=["The clock ran out.", "Then an|A.I. sales voice."], src=SRC_TMZ + " · " + SRC_TONE),
   show="TMZ reported, citing sources, that his obligation to keep paying expired on April 28, 2026. And on Monday, November 16, according to tech press reports, he launched a new company: an AI that makes sales calls, trained on his sales methods."),
 L("So where did the hundred and ten million go? This is the paper trail, from the government's own filings.",
   dict(type="title", kicker="SWORN · CASE 017 · THE PAPER TRAIL", title="The $110 Million|Paper Trail", sub="United States v. Jordan Ross Belfort · E.D.N.Y. · CR-98-0859"),
   show="So where did the $110 million go? This is the paper trail, from the government's own filings."),
 # I
 L("Chapter one. The order.", dict(type="chapter", n="I", title="The Order")),
 L("Start with the crime. Belfort ran Stratton Oakmont, a penny-stock brokerage on Long Island. According to the Associated Press, it started with a few desks and phones in a former auto shop.",
   dict(type="big", kicker="STRATTON OAKMONT · LONG ISLAND", lines=["A few desks.", "A former|auto shop."], src=SRC_AP13)),
 L("The method, as the A.P. described it: high-pressure sales of penny stocks at inflated prices. Once the prices were pumped up, Belfort and others sold their own shares.",
   dict(type="list", kicker="THE PUMP AND DUMP", items=[["1", "brokers push cheap stocks by phone"], ["2", "buying drives the price up"], ["3", "insiders sell their own shares"], ["4", "the customers are left holding them"]], src=SRC_AP13)),
 L("Bloomberg reported that at its peak, the firm employed more than a thousand brokers. The FBI arrested Belfort in nineteen ninety-eight.",
   dict(type="stat", kicker="STRATTON OAKMONT AT ITS PEAK", value="1,000+", label="brokers, Bloomberg reported", src=SRC_BBG13)),
 L("He pleaded guilty in nineteen ninety-nine, and agreed to testify as a government witness against other defendants.",
   dict(type="timeline", kicker="THE CRIMINAL CASE", events=[{"date": "1998", "text": "Arrested by the FBI"}, {"date": "1999", "text": "Pleads guilty, agrees to cooperate"}, {"date": "JULY 18, 2003", "text": "Sentenced"}], at=1, src=SRC_BBG13 + " · " + SRC_AP13 + " · " + SRC_MTC)),
 L("On July eighteenth, two thousand three, he was sentenced. The Justice Department lists the convictions: conspiracy to commit securities fraud, conspiracy to commit money laundering, securities fraud, and false statements.",
   doc("mtc_2", MTC, "Sentenced July 18, 2003", SRC_MTC, 0),
   show="On July 18, 2003, he was sentenced. The Justice Department lists the convictions: conspiracy to commit securities fraud, conspiracy to commit money laundering, securities fraud, and false statements."),
 L("He served twenty-two months in prison, Bloomberg reported. The restitution was the part meant to last. One thousand five hundred thirteen investors, who, according to Bloomberg, lost more than two hundred million dollars.",
   dict(type="stat", kicker="THE VICTIMS", value="1,513", label="investors · more than $200 million lost, per Bloomberg", src=SRC_BBG18),
   show="He served 22 months in prison, Bloomberg reported. The restitution was the part meant to last. 1,513 investors, who, according to Bloomberg, lost more than $200 million."),
 L("And the plan for paying them back was simple. After his release, he was ordered to pay fifty percent of his gross income to his victims.",
   dict(type="big", kicker="THE PAYBACK PLAN", lines=["50% of everything", "he earns."], src=SRC_BBG18 + " · " + SRC_AP13)),
 L("Remember that number. Fifty percent. Because the next twenty years are a fight over what it covered, and for how long.",
   dict(type="big", kicker="HOLD ON TO THIS", lines=["50 percent.", "Of what?|For how long?"], src=SRC_AP13)),
 # II
 L("Chapter two. The book and the movie.", dict(type="chapter", n="II", title="The Book and the Movie")),
 L("Belfort wrote a memoir. According to Bloomberg, government lawyers learned of the book deal in April two thousand seven, and filed restraining orders against the publisher, Bantam Books, and against Warner Brothers and the production company Appian Way.",
   dict(type="list", kicker="RESTRAINED BY THE GOVERNMENT · 2007", items=[["1", "Bantam Books (the memoir)"], ["2", "Warner Bros."], ["3", "Appian Way"]], src=SRC_BBG18),
   show="Belfort wrote a memoir. According to Bloomberg, government lawyers learned of the book deal in April 2007, and filed restraining orders against the publisher, Bantam Books, and against Warner Brothers and the production company Appian Way."),
 L("He agreed to pay half of his movie earnings to the United States. And the money that came in? According to court papers cited by the A.P., book sales produced about seven hundred thousand dollars in payments from two thousand seven to two thousand nine.",
   dict(type="stat", kicker="PAID FROM BOOK SALES · 2007–2009", value="$700K", label="about, per court papers cited by the AP", src=SRC_AP13),
   show="He agreed to pay half of his movie earnings to the United States. And the money that came in? According to court papers cited by the AP, book sales produced about $700,000 in payments from 2007 to 2009."),
 L("In twenty ten, prosecutors later said, he paid nothing.",
   dict(type="stat", kicker="PAID IN 2010", value="$0", label="according to prosecutors", src=SRC_BBG18)),
 L("Twenty ten was also the year his probation ended. And Belfort's lawyers argued that the fifty percent obligation ended with it.",
   dict(type="big", kicker="2010 · THE DEFENSE ARGUMENT", lines=["Probation over.", "So is the|50 percent?"], src=SRC_AP13)),
 L("Meanwhile, Hollywood came calling. Belfort earned nine hundred forty thousand five hundred dollars from the sale of the movie rights, the A.P. reported, and prosecutors said his payments fell sharply after his probation ended.",
   dict(type="stat", kicker="THE MOVIE RIGHTS", value="$940,500", label="Belfort's earnings from the sale, per the AP", src=SRC_AP13),
   show="Meanwhile, Hollywood came calling. Belfort earned $940,500 from the sale of the movie rights, the AP reported, and prosecutors said his payments fell sharply after his probation ended."),
 L("In October twenty thirteen, about two months before the film's release, prosecutors asked a federal judge in Brooklyn to find Belfort in default. They said he had paid only eleven point six million of the hundred and ten million he owed. They later withdrew the request, to allow settlement talks.",
   dict(type="bars", kicker="OCTOBER 2013 · PROSECUTORS", title="Paid vs. owed", items=[{"label": "OWED", "value": 110, "display": "$110M"}, {"label": "PAID", "value": 11.6, "display": "$11.6M"}], src=SRC_AP13),
   show="In October 2013, about two months before the film's release, prosecutors asked a federal judge in Brooklyn to find Belfort in default. They said he had paid only $11.6 million of the $110 million he owed. They later withdrew the request, to allow settlement talks."),
 L("Belfort told the A.P. he had offered to pay one hundred percent of his book and movie profits. I don't want to make any money from the books or the movie, he said.",
   dict(type="quote", q="I don't want to make any money from the books or the movie.", case="JORDAN BELFORT", doc="TO THE ASSOCIATED PRESS · NOVEMBER 2013", cite=SRC_AP13),
   show="Belfort told the AP he had offered to pay 100 percent of his book and movie profits. \"I don't want to make any money from the books or the movie,\" he said."),
 L("And then the film came out. Bloomberg reported that it made about one hundred million dollars. But the strangest part of the movie's money was not what it earned. It was where it came from.",
   dict(type="big", kicker="THE WOLF OF WALL STREET · 2013", lines=["The question", "nobody asked:|who paid for it?"], src=SRC_BBG18)),
 # III
 L("Chapter three. Life imitates art.", dict(type="chapter", n="III", title="Life Imitates Art")),
 L("July twentieth, twenty sixteen. The Justice Department announced its largest kleptocracy case, against money stolen from a Malaysian state investment fund called one M.D.B.",
   doc("cald", "DEPARTMENT OF JUSTICE · JULY 20, 2016", "The 1MDB case", SRC_CALD, 0),
   show="July 20, 2016. The Justice Department announced its largest kleptocracy case, against money stolen from a Malaysian state investment fund called 1MDB."),
 L("In her remarks, Assistant Attorney General Leslie Caldwell described where some of that money went, including to a California motion picture company, Red Granite Pictures.",
   doc("cald", "AAG LESLIE R. CALDWELL · REMARKS", "Red Granite Pictures", SRC_CALD, 1)),
 L("Then she said this. Red Granite Pictures, in turn, used more than one hundred million dollars involved in the theft from one M.D.B. to finance the award-winning twenty thirteen film, The Wolf of Wall Street.",
   doc("cald", "AAG LESLIE R. CALDWELL · REMARKS", "“to finance … The Wolf of Wall Street”", SRC_CALD, 2),
   show="Then she said this: \"Red Granite Pictures, in turn, used more than $100 million involved in the theft from 1MDB to finance the award-winning 2013 film The Wolf of Wall Street.\""),
 L("And, as she put it, according to the allegations in the complaint, this is a case where life imitated art.",
   dict(type="quote", q="According to the allegations in the complaint, this is a case where life imitated art.", case="AAG LESLIE R. CALDWELL", doc="DOJ PRESS CONFERENCE · JULY 20, 2016", cite=SRC_CALD)),
 L("To be clear, Belfort was not accused of anything in that case. But in March twenty eighteen, Red Granite agreed to pay the U.S. government sixty million dollars to settle the forfeiture lawsuit. The settlement says the payment is not an admission of wrongdoing or liability.",
   dict(type="stat", kicker="RED GRANITE SETTLEMENT · MARCH 2018", value="$60M", label="to the U.S. · no admission of wrongdoing", src=SRC_CNBC),
   show="To be clear, Belfort was not accused of anything in that case. But in March 2018, Red Granite agreed to pay the U.S. government $60 million to settle the forfeiture lawsuit. The settlement says the payment is not an admission of wrongdoing or liability."),
 L("So a movie about a fraud was paid for, prosecutors alleged, with money from another fraud. And the studio agreed to pay sixty million dollars, almost five times what prosecutors said Belfort had paid his victims by then.",
   dict(type="bars", kicker="BY 2018", title="Two numbers, same movie", items=[{"label": "RED GRANITE SETTLEMENT", "value": 60, "display": "$60M"}, {"label": "PAID FOR BELFORT'S VICTIMS", "value": 12.8, "display": "$12.8M"}], src=SRC_CNBC + " · " + SRC_BBG18),
   show="So a movie about a fraud was paid for, prosecutors alleged, with money from another fraud. And the studio agreed to pay $60 million, almost five times what prosecutors said Belfort had paid his victims by then."),
 L("But the victims were still waiting. And in twenty seventeen, prosecutors started digging into Belfort's own companies.",
   dict(type="big", kicker="2017", lines=["Follow the money.", "Into his|own companies."], src=SRC_LAS)),
 # IV
 L("Chapter four. The subpoenas.", dict(type="chapter", n="IV", title="The Subpoenas")),
 L("In November twenty seventeen, the government served subpoenas on three companies it said were jointly owned by Belfort: Global Motivation, J.B. Global Holdings, and J.B. Global. It wanted their books and records.",
   doc("mtc_2", MTC, "Three companies, jointly owned", SRC_MTC, 1),
   show="In November 2017, the government served subpoenas on three companies it said were jointly owned by Belfort: Global Motivation, JB Global Holdings, and JB Global. It wanted their books and records."),
 L("The deadline was December first. According to the prosecutor's sworn declaration, the companies failed to produce any documents, or respond to the subpoenas in any manner.",
   doc("las_3", "PROSECUTOR'S DECLARATION · MARCH 2018", "No documents. No response.", SRC_LAS, 0)),
 L("The government sent a letter in December. No response. It sent more letters in March. No response.",
   doc("las_3", "PROSECUTOR'S DECLARATION · MARCH 2018", "Still no response", SRC_LAS, 1)),
 L("So on March twenty-ninth, twenty eighteen, the United States went to federal court in Nevada and filed this: a motion to compel the companies to comply.",
   doc("mtc_1", "FILED MARCH 29, 2018 · DISTRICT OF NEVADA", "Motion to Compel", SRC_MTC, 0),
   show="So on March 29, 2018, the United States went to federal court in Nevada and filed this: a motion to compel the companies to comply."),
 L("And attached to it was the work of a forensic accountant, a former I.R.S. criminal investigator hired by the U.S. Attorney's Office, who had gone through the books of Belfort's companies.",
   doc("gil_1", GIL, "A forensic accountant", SRC_GIL, 0)),
 L("He found an account on the balance sheet of Global Motivation called Distributions. It recorded personal expenses of Belfort and his business partner, paid by the company.",
   doc("gil_1", GIL, "Personal expenses, paid by the company", SRC_GIL, 1)),
 L("As of August fifth, twenty seventeen, the balance was nine million, one hundred eighty-eight thousand, eight hundred seventy-six dollars and six cents.",
   doc("gil_1", GIL, "$9,188,876.06", SRC_GIL, 2),
   show="As of August 5, 2017, the balance was $9,188,876.06."),
 L("Was it a loan? The accountant wrote that he found no documentation of any promise or agreement to pay the company back. In a deposition, Belfort was asked if he signed any loan agreements with the company. His answer: No. Had the company loaned him money? Not to my knowledge.",
   doc("gil_2", GIL, "“No.” · “Not to my knowledge.”", SRC_GIL, 0)),
 # V
 L("Chapter five. Nine million dollars.", dict(type="chapter", n="V", title="Nine Million Dollars")),
 L("Now look at the years. In twenty thirteen, twenty fourteen and twenty fifteen, the accountant found, Belfort and his partner had the company pay their personal expenses: one point four million, then two point eight million, then three point seven million dollars.",
   doc("gil_2", GIL, "2013 · 2014 · 2015", SRC_GIL, 1),
   show="Now look at the years. In 2013, 2014 and 2015, the accountant found, Belfort and his partner had the company pay their personal expenses: $1.4 million, then $2.8 million, then $3.7 million."),
 L("And on his own tax returns for those years, Belfort reported income from his four companies of about eight hundred ninety-three thousand, one point nine million, and one point eight million dollars.",
   dict(type="bars", kicker="PER THE GOVERNMENT'S ACCOUNTANT", title="Expenses paid by the company vs. income reported", items=[{"label": "2013 EXPENSES*", "value": 1.42, "display": "$1.42M"}, {"label": "2013 INCOME REPORTED", "value": 0.89, "display": "$0.89M"}, {"label": "2014 EXPENSES*", "value": 2.79, "display": "$2.79M"}, {"label": "2014 INCOME REPORTED", "value": 1.87, "display": "$1.87M"}, {"label": "2015 EXPENSES*", "value": 3.72, "display": "$3.72M"}, {"label": "2015 INCOME REPORTED", "value": 1.77, "display": "$1.77M"}], src=SRC_GIL + " · *Belfort and his partner together"),
   show="And on his own tax returns for those years, Belfort reported income from his four companies of about $893,000, $1.9 million, and $1.8 million."),
 L("The accountant's conclusion: those personal expenses were not reported as income on the returns, as standard accounting principles require.",
   doc("gil_2", GIL, "Not reported as income", SRC_GIL, 3)),
 L("Why does that matter? Because the deal was half his income. In the motion, the government wrote: at least a portion of these funds could have been applied to the defendant's restitution liability.",
   doc("mtc_6", MTC, "“could have been applied to the defendant's restitution”", SRC_MTC, 2),
   show="Why does that matter? Because the deal was half his income. In the motion, the government wrote: \"At least a portion [of] these funds could have been applied to the defendant's restitution liability.\""),
 L("The government went further. It said the company also paid hundreds of thousands of dollars in salary to two of Belfort's children, neither of whom, it said, actually worked there. And it argued the companies were his alter egos.",
   doc("mtc_7", MTC, "“alter egos”", SRC_MTC, 1)),
 L("The companies hired a lawyer, and produced QuickBooks records that, prosecutors said, were only partially responsive. In May twenty eighteen, the U.S. Attorney's Office told the judge the delay had been extensive and seemingly willful.",
   doc("l9_2", "U.S. ATTORNEY'S LETTER · MAY 23, 2018", "“extensive and seemingly willful”", SRC_L9, 1),
   show="The companies hired a lawyer, and produced QuickBooks records that, prosecutors said, were only partially responsive. In May 2018, the U.S. Attorney's Office told the judge the delay had been \"extensive and seemingly willful.\""),
 L("That same month, in court papers, prosecutors said Belfort had earned at least nine million dollars from speaking engagements from twenty thirteen to twenty fifteen, and kept all of it. Bloomberg reported their words: he isn't just a con, but also a deadbeat.",
   dict(type="quote", q="isn't just a con, but also a deadbeat", case="FEDERAL PROSECUTORS", doc="COURT PAPERS · AS QUOTED BY BLOOMBERG · MAY 2018", cite=SRC_BBG18),
   show="That same month, in court papers, prosecutors said Belfort had earned at least $9 million from speaking engagements from 2013 to 2015, and kept all of it. Bloomberg reported their words: he \"isn't just a con, but also a deadbeat.\""),
 L("Belfort and his lawyer disputed the government's numbers. She argued he was cash-strapped.",
   dict(type="big", kicker="THE DEFENSE · MAY 2018", lines=["\"Cash-strapped.\"", "He disputes|their numbers."], src=SRC_BBG18)),
 L("At the hearing, Belfort wasn't there. He was in Lithuania, scheduled to give a motivational speech. Judge Ann Donnelly, as Bloomberg reported it: It seems like he has some spare change lying around.",
   dict(type="quote", q="It seems like he has some spare change lying around.", case="JUDGE ANN M. DONNELLY", doc="E.D.N.Y. HEARING · AS REPORTED BY BLOOMBERG · MAY 2018", cite=SRC_BBG18),
   show="At the hearing, Belfort wasn't there. He was in Lithuania, scheduled to give a motivational speech. Judge Ann Donnelly, as Bloomberg reported it: \"It seems like he has some spare change lying around.\""),
 L("And, she added: He's going to have to come here so we can get a grip on what's going on.",
   dict(type="quote", q="He's going to have to come here so we can get a grip on what's going on.", case="JUDGE ANN M. DONNELLY", doc="AS REPORTED BY BLOOMBERG · MAY 2018", cite=SRC_BBG18)),
 # VI
 L("Chapter six. The quiet ending.", dict(type="chapter", n="VI", title="The Quiet Ending")),
 L("So what happened next? Not a trial. Not a contempt finding. Paperwork.",
   dict(type="big", kicker="2018–2022", lines=["No trial.", "Paperwork."], src=SRC_L16 + " · " + SRC_L12)),
 L("In October twenty twenty-one, the U.S. Attorney's Office told the court there were no outstanding disputes about the subpoenas, and asked the judge to dismiss the case.",
   doc("l16_1", "U.S. ATTORNEY'S LETTER · OCTOBER 15, 2021", "“no outstanding disputes”", SRC_L16, 0),
   show="In October 2021, the U.S. Attorney's Office told the court there were no outstanding disputes about the subpoenas, and asked the judge to dismiss the case."),
 L("And in April twenty twenty-two, in the other case, it wrote that Belfort and his companies had complied with the subpoenas. Dismissed.",
   doc("l12_1", "U.S. ATTORNEY'S LETTER · APRIL 8, 2022", "“have complied”", SRC_L12, 0),
   show="And in April 2022, in the other case, it wrote that Belfort and his companies had complied with the subpoenas. Dismissed."),
 L("The public court record we found does not say what those records showed, or what deal, if any, followed.",
   dict(type="list", kicker="WHAT THE PUBLIC RECORD DOESN'T SHOW", items=[["?", "what the records revealed"], ["?", "any settlement of the 50% dispute"], ["?", "a final accounting of payments"]], src=SRC_L12 + " · " + SRC_CNW)),
 L("Then came the clock. Federal law puts an end date on restitution. The liability to pay restitution shall terminate on the date that is the later of twenty years from the entry of judgment, or twenty years after release from prison.",
   dict(type="quote", q="The liability to pay restitution shall terminate on the date that is the later of 20 years from the entry of judgment…", case="18 U.S.C. § 3613(b)", doc="FEDERAL LAW · TERMINATION OF LIABILITY", cite=SRC_LAW),
   show="Then came the clock. Federal law puts an end date on restitution: \"The liability to pay restitution shall terminate on the date that is the later of 20 years from the entry of judgment\" — or 20 years after release from prison."),
 L("For Belfort, according to TMZ's sources, that date was April twenty-eighth, twenty twenty-six. TMZ reported that a court-appointed trustee had distributed a much lower amount than the order to the fifteen hundred thirteen victims.",
   dict(type="big", kicker="APRIL 28, 2026 · PER TMZ'S SOURCES", lines=["20 years.", "Time's up."], src=SRC_TMZ),
   show="For Belfort, according to TMZ's sources, that date was April 28, 2026. TMZ reported that a court-appointed trustee had distributed a much lower amount than the order to the 1,513 victims."),
 L("How much lower? No final public accounting has been released. One outside estimate, by the website Celebrity Net Worth, puts the total at about thirteen point seven five million dollars. That would be roughly twelve and a half cents on the dollar.",
   dict(type="stat", kicker="AN OUTSIDE ESTIMATE · NOT AN OFFICIAL FIGURE", value="≈12.5¢", label="per dollar ordered (~$13.75M of $110.4M)", src=SRC_CNW),
   show="How much lower? No final public accounting has been released. One outside estimate, by the website Celebrity Net Worth, puts the total at about $13.75 million. That would be roughly 12.5 cents on the dollar."),
 L("Belfort sees it differently. For nearly three decades, he told TMZ, I've lived with the consequences of my past and worked every day to take responsibility for it.",
   dict(type="quote", q="For nearly three decades, I've lived with the consequences of my past and worked every day to take responsibility for it.", case="JORDAN BELFORT", doc="STATEMENT TO TMZ · JULY 2026", cite=SRC_TMZ)),
 # CLOSE
 L("Which brings us to this week. Tech press reports say Belfort's new startup, Tone, co-founded with investor Shervin Pishevar, builds A.I. voices trained on the sales techniques he calls tonalities, for automated sales calls.",
   dict(type="list", kicker="TONE · LAUNCHED NOV 16, 2026 · PER TECH PRESS", items=[["1", "AI voices trained on Belfort's sales methods"], ["2", "automated sales calls"], ["3", "≈$10M raised, Belfort says"], ["4", "$700K–$1M in revenue, Belfort says"]], src=SRC_TONE),
   show="Which brings us to this week. Tech press reports say Belfort's new startup, Tone, co-founded with investor Shervin Pishevar, builds AI voices trained on the sales techniques he calls \"tonalities,\" for automated sales calls."),
 L("In twenty fourteen, he said he hoped to earn north of a hundred million dollars from his speeches, and told reporters: once everyone is paid back, believe me, I will feel a lot better.",
   dict(type="quote", q="Once everyone is paid back, believe me I will feel a lot better.", case="JORDAN BELFORT", doc="2014 · AS QUOTED BY BLOOMBERG", cite=SRC_BBG18),
   show="In 2014, he said he hoped to earn \"north of $100 million\" from his speeches, and told reporters: \"Once everyone is paid back, believe me I will feel a lot better.\""),
 L("The order said one hundred ten million dollars. The prosecutors' last public count said twelve point eight. The law said twenty years.",
   dict(type="list", kicker="THE PAPER TRAIL, IN THREE NUMBERS", items=[["$110.4M", "ordered, 2003"], ["$12.8M", "paid by 2018, prosecutors said"], ["20 YRS", "then the liability ends"]], src=SRC_MTC + " · " + SRC_BBG18 + " · " + SRC_LAW),
   show="The order said $110 million. The prosecutors' last public count said $12.8 million. The law said 20 years."),
 L("So here is the question. Should restitution to fraud victims ever expire? Tell us in the comments. This is SWORN.",
   dict(type="end", cta="SHOULD RESTITUTION EVER EXPIRE?")),
]

# ---- fact-check fixes (factcheck.md, 26 FIX items) and digit subtitles ----
SRC_TONE2 = "Startup Fortune (Nov 17, 2026, citing TechCrunch and TokenPost) · Analytics Insight (Nov 17, 2026)"
def P(i, say=None, show=None, **sc):
    if say: lines[i]["say"] = say
    if show: lines[i]["show"] = show
    for k, v in sc.items(): lines[i]["scene"][k] = v
lines[4]["scene"]["kicker"] = "APRIL 28, 2026 (PER TMZ'S SOURCES) → NOV 16, 2026"
lines[4]["scene"]["src"] = SRC_TMZ + " · " + SRC_TONE2
lines[8]["scene"]["items"][3] = ["4", "then the prices crash"]
P(10, say="He pleaded guilty in nineteen ninety-nine, and agreed to become a government witness.", show="He pleaded guilty in 1999, and agreed to become a government witness.")
lines[21]["say"] = lines[21]["say"].replace("about two months before", "less than three months before")
lines[21]["show"] = lines[21]["show"].replace("about two months before", "less than three months before")
P(25, say="July twentieth, twenty sixteen. The Justice Department announced the largest action ever brought by its Kleptocracy Initiative, over money it alleged was stolen from a Malaysian state investment fund called one M.D.B.",
      show="July 20, 2016. The Justice Department announced the largest action ever brought by its Kleptocracy Initiative, over money it alleged was stolen from a Malaysian state investment fund called 1MDB.")
P(26, say="In her remarks, Assistant Attorney General Leslie Caldwell described where, according to the complaint, some of that money went, including to a California-based motion picture company, Red Granite Pictures.")
P(31, say="But the victims were still waiting. And by twenty seventeen, prosecutors were digging into Belfort's own companies.", show="But the victims were still waiting. And by 2017, prosecutors were digging into Belfort's own companies.")
P(44, say="The accountant's conclusion: Belfort's personal expenses paid by the company were not reported as income on his tax returns, as standard accounting principles require.")
lines[46]["say"] = lines[46]["say"].replace("two of Belfort's children", "Belfort's two children")
P(48, say="That same month, prosecutors said, as Bloomberg reported, that Belfort had earned at least nine million dollars from speaking engagements from twenty thirteen to twenty fifteen, and kept all of it. Bloomberg summed up their position: he isn't just a con, but also a deadbeat, prosecutors say.",
      show="That same month, prosecutors said, as Bloomberg reported, that Belfort had earned at least $9 million from speaking engagements from 2013 to 2015, and kept all of it. Bloomberg summed up their position: he \"isn't just a con, but also a deadbeat, prosecutors say.\"",
      q="…isn't just a con, but also a deadbeat, prosecutors say.", case="BLOOMBERG NEWS", doc="SUMMING UP PROSECUTORS' POSITION · MAY 2018")
P(55, say="And in April twenty twenty-two, in the other case, it wrote that Belfort and his companies had complied with the subpoenas, and asked the court to dismiss the case.",
      show="And in April 2022, in the other case, it wrote that Belfort and his companies had complied with the subpoenas, and asked the court to dismiss the case.")
lines[61]["scene"]["src"] = SRC_TONE2
lines[62]["say"] = lines[62]["say"].replace("and told reporters:", "and said:")
lines[62]["show"] = lines[62]["show"].replace("and told reporters:", "and said:")
P(63, say="The order said one hundred ten million dollars. The last count from prosecutors that we found said twelve point eight million. The law said twenty years.",
      show="The order said $110 million. The last count from prosecutors that we found said $12.8 million. The law said 20 years.")
for i, t in {9: "Bloomberg reported that at its peak, the firm employed more than 1,000 brokers. The FBI arrested Belfort in 1998.",
             13: "And the plan for paying them back was simple. After his release, he was ordered to pay 50 percent of his gross income to his victims.",
             14: "Remember that number. 50 percent. Because the next 20 years are a fight over what it covered, and for how long.",
             18: "In 2010, prosecutors later said, he paid nothing.",
             19: "2010 was also the year his probation ended. And Belfort's lawyers argued that the 50 percent obligation ended with it.",
             23: "And then the film came out. Bloomberg reported that it made about $100 million. But the strangest part of the movie's money was not what it earned. It was where it came from.",
             34: "The deadline was December 1. According to the prosecutor's sworn declaration, the companies failed to produce any documents, or respond to the subpoenas in any manner.",
             41: "Chapter five. $9 million."}.items():
    lines[i]["show"] = t
from panfix import fix
fix(lines, "long")
spec = {"label": "SWORN · CASE 017", "lines": lines}
if __name__ == "__main__":
    json.dump(spec, open(os.path.join(HERE, "episode.json"), "w"), indent=1, ensure_ascii=False)
    print(len(lines), "lines,", sum(len(l["say"].split()) for l in lines), "words")
