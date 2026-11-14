import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
def hl(name, i=0):
    a, b = HL[name][i]
    return [0.0, a, 1.0, round(b - a, 4)]
CASE = "UNITED STATES v. LINK"
SRC_V = "U.S. Attorney's Office, N.D. Tex., press release (Nov 11, 2026)"
SRC_I = "U.S. Attorney's Office, N.D. Tex., press release (Feb 12, 2026)"
SRC_SSI = "Second Superseding Indictment, U.S. v. Link et al., No. 4:26-CR-051-P, Dkt. 168 (N.D. Tex. Sep 11, 2026) — charges"
SRC_IND2 = "Indictment, U.S. v. Jason Allen Link & Joshua Robert Link, No. 4:26-CR-060-P, Dkt. 1 (N.D. Tex. Mar 11, 2026)"
SRC_FBI = "FBI wanted poster, Joshua Robert Link (2026), via USAO N.D. Tex."
SRC_SEC = "SEC v. Agridime LLC et al., No. 4:23-cv-01224-P, Complaint (N.D. Tex. Dec 11, 2023) — allegations"
SRC_CFTC = "CFTC v. Agridime LLC et al., No. 4:24-cv-0424-P, Consent Order, Dkt. 44 (N.D. Tex. Jun 10, 2025)"
SRC_WOOD = "Factual Resume, U.S. v. Jed Hansel Wood, No. 4:26-CR-051-P, Dkt. 63 (Mar 25, 2026)"
SRC_TIA = "Factual Resume, U.S. v. Tia Makenzie Link, No. 4:26-CR-051-P, Dkt. 116 (Jun 17, 2026)"
SRC_BANG = "Factual Resume, U.S. v. Taylor Orris Bang, No. 4:26-CR-051-P (2026)"
SRC_EX = "Gov't trial exhibit, as published by the U.S. Attorney's Office, N.D. Tex. (Nov 11, 2026)"
SRC_DTN = "DTN/Progressive Farmer, citing FBI Dallas (Mar 16, 2026); Cowboy State Daily (Mar 16, 2026)"
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
def doc(img, kicker, title, src, i=0, pan=None):
    return dict(type="doc", img=f"img/{img}.jpg", pan=pan or [0.0, 0.1], hl=hl(img, i), kicker=kicker, title=title, src=src)
def photo(img, caption, src, fit="contain"):
    return dict(type="photo", img=f"img/{img}.jpg", caption=caption, src=src, fit=fit)
