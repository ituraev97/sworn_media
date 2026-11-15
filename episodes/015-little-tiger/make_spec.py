import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
def hl(name, i=0):
    a, b = HL[name][i]
    return [0.0, a, 1.0, round(b - a, 4)]
CASE = "UNITED STATES v. CHEN"
SRC_S = "U.S. Attorney's Office, S.D. Cal., press release (Nov 13, 2026)"
SRC_I = "U.S. Attorney's Office, S.D. Cal., press release on the indictment (Jul 31, 2024)"
SRC_WP = "U.S. Attorney's Office, S.D. Cal., press release (Jan 15, 2026)"
SRC_CP = "U.S. Attorney's Office, S.D. Cal., press release (Apr 2, 2026)"
SRC_WS = "U.S. Attorney's Office, S.D. Cal., press release (May 8, 2026)"
SRC_R = "U.S. Attorney's Office, S.D. Cal., press release (Aug 27, 2025)"
SRC_F = "U.S. Attorney's Office, S.D. Cal., press release (Oct 26, 2026)"
SRC_SL = "DOJ sentencing slide, published with the U.S. Attorney's release (Nov 13, 2026)"
SRC_YT = "YouTube Data API, Trilogy Media video qjiFJWsHbwE (checked Nov 15, 2026)"
SRC_IC3 = "FBI Internet Crime Complaint Center, 2025 report, as reported by Bitdefender (May 19, 2026)"
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
def doc(img, kicker, title, src, i=0, pan=None):
    return dict(type="doc", img=f"img/{img}.jpg", pan=pan or [0.0, 0.1], hl=hl(img, i), kicker=kicker, title=title, src=src)
def photo(img, caption, src, fit="contain"):
    return dict(type="photo", img=f"img/{img}.jpg", caption=caption, src=src, fit=fit)
