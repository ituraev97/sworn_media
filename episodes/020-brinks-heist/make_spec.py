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
SRC_I = "Indictment, U.S. v. Mestanza Cercado et al. (C.D. Cal. 5:25-cr-198, filed June 11, 2025)"
SRC_P = "Plea agreement for defendant Mestanza, Dkt. 158 (C.D. Cal., filed Nov 9, 2026) — agreed facts"
SRC_S = "Joint stipulation to continue trial, Dkt. 156 (C.D. Cal., filed Sep 10, 2026)"
SRC_PR26 = "U.S. Attorney's Office, C.D. Cal., press release (Nov 19, 2026)"
SRC_PR25 = "U.S. Attorney's Office, C.D. Cal., press release (June 17, 2025)"
SRC_LAT = "Los Angeles Times, \"Inside the Brink's heist probe\" (2025), citing officials not authorized to comment"
SRC_AP22 = "Associated Press / NBC News (Aug 2022), on the lawsuits"
SRC_NPR = "NPR (June 18, 2025)"
SRC_REUT = "Reuters (Steve Gorman, Nov 19, 2026)"
I = "INDICTMENT · "
PA = "PLEA AGREEMENT · "
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
lines = [
 # COLD OPEN
 L("July eleventh, twenty twenty-two. The early hours. A Brinks semitruck carrying seventy-three bags of jewelry stops at a truck stop in Lebec, California, north of Los Angeles.",
   doc("p_73", PA + "¶ 13 · JULY 10, 2022", "73 bags of jewelry", SRC_P),
   show="July 11, 2022. The early hours. A Brinks semitruck carrying 73 bags of jewelry stops at a truck stop in Lebec, California, north of Los Angeles."),
 L("By the time it is noticed, twenty-four bags are gone. Their owners later put the value at about one hundred million dollars.",
   dict(type="stat", kicker="LEBEC, CALIFORNIA · JULY 11, 2022", value="$100M", label="24 bags of jewelry, as valued by the victims", src=SRC_P),
   show="By the time it is noticed, 24 bags are gone. Their owners later put the value at about $100 million."),
 L("Federal prosecutors would call it the largest jewelry heist in U.S. history.",
   doc("pr25:largest", "U.S. ATTORNEY · C.D. CAL. · JUNE 17, 2025", "“the largest jewelry heist in U.S. history”", SRC_PR25)),
 L("On November nineteenth, twenty twenty-six, the man prosecutors call the lead defendant stood in a federal courtroom in Riverside and pleaded guilty.",
   dict(type="verdict", kicker="NOVEMBER 19, 2026 · RIVERSIDE", stamp="GUILTY PLEA", big="Mestanza Cercado", sub="Carlos Victor Mestanza Cercado · lead defendant · sentencing April 15, 2027"),
   show="On November 19, 2026, the man prosecutors call the lead defendant stood in a federal courtroom in Riverside and pleaded guilty."),
 L("But inside his plea agreement is a sentence that changes the whole story. He says certain victims had declared that jewelry to Brinks at a total of less than ten million dollars.",
   doc("p_declared", PA + "¶ 9", "“a total value of less than $10,000,000”", SRC_P),
   show="But inside his plea agreement is a sentence that changes the whole story. He says certain victims had declared that jewelry to Brinks at a total of less than $10 million."),
 L("A hundred million, or under ten. This is the case, from the court records.",
   dict(type="title", kicker="SWORN · CASE 020 · BREAKING", title="The Brinks Heist|$100 Million", sub="United States v. Mestanza Cercado et al. · C.D. Cal. · guilty plea"),
   show="$100 million, or under $10 million. This is the case, from the court records."),
 # I
 L("Chapter one. The crew.", dict(type="chapter", n="I", title="The Crew")),
 L("The defendant is Carlos Victor Mestanza Cercado, an Ecuadorian national, thirty-three years old, whose past addresses include one in Pasadena.",
   doc("pr26:plea", "U.S. ATTORNEY · C.D. CAL. · NOV 19, 2026", "Ecuadorian national, 33", SRC_PR26),
   show="The defendant is Carlos Victor Mestanza Cercado, an Ecuadorian national, 33 years old, whose past addresses include one in Pasadena."),
 L("In his plea agreement, he admits what he and his co-conspirators did, starting no later than March second, twenty twenty-two.",
   doc("p_guilty", PA + "¶ 13 · FACTUAL BASIS", "“in fact, guilty”", SRC_P),
   show="In his plea agreement, he admits what he and his co-conspirators did, starting no later than March 2, 2022."),
 L("The method was simple. Use several cars. Follow a truck carrying valuable cargo. Wait for the driver to stop, at a truck stop, a store, a restaurant. Then take what is inside, and drive it back to Los Angeles County to divide up and sell.",
   doc("p_series", PA + "¶ 13", "Follow the truck. Wait for the stop.", SRC_P)),
 L("March second. A truck carrying Samsung electronics stops at a 7-Eleven in Ontario, California. Someone approaches the driver and asks for help translating from Spanish into English, to buy a prepaid phone to call Mexico.",
   doc("p_711", PA + "¶ 13 · MARCH 2, 2022", "The translation request", SRC_P),
   show="March 2. A truck carrying Samsung electronics stops at a 7-Eleven in Ontario, California. Someone approaches the driver and asks for help translating from Spanish into English, to buy a prepaid phone to call Mexico."),
 L("It was a decoy. While the driver helped, the others emptied the truck. The victims later valued that load at about two hundred forty thousand dollars.",
   dict(type="stat", kicker="ONTARIO, CA · MARCH 2, 2022", value="$240,573", label="Samsung electronics, as valued by the victims", src=SRC_P),
   show="It was a decoy. While the driver helped, the others emptied the truck. The victims later valued that load at about $240,573."),
 L("Nine days later, in Fontana, it was Apple AirTags, shipped from China. The driver stopped for food. This time he came back too early, and caught them in the act.",
   doc("p_airtag", PA + "¶ 13 · MARCH 11, 2022", "Caught in the act", SRC_P),
   show="9 days later, in Fontana, it was Apple AirTags, shipped from China. The driver stopped for food. This time he came back too early, and caught them in the act."),
 L("According to the agreed facts, a co-conspirator held a small knife and yelled at him: Don't move, or I will, and then an obscenity. The driver did not intervene.",
   dict(type="quote", q="“Don’t move, or I will [expletive] you up!”", case="A co-conspirator, to the AirTags driver · March 11, 2022", doc="As quoted in the plea agreement, ¶ 13", cite=SRC_P),
   show="According to the agreed facts, a co-conspirator held a small knife and yelled at him: \"Don't move, or I will [expletive] you up!\" The driver did not intervene."),
 L("That moment matters more than the AirTags themselves, which were valued at about fifty-seven thousand dollars. Because a threat of force turns a theft into a robbery. Hold on to that. It comes back at the end.",
   dict(type="big", kicker="MARCH 11, 2022 · FONTANA", lines=["$57,377", "in AirTags.|Theft → robbery."], src=SRC_P),
   show="That moment matters more than the AirTags themselves, which were valued at about $57,377. Because a threat of force turns a theft into a robbery. Hold on to that. It comes back at the end."),
 L("Mestanza admits he was driving the van the stolen goods were to be loaded into, and that he stayed on the phone with a co-conspirator for eighty-seven minutes, tracking the driver's movements.",
   doc("p_87", PA + "¶ 13", "87 minutes on the phone", SRC_P),
   show="Mestanza admits he was driving the van the stolen goods were to be loaded into, and that he stayed on the phone with a co-conspirator for 87 minutes, tracking the driver's movements."),
 L("May twenty-fifth, Fontana again. At a truck stop, a crowbar on a semitruck, and they fled. The same day, Samsung electronics from another truck, about fourteen thousand dollars' worth.",
   dict(type="timeline", kicker="2022 · PER THE PLEA AGREEMENT", events=[{"date": "Mar 2", "text": "Ontario · Samsung · $240,573"}, {"date": "Mar 11", "text": "Fontana · AirTags · $57,377"}, {"date": "May 25", "text": "Fontana · crowbar, then Samsung · $14,081"}, {"date": "Jul 11", "text": "Lebec · jewelry · ~$100M"}], at=2, src=SRC_P),
   show="May 25, Fontana again. At a truck stop, a crowbar on a semitruck, and they fled. The same day, Samsung electronics from another truck, about $14,081 worth."),
 L("A few hundred thousand dollars in four months. Then, in July, they found a truck carrying something else entirely.",
   dict(type="big", lines=["Then, July 2022.", "A jewelry show."], src=SRC_P)),
 # II
 L("Chapter two. The show.", dict(type="chapter", n="II", title="The Show")),
 L("July eighth, ninth and tenth, twenty twenty-two. An international jewelry show in San Mateo, south of San Francisco. According to the plea agreement, a co-conspirator scouted it, on the phone with Mestanza and the others, planning to steal the jewelry in transit after the show.",
   doc("p_scout", PA + "¶ 13 · JULY 8–10, 2022", "Scouting the show", SRC_P),
   show="July 8, 9 and 10, 2022. An international jewelry show in San Mateo, south of San Francisco. According to the plea agreement, a co-conspirator scouted it, on the phone with Mestanza and the others, planning to steal the jewelry in transit after the show."),
 L("On the tenth they picked their target. A Brinks semitruck at the show, loaded with seventy-three bags containing millions of dollars of jewelry.",
   doc("i_oa17", I + "OVERT ACT 17 · JULY 10, 2022", "“73 bags containing millions of dollars in jewelry”", SRC_I),
   show="On the 10th they picked their target. A Brinks semitruck at the show, loaded with 73 bags containing millions of dollars of jewelry."),
 L("The indictment lists the phone chain when the truck left: one defendant called a second, the second called a third, the third called a fourth.",
   doc("i_oa18", I + "OVERT ACT 18", "Upon the truck's departure: the calls", SRC_I)),
 L("Then they followed it. From the late hours of July tenth into the early hours of the eleventh. About three hundred miles, from San Mateo south through the Central Valley, to rest stops in Buttonwillow and Lebec.",
   doc("p_300", PA + "¶ 13 · JULY 10–11, 2022", "About 300 miles", SRC_P),
   show="Then they followed it. From the late hours of July 10 into the early hours of the 11th. About 300 miles, from San Mateo south through the Central Valley, to rest stops in Buttonwillow and Lebec."),
 L("Lebec sits on Interstate five, in the mountains north of Los Angeles. A place where truckers stop.",
   dict(type="big", kicker="LEBEC, CALIFORNIA", lines=["Interstate 5.", "The truck stops."], src=SRC_P),
   show="Lebec sits on Interstate 5, in the mountains north of Los Angeles. A place where truckers stop."),
 L("What happened next is told in one sentence of the agreed facts. They broke the locks on the Brinks truck and stole twenty-four bags of jewelry, which the victims later valued at approximately one hundred million dollars.",
   doc("p_24", PA + "¶ 13 · JULY 11, 2022", "“stole 24 bags of jewelry”", SRC_P),
   show="What happened next is told in one sentence of the agreed facts. They \"broke the locks on the Brinks truck and stole 24 bags of jewelry, which the victims later valued at approximately $100,000,000.\""),
 L("Where were the guards? The court papers don't say. Brinks's own lawsuit, filed weeks later, did. According to the Associated Press, it said one driver was asleep in the truck's sleeping berth, and the other was getting food. He was gone, the suit said, for twenty-seven minutes.",
   dict(type="big", kicker="PER BRINKS'S 2022 LAWSUIT, AS REPORTED BY AP", lines=["One driver asleep.", "One getting food.|27 minutes."], src=SRC_AP22),
   show="Where were the guards? The court papers don't say. Brinks's own lawsuit, filed weeks later, did. According to the Associated Press, it said one driver was asleep in the truck's sleeping berth, and the other was getting food. He was gone, the suit said, for 27 minutes."),
 L("Twenty-seven minutes. Twenty-four bags. Then the crew drove to East Hollywood with the jewelry.",
   doc("i_oa21", I + "OVERT ACT 21", "East Hollywood", SRC_I),
   show="27 minutes. 24 bags. Then the crew drove to East Hollywood with the jewelry."),
 L("One detail in the numbers. Brinks's lawsuit said twenty-two bags were missing. The indictment and the plea agreement both say twenty-four.",
   dict(type="bars", kicker="BAGS TAKEN · WHO SAYS WHAT", title="Out of 73 bags", items=[{"label": "Brinks lawsuit (2022, per AP)", "value": 22, "display": "22"}, {"label": "Indictment & plea agreement", "value": 24, "display": "24"}], src="AP (Aug 2022); " + SRC_P)),
 L("Twenty-four of seventy-three. About one bag in every three on that truck, gone while it sat at a truck stop in the middle of the night.",
   dict(type="stat", kicker="JULY 11, 2022 · LEBEC", value="24 / 73", label="about one bag in three", src=SRC_P),
   show="24 of 73. About one bag in every three on that truck, gone while it sat at a truck stop in the middle of the night."),
 L("And then the crew did the one thing that, for three years, seemed to work. They went silent.",
   dict(type="big", lines=["Then:", "silence."], src=SRC_P)),
 # III
 L("Chapter three. The silence.", dict(type="chapter", n="III", title="The Silence")),
 L("For almost three years, no one would be charged. And first, the crew went dark.",
   dict(type="big", lines=["Almost", "three years.|No charges."], src=SRC_I)),
 L("On July fourteenth, fifteenth and sixteenth, three of the defendants deactivated the cellphone numbers they had used for the heist. On July twentieth, two more did the same.",
   doc("i_oa22", I + "OVERT ACTS 22–23", "Phone numbers deactivated", SRC_I),
   show="On July 14, 15 and 16, three of the defendants deactivated the cellphone numbers they had used for the heist. On July 20, two more did the same."),
 L("Mestanza admits the reason: to try to conceal their identities.",
   doc("p_deact", PA + "¶ 13", "“to try to conceal their identities”", SRC_P)),
 L("While investigators worked in silence, the fight moved to civil court. And the fight was about one number.",
   dict(type="big", lines=["Who lost", "how much?"], src=SRC_AP22)),
 L("In August twenty twenty-two, Brinks sued the jewelers in federal court in New York. The Associated Press reported that its suit said the shipping manifests for the missing bags listed about eight point seven million dollars.",
   dict(type="stat", kicker="BRINKS'S LAWSUIT · AUG 2022 · PER AP", value="$8.7M", label="declared value on the manifests, per Brinks", src=SRC_AP22),
   show="In August 2022, Brinks sued the jewelers in federal court in New York. The Associated Press reported that its suit said the shipping manifests for the missing bags listed about $8.7 million."),
 L("The jewelers sued Brinks in Los Angeles. They said the loss was about one hundred million dollars, and, according to the AP, they alleged a Brinks employee had told them to under-value their goods.",
   dict(type="bars", kicker="THE SAME 24 BAGS · TWO NUMBERS", title="What was it worth?", items=[{"label": "Declared to Brinks (per Brinks's suit)", "value": 8.7, "display": "$8.7M"}, {"label": "Claimed by the jewelers", "value": 100, "display": "~$100M"}], src=SRC_AP22),
   show="The jewelers sued Brinks in Los Angeles. They said the loss was about $100 million, and, according to the AP, they alleged a Brinks employee had told them to under-value their goods."),
 L("Their lawyer, Jerry Kroll, told the AP: We are astounded by Brinks's lack of support for their longtime customers, who thought they were in safe hands with Brinks.",
   dict(type="quote", q="We are astounded by Brink’s lack of support for their longtime customers who thought they were in safe hands with Brink’s", case="Jerry Kroll, attorney for jewelers, 2022", doc="Quoted by the Associated Press", cite=SRC_AP22),
   show="Their lawyer, Jerry Kroll, told the AP: \"We are astounded by Brink's lack of support for their longtime customers who thought they were in safe hands with Brink's.\""),
 L("Hold on to that gap, eight point seven million against a hundred million. It shows up again, years later, in the criminal case.",
   dict(type="big", lines=["$8.7M", "vs. $100M."], src=SRC_AP22),
   show="Hold on to that gap, $8.7 million against $100 million. It shows up again, years later, in the criminal case."),
 L("So how do you find a crew that switched off its phones? The government's filings list the kind of evidence it gathered: law enforcement reports, videos, photographs, license plate reader information, and cell-site location information.",
   doc("s_discovery", "JOINT STIPULATION · DKT. 156 · SEP 2026", "License plates. Cell sites.", SRC_S)),
 L("By September twenty twenty-six, the discovery handed to the defense came to one point eight nine terabytes, thirty-three thousand one hundred sixty-four files.",
   dict(type="stat", kicker="DISCOVERY · AS OF SEP 2026", value="1.89 TB", label="33,164 files", src=SRC_S),
   show="By September 2026, the discovery handed to the defense came to 1.89569 terabytes, 33,164 files."),
 L("The Los Angeles Times later reported, citing officials who were not authorized to speak publicly, that one break came from a phone number one of the men had given to a police officer after witnessing a traffic collision. That account has not been tested in court.",
   dict(type="big", kicker="REPORTED · NOT TESTED IN COURT", lines=["A traffic collision.", "A phone number."], src=SRC_LAT)),
 L("Whatever the break was, the silence ended almost three years after the heist.",
   dict(type="big", lines=["June 2025.", "The silence ends."], src=SRC_I)),
 # IV
 L("Chapter four. The run.", dict(type="chapter", n="IV", title="The Run")),
 L("On June eleventh, twenty twenty-five, a federal grand jury in Los Angeles returned an indictment against seven men, Mestanza listed first.",
   doc("i_caption", I + "FILED JUNE 11, 2025", "United States v. Mestanza Cercado et al.", SRC_I),
   show="On June 11, 2025, a federal grand jury in Los Angeles returned an indictment against seven men, Mestanza listed first."),
 L("The charges: conspiracy, theft from interstate shipment, and, for five of them, robbery under the Hobbs Act. Count six alone covered the jewelry, valued by the victims at about one hundred million dollars.",
   doc("i_count6", I + "COUNT SIX", "Jewelry valued at ~$100,000,000", SRC_I),
   show="The charges: conspiracy, theft from interstate shipment, and, for five of them, robbery under the Hobbs Act. Count six alone covered the jewelry, valued by the victims at about $100 million."),
 L("On June sixteenth, agents executed search warrants. The U.S. Attorney's Office said some of the jewelry was recovered. It did not say how much.",
   doc("pr25:recovered", "U.S. ATTORNEY · C.D. CAL. · JUNE 17, 2025", "“Some of that jewelry was recovered”", SRC_PR25),
   show="On June 16, agents executed search warrants. The U.S. Attorney's Office said some of the jewelry was recovered. It did not say how much."),
 L("On June seventeenth, the indictment was made public, and two of the men were arrested. The F.B.I.'s Los Angeles chief, Akil Davis, said in a statement quoted by NPR: I'm gratified that we can finally begin to give answers to the victims of this massive theft.",
   dict(type="quote", q="I’m gratified that we can finally begin to give answers to the victims of this massive theft", case="Akil Davis, FBI Los Angeles, June 2025", doc="Statement quoted by NPR", cite=SRC_NPR),
   show="On June 17, the indictment was made public, and two of the men were arrested. The FBI's Los Angeles chief, Akil Davis, said in a statement quoted by NPR: \"I'm gratified that we can finally begin to give answers to the victims of this massive theft.\""),
 L("Mestanza was not one of them. And according to his own plea agreement, here is what he did next.",
   dict(type="big", lines=["He was", "not arrested.|Yet."], src=SRC_P)),
 L("After the indictment went public, he ran several internet searches about a person wanted by the police and Interpol, and about Ecuadorians like him traveling to Mexico, El Salvador, Guatemala, Belize, and Canada.",
   doc("p_search", PA + "¶ 13 · JUNE 2025", "Searches: “wanted by the police, Interpol”", SRC_P)),
 L("Between June eighteenth and twentieth, he texted someone about his stupidities from the past that I'm now paying for. He didn't know if the police were after him, he wrote, but he still had to be careful.",
   doc("p_texts", PA + "¶ 13 · JUNE 18–20, 2025", "“stupidities from the past that I’m now paying for”", SRC_P),
   show="Between June 18 and 20, he texted someone about his \"stupidities from the past that I'm now paying for.\" He didn't know if the police were after him, he wrote, but he \"still ha[s] to be careful.\""),
 L("On June twenty-eighth, he messaged a South American number on WhatsApp about crossing the U.S.-Mexico border after a robo grande. A big robbery.",
   doc("p_robo", PA + "¶ 13 · JUNE 28, 2025", "“robo grande”", SRC_P),
   show="On June 28, he messaged a South American number on WhatsApp about crossing the U.S.-Mexico border after a \"robo grande.\" A big robbery."),
 L("Prosecutors say he left the United States in June twenty twenty-five. He made it as far as Panama.",
   doc("pr26:fled", "U.S. ATTORNEY · C.D. CAL. · NOV 19, 2026", "Fled the U.S. in June 2025", SRC_PR26),
   show="Prosecutors say he left the United States in June 2025. He made it as far as Panama."),
 L("On July first, twenty twenty-five, he was detained at Tocumen International Airport in Panama City, during a layover on the way from Guatemala to Ecuador.",
   dict(type="photo", img="img/tocumen.jpg", caption="TOCUMEN INTERNATIONAL AIRPORT, PANAMA CITY (FILE PHOTO)", src="Photo: TomasVial, CC BY-SA 4.0 via Wikimedia Commons (2024)"),
   show="On July 1, 2025, he was detained at Tocumen International Airport in Panama City, during a layover on the way from Guatemala to Ecuador."),
 L("He was extradited. Since August twenty twenty-five, he has been in federal custody.",
   doc("pr26:custody", "U.S. ATTORNEY · C.D. CAL. · NOV 19, 2026", "In federal custody since August 2025", SRC_PR26),
   show="He was extradited. Since August 2025, he has been in federal custody."),
 L("His trial date was pushed back again and again. Then, in November twenty twenty-six, he signed a deal.",
   dict(type="big", lines=["November 2026.", "The deal."], src=SRC_P),
   show="His trial date was pushed back again and again. Then, in November 2026, he signed a deal."),
 # V
 L("Chapter five. The plea.", dict(type="chapter", n="V", title="The Plea")),
 L("The plea agreement was filed November ninth. On November nineteenth, in Riverside, Mestanza pleaded guilty to one count: count three.",
   doc("p_count3", PA + "¶ 2", "“plead guilty to count three”", SRC_P),
   show="The plea agreement was filed November 9. On November 19, in Riverside, Mestanza pleaded guilty to one count: count three."),
 L("Count three is not the jewelry. It is the March twenty twenty-two AirTags robbery, the one with the knife. Interference with commerce by robbery, under the Hobbs Act.",
   dict(type="big", kicker="THE COUNT HE PLEADED TO", lines=["Count three:", "the AirTags|robbery."], src=SRC_P),
   show="Count three is not the jewelry. It is the March 2022 AirTags robbery, the one with the knife. Interference with commerce by robbery, under the Hobbs Act."),
 L("In return, prosecutors will move to dismiss his remaining counts at sentencing. But the deal lets the judge consider those dismissed charges when deciding the sentence.",
   doc("p_dismiss", PA + "¶ 3(c)", "Remaining counts: dismissed at sentencing", SRC_P)),
 L("Why that one? A theft charge from an interstate shipment carries up to ten years. Robbery under the Hobbs Act carries up to twenty.",
   doc("p_max", PA + "¶ 8", "Statutory maximum: 20 years", SRC_P),
   show="Why that one? A theft charge from an interstate shipment carries up to 10 years. Robbery under the Hobbs Act carries up to 20."),
 L("And the Brinks heist is still in the deal. He admits it in the factual basis, and he agrees the court may order restitution for conduct beyond the count he pleaded to. The government believes that restitution is at least one hundred million, three hundred twelve thousand, thirty-one dollars.",
   doc("p_restit", PA + "¶ 9", "“at least $100,312,031.54”", SRC_P),
   show="And the Brinks heist is still in the deal. He admits it in the factual basis, and he agrees the court may order restitution for conduct beyond the count he pleaded to. The government believes that restitution is \"at least $100,312,031.54.\""),
 L("Now, the sentence from the beginning. Mestanza contends that before the theft, certain victims declared in their contracts with Brinks a total value of less than ten million dollars.",
   doc("p_declared", PA + "¶ 9", "“less than $10,000,000”", SRC_P),
   show="Now, the sentence from the beginning. Mestanza contends that before the theft, certain victims declared in their contracts with Brinks a total value of less than $10 million."),
 L("The government disputes that those declarations limit the victims' actual losses. Both sides may present evidence when the court decides restitution.",
   dict(type="bars", kicker="RESTITUTION · THE DISPUTE IN THE PLEA DEAL", title="What will he owe?", items=[{"label": "Government: at least", "value": 100.3, "display": "$100.3M"}, {"label": "Declared to Brinks, per defense", "value": 10, "display": "< $10M"}], src=SRC_P),
   show="The government disputes that those declarations limit the victims' actual losses. Both sides may present evidence when the court decides restitution."),
 L("It is the same gap from the civil cases, now inside a criminal plea. A hundred million dollars, or under ten.",
   dict(type="big", lines=["$100M", "or under $10M?"], src=SRC_P),
   show="It is the same gap from the civil cases, now inside a criminal plea. $100 million, or under $10 million."),
 L("United States District Judge Kenly Kiya Kato set sentencing for April fifteenth, twenty twenty-seven. The maximum is twenty years in federal prison.",
   doc("pr26:sentencing", "U.S. ATTORNEY · C.D. CAL. · NOV 19, 2026", "Sentencing: April 15, 2027", SRC_PR26),
   show="United States District Judge Kenly Kiya Kato set sentencing for April 15, 2027. The maximum is 20 years in federal prison."),
 L("And the others? Three co-defendants have pleaded not guilty and are set for trial on March twenty-second, twenty twenty-seven. They are presumed innocent.",
   doc("pr26:trial", "U.S. ATTORNEY · C.D. CAL. · NOV 19, 2026", "Trial: March 22, 2027", SRC_PR26),
   show="And the others? Three co-defendants have pleaded not guilty and are set for trial on March 22, 2027. They are presumed innocent."),
 L("Two co-defendants have never appeared in a U.S. courtroom. And the charges against one more were dismissed without prejudice in February, after he was removed from the United States.",
   doc("pr26:removed", "U.S. ATTORNEY · C.D. CAL. · NOV 19, 2026", "Dismissed; removed from the U.S.", SRC_PR26),
   show="Two co-defendants have never appeared in a U.S. courtroom. And the charges against one more were dismissed without prejudice in February, after he was removed from the United States."),
 L("Reuters noted it was not clear from court documents whether any of the jewelry from the heist was ever recovered, beyond the government's word in twenty twenty-five that some of it was.",
   dict(type="big", kicker="STILL OPEN", lines=["How much", "came back?"], src=SRC_REUT + "; " + SRC_PR25),
   show="Reuters noted it was not clear from court documents whether any of the jewelry from the heist was ever recovered, beyond the government's word in 2025 that some of it was."),
 L("So here is where it stands. Seventy-three bags. Twenty-four taken in the night. A crew that went silent for three years. A fugitive caught on a layover. And a guilty plea that leaves the biggest number in the case still open.",
   dict(type="verdict", kicker="UNITED STATES v. MESTANZA CERCADO", stamp="GUILTY PLEA", big="Sentencing: April 15, 2027", sub="Restitution claimed: at least $100.3M · disputed"),
   show="So here is where it stands. 73 bags. 24 taken in the night. A crew that went silent for three years. A fugitive caught on a layover. And a guilty plea that leaves the biggest number in the case still open."),
 L("If the declared value was under ten million dollars, should he owe a hundred million? Tell us in the comments.",
   dict(type="end"),
   show="If the declared value was under $10 million, should he owe $100 million? Tell us in the comments."),
]

