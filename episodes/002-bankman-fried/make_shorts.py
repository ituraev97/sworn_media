import json
CASE = "U.S. v. BANKMAN-FRIED"
SRC_MEMO = "Gov't sentencing memorandum, Mar 15, 2024"
SRC_TR = "Sentencing transcript, Mar 28, 2024"
SRC_JUDG = "Judgment, S.D.N.Y., Mar 28, 2024"
SRC_NT = "Memorandum and order, S.D.N.Y., Apr 28, 2026"
SRC_CA2 = "2d Cir., No. 24-961, Jun 12, 2026"
TR = dict(case=CASE, doc="JUDGE KAPLAN", cite="Sentencing transcript, Mar 28, 2024")
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
END = L("Real trials. Real evidence. The verdict.", dict(type="end"))
shorts = [
 {"title": "\"FTX Is Fine. Assets Are Fine.\" — What He Wrote the Day Before", "hook": "\"FTX is fine.\"|What he knew.", "lines": [
  L("November seventh, two thousand twenty-two. Sam Bankman-Fried tweets to his customers.",
    dict(type="doc", img="img/tweets.jpg", pan=[0.04, 0.1], hl=[0.0, 0.10, 1.0, 0.145], kicker="NOVEMBER 7, 2022", src=SRC_MEMO),
    show="November 7, 2022. Sam Bankman-Fried tweets to his customers."),
  L("FTX is fine. Assets are fine.",
    dict(type="quote", q="FTX is fine. Assets are fine.", case=CASE, doc="TWEET · NOV 7, 2022", cite="As quoted in the gov't sentencing memorandum", size=60)),
  L("FTX has enough to cover all client holdings.",
    dict(type="quote", q="FTX has enough to cover all client holdings.", case=CASE, doc="TWEET · NOV 7, 2022", cite="As quoted in the gov't sentencing memorandum", size=56)),
  L("But according to the trial evidence, the day before, he had written that FTX had enough to process about one third of remaining client assets.",
    dict(type="doc", img="img/tweets.jpg", pan=[0.45, 0.52], hl=[0.0, 0.695, 1.0, 0.1], kicker="NOVEMBER 6, 2022 · HIS OWN DOCUMENT", src=SRC_MEMO)),
  L("Hours before the tweets, prosecutors said, he wrote in a group chat that FTX had three point nine billion of a twelve billion dollar total.",
    dict(type="bars", kicker="PER PROSECUTORS", items=[{"label": "TOTAL", "value": 12, "display": "$12B"}, {"label": "ON HAND", "value": 3.9, "display": "$3.9B"}], src=SRC_MEMO),
    show="Hours before the tweets, prosecutors said, he wrote in a group chat that FTX had $3.9 billion of a $12 billion total."),
  L("Four days later, FTX filed for bankruptcy. A jury later convicted him on all seven counts.",
    dict(type="verdict", kicker="NOVEMBER 2, 2023", stamp="GUILTY", big="All 7 counts", sub="United States v. Bankman-Fried"),
    show="Four days later, FTX filed for bankruptcy. A jury later convicted him on all 7 counts."),
  END]},
 {"title": "The Coin Flip That Explained the Whole FTX Case, According to the Judge", "hook": "The coin flip|the judge read out.", "lines": [
  L("At Sam Bankman-Fried's sentencing, Judge Lewis Kaplan read aloud from Caroline Ellison's trial testimony.",
    dict(type="big", kicker="MARCH 28, 2024 · SENTENCING", lines=["The judge reads|her testimony."], src=SRC_TR)),
  L("She said he talked about taking a coin flip where tails might lose ten million dollars, and heads might make slightly more.",
    show="She said he talked about taking a coin flip where tails might lose $10 million, and heads might make slightly more."),
  L("And that he would be happy to flip a coin where tails meant the world was destroyed, as long as heads made the world more than twice as good.",
    dict(type="quote", q="… he would be happy to flip a coin if it came up tails and the world was destroyed. As long as if it came up heads, the world would be like more than twice as good.", case=CASE, doc="ELLISON'S TESTIMONY", cite="Sentencing transcript, Mar 28, 2024", size=34)),
  L("The judge called it a leitmotif of the entire case.",
    dict(type="quote", q="that's really a leitmotif in my judgment of this entire case.", size=46, **TR)),
  L("FTX customer funds, he said, were not his to use. He was betting on expected value.",
    dict(type="big", kicker="JUDGE KAPLAN", lines=["“not his to use”", "“betting on|expected value”"], src=SRC_TR)),
  L("The sentence: twenty-five years.",
    dict(type="verdict", kicker="THE SENTENCE", stamp="SENTENCED", big="25 years", sub="300 months in federal prison"),
    show="The sentence: 25 years."),
  END]},
 {"title": "The Hidden Code Behind the FTX Collapse: \"Allow Negative\"", "hook": "The secret line|in FTX's code.", "lines": [
  L("FTX told customers their deposits were theirs. Its terms of service said customer assets could not be loaned to FTX.",
    dict(type="quote", q="none of the digital assets in [a customer's] account are the property of, or shall or may be loaned to, FTX Trading.", case=CASE, doc="FTX TERMS OF SERVICE", cite="As quoted in the gov't sentencing memorandum", size=40)),
  L("But according to trial evidence cited by prosecutors, special features were written into FTX's code for Sam Bankman-Fried's trading firm, Alameda Research.",
    dict(type="doc", img="img/allownegative.jpg", pan=[0.2, 0.32], hl=[0.0, 0.515, 1.0, 0.175], kicker="PER TRIAL EVIDENCE", src=SRC_MEMO)),
  L("One was called allow negative. Alameda's balance could go below zero.",
    dict(type="big", kicker="FEATURE ONE", lines=["“allow negative”"], src=SRC_MEMO),
    show="One was called \"allow negative.\" Alameda's balance could go below zero."),
  L("Another was a sixty-five billion dollar line of credit. And Alameda was exempt from automatic liquidation.",
    dict(type="stat", kicker="FEATURE TWO", value="$65B", label="line of credit for Alameda", src=SRC_MEMO),
    show="Another was a $65 billion line of credit. And Alameda was exempt from automatic liquidation."),
  L("By June two thousand twenty-two, according to trial evidence, a spreadsheet showed Alameda borrowing thirteen billion dollars in customer funds.",
    dict(type="stat", kicker="JUNE 2022 · PER PROSECUTORS", value="$13B", label="in FTX customer funds|borrowed by Alameda", src=SRC_MEMO),
    show="By June 2022, according to trial evidence, a spreadsheet showed Alameda borrowing $13 billion in customer funds."),
  L("In twenty twenty-three, a jury convicted Bankman-Fried on all seven counts, including fraud.",
    dict(type="verdict", kicker="NOVEMBER 2, 2023", stamp="GUILTY", big="All 7 counts", sub="United States v. Bankman-Fried"),
    show="In 2023, a jury convicted Bankman-Fried on all 7 counts, including fraud."),
  END]},
 {"title": "Prosecutors Asked for 40–50 Years. The Defense Asked for About 6. Here's What SBF Got", "hook": "40–50 years?|Or about 6?", "lines": [
  L("March twenty-eighth, two thousand twenty-four. Sam Bankman-Fried faces sentencing in Manhattan.",
    dict(type="big", kicker="MARCH 28, 2024 · MANHATTAN", lines=["Sentencing day."], src=SRC_TR),
    show="March 28, 2024. Sam Bankman-Fried faces sentencing in Manhattan."),
  L("Prosecutors asked for forty to fifty years. His lawyers asked for sixty-three to seventy-eight months.",
    dict(type="bars", kicker="WHAT EACH SIDE ASKED FOR", items=[{"label": "PROSECUTORS", "value": 50, "display": "40–50 yrs"}, {"label": "DEFENSE", "value": 6.5, "display": "63–78 mos"}], src="Gov't memorandum · NPR, Mar 28, 2024"),
    show="Prosecutors asked for 40 to 50 years. His lawyers asked for 63 to 78 months."),
  L("Judge Lewis Kaplan found that he had lied at trial.",
    dict(type="quote", q="And when he wasn't outright lying, he was often evasive, hairsplitting, dodging questions …", size=40, **TR)),
  L("I've been doing this job for close to thirty years. I've never seen a performance quite like that.",
    dict(type="quote", q="I've been doing this job for close to 30 years. I've never seen a performance quite like that.", size=44, **TR),
    show="\"I've been doing this job for close to 30 years. I've never seen a performance quite like that.\""),
  L("He said there was never a word of remorse for the commission of terrible crimes.",
    dict(type="quote", q="never a word of remorse for the commission of terrible crimes.", size=48, **TR)),
  L("The sentence: three hundred months. Twenty-five years. Plus a forfeiture of about eleven billion dollars.",
    dict(type="verdict", kicker="THE SENTENCE", stamp="SENTENCED", big="25 years", sub="300 months · $11.02 billion forfeiture"),
    show="The sentence: 300 months. 25 years. Plus a forfeiture of about $11 billion."),
  END]},
 {"title": "They Testified Against SBF. Here's What Happened to Them", "hook": "They testified|against him.", "lines": [
  L("Sam Bankman-Fried's trial turned on three former insiders: Caroline Ellison, Gary Wang, and Nishad Singh. All three had pleaded guilty.",
    dict(type="list", kicker="WITNESSES FOR THE GOVERNMENT", items=[["CE", "Caroline Ellison · ran Alameda"], ["GW", "Gary Wang · FTX co-founder"], ["NS", "Nishad Singh · FTX co-founder"]], size=42, src="Washington Post via Spokesman-Review · Straight Arrow News")),
  L("Ellison testified she told him, we don't really have the money for this, we'll have to borrow from FTX to do it.",
    dict(type="quote", q="We don't really have the money for this, we'll have to borrow from FTX to do it.", case=CASE, doc="ELLISON · TRIAL TESTIMONY", cite="As quoted in the gov't sentencing memorandum", size=44)),
  L("Singh testified about a talk on a penthouse balcony, where Bankman-Fried acknowledged they were a little short on deliverable.",
    dict(type="big", kicker="SEPTEMBER 2022 · PER TRIAL TESTIMONY", lines=["“a little short|on deliverable”"], src=SRC_MEMO)),
  L("The jury convicted Bankman-Fried on all seven counts. He got twenty-five years.",
    dict(type="verdict", kicker="MARCH 28, 2024", stamp="SENTENCED", big="25 years", sub="Samuel Bankman-Fried"),
    show="The jury convicted Bankman-Fried on all 7 counts. He got 25 years."),
  L("Ellison was sentenced to two years. Singh and Wang avoided prison. Another FTX executive, Ryan Salame, got seven and a half years.",
    dict(type="list", kicker="THEIR SENTENCES", items=[["2 YRS", "Caroline Ellison"], ["NONE", "Nishad Singh"], ["NONE", "Gary Wang"], ["7½ YRS", "Ryan Salame"]], size=42, src="NBC New York, Nov 20, 2024 · Cointelegraph"),
    show="Ellison was sentenced to two years. Singh and Wang avoided prison. Another FTX executive, Ryan Salame, got 7½ years."),
  END]},
 {"title": "Where Sam Bankman-Fried's Case Stands Now (2026)", "hook": "Where SBF's case|stands now.", "lines": [
  L("In twenty twenty-four, Sam Bankman-Fried was sentenced to twenty-five years for the FTX fraud.",
    dict(type="doc", img="img/judgment3.jpg", pan=[0.1, 0.2], hl=[0.0, 0.88, 1.0, 0.11], kicker="JUDGMENT · 300 MONTHS", src=SRC_JUDG),
    show="In 2024, Sam Bankman-Fried was sentenced to 25 years for the FTX fraud."),
  L("In April twenty twenty-six, the trial judge denied his bid for a new trial, calling his claim of government threats wildly conspiratorial.",
    dict(type="doc", img="img/newtrial3.jpg", pan=[0.0, 0.1], hl=[0.0, 0.32, 1.0, 0.06], kicker="APRIL 28, 2026", src=SRC_NT),
    show="In April 2026, the trial judge denied his bid for a new trial, calling his claim of government threats \"wildly conspiratorial.\""),
  L("In June, the Second Circuit affirmed. The evidence, it said, was overwhelming.",
    dict(type="doc", img="img/mandate.jpg", pan=[0.36, 0.45], hl=[0.0, 0.905, 1.0, 0.075], kicker="JUNE 12, 2026 · AFFIRMED", src=SRC_CA2)),
  L("He has asked President Trump for a pardon. According to news reports, Trump has said he has no plans to grant one. None has been granted.",
    dict(type="big", kicker="ACCORDING TO NEWS REPORTS", lines=["Pardon requested.", "None granted."], src="The Block · Unchained, 2026")),
  L("In September, he asked the Supreme Court to hear his case. As this video was made, that petition was pending.",
    dict(type="stat", kicker="SUPREME COURT", value="No. 26-349", label="petition filed Sept 10, 2026|pending", src="Supreme Court docket")),
  END]},
]
for i, s in enumerate(shorts, 1):
    s["label"] = "SWORN"
    json.dump(s, open(f"short{i}.json", "w"), indent=1, ensure_ascii=False)
    print(i, len(s["title"]), sum(len(l["say"].split()) for l in s["lines"]), "words")
