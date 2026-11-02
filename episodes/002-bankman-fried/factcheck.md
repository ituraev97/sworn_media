# Fact-check — SWORN Case 002: The FTX Verdict (United States v. Samuel Bankman-Fried)

Independent check of `episode.json` (64 lines, 0-based), `short1.json`–`short6.json` (40 lines), `meta.json` (title, summary) and `thumb.json` (words, hook). Checked 2026-11-02 against the primary sources listed below. The script was not used as a source.

Sources opened:
- [IND] Sealed Indictment, Dkt. 1, Dec 9, 2022: /home/claude/research/d/ind1.pdf (Counts One–Seven text; "BANKMAN-FRIED's proprietary crypto hedge fund", p.2–4)
- [LET] U.S. Attorney letter, Dkt. 388, Dec 29, 2023: gov.uscourts.nysd.590940.388.0.pdf (original indictment of Dec 9, 2022 in eight counts; Count Eight campaign contributions; Bahamas extradited Dec 2022, did not consent to trial on Count Eight)
- [MEMO] Gov't sentencing memorandum, Dkt. 410, Mar 15, 2024: g410.txt / gov.uscourts.nysd.590940.410.0.pdf (pp.5–14, 29–31; Chapter 11 mention at p.~39)
- [TR] Sentencing transcript, Dkt. 426, Mar 28, 2024: s426.txt (pp.6, 10, 33–34, 51–55, 57–59)
- [JUDG] Judgment, Dkt. 424, Mar 28, 2024: scanned image pages viewed via img/judgment.jpg, judgment3.jpg, forfeit.jpg ("(S6)1 through (S6)7"; 300 months; 3 years supervised release; $11,020,000,000)
- [NT] Memorandum and Order denying new trial, Dkt. 595, Apr 28, 2026: gov.uscourts.nysd.590940.595.0.pdf (pp.1–3)
- [MAND] 2d Cir. judgment/mandate, Dkt. 601 (judgment Jun 12, 2026, AFFIRMED; filed in SDNY Aug 4, 2026)
- [CA2] 2d Cir. opinion No. 24-961, Jun 12, 2026 — https://ww3.ca2.uscourts.gov/decisions/OPN/24-961_opn.pdf (WebFetch; exact wording requested)
- [DOJ-CHG] https://www.justice.gov/usao-sdny/pr/united-states-attorney-announces-charges-against-ftx-founder-samuel-bankman-fried (Dec 13, 2022; "arrested yesterday in the Bahamas"; Williams quote)
- [DOJ-CONV] https://www.justice.gov/usao-sdny/pr/statement-us-attorney-damian-williams-conviction-samuel-bankman-fried (Nov 2, 2023)
- [SCOTUS] https://www.supremecourt.gov/docket/docketfiles/html/public/26-349.html (petition filed Sep 10, 2026; response deadline extended to Nov 16, 2026; no disposition)
- [PET] Cert petition, No. 26-349 (counsel of record Jeffrey L. Fisher; filed by counsel)
- [NPR] https://www.kaxe.org/news/2024-03-28/sam-bankman-fried-sentenced-to-25-years-in-prison-for-his-ftx-crimes
- [WAPO] https://www.spokesman.com/stories/2023/nov/02/bankman-fried-convicted-on-all-charges-after-weeks
- [NBC] https://www.nbcnewyork.com/news/business/money-report/ftx-co-founder-gary-wang-avoids-prison-time-for-role-in-crypto-fraud/6002582/
- [CT] https://cointelegraph.com/news/caroline-ellison-sentenced-2-years-prison
- [SAN] https://san.com/cc/where-are-they-now-ftx-criminals-making-headlines-in-and-out-of-jail
- [BLOCK] https://www.theblock.co/news/markets/2026-06-12-appeals-court-rejects-sam-bankman-frieds-bid-for-new-trial-in-ftx-fraud-case-404637
- [UNCH] https://unchainedcrypto.com/sam-bankman-fried-asks-the-supreme-court-to-overturn-his-fraud-conviction-and-11-billion-forfeiture/
- [SF] https://startupfortune.com/sam-bankman-frieds-last-legal-door-closes-leaving-only-a-pardon/
- Document images in img/ were opened and every `hl` box was drawn onto its image (renderer semantics from pipeline/stage.html: hl = [x, y, w, h] as fractions of the image).