# ---- independent fact-check fixes (factcheck.md) ----
def F(i, say=None, show=None, **sc):
    l = lines[i]
    if say is not None: l["say"] = say
    if show is not None: l["show"] = show
    elif say is not None: l.pop("show", None)
    if sc: l["scene"].update(sc)
F(4, "But inside his plea agreement is a sentence that puts that number in dispute. He contends that certain victims had declared the jewelry Brinks was carrying at a total value of less than ten million dollars.",
  "But inside his plea agreement is a sentence that puts that number in dispute. He contends that certain victims had declared the jewelry Brinks was carrying at a total value of less than $10 million.")
lines[7]["scene"] = doc("pr26:who", "U.S. ATTORNEY · C.D. CAL. · NOV 19, 2026", "Ecuadorian national, 33", SRC_PR26)
F(11, "It was a decoy. While the driver was distracted, others stole Samsung electronics from the truck. The victims later valued them at about two hundred forty thousand dollars.",
  "It was a decoy. While the driver was distracted, others stole Samsung electronics from the truck. The victims later valued them at about $240,000.")
F(12, "Nine days later, in Fontana, it was Apple AirTags, shipped from China. The driver stopped for food. This time, he caught them in the act.",
  "9 days later, in Fontana, it was Apple AirTags, shipped from China. The driver stopped for food. This time, he caught them in the act.")
