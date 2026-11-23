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
CASE = "United States v. Garcia, N.D. Tex. 4:26-cr-146-P"
S_IND = f"Superseding Indictment ({CASE}, Dkt. 35, filed Oct 7, 2026)"
S_PR = "U.S. Attorney's Office, N.D. Tex., press release (Nov 20, 2026)"
S_EX = f"Government trial exhibits (summary charts marked \"DRAFT\"), released by the U.S. Attorney's Office, N.D. Tex. ({CASE})"
S_NBC = "NBC 5 Dallas-Fort Worth (Jose Herrera), Nov 20, 2026"
IK = "SUPERSEDING INDICTMENT · ALLEGATIONS · "
PK = "U.S. ATTORNEY · N.D. TEX. · NOV 20, 2026"
XK = "GOV'T TRIAL EXHIBIT · DRAFT CHART"
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
VERDICT = dict(type="verdict", kicker="NOVEMBER 19, 2026 · FORT WORTH, TEX.", stamp="GUILTY", big="4 Counts", sub="Richard Reinaldo Garcia · Judge Mark T. Pittman · sentencing Mar 4, 2027")
lines = [
 # COLD OPEN
 L("Three church buildings. One in Texarkana. One in Lubbock. One in Fort Worth.",
   photo("f_never", XK + " · NAMES OF INVESTORS REDACTED BY SWORN", S_EX),
   show="Three church buildings. One in Texarkana. One in Lubbock. One in Fort Worth."),
 L("Investors put in six hundred eighty-three thousand dollars to buy them, fix them up, and sell them at a profit. A pastor called it church flipping.",
   show="Investors put in $683,000 to buy them, fix them up, and sell them at a profit. A pastor called it \"church flipping.\""),
 L("The government's chart at trial has two words under each address. Never purchased. Proceeds from sale: zero dollars.",
   dict(type="big", kicker=XK, lines=["Never purchased.", "Proceeds: $0."], src=S_EX),
   show="The government's chart at trial has two words under each address: \"NEVER PURCHASED.\" Proceeds from sale: $0."),
 L("On November nineteenth, twenty twenty-six, after a four-day trial, a federal jury in Fort Worth convicted the pastor. Richard Reinaldo Garcia, of Arlington, Texas. Guilty of conspiracy to commit wire fraud, and three counts of wire fraud.",
   VERDICT,
   show="On November 19, 2026, after a four-day trial, a federal jury in Fort Worth convicted the pastor. Richard Reinaldo Garcia, of Arlington, Texas. Guilty of conspiracy to commit wire fraud, and three counts of wire fraud."),
 L("More than seventy victims, in the United States, Colombia, Mexico and the Dominican Republic. More than six million dollars lost.",
   doc("p_70", PK, "More than 70 victims", S_PR),
   show="More than 70 victims, in the United States, Colombia, Mexico and the Dominican Republic. More than $6 million lost."),
 L("This is how a church became the bank account. From the indictment, the trial exhibits, and the verdict.",
   dict(type="title", kicker="SWORN · CASE 023 · BREAKING", title="The Church|Flipping Pastor", sub="United States v. Garcia · N.D. Tex. 4:26-cr-146 · jury verdict Nov 19, 2026"),
   show="This is how a church became the bank account. From the indictment, the trial exhibits, and the verdict."),
 # I
 L("Chapter one. The pastor.", dict(type="chapter", n="I", title="The Pastor")),
 L("Richard Garcia is fifty-three. According to the U.S. Attorney's Office, he served as a pastor during the entire scheme, and he used that position.",
   doc("p_church", PK, "“served as a pastor during the scheme”", S_PR),
   show="Richard Garcia is 53. According to the U.S. Attorney's Office, he served as a pastor during the scheme, and he used that position."),
 L("His church had many names. The indictment lists the entities he did business through: Ministerio Gracia. Iglesia Gracia de Texas. Gracia Church of Texas. A Pesar de Todo, L.L.C. And M.G. Kingdom, Incorporated.",
   doc("i_entities", IK + "¶ 1", "The “Relevant Entities”", S_IND),
   show="His church had many names. The indictment lists the entities he did business through: Ministerio Gracia. Iglesia Gracia de Texas. Gracia Church of Texas. A Pesar de Todo, LLC. And MG Kingdom, Inc."),
 L("Ministerio Gracia goes back to twenty twelve, with an address on South Collins Street in Arlington. Over the years, the indictment says, it also operated as Gracia Church Arlington, Dallas West International Church, and Jessed Community Church.",
   dict(type="list", kicker="MINISTERIO GRACIA · PER THE INDICTMENT", items=[["2012", "Registered in Texas · South Collins St, Arlington"], ["aka", "Gracia Church Arlington"], ["aka", "Dallas West International Church, Inc."], ["aka", "Jessed Community Church, Inc."]], src=S_IND + " ¶ 2"),
   show="Ministerio Gracia goes back to 2012, with an address on South Collins Street in Arlington. Over the years, the indictment says, it also operated as Gracia Church Arlington, Dallas West International Church, and Jessed Community Church."),
 L("Iglesia Gracia de Texas, registered in twenty twenty-two, had previously used the names Gracia Church Atlanta and Gracia Church. And Gracia Church of Texas, registered in twenty eighteen, had once been called Richard Garcia Ministries.",
   doc("i_names", IK + "¶¶ 3–4", "One pastor, many names", S_IND),
   show="Iglesia Gracia de Texas, registered in 2022, had previously used the names Gracia Church Atlanta and Gracia Church. And Gracia Church of Texas, registered in 2018, had once been called Richard Garcia Ministries."),
 L("The trial evidence showed that he encouraged church members to give two things to church-owned real estate projects. Their money, and their labor.",
   doc("p_church", PK, "Money and labor", S_PR),
   show="The trial evidence showed that he encouraged church members to contribute both money and labor toward church-owned real estate projects."),
 L("And some of those projects were real. According to prosecutors, properties were improved and later sold for profit. While, at the same time, Garcia was asking victims for more investments.",
   show="And some of those projects were real. According to prosecutors, properties were improved and later sold for profit. While, at the same time, Garcia was soliciting additional investments from victims."),
 L("That is what made the pitch work. The churches existed. The renovations happened. The profits were possible. The question the jury had to answer was what happened to the investors' money.",
   dict(type="big", lines=["The churches existed.", "So where did|the money go?"], src=S_PR),
   show="That is what made the pitch work. The churches existed. The renovations happened. The profits were possible. The question the jury had to answer was what happened to the investors' money."),
 # II
 L("Chapter two. The pitch.", dict(type="chapter", n="II", title="The Pitch")),
 L("From about August twenty twenty-one to April twenty twenty-five, the indictment says, Garcia sold two kinds of deals.",
   doc("p_scheme", PK, "August 2021 – April 2025", S_PR),
   show="From about August 2021 to April 2025, the indictment says, Garcia sold two kinds of deals."),
 L("Deal number one: partnership agreements. The indictment calls them church flipping contracts. Investors' money would renovate church properties that Garcia owned, the properties would be sold to a third-party buyer, and each investor would get a specific return, written into the contract.",
   doc("i_flip", IK + "¶ 10(a)", "“Church Flipping” contracts", S_IND),
   show="Deal number one: partnership agreements. The indictment calls them \"Church Flipping\" contracts. Investors' money would renovate church properties that Garcia owned, the properties would be sold to a third-party buyer, and each investor would get a specific return, written into the contract."),
 L("Deal number two: joint venture agreements for international Christian music concerts. According to the indictment, investors were told their money, combined with sponsorship deals and agreements with local Colombian government entities, would fund concerts that sold tickets, and profits would be shared.",
   doc("i_concert", IK + "¶ 10(b)", "Christian music concerts", S_IND),
   show="Deal number two: \"Joint Venture\" agreements for international Christian music concerts. According to the indictment, investors were told their money, combined with sponsorship deals and agreements with local Colombian government entities, would fund concerts that sold tickets, and profits would be shared."),
 L("The grand jury charged that he never intended to host the concerts as scheduled, or to share the profits. The money, it says, went to operating costs, unrelated business, and personal expenses.",
   doc("i_notintend", IK + "¶ 10(b)", "“did not intend”", S_IND),
   show="The grand jury charged that he did not intend to host the concerts as scheduled, or to share the profits. The money, it says, went to operating costs, unrelated business, and personal expenses."),
 L("There was more. The indictment says some investors were sold the same stake that other investors already owned.",
   doc("i_dup", IK + "¶ 10(d)", "Duplicate agreements", S_IND),
   show="There was more. The indictment says some investors were offered an interest already \"owned\" by other investors."),
 L("And members were asked for money for trips to Kenya, typically two thousand dollars a person, for church programs there. According to the indictment, Garcia would cancel or never book those trips.",
   doc("i_kenya", IK + "¶ 10(e)", "$2,000 per person · Kenya", S_IND),
   show="And people were asked for money for trips to Kenya, typically $2,000 per person, for church programs there. According to the indictment, Garcia would cancel or never book those trips."),
 L("Keep the word donation in mind. Because, according to the evidence, it is how the money moved.",
   dict(type="big", lines=["Keep one word", "in mind:|“donation.”"], src=S_IND),
   show="Keep the word \"donation\" in mind. Because, according to the evidence, it is how the money moved."),
 # III
 L("Chapter three. The paper trail.", dict(type="chapter", n="III", title="The Paper Trail")),
 L("The first example in the indictment is from August twenty twenty-one. A church property on South Collins Street in Arlington. Two investors sent a cashier's check for fifty thousand dollars, made out to M.G. Kingdom, Collins Project.",
   doc("i_check", IK + "¶ 14(a)", "A $50,000 cashier's check", S_IND),
   show="The first example in the indictment is from August 2021. A church property on South Collins Street in Arlington. Two investors sent a cashier's check for $50,000, made out to \"MG Kingdom (Collins Project).\""),
 L("Later, the indictment says, Garcia told them the project had made a profit of about fifty-five thousand dollars. And that he had used their money to invest in a new project. They never agreed to that.",
   doc("i_55k", IK + "¶ 14(a)(i)", "A $55,000 “profit”", S_IND),
   show="Later, the indictment says, Garcia told them the project had made a profit of about $55,000. And that he had used their money to invest in a new project. They never agreed to that."),
 L("Then came the big ones. October twenty twenty-three. An investor from Arizona, called Individual C, signs a partnership agreement for a church property on Hazel Street in Texarkana.",
   doc("i_hazel", IK + "¶ 14(b)", "Hazel Street, Texarkana", S_IND),
   show="Then came the big ones. October 2023. An investor from Arizona, called Individual C, signs a partnership agreement for a church property on Hazel Street in Texarkana."),
 L("He wires one hundred twenty-five thousand dollars on October eighteenth, and one hundred thousand more on October twenty-sixth. Two hundred twenty-five thousand in all.",
   show="He wires $125,000 on October 18, and $100,000 more on October 26. $225,000 in all."),
 L("Two weeks later, a second deal. A church property on East Queens Street in Lubbock. One hundred sixty-eight thousand dollars.",
   doc("i_lubbock", IK + "¶ 14(c)", "East Queens Street, Lubbock", S_IND),
   show="Two weeks later, a second deal. A church property on East Queens Street in Lubbock. $168,000."),
 L("In twenty twenty-four, according to the indictment, Garcia told him both projects were done. That he had secured title to the properties. That they had sold at a profit. And that he had used the profits to buy another church.",
   doc("i_hazellie", IK + "¶ 14(b)(i)", "“secured title ownership”", S_IND),
   show="In 2024, according to the indictment, Garcia told him both projects were done. That he had secured title to the properties. That they had sold at a profit. And that he had used the profits to buy another church."),
 L("The indictment says none of that was true. Garcia never got ownership of either property, and the money never went into improvements.",
   show="The indictment says none of that was true. Garcia did not obtain ownership of either property, and the money was not used for improvements."),
 L("And here is the chart prosecutors released with the verdict. Hazel Street. East Queens Street. And a third property, on Ryan Avenue in Fort Worth, with a second investor's two hundred ninety thousand dollars. All three: never purchased.",
   photo("f_never", XK + " · NAMES OF INVESTORS REDACTED BY SWORN", S_EX),
   show="And here is the chart prosecutors released with the verdict. Hazel Street. East Queens Street. And a third property, on Ryan Avenue in Fort Worth, with a second investor's $290,000. All three: \"NEVER PURCHASED.\""),
 L("So if the churches were never bought, where did the money go? The government followed it, dollar by dollar.",
   dict(type="stat", kicker=XK, value="$683,000", label="three church deals · proceeds from sale: $0", src=S_EX),
   show="So if the churches were never bought, where did the money go? The government followed it, dollar by dollar."),
 # IV
 L("Chapter four. Follow the money.", dict(type="chapter", n="IV", title="Follow the Money")),
 L("October eighteenth, twenty twenty-three. The first one hundred twenty-five thousand for Texarkana lands in a Bank of America account in the name of Gracia Church. Before it arrived, according to the government's chart, the balance was one thousand five hundred sixty-six dollars.",
   photo("f_tx1", XK + " · GRACIA CHURCH BOA #2450 · OCT 18–25, 2023", S_EX),
   show="October 18, 2023. The first $125,000 for Texarkana lands in a Bank of America account in the name of Gracia Church. Before it arrived, according to the government's chart, the balance was $1,566.03."),
 L("Then it goes out. Thirty-six thousand to payments to others, including to another investor. Twenty-two thousand to a title company, later reversed. Eighteen thousand in travel. Seventeen thousand in debt payments. Thirteen thousand to Richard Garcia's own account.",
   dict(type="bars", kicker=XK + " · OCT 18–25, 2023", title="Out of Gracia Church #2450", items=[
     {"label": "Payments to others, incl. another investor", "value": 36282, "display": "$36,282"},
     {"label": "Alamo Title Co. (later reverses)", "value": 22000, "display": "$22,000"},
     {"label": "Travel", "value": 18068, "display": "$18,068"},
     {"label": "Debt payments", "value": 17439, "display": "$17,439"},
     {"label": "Richard R. Garcia, BOA #4494", "value": 13000, "display": "$13,000"}], src=S_EX),
   show="Then it goes out. $36,282 to payments to others, including to another investor. $22,000 to a title company, later reversed. $18,068 in travel. $17,439 in debt payments. $13,000 to Richard Garcia's own account."),
 L("One week later, the account was down to about thirteen thousand nine hundred dollars. None of it, according to the chart, went to buy a church in Texarkana.",
   show="One week later, the account was down to $13,911.14. According to the government's chart, the property was never purchased."),
 L("Look at the other arrows on that chart, too. On the same days, the church account also took in income from others, including tithes and offerings. Investor money and Sunday offerings went into one account, and out of it.",
   photo("f_tx1", XK + " · GRACIA CHURCH BOA #2450 · OCT 18–25, 2023", S_EX),
   show="Look at the other arrows on that chart, too. On the same days, the church account also took in \"income from others, including tithes/offerings.\" Investor money and offerings went into one account, and out of it."),
 L("Now follow the thirteen thousand into his personal account. That account had started the week overdrawn, at minus two thousand three hundred thirty-two dollars.",
   photo("f_rg1", XK + " · RICHARD R GARCIA BOA #4494 · OCT 18–27, 2023", S_EX),
   show="Now follow the $13,000 into his personal account. That account had started the week overdrawn, at minus $2,332.49."),
 L("Out of it: five thousand three hundred in international transactions, in Panama. Utilities. And one thousand six hundred forty-five dollars to Mercedes-Benz Financial Services.",
   show="Out of it: $5,326.29 in international transactions, in Panama. Utilities. And $1,645.23 to Mercedes-Benz Financial Services."),
 L("Two weeks later, the second Texarkana wire, one hundred thousand dollars. Another six thousand goes from the church account to Garcia. Out of his account, according to the chart: debt payments. One thousand two hundred dollars more to Mercedes-Benz. Two hundred eighty-nine dollars at the Texas Rangers, baseball and concessions. And smaller charges, labeled Jackpocket, Apple and Audible.",
   photo("f_rg2", XK + " · RICHARD R GARCIA BOA #4494 · OCT 30–31, 2023", S_EX),
   show="Two weeks later, the second Texarkana wire, $100,000. Another $6,000 goes from the church account to Garcia. Out of his account, according to the chart: debt payments. $1,204.18 more to Mercedes-Benz. $289.22 at the Texas Rangers, \"baseball & concessions.\" And smaller charges, labeled Jackpocket, Apple and Audible."),
 L("Then Lubbock. November third, one hundred sixty-eight thousand dollars into the same church account. One week later, the balance is back to about six thousand.",
   photo("f_lub", XK + " · GRACIA CHURCH BOA #2450 · NOV 3–10, 2023", S_EX),
   show="Then Lubbock. November 3, $168,000 into the same church account. One week later, the balance is back to $6,158.24."),
 L("Remember the payments to other investors. The indictment has a name for that: lulling payments. Money paid to victims who asked for their profits, designed to keep them calm.",
   doc("i_lulling", IK + "¶ 19", "“Lulling Payments”", S_IND),
   show="Remember the payments to other investors. The indictment has a name for that: \"lulling payments.\" Money paid to victims who asked for their profits, designed to address their requests."),
 L("And when victims questioned missing profits, prosecutors say, Garcia often told them the earnings had been reinvested in other projects.",
   doc("p_reinvest", PK, "“reinvested”", S_PR),
   show="And when victims questioned missing profits, prosecutors say, Garcia often falsely claimed their earnings had been reinvested into other projects."),
 # V
 L("Chapter five. The donations.", dict(type="chapter", n="V", title="The Donations")),
 L("So far: the deals, the money trail, the Mercedes payments. But the strangest part of this case is a single word on the bank records. And then a two point four million dollar contract with someone else's name on it.",
   dict(type="big", lines=["A $2.4 million contract.", "Someone else's|name on it."], src=S_IND + " ¶ 17"),
   show="So far: the deals, the money trail, the Mercedes payments. But the strangest part of this case is a single word on the bank records. And then a $2.4 million contract with someone else's name on it, according to the indictment."),
 L("Here is the word from chapter two. According to the evidence, Garcia told victims to send their money to accounts in the name of Gracia Church, and to call the payments donations.",
   doc("p_accounts", PK, "Call it a “donation”", S_PR),
   show="Here is the word from chapter two. According to the evidence, Garcia instructed victims to transfer money to church-related accounts and to characterize the payments as \"donations\" to Gracia Church."),
 L("Even though, the U.S. Attorney's Office says, the money was meant for investments.",
   show="Even though, the U.S. Attorney's Office says, the funds were intended for investment opportunities."),
 L("The investor from Arizona, Individual C, is one example. In twenty twenty-four, the indictment says, Garcia directed him to describe his partnership money as donations. Afterward, he received a donation letter from Ministerio Gracia.",
   doc("i_donletter", IK + "¶ 15(a)", "A “Donation Letter”", S_IND),
   show="The investor from Arizona, Individual C, is one example. In 2024, the indictment says, Garcia directed him to describe his partnership money as donations. Afterward, he received a Donation Letter from Ministerio Gracia."),
 L("An investment has a contract, and an investor expects a return. A donation is a gift. The indictment says labeling it that way disguised business money as charity.",
   dict(type="big", lines=["Investment: a return.", "Donation:|a gift."], src=S_IND + " ¶ 15"),
   show="An investment has a contract, and an investor expects a return. A donation is a gift. The indictment says labeling it that way disguised funds for a business venture as charitable donations."),
 L("And the requests did not stop. In May twenty twenty-five, the indictment says, Garcia asked another person, Individual E, for money, and showed him a commercial contract.",
   doc("i_may2025", IK + "¶ 17", "May 2025", S_IND),
   show="And the requests did not stop. In May 2025, the indictment says, Garcia asked another person, Individual E, for money, and showed him a Commercial Contract."),
 L("It showed Ministerio Gracia selling a church property at seventeen hundred New York Avenue, Arlington, for two point four million dollars. The indictment says the man listed as the buyer never agreed to buy it, and never consented to his name and digital signature being put on the contract.",
   doc("i_24m", IK + "¶ 17", "$2,400,000", S_IND),
   show="It showed Ministerio Gracia selling the property at 1700 New York Ave, Arlington, for $2,400,000. The indictment says the man listed as the buyer did not agree to buy it, and did not consent to his name and digital signature being put on the contract."),
 L("That allegation was also charged as aggravated identity theft. The U.S. Attorney's announcement of the verdict lists four counts of conviction, and does not mention that fifth count.",
   doc("i_caption", "SUPERSEDING INDICTMENT · FILED OCT 7, 2026", "Five counts charged", S_IND),
   show="That allegation was also charged as aggravated identity theft. The U.S. Attorney's announcement of the verdict lists four counts of conviction, and does not mention that fifth count."),
 # VI
 L("Chapter six. The verdict.", dict(type="chapter", n="VI", title="The Verdict")),
 L("The trial lasted four days, before U.S. District Judge Mark T. Pittman, in Fort Worth. The jury found Garcia guilty on November nineteenth.",
   doc("p_verdict", PK, "Guilty on Nov. 19", S_PR),
   show="The trial lasted four days, before U.S. District Judge Mark T. Pittman, in Fort Worth. The jury found Garcia guilty on November 19."),
 L("So which deals did the jury convict on? The superseding indictment lays out three wire fraud counts, each tied to an email Garcia sent or caused to be sent.",
   dict(type="list", kicker="SUPERSEDING INDICTMENT · COUNTS 2–4 · WIRE FRAUD", items=[["Count 2", "Email to Individual C in Arizona · Lubbock deal · $168,000"], ["Count 3", "Email to Individual C in Arizona · Texarkana deal · $225,000"], ["Count 4", "Email to Individual H, Florida & Colombia · Ryan Ave, Fort Worth · $210,000"]], src=S_IND + " ¶ 23"),
   show="So which deals did the jury convict on? The superseding indictment lays out three wire fraud counts, each tied to an email Garcia sent or caused to be sent."),
 L("Counts two and three are the Lubbock and Texarkana deals, emails dated November thirtieth, twenty twenty-three, to the investor in Arizona. Count four is an email in January twenty twenty-three to an investor in Florida and Colombia, about the church property on Ryan Avenue in Fort Worth. The indictment puts that one at two hundred ten thousand dollars.",
   show="Counts Two and Three are the Lubbock and Texarkana deals, emails dated November 30, 2023, to the investor in Arizona. Count Four is an email dated January 17, 2023, to an investor in Florida and Colombia, about the church property on Ryan Ave in Fort Worth. The indictment puts that one at $210,000."),
 L("Count one ties it all together: a conspiracy to commit wire fraud, with a co-conspirator the indictment does not name. The jury said guilty on all four.",
   show="Count One ties it all together: a conspiracy to commit wire fraud, with a co-conspirator the indictment does not name. The jury found him guilty on all four."),
 L("And according to the U.S. Attorney, it did not take long. His words: a very quick decision by the jury.",
   doc("p_quick", PK, "“a very quick decision”", S_PR),
   show="And according to the U.S. Attorney, it did not take long. His words: \"a very quick decision by the jury.\""),
 L("Prosecutors also showed the jury how Garcia lived. Between about twenty twenty-three and October twenty twenty-five, he directed more than two hundred thousand dollars a year to his personal bank accounts.",
   doc("p_personal", PK, "$200,000+ a year", S_PR),
   show="Prosecutors also showed the jury how Garcia lived. Between approximately 2023 and October 2025, he directed more than $200,000 annually to his personal bank accounts."),
 L("He drove a twenty twenty-three Mercedes electric S.U.V. And he lived in a Mansfield residence that sold for more than one point six million dollars.",
   dict(type="list", kicker="PER TRIAL EVIDENCE · U.S. ATTORNEY", items=[["$200K+", "a year to personal accounts (≈2023 – Oct 2025)"], ["2023", "Mercedes electric SUV"], ["$1.6M+", "Mansfield residence, sale price"]], src=S_PR),
   show="He drove a 2023 Mercedes electric SUV. And he lived in a Mansfield residence that sold for more than $1.6 million."),
 L("U.S. Attorney Ryan Raybould, after the verdict.",
   dict(type="quote", q="This defendant didn't just take money from his victims. He abused personal relationships, exploited the trust people placed in him as a pastor, and invoked his purported Christian faith to execute his large-scale fraud scheme.", case="U.S. Attorney Ryan Raybould · Nov 20, 2026", doc="Press release, U.S. Attorney's Office, N.D. Tex.", cite=S_PR),
   show="U.S. Attorney Ryan Raybould, after the verdict: \"This defendant didn't just take money from his victims. He abused personal relationships, exploited the trust people placed in him as a pastor, and invoked his purported Christian faith to execute his large-scale fraud scheme.\""),
 L("And the F.B.I. in Dallas said the scheme betrayed the trust of his congregants and others.",
   dict(type="quote", q="The defendant's scheme betrayed the trust of his congregants and others and used deception to lure them into making investments in his fraudulent projects.", case="FBI Dallas Special Agent in Charge R. Joseph Rothrock", doc="Press release, U.S. Attorney's Office, N.D. Tex., Nov 20, 2026", cite=S_PR),
   show="And FBI Dallas Special Agent in Charge R. Joseph Rothrock: \"The defendant's scheme betrayed the trust of his congregants and others and used deception to lure them into making investments in his fraudulent projects.\""),
 L("The final count, according to court documents and trial evidence: more than seventy victims, and more than six million dollars lost.",
   doc("p_6m", PK, "More than $6 million", S_PR),
   show="The final count, according to court documents and trial evidence: more than 70 victims, and more than $6 million lost."),
 L("Garcia faces up to twenty years in federal prison on each count. Sentencing is set for March fourth, twenty twenty-seven.",
   doc("p_sent", PK, "Sentencing: March 4, 2027", S_PR),
   show="Garcia faces up to 20 years in federal prison on each count. Sentencing is set for March 4, 2027."),
 L("And the case may not be finished. The F.B.I. is still asking people who think they were victims to come forward, through an online questionnaire, in English and in Spanish.",
   doc("p_fbi", PK, "The FBI is still looking", S_PR),
   show="And the case may not be finished. The FBI is still asking people who think they were victims to come forward, through an online questionnaire, in English and in Spanish."),
 L("Three churches that were never bought. Donations that were really investments. And, according to the government's own charts, a pastor's personal account that paid Mercedes-Benz.",
   dict(type="timeline", kicker="UNITED STATES v. GARCIA · N.D. TEX.", events=[
     {"date": "Aug 2021", "text": "Scheme begins, per indictment"},
     {"date": "Oct–Nov 2023", "text": "$393,000 for Texarkana + Lubbock"},
     {"date": "May 2025", "text": "$2.4M \"Commercial Contract\""},
     {"date": "Oct 7, 2026", "text": "Superseding indictment"},
     {"date": "Nov 19, 2026", "text": "GUILTY on 4 counts"},
     {"date": "Mar 4, 2027", "text": "Sentencing"}], src=S_IND + "; " + S_PR),
   show="Three churches that were never bought. Donations that were really investments. And, according to the government's own charts, a pastor's personal account that paid Mercedes-Benz."),
 L("The judge will decide his sentence in March. What do you think a pastor who did this should get? Tell us in the comments.",
   dict(type="end"),
   show="The judge will decide his sentence in March. What do you think a pastor who did this should get? Tell us in the comments."),
]