SSI = "SECOND SUPERSEDING INDICTMENT"
SEC = "SEC v. AGRIDIME · COMPLAINT · ALLEGATIONS"
lines = [
 # COLD OPEN
 L("In February, the FBI put a thirty-two-year-old cattle executive on its wanted list. A month later, he was taken into custody at Los Angeles International Airport.",
   doc("poster", "WANTED BY THE FBI · 2026", "Joshua Robert Link", SRC_FBI, 0, pan=[0.0, 0.05]),
   show="In February, the FBI put a 32-year-old cattle executive on its wanted list. A month later, he was taken into custody at Los Angeles International Airport."),
 L("On Tuesday, November tenth, a federal jury in Fort Worth, Texas, convicted him, and his brother.",
   dict(type="verdict", kicker="FORT WORTH · NOVEMBER 10, 2026", stamp="GUILTY", big="Joshua & Jason Link", sub="wire fraud conspiracy · wire fraud · money laundering"),
   show="On Tuesday, November 10, a federal jury in Fort Worth, Texas, convicted him, and his brother."),
 L("Prosecutors say their company sold cattle to more than twenty-two hundred Americans, and collected over two hundred forty million dollars. It sold about sixty thousand more head of cattle than it controlled.",
   dict(type="stat", kicker="AGRIDIME · 2021–2023", value="$240M", label="collected from more than 2,200 victims", src=SRC_V),
   show="Prosecutors say their company sold cattle to more than 2,200 Americans, and collected over $240 million. It sold about 60,000 more head of cattle than it controlled."),
 L("The U.S. Attorney called it a high-tech Ponzi scheme. This is the paper trail: the offer, the missing herd, the ranch, the flight, and the verdict.",
   dict(type="title", kicker="SWORN · CASE 014 · BREAKING", title="The Missing|Herd", sub="United States v. Joshua & Jason Link · N.D. Tex. · 2026"),
   show="The U.S. Attorney called it a \"high-tech Ponzi scheme.\" This is the paper trail: the offer, the missing herd, the ranch, the flight, and the verdict."),
 # I
 L("Chapter one. Two thousand dollars a head.", dict(type="chapter", n="I", title="$2,000 a Head"), show="Chapter one. $2,000 a head."),
 L("Agridime was registered in Texas in April twenty seventeen and headquartered in Fort Worth. It sold cattle, processed meat, and sold that meat to stores and restaurants.",
   doc("ssi_1", SSI + " · PAGE 1", "United States v. Joshua Robert Link et al.", SRC_SSI, 1),
   show="Agridime was registered in Texas in April 2017 and headquartered in Fort Worth. It sold cattle, processed meat, and sold that meat to stores and restaurants."),
 L("Joshua Link co-founded it with an older partner, Jed Wood. According to the SEC, each owned forty-five and a half percent. Link was the Executive Director, a role the SEC said he described as equivalent to CEO. In twenty twenty-three, he was thirty years old.",
   doc("sec_3", SEC, "“Joshua Link, age 30”", SRC_SEC, 0),
   show="Joshua Link co-founded it with an older partner, Jed Wood. According to the SEC, each owned 45.5%. Link was the Executive Director, a role the SEC said he described as \"equivalent to CEO.\" In 2023, he was 30 years old."),
 L("From at least January twenty twenty-one, Agridime sold the public something else. Not beef. Cattle contracts.",
   dict(type="big", kicker="AGRIDIME · FROM 2021", lines=["Not beef.", "Cattle|contracts."], src=SRC_SSI)),
 L("Here is how the company's website explained it. The customer purchases cattle from us for two thousand dollars per head. That two thousand dollars is used to purchase one steer or heifer, feed that animal to finish, fully process the beef into retail packaging, and then ultimately sell the beef.",
   doc("ssi_13", SSI + " · PAGE 13", "The website pitch", SRC_SSI, 0),
   show="Here is how the company's website explained it: \"The customer purchases cattle from us for $2,000 per head. That $2,000 is used to purchase one steer or heifer, feed that animal to finish, fully process the beef into retail packaging and then ultimately sell the beef.\""),
 L("You could even buy online. One live steer or heifer, two thousand dollars, add to cart.",
   doc("ssi_13", SSI + " · PAGE 13", "“1 LIVE STEER OR HEIFER · $2,000.00”", SRC_SSI, 0, pan=[0.45, 0.6]),
   show="You could even buy online. \"1 LIVE STEER OR HEIFER. $2,000.00.\" Add to cart."),
 L("And the return was written into the promise. All cattle purchased during the second quarter of twenty twenty-three, the site said, will be guaranteed fifteen to twenty percent yearly profits.",
   doc("ssi_4", SSI + " · PAGE 4", "“guaranteed 15-20% yearly profits”", SRC_SSI, 0),
   show="And the return was written into the promise. \"All cattle purchased during the Q2 of 2023,\" the site said, \"will be guaranteed 15-20% yearly profits.\""),
 L("The SEC later quoted one of the company's own ads. Have you ever wanted to make money raising cattle without having to do all the work? We know it sounds too good to be true.",
   doc("sec_7", SEC, "“We know it sounds too good to be true”", SRC_SEC, 0),
   show="The SEC later quoted one of the company's own ads: \"Have you ever wanted to make money raising cattle without having to do all the work? We know it sounds too good to be true.\""),
 L("For bigger buyers, according to the SEC, the guarantee went as high as thirty-two percent. The FBI put the range at fifteen to thirty-two percent.",
   dict(type="stat", kicker="PROMISED RETURNS", value="15–32%", label="a year, \"guaranteed\" in the contracts", src=SRC_FBI + " · " + SRC_SEC),
   show="For bigger buyers, according to the SEC, the guarantee went as high as 32%. The FBI put the range at 15% to 32%."),
 L("According to the SEC, buyers never took delivery of an animal. Their money was supposed to become their cows. Prosecutors say it didn't.",
   dict(type="big", lines=["Their money was", "supposed to|become their cows."], src=SRC_SEC)),
 # II
 L("Chapter two. The missing herd.", dict(type="chapter", n="II", title="The Missing Herd")),
 L("Here is what the grand jury charged. Agridime promised each buyer that their money would buy specific individual cattle, raise them, process them, and sell the meat. In reality, the indictment says, the money paid Agridime's operating expenses, its loans, and the people who had bought in earlier.",
   doc("ssi_6", SSI + " · PAGE 6", "The object of the conspiracy", SRC_SSI, 0),
   show="Here is what the grand jury charged. Agridime promised each buyer that their money would buy specific individual cattle, raise them, process them, and sell the meat. In reality, the indictment says, the money paid Agridime's operating expenses, its loans, and the people who had bought in earlier."),
 L("At trial, prosecutors put the gap on a single chart. By December eleventh, twenty twenty-three, Agridime had sold cattle contracts for about one hundred fifteen thousand, two hundred fifty-five head.",
   dict(type="bars", kicker="GOV'T TRIAL EXHIBIT · JAN 2021 – DEC 11, 2023", title="Cattle sold vs. cattle bought", sync=True,
        items=[{"label": "CONTRACTS SOLD (HEAD)", "value": 115255, "display": "115,255"}, {"label": "NET CATTLE PURCHASED", "value": 51704, "display": "51,704"}], src=SRC_EX),
   show="At trial, prosecutors put the gap on a single chart. By December 11, 2023, Agridime had sold cattle contracts for about 115,255 head."),
 L("The cattle it had actually bought, net: about fifty-one thousand, seven hundred four."),
 L("That is the gap the U.S. Attorney's Office described: about sixty thousand more head of cattle sold to the public than Agridime controlled.",
   photo("rel_chart", "GOV'T EXHIBIT KC15 · AS PUBLISHED BY THE U.S. ATTORNEY", SRC_EX),
   show="That is the gap the U.S. Attorney's Office described: about 60,000 more head of cattle sold to the public than Agridime controlled."),
 L("So where did the new money go? The SEC traced at least fifty-eight million dollars, between December twenty twenty-two and September twenty twenty-three, that was used to pay earlier investors. In short, the SEC wrote, Agridime is operating a Ponzi scheme.",
   doc("sec_9", SEC + " · PAGE 9", "“In short, Agridime is operating a Ponzi scheme.”", SRC_SEC, 0),
   show="So where did the new money go? The SEC traced at least $58 million, between December 2022 and September 2023, that was used to pay earlier investors. \"In short,\" the SEC wrote, \"Agridime is operating a Ponzi scheme.\""),
 L("By September twenty twenty-three, the SEC said, Agridime owed investors more than one hundred twenty-three million dollars in principal, plus about twenty-four million in guaranteed profits. Its cash: less than one and a half million.",
   doc("sec_9", SEC + " · PAGE 9", "$123 million owed · under $1.5 million cash", SRC_SEC, 1),
   show="By September 2023, the SEC said, Agridime owed investors more than $123 million in principal, plus about $24 million in guaranteed \"profits.\" Its cash: less than $1.5 million."),
 L("And someone was getting paid. A government exhibit shows salaries and commissions from twenty twenty-one through twenty twenty-three. Josh and Tia Link, combined because of a joint bank account: two point seven three million dollars. Jed Wood: two point four one million.",
   photo("rel_salary", "GOV'T EXHIBIT · SALARY & COMMISSION TABLE", SRC_EX),
   show="And someone was getting paid. A government exhibit shows salaries and commissions from 2021 through 2023. Josh and Tia Link, combined because of a joint bank account: $2.73 million. Jed Wood: $2.41 million."),
 L("Brokers took a cut too. The indictment says sales agents were paid up to ten percent of every contract, and one broker in North Dakota, Taylor Bang, collected nearly seven million dollars in commissions.",
   doc("ssi_20", SSI + " · PAGE 20", "$6,987,000 of commission payments", SRC_SSI, 1),
   show="Brokers took a cut too. The indictment says sales agents were paid up to 10% of every contract, and one broker in North Dakota, Taylor Bang, collected nearly $7 million in commissions."),
 L("Now hold that number. Fifteen to twenty percent guaranteed, paid out of a herd that, by the government's chart, was less than half the size of what had been sold. The next question is how they kept buyers from noticing.",
   dict(type="big", lines=["Less than half", "the herd|that was sold."], src=SRC_EX)),
 # III
 L("Chapter three. The cover.", dict(type="chapter", n="III", title="The Cover")),
 L("Some buyers asked for proof, like their cattle's ear-tag numbers. According to the indictment, in April twenty twenty-three Joshua Link gave the same tag information to two different buyers, purporting to show that specific cattle had been bought for each of them.",
   doc("ssi_20", SSI + " · PAGE 20", "“duplicative Electronic Identification (“EID”) tag information”", SRC_SSI, 2),
   show="Some buyers asked for proof, like their cattle's ear-tag numbers. According to the indictment, in April 2023 Joshua Link gave the same tag information to two different buyers, \"purporting to show specific heads of cattle had been purchased for each victim.\""),
 L("Then the regulators arrived. In April twenty twenty-three, Arizona ordered Agridime to stop selling. In May, North Dakota did the same.",
   dict(type="timeline", kicker="STATE ORDERS · 2023", at=1, sync=True, events=[{"date": "APR 18, 2023", "text": "Arizona: cease and desist"}, {"date": "MAY 24, 2023", "text": "North Dakota: cease and desist"}, {"date": "DEC 11, 2023", "text": "SEC sues; receiver appointed"}], src=SRC_SSI + " · " + SRC_SEC),
   show="Then the regulators arrived. In April 2023, Arizona ordered Agridime to stop selling. In May, North Dakota did the same."),
 L("The sales kept going. Agridime's marketing director, Tia Link, has admitted in her plea papers that in August twenty twenty-three she sent a buyer the current contract and wrote: Agridime is regulated by the USDA and just went through and passed our twenty twenty-three audit with the USDA.",
   doc("tia_3", "FACTUAL RESUME · TIA LINK · STIPULATED", "“passed our 2023 audit with the USDA”", SRC_TIA, 0),
   show="The sales kept going. Agridime's marketing director, Tia Link, has admitted in her plea papers that in August 2023 she sent a buyer the current contract and wrote: \"Agridime is regulated by the USDA and just went through and passed our 2023 audit with the USDA.\""),
 L("Another buyer asked whether it was guaranteed that one year from now you will pay me fifty-five hundred. Her answer, as stipulated: Yes, that is correct.",
   doc("tia_3", "FACTUAL RESUME · TIA LINK · STIPULATED", "“Yes, that is correct”", SRC_TIA, 1),
   show="Another buyer asked whether it was \"guaranteed that one year from now you will pay me 5500.\" Her answer, as stipulated: \"Yes, that is correct.\""),
 L("In October twenty twenty-three, an Arizona buyer agreed to pay two hundred forty thousand dollars for eighty specific cattle, with a promised thirty percent profit within nine months. Broker Taylor Bang has admitted the deal was made despite the Arizona order.",
   doc("bang_4", "FACTUAL RESUME · TAYLOR BANG · STIPULATED", "$240,000 · 80 cattle · 30% in 9 months", SRC_BANG, 0),
   show="In October 2023, an Arizona buyer agreed to pay $240,000 for 80 specific cattle, with a promised 30% profit within nine months. Broker Taylor Bang has admitted the deal was made despite the Arizona order."),
 L("The indictment says the contract was then written in Bang's name, and the money sent to his account instead of Agridime's, to hide the Arizona buyer.",
   dict(type="big", kicker="SECOND SUPERSEDING INDICTMENT · CHARGES", lines=["The buyer's name", "left off|the contract."], src=SRC_SSI)),
 L("And in November, Agridime's financial controller pitched a buyer by phone. According to the indictment, she offered him twenty-four point four four percent, and explained where the profits came from.",
   doc("ssi_10", SSI + " · PAGE 10", "“I could offer you [profits of] 24.44%”", SRC_SSI, 0),
   show="And in November, Agridime's financial controller pitched a buyer by phone. According to the indictment, she offered him 24.44%, and explained where the profits came from."),
 L("Where we end up making the money, she said, is when we harvest, process and get the meat out. And that's why we're able to offer that percentage. The indictment calls that false. The controller, Royana Thomas, pleaded guilty on November fourth.",
   dict(type="quote", q="where we end up making the money is when we harvest, process and get the meat out", case=CASE, doc="ROYANA THOMAS · PHONE CALL · NOV 28, 2023", cite="As quoted in " + SRC_SSI, size=46),
   show="\"Where we end up making the money,\" she said, \"is when we harvest, process and get the meat out … and that's why we're able to offer that percentage.\" The indictment calls that false. The controller, Royana Thomas, pleaded guilty on November 4."),
 # IV
 L("Chapter four. The ranch in Kansas.", dict(type="chapter", n="IV", title="The Ranch")),
 L("There was a second scheme. And this one, the jury found, the Link brothers ran on their own company.",
   dict(type="big", lines=["A second scheme.", "Against|Agridime itself."], src=SRC_V)),
 L("Jason Link, Joshua's brother, owned Shady Brook Ranch in Hope, Kansas, and worked for Agridime as a livestock broker and Meat Chain Director. Some Agridime cattle were kept on his ranch.",
   doc("ssi_1", SSI + " · PAGE 1", "Jason Allen Link (06)", SRC_SSI, 0),
   show="Jason Link, Joshua's brother, owned Shady Brook Ranch in Hope, Kansas, and worked for Agridime as a livestock broker and Meat Chain Director. Some Agridime cattle were kept on his ranch."),
 L("From November twenty twenty-one, Joshua sent bills to Agridime's accountants: payments due to Shady Brook for feed and yardage. The trial evidence showed a separate company was already feeding those cattle, and being paid for it. Agridime paid twice.",
   photo("rel_feed", "GOV'T EXHIBIT · PAYMENTS TO SHADY BROOK", SRC_EX),
   show="From November 2021, Joshua sent bills to Agridime's accountants: payments due to Shady Brook for \"feed and yardage.\" The trial evidence showed a separate company was already feeding those cattle, and being paid for it. Agridime paid twice."),
 L("And the math, the indictment says, did not add up. One September twenty twenty-three email read: one hundred twenty-four head, times seven hundred fifty dollars per head, equals one hundred twenty-three thousand. At that rate, the correct figure was ninety-three thousand.",
   doc("ssi_35", SSI + " · PAGE 35", "“124 head x $750 per head = $123,000”", SRC_SSI, 0),
   show="And the math, the indictment says, did not add up. One September 2023 email read: \"124 head x $750 per head = $123,000.\" At that rate, the correct figure was $93,000."),
 L("When the accountants asked for a copy of the lease with Jason, Joshua answered: we do the billing on a per head basis at seven hundred fifty dollars per head. No lease existed, according to the indictment.",
   doc("ssi_36", SSI + " · PAGE 36", "“Can you send us the lease you have with Jason”", SRC_SSI, 1),
   show="When the accountants asked for a copy of the lease with Jason, Joshua answered: \"we do the billing on a per head basis at $750 per head.\" No lease existed, according to the indictment."),
 L("In all, prosecutors say, more than two point seven million dollars went to Shady Brook. Here is what bank records showed it bought.",
   dict(type="stat", kicker="\"FEED AND YARDAGE\" · NOV 2021 – JAN 2024", value="$2.7M+", label="paid to the brother's ranch for services it did not provide", src=SRC_V),
   show="In all, prosecutors say, more than $2.7 million went to Shady Brook. Here is what bank records showed it bought."),
 L("One million, four hundred ninety-eight thousand, two hundred seventy-five dollars, for a five-bedroom, four-bathroom barndominium in Kansas, built, prosecutors say, for the brothers' recreational use.",
   photo("rel_barndo", "THE \"BARNDOMINIUM\" · PHOTO RELEASED BY THE U.S. ATTORNEY", SRC_V, fit="cover"),
   show="$1,498,275 for a five-bedroom, four-bathroom \"barndominium\" in Kansas, built, prosecutors say, for the brothers' recreational use."),
 L("Twenty-four thousand, eight hundred thirty-eight dollars for a two thousand six Hummer H two. And thousands more for solar panels and plumbing supplies.",
   doc("ssi_37", SSI + " · PAGE 37", "Barndominium · 2006 Hummer H2", SRC_SSI, 2),
   show="$24,838 for a 2006 Hummer H2. And thousands more for solar panels and plumbing supplies."),
 L("Even after the company collapsed, the bills kept coming. In January twenty twenty-four, Jason emailed the court-appointed receiver now running Agridime, demanding payment. If Shady Brook is not paid, he wrote, I will have no choice but to start selling cattle to cover those bills.",
   doc("ssi_37", SSI + " · PAGE 37", "“I will have no choice but to start selling cattle”", SRC_SSI, 0),
   show="Even after the company collapsed, the bills kept coming. In January 2024, Jason emailed the court-appointed receiver now running Agridime, demanding payment. \"If Shady Brook is not paid,\" he wrote, \"I will have no choice but to start selling cattle to cover those bills.\""),
 L("The next day he explained the seven-hundred-fifty-dollar rate: there is still feed that grows out of the ground.",
   dict(type="quote", q="There is still feed that grows out of the ground.", case=CASE, doc="JASON LINK · E-MAIL · JAN 11, 2024", cite="As quoted in " + SRC_SSI, size=58),
   show="The next day he explained the $750 rate: \"There is still feed that grows out of the ground.\""),
 # V
 L("Chapter five. The collapse and the flight.", dict(type="chapter", n="V", title="The Flight")),
 L("On December eleventh, twenty twenty-three, the SEC filed suit, under seal, to halt what it called an active Ponzi scheme. The same day, a federal judge in Fort Worth appointed a receiver to take control of Agridime.",
   doc("sec_1", "SEC v. AGRIDIME · COMPLAINT · DEC 11, 2023", "“active Ponzi scheme”", SRC_SEC, 0),
   show="On December 11, 2023, the SEC filed suit, under seal, to halt what it called an \"active Ponzi scheme.\" The same day, a federal judge in Fort Worth appointed a receiver to take control of Agridime."),
 L("In May twenty twenty-four, the Commodity Futures Trading Commission sued too. In June twenty twenty-five, Agridime agreed to a judgment ordering one hundred two point nine million dollars in restitution, to be paid through the receiver.",
   doc("cftc_5", "CFTC v. AGRIDIME · CONSENT ORDER · JUNE 2025", "Restitution: $102,936,904", SRC_CFTC, 0),
   show="In May 2024, the Commodity Futures Trading Commission sued too. In June 2025, Agridime agreed to a judgment ordering $102.9 million in restitution, to be paid through the receiver."),
 L("Then the criminal case. On January twenty-ninth, twenty twenty-six, a federal arrest warrant was issued for Joshua Link. On February eleventh, a Fort Worth grand jury indicted him and four others.",
   doc("poster", "FBI WANTED POSTER · CAUTION", "Warrant: January 29, 2026", SRC_FBI, 0, pan=[0.35, 0.45]),
   show="Then the criminal case. On January 29, 2026, a federal arrest warrant was issued for Joshua Link. On February 11, a Fort Worth grand jury indicted him and four others."),
 L("Link was not in custody. He was already on the FBI's wanted list. In reality, the poster said, Agridime purchased only a fraction of the cattle. Approximate loss: one hundred fifteen million dollars, to over two thousand buyers.",
   doc("poster", "WANTED BY THE FBI", "“purchased only a fraction of the cattle”", SRC_FBI, 0),
   show="Link was not in custody. He was already on the FBI's wanted list. \"In reality,\" the poster said, \"Agridime purchased only a fraction of the cattle.\" Approximate loss: $115 million, to over 2,000 buyers."),
 L("For more than a month he was on the FBI's white-collar wanted list. On March ninth, according to FBI Dallas, he was taken into custody at Los Angeles International Airport, by Customs and Border Protection, airport police and FBI task force officers.",
   dict(type="big", kicker="LAX · MARCH 9, 2026", lines=["Fugitive:", "taken into custody|at the airport."], src=SRC_DTN),
   show="For more than a month he was on the FBI's white-collar wanted list. On March 9, according to FBI Dallas, he was taken into custody at Los Angeles International Airport, by Customs and Border Protection, airport police and FBI task force officers."),
 L("Two days later, a second indictment charged both Link brothers over the ranch payments. One by one, the others pleaded guilty.",
   doc("ssi_1", SSI + " · SEPTEMBER 2026", "Joshua Link · Royana Thomas · Jason Link", SRC_SSI + " · " + SRC_IND2, 0),
   show="Two days later, a second indictment charged both Link brothers over the ranch payments. One by one, the others pleaded guilty."),
 L("Jed Wood, the co-founder, in March. In his plea papers he stipulated that he and others obtained over two hundred twenty million dollars from over two thousand victims.",
   doc("wood_5", "FACTUAL RESUME · JED WOOD · STIPULATED", "“over $220 million from over 2,000 victims”", SRC_WOOD, 0),
   show="Jed Wood, the co-founder, in March. In his plea papers he stipulated that he and others \"obtained over $220 million from over 2,000 victims.\""),
 L("Tia Link in June. Taylor Bang in September. Royana Thomas on November fourth. That left the two brothers.",
   dict(type="list", kicker="GUILTY PLEAS · 2026", items=[["MAR 25", "Jed Wood · Operations Director · wire fraud conspiracy"], ["JUN 17", "Tia Link · Marketing Director · money laundering"], ["SEP 9", "Taylor Bang · cattle broker · wire fraud conspiracy"], ["NOV 4", "Royana Thomas · Financial Controller · wire fraud conspiracy"]], src=SRC_V),
   show="Tia Link in June. Taylor Bang in September. Royana Thomas on November 4. That left the two brothers."),
 # VI
 L("Chapter six. The verdict.", dict(type="chapter", n="VI", title="The Verdict")),
 L("The trial lasted six days, before U.S. District Judge Mark Pittman. Prosecutors laid out the contracts, the money, and the ranch.",
   dict(type="big", kicker="FORT WORTH · NOVEMBER 2026", lines=["Six days.", "One jury."], src=SRC_V),
   show="The trial lasted six days, before U.S. District Judge Mark Pittman. Prosecutors laid out the contracts, the money, and the ranch."),
 L("On November tenth, it returned its verdict. Joshua Link: guilty on two counts of wire fraud conspiracy, two counts of wire fraud, and two counts of money laundering.",
   dict(type="verdict", kicker="NOVEMBER 10, 2026 · JOSHUA LINK", stamp="GUILTY", big="6 counts", sub="2 wire fraud conspiracy · 2 wire fraud · 2 money laundering"),
   show="On November 10, it returned its verdict. Joshua Link: guilty on two counts of wire fraud conspiracy, two counts of wire fraud, and two counts of money laundering."),
 L("Jason Link: guilty on one count of wire fraud conspiracy, two counts of wire fraud, and two counts of money laundering.",
   dict(type="verdict", kicker="NOVEMBER 10, 2026 · JASON LINK", stamp="GUILTY", big="5 counts", sub="1 wire fraud conspiracy · 2 wire fraud · 2 money laundering")),
 L("The jury also found that the brothers conspired to defraud Agridime itself, and its owners.",
   dict(type="big", lines=["Guilty of", "defrauding|their own company."], src=SRC_V)),
 L("These defendants preyed directly on Main Street Americans, U.S. Attorney Ryan Raybould said. Instead of building a legitimate cattle business, the Link brothers ran a high-tech Ponzi scheme.",
   dict(type="quote", q="Instead of building a legitimate cattle business, the Link brothers ran a high-tech Ponzi scheme", case=CASE, doc="U.S. ATTORNEY RYAN RAYBOULD", cite=SRC_V, size=46),
   show="\"These defendants preyed directly on Main Street Americans,\" U.S. Attorney Ryan Raybould said. \"Instead of building a legitimate cattle business, the Link brothers ran a high-tech Ponzi scheme.\""),
 L("The FBI's special agent in charge in Dallas spoke of the brothers' calculated efforts to lure prospective investors.",
   dict(type="quote", q="the two brothers' calculated efforts to lure prospective investors", case=CASE, doc="FBI DALLAS SAC R. JOSEPH ROTHROCK", cite=SRC_V, size=50),
   show="The FBI's special agent in charge in Dallas spoke of \"the two brothers' calculated efforts to lure prospective investors.\""),
 L("Each conspiracy and wire fraud count carries up to twenty years in prison. Each money laundering count, up to ten. The judge, not the maximum, will decide the sentence. Sentencing for both brothers is set for March fourth, twenty twenty-seven.",
   dict(type="stat", kicker="SENTENCING", value="Mar 4, 2027", label="up to 20 years per fraud count · up to 10 per laundering count", src=SRC_V),
   show="Each conspiracy and wire fraud count carries up to 20 years in prison. Each money laundering count, up to 10. The judge, not the maximum, will decide the sentence. Sentencing for both brothers is set for March 4, 2027."),
 L("The four who pleaded guilty face their own sentences, and restitution to the victims is still to be decided.",
   dict(type="big", lines=["Restitution:", "still to be|decided."], src=SRC_V)),
 L("So here is the whole case in one line. Two thousand dollars a head, fifteen to twenty percent guaranteed. More than two hundred forty million dollars collected. About sixty thousand more head of cattle sold than Agridime controlled.",
   dict(type="list", kicker="THE CASE IN NUMBERS", items=[["$2,000", "per head, \"guaranteed 15-20% yearly profits\""], ["$240M+", "collected from more than 2,200 victims, 2021–2023"], ["~60,000", "more head sold than Agridime controlled"], ["$2.7M+", "in \"feed and yardage\" to the brother's ranch"], ["6 + 5", "guilty counts · Joshua and Jason Link"]], src=SRC_V + " · " + SRC_SSI),
   show="So here is the whole case in one line. $2,000 a head, 15-20% guaranteed. More than $240 million collected. About 60,000 more head of cattle sold than Agridime controlled."),
 L("Their own ad said it first. We know it sounds too good to be true.",
   doc("sec_1", "SEC v. AGRIDIME · COMPLAINT", "“We know it sounds too good to be true.”", SRC_SEC, 1),
   show="Their own ad said it first: \"We know it sounds too good to be true.\""),
 L("What sentence should the Link brothers get in March? Tell me in the comments. This is SWORN. Real trials. Real evidence. The verdict.", dict(type="end")),
]

