import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
HL = json.load(open(os.path.join(HERE, "hl.json")))
def hl(name, i=0):
    a, b = HL[name][i]
    return [0.0, a, 1.0, round(b - a, 4)]
CASE = "UNITED STATES v. MILTON"
SRC_GM = "Gov't Sentencing Memorandum, U.S. v. Milton, S1 21 Cr. 478 (ER), Dkt. 315 (S.D.N.Y. Dec 12, 2023)"
SRC_OP = "Opinion and Order, U.S. v. Milton, Dkt. 286 (S.D.N.Y. Aug 30, 2023)"
SRC_OP2 = "Opinion & Order (forfeiture), U.S. v. Milton, Dkt. 334 (S.D.N.Y. Feb 26, 2024)"
SRC_JDG = "Judgment, U.S. v. Milton, Dkt. 327 (S.D.N.Y. Jan 17, 2024)"
SRC_TR = "Sentencing transcript, U.S. v. Milton, Dkt. 322 (S.D.N.Y. Dec 18, 2023)"
SRC_REST = "Gov't restitution letter, U.S. v. Milton, Dkt. 361 (S.D.N.Y. Mar 14, 2025)"
SRC_PARD = "Executive Grant of Clemency (Mar 2025), Exhibit A to Dkt. 362, U.S. v. Milton"
SRC_DEF = "Joint status letter, U.S. v. Milton, Dkt. 362 (Apr 1, 2025)"
SRC_BAIL = "Order Exonerating Bail, U.S. v. Milton, Dkt. 365 (S.D.N.Y. Apr 7, 2025)"
SRC_IND = "Indictment, U.S. v. Milton, 21 Cr. 478, Dkt. 1 (S.D.N.Y. Jul 28, 2021)"
SRC_SEC = "SEC v. Milton, No. 1:21-cv-06445, Complaint (S.D.N.Y. Jul 29, 2021) — allegations"
SRC_SECD = "SEC v. Milton, Joint Stipulation to Dismiss, Dkt. 53 (S.D.N.Y. Sep 11, 2025)"
SRC_DOJ = "U.S. Attorney's Office, S.D.N.Y., press release (Dec 18, 2023)"
SRC_AP1 = "Associated Press (Oct 14, 2022)"
SRC_AP2 = "Associated Press (Mar 28, 2025)"
SRC_EW = "eWEEK, citing The Wall Street Journal and TechCrunch (Mar 19, 2026)"
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
def doc(img, kicker, title, src, i=0, pan=None):
    return dict(type="doc", img=f"img/{img}.jpg", pan=pan or [0.0, 0.1], hl=hl(img, i), kicker=kicker, title=title, src=src)