# ---- fact-check fixes (factcheck.md, 35 FIX items) ----
def F(i, say=None, show=None, **sc):
    if say: lines[i]["say"] = say
    if show: lines[i]["show"] = show
    if sc: lines[i]["scene"] = dict(lines[i]["scene"], **sc)
def R(i, a, b):
    for k in ("say", "show"):
        if k in lines[i]: lines[i][k] = lines[i][k].replace(a, b)
F(1, "According to the government's chart, investors put in a combined six hundred eighty-three thousand dollars to fix them up and sell them at a profit. Prosecutors call it church flipping.",
  "According to the government's chart, investors put in a combined $683,000 to fix them up and sell them at a profit. Prosecutors call it \"church flipping.\"")
R(7, "during the entire scheme", "during the scheme")
R(10, "Gracia Church Atlanta and Gracia Church.", "Gracia Church Atlanta and Gracia Church, according to the indictment.")
F(13, "That is what made the pitch work. The churches existed. Some renovations happened. Some properties did sell at a profit. The question was what happened to the investors' money.",
  "That is what made the pitch work. The churches existed. Some renovations happened. Some properties did sell at a profit. The question was what happened to the investors' money.")
F(15, "From at least August twenty twenty-one through April twenty twenty-five, according to the trial evidence, Garcia and others solicited money for two kinds of deals.",
  "From at least August 2021 through April 2025, according to the trial evidence, Garcia and others solicited money for two kinds of deals.")