## episode.json

| file | line# | field | claim | verdict | source | fix text |
|---|---|---|---|---|---|---|
| episode | 0 | say/show/scene | Nov 7, 2022 message to customers; doc hl on tweets paragraph | OK | MEMO p.12–13 | hl box covers the "November 7, 2022 … FTX is fine. Assets are fine." lines. |
| episode | 1 | say/scene.q | "A competitor is trying to go after us with false rumors. FTX is fine. Assets are fine." | OK | MEMO p.13 (GX-866) | Verbatim; cite "As quoted in the gov't sentencing memorandum" is correct. |
| episode | 2 | say/scene.q | "FTX has enough to cover all client holdings. We don't invest client assets …" | OK | MEMO p.13 | Verbatim ("(even in treasuries)" elided by ellipsis). |
| episode | 3 | say/scene | Day before, internal document: "enough to process ~1/3 of remaining client assets" | OK | MEMO p.13 (GX-21) | Memo: "on or about November 6, 2022"; attributed to trial evidence. hl correct. |
| episode | 4 | say/scene | Four days after tweets, bankruptcy, Nov 11, 2022 | OK | MEMO p.14 | Nov 7 to Nov 11 = 4 days. |
| episode | 5 | say/show | Intro | OK | — | |
| episode | 6 | scene | Title; S.D.N.Y.; 2022–2026 | OK | IND; MAND | |
| episode | 7 | say | Chapter title | OK | — | |
| episode | 8 | say/show/scene | Ran FTX from founding in 2019; by 2022 customers traded ~$10–15B daily, per 2d Cir. | OK | CA2 | "served as CEO of FTX from its founding in 2019"; "around $10–$15 billion daily". |
| episode | 9 | say/scene.note | Alameda: his "proprietary crypto hedge fund" | OK | IND p.2–4 | Verbatim. Note: phrase is on p.2 of the indictment, not on the p.1 image shown; the note is a correct quote of the document, so acceptable. |
| episode | 10 | say/scene | Prosecutors: comfortable upbringing, MIT education, prestigious start in finance; "all the advantages" | OK | MEMO p.5 (PDF p.5) | Attributed; hl on the right sentence. |
| episode | 11 | say/scene.q | Ads featuring celebrities: "FTX is the safest and easiest way to buy and sell crypto." | OK | MEMO p.5 (GX-900, 905) | Verbatim. |
| episode | 12 | say/scene.q | Terms of service quote | OK | MEMO p.5 (GX-558) | Verbatim. |
| episode | 13 | say/scene | Customers saw balances, believed they could withdraw | OK | MEMO p.6 | Memo: "which they believed they could withdraw"; website "represented that customers could withdraw all the funds". |
| episode | 14 | say | Chapter title | OK | — | |
| episode | 15 | say/scene | Grand jury charge: agreed with others to defraud FTX customers, using deposits to pay Alameda expenses/debts and make investments | OK | IND ¶2 | Attributed to grand jury charge. hl on Count One ¶1, title matches Count One heading. |
| episode | 16 | say/scene | Per prosecutors: customer deposits to Alameda-controlled accounts, incl. North Dimension | OK | MEMO p.7 | Attributed. |
| episode | 17 | say/show/scene | "allow negative"; $65B line of credit; exemption from auto-liquidation | OK | MEMO p.7 (GX-644) | hl correct. |
| episode | 18 | say/scene.q | Ellison: "a good source of capital, and he set up [a] system that allowed Alameda to borrow from FTX." | OK | MEMO p.6 (Tr. 654) | Verbatim. |
| episode | 19 | say/show/scene.q | 2021 Binance buyback; "We don't really have the money for this, we'll have to borrow from FTX to do it." | OK | MEMO p.9 (Tr. 668) | Verbatim. |
| episode | 20 | say/scene.q | "That's okay. I think this is really important, we have to get it done." | OK | MEMO p.9 | Verbatim. |
| episode | 21 | say/show/scene | Per prosecutors: venture investments, political donations, >$100M Bahamas real estate incl. $30M penthouse | OK | MEMO p.10 | Attributed. |
| episode | 22 | say/show/scene.kicker | June 2022 spreadsheet: −$11B on FTX, $13B customer funds borrowed (stated without attribution) | FIX | MEMO p.11 ("As several witnesses testified at trial … That spreadsheet indicated …") | Numbers correct but the claim is unattributed trial evidence. say: "In June two thousand twenty-two, after a crypto market crash, Alameda's lenders demanded their money back. According to trial testimony, a spreadsheet prepared at his request showed Alameda with a negative balance of eleven billion dollars on FTX, borrowing thirteen billion dollars in customer funds." show: "In June 2022, after a crypto market crash, Alameda's lenders demanded their money back. According to trial testimony, a spreadsheet prepared at his request showed Alameda with a negative balance of $11 billion on FTX, borrowing $13 billion in customer funds." scene.kicker: "JUNE 2022 · PER TRIAL TESTIMONY" |
| episode | 23 | say/show/scene | Per prosecutors: of $6.5B repaid, almost 70% customer money | OK | MEMO p.11 | |
| episode | 24 | say/scene | Sept 2022; balcony; "a little short on deliverable"; spending went on | OK | MEMO p.11–12 (Tr. 1407) | Attributed. |
| episode | 25 | say | Chapter title | OK | — | |
| episode | 26 | say/show/scene | Nov 2, 2022 leaked balance sheet; Binance founder's posts; withdrawals; Nov 11 | OK | MEMO p.12 | |
| episode | 27 | say/show/scene | Signal "small group chat": $3.9B of $12B; $8.1B shortfall | OK | MEMO p.13 (GX-406) | Attributed. |
| episode | 28 | say/show/scene | Withdrawals halted; Nov 11 FTX, FTX US, Alameda and related entities; Chapter 11 | OK | MEMO p.14; Chapter 11 at MEMO p.~39 | |
| episode | 29 | say/show | Dec 9 sealed indictment, eight counts; arrested in Bahamas 3 days later; extradited that month | OK | LET p.1; DOJ-CHG ("arrested yesterday", release Dec 13 → Dec 12) | |
| episode | 29 | scene (img/hl/pan) | Doc highlight on letter | FIX | LET p.1 | The hl box sits on the opening paragraph ("does not plan to proceed with a second trial"), not the Dec 9 / eight counts / extradition paragraph, and the current crop (y 0.115–0.66) cuts off before the extradition and Count Eight sentences. Re-crop letter.jpg in make_img.py to `('gov.uscourts.nysd.590940.388.0.pdf',1,0.04,0.96,0.40,0.80)` (and update the crop line in sources.md), then scene.hl: [0.0, 0.43, 1.0, 0.335]; scene.pan: [0.25, 0.35] (verified on a test render). |
| episode | 30 | say/scene.q | Williams: "not a case of mismanagement or poor oversight, but of intentional fraud, plain and simple." | OK | DOJ-CHG | Verbatim. |
| episode | 31 | say/scene.lines/src | Bail revoked "after finding that he had tried to influence witnesses"; screen: "Witness tampering." | FIX | MEMO p.30–31; NPR | Kaplan found *probable cause* of *attempted* witness tampering. He was never charged with or convicted of it, so the bare on-screen "Witness tampering." reads as an established offense. say: "He was released on bail. But before trial, Judge Lewis Kaplan revoked it, finding probable cause that he had tried to tamper with witnesses." scene.lines: ["Bail revoked.", "Attempted witness\|tampering, the judge found."] scene.src: "Gov't sentencing memorandum, Mar 15, 2024 · NPR, Mar 28, 2024" |
| episode | 32 | say | Chapter title | OK | — | |
| episode | 33 | say | 7 of 8 counts tried; Bahamas had not extradited on Count Eight (campaign finance) | OK | LET p.1 | |
| episode | 33 | scene (img/hl/pan) | Title "The Bahamas did not consent to Count Eight" over letter image | FIX | LET p.1 | The current image does not contain the Count Eight / "did not consent" sentences (crop ends at page y=0.66), and the hl box marks the wrong paragraph. With the re-crop from line 29: scene.hl: [0.0, 0.61, 1.0, 0.28]; scene.pan: [0.45, 0.55]. |
| episode | 34 | say/show/scene | ~4-week trial; Ellison, Wang, Singh testified; Wang/Singh co-founders; all three pleaded guilty | OK | CA2 ("four-week trial"); WAPO; SAN; CT | |
| episode | 34 | scene.src | "Washington Post via Spokesman-Review · Second Circuit" | FIX (minor) | SAN; CT | WAPO does not report the guilty pleas. src: "Washington Post via Spokesman-Review · Straight Arrow News · Second Circuit" |
| episode | 35 | say/scene | He testified | OK | CA2 | |
| episode | 36 | say/show | Nov 2, 2023, one year after the Nov 2, 2022 leak; jury deliberated a few hours | OK | DOJ-CONV; WAPO | |
| episode | 37 | say | Guilty on all 7: 2 wire fraud, 2 wire fraud conspiracy, conspiracies to commit securities fraud, commodities fraud, money laundering | OK | DOJ-CONV; JUDG; MEMO p.1 | |
| episode | 37 | scene.hl | Doc hl for "Found guilty on all seven counts" | FIX | JUDG p.1 | Box misses the line "was found guilty on count(s) (S6)1 through (S6)7". scene.hl: [0.0, 0.53, 1.0, 0.27] (verified). |
| episode | 38 | say/scene.q | "has always been about lying, cheating, and stealing" | OK | DOJ-CONV | Verbatim fragment. |
| episode | 39 | say | Chapter title | OK | — | |
| episode | 40 | say/show/scene | Losses: customers ~$8B, investors $1.7B, lenders $1.3B | OK | TR p.6 | |
| episode | 41 | say/show/scene | Gov't 40–50 yrs; defense 63–78 months | OK | MEMO; NPR | Bar value 6.5 = 78 months, consistent with the upper bound used for prosecutors. |
| episode | 42 | say/scene.q | "I'm sorry about what happened at every stage, things I should have done and said, things I shouldn't have. I failed everyone that I care about …" | OK | TR p.33 | Verbatim. |
| episode | 43 | say/scene | "I made a series of bad decisions. They weren't selfish decisions. They weren't selfless decisions. They were bad decisions." | OK | TR p.34 | On-screen "They weren't selfish. / They weren't selfless." trims "decisions"; acceptable as condensed display, spoken text verbatim. |
| episode | 44 | say/show/scene.q | Judge read Ellison testimony: coin flip, $10M | OK | TR p.51–52 | Court: "I am going to read you something else that Caroline Ellison said". q verbatim. |
| episode | 45 | say/scene.q | World-destroyed coin flip | OK | TR p.52 | Verbatim. |
| episode | 46 | say/scene | "that's really a leitmotif in my judgment of this entire case" | OK | TR p.53 | |
| episode | 47 | say/scene.q | "never a word of remorse for the commission of terrible crimes." | OK | TR p.54 | Verbatim. |
| episode | 48 | say/scene | Found he lied at trial; "outright lying"; "evasive, hairsplitting, dodging questions" | OK | TR p.10–11, 57 | Three perjury findings. |
| episode | 49 | say/show/scene.q | "I've been doing this job for close to 30 years. I've never seen a performance quite like that." | OK | TR p.57–58 | Verbatim. |
| episode | 50 | say/scene.q | "But there is a risk that this man will be in a position to do something very bad in the future …"; disabling him | OK | TR p.55 | Verbatim. |
| episode | 51 | say/show/scene | 300 months = 25 years; then 3 years supervised release | OK | TR p.58–59; JUDG p.3 | |
| episode | 52 | say/show/scene.title | Forfeit $11,020,000,000 | OK | JUDG p.7 | |
| episode | 52 | scene.hl | hl box | FIX | JUDG p.7 | Box currently marks "prosecution and court costs" in the payment-order boilerplate. scene.hl: [0.0, 0.49, 1.0, 0.13] (covers the forfeiture line, verified). |
| episode | 53 | say | Chapter title | OK | — | |
| episode | 54 | say/show/scene | Salame 7½ yrs (May 2024); Ellison 2 yrs (Sept 2024); Singh (Oct 2024) and Wang (Nov 2024) avoided prison | OK | NBC; CT; SAN | |
| episode | 55 | say/show/scene | Feb 2026 motion; "newly discovered" witnesses; denied Apr 28, 2026; "wildly conspiratorial and entirely contradicted by the record" | OK | NT p.1–3 | Motion filed Feb 5, 2026; quote verbatim; hl correct. |
| episode | 56 | say | "his claim that all of his victims were paid in full in the bankruptcy? Inaccurate or misleading, the judge wrote." | FIX | NT p.3 | The order calls "his protestations that one or more of [the witnesses] would have supported his claims that FTX was not insolvent and that his victims all were compensated fully in the bankruptcy proceedings" inaccurate or misleading. say: "And his insistence that those witnesses would have backed his claims that FTX was not insolvent, and that his victims were all paid in full in the bankruptcy? Inaccurate or misleading, the judge wrote." |
| episode | 56 | scene.hl | hl box | FIX | NT p.3 | Box misses the line containing "inaccurate or misleading". scene.hl: [0.0, 0.48, 1.0, 0.18] (verified). |
| episode | 57 | say/show/scene | Jun 12, 2026 affirmed; "overwhelming evidence … knowingly and intentionally committed large-scale fraud on FTX's customers" | OK | CA2; MAND | "We AFFIRM the judgment of the district court" (conviction, sentence, forfeiture). hl on "AFFIRMED" correct. |
| episode | 58 | say/scene.q | "he was simultaneously using FTX as his own personal piggy bank" while reassuring the public | OK | CA2 | Preceded by "While he was publicly reassuring customers, investors, and regulators that FTX customer funds were safe,". |
| episode | 59 | say/scene | Pardon requested; Trump said no plans; July Senate unanimous resolution opposing clemency; none granted | OK | BLOCK; UNCH; SF | Attributed to news reports. |
| episode | 60 | say/show/scene | Lawyers petitioned SCOTUS in Sept; No. 26-349 filed Sept 10, 2026; pending | OK | SCOTUS; PET | Filed by counsel; no disposition on docket. |
| episode | 61 | say/scene | "FTX is fine. Assets are fine." | OK | MEMO p.13 | |
| episode | 62 | say/scene | Jury, judge, appellate panel reached same conclusion; money "never his to use" | OK | CA2; TR p.53 | |
| episode | 63 | say | Tagline | OK | — | |