GM = "GOV'T SENTENCING MEMORANDUM"
lines = [
 # COLD OPEN
 L("The Nikola truck in the famous video was not driving. It was rolling down a hill. And that video became evidence in a federal fraud trial.",
   dict(type="big", kicker="THE NIKOLA ONE · 2018", lines=["Not driving.", "Rolling|downhill."], src=SRC_DOJ)),
 L("Its founder, Trevor Milton, had written that this would be the first time anyone has seen the Nikola truck move.",
   dict(type="quote", q="the first time anyone has seen the Nikola truck move", case=CASE, doc="TREVOR MILTON · E-MAIL (GX 929)", cite="As quoted in " + SRC_GM, size=56),
   show="Its founder, Trevor Milton, had written that this would be \"the first time anyone has seen the Nikola truck move.\""),
 L("In twenty twenty-two, a jury convicted Milton of fraud. A judge gave him four years. He never went to prison. This is the paper trail, from the hill to the verdict, and to the pardon.",
   dict(type="title", kicker="SWORN · CASE 013 · THE VERDICT", title="The Truck That|Rolled Downhill", sub="United States v. Trevor Milton · S.D.N.Y. · 2022"),
   show="In 2022, a jury convicted Milton of fraud. A judge gave him four years. He never went to prison. This is the paper trail, from the hill to the verdict, and to the pardon."),
 # I
 L("Chapter one. The unveiling.", dict(type="chapter", n="I", title="The Unveiling")),
 L("Trevor Milton founded Nikola to build trucks that would run on hydrogen and batteries. On December first and second, twenty sixteen, he unveiled a prototype semi-truck, the Nikola One, at an event broadcast on the internet.",
   doc("gm_6", GM + " · PAGE 4", "The Nikola One unveiling, Dec 1–2, 2016", SRC_GM, 0),
   show="Trevor Milton founded Nikola to build trucks that would run on hydrogen and batteries. On December 1 and 2, 2016, he unveiled a prototype semi-truck, the Nikola One, at an event broadcast on the internet."),
 L("On stage, according to the SEC's complaint, he said the truck fully functions and works, which is really incredible.",
   doc("sec_17", "SEC v. MILTON · COMPLAINT · ALLEGATIONS", "“fully functions and works which is really incredible”", SRC_SEC, 0),
   show="On stage, according to the SEC's complaint, he said the truck \"fully functions and works which is really incredible.\""),
 L("Prosecutors told the court what the trial showed. The Nikola One was neither functioning nor even designed to be hydrogen-powered, and it was missing critical parts.",
   doc("gm_6", GM, "“missing critical parts”", SRC_GM, 1),
   show="Prosecutors told the court what the trial showed. The Nikola One was \"neither functioning nor even designed to be hydrogen-powered and was missing critical parts.\""),
 L("Even the screens inside the cab. The infotainment screens Milton bragged about, the memo says, were static mockups saved to laptop lock screens.",
   doc("gm_6", GM, "“static mockups saved to laptop lock screens”", SRC_GM, 2),
   show="Even the screens inside the cab. The infotainment screens Milton bragged about, the memo says, were \"nothing more than static mockups saved to laptop lock screens.\""),
 L("The SEC alleged that Nikola's chief engineer had warned Milton the truck would not be functioning at the event unless it was postponed. Milton went ahead.",
   doc("sec_17", "SEC v. MILTON · COMPLAINT · ALLEGATIONS", "The engineer's warning", SRC_SEC, 0),
   show="The SEC alleged that Nikola's chief engineer had warned Milton the truck would not be functioning at the event unless it was postponed. Milton went ahead."),
 # II
 L("Chapter two. The hill.", dict(type="chapter", n="II", title="The Hill")),
 L("More than a year later, the Nikola One appeared in a commercial shoot for a trucking-parts company. It still could not move under its own power.",
   doc("sec_20", "SEC v. MILTON · COMPLAINT · ALLEGATIONS", "“could not run under its own power”", SRC_SEC, 0),
   show="More than a year later, the Nikola One appeared in a commercial shoot for a trucking-parts company. It still could not move under its own power."),
 L("So, according to the SEC, it was towed to the top of an inclined stretch of road, and filmed rolling down. Three times.",
   doc("sec_20", "SEC v. MILTON · COMPLAINT · ALLEGATIONS", "Towed to the top. Filmed rolling down.", SRC_SEC, 0),
   show="So, according to the SEC, it was \"towed to the top of an inclined stretch of road and then filmed rolling down the incline.\" Three times."),
 L("When Milton saw the company's first cut, prosecutors wrote, he became irate. The truck was not going down the road as we talked about, which, he wrote, was the reason he approved it.",
   doc("gm_7", GM + " · PAGE 5", "“going down the road as we talked about”", SRC_GM, 0),
   show="When Milton saw the company's first cut, prosecutors wrote, he \"became irate.\" The truck was not \"going down the road as we talked about,\" which, he wrote, \"was the reason why I approved it.\""),
 L("He wanted the footage for Nikola. This will be the first time anyone has seen the Nikola truck move, he wrote, so it could get millions of views on our YouTube channel.",
   dict(type="quote", q="so it could get millions of views on our youtube channel.", case=CASE, doc="TREVOR MILTON · E-MAIL (GX 929)", cite="As quoted in " + SRC_GM, size=54),
   show="He wanted the footage for Nikola. \"[T]his will be the first time anyone has seen the Nikola truck move,\" he wrote, \"so it could get millions of views on our youtube channel.\""),
 L("Milton then had a Nikola employee cut the footage into what looked like the truck driving under its own power. Prosecutors called it the In Motion video.",
   doc("gm_7", GM, "The “In Motion Video”", SRC_GM, 2),
   show="Milton then had a Nikola employee cut the footage into what looked like the truck driving under its own power. Prosecutors called it the \"In Motion Video.\""),
 L("On January twenty-fifth, twenty eighteen, it went up on Nikola's Twitter and Facebook. The caption, which the SEC says Milton drafted: Behold, the Nikola One in motion.",
   doc("sec_20", "SEC v. MILTON · COMPLAINT · ALLEGATIONS", "“Behold, the Nikola One in motion.”", SRC_SEC, 1),
   show="On January 25, 2018, it went up on Nikola's Twitter and Facebook. The caption, which the SEC says Milton drafted: \"Behold, the Nikola One in motion.\""),
 L("The video did not say the truck was rolling downhill. According to the SEC, it stayed up on Nikola's accounts until at least September twenty twenty.",
   dict(type="big", kicker="SEC v. MILTON · COMPLAINT", lines=["Posted Jan 2018.", "Up until at least|Sept 2020."], src=SRC_SEC),
   show="The video did not say the truck was rolling downhill. According to the SEC, it stayed up on Nikola's accounts until at least September 2020."),
 # III
 L("Chapter three. Seven billion on paper.", dict(type="chapter", n="III", title="Seven Billion on Paper")),
 L("In June twenty twenty, Nikola went public by merging with a blank-check company, a SPAC. Milton became executive chairman and its largest shareholder.",
   dict(type="stat", kicker="JUNE 2020", value="Public", label="Nikola merges with a SPAC; Milton is executive chairman", src=SRC_OP + " · " + SRC_GM),
   show="In June 2020, Nikola went public by merging with a blank-check company, a SPAC. Milton became executive chairman and its largest shareholder."),
 L("At one point, prosecutors wrote, Nikola's market value was higher than Ford's, though Nikola had never produced a vehicle for sale.",
   doc("gm_pre", GM + " · PAGE 1", "Worth more than Ford", SRC_GM, 0),
   show="At one point, prosecutors wrote, Nikola's market capitalization was \"higher than that of Ford's, despite Nikola never having produced a vehicle for sale at the time.\""),
 L("And Milton talked. On social media, on television, on podcasts. Prosecutors said he aimed at retail investors: individual, non-professional investors.",
   doc("ind_1", "INDICTMENT · 21 CR. 478", "“so-called ‘retail investors’”", SRC_IND, 0),
   show="And Milton talked. On social media, on television, on podcasts. Prosecutors said he aimed at \"retail investors\": individual, non-professional investors."),
 L("The pickup truck, the Badger. Milton claimed Nikola engineered it from the ground up. In fact, the memo says, the prototypes were reworked Ford trucks, and production versions would be GM trucks with Nikola branding.",
   doc("gm_9", GM + " · PAGE 6", "Reworked Ford trucks", SRC_GM, 0),
   show="The pickup truck, the Badger. Milton claimed Nikola engineered it \"from the ground up.\" In fact, the memo says, the prototypes were reworked Ford trucks, and production versions would be \"GM trucks with Nikola branding.\""),
 L("Hydrogen. Milton claimed Nikola was producing it, below four dollars a kilogram. According to the government, it was not producing hydrogen at all.",
   doc("gm_9", GM, "Producing hydrogen? “when it was not”", SRC_GM, 1),
   show="Hydrogen. Milton claimed Nikola was producing it, below $4 a kilogram. According to the government, it was not producing hydrogen at all."),
 L("And orders. In one interview quoted by the SEC, Milton spoke of billions and billions of dollars with the contracts. Most reservations, the SEC said, could be cancelled.",
   doc("gm_9", GM, "“That too was false.”", SRC_GM, 2),
   show="And orders. In one interview quoted by the SEC, Milton spoke of \"billions and billions of dollars with the contracts.\" Most reservations, the SEC said, could be cancelled."),
 L("His own executives, prosecutors wrote, warned him over and over again not to mischaracterize the business. He kept going.",
   doc("gm_9", GM, "“warned over and over again”", SRC_GM, 3),
   show="His own executives, prosecutors wrote, \"warned him over and over again\" not to mischaracterize the business. He kept going."),
 L("Meanwhile, the value of Milton's Nikola holdings rose from about one point one billion dollars in March twenty twenty to a peak of about seven point three billion in June.",
   doc("gm_7", GM, "$1.099 billion → $7.303 billion", SRC_GM, 3),
   show="Meanwhile, the value of Milton's Nikola holdings rose from about $1.1 billion in March 2020 to a peak of about $7.3 billion in June."),
 L("His chief financial officer testified that Milton said one of his goals was to be in the top one hundred of the Forbes list of the wealthiest Americans, by raising Nikola's stock price.",
   doc("gm_7", GM, "“to be in the top 100”", SRC_GM, 4),
   show="His chief financial officer testified that Milton said \"one of [his] goal[s] was to be in the top 100\" of the Forbes list of the wealthiest Americans, by raising Nikola's stock price."),
 L("He sold about one hundred million dollars of stock around the merger. By September, the memo says, he had spent about eighty-three and a half million, including on an airplane, a hangar, and an estate in Turks and Caicos.",
   doc("gm_8", GM + " · PAGE 5", "$83.5 million spent", SRC_GM, 1),
   show="He sold about $100 million of stock around the merger. By September, the memo says, he had spent about $83.5 million, including on an airplane, a hangar, and an estate in Turks & Caicos."),
 L("He also used stock options to buy a Utah ranch. Eight and a half million in cash, plus options then valued at eight and a half million. The seller was persuaded, prosecutors said, by Milton's false claims about Nikola.",
   doc("gm_10", GM + " · PAGE 8", "The Wasatch Creeks Ranch", SRC_GM, 0),
   show="He also used stock options to buy a Utah ranch: $8.5 million in cash, plus options then valued at $8.5 million. The seller was persuaded, prosecutors said, by Milton's false claims about Nikola."),
 # IV
 L("On a call in April twenty twenty, the seller and his son asked about Nikola's business. Milton told them, according to prosecutors: we've already begun procuring power and planning stations. None of that was true, the government said.",
   dict(type="quote", q="we've already begun procuring power and planning stations", case=CASE, doc="TREVOR MILTON · CALL, APRIL 2020 (GX 1400-T)", cite="As quoted in " + SRC_GM, size=52),
   show="On a call in April 2020, the seller and his son asked about Nikola's business. Milton told them, according to prosecutors: \"we've already begun procuring power and planning stations.\" \"None of these claims were true,\" the government said."),
 L("Chapter four. The report.", dict(type="chapter", n="IV", title="The Report")),
 L("On September tenth, twenty twenty, the short-seller firm Hindenburg Research published a report, in the government's words, detailing evidence of Milton's fraud.",
   dict(type="stat", kicker="SEPTEMBER 10, 2020", value="Hindenburg", label="Short-seller report on Nikola", src=SRC_GM),
   show="On September 10, 2020, the short-seller firm Hindenburg Research published a report, in the government's words, \"detailing evidence of the defendant's fraud.\""),
 L("Nikola was worth sixteen billion dollars on September ninth. Two days later, twelve point one three billion.",
   dict(type="bars", kicker="NIKOLA MARKET CAPITALIZATION · SEPT 2020", title="Billions of dollars", items=[{"label": "Sept 9", "value": 16, "display": "$16 billion"}, {"label": "Sept 10", "value": 14.19, "display": "$14.19 billion"}, {"label": "Sept 11", "value": 12.13, "display": "$12.13 billion"}], src=SRC_GM),
   show="Nikola was worth $16 billion on September 9. Two days later, $12.13 billion."),
 L("On September twenty-first, Nikola announced that Milton had resigned.",
   dict(type="timeline", kicker="UNITED STATES v. MILTON", events=[{"date": "Sept 10, 2020", "text": "Hindenburg report"}, {"date": "Sept 21, 2020", "text": "Resignation announced"}, {"date": "Jul 28, 2021", "text": "Indictment filed"}, {"date": "Sept 13, 2022", "text": "Trial begins"}], at=1, src=SRC_GM + " · " + SRC_OP),
   show="On September 21, Nikola announced that Milton had resigned."),
 L("On July twenty-eighth, twenty twenty-one, prosecutors in Manhattan filed the indictment. Securities fraud and wire fraud. The SEC sued him the next day.",
   doc("ind_1", "SEALED INDICTMENT · 21 CR. 478", "United States v. Trevor Milton", SRC_IND, 0),
   show="On July 28, 2021, prosecutors in Manhattan filed the indictment: securities fraud and wire fraud. The SEC sued him the next day."),
 L("Milton pleaded not guilty.",
   dict(type="timeline", kicker="UNITED STATES v. MILTON", events=[{"date": "Sept 10, 2020", "text": "Hindenburg report"}, {"date": "Sept 21, 2020", "text": "Resignation announced"}, {"date": "Jul 28, 2021", "text": "Indictment filed"}, {"date": "Sept 13, 2022", "text": "Trial begins"}], at=2, src=SRC_OP + " · " + SRC_AP1)),
 # V
 L("Chapter five. The verdict.", dict(type="chapter", n="V", title="The Verdict")),
 L("The trial began on September thirteenth, twenty twenty-two, and ran a month. The evidence, the judge later wrote, focused on four big categories of alleged lies.",
   doc("op_5", "OPINION AND ORDER · S.D.N.Y.", "“four big categories”", SRC_OP, 0),
   show="The trial began on September 13, 2022, and ran a month. The evidence, the judge later wrote, focused on \"four big categories\" of alleged lies."),
 L("Hydrogen production and its cost. Whether the Nikola One worked in twenty sixteen. Whether pre-orders were binding. And the Badger, built from the ground up or not.",
   doc("op_5", "OPINION AND ORDER · S.D.N.Y.", "Hydrogen · Nikola One · orders · Badger", SRC_OP, 1),
   show="Hydrogen production and its cost. Whether the Nikola One worked in 2016. Whether pre-orders were binding. And the Badger, built \"from the ground up\" or not."),
 L("The prosecutor's summary to the jury, as reported by the Associated Press: The lies. That is what this case is about. The defense told jurors there was a stunning lack of evidence.",
   dict(type="quote", q="The lies - that is what this case is about.", case=CASE, doc="PROSECUTOR MATTHEW PODOLSKY · 2022", cite="As quoted by " + SRC_AP1, size=58),
   show="The prosecutor's summary to the jury, as reported by the Associated Press: \"The lies - that is what this case is about.\" The defense told jurors there was \"a stunning lack of evidence.\""),
 L("On October fourteenth, twenty twenty-two, after about five hours of deliberation, the jury returned its verdict.",
   dict(type="stat", kicker="MANHATTAN · OCTOBER 14, 2022", value="≈ 5 hours", label="Jury deliberations", src=SRC_AP1)),
 L("Guilty on three of four counts. One count of securities fraud, and two of wire fraud. One for investors. One for the ranch.",
   dict(type="verdict", kicker="S.D.N.Y. · OCTOBER 14, 2022", stamp="GUILTY", big="3 of 4 counts", sub="United States v. Trevor Milton"),
   show="Guilty on three of four counts: one count of securities fraud, and two of wire fraud. One for investors. One for the ranch."),
 L("Not guilty on the fourth, a second securities-fraud charge under a different statute.",
   doc("jdg_1", "JUDGMENT IN A CRIMINAL CASE", "Not guilty: Count 2", SRC_JDG, 1)),
 L("Milton asked for a new trial, arguing the jury was wrongly instructed and that one juror was biased. In August twenty twenty-three, the judge denied the motions.",
   doc("op_1", "OPINION AND ORDER · AUG 30, 2023", "Motions DENIED", SRC_OP, 0),
   show="Milton asked for a new trial, arguing the jury was wrongly instructed and that one juror was biased. In August 2023, the judge denied the motions."),
 L("Sentencing came on December eighteenth, twenty twenty-three. By the government's math, investors lost between six hundred sixty and six hundred seventy-four million dollars, and the guidelines called for sixty years.",
   doc("gm_pre", GM, "Guidelines: 60 years", SRC_GM, 1),
   show="Sentencing came on December 18, 2023. By the government's math, investors lost between $660.8 million and $673.6 million, and the guidelines called for 60 years."),
 L("The defense said the loss was zero, and asked for probation. Prosecutors backed the probation office's recommendation: eleven years.",
   dict(type="bars", kicker="SENTENCING · DEC 18, 2023", title="What each side asked", items=[{"label": "Guidelines (gov't calc.)", "value": 720, "display": "60 years"}, {"label": "Probation office / gov't", "value": 132, "display": "11 years"}, {"label": "Defense", "value": 4, "display": "Probation"}], src=SRC_GM),
   show="The defense said the loss was zero, and asked for probation. Prosecutors backed the probation office's recommendation: 11 years."),
 L("The judge sided with the government on loss. There was real loss to real people, he said, who listened to Mr. Milton and invested in Nikola because of what they heard from him.",
   dict(type="quote", q="There was real loss to real people who listened to Mr. Milton", case=CASE, doc="JUDGE EDGARDO RAMOS · DEC 18, 2023", cite=SRC_TR, size=52),
   show="The judge sided with the government on loss. \"There was real loss to real people,\" he said, \"who listened to Mr. Milton and invested in Nikola because of what they heard from him.\""),
 L("Prosecutors compared Milton to Elizabeth Holmes of Theranos, who got one hundred thirty-five months. The judge did not. Holmes, he said, marketed technology that affected people's health. That's not what Mr. Milton did, in my view.",
   dict(type="quote", q="That's not what Mr. Milton did, in my view.", case=CASE, doc="JUDGE EDGARDO RAMOS · ON THE HOLMES COMPARISON", cite=SRC_TR + " · " + SRC_GM, size=58),
   show="Prosecutors compared Milton to Elizabeth Holmes of Theranos, who got 135 months. The judge did not. Holmes, he said, marketed technology that affected people's health. \"That's not what Mr. Milton did, in my view.\""),
 L("Milton spoke. He insisted he had not lied. On one of his statements, he told the judge: I told the truth.",
   dict(type="quote", q="I told the truth.", case=CASE, doc="TREVOR MILTON · SENTENCING, DEC 18, 2023", cite=SRC_TR, size=72),
   show="Milton spoke. He insisted he had not lied. On one of his statements, he told the judge: \"I told the truth.\""),
 L("The judge read from victims' letters. One investor, a truck driver, wrote: I watched a video of a Nikola truck appearing to drive effortlessly.",
   dict(type="quote", q="I watched a video of a Nikola truck appearing to drive effortlessly.", case=CASE, doc="VICTIM LETTER · READ AT SENTENCING", cite=SRC_TR, size=50),
   show="The judge read from victims' letters. One investor, a truck driver, wrote: \"I watched a video of a Nikola truck appearing to drive effortlessly.\""),
 L("Then Judge Edgardo Ramos gave his view. I believe the jury got it right. And: the law does not grant a pass for good intentions.",
   dict(type="quote", q="I believe the jury got it right.", case=CASE, doc="JUDGE EDGARDO RAMOS · DEC 18, 2023", cite=SRC_TR, size=64),
   show="Then Judge Edgardo Ramos gave his view: \"I believe the jury got it right.\" And: \"The law does not grant a pass for good intentions.\""),
 L("The sentence: forty-eight months, a one million dollar fine, and forfeiture of the Utah ranch. Restitution would be set later.",
   doc("jdg_2", "JUDGMENT · IMPRISONMENT", "48 months on counts 1, 3 and 4", SRC_JDG, 0),
   show="The sentence: 48 months, a $1 million fine, and forfeiture of the Utah ranch. Restitution would be set later."),
 L("And the judge granted bail pending appeal. Milton remained free.",
   dict(type="verdict", kicker="DECEMBER 18, 2023", stamp="SENTENCED", big="4 years", sub="Free on bail pending appeal")),
 # VI
 L("In February twenty twenty-four, the judge also paused the fine, the forfeiture and all other financial parts of the sentence while Milton appealed.",
   dict(type="stat", kicker="FEBRUARY 26, 2024", value="Stayed", label="Fine, forfeiture and other financial penalties, pending appeal", src=SRC_OP2),
   show="In February 2024, the judge also paused the fine, the forfeiture and all other financial parts of the sentence while Milton appealed."),
 L("Chapter six. The pardon.", dict(type="chapter", n="VI", title="The Pardon")),
 L("In February twenty twenty-five, Nikola filed for bankruptcy protection.",
   dict(type="stat", kicker="FEBRUARY 2025", value="Chapter 11", label="Nikola files for bankruptcy protection", src=SRC_AP2)),
 L("On March fourteenth, twenty twenty-five, prosecutors asked the court to order Milton to pay restitution of six hundred sixty point eight million dollars to Nikola's shareholders.",
   doc("rest", "U.S. ATTORNEY, S.D.N.Y. · MARCH 14, 2025", "$660,800,000 in restitution", SRC_REST, 1),
   show="On March 14, 2025, prosecutors asked the court to order Milton to pay restitution of $660.8 million to Nikola's shareholders."),
 L("Thirteen days later, on March twenty-seventh, President Donald Trump issued Milton a full and unconditional pardon.",
   doc("pard", "EXECUTIVE GRANT OF CLEMENCY · MARCH 2025", "“A Full and Unconditional Pardon”", SRC_PARD, 0),
   show="Thirteen days later, on March 27, President Donald Trump issued Milton \"A Full and Unconditional Pardon.\""),
 L("It included remission of any and all fines, penalties, forfeitures, and restitution ordered by the court.",
   doc("pard", "EXECUTIVE GRANT OF CLEMENCY", "Fines, forfeitures, restitution", SRC_PARD, 1),
   show="It included \"remission of any and all fines, penalties, forfeitures, and restitution ordered by the court.\""),
 L("Milton's lawyers told the court the pardon blots out of existence the guilt, quoting an eighteen sixty-six Supreme Court case. Both sides agreed the restitution request and his appeal were now moot.",
   dict(type="quote", q="blots out of existence the guilt", case=CASE, doc="EX PARTE GARLAND (1866), QUOTED BY MILTON'S LAWYERS", cite=SRC_DEF, size=60),
   show="Milton's lawyers told the court the pardon \"blots out of existence the guilt,\" quoting an 1866 Supreme Court case. Both sides agreed the restitution request and his appeal were now moot."),
 L("On April seventh, the judge exonerated his bail and ordered the court to refund his three hundred dollar special assessment.",
   doc("bail", "ORDER · APRIL 7, 2025", "Bail exonerated", SRC_BAIL, 1),
   show="On April 7, the judge exonerated his bail and ordered the court to refund his $300 special assessment."),
 L("Milton thanked the president. Trump said the pardon was highly recommended by many people. Milton had never been incarcerated.",
   dict(type="quote", q="I am incredibly grateful to President Trump", case=CASE, doc="TREVOR MILTON · MARCH 2025", cite="As quoted by " + SRC_AP2, size=54),
   show="Milton thanked the president: \"I am incredibly grateful to President Trump.\" Trump said the pardon was \"highly recommended by many people.\" Milton had not been incarcerated."),
 L("In September twenty twenty-five, the SEC agreed to dismiss its civil case, in the exercise of its discretion.",
   doc("secd", "SEC v. MILTON · SEPTEMBER 2025", "“in the exercise of its discretion”", SRC_SECD, 0),
   show="In September 2025, the SEC agreed to dismiss its civil case, \"in the exercise of its discretion.\""),
 L("And in twenty twenty-six, according to published reports, Milton was trying to raise a billion dollars for AI-powered aircraft, at SyberJet, an aviation company he and an investment group bought.",
   dict(type="stat", kicker="2026", value="$1 billion", label="Reported fundraising target for AI-powered aircraft", src=SRC_EW),
   show="And in 2026, according to published reports, Milton was trying to raise $1 billion for AI-powered aircraft, at SyberJet, an aviation company he and an investment group bought."),
 L("The pardon erased the punishment. It did not erase the record: the hill, the e-mails, and a jury's verdict on three counts.",
   dict(type="big", lines=["The record", "is still|the record."], src=SRC_JDG + " · " + SRC_PARD)),
 L("This is SWORN. Real trials. Real evidence. The verdict.", dict(type="end")),
]
# --- Fact-check FIXes (factcheck.md, independent agent, 22 fixes) ---
def setline(prefix, say=None, show=None, scene=None):
    m = [l for l in lines if l["say"].startswith(prefix)]
    assert len(m) == 1, prefix
    l = m[0]
    if say: l["say"] = say
    if show: l["show"] = show
    if scene:
        l["scene"].update(scene)
        if "hl" in scene and "pan" not in scene: l["scene"]["pan"] = [0.0, 0.1]