F(18, "The grand jury charged that he did not intend to host the concerts as scheduled, or to share the profits. Instead, it says, he intended to use the money for operating costs, unrelated business, and personal expenses.",
  "The grand jury charged that he did not intend to host the concerts as scheduled, or to share the profits. Instead, it says, he intended to use the money for operating costs, unrelated business, and personal expenses.")
F(19, "There was more. The indictment says some investors were offered an interest already owned by other investors.")
R(20, "And members were asked", "And people were asked")
F(25, "Then came the big ones. According to the indictment, in October twenty twenty-three, an investor from Arizona, called Individual C, signed a partnership agreement for a church property on Hazel Street in Texarkana.",
  "Then came the big ones. According to the indictment, in October 2023, an investor from Arizona, called Individual C, signed a partnership agreement for a church property on Hazel Street in Texarkana.")
F(27, "About a week after that second wire, on November third, a second deal, the indictment says. A church property on East Queens Street in Lubbock. One hundred sixty-eight thousand dollars.",
  "About a week after that second wire, on November 3, a second deal, the indictment says. A church property on East Queens Street in Lubbock. $168,000.")
R(30, "the chart prosecutors released with the verdict", "the chart prosecutors released when they announced the verdict")
F(31, "So if the churches were never bought, where did the money go? The government's charts follow it, account by account.",
  "So if the churches were never bought, where did the money go? The government's charts follow it, account by account.",
  label="the chart's three investments, added together · proceeds from sale: $0")
