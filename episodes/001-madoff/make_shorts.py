import json
CASE = "U.S. v. MADOFF"
PLEA = dict(case=CASE, doc="PLEA STATEMENT", cite="Madoff, plea allocution · S.D.N.Y. · Mar 12, 2009")
SRC_ARR = "U.S. Attorney, S.D.N.Y. — release, Dec 11, 2008"
SRC_PLEA = "U.S. Attorney, S.D.N.Y. — release, Mar 12, 2009"
SRC_SENT = "U.S. Attorney, S.D.N.Y. — release, Jun 29, 2009"
SRC_OIG = "SEC Inspector General, Report OIG-509 (2009)"
AP = "AP via OPB, Apr 14, 2021"
def L(say, scene=None, show=None):
    d = {"say": say}
    if show: d["show"] = show
    if scene: d["scene"] = scene
    return d
END = L("Real trials. Real evidence. The verdict.", dict(type="end"))
shorts = [
 {"title": "He Confessed. Then the Judge Spoke. (Bernie Madoff)", "hook": "He confessed.|Then the judge spoke.", "lines": [
  L("March twelfth, two thousand nine. A federal courtroom in Manhattan. Bernard Madoff stands up and reads a confession.",
    dict(type="doc", img="img/plea.jpg", pan=[0.2, 0.36], kicker="MARCH 12, 2009 · MANHATTAN FEDERAL COURT", src=SRC_PLEA),
    show="March 12, 2009. A federal courtroom in Manhattan. Bernard Madoff stands up and reads a confession."),
  L("To the best of my recollection, my fraud began in the early nineteen nineties.",
    dict(type="quote", q="To the best of my recollection, my fraud began in the early 1990s.", **PLEA),
    show="\"To the best of my recollection, my fraud began in the early 1990s.\""),
  L("His clients believed their money was in the stock market. It wasn't.",
    dict(type="big", kicker="WHAT CLIENTS BELIEVED", lines=["In the stock|market.", "It wasn't."])),
  L("I never invested those funds in the securities, as I had promised. Instead, those funds were deposited in a bank account at Chase Manhattan Bank.",
    dict(type="quote", q="I never invested those funds in the securities, as I had promised. Instead, those funds were deposited in a bank account at Chase Manhattan Bank.", size=36, **PLEA)),
  L("He pleaded guilty to all eleven counts.", dict(type="stat", kicker="GUILTY PLEA", value="11", label="felony counts", src=SRC_PLEA), show="He pleaded guilty to all 11 counts."),
  L("June twenty-ninth. Judge Denny Chin called his crimes extraordinarily evil.",
    dict(type="big", kicker="JUNE 29, 2009 · JUDGE DENNY CHIN", lines=["“extraordinarily|evil”"], src=SRC_SENT),
    show="June 29. Judge Denny Chin called his crimes \"extraordinarily evil.\""),
  L("The sentence: one hundred fifty years in prison. The maximum.",
    dict(type="verdict", kicker="THE SENTENCE", stamp="SENTENCED", big="150 years", sub="the statutory maximum"),
    show="The sentence: 150 years in prison. The maximum."),
  END]},
 {"title": "Six Warnings. Nobody Stopped Him. #Madoff", "hook": "Six warnings.|Nobody stopped him.", "lines": [
  L("Between nineteen ninety-two and two thousand eight, the SEC received six substantive complaints about Bernie Madoff.",
    dict(type="stat", kicker="SEC INSPECTOR GENERAL · 2009", value="6", label="substantive complaints|June 1992 – December 2008", src=SRC_OIG),
    show="Between 1992 and 2008, the SEC received six substantive complaints about Bernie Madoff."),
  L("That's what the SEC's own inspector general found in two thousand nine.", show="That's what the SEC's own inspector general found in 2009."),
  L("One analyst, Harry Markopolos, sent versions of his analysis in May two thousand, March two thousand one, and October two thousand five.",
    dict(type="timeline", kicker="MARKOPOLOS → SEC", events=[{"date": "MAY 2000", "text": "First version"}, {"date": "MARCH 2001", "text": "Second version"}, {"date": "OCT 2005", "text": "Third version"}], at=2, src=SRC_OIG),
    show="One analyst, Harry Markopolos, sent versions of his analysis in May 2000, March 2001, and October 2005."),
  L("The last one was titled: The world's largest hedge fund is a fraud.",
    dict(type="quote", q="The World's Largest Hedge Fund is a Fraud", case="H. MARKOPOLOS → SEC", doc="OCTOBER 2005", cite="As cited in SEC OIG Report OIG-509", size=52),
    show="The last one was titled: \"The World's Largest Hedge Fund is a Fraud.\""),
  L("Three examinations. Two investigations. The inspector general found a thorough and competent investigation was never performed.",
    dict(type="big", kicker="THE FINDING", lines=["3 exams.|2 investigations.", "Never thorough."], src=SRC_OIG)),
  L("Madoff confessed in December two thousand eight, more than three years after that October two thousand five complaint.",
    dict(type="big", kicker="DECEMBER 2008", lines=["3+ years", "after the 2005 complaint."]),
    show="Madoff confessed in December 2008, more than three years after that October 2005 complaint."),
  END]},
 {"title": "\"It's All Just One Big Lie\" — Madoff's Confession", "hook": "\"It's all just|one big lie.\"", "lines": [
  L("December tenth, two thousand eight. Bernie Madoff tells two senior employees his business is a fraud.",
    dict(type="doc", img="img/arrest2.jpg", pan=[0.38, 0.5], hl=[0.0, 0.46, 1.0, 0.37], kicker="DECEMBER 10, 2008", src=SRC_ARR),
    show="December 10, 2008. Bernie Madoff tells two senior employees his business is a fraud."),
  L("According to prosecutors, he said he was finished, that he had absolutely nothing, and that it was all just one big lie.",
    dict(type="quote", q="finished … absolutely nothing … it's all just one big lie", case=CASE, doc="AS QUOTED BY PROSECUTORS", cite="U.S. Attorney's release, Dec 11, 2008", size=46)),
  L("Basically, a giant Ponzi scheme.",
    dict(type="big", lines=["“basically, a giant|Ponzi scheme.”"], src=SRC_ARR)),
  L("He put the losses at fifty billion dollars, at least.", dict(type="stat", kicker="HIS ESTIMATE", value="$50B+", label="in losses, at least", src=SRC_ARR), show="He put the losses at $50 billion, at least."),
  L("And he said he had two to three hundred million left, which he planned to pay to selected employees, family, and friends.",
    dict(type="stat", kicker="WHAT HE HAD LEFT", value="$200–300M", label="for selected employees,|family and friends", src=SRC_ARR),
    show="And he said he had $200–300 million left, which he planned to pay to selected employees, family, and friends."),
  L("The next morning, the FBI arrested him.", dict(type="doc", img="img/arrest.jpg", pan=[0.0, 0.1], kicker="DECEMBER 11, 2008 · ARRESTED", src=SRC_ARR)),
  END]},
 {"title": "Where Madoff's Clients' Money Actually Went", "hook": "Where the money|actually went.", "lines": [
  L("Bernie Madoff told clients he would buy stock, options and other securities of large, well-known corporations.",
    dict(type="quote", q="that I would invest their money in shares of common stock, options and other securities of large well-known corporations", size=38, **PLEA)),
  L("In court, he admitted he never did.",
    dict(type="big", kicker="HIS PLEA · MARCH 12, 2009", lines=["He never", "invested it."])),
  L("Those funds were deposited in a bank account at Chase Manhattan Bank.",
    dict(type="quote", q="Instead, those funds were deposited in a bank account at Chase Manhattan Bank.", **PLEA)),
  L("He knowingly caused false trading confirmations and client account statements, to show trades that never happened.",
    dict(type="quote", q="I knowingly caused false trading confirmations and client account statements …", **PLEA)),
  L("When clients wanted money back, he paid them with other clients' money.",
    dict(type="list", kicker="THE CYCLE", items=[["1", "New money comes in"], ["2", "Sits in a Chase account"], ["3", "Fake statements go out"], ["4", "Old clients paid with new money"]], size=40, src="Madoff, plea allocution, 2009")),
  L("By late two thousand eight, the statements claimed about sixty-five billion dollars. Investors had put in an estimated seventeen and a half.",
    dict(type="bars", kicker="ON PAPER VS. PUT IN", items=[{"label": "ON PAPER", "value": 65, "display": "$65B"}, {"label": "PUT IN", "value": 17.5, "display": "$17.5B"}], src=AP),
    show="By late 2008, the statements claimed about $65 billion. Investors had put in an estimated $17.5 billion."),
  END]},
 {"title": "How a Judge Got to 150 Years (Bernie Madoff)", "hook": "How the judge|got to 150 years.", "lines": [
  L("June twenty-ninth, two thousand nine. Nine victims spoke before Bernie Madoff's sentence.",
    dict(type="doc", img="img/sentence.jpg", pan=[0.4, 0.55], kicker="JUNE 29, 2009 · SENTENCING", src=SRC_SENT),
    show="June 29, 2009. Nine victims spoke before Bernie Madoff's sentence."),
  L("One said she lived on food stamps, and sometimes scavenged in dumpsters.",
    dict(type="quote", q="I live on food stamps. At the end of the month, I sometimes scavenge in dumpsters.", case=CASE, doc="VICTIM STATEMENT", cite="Fortune/CNN Money, Jun 29, 2009", size=44)),
  L("Judge Denny Chin said the fraud was staggering, and the breach of trust was massive.",
    dict(type="quote", q="Objectively speaking, the fraud was staggering … the breach of trust was massive.", case=CASE, doc="JUDGE CHIN", cite="U.S. Attorney's release, Jun 29, 2009", size=44)),
  L("Then the math. Eleven counts. Each with a maximum. Six at twenty years, one at ten, four at five.",
    dict(type="doc", img="img/counts.jpg", pan=[0.0, 0.5], kicker="STATUTORY MAXIMUMS · 11 COUNTS", src=SRC_PLEA)),
  L("Add them up: exactly one hundred fifty.", dict(type="big", kicker="THE MATH", lines=["120 + 10 + 20", "= 150"]), show="Add them up: exactly 150."),
  L("And that is what he got. One hundred fifty years.",
    dict(type="verdict", kicker="THE SENTENCE", stamp="SENTENCED", big="150 years", sub="the statutory maximum"),
    show="And that is what he got. 150 years."),
  END]},
 {"title": "Did Madoff's Victims Get Their Money Back?", "hook": "Did the victims get|their money back?", "lines": [
  L("Bernie Madoff's investors put in an estimated seventeen and a half billion dollars.",
    dict(type="stat", kicker="PUT IN · AP ESTIMATE", value="$17.5B", label="invested by clients", src=AP),
    show="Bernie Madoff's investors put in an estimated $17.5 billion."),
  L("By twenty twenty-one, trustees had recovered more than fourteen billion.",
    dict(type="bars", kicker="RECOVERED BY TRUSTEES · BY 2021", items=[{"label": "PUT IN", "value": 17.5, "display": "$17.5B"}, {"label": "RECOVERED", "value": 14, "display": "$14B+"}], src=AP),
    show="By 2021, trustees had recovered more than $14 billion."),
  L("Separately, the Justice Department's Madoff Victim Fund paid out more than four point three billion dollars.",
    dict(type="stat", kicker="MADOFF VICTIM FUND", value="$4.3B+", label="paid out by the U.S. Justice Department", src="U.S. DOJ via NBC New York, Dec 2024"),
    show="Separately, the Justice Department's Madoff Victim Fund paid out more than $4.3 billion."),
  L("To more than forty thousand victims, in nearly one hundred thirty countries.",
    dict(type="stat", kicker="WHO GOT PAID", value="40,000+", label="victims in nearly 130 countries", src="U.S. DOJ via NBC New York, Dec 2024"),
    show="To more than 40,000 victims, in nearly 130 countries."),
  L("The final payout started in December twenty twenty-four. The Justice Department said eligible victims had recovered nearly ninety-four percent of their fraud losses.",
    dict(type="stat", kicker="FINAL PAYOUT · DECEMBER 2024", value="~94%", label="of fraud losses recovered|by eligible claimants", src="U.S. DOJ via NBC New York, Dec 2024"),
    show="The final payout started in December 2024. The Justice Department said eligible victims had recovered nearly 94% of their fraud losses."),
  L("Madoff never saw it. He died in federal custody in twenty twenty-one, at eighty-two.",
    dict(type="big", kicker="APRIL 14, 2021", lines=["Died in custody.", "Age 82."], src=AP),
    show="Madoff never saw it. He died in federal custody in 2021, at 82."),
  END]},
]
for i, s in enumerate(shorts, 1):
    s["label"] = "SWORN"
    json.dump(s, open(f"short{i}.json", "w"), indent=1, ensure_ascii=False)
    print(i, sum(len(l["say"].split()) for l in s["lines"]), "words")