F(14, show="That moment matters more than the AirTags themselves, which were valued at about $57,000. Because a threat of force turns a theft into a robbery. Hold on to that. It comes back at the end.")
F(16, "May twenty-fifth, Fontana again. At a truck stop, a crowbar on a semitruck, and they fled. The same day, Samsung electronics from another truck, about fourteen thousand dollars' worth.",
  "May 25, Fontana again. At a truck stop, a crowbar on a semitruck, and they fled. The same day, Samsung electronics from another truck, about $14,000 worth.")
F(17, "About three hundred thousand dollars in under three months. Then, in July, they found a truck carrying something else entirely.",
  "About $300,000 in under three months. Then, in July, they found a truck carrying something else entirely.", lines=["Then, July 2022.", "A jewelry show."])
F(21, "The indictment alleges a phone chain when the truck left: one defendant calling a second, the second a third, the third a fourth. Those are charges, not proof.")
F(23, src="Background: Wikipedia, \"2022 Brink's theft\" (Lebec, on I-5 at Tejon Pass)")
F(25, "Where were the drivers? The court papers don't say. Brinks's own lawsuit, filed weeks later, did. According to the Associated Press, it said one driver was asleep in the truck's sleeping berth, and the other was getting food. He was gone, the suit said, for twenty-seven minutes.",
  "Where were the drivers? The court papers don't say. Brinks's own lawsuit, filed weeks later, did. According to the Associated Press, it said one driver was asleep in the truck's sleeping berth, and the other was getting food. He was gone, the suit said, for 27 minutes.")