F(34, "Then, the chart shows, money goes out of that account. About thirty-six thousand dollars in payments to others, including to another investor. Twenty-two thousand to a title company, later reversed. About eighteen thousand in travel. About seventeen thousand in debt payments. Thirteen thousand to Richard Garcia's own account.",
  "Then, the chart shows, money goes out of that account. About $36,000 in payments to others, including to another investor. $22,000 to a title company, later reversed. About $18,000 in travel. About $17,000 in debt payments. $13,000 to Richard Garcia's own account.")
F(35, "One week later, the account was down to about thirteen thousand nine hundred dollars. According to the government's chart, the property was never purchased.",
  "One week later, the account was down to about $13,900. According to the government's chart, the property was never purchased.")
R(36, "Sunday offerings", "offerings"); R(36, "On the same days", "That same week")
F(38, "Out of it: five thousand three hundred twenty-six dollars in international transactions, in Panama. Utilities. And one thousand six hundred forty-five dollars to Mercedes-Benz Financial Services.",
  "Out of it: $5,326 in international transactions, in Panama. Utilities. And $1,645 to Mercedes-Benz Financial Services.")
F(39, "On October twenty-sixth, the second Texarkana wire, one hundred thousand dollars, lands in the church account. A few days later, another six thousand goes from the church account to Garcia. Out of his account, according to the chart: debt payments. One thousand two hundred four dollars more to Mercedes-Benz. Two hundred eighty-nine dollars at the Texas Rangers, baseball and concessions. And smaller charges, labeled Jackpocket, Apple and Audible.",
  "On October 26, the second Texarkana wire, $100,000, lands in the church account. A few days later, another $6,000 goes from the church account to Garcia. Out of his account, according to the chart: debt payments. $1,204 more to Mercedes-Benz. $289 at the Texas Rangers, \"baseball & concessions.\" And smaller charges, labeled Jackpocket, Apple and Audible.")