## Shorts

| file | line# | field | claim | verdict | source | fix text |
|---|---|---|---|---|---|---|
| short1 | 0 | say/show/scene | Nov 7, 2022 tweets | OK | MEMO p.13 | |
| short1 | 1 | say/scene.q | "FTX is fine. Assets are fine." | OK | MEMO p.13 | |
| short1 | 2 | say/scene.q | "FTX has enough to cover all client holdings." | OK | MEMO p.13 | |
| short1 | 3 | say/scene | Day before, ~1/3; "HIS OWN DOCUMENT" | OK | MEMO p.13 | "internal document that he authored". |
| short1 | 4 | say/show/scene | Per prosecutors, $3.9B of $12B | OK | MEMO p.13 | |
| short1 | 5 | say/show/scene | Bankruptcy 4 days later; convicted on all 7 counts Nov 2, 2023 | OK | MEMO; DOJ-CONV | |
| short1 | 6 | say | Tagline | OK | — | |
| short1 | meta | title/hook | "FTX Is Fine. Assets Are Fine." — What He Wrote the Day Before / What he knew. | OK | MEMO | |
| short2 | 0 | say/scene | Judge read Ellison's testimony at sentencing | OK | TR p.51 | |
| short2 | 1 | say/show | $10M coin flip | OK | TR p.52 | |
| short2 | 2 | say/scene.q | World-destroyed coin flip | OK | TR p.52 | Verbatim. |
| short2 | 3 | say/scene.q | "that's really a leitmotif in my judgment of this entire case." | OK | TR p.53 | Verbatim. |
| short2 | 4 | say/scene | "not his to use"; "betting on expected value" | OK | TR p.53 | |
| short2 | 5 | say/show/scene | 25 years / 300 months | OK | TR p.58 | |
| short2 | 6 | say | Tagline | OK | — | |
| short2 | meta | title/hook | Coin flip "explained the whole case, according to the judge" | OK | TR p.53 | Matches "leitmotif … of this entire case". |
| short3 | 0 | say/scene.q | Terms of service quote | OK | MEMO p.5 | |
| short3 | 1 | say/scene | Per trial evidence cited by prosecutors, special code features for Alameda | OK | MEMO p.7 | |
| short3 | 2 | say/show/scene | "allow negative" | OK | MEMO p.7 | |
| short3 | 3 | say/show/scene | $65B line of credit; exempt from auto-liquidation | OK | MEMO p.7 | |
| short3 | 4 | say/show | "a spreadsheet showed Alameda borrowing $13 billion" (spoken without attribution; kicker says per prosecutors) | FIX | MEMO p.11 | say: "By June two thousand twenty-two, according to trial evidence, a spreadsheet showed Alameda borrowing thirteen billion dollars in customer funds." show: "By June 2022, according to trial evidence, a spreadsheet showed Alameda borrowing $13 billion in customer funds." |
| short3 | 5 | say/show | "convicted Bankman-Fried of fraud on all seven counts" | FIX | DOJ-CONV; JUDG | One of the seven counts is money-laundering conspiracy, not fraud. say: "In twenty twenty-three, a jury convicted Bankman-Fried on all seven counts, including fraud." show: "In 2023, a jury convicted Bankman-Fried on all 7 counts, including fraud." |
| short3 | 6 | say | Tagline | OK | — | |
| short3 | meta | title/hook | Hidden code / "Allow Negative" | OK | MEMO p.7 | "secretly introduced special features". |
| short4 | meta | title | "Prosecutors Asked for 50 Years. The Defense Asked for 6." | FIX | MEMO; NPR | Prosecutors asked for 40–50 years; defense asked for 63–78 months (5¼–6½ years). title: "Prosecutors Asked for 40–50 Years. The Defense Asked for About 6. Here's What SBF Got" |
| short4 | meta | hook | "40–50 years?\|Or 6?" | FIX | NPR | hook: "40–50 years?\|Or about 6?" |
| short4 | 0 | say/show | Mar 28, 2024 sentencing in Manhattan | OK | TR | |
| short4 | 1 | say/show/scene | 40–50 yrs vs 63–78 months | OK | MEMO; NPR | |
| short4 | 2 | say/scene.q | Lied at trial; "And when he wasn't outright lying, he was often evasive, hairsplitting, dodging questions …" | OK | TR p.10, 57 | Verbatim. |
| short4 | 3 | say/show/scene.q | "close to 30 years … performance" | OK | TR p.57–58 | |
| short4 | 4 | say/scene.q | "never a word of remorse …" | OK | TR p.54 | |
| short4 | 5 | say/show/scene | 300 months / 25 years; forfeiture ~$11B / $11.02B | OK | JUDG p.3, 7 | |
| short4 | 6 | say | Tagline | OK | — | |
| short5 | 0 | say/scene | Ellison, Wang, Singh; all pleaded guilty | OK | SAN; CT; WAPO | |
| short5 | 0 | scene.src | "Washington Post via Spokesman-Review" | FIX (minor) | SAN; CT | WAPO does not report the pleas. src: "Washington Post via Spokesman-Review · Straight Arrow News" |
| short5 | 1 | say/scene.q | Ellison: "We don't really have the money …" | OK | MEMO p.9 | |
| short5 | 2 | say/scene | Singh: balcony, "a little short on deliverable" | OK | MEMO p.12 (Tr. 1407) | |
| short5 | 3 | say/show/scene | All seven counts; 25 years; Mar 28, 2024 | OK | DOJ-CONV; TR | |
| short5 | 4 | say/show/scene | Ellison 2 yrs; Singh, Wang no prison; Salame 7½ | OK | NBC; CT; SAN | Script doesn't claim Salame testified (SAN: he did not). |
| short5 | 5 | say | Tagline | OK | — | |
| short5 | meta | title/hook | "They Testified Against SBF" | OK | — | |
| short6 | 0 | say/show | 2024: sentenced to 25 years | OK | JUDG; TR | |
| short6 | 0 | scene.hl | Kicker "JUDGMENT · 300 MONTHS"; hl box | FIX | JUDG p.3 | Box stops just above "aggregate term of imprisonment of 300 months". scene.hl: [0.0, 0.88, 1.0, 0.11] (verified). |
| short6 | 1 | say/show/scene | April 2026 denial; "wildly conspiratorial" | OK | NT p.3 | |
| short6 | 2 | say/scene | June 2026 affirmed; evidence "overwhelming" | OK | CA2; MAND | |
| short6 | 3 | say/scene | Pardon requested; Trump no plans; none granted | OK | BLOCK; UNCH; SF | |
| short6 | 4 | say/scene | Sept 2026 petition No. 26-349 filed Sept 10, pending | OK | SCOTUS | |
| short6 | 5 | say | Tagline | OK | — | |
| short6 | meta | title/hook | Where the case stands (2026) | OK | — | |