PR = "U.S. ATTORNEY · S.D. CAL. · "
lines = [
 # COLD OPEN
 L("In July twenty twenty-three, a man went to a house in the Los Angeles area to pick up a package of cash. He believed it came from an elderly fraud victim.",
   doc("chenplea", PR + "APRIL 2, 2026", "“to pick up bulk cash”", SRC_CP, 1),
   show="In July 2023, a man went to a house in the Los Angeles area to pick up a package of cash. He believed it came from an elderly fraud victim."),
 L("Instead, two YouTubers from Trilogy Media, Ashton Bingham and Art Kulik, confronted him about working for a scam organization. Their video has now been watched more than one point four million times.",
   dict(type="big", kicker="TRILOGY MEDIA · YOUTUBE · 2023", lines=["Confronted", "on camera.|1.4 million views."], src=SRC_S + " · " + SRC_YT),
   show="Instead, two YouTubers from Trilogy Media, Ashton Bingham and Art Kulik, confronted him about working for a scam organization. Their video has now been watched more than 1.4 million times."),
 L("Court records list the man as Jiandong Chen, also known as Little Tiger.",
   photo("slide_0222", "JIANDONG CHEN, AKA \"LITTLE TIGER\" · DOJ SENTENCING SLIDE", SRC_SL),
   show="Court records list the man as Jiandong Chen, also known as \"Little Tiger.\""),
 L("On Friday, November thirteenth, twenty twenty-six, a federal judge in San Diego sentenced him to seventy-eight months in prison. Six and a half years. And the two YouTubers were in the courtroom.",
   dict(type="verdict", kicker="SAN DIEGO · NOVEMBER 13, 2026", stamp="SENTENCED", big="78 months", sub="Jiandong Chen · fraud & money laundering conspiracy"),
   show="On Friday, November 13, 2026, a federal judge in San Diego sentenced him to 78 months in prison. Six and a half years. And the two YouTubers were in the courtroom."),
 L("Investigators identified more than two thousand elderly victims, with more than twenty-seven million dollars in losses. The victims were in their seventies and eighties.",
   dict(type="stat", kicker="2021–2023", value="$27M+", label="lost by 2,000+ elderly victims", src=SRC_S),
   show="Investigators identified more than 2,000 elderly victims, with more than $27 million in losses. The victims were in their 70s and 80s."),
 L("This is how the scam worked, how the cash moved, and how a YouTube prank channel ended up in a federal sentencing hearing.",
   dict(type="title", kicker="SWORN · CASE 015 · BREAKING", title="The Little Tiger|Sting", sub="United States v. Jiandong Chen · S.D. Cal. · 24-cr-1317"),
   show="This is how the scam worked, how the cash moved, and how a YouTube prank channel ended up in a federal sentencing hearing."),
 # I
 L("Chapter one. The pop-up.", dict(type="chapter", n="I", title="The Pop-Up")),
 L("It usually started on a screen. According to the Justice Department, victims received unsolicited phone calls, emails and pop-up ads, telling them to call a phone number.",
   doc("chenplea", PR + "APRIL 2, 2026", "Unsolicited calls, emails, pop-up ads", SRC_CP, 3),
   show="It usually started on a screen. According to the Justice Department, victims received unsolicited phone calls, emails and pop-up ads, telling them to call a phone number."),
 L("Unbeknownst to the victims, the release says, those phone numbers belonged to India-based scam call centers.",
   show="\"Unbeknownst to the victims,\" the release says, \"those phone numbers belonged to India-based scam call centers.\""),
 L("The callers played tech support, the bank, or the government. In many cases, they had victims download commercially available remote desktop software, and used it to get into their computers.",
   doc("chenplea", PR + "APRIL 2, 2026", "“remote desktop software”", SRC_CP, 4),
   show="The callers played tech support, the bank, or the government. In many cases, they had victims download commercially available remote desktop software, and used it to get into their computers."),
 L("This is not a small problem. According to the FBI's Internet Crime Complaint Center, Americans sixty and older reported more than seven point seven billion dollars in losses in twenty twenty-five alone.",
   dict(type="stat", kicker="FBI IC3 · AGE 60+ · 2025", value="$7.7B+", label="in reported losses in one year", src=SRC_IC3),
   show="This is not a small problem. According to the FBI's Internet Crime Complaint Center, Americans 60 and older reported more than $7.7 billion in losses in 2025 alone."),
 L("In this case, one of the most frequent tricks was the refund scam. And it is worth knowing exactly how it works.",
   dict(type="big", kicker="THE MOST FREQUENT SCAM", lines=["The refund", "that|never came."], src=SRC_CP)),
 L("The victim was told they were owed a small refund, for example, from a retailer, for an unauthorized charge. While pretending to process it, the caller would accidentally over-refund them.",
   doc("chenplea", PR + "APRIL 2, 2026", "“accidentally ‘over-refunded’”", SRC_CP, 0),
   show="The victim was told they were owed a small refund, for example, from a retailer, for an unauthorized charge. While pretending to process it, the caller would \"accidentally\" over-refund them."),
 L("Then came the request. Send back the difference, by wire transfer, or in cash, by express mail.",
   dict(type="list", kicker="HOW THE MONEY WAS SENT", items=[["1", "wire transfer"], ["2", "bulk cash in express-mail packages"], ["3", "in-person pickups"]], src=SRC_CP + " · " + SRC_S),
   show="Then came the request. Send back the difference, by wire transfer, or in cash, by express mail."),
 L("In reality, the Justice Department says, the victims had not received any money. They were sending their own.",
   dict(type="big", lines=["No refund.", "They sent|their own money."], src=SRC_CP + " · " + SRC_WS)),
 L("So who was waiting for those boxes of cash? People on this side of the ocean. People like the Little Tiger.",
   dict(type="big", kicker="WHO PICKED UP THE CASH", lines=["The couriers.", "Like|the Little Tiger."], src=SRC_S)),
 # II
 L("Chapter two. Cash in a box.", dict(type="chapter", n="II", title="Cash in a Box")),
 L("Here is what the indictment said. The defendants provided fake names, and addresses of retail locations, including CVS Pharmacy stores, where the packages were picked up. They picked up the money-laden packages using fake IDs.",
   doc("ind", PR + "JULY 31, 2024 · THE INDICTMENT", "“fake names and addresses”", SRC_I, 2),
   show="Here is what the indictment said. The defendants provided fake names, and addresses of retail locations, including CVS Pharmacy stores, where the packages were picked up. They picked up the \"money-laden packages using fake IDs.\""),
 L("In his plea agreement, Chen admitted exactly that. He used fraudulent driver's licenses or IDs, matching the fictitious recipient names, to retrieve the packages of bulk cash.",
   doc("chenplea", PR + "APRIL 2, 2026", "“fraudulent driver’s licenses or IDs”", SRC_CP, 2),
   show="In his plea agreement, Chen admitted exactly that. He used fraudulent driver's licenses or IDs, matching the fictitious recipient names, to retrieve the packages of bulk cash."),
 L("Then the cash had to vanish. The ringleader, Zhao Wang, known as Oscar, admitted that his couriers typically delivered the money to him each day after collecting the packages.",
   doc("wangplea", PR + "JANUARY 15, 2026", "Zhao Wang, aka “Oscar” · guilty plea", SRC_WP, 0),
   show="Then the cash had to vanish. The ringleader, Zhao Wang, known as \"Oscar,\" admitted that his couriers typically delivered the money to him each day after collecting the packages."),
 L("His partners overseas supplied a cryptocurrency wallet. Wang transferred the money in crypto, and kept upwards of eighteen percent for himself.",
   dict(type="stat", kicker="ZHAO WANG · ADMITTED", value="18%", label="his cut — the rest went out in crypto", src=SRC_WP),
   show="His partners overseas supplied a cryptocurrency wallet. Wang transferred the money in crypto, and kept upwards of 18% for himself."),
 L("He also admitted he obtained the fake IDs personally, gave them to his co-conspirators, and recruited others, including his co-defendants.",
   doc("wangplea", PR + "JANUARY 15, 2026", "“obtained the fake IDs personally”", SRC_WP, 1),
   show="He also admitted he obtained the fake IDs personally, gave them to his co-conspirators, and recruited others, including his co-defendants."),
 L("Chen admitted the same pipeline. Fraud proceeds laundered through cryptocurrency, to send funds to partners abroad, to pay co-conspirators, and to pay for trips to collect more cash, including to Las Vegas.",
   doc("sent", PR + "NOVEMBER 13, 2026", "Laundered through cryptocurrency", SRC_S, 8),
   show="Chen admitted the same pipeline. Fraud proceeds laundered through cryptocurrency, to send funds to partners abroad, to pay co-conspirators, and to pay for trips to collect more cash, including to Las Vegas."),
 L("And here is the strangest detail. The couriers filmed themselves. In Wang's sentencing papers, the government said co-conspirators documented themselves retrieving packages, opening them, and counting the money inside.",
   doc("wangsent", PR + "MAY 8, 2026", "“countless such photos and videos”", SRC_WS, 1),
   show="And here is the strangest detail. The couriers filmed themselves. In Wang's sentencing papers, the government said co-conspirators documented themselves retrieving packages, opening them, and counting the money inside."),
 L("Agents seized countless such photos and videos from Wang's phone. Some of those videos, prosecutors say, show the Little Tiger.",
   dict(type="big", kicker="SEIZED FROM THE RINGLEADER'S PHONE", lines=["Countless", "photos|and videos."], src=SRC_WS + " · " + SRC_S),
   show="\"Agents seized countless such photos and videos from Wang's phone.\" Some of those videos, prosecutors say, show the Little Tiger."),
 # III
 L("Chapter three. The package videos.", dict(type="chapter", n="III", title="Package Videos")),
 L("At Chen's sentencing, the prosecutor laid out a timeline. Chen moved to the United States in November twenty twenty-two. By February twenty twenty-three, he was actively participating in the scheme.",
   doc("sent", PR + "NOVEMBER 13, 2026", "“actively participating”", SRC_S, 2),
   show="At Chen's sentencing, the prosecutor laid out a timeline. Chen moved to the United States in November 2022. By February 2023, he was actively participating in the scheme."),
 L("The U.S. Attorney's Office published these slides. February twenty-second, twenty twenty-three. A package, cut open. Hundred-dollar bills, counted by hand.",
   photo("slide_0222", "\"PACKAGE VIDEOS\" · 2/22/2023 · DOJ SENTENCING SLIDE", SRC_SL),
   show="The U.S. Attorney's Office published these slides. February 22, 2023. A package, cut open. $100 bills, counted by hand."),
 L("The next day, February twenty-third. The slide is labeled with a CVS store in San Marcos, California. An express shipping label. And a book, with cash between its pages.",
   photo("slide_0223", "\"PACKAGE VIDEOS\" · 2/23/2023 · DOJ SENTENCING SLIDE", SRC_SL),
   show="The next day, February 23. The slide is labeled with a CVS store in San Marcos, California. An express shipping label. And a book, with cash between its pages."),
 L("May nineteenth. Another box. Another stack of cash.",
   photo("slide_0519", "\"PACKAGE VIDEOS\" · 5/19/2023 · DOJ SENTENCING SLIDE", SRC_SL),
   show="May 19. Another box. Another stack of cash."),
 L("The government said that in some of these videos, Chen was wearing the same distinctive clothing as in the viral YouTube video.",
   doc("sent", PR + "NOVEMBER 13, 2026", "“the same distinctive clothing”", SRC_S, 2)),
 L("In June twenty twenty-three, local police arrested him. Based on publicly filed documents, it did not stop him.",
   doc("sent", PR + "NOVEMBER 13, 2026", "“despite being arrested by local law enforcement”", SRC_S, 3),
   show="In June 2023, local police arrested him. Based on publicly filed documents, it did not stop him."),
 L("A month later came the house in the Los Angeles area. Chen arrived to pick up bulk cash from someone he believed to be an elderly victim. Bingham and Kulik confronted him about working for a scam organization.",
   doc("sent", PR + "NOVEMBER 13, 2026", "“confronted in a viral YouTube video”", SRC_S, 1),
   show="A month later came the house in the Los Angeles area. Chen arrived to pick up bulk cash from someone he believed to be an elderly victim. Bingham and Kulik confronted him about working for a scam organization."),
 L("Trilogy Media posted the video on August nineteenth, twenty twenty-three. Its title: Confronting Scammers With a Fake Funeral. Epic Reactions.",
   dict(type="big", kicker="TRILOGY MEDIA · AUG 19, 2023", lines=["“Confronting Scammers", "With a|Fake Funeral”"], src=SRC_YT + " · " + SRC_CP),
   show="Trilogy Media posted the video on August 19, 2023. Its title: \"CONFRONTING SCAMMERS WITH A FAKE FUNERAL (EPIC REACTIONS).\""),
 L("You might think that being exposed on YouTube would end a cash courier's career. According to the government, it didn't.",
   dict(type="big", lines=["Exposed on YouTube.", "Still|picking up cash."], src=SRC_S)),
 L("His involvement continued through at least December twenty-second, twenty twenty-three, when federal agents encountered him in Upland, California, attempting to retrieve more victim packages.",
   doc("sent", PR + "NOVEMBER 13, 2026", "Upland, California · December 22, 2023", SRC_S, 3),
   show="His involvement continued through at least December 22, 2023, when federal agents encountered him in Upland, California, attempting to retrieve more victim packages."),
 L("In his plea agreement he admitted something else. He frequently relocated to different jurisdictions, including the Southern District of California, to evade law enforcement.",
   doc("sent", PR + "NOVEMBER 13, 2026", "“to evade law enforcement”", SRC_S, 4),
   show="In his plea agreement he admitted something else. He frequently relocated to different jurisdictions, including the Southern District of California, to evade law enforcement."),
 L("So the Little Tiger kept moving. Seven months later, the FBI and its partners moved first.",
   dict(type="timeline", kicker="THE LITTLE TIGER · 2022–2024", at=4, sync=True, events=[
       {"date": "NOV 2022", "text": "moves to the U.S."}, {"date": "FEB 2023", "text": "package videos"},
       {"date": "JUN 2023", "text": "arrested by local police"}, {"date": "JUL 2023", "text": "confronted on YouTube"},
       {"date": "DEC 22, 2023", "text": "federal agents, Upland"}, {"date": "JUL 31, 2024", "text": "federal arrests"}], src=SRC_S + " · " + SRC_I)),
 # IV
 L("Chapter four. The takedown.", dict(type="chapter", n="IV", title="The Takedown")),
 L("In June twenty twenty-four, a federal indictment charged five defendants. On July thirty-first, it was unsealed.",
   doc("ind", PR + "JULY 31, 2024", "“An indictment was unsealed today”", SRC_I, 0),
   show="In June 2024, a federal indictment charged five defendants. On July 31, it was unsealed."),
 L("That morning, about sixty federal, state and local officers arrested four of them, in Los Angeles and Las Vegas, and searched their homes. Jiandong Chen, then of Pomona, California, was one of the four.",
   doc("ind", PR + "JULY 31, 2024", "About 60 officers · four arrests", SRC_I, 1),
   show="That morning, about 60 federal, state and local officers arrested four of them, in Los Angeles and Las Vegas, and searched their homes. Jiandong Chen, then of Pomona, California, was one of the four."),
 L("The charges: conspiracy to commit mail and wire fraud, up to forty years in prison. And conspiracy to launder money, up to twenty.",
   dict(type="list", kicker="CASE NO. 24CR1317-RSH · CHARGES", items=[["40 YRS", "max · conspiracy to commit mail and wire fraud"], ["20 YRS", "max · conspiracy to launder monetary instruments"]], src=SRC_I),
   show="The charges: conspiracy to commit mail and wire fraud, up to 40 years in prison. And conspiracy to launder money, up to 20."),
 L("According to the indictment, the defendants specifically targeted elderly Americans. At that point, those were allegations. Then came the admissions.",
   dict(type="big", kicker="THE INDICTMENT · 2024", lines=["“Specifically", "targeted|elderly Americans”"], src=SRC_I)),
 L("In January twenty twenty-six, the ringleader, Zhao Wang, pleaded guilty. In April, Jiandong Chen did too.",
   dict(type="list", kicker="GUILTY PLEAS", items=[["JAN 15, 2026", "Zhao Wang, aka \"Oscar\" · lead defendant"], ["APR 2, 2026", "Jiandong Chen, aka \"Little Tiger\""]], src=SRC_WP + " · " + SRC_CP),
   show="In January 2026, the ringleader, Zhao Wang, pleaded guilty. In April, Jiandong Chen did too."),
 L("In May, U.S. District Judge Robert Huie sentenced Wang to one hundred fifty-one months. Just over twelve and a half years.",
   dict(type="verdict", kicker="MAY 8, 2026 · ZHAO WANG", stamp="SENTENCED", big="151 months", sub="the ringleader · Judge Robert S. Huie"),
   show="In May, U.S. District Judge Robert Huie sentenced Wang to 151 months. Just over twelve and a half years."),
 L("The judge called the scope of the fraud staggering, and Wang's domestic operation one hundred percent reprehensible.",
   doc("wangsent", PR + "MAY 8, 2026", "“100 percent reprehensible”", SRC_WS, 4),
   show="The judge called the scope of the fraud \"staggering,\" and Wang's domestic operation \"100 percent reprehensible.\""),
 L("And he explained why age mattered. Their vulnerability was not incidental. It was not coincidence. It was how they were selected. It was how they came to be scammed.",
   dict(type="quote", q="Their vulnerability was not incidental. It was not coincidence. It was how they were selected.", case=CASE, doc="JUDGE ROBERT S. HUIE · MAY 8, 2026", cite="As quoted in " + SRC_WS, size=48),
   show="And he explained why age mattered. \"Their vulnerability was not incidental. It was not coincidence. It was how they were selected. It was how they came to be scammed.\""),
 L("At that hearing, the wife and daughter of an eighty-three-year-old victim spoke. They said that within months of being scammed, he lived with suspicion, distrust and resentment. He soon passed away.",
   doc("wangsent", PR + "MAY 8, 2026", "An 83-year-old victim's family", SRC_WS, 3),
   show="At that hearing, the wife and daughter of an 83-year-old victim spoke. They said that within months of being scammed, he lived with suspicion, distrust and resentment. He soon passed away."),
 L("The judge said: it's really hard to fathom the depth of that harm in somebody's last months on this planet.",
   dict(type="quote", q="It's really hard to fathom the depth of that harm in somebody's last months on this planet.", case=CASE, doc="JUDGE ROBERT S. HUIE · MAY 8, 2026", cite="As quoted in " + SRC_WS, size=48),
   show="The judge said: \"It's really hard to fathom the depth of that harm in somebody's last months on this planet.\""),
 L("But this story is bigger than one crew. Because the YouTubers had been hunting these couriers for years.",
   dict(type="big", lines=["Bigger than", "one|crew."], src=SRC_R)),
 # V
 L("Chapter five. The scambaiters.", dict(type="chapter", n="V", title="The Scambaiters")),
 L("In August twenty twenty-five, the same U.S. Attorney's Office announced a separate case. Twenty-eight alleged members of what it called a Chinese organized crime ring, charged in a sixty-five million dollar fraud scheme targeting thousands of seniors.",
   doc("ring65", PR + "AUGUST 27, 2025", "$65 million · 28 charged", SRC_R, 0),
   show="In August 2025, the same U.S. Attorney's Office announced a separate case. Twenty-eight alleged members of what it called a Chinese organized crime ring, charged in a $65 million fraud scheme targeting thousands of seniors."),
 L("Among the victims, prosecutors said, was a ninety-seven-year-old San Diego widow of a Holocaust survivor, who lost her entire life savings.",
   show="Among the victims, prosecutors said, was a 97-year-old San Diego widow of a Holocaust survivor, who lost her entire life savings."),
 L("That investigation began in December twenty twenty, when an elderly victim contacted an express mail carrier. Investigators found eleven packages, holding about one hundred thirty-five thousand dollars in cash, each addressed to a fake name.",
   doc("final65", PR + "OCTOBER 26, 2026", "11 packages · about $135,000", SRC_F, 2),
   show="That investigation began in December 2020, when an elderly victim contacted an express mail carrier. Investigators found 11 packages, holding about $135,000 in cash, each addressed to a fake name."),
 L("And the Justice Department credited YouTube. Scammer Payback, run by a YouTuber known as Pierogi, teamed up with Trilogy Media for coordinated stings. Videos they posted in twenty twenty and twenty twenty-one helped law enforcement identify three of the defendants.",
   doc("ring65", PR + "AUGUST 27, 2025", "“helped law enforcement identify”", SRC_R, 3),
   show="And the Justice Department credited YouTube. Scammer Payback, run by a YouTuber known as Pierogi, teamed up with Trilogy Media for coordinated stings. Videos they posted in 2020 and 2021 helped law enforcement identify three of the defendants."),
 L("In one sting, according to a government memo, scammers told Pierogi to send cash to a Hans Bum, at an address in South San Francisco. Trilogy Media delivered a decoy package there, and confronted the man who received it.",
   doc("ring65", PR + "AUGUST 27, 2025", "The decoy package", SRC_R, 2),
   show="In one sting, according to a government memo, scammers told Pierogi to send cash to a \"Hans Bum,\" at an address in South San Francisco. Trilogy Media delivered a decoy package there, and confronted the man who received it."),
 L("He turned out to be Zhiyi Zhang. The government says he revealed his real identity and admitted on camera to receiving packages for money. Federal agents arrested him at Los Angeles International Airport in August twenty twenty-five.",
   show="He turned out to be Zhiyi Zhang. The government says he revealed his real identity and admitted on camera to receiving packages for money. Federal agents arrested him at Los Angeles International Airport in August 2025."),
 L("The U.S. Attorney, Adam Gordon, put it this way. Not all heroes wear capes. Some have YouTube channels.",
   dict(type="quote", q="Not all heroes wear capes. Some have YouTube channels.", case=CASE, doc="U.S. ATTORNEY ADAM GORDON · AUG 2025", cite=SRC_R, size=58),
   show="The U.S. Attorney, Adam Gordon, put it this way: \"Not all heroes wear capes. Some have YouTube channels.\""),
 L("The ring rented short-term homes in what prosecutors called a hub-and-spoke pattern. A hub for about a week, smaller spokes nearby for shorter stays, then move and repeat.",
   doc("final65", PR + "OCTOBER 26, 2026", "“a hub-and-spoke pattern”", SRC_F, 3),
   show="The ring rented short-term homes in what prosecutors called a \"hub-and-spoke pattern.\" A hub for about a week, smaller spokes nearby for shorter stays, then move and repeat."),
 L("By late October twenty twenty-six, the last of the twenty-five arrested defendants had admitted their crimes. Three charged defendants are still fugitives.",
   doc("final65", PR + "OCTOBER 26, 2026", "“The last of 25 defendants”", SRC_F, 0),
   show="By late October 2026, the last of the 25 arrested defendants had admitted their crimes. Three charged defendants are still fugitives."),
 L("In their plea agreements, Zhiyi Zhang and another defendant, Huajian Chen, admitted being in YouTube videos in which they were confronted about their involvement.",
   doc("final65", PR + "OCTOBER 26, 2026", "“admitted to being in YouTube videos”", SRC_F, 1)),
 L("Which brings us back to San Diego, and the Little Tiger's day in court.",
   dict(type="big", lines=["Back to", "San Diego.|November 13."], src=SRC_S)),
 # VI
 L("Chapter six. The sentence.", dict(type="chapter", n="VI", title="The Sentence")),
 L("November thirteenth, twenty twenty-six. Ashton Bingham and Art Kulik, the YouTubers from the video, attended the hearing.",
   doc("sent", PR + "NOVEMBER 13, 2026", "“both of whom attended today’s sentencing hearing”", SRC_S, 1),
   show="November 13, 2026. Ashton Bingham and Art Kulik, the YouTubers from the video, attended the hearing."),
 L("Chen had pleaded guilty to conspiracy to commit mail and wire fraud, and conspiracy to launder money. In his plea agreement, he admitted his time in the conspiracy involved more than nine point five million dollars in victim losses.",
   doc("sent", PR + "NOVEMBER 13, 2026", "“over $9.5 million in victim loss”", SRC_S, 4),
   show="Chen had pleaded guilty to conspiracy to commit mail and wire fraud, and conspiracy to launder money. In his plea agreement, he admitted his time in the conspiracy involved more than $9.5 million in victim losses."),
 L("Before pronouncing the sentence, Judge Huie said Chen engaged in extensive course of conduct in stealing from some of the most vulnerable people here in the United States.",
   doc("sent", PR + "NOVEMBER 13, 2026", "Judge Robert S. Huie", SRC_S, 6),
   show="Before pronouncing the sentence, Judge Huie said Chen \"engaged in extensive course of conduct in stealing from some of the most vulnerable people here in the United States.\""),
 L("The money taken, the judge said, was more than just money. It included people's self-respect, their dignity, trust with their family members.",
   dict(type="quote", q="people's self-respect, their dignity, trust with their family members", case=CASE, doc="JUDGE ROBERT S. HUIE · NOV 13, 2026", cite="As quoted in " + SRC_S, size=52),
   show="The money taken, the judge said, was \"more than just money.\" It included \"people's self-respect, their dignity, trust with their family members.\""),
 L("What the victims went through, he said, involved desperation in the last years of somebody's life, and was a tragic thing to suffer.",
   doc("sent", PR + "NOVEMBER 13, 2026", "“a tragic thing to suffer”", SRC_S, 7),
   show="What the victims went through, he said, involved \"desperation in the last years of somebody's life,\" and was a \"tragic thing to suffer.\""),
 L("Then the sentence. Seventy-eight months in federal prison. Six and a half years.",
   dict(type="verdict", kicker="NOVEMBER 13, 2026 · JIANDONG CHEN", stamp="SENTENCED", big="78 months", sub="6½ years in federal prison · Judge Robert S. Huie"),
   show="Then the sentence. 78 months in federal prison. Six and a half years."),
 L("These victims weren't foolish, said U.S. Attorney Adam Gordon. They were lied to and exploited by a sophisticated criminal network.",
   dict(type="quote", q="These victims weren't foolish. They were lied to and exploited by a sophisticated criminal network.", case=CASE, doc="U.S. ATTORNEY ADAM GORDON · NOV 13, 2026", cite=SRC_S, size=50),
   show="\"These victims weren't foolish,\" said U.S. Attorney Adam Gordon. \"They were lied to and exploited by a sophisticated criminal network.\""),
 L("And he thanked the YouTubers by name. Stopping fraud takes an online village, he said. With friends to our cause like Ash and Art, we can do even more.",
   doc("sent", PR + "NOVEMBER 13, 2026", "“Stopping fraud takes an online village”", SRC_S, 5),
   show="And he thanked the YouTubers by name. \"Stopping fraud takes an online village,\" he said. \"With friends to our cause like Ash and Art, we can do even more.\""),
 L("Put the sentences side by side. The ringleader, Zhao Wang: one hundred fifty-one months. The Little Tiger: seventy-eight. In the sixty-five million dollar ring, two defendants, Na Rong and Bing Shen, have received seventy-eight and seventy months.",
   dict(type="bars", kicker="SENTENCES SO FAR · S.D. CAL.", title="Months in federal prison", sync=True,
        items=[{"label": "ZHAO WANG · RINGLEADER", "value": 151, "display": "151"}, {"label": "JIANDONG CHEN · \"LITTLE TIGER\"", "value": 78, "display": "78"},
               {"label": "NA RONG · $65M RING", "value": 78, "display": "78"}, {"label": "BING SHEN · $65M RING", "value": 70, "display": "70"}], src=SRC_WS + " · " + SRC_S + " · " + SRC_F),
   show="Put the sentences side by side. The ringleader, Zhao Wang: 151 months. The Little Tiger: 78. In the $65 million ring, two defendants, Na Rong and Bing Shen, have received 78 and 70 months."),
 L("Back in twenty twenty-four, the U.S. Attorney's Office gave one piece of advice. Use caution and consult with others before sending money to strangers you know only through phone calls, texts, or a computer.",
   doc("ind", PR + "JULY 31, 2024", "“consult with others before sending money”", SRC_I, 4),
   show="Back in 2024, the U.S. Attorney's Office gave one piece of advice: \"use caution and consult with others before sending money to strangers they know only through phone calls, texts, or a computer.\""),
 L("If you or someone you know is sixty or older and has been a victim of financial fraud, the National Elder Fraud Hotline is one eight three three, three seven two, eight three one one.",
   dict(type="stat", kicker="NATIONAL ELDER FRAUD HOTLINE", value="1-833-FRAUD-11", label="1-833-372-8311 · age 60+ · or report at ic3.gov", src=SRC_I),
   show="If you or someone you know is 60 or older and has been a victim of financial fraud, the National Elder Fraud Hotline is 1-833-372-8311."),
 L("So here is the case in one line. A fake refund. A box of cash. A fake ID. And a YouTube video that ended up in a federal courtroom.",
   dict(type="list", kicker="THE CASE IN NUMBERS", items=[["$27M+", "lost by more than 2,000 elderly victims, 2021–2023"], ["$9.5M+", "in victim losses tied to Chen's time in the conspiracy"], ["18%", "the ringleader's cut, as he admitted"], ["1.4M+", "views of the Trilogy Media video"], ["78 months", "Jiandong Chen's sentence, Nov 13, 2026"]], src=SRC_S + " · " + SRC_WP + " · " + SRC_YT)),
 L("Would the people you love recognize a refund scam? Tell me in the comments. This is SWORN. Real trials. Real evidence. The verdict.", dict(type="end")),
]