lines[26]["scene"] = doc("p_24", PA + "¶ 13 · JULY 11, 2022", "East Hollywood", SRC_P)
F(29, "And then the crew did the one thing that, for almost three years, seemed to work. They went silent.")
F(32, "According to the indictment, on July fourteenth, fifteenth and sixteenth, three of the defendants deactivated the cellphone numbers they had used for the heist, and on July twentieth, two more did the same. For everyone but Mestanza, those are still only allegations.",
  "According to the indictment, on July 14, 15 and 16, three of the defendants deactivated the cellphone numbers they had used for the heist, and on July 20, two more did the same. For everyone but Mestanza, those are still only allegations.")
lines[32]["scene"] = doc("i_oa2223", I + "OVERT ACTS 22–23 · ALLEGATIONS", "Phone numbers deactivated", SRC_I)
F(39, "So how do you find a crew that switched off its phones? A joint filing in the case lists the discovery the government has turned over: law enforcement reports, videos, photographs, license plate reader information, and cell-site location information.")
F(40, show="By September 2026, the discovery handed to the defense came to 1.89 terabytes, 33,164 files.")
F(41, "The Los Angeles Times later reported, citing two people involved with the case, that one break came from a burner-phone number one of the alleged thieves had given to a police officer after witnessing a traffic collision. That account has not been tested in court.",
  src="Los Angeles Times, \"Inside the Brink's heist probe\" (2025), citing two people involved with the case")
