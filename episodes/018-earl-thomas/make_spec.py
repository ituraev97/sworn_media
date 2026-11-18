import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
def hl(name, i=0):
    a, b = HL[name][i]
    return [0.0, a, 1.0, round(b - a, 4)]
SRC_P = "U.S. Attorney's Office, E.D. La., press release (Nov 17, 2026)"
SRC_I = "U.S. Attorney's Office, E.D. La., press release on the superseding indictment (Dec 23, 2024)"
SRC_FOX = "Fox News (Nov 8, 2023), citing NOLA.com and the Jefferson Parish Sheriff's Office"
SRC_CBS = "CBS Sports (Nov 8, 2023), citing NOLA.com"
SRC_TMZ24 = "TMZ (Dec 21, 2024), citing court documents"
SRC_TMZ13 = "TMZ (Nov 13, 2026), citing a federal court document"
SRC_TMZ16 = "TMZ (Nov 16, 2026), citing court documents"
SRC_WIKI = "Wikipedia, \"Earl Thomas\" (accessed Nov 18, 2026)"
SRC_SI = "Sports Illustrated / Longhorns On SI (Nov 9, 2023)"
PH14 = "PHOTO: KEITH ALLISON · CC BY-SA 2.0 · WIKIMEDIA COMMONS · 2014"
PH18 = "PHOTO: JEFFREY BEALL · CC BY 4.0 · WIKIMEDIA COMMONS · 2018"
PH11 = "PHOTO: JEFFREY BEALL · CC BY-SA 3.0 · WIKIMEDIA COMMONS · 2011"
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
def doc(img, kicker, title, src, i=0, pan=None):
    return dict(type="doc", img=f"img/{img}.jpg", pan=pan or [0.0, 0.1], hl=hl(img, i), kicker=kicker, title=title, src=src)
def photo(img, caption, src):
    return dict(type="photo", img=f"img/{img}.jpg", caption=caption, src=src, fit="contain")