F(40, "Then Lubbock. November third, one hundred sixty-eight thousand dollars into the same church account. One week later, the balance is down to about six thousand one hundred.",
  "Then Lubbock. November 3, $168,000 into the same church account. One week later, the balance is down to $6,158.24.")
F(41, "The indictment also describes what it calls lulling payments: payments to victims, designed to address their requests to be paid their profits.",
  "The indictment also describes what it calls \"lulling payments\": payments to victims, designed to address their requests to be paid their profits.")
F(44, "So far: the deals, the money trail, the Mercedes payments. But the strangest part of this case is a single word on the bank records. And then, according to the indictment, a two point four million dollar contract with someone else's name on it.",
  "So far: the deals, the money trail, the Mercedes payments. But the strangest part of this case is a single word on the bank records. And then, according to the indictment, a $2.4 million contract with someone else's name on it.",
  lines=["A $2.4 million contract.", "Someone else's name|on it, per the indictment."])
F(45, "Here is the word from chapter two. According to the evidence, Garcia told victims to send their money to church-related accounts, and to call the payments donations to Gracia Church.")
F(50, "It showed Ministerio Gracia selling the property at seventeen hundred New York Avenue, Arlington, for two point four million dollars, to a buyer: Individual E himself. The indictment says he did not agree to buy it, did not know about the contract, and did not consent to his name and digital signature being put on it.",
  "It showed Ministerio Gracia selling the property at 1700 New York Ave, Arlington, for $2,400,000, to a buyer: Individual E himself. The indictment says he did not agree to buy it, did not know about the contract, and did not consent to his name and digital signature being put on it.")