F(44, "On June eleventh, twenty twenty-five, a federal grand jury returned an indictment against seven men, Mestanza listed first.",
  "On June 11, 2025, a federal grand jury returned an indictment against seven men, Mestanza listed first.")
F(45, "The charges: conspiracy, theft from interstate shipment, and, for five of them, robbery under the Hobbs Act. Count six, a theft count, covered the jewelry, valued by the victims at about one hundred million dollars.",
  "The charges: conspiracy, theft from interstate shipment, and, for five of them, robbery under the Hobbs Act. Count six, a theft count, covered the jewelry, valued by the victims at about $100 million.")
F(47, "On June seventeenth, the indictment was made public, and two of the men were arrested. Akil Davis, then the assistant director in charge of the F.B.I.'s Los Angeles field office, said in a statement quoted by NPR: I'm gratified that we can finally begin to give answers to the victims of this massive theft.",
  "On June 17, the indictment was made public, and two of the men were arrested. Akil Davis, then the assistant director in charge of the FBI's Los Angeles field office, said in a statement quoted by NPR: \"I'm gratified that we can finally begin to give answers to the victims of this massive theft.\"",
  case="Akil Davis, then assistant director in charge, FBI Los Angeles · June 2025")
F(60, "Why does that matter? A theft charge from an interstate shipment carries up to ten years. Robbery under the Hobbs Act carries up to twenty.",
  "Why does that matter? A theft charge from an interstate shipment carries up to 10 years. Robbery under the Hobbs Act carries up to 20.")