setline("Its founder, Trevor Milton, had written", say="Its founder, Trevor Milton, had said that this would be the first time anyone has seen the Nikola truck move.", show="Its founder, Trevor Milton, had said that this would be \"the first time anyone has seen the Nikola truck move.\"", scene={"doc": "TREVOR MILTON · GX 929"})
setline("More than a year later", say="More than a year later, the Nikola One appeared in a commercial shoot for a trucking-parts company. The SEC alleged it still could not run under its own power.", show="More than a year later, the Nikola One appeared in a commercial shoot for a trucking-parts company. The SEC alleged it still \"could not run under its own power.\"")
setline("So, according to the SEC, it was towed", scene={"hl": [0.0, 0.0972, 1.0, 0.1036]})
setline("The SEC alleged that Nikola's chief engineer", scene={"hl": [0.0, 0.0972, 1.0, 0.1036]})
setline("When Milton saw the company's first cut", say="When Milton saw the company's first cut, prosecutors wrote, he became irate that it did not show the truck going down the road as we talked about, which, he wrote, was the reason why I approved it.", show="When Milton saw the company's first cut, prosecutors wrote, he \"became irate\" that it did not show the truck \"going down the road as we talked about,\" which, he wrote, \"was the reason why I approved it.\"")
setline("He wanted the footage for Nikola.", say="He wanted the footage for Nikola. It would be, he said, the first time anyone has seen the Nikola truck move, so it could get millions of views on our YouTube channel.", show="He wanted the footage for Nikola. It would be, he said, \"the first time anyone has seen the Nikola truck move … so it could get millions of views on our youtube channel.\"", scene={"doc": "TREVOR MILTON · GX 929"})
setline("The pickup truck, the Badger.", scene={"kicker": "GOV'T SENTENCING MEMORANDUM · PAGE 7"})
setline("His own executives, prosecutors wrote", show="His own executives, prosecutors wrote, warned him \"over and over again\" not to mischaracterize the business. He kept going.")
setline("His chief financial officer testified", show="His chief financial officer testified that Milton said \"one of [Milton's] goal[s] was to be in the top 100\" of the Forbes list of the wealthiest Americans, by raising Nikola's stock price.")
setline("He sold about one hundred million", scene={"kicker": "GOV'T SENTENCING MEMORANDUM · PAGE 6"})
setline("He also used stock options", scene={"hl": [0.0, 0.8732, 1.0, 0.0648]})
setline("The trial began on September thirteenth", say="The trial began on September thirteenth, twenty twenty-two, and ran a month. The evidence, the judge later wrote, citing Milton's own lawyers, focused on four big categories of alleged lies.", show="The trial began on September 13, 2022, and ran a month. The evidence, the judge later wrote, citing Milton's own lawyers, focused on \"four big categories\" of alleged lies.", scene={"hl": [0.0, 0.4867, 1.0, 0.1394]})
setline("Not guilty on the fourth", say="Not guilty on Count Two, a second securities-fraud charge under a different statute.")
setline("Milton asked for a new trial", scene={"hl": [0.0, 0.852, 1.0, 0.148]})
setline("Sentencing came on December eighteenth", say="Sentencing came on December eighteenth, twenty twenty-three. By the government's math, investors lost between six hundred sixty point eight and six hundred seventy-three point six million dollars, and the guidelines called for sixty years.")
setline("Then Judge Edgardo Ramos gave his view", say="Judge Edgardo Ramos had already given his view. I believe the jury got it right. And: the law does not grant a pass for good intentions.", show="Judge Edgardo Ramos had already given his view: \"I believe the jury got it right.\" And: \"The law does not grant a pass for good intentions.\"")
setline("Milton thanked the president.", say="Milton thanked the president. Trump said the pardon was highly recommended by many people. Milton had not been incarcerated.")
setline("The pardon erased the punishment.", say="The pardon erased the punishment. It did not erase the record: the hill, his own messages, and a jury's verdict on three counts.")
from panfix import fix
fix(lines, "long")
spec = {"label": "SWORN · CASE 013", "lines": lines}
if __name__ == "__main__":
    json.dump(spec, open(os.path.join(HERE, "episode.json"), "w"), indent=1, ensure_ascii=False)
    print(len(lines), "lines,", sum(len(l["say"].split()) for l in lines), "words")