F(51, "The indictment also charged a fifth count, aggravated identity theft, over the use of Individual E's name and address on a Texas business filing in December twenty twenty-three. The U.S. Attorney's announcement of the verdict lists four counts of conviction, and does not mention that fifth count.",
  "The indictment also charged a fifth count, aggravated identity theft, over the use of Individual E's name and address on a Texas business filing in December 2023. The U.S. Attorney's announcement of the verdict lists four counts of conviction, and does not mention that fifth count.",
  title="The superseding indictment")
F(65, "Three churches that, according to the government's chart, were never bought. Donations that were really investments. And, according to the government's own charts, a pastor's personal account that paid Mercedes-Benz.",
  "Three churches that, according to the government's chart, were never bought. Donations that were really investments. And, according to the government's own charts, a pastor's personal account that paid Mercedes-Benz.")
F(66, "The judge will decide his sentence in March. What sentence do you think he should get? Tell us in the comments.",
  "The judge will decide his sentence in March. What sentence do you think he should get? Tell us in the comments.")
json.dump({"label": "SWORN · CASE 023", "lines": lines}, open(os.path.join(HERE, "episode.json"), "w"), indent=1, ensure_ascii=False)
print(len(lines), "lines,", sum(len(l["say"].split()) for l in lines), "words")