F(61, "And the Brinks heist is still in the deal. He admits it in the factual basis, and he agrees the court may order restitution for conduct beyond the count he pleaded to. The government believes that restitution is at least one hundred million, three hundred twelve thousand, thirty-one dollars and fifty-four cents.",
  lines[61]["show"])
F(67, "Two other co-defendants have not appeared in a U.S. courtroom to face the charges. And the charges against one more were dismissed without prejudice in February twenty twenty-six, after he was removed from the United States. All of them are presumed innocent.",
  "Two other co-defendants have not appeared in a U.S. courtroom to face the charges. And the charges against one more were dismissed without prejudice in February 2026, after he was removed from the United States. All of them are presumed innocent.")
lines[67]["scene"] = doc("pr26:notappeared", "U.S. ATTORNEY · C.D. CAL. · NOV 19, 2026", "Not appeared · dismissed", SRC_PR26)
F(68, "Reuters noted it was not clear from court documents whether any of the stolen jewelry from the heist was ever recovered. In twenty twenty-five, the government said some of it was, but not how much.",
  "Reuters noted it was not clear from court documents whether any of the stolen jewelry from the heist was ever recovered. In 2025, the government said some of it was, but not how much.")
F(69, "So here is where it stands. Seventy-three bags. Twenty-four taken in the night. A crew that went silent for almost three years. A fugitive caught on a layover. And a guilty plea that leaves the biggest number in the case still open.",
  "So here is where it stands. 73 bags. 24 taken in the night. A crew that went silent for almost three years. A fugitive caught on a layover. And a guilty plea that leaves the biggest number in the case still open.")

json.dump({"label": "SWORN · CASE 020", "lines": lines}, open(os.path.join(HERE, "episode.json"), "w"), indent=1, ensure_ascii=False)
print(len(lines), "lines,", sum(len(l["say"].split()) for l in lines), "words")