PR = "U.S. ATTORNEY · E.D. LA. · "
PLEA = PR + "NOV 17, 2026"
IND = PR + "DEC 23, 2024 · THE INDICTMENT"
lines = [
 # COLD OPEN
 L("June twenty twenty-three. A man pulls up to a credit union near New Orleans, driving a Rolls-Royce. The account he has come to use is in another man's name.",
   doc("plea", PLEA, "“arrived driving a Rolls Royce”", SRC_P, 11),
   show="June 2023. A man pulls up to a credit union near New Orleans, driving a Rolls-Royce. The account he has come to use is in another man's name."),
 L("According to the Justice Department, the Rolls-Royce had been fraudulently obtained from that same man. Credit union officials had already called the sheriff's office.",
   show="According to the Justice Department, the Rolls-Royce had been \"fraudulently obtained\" from that same man. Credit union officials had already called the sheriff's office."),
 L("News reports, citing the sheriff's office and court records, identified the man whose name was on that account. Earl Thomas. Super Bowl champion, seven-time Pro Bowl safety, a star of Seattle's Legion of Boom.",
   photo("earl_2014", "EARL THOMAS · SEATTLE SEAHAWKS · 2014", PH14),
   show="News reports, citing the sheriff's office and court records, identified the man whose name was on that account. Earl Thomas. Super Bowl champion, 7-time Pro Bowl safety, a star of Seattle's Legion of Boom."),
 L("And on November twelfth, twenty twenty-six, in federal court in New Orleans, two people pleaded guilty. The man in the Rolls-Royce, Kevin Thompson. And Earl Thomas's estranged wife, Nina Thomas.",
   dict(type="verdict", kicker="NEW ORLEANS · NOVEMBER 12, 2026", stamp="PLEADED GUILTY", big="Conspiracy to commit wire fraud", sub="Kevin J. Thompson · Nina Thomas"),
   show="And on November 12, 2026, in federal court in New Orleans, two people pleaded guilty. The man in the Rolls-Royce, Kevin Thompson. And Earl Thomas's estranged wife, Nina Thomas."),
 L("The Justice Department's total: between one and a half and three million dollars, stolen from the victim.",
   dict(type="stat", kicker="THE JUSTICE DEPARTMENT'S TOTAL", value="$1.5M–$3M", label="stolen from the victim", src=SRC_P),
   show="The Justice Department's total: between $1.5 million and $3 million, stolen from the victim."),
 L("This is how it worked. Fake signatures, accounts in his name, his paychecks rerouted, his cars sold. And how a phone number on a form brought it all down.",
   dict(type="title", kicker="SWORN · CASE 018 · BREAKING", title="The Earl Thomas|Accounts", sub="United States v. Thompson & Thomas · E.D. La. · 2:24-cr-00058")),
 # I
 L("Chapter one. The star.", dict(type="chapter", n="I", title="The Star")),
 L("To understand why anyone would target Earl Thomas, start with the money he earned.",
   dict(type="big", kicker="WHY HIM", lines=["Start with", "the money|he earned."], src=SRC_WIKI)),
 L("Thomas grew up in Orange, Texas, and starred at the University of Texas. In twenty ten, the Seattle Seahawks took him in the first round, fourteenth overall.",
   photo("earl_2011", "EARL THOMAS · SEAHAWKS · 2011", PH11),
   show="Thomas grew up in Orange, Texas, and starred at the University of Texas. In 2010, the Seattle Seahawks took him in the first round, 14th overall."),
 L("At Texas, he was a consensus All-American in twenty oh nine, and played in the national championship game against Alabama.",
   dict(type="big", kicker="UNIVERSITY OF TEXAS · 2009", lines=["Consensus", "All-American."], src=SRC_WIKI + " · " + SRC_SI),
   show="At Texas, he was a consensus All-American in 2009, and played in the national championship game against Alabama."),
 L("He became the center field of the Legion of Boom, the Seattle secondary that won the franchise's first Super Bowl, forty-three to eight over Denver, in February twenty fourteen.",
   dict(type="stat", kicker="SUPER BOWL XLVIII · FEB 2, 2014", value="43–8", label="Seattle over Denver", src=SRC_WIKI),
   show="He became the center field of the Legion of Boom, the Seattle secondary that won the franchise's first Super Bowl, 43 to 8 over Denver, in February 2014."),
 L("A year later, he started in a second Super Bowl, a loss to New England.",
   photo("earl_back", "EARL THOMAS III · SEAHAWKS · 2013", "PHOTO: MIKE MORRIS · CC BY-SA 2.0 · WIKIMEDIA COMMONS · 2013")),
 L("Seven Pro Bowls. Three first-team All-Pro selections. A place on the NFL's All-Decade Team of the twenty-tens.",
   dict(type="list", kicker="THE RÉSUMÉ", items=[["7", "Pro Bowls"], ["3", "first-team All-Pro selections"], ["1", "Super Bowl ring (XLVIII)"], ["2010s", "All-Decade Team"]], src=SRC_WIKI),
   show="7 Pro Bowls. 3 first-team All-Pro selections. A place on the NFL's All-Decade Team of the 2010s."),
 L("And the contracts were big. In twenty fourteen, Seattle extended him for four years and forty million dollars. In twenty nineteen, he signed with the Baltimore Ravens: four years, fifty-five million, thirty-two million of it guaranteed.",
   dict(type="bars", kicker="CONTRACTS", title="Reported contract values", items=[{"label": "Seattle extension · 2014", "value": 40, "display": "$40M"}, {"label": "Baltimore · 2019", "value": 55, "display": "$55M"}], src=SRC_WIKI),
   show="And the contracts were big. In 2014, Seattle extended him for 4 years and $40 million. In 2019, he signed with the Baltimore Ravens: 4 years, $55 million, $32 million of it guaranteed."),
 L("He has not played in the NFL since the Ravens released him in August twenty twenty. By December, his marriage was ending too.",
   photo("earl_2018", "EARL THOMAS · SEAHAWKS · 2018", PH18),
   show="He has not played in the NFL since the Ravens released him in August 2020. By December, his marriage was ending too."),
 L("And that is where the federal case begins. Not on a football field. In a divorce court.",
   dict(type="big", lines=["Not on a", "football field.|In a divorce court."], src=SRC_P)),
 # II
 L("Chapter two. The order.", dict(type="chapter", n="II", title="The Order")),
 L("According to court documents, in December twenty twenty, Nina Thomas filed a petition for divorce from her husband, the victim.",
   doc("plea", PLEA, "“filed a petition for divorce”", SRC_P, 2, pan=[0.12, 0.16]),
   show="According to court documents, in December 2020, Nina Thomas filed a petition for divorce from her husband, \"the victim.\""),
 L("The Justice Department's release never names him. News reports have, since twenty twenty-three, and this video follows them.",
   dict(type="big", kicker="A NOTE ON NAMES", lines=["DOJ: “the victim.”", "News reports:|Earl Thomas."], src=SRC_P + " · " + SRC_FOX + " · " + SRC_TMZ13)),
 L("Under the terms of a court order, both parties were ordered to not transfer property, or negotiate any negotiable instruments or checks, in the other's name.",
   doc("plea", PLEA, "“ordered to not transfer property”", SRC_P, 2),
   show="Under the terms of a court order, both parties were \"ordered to not transfer property or negotiate any negotiable instruments or checks in the other’s name.\""),
 L("Remember that order. Because in twenty twenty-one, the release says, Nina Thomas entered into a romantic relationship with Kevin Thompson, of New Orleans.",
   doc("plea", PLEA, "“a romantic relationship”", SRC_P, 3),
   show="Remember that order. Because in 2021, the release says, Nina Thomas entered into a romantic relationship with Kevin Thompson, of New Orleans."),
 L("And together, prosecutors say, they devised a scheme to defraud the victim, including by impersonating him, and making unauthorized financial transfers by electronic wires.",
   show="And together, prosecutors say, they devised a scheme to defraud the victim, \"including by impersonating the victim and making unauthorized financial transfers by electronic wires.\""),
 L("The indictment put a start date on it: on or about September sixth, twenty twenty-one.",
   doc("ind", IND, "From September 6, 2021", SRC_I, 3),
   show="The indictment put a start date on it: on or about September 6, 2021."),
 L("And it ran, the indictment says, to on or about December thirteenth, twenty twenty-four. More than three years, money moving from the victim's real accounts into accounts the two of them created.",
   doc("ind", IND, "From his accounts to theirs", SRC_I, 3),
   show="And it ran, the indictment says, to on or about December 13, 2024. More than 3 years, money moving from the victim's real accounts into accounts the two of them created."),
 L("So how do you become another man? The first step, according to the indictment, was an email address.",
   dict(type="big", kicker="THE QUESTION", lines=["How do you become", "another man?"], src=SRC_I)),
 # III
 L("Chapter three. The accounts.", dict(type="chapter", n="III", title="The Accounts")),
 L("The indictment says they created an email account in the victim's name. Then they used it to open several bank accounts, with Thompson's address, or his telephone number.",
   doc("ind", IND, "“an email account in Victim 1’s name”", SRC_I, 4),
   show="The indictment says they created an email account in the victim's name. Then they used it to open several bank accounts, with Thompson's address, or his telephone number."),
 L("In twenty twenty-two, the plea release says, they opened accounts at a credit union and a bank in the New Orleans area, under the victim's name.",
   doc("plea", PLEA, "Accounts “under the victim’s name”", SRC_P, 4),
   show="In 2022, the plea release says, they opened accounts at a credit union and a bank in the New Orleans area, under the victim's name."),
 L("And one detail stands out. At the direction of Nina Thomas, the release says, Thompson practiced signing the victim's name.",
   dict(type="quote", q="At the direction of THOMAS, THOMPSON practiced signing the victim’s name.", case="UNITED STATES v. THOMPSON & THOMAS", doc="U.S. ATTORNEY'S RELEASE · NOV 17, 2026", cite=SRC_P),
   show="And one detail stands out. \"At the direction of THOMAS,\" the release says, \"THOMPSON practiced signing the victim’s name.\""),
 L("Sheriff's investigators said in twenty twenty-three that Thompson opened the credit union account with a driver's license bearing Thomas's information, and his own photo.",
   dict(type="big", kicker="JEFFERSON PARISH SHERIFF'S OFFICE · 2023", lines=["His name.", "Thompson's|photo."], src=SRC_CBS),
   show="Sheriff's investigators said in 2023 that Thompson opened the credit union account with a driver's license bearing Thomas's information, and his own photo."),
 L("Then came the money. After the accounts were opened, a direct deposit form was signed and submitted to the victim's labor union association, sending all of his payments to the new account. Without his authorization.",
   doc("plea", PLEA, "“direct deposit authorization form”", SRC_P, 5),
   show="Then came the money. After the accounts were opened, a direct deposit form was signed and submitted to the victim's labor union association, sending all of his payments to the new account. Without his authorization."),
 L("One check deposited into that account totaled eight hundred eighty-five thousand, four hundred nineteen dollars.",
   dict(type="stat", kicker="ONE CHECK", value="$885,419", label="deposited into the account in his name", src=SRC_P),
   show="One check deposited into that account totaled $885,419."),
 L("Between twenty twenty-two and twenty twenty-three, the release says, Thompson, using the victim's identification and aided by Nina Thomas, deposited or withdrew hundreds of thousands of dollars at a bank in New Orleans.",
   doc("plea", PLEA, "“hundreds of thousands of dollars”", SRC_P, 6),
   show="Between 2022 and 2023, the release says, Thompson, using the victim's identification and aided by Nina Thomas, deposited or withdrew hundreds of thousands of dollars at a bank in New Orleans."),
 L("The deposits included union checks payable to the victim, and proceeds from vehicles owned by the victim, sold without his authorization.",
   show="The deposits included union checks payable to the victim, and proceeds from vehicles owned by the victim, sold without his authorization."),
 L("The indictment described cash withdrawals of as much as three hundred thousand dollars at a time.",
   doc("ind", IND, "Withdrawals “as much as $300,000.00”", SRC_I, 5),
   show="The indictment described cash withdrawals of as much as $300,000 at a time."),
 L("And it named two purchases. A Hermès Birkin handbag, for twenty-eight thousand, seven hundred ninety-six dollars. And a Porsche Panamera, for fifty-two thousand, eight hundred ninety.",
   doc("ind", IND, "A Birkin and a Porsche", SRC_I, 6),
   show="And it named two purchases. A Hermès Birkin handbag, for $28,796. And a Porsche Panamera, for $52,890."),
 L("Even his credit card was used. The plea release says they used his driver's license to authorize a charge on his card, for plastic surgery for another person.",
   doc("plea", PLEA, "His card, someone else’s surgery", SRC_P, 7),
   show="Even his credit card was used. The plea release says they used his driver's license to authorize a charge on his card, for plastic surgery for another person."),
 L("Proceeds from other transactions, it says, were used to buy luxury items for the two of them.",
   doc("plea", PLEA, "“luxury items”", SRC_P, 8)),
 L("It went on for about two years. And it might have gone on longer, if not for one line on one form.",
   dict(type="big", kicker="2022 → 2023", lines=["One line", "on one form."], src=SRC_P)),
 # IV
 L("Chapter four. The Rolls-Royce.", dict(type="chapter", n="IV", title="The Rolls-Royce")),
 L("In June twenty twenty-three, the credit union contacted the Jefferson Parish Sheriff's Office. Someone, it said, had assumed the victim's identity, and withdrawn more than seven hundred thousand dollars from his account.",
   doc("plea", PLEA, "“had assumed the victim’s identity”", SRC_P, 10),
   show="In June 2023, the credit union contacted the Jefferson Parish Sheriff's Office. Someone, it said, had assumed the victim's identity, and withdrawn more than $700,000 from his account."),
 L("Thompson was scheduled to visit the credit union. He arrived driving a Rolls-Royce, fraudulently obtained from the victim.",
   doc("plea", PLEA, "“driving a Rolls Royce”", SRC_P, 11),
   show="Thompson was scheduled to visit the credit union. He arrived driving a Rolls-Royce, fraudulently obtained from the victim."),
 L("Reports at the time, citing the sheriff's office, described it as a blue Rolls-Royce Cullinan SUV. The date was June ninth.",
   dict(type="big", kicker="JUNE 9, 2023 · PER NOLA.COM VIA FOX NEWS", lines=["A blue", "Rolls-Royce|Cullinan."], src=SRC_FOX),
   show="Reports at the time, citing the sheriff's office, described it as a blue Rolls-Royce Cullinan SUV. The date was June 9."),
 L("And here is the line on the form. Credit union officials reviewed the membership form, and learned that though the account was in the victim's name, the phone number used to open it was Thompson's.",
   doc("plea", PLEA, "The phone number was Thompson’s", SRC_P, 12),
   show="And here is the line on the form. Credit union officials reviewed the membership form, and learned that though the account was in the victim's name, the phone number used to open it was Thompson's."),
 L("Officers arrested him. In his possession, the release says: a driver's license, a Social Security card, and bank cards, all in the victim's name.",
   doc("plea", PLEA, "His ID cards, in the victim’s name", SRC_P, 13),
   show="Officers arrested him. In his possession, the release says: a driver's license, a Social Security card, and bank cards, all in the victim's name."),
 L("Then officers got a search warrant for Thompson's home. What they found turned an identity theft case into a drug case too.",
   dict(type="big", kicker="THE SEARCH WARRANT", lines=["An identity case", "becomes|a drug case."], src=SRC_P)),
 L("Three thousand, seven hundred sixteen grams of cocaine. A Springfield Armory Hellcat pistol. And two hundred twenty-eight thousand dollars in cash.",
   doc("plea", PLEA, "What the search found", SRC_P, 14),
   show="3,716 grams of cocaine. A Springfield Armory Hellcat pistol. And $228,000 in cash."),
 L("At first, the charges were local. Identity theft, forgery, money laundering, bank fraud and more, and a bond reported at seven hundred thirty thousand dollars.",
   dict(type="list", kicker="STATE CHARGES · 2023 · PER NOLA.COM", items=[["1", "identity theft"], ["2", "forgery"], ["3", "money laundering"], ["4", "credit card, computer & bank fraud"]], src=SRC_FOX),
   show="At first, the charges were local. Identity theft, forgery, money laundering, bank fraud and more, and a bond reported at $730,000."),
 L("And then, according to those reports, after his release, Thompson went to the sheriff's office to try to get the Rolls-Royce back. He arrived in a car that had been reported stolen in Atlanta.",
   dict(type="big", kicker="PER NOLA.COM, AS REPORTED BY FOX NEWS & CBS SPORTS", lines=["He came back", "for the Rolls."], src=SRC_FOX + " · " + SRC_CBS)),
 L("The sheriff's office said federal investigators were also involved. By twenty twenty-four, it was a federal case.",
   dict(type="big", lines=["Then the", "FBI and DEA|stepped in."], src=SRC_FOX + " · " + SRC_P)),
 # V
 L("When the story first broke, in November twenty twenty-three, reports put the loss at about one point nine million dollars. The number would keep moving.",
   dict(type="bars", kicker="THE NUMBER, OVER TIME", title="How much was taken?", items=[{"label": "Nov 2023 · news reports", "value": 1.9, "display": "~$1.9M"}, {"label": "Dec 2024 · alleged, per TMZ", "value": 2.7, "display": "$2.7M+"}, {"label": "Nov 2026 · DOJ, after the pleas", "value": 3, "display": "$1.5M–$3M"}], src=SRC_FOX + " · " + SRC_TMZ24 + " · " + SRC_P),
   show="When the story first broke, in November 2023, reports put the loss at about $1.9 million. The number would keep moving."),
 L("Chapter five. The indictment.", dict(type="chapter", n="V", title="The Indictment")),
 L("On December thirteenth, twenty twenty-four, a federal grand jury in New Orleans returned a superseding indictment, now charging Kevin Thompson and Nina Thomas together.",
   doc("ind", IND, "The superseding indictment", SRC_I, 0),
   show="On December 13, 2024, a federal grand jury in New Orleans returned a superseding indictment, now charging Kevin Thompson and Nina Thomas together."),
 L("The counts: conspiracy to commit wire fraud, wire fraud, aggravated identity theft, and money laundering.",
   dict(type="list", kicker="SUPERSEDING INDICTMENT · DEC 13, 2024", items=[["1", "conspiracy to commit wire fraud"], ["2", "wire fraud"], ["3", "aggravated identity theft"], ["4", "money laundering"]], src=SRC_I)),
 L("Thompson alone was also charged with possessing cocaine with intent to distribute, and with possessing a firearm in furtherance of a drug trafficking crime.",
   doc("ind", IND, "Thompson alone", SRC_I, 1)),
 L("TMZ reported that both were taken into custody on December sixteenth, and that the court documents alleged more than two point seven million dollars had been taken.",
   dict(type="stat", kicker="ALLEGED IN DECEMBER 2024 · PER TMZ", value="$2.7M+", label="taken, the court documents alleged", src=SRC_TMZ24),
   show="TMZ reported that both were taken into custody on December 16, and that the court documents alleged more than $2.7 million had been taken."),
 L("TMZ also reported that Nina Thomas was released shortly after her arrest. The case went on, quietly, for almost two years.",
   dict(type="big", kicker="DECEMBER 2024 · PER TMZ", lines=["Released.", "The case|went on."], src=SRC_TMZ24)),
 L("The stakes were high. Each wire fraud count carried up to thirty years. Aggravated identity theft carries a mandatory two years, on top of any other sentence.",
   doc("ind", IND, "Up to 30 years · 2 years mandatory", SRC_I, 7),
   show="The stakes were high. Each wire fraud count carried up to 30 years. Aggravated identity theft carries a mandatory 2 years, on top of any other sentence."),
 L("And at that point, it was all an accusation. The U.S. Attorney reiterated that the indictment was merely a charging document, and that guilt had to be proven beyond a reasonable doubt.",
   doc("ind", IND, "“merely a charging document”", SRC_I, 9),
   show="And at that point, it was all an accusation. The U.S. Attorney \"reiterated that the superseding indictment is merely a charging document,\" and that guilt had to be proven beyond a reasonable doubt."),
 L("For almost two years, the case moved slowly. Then, this month, it ended without a trial.",
   dict(type="timeline", kicker="THE CASE", events=[{"date": "DEC 2020", "text": "Divorce petition filed"}, {"date": "SEP 2021", "text": "Scheme begins, per indictment"}, {"date": "JUN 9, 2023", "text": "Arrest at the credit union"}, {"date": "DEC 13, 2024", "text": "Superseding indictment"}, {"date": "NOV 12, 2026", "text": "Both plead guilty"}], at=4, src=SRC_P + " · " + SRC_I + " · " + SRC_FOX)),
 # VI
 L("Chapter six. The plea.", dict(type="chapter", n="VI", title="The Plea")),
 L("On November twelfth, twenty twenty-six, before U.S. District Judge Brandon S. Long, Kevin Thompson and Nina Thomas each pleaded guilty to one count of conspiracy to commit wire fraud.",
   doc("plea", PLEA, "Both pleaded guilty", SRC_P, 0),
   show="On November 12, 2026, before U.S. District Judge Brandon S. Long, Kevin Thompson and Nina Thomas each pleaded guilty to one count of conspiracy to commit wire fraud."),
 L("Thompson also pleaded guilty to possession with intent to distribute five hundred grams or more of cocaine.",
   doc("plea", PLEA, "And the cocaine count", SRC_P, 1),
   show="Thompson also pleaded guilty to possession with intent to distribute 500 grams or more of cocaine."),
 L("A conspiracy count means each of them admitted agreeing with the other to commit wire fraud. The release lists only those counts. Aggravated identity theft, with its mandatory two years, is not among them.",
   dict(type="big", kicker="WHAT THEY PLEADED TO", lines=["One count each.", "Not aggravated|identity theft."], src=SRC_P + " · " + SRC_I),
   show="A conspiracy count means each of them admitted agreeing with the other to commit wire fraud. The release lists only those counts. Aggravated identity theft, with its mandatory 2 years, is not among them."),
 L("Here is what that means in years. The wire fraud conspiracy count carries a maximum of five years in prison, for each of them.",
   doc("plea", PLEA, "Up to 5 years", SRC_P, 15),
   show="Here is what that means in years. The wire fraud conspiracy count carries a maximum of 5 years in prison, for each of them."),
 L("For Thompson, the drug count is heavier: a mandatory minimum of five years, and up to forty.",
   dict(type="bars", kicker="MAXIMUM PRISON TERMS · PER DOJ", title="What the counts carry", items=[{"label": "Wire fraud conspiracy · each", "value": 5, "display": "5 yrs max"}, {"label": "Cocaine count · Thompson (min. 5)", "value": 40, "display": "40 yrs max"}], src=SRC_P),
   show="For Thompson, the drug count is heavier: a mandatory minimum of 5 years, and up to 40."),
 L("The final number in the release: between one point five and three million dollars, stolen from the victim.",
   doc("plea", PLEA, "“stole between $1,500,000.00 and $3,000,000.00”", SRC_P, 9),
   show="The final number in the release: between $1.5 million and $3 million, stolen from the victim."),
 L("TMZ, citing the plea documents, reported a restitution figure of three million, four hundred ninety-seven thousand, four hundred forty-four dollars, owed by the two of them jointly.",
   dict(type="stat", kicker="RESTITUTION · PER TMZ", value="$3,497,444.64", label="owed jointly, TMZ reported", src=SRC_TMZ13),
   show="TMZ, citing the plea documents, reported a restitution figure of $3,497,444.64, owed by the two of them jointly."),
 L("And TMZ listed what prosecutors want forfeited. A twenty twenty Rolls-Royce Cullinan. A twenty twenty Aston Martin Vantage. A twenty eighteen Porsche Panamera. A Birkin bag, Chanel jewelry, gold chains, designer clothes, and two hundred twenty-eight thousand, eight hundred sixty dollars in cash.",
   dict(type="list", kicker="FORFEITURE LIST · PER TMZ", items=[["1", "2020 Rolls-Royce Cullinan"], ["2", "2020 Aston Martin Vantage"], ["3", "2018 Porsche Panamera"], ["4", "Birkin bag, Chanel, gold chains"], ["5", "$228,860 in cash"]], src=SRC_TMZ16),
   show="And TMZ listed what prosecutors want forfeited. A 2020 Rolls-Royce Cullinan. A 2020 Aston Martin Vantage. A 2018 Porsche Panamera. A Birkin bag, Chanel jewelry, gold chains, designer clothes, and $228,860 in cash."),
 L("According to TMZ, prosecutors also warned that if any of that property cannot be found, they can seek a money judgment, or other assets, up to the value of what is missing.",
   dict(type="big", kicker="FORFEITURE · PER TMZ", lines=["Can't find it?", "Then other|assets."], src=SRC_TMZ16)),
 L("No sentencing date was given in the release. Judge Long will decide how much prison time, if any, comes with these pleas.",
   dict(type="big", kicker="WHAT'S NEXT", lines=["Sentencing:", "Judge|Brandon S. Long."], src=SRC_P)),
 L("The case was investigated by the FBI, the Drug Enforcement Administration, and the Jefferson Parish Sheriff's Office.",
   doc("plea", PLEA, "The investigators", SRC_P, 17)),
 # CLOSE
 L("And notice what did not stop this. A court order told both spouses not to move each other's money. It did not stop the transfers. A credit union, reading one form, did.",
   dict(type="big", kicker="THE LESSON", lines=["The order didn't", "stop it.|One form did."], src=SRC_P)),
 L("So here is the case, in numbers. A court order not to touch each other's property. A practiced signature. One check for eight hundred eighty-five thousand dollars. More than seven hundred thousand withdrawn at one credit union. And a phone number that did not belong to the man on the account.",
   dict(type="list", kicker="THE CASE IN NUMBERS", items=[["$885,419", "one check"], ["$700,000+", "withdrawn at the credit union"], ["3,716 g", "cocaine found"], ["$1.5M–$3M", "stolen, per DOJ"]], src=SRC_P),
   show="So here is the case, in numbers. A court order not to touch each other's property. A practiced signature. One check for $885,419. More than $700,000 withdrawn at one credit union. And a phone number that did not belong to the man on the account."),
 L("Earl Thomas spent a decade reading quarterbacks, and taking the ball away. Off the field, according to the guilty pleas, his estranged wife and her boyfriend were taking the money, in his own name.",
   photo("earl_2014", "EARL THOMAS · 2014", PH14)),
 L("Both now wait for Judge Long's sentence. The maximum on the fraud count is five years.",
   dict(type="verdict", kicker="UNITED STATES v. THOMPSON & THOMAS", stamp="PLEADED GUILTY", big="Up to 5 years", sub="wire fraud conspiracy · sentencing pending"),
   show="Both now wait for Judge Long's sentence. The maximum on the fraud count is 5 years."),
 L("What sentence would be fair here? Tell us in the comments.",
   dict(type="end", cta="WHAT SENTENCE WOULD BE FAIR?")),
]
# ---- fact-check fixes (factcheck.md, 27 FIX items) ----
def P(i, say=None, show=None, **sc):
    if say is not None: lines[i]["say"] = say
    if show is not None: lines[i]["show"] = show
    for k, v in sc.items(): lines[i]["scene"][k] = v