# --- Fact-check FIXes (factcheck.md, independent agent, 16 fixes) ---
def setline(prefix, say=None, show=None, scene=None):
    m = [l for l in lines if l["say"].startswith(prefix)]
    assert len(m) == 1, prefix
    l = m[0]
    if say: l["say"] = say
    if show: l["show"] = show
    if scene: l["scene"].update(scene)
setline("Prosecutors say their company", say="Prosecutors say Joshua Link's company sold cattle to more than twenty-two hundred people across the U.S., and collected over two hundred forty million dollars. It sold about sixty thousand more head of cattle than it controlled.", show="Prosecutors say Joshua Link's company sold cattle to more than 2,200 people across the U.S., and collected over $240 million. It sold about 60,000 more head of cattle than it controlled.")
setline("Agridime was registered in Texas", say="Agridime was registered in Texas in April twenty seventeen and headquartered in Fort Worth. It offered cattle sales, meat processing, distribution and retail meat sales.", show="Agridime was registered in Texas in April 2017 and headquartered in Fort Worth. It offered cattle sales, meat processing, distribution and retail meat sales.", scene={"hl": [0.0, 0.855, 1.0, 0.11]})
setline("So where did the new money go?", say="So where did the new money go? The SEC alleged that at least fifty-eight million dollars, between December twenty twenty-two and September twenty twenty-three, was used to pay earlier investors. In short, the SEC wrote, Agridime is operating a Ponzi scheme.", show="So where did the new money go? The SEC alleged that at least $58 million, between December 2022 and September 2023, was used to pay earlier investors. \"In short,\" the SEC wrote, \"Agridime is operating a Ponzi scheme.\"")
setline("And someone was getting paid.", say="And someone was getting paid. A table released by the U.S. Attorney's Office shows salaries and commissions from twenty twenty-one through twenty twenty-three. Josh and Tia Link, combined because of a joint bank account: two point seven three million dollars. Jed Wood: two point four one million.", show="And someone was getting paid. A table released by the U.S. Attorney's Office shows salaries and commissions from 2021 through 2023. Josh and Tia Link, combined because of a joint bank account: $2.73 million. Jed Wood: $2.41 million.", scene={"caption": "SALARY & COMMISSION TABLE · RELEASED BY THE U.S. ATTORNEY"})
setline("Then the regulators arrived.", say="Then the regulators arrived. In April twenty twenty-three, Arizona ordered Agridime to stop selling its cattle contracts in that state. In May, North Dakota issued its own cease-and-desist order.", show="Then the regulators arrived. In April 2023, Arizona ordered Agridime to stop selling its cattle contracts in that state. In May, North Dakota issued its own cease-and-desist order.")
setline("There was a second scheme.", say="There was a second scheme. And this one, the jury found, the Link brothers ran against Agridime itself.")
setline("Jason Link, Joshua's brother", scene={"hl": [0.0, 0.4295, 1.0, 0.04]})
setline("From November twenty twenty-one", scene={"caption": "PAYMENTS TO SHADY BROOK · TABLE RELEASED BY THE U.S. ATTORNEY"})
setline("Even after the company collapsed", say="Even after the company collapsed, the bills kept coming. In January twenty twenty-four, the indictment says, Jason emailed the court-appointed receiver now running Agridime, demanding payment. If Shady Brook is not paid, he wrote, I will have no choice but to start selling cattle to cover those bills.", show="Even after the company collapsed, the bills kept coming. In January 2024, the indictment says, Jason emailed the court-appointed receiver now running Agridime, demanding payment. \"If Shady Brook is not paid …,\" he wrote, \"I will have no choice but to start selling cattle to cover those bills.\"")
setline("Then the criminal case.", scene={"hl": [0.0, 0.866, 1.0, 0.03]})
setline("For more than a month", say="For about four weeks he was on the FBI's white-collar wanted list. On March ninth, according to FBI Dallas, he was taken into custody at Los Angeles International Airport, by Customs and Border Protection, airport police and FBI task force officers.", show="For about four weeks he was on the FBI's white-collar wanted list. On March 9, according to FBI Dallas, he was taken into custody at Los Angeles International Airport, by Customs and Border Protection, airport police and FBI task force officers.")
setline("Two days later, a second indictment", scene={"hl": [0.0, 0.362, 1.0, 0.108]})
setline("The jury also found", scene={"lines": ["Guilty of", "defrauding|Agridime itself."]})
from panfix import fix
fix(lines, "long")
spec = {"label": "SWORN · CASE 014", "lines": lines}
if __name__ == "__main__":
    json.dump(spec, open(os.path.join(HERE, "episode.json"), "w"), indent=1, ensure_ascii=False)
    print(len(lines), "lines,", sum(len(l["say"].split()) for l in lines), "words")