## meta.json / thumb.json

| file | line# | field | claim | verdict | source | fix text |
|---|---|---|---|---|---|---|
| meta | — | title | "FTX Is Fine" — tweets, coin flip, 25-year sentence | OK | MEMO; TR | |
| meta | — | summary | Nov 7 tweet; bankrupt 4 days later; built from listed filings; 25 years; status | OK | MEMO; TR; JUDG; CA2 | |
| thumb | — | A words/hook | "FTX IS FINE?" / "THE TWEET VS. THE TRUTH" | OK | MEMO p.13 | |
| thumb | — | C words/hook | "25 YEARS" / "THE COIN FLIP" | OK | TR | |

## Summary

- Lines checked: 104 script lines (episode 64 + shorts 40) plus meta.json (title, summary), thumb.json (2 variants) and the 6 short titles/hooks.
- FIX items: 15. Substantive: 7 (ep 22 attribution; ep 31 witness-tampering finding; ep 56 the scope of "inaccurate or misleading"; short3 4 attribution; short3 5 "of fraud"; short4 title; short4 hook). Document image/highlight: 6 (ep 29 and ep 33 letter crop+hl, ep 37, ep 52, ep 56, short6 0). Source line: 2 (ep 34 src, short5 0 src).
- All on-screen quotations were checked against the transcript, memo, indictment, orders and DOJ releases and are verbatim. No private victims are named. Counts not tried (campaign finance, bribery etc.) are never presented as convictions. The status claims (affirmed Jun 12, 2026; mandate Aug 4, 2026; cert No. 26-349 filed Sept 10, 2026 and pending; pardon requested, none granted; July 2026 unanimous Senate resolution) match the cited sources.
- Overall verdict: **PUBLISHABLE after fixes.**


## Applied
All 15 FIX items above were applied to make_spec.py / make_shorts.py / make_img.py (letter.jpg re-cropped) before the final build, 2026-11-02.