assert lines[63]["say"].startswith("A conspiracy count")
P(63, lines=["One conspiracy count each.", "Not aggravated|identity theft."])
P(70, say="No sentencing date was given in the release. Judge Long will decide the sentences.")
P(59, say="For almost two years, there was no trial. Then, this month, both defendants pleaded guilty.")
P(38, say="The plea release describes this activity across twenty twenty-two and twenty twenty-three. Then a credit union noticed.",
      show="The plea release describes this activity across 2022 and 2023. Then a credit union noticed.", lines=["Then a credit union", "noticed."])
P(72, say="And notice what did not stop this. A court order told both spouses not to move each other's money. It did not stop the transfers. What exposed it was a credit union that noticed, and a phone number on a form.",
      lines=["The order didn't", "stop it.|A credit union noticed."])
P(5, say="This is how it worked. A practiced signature, accounts in his name, his union payments rerouted, his cars sold. And how a phone number on a form led to an arrest.",
     sub="United States v. Thompson & Thomas · E.D. La.")
P(42, say="Reports in November twenty twenty-three, citing the sheriff's office, described it as a blue Rolls-Royce Cullinan SUV. The date was June ninth.",
      show="Reports in November 2023, citing the sheriff's office, described it as a blue Rolls-Royce Cullinan SUV. The date was June 9.")