# --- Fact-check FIXes (factcheck.md, independent agent, 36 fixes) ---
def setline(prefix, say=None, show=None, scene=None):
    m = [l for l in lines if l["say"].startswith(prefix)]
    assert len(m) == 1, prefix
    l = m[0]
    if say: l["say"] = say
    if show: l["show"] = show
    elif say and "show" in l: l["show"] = say
    if scene: l["scene"].update(scene)
setline("In July twenty twenty-three, a man", say="In July twenty twenty-three, a man went to a house in the Los Angeles area to pick up bulk cash from someone he believed was an elderly fraud victim.", show="In July 2023, a man went to a house in the Los Angeles area to pick up bulk cash from someone he believed was an elderly fraud victim.")
setline("Court records list the man", say="Federal prosecutors identify the man as Jiandong Chen, also known as Little Tiger.", show="Federal prosecutors identify the man as Jiandong Chen, also known as \"Little Tiger.\"")
setline("This is how the scam worked", say="This is how the scam worked, how the cash moved, and how a YouTube channel ended up in a federal sentencing hearing.")
setline("It usually started on a screen.", say="It could start with a phone call, an email, or a pop-up ad. According to the Justice Department, victims received unsolicited phone calls, emails and pop-up ads, telling them to call a phone number.")
setline("This is not a small problem.", say="This is not a small problem. According to the FBI, Americans sixty and older reported more than seven point seven billion dollars in losses in twenty twenty-five alone.", show="This is not a small problem. According to the FBI, Americans 60 and older reported more than $7.7 billion in losses in 2025 alone.", scene={"kicker": "FBI · AGE 60+ · 2025", "src": "FBI figures for 2025, as reported by Bitdefender (May 19, 2026)"})
setline("In this case, one of the most frequent", scene={"kicker": "ONE OF THE MOST FREQUENT SCAMS"})
setline("The victim was told they were owed", say="The victim was told they were owed a small refund, for example, from a retailer, for an alleged unauthorized charge. While pretending to process it, the caller would accidentally over-refund them.", show="The victim was told they were owed a small refund, for example, from a retailer, for an alleged unauthorized charge. While pretending to process it, the caller would \"accidentally\" over-refund them.")
setline("In his plea agreement, Chen admitted exactly", say="In his plea agreement, Chen admitted using fraudulent driver's licenses or IDs, matching the fictitious recipient names, to retrieve the victim packages containing bulk cash.")
setline("His partners overseas supplied", scene={"value": "18%+", "label": "his cut (\"upwards of 18%\") — the rest went out in crypto"})
setline("And here is the strangest detail.", say="And here is the strangest detail. According to prosecutors, the couriers filmed themselves. In Wang's sentencing papers, the government said co-conspirators documented themselves retrieving packages, opening them, and counting the money inside.")
setline("Agents seized countless", say="Agents seized countless such photos and videos from Wang's phone. And at Chen's own sentencing, prosecutors pointed to numerous videos of him doing the same.", show="\"Agents seized countless such photos and videos from Wang's phone.\" And at Chen's own sentencing, prosecutors pointed to numerous videos of him doing the same.")
setline("The government said that in some of these videos", scene={"hl": hl("sent", 9)})
setline("In June twenty twenty-three, local police", say="In June twenty twenty-three, local law enforcement arrested him. Based on publicly filed documents, it did not stop him.", show="In June 2023, local law enforcement arrested him. Based on publicly filed documents, it did not stop him.")
[l for l in lines if l["say"].startswith("So the Little Tiger kept moving.")][0]["scene"]["events"][2]["text"] = "arrested by local law enforcement"
setline("A month later came the house", say="The next month came the house in the Los Angeles area. Chen arrived to pick up bulk cash from someone he believed to be an elderly victim. Bingham and Kulik confronted him about working for a scam organization.")
setline("And he explained why age mattered.", scene={"case": "UNITED STATES v. WANG"})
setline("The judge said: it's really hard", scene={"case": "UNITED STATES v. WANG"})
setline("But this story is bigger", say="But this story is bigger than one crew. Because the same YouTubers had been confronting cash couriers for years.")
setline("And the Justice Department credited YouTube.", say="And the Justice Department credited YouTube. A YouTuber known as Pierogi, from Scammer Payback, teamed up with Trilogy Media for coordinated stings. Videos they posted in twenty twenty and twenty twenty-one helped law enforcement identify three of the defendants.", show="And the Justice Department credited YouTube. A YouTuber known as Pierogi, from Scammer Payback, teamed up with Trilogy Media for coordinated stings. Videos they posted in 2020 and 2021 helped law enforcement identify three of the defendants.")
setline("The U.S. Attorney, Adam Gordon, put it", scene={"case": "THE $65 MILLION RING CASE"})
setline("The ring rented short-term homes", say="In their plea agreements, defendants in that ring admitted booking short-term rentals in a hub-and-spoke pattern. A hub for about a week, spokes nearby for shorter stays, then move and repeat.", show="In their plea agreements, defendants in that ring admitted booking short-term rentals in a \"hub-and-spoke pattern.\" A hub for about a week, spokes nearby for shorter stays, then move and repeat.")
setline("By late October twenty twenty-six", say="By late October twenty twenty-six, the last of the twenty-five arrested defendants had admitted their crimes. Three charged defendants remained fugitives.", show="By late October 2026, the last of the 25 arrested defendants had admitted their crimes. Three charged defendants remained fugitives.")
setline("And he thanked the YouTubers", say="And he named the YouTubers. Stopping fraud takes an online village, he said. With friends to our cause like Ash and Art, we can do even more.", show="And he named the YouTubers. \"Stopping fraud takes an online village,\" he said. \"With friends to our cause like Ash and Art, we can do even more.\"")
setline("Put the sentences side by side.", say="Put the sentences side by side. The ringleader, Zhao Wang: one hundred fifty-one months. The Little Tiger: seventy-eight. And as of late October, in the related sixty-five million dollar ring, one defendant, Bing Shen, had been sentenced to seventy months.", show="Put the sentences side by side. The ringleader, Zhao Wang: 151 months. The Little Tiger: 78. And as of late October, in the related $65 million ring, one defendant, Bing Shen, had been sentenced to 70 months.",
        scene={"kicker": "SENTENCES ANNOUNCED · S.D. CAL.", "items": [{"label": "ZHAO WANG · RINGLEADER", "value": 151, "display": "151"}, {"label": "JIANDONG CHEN · \"LITTLE TIGER\"", "value": 78, "display": "78"}, {"label": "BING SHEN · $65M RING (AS OF OCT 26)", "value": 70, "display": "70"}]})
setline("Back in twenty twenty-four", say="Back in twenty twenty-four, then-U.S. Attorney Tara McGrath gave one piece of advice. Use caution and consult with others before sending money to strangers you know only through phone calls, texts, or a computer.", show="Back in 2024, then-U.S. Attorney Tara McGrath gave one piece of advice: \"use caution and consult with others before sending money to strangers they know only through phone calls, texts, or a computer.\"")
[l for l in lines if l["say"].startswith("So here is the case in one line.")][0]["scene"]["items"][2] = ["18%+", "the ringleader's cut (\"upwards of 18%\"), as he admitted"]
from panfix import fix
fix(lines, "long")
spec = {"label": "SWORN · CASE 015", "lines": lines}
if __name__ == "__main__":
    json.dump(spec, open(os.path.join(HERE, "episode.json"), "w"), indent=1, ensure_ascii=False)
    print(len(lines), "lines,", sum(len(l["say"].split()) for l in lines), "words")