P(67, say="TMZ, citing a federal court document, reported a restitution figure of three million, four hundred ninety-seven thousand, four hundred forty-four dollars and sixty-four cents, which it said the two of them would be jointly responsible for paying. That is more than the Justice Department's theft range.",
      show="TMZ, citing a federal court document, reported a restitution figure of $3,497,444.64, which it said the two of them would be jointly responsible for paying. That is more than the Justice Department's theft range.",
      label="jointly, TMZ reported", src="TMZ (Nov 13, 2026), citing a federal court document")
for k in ("say", "show"):
    lines[68][k] = lines[68][k].replace("And TMZ listed what prosecutors want forfeited.", "And TMZ listed the property Nina Thomas must forfeit under her plea deal.")
lines[73]["say"] = lines[73]["say"].replace("One check for eight hundred eighty-five thousand dollars.", "One check for eight hundred eighty-five thousand, four hundred nineteen dollars.")
assert "four hundred nineteen" in lines[73]["say"] and "must forfeit" in lines[68]["say"]
t26 = "The indictment says they created an email account in the victim's name. Then they used it to open several bank accounts, using the victim's or Thompson's address, and in some cases Thompson's phone number."
P(26, say=t26, show=t26)
P(55, src="TMZ (Dec 21, 2024), citing court documents · TMZ (Nov 13, 2026)")
P(17, hl=[0.0, 0.2374, 1.0, 0.0353])
P(57, hl=[0.0, 0.6133, 1.0, 0.064])
from panfix import fix
fix(lines, "long")
spec = {"label": "SWORN · CASE 018", "lines": lines}
if __name__ == "__main__":
    json.dump(spec, open(os.path.join(HERE, "episode.json"), "w"), indent=1, ensure_ascii=False)
    print(len(lines), "lines,", sum(len(l["say"].split()) for l in lines), "words")
