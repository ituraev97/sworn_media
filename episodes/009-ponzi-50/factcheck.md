# Fact-check — SWORN 009 · 5 Ponzi Schemes That Ended in 50+ Years in Prison (countdown)

Checked 2026-11-09 by an independent checker against the documents themselves (sources.md used only as a pointer):
- **RR_SENT**: USAO S.D. Fla. release, Jun 9, 2010 (local 100609-01.html).
- **RR_PLEA**: USAO S.D. Fla. release, Jan 27, 2010 (local 100127-01.html).
- **RR_AP**: AP via Washington Times, Apr 16, 2018 (WebFetch).
- **PT_AFF**: Criminal complaint + affidavit of FBI SA Dan Harris, D. Minn. 08-MJ-364, Dkt. 26, Oct 2, 2008 (OCR of pet26-1…8).
- **PT_PR**: USAO D. Minn. release, Apr 8, 2010 (petpr.pdf, pdftotext). **FBI-MN**: FBI Minneapolis release, Apr 8, 2010 (WebFetch, same text).
- **PT_GOV**: Gov't Position Regarding Sentencing, Dkt. 388, Mar 8, 2010 (pdftotext).
- **PT_VER**: Jury verdict, Dkt. 361, Dec 2, 2009 (OCR pp. 1–2). **PT_JUD**: Judgment, Dkt. 400, Apr 8, 2010 (OCR pp. 1–2). **PT_DKT**: D. Minn. docket 0:08-cr-00364.
- **KARE**: KARE 11, "Petters conviction upheld by federal appeals court" (WebFetch). **STRIB**: Star Tribune, "Supreme Court won't pick up Petters appeal" (WebFetch).
- **OK_REL**: USAO E.D. Va. release, Nov 17, 2011 (local 20111117okunnr.html).
- **OK_OP**: Memorandum Opinion, U.S. v. Okun, E.D. Va. 3:08cr132, Dkt. 324, Aug 27, 2009 (OCR pp. 1–3).
- **OK_BOP / OK_FLS**: BOP inmate-locator record (Okun 81060-004, FMC Butner, "actual release date 04/09/2020") and the Free Lance-Star headline "Edward Okun, who was sentenced to 100 years in massive fraud case, dies in prison" (body paywalled), both as reported by the writer; one WebSearch ("Edward Okun 1031 Tax Group dies in prison 2020") returned only 2009–2011 coverage, so nothing independent corroborates the year.
- **Stanford**: episodes/004-stanford/sources.md + factcheck.md (CMP, PRS, BR, CA5, DAVIS, BOP), and images img/st_cmp.jpg (CMP p.1), st_tier.jpg (BR p.42), st_sent.jpg (DOJ release, Jun 14, 2012), read directly.
- **Madoff**: episodes/001-madoff/factcheck.md + make_spec.py (ARREST, PLEA-PR, SENT-PR), and **MD_AP**: AP via OPB, Apr 14, 2021 (WebFetch).

Lines without a `show` field use the `say` text as the subtitle. Line numbers are 0-based indexes into `lines`.

## Long episode (episode.json)

| # | First words | Status | Note / evidence |
|---|---|---|---|
| 0 | How long can a Ponzi scheme put you in prison? | OK | Sentences 50, 50, 100, 110, 150 (RR_SENT, PT_JUD, OK_REL, PRS, SENT-PR). Scene "50 years / or more." OK. |
| 1 | A lawyer whose firm sold lawsuit settlements that never existed… | OK | RR_SENT "In both instances, the purported investment vehicles never existed"; PT_PR Coleman (office manager, hired by Petters) wore a recording device; OK_REL "misappropriated approximately $126 million in client funds"; SIB is an Antigua bank (PRS). Bars 50/50/100/110/150 and src dates all match the releases. |
| 2 | Two got fifty years. One got a hundred… | OK | As above; numbers say = show. |
| 3 | Every fact in this countdown comes from court records… | OK | Title/sub contain no factual claim beyond the five sentences. |
| 4 | Number five. Fifty years. | OK | RR_SENT "sentenced Rothstein to 50 years in prison". |
| 5 | Scott Rothstein was a lawyer in Fort Lauderdale, Florida… | OK | RR_SENT "attorney Scott Rothstein, 47, of Fort Lauderdale … operation of a $1.2 billion Ponzi scheme through the defunct Ft. Lauderdale law firm Rothstein Rosenfeldt and Adler"; RR_PLEA "his law firm". Title "A billion-dollar Ponzi scheme" = release headline "BILLION DOLLAR PONZI SCHEME". |
| 6 | The pitch: confidential settlements of civil lawsuits… | OK | RR_SENT "purported confidential civil settlement agreements … could be purchased at a discount and would be repaid over time to the investors at full face value … investors were told that these funds would be held in the trust account of RRA." |
| 7 | In both instances, the purported investment vehicles never existed. | OK (note) | Verbatim RR_SENT. NOTE: "both instances" refers to the bridge-loan and settlement schemes; the episode only describes the settlement scheme, so "both" has no antecedent for the viewer. Optional say: "The purported investment vehicles, the Justice Department said, never existed." (doc highlight can stay). |
| 8 | To make them look real, prosecutors said… | OK | RR_SENT "created and caused the creation of false bank documents, false on-line bank account information, and false settlement agreements and promissory notes, which were shown to investors". List items match. |
| 9 | Then they went further. Without its clients' knowledge… | **FIX** | RR_SENT "defrauded clients of RRA in a civil suit initiated by RRA on their behalf as plaintiffs. Without the clients' knowledge, RRA settled the lawsuit in favor of the defendant, thereby obligating the clients to pay $500,000 … created a false federal court order, purportedly signed by a U.S. District Judge, stating that the clients had won the lawsuit and were owed a judgment of approximately $23 million." "settled one of their lawsuits against them" is ambiguous (it can be heard as a lawsuit *against the clients*). Rest of line OK. **say:** "Then they went further. Without its clients' knowledge, his firm had settled a lawsuit it filed for them, in the other side's favor. To hide it, prosecutors said, they created a false federal court order, purportedly signed by a U.S. District Judge, saying the clients had won about twenty-three million dollars." **show:** same with "$23 million". |
| 10 | To collect it, the clients were told to post bonds… | OK | RR_SENT "the clients were required to post bonds … caused the clients to wire transfer approximately $57 million to a trust account he controlled". |
| 11 | From around two thousand five through November two thousand nine… | OK | RR_PLEA "from around 2005 through November 2009 … fraudulently obtained approximately $1.2 billion from investors". Stat "$1.2B obtained from investors" OK. |
| 12 | He pleaded guilty to five counts, including racketeering conspiracy… | OK | RR_SENT: plea to RICO conspiracy, money-laundering conspiracy, mail/wire-fraud conspiracy, two wire-fraud counts (5); "U.S. District Court Judge James I. Cohn sentenced Rothstein to 50 years"; dated June 9, 2010. Kicker "FORT LAUDERDALE": case no. 0:09-cr-60331 (Fort Lauderdale division) — acceptable. |
| 13 | He went on to cooperate with prosecutors. But in two thousand eighteen… | OK | RR_AP: Judge Cohn "granted a federal prosecutor's motion Monday to withdraw an earlier offer to reduce Scott Rothstein's sentence"; "Prosecutors say Rothstein failed to comply with his plea agreement by providing false information to the government"; dated Apr 16, 2018. Cooperation per his attorney in RR_AP; an offer to reduce the sentence presupposes it. |
| 14 | Number four. Also fifty years. | OK | PT_JUD "600 months - 50 years". |
| 15 | Tom Petters, of Wayzata, Minnesota, bought companies… | OK | PT_PR "of Wayzata"; "The companies he bought were purchased with proceeds of the PCI fraud, and they included Fingerhut, Polaroid, and Sun Country Airlines, which, collectively, became known as Petters Group Worldwide". Attributed to DOJ. |
| 16 | At the center was Petters Company, Inc. Investors lent it money… | OK (note) | PT_PR "inducing investors to provide Petters Company, Inc., ('PCI') funds to purchase merchandise that was to be resold to retailers at a profit. However, no such purchases were made."; "lending Petters money purportedly to buy electronic goods to be sold to big-box retailers, such as Costco and Sam's Club". Scene title "entirely fabricated" = PT_AFF ¶7d "The purchase orders and other documents in support of the transactions are entirely fabricated" — NOTE: that is the cooperating witness's account as relayed in the affidavit ("the CW informed the government that"); fine under the "FBI AFFIDAVIT" kicker, but see short2 #1. |
| 17 | A Walmart security official told agents… | OK | PT_AFF ¶9a "The Wal-Mart official reported that PCI's purported vendor number on the Sam's Club purchase order was fictitious." (official = "a security official for Wal-Mart Stores, Inc."). |
| 18 | From two thousand three to September two thousand eight, about thirty-five billion… | OK | PT_PR "PCI opened a new bank account that only Petters and Coleman were authorized to use. From January 2003 to September 2008, approximately $35 billion was wired into that account … none of the deposits into the account came from retailers." Coleman was "hired by Petters as an office manager in 1993" → "one employee" OK. |
| 19 | That employee was Deanna Coleman… | OK | PT_PR "began on September 8, 2008, when co-conspirator Deanna Coleman and her attorney reported to authorities"; "She wore a recording device". Coleman is a convicted co-conspirator, not a private victim. |
| 20 | Within the first few hours of her recordings… | OK | PT_PR verbatim: "Within the first few hours of Coleman's recorded conversations, Petters was heard admitting that purchase orders were 'fake' and claiming 'divine intervention' was the only explanation for how he and his co-conspirators 'could of got away with this for so long.'" Quoted fragments in show are verbatim. |
| 21 | On the recordings, the FBI agent wrote, Petters also talked about fleeing… | OK | PT_AFF ¶12a "PETTERS talks about fleeing the country and creating fabricated defenses". PT_PR "On September 24, 2008 … executed search warrants at Petters's headquarters, Petters's home"; "On October 3, Petters was arrested". |
| 22 | Petters went to trial. On December second, two thousand nine… | OK | PT_PR "Following a month-long trial, Petters was convicted on December 2, 2009" (10+3+1+1+5 = 20 counts); PT_JUD "found guilty on count(s) 1-20 after a plea of not guilty"; PT_DKT superseding indictment charged Petters with 1s–20s, verdict "Guilty on Counts 1s-10s,11s-13s,14s,15s,16s-20s" → "all twenty" OK. PT_GOV "a life sentence, which in this case gives rise to the maximum statutory sentence permitted by the counts of conviction (335 years)". |
| 23 | On April eighth, two thousand ten, Judge Richard Kyle gave him six hundred months… | OK | PT_JUD "total term of 600 months - 50 years", signed Richard H. Kyle, Apr 8, 2010; PT_PR "represents the longest term of imprisonment ever ordered in a financial fraud case in Minnesota history" (attributed). |
| 24 | On Petters' own testimony at trial, the judge said… | OK | PT_PR "while referring to the lack of believability in Petters's trial testimony, Judge Kyle said, 'It just didn't pass the smell test.'" Cite "As quoted in" correct. |
| 25 | A federal appeals court upheld the conviction and the sentence… | OK (note) | KARE: the Eighth Circuit "upheld the 2009 conviction and 50-year prison sentence"; STRIB: Supreme Court denied his petition for review. NOTE: the scene stamps "GUILTY · DECEMBER 2, 2009" over the appeals narration — accurate facts, just not the event being narrated; optional kicker "8TH CIRCUIT · SUPREME COURT", stamp "UPHELD". |
| 26 | Number three. One hundred years. And the smallest dollar figure on this list. | OK (note) | Okun's $126M (OK_REL) is below Rothstein $1.2B, Petters $3.7B (PT_PR), Stanford $7B (PRS), Madoff ~$50B (ARREST). The measures differ (misappropriated vs. obtained vs. losses), and smaller figures ($15,000, $23M, $57M) also appear in the episode. Optional: "And the smallest fraud on this list." |
| 27 | Edward Okun owned The ten thirty-one Tax Group… | OK | OK_REL "the former owner of The 1031 Tax Group LLP"; "Section 1031 of the Internal Revenue Code allows investment property owners to defer the capital gains tax … if the proceeds are used to purchase new property in a specified time frame … deposit the proceeds of property sales with qualified intermediaries". List items match. |
| 28 | Clients were promised their money would be used solely for those exchanges… | OK | OK_REL "promising clients that their money would be used solely to effect 1031 exchanges … evidence showed that Okun and others misappropriated approximately $126 million in client funds". |
| 29 | It paid for his lavish lifestyle, his companies' expenses… | OK | OK_REL "to support his lavish lifestyle, pay operating expenses for his various companies, invest in commercial real estate, and purchase additional qualified intermediary companies to obtain access to additional client funds." |
| 30 | The trial judge, Robert Payne, put it this way. | OK | OK_REL "U.S. District Judge Robert E. Payne"; OK_OP case 3:08-cr-00132-REP, filed 08/27/09. Title "somewhat unconventional" verbatim. |
| 31 | In sum, Okun was running a large, somewhat unconventional Ponzi scheme. | OK | OK_OP p.2 verbatim: "In sum, Okun was running a large, somewhat unconventional Ponzi scheme." Cite correct. |
| 32 | The evidence also showed he had employees withdraw fifteen thousand dollars… | OK | OK_REL "Okun instructed his employees in Richmond to withdraw $15,000 in cash … and smuggle the cash to his personal yacht on Paradise Island in the Bahamas to avoid federal currency reporting requirements." |
| 33 | On March nineteenth, two thousand nine, a jury in Richmond… | OK | OK_REL "convicted by a federal jury in Richmond, Va., on March 19, 2009, of conspiracy to commit mail and wire fraud, wire fraud, conspiracy to commit money laundering, money laundering, bulk cash smuggling and perjury. He was sentenced by U.S. District Judge Robert E. Payne on Aug. 4, 2009, to 100 years". |
| 34 | In two thousand eleven, the Fourth Circuit upheld… | OK | OK_REL, Nov 17, 2011: "the Fourth Circuit upholding the conviction and 100-year sentence". |
| 35 | Financial fraudsters make calculated, rational decisions… | OK | OK_REL verbatim, "said U.S. Attorney MacBride" (Neil H. MacBride). Statement is in his own office's release, so no "As quoted in" needed. |
| 36 | Number two. One hundred and ten years. | OK | PRS / st_sent "sentenced to a total of 110 years". |
| 37 | R. Allen Stanford was chairman of the board of Stanford International Bank… | OK | st_sent: "R. Allen Stanford, the former Board of Directors Chairman of Stanford International Bank (SIB)" (former as of 2012; chairman during the scheme). Antigua: PRS. CMP ¶3 approx. $8 billion of CDs by year-end 2008, attributed to the SEC. |
| 38 | For at least a decade, the SEC alleged, Stanford and his chief financial officer… | OK | st_cmp ¶1 "For at least a decade, R. Allen Stanford and James M. Davis, through companies they control … executed a massive Ponzi scheme." Davis = former CFO of Stanford Financial Group entities (004 [DAVIS]). "alleged" correct for a complaint. |
| 39 | Where did the money go? According to the government's appeals brief… | OK (note) | st_tier (BR p.42): "25% of the bank's reported assets, Tier 1 and Tier 2, were invested consistently with its annual reports and marketing materials … Stanford siphoned the remaining 75% of the bank's assets, 'Tier 3,' to his companies, real estate purchases, and lifestyle." NOTE: "which insiders called Tier Three" is a light gloss; the brief says "many employees knew about the existence of 'Tier 3'", so it was an internal label — acceptable. |
| 40 | In March two thousand twelve, a Houston jury convicted him on thirteen of fourteen counts… | OK | st_sent "convicted on 13 of 14 counts by a federal jury … before U.S. District Judge David Hittner"; PRC Mar 6, 2012, Houston; "110 years … for orchestrating a 20-year investment fraud scheme in which he misappropriated $7 billion". |
| 41 | The judge called it one of the most egregious frauds… | OK | PRS: Hittner "this is one of the most egregious frauds ever presented to a trial jury in federal court" (verbatim, checked in 004). Cite "As quoted in" correct. |
| 42 | The Fifth Circuit affirmed. The Bureau of Prisons lists… | OK | CA5 "we AFFIRM" (Oct 29, 2015); BOP projected release 03/13/2103 (004, checked 2026-11-04). |
| 43 | Number one. One hundred and fifty years. | OK | SENT-PR. |
| 44 | On December tenth, two thousand eight, according to federal prosecutors… | OK | ARREST: on Dec 10, 2008 Madoff told senior employees the advisory business was a fraud, "it's all just one big lie", "basically, a giant Ponzi scheme" (001 factcheck lines 0–1). |
| 45 | He estimated the losses at approximately fifty billion dollars, at least. | OK | ARREST "at least approximately $50 billion" (wording already corrected in 001). |
| 46 | He was arrested the next day. In March two thousand nine… | OK | ARREST (Dec 11); PLEA-PR Mar 12, 2009, guilty plea to the 11-count information → "all eleven counts" OK; no trial. |
| 47 | On June twenty-ninth, two thousand nine, Judge Denny Chin… | OK | SENT-PR: 150 years; "extraordinarily evil". |
| 48 | And he said it was not merely a bloodless crime… | OK | SENT-PR verbatim "not merely a bloodless crime that takes place on paper but one that takes a staggering human toll." Cite "As quoted in" correct. |
| 49 | Madoff died in federal prison in April two thousand twenty-one. He was eighty-two. | OK | MD_AP "died early Wednesday, April 14, 2021, in a federal prison … He was 82." (FMC Butner). |
| 50 | Five schemes. Look at what they ran on… | OK (note) | Purchase orders (PT_PR); fake settlements (RR_SENT); "false federal court order, purportedly signed by a U.S. District Judge" (RR_SENT); safekeeping promises (OK_REL "promises … regarding the safekeeping and use of exchange funds"); false statements (Madoff PLEA; Stanford BR). List items OK. NOTE: "Settlements of lawsuits that were never settled" sits awkwardly beside line 9, where the firm *did* settle a lawsuit; optional: "Settlements that never existed." |
| 51 | Two pleaded guilty. Three went to trial and lost… | OK | Pleas: Rothstein (RR_PLEA), Madoff (PLEA-PR). Trials: Petters (PT_JUD "after a plea of not guilty", jury verdict), Okun (jury, OK_REL), Stanford (jury, 13 of 14). All ≥ 50 years. Bars match. |
| 52 | Madoff died in prison. Edward Okun died in federal custody in two thousand twenty… | **FIX** | Madoff: MD_AP. Stanford: BOP (USP Coleman II, release 2103). Petters: KARE, STRIB (plus § 2255 denial, PT_DKT Dkt. 628). Rothstein: RR_AP. **Okun:** the only Free Lance-Star evidence is a headline, "…dies in prison", with no year; the year 2020 comes from a BOP locator "actual release date 04/09/2020", which the paper is not known to have reported and which does not itself say "died". As written, the year is attributed to a source that has not been read. **say:** "Madoff died in prison. Edward Okun died in prison, the Free Lance-Star of Virginia reported. Stanford is still in federal prison. Petters and Rothstein lost their bids for relief." **show:** same. (If the year must stay: "…the Free Lance-Star of Virginia reported; federal prison records list his release in April twenty twenty." — and add "Federal Bureau of Prisons inmate locator (Okun)" to scene.src.) |
| 53 | This is SWORN. Real trials. Real evidence. The verdict. | OK | Brand tagline. |

## Short 1 (short1.json) — title "50 to 150 Years: 5 Ponzi Schemes, Ranked" · hook "50 → 150|YEARS"

| # | First words | Status | Note / evidence |
|---|---|---|---|
| T | title / hook | OK | Sentences 50–150 as above; ranked by sentence. |
| 0 | Fifty years. Fifty. One hundred… | OK | Same five sentences; bars OK. |
| 1 | Fifty: Scott Rothstein, a lawyer whose firm sold settlements that never existed… | OK | RR_SENT; PT_PR "no such purchases were made"; electronics per PT_PR. |
| 2 | One hundred: Edward Okun, who took clients' tax-exchange money… | OK | OK_REL; PRS (Antigua bank). |
| 3 | And one hundred fifty years: Bernie Madoff. | OK | SENT-PR, Jun 29, 2009. |
| 4 | Real trials. Real evidence. The verdict. | OK | Tagline. |

## Short 2 (short2.json) — title '"Divine Intervention": How a $3.7B Ponzi Got Caught' · hook "“DIVINE|INTERVENTION”"

| # | First words | Status | Note / evidence |
|---|---|---|---|
| T | title / hook | OK | PT_PR headline "orchestrating $3.7 billion Ponzi scheme"; "divine intervention" verbatim; the case began with Coleman's report and recordings (PT_PR). |
| 0 | Divine intervention. That, the Justice Department said… | OK | PT_PR (quote as in line 20). "recorded by his own employee": Coleman was "hired by Petters as an office manager in 1993" and "wore a recording device to tape conversations with Petters". |
| 1 | Investors lent his company money to buy electronics for Costco and Sam's Club… | **FIX** | PT_PR supports the first two sentences. But "The FBI called the purchase orders entirely fabricated" misattributes: in PT_AFF ¶7d the phrase is the cooperating witness's account ("During the proffer and in subsequent interviews the CW informed the government that: … d. The purchase orders and other documents in support of the transactions are entirely fabricated."). **say:** "Investors lent his company money to buy electronics for Costco and Sam's Club. No such purchases were made. In an FBI affidavit, a cooperating witness called the purchase orders entirely fabricated." **show:** "Investors lent his company money to buy electronics for Costco and Sam's Club. No such purchases were made. In an FBI affidavit, a cooperating witness called the purchase orders \"entirely fabricated.\"" |
| 2 | A three point seven billion dollar Ponzi scheme. Guilty on all twenty counts. Fifty years. | OK | PT_PR "$3.7 billion Ponzi scheme"; PT_JUD guilty on counts 1–20 (all counts charged in the superseding indictment, PT_DKT); 600 months – 50 years. Scene "APRIL 8, 2010 · ST. PAUL" = PT_PR ("earlier this morning in St. Paul"). |
| 3 | Real trials. Real evidence. The verdict. | OK | Tagline. |

## Short 3 (short3.json) — title "$57 Million to Collect a Win. The Court Order Was Fake." · hook "$57 MILLION|FAKE COURT ORDER"

| # | First words | Status | Note / evidence |
|---|---|---|---|
| T | title / hook | OK | RR_SENT "$57 million"; "false federal court order … stating that the clients had won the lawsuit". |
| 0 | Fifty-seven million dollars. That's what one law firm's clients wired… | OK | RR_SENT ($57M wired "purportedly to satisfy the bonds"; judgment of approx. $23M in the false order). Label "wired to post “bonds”" OK. |
| 1 | The firm had secretly settled their case against them… | **FIX** | RR_SENT "Without the clients' knowledge, RRA settled the lawsuit in favor of the defendant". "settled their case against them" is ambiguous (sounds like a case brought against the clients). **say:** "The firm had secretly settled their lawsuit, in the other side's favor. Then came a false federal court order, purportedly signed by a U.S. District Judge." |
| 2 | Behind it, prosecutors said, was attorney Scott Rothstein… | OK (note) | RR_SENT/RR_PLEA $1.2 billion; 50 years; Jun 9, 2010. NOTE: the $1.2B covered both the settlement and the bridge-loan schemes; "on settlements that never existed" is a simplification. Optional: "on settlements and loans that never existed." |
| 3 | Real trials. Real evidence. The verdict. | OK | Tagline. |

## meta.json / thumb.json

| Field | Text | Status | Note / evidence |
|---|---|---|---|
| meta.title | 5 Ponzi Schemes That Ended in 50+ Years in Prison | OK | All five sentences ≥ 50 years. |
| meta.summary | Five Ponzi schemes, five federal sentences… FBI affidavits, jury verdicts, judgments, SEC complaints and the Justice Department's own releases. | OK | Names and years correct; source types used (plus AP/local press for aftermath — fine). |
| thumb.A | words "50+|YEARS", hook "5 PONZI SCHEMES" | OK | — |
| thumb.C | words "150|YEARS", hook "THE #1 PONZI SENTENCE" | **FIX** | Read alone on a thumbnail this is a superlative ("the longest Ponzi sentence ever"), which no source here supports (longer fraud sentences exist). It is only #1 within this countdown. **hook:** "#1 ON THE LIST" (or "#1 OF 5"). |

## Summary

- Lines checked: 54 (episode) + 5 (short1) + 4 (short2) + 4 (short3) = 67 lines, plus 3 Short titles/hooks, meta title/summary and 2 thumbnails.
- **FIXes: 5** — episode #9 (ambiguous "settled one of their lawsuits against them"), episode #52 (Okun's 2020 death year attributed to the Free Lance-Star, which has only been seen as an undated headline), short2 #1 ("The FBI called" → cooperating witness in an FBI affidavit), short3 #1 (ambiguous "their case against them"), thumb C hook ("THE #1 PONZI SENTENCE" superlative).
- Optional NOTEs: episode #7 ("both instances"), #16 (affidavit phrase is the CW's), #25 (scene stamps the verdict over appeals narration), #26 ("smallest dollar figure"), #39 ("insiders called"), #50 ("lawsuits that were never settled"), short3 #2 ("on settlements").
- Specifically verified as OK: "chairman" (DOJ "former Board of Directors Chairman of SIB"); "all twenty counts" (judgment counts 1–20; superseding indictment 1s–20s); "all eleven counts" (11-count information); "Three went to trial and lost / two pleaded guilty"; Stanford's "chief financial officer" (Davis); "about a quarter … invested" (BR: 25% "invested consistently with its annual reports and marketing materials"); Polaroid "purchased with proceeds of the PCI fraud"; account "only Petters and Coleman were authorized to use"; "Guilty on all 20 counts"; "$3.7 billion"; "recorded by his own employee"; bars/list scenes.
- No private victims are named (Coleman is a convicted co-conspirator; the Petters verdict page naming a lender is not shown).

## Re-check (2026-11-09, after fixes; episode.json now 56 lines)

| File · # | First words | Status | Note / evidence |
|---|---|---|---|
| episode 7 | The Justice Department put it plainly… | OK | RR_SENT "the purported investment vehicles never existed". |
| episode 9 | Then they went further… settled a lawsuit it filed for them, in the other side's favor | OK | RR_SENT "civil suit initiated by RRA on their behalf as plaintiffs … settled the lawsuit in favor of the defendant". |
| episode 19 (NEW) | The money passed through two so-called vendors… | OK | PT_PR p.3: "Petters recruited purported vendors" (NIR and EFBC); "Catain created a sham company, Enchanted Family Buying Co. … EFBC did no real business. In fact, its headquarters was above Catain's car wash, just a few miles from Petters's headquarters"; p.3–4 "Although each company was purportedly a vendor … money only flowed one way – from the companies to PCI." Scene "THE "VENDORS" · PER THE JUSTICE DEPARTMENT" / "Above a car wash." OK. |
| episode 20 | That employee was Deanna Coleman… | **FIX** | The new line 19 now sits between line 18 ("one account that only Petters and one employee were authorized to use") and this line, so "That employee" has lost its antecedent (the nearest noun is the sham vendor company). **say:** "The employee who shared that account was Deanna Coleman. On September eighth, two thousand eight, she and her attorney went to the authorities. She agreed to wear a recording device." **show:** "The employee who shared that account was Deanna Coleman. On September 8, 2008, she and her attorney went to the authorities. She agreed to wear a recording device." |
| episode 40 | Where did the money go?… known as Tier Three | OK | BR p.42 "the remaining 75% of the bank's assets, 'Tier 3,'". |
| episode 46 (NEW) | Months earlier, in a January two thousand eight filing with the SEC… | OK | md_lie (ARREST): "According to a document filed by MADOFF with the United States Securities and Exchange Commission ("SEC") on January 7, 2008, MADOFF's investment advisory business served between 11 and 25 clients and had a total of approximately $17.1 billion in assets under management." Numbers say = show; scene "$17.1 billion / 11 to 25 clients", kicker "JANUARY 2008 · FILED WITH THE SEC", src Dec 11, 2008 release OK. |
| episode 47 | He estimated the losses at approximately fifty billion dollars, at least. | **FIX** | Because the new line 46 goes back to January 2008, "He estimated the losses…" now reads as if the estimate was made in that filing. ARREST: on December 10, 2008 he "estimated the losses from this fraud to be at least approximately $50 billion". **say:** "That December, he estimated the losses at approximately fifty billion dollars, at least." **show:** "That December, he estimated the losses at approximately $50 billion, at least." (Scene kicker "DECEMBER 2008 · MADOFF'S OWN ESTIMATE" already correct.) |
| episode 52 | Five schemes… Settlements that never existed… | OK | RR_SENT. |
| episode 54 | Madoff died in prison. Edward Okun died in prison, the Free Lance-Star… | OK | Year removed; matches the FLS headline "…dies in prison". scene.src still lists the BOP locator, which is correct for Stanford. |
| short2 1 | …In an FBI affidavit, a cooperating witness called the purchase orders entirely fabricated. | OK | PT_AFF ¶7d. |
| short3 1 | The firm had secretly settled their lawsuit, in the other side's favor… | OK | RR_SENT. |
| short3 2 | …built on settlements and loans that never existed… | OK | RR_SENT (loans to "non-existent borrowers" and settlements). |
| thumb C | hook "#1 OF 5" | OK | Ranked within the countdown only. |

Re-check result: 2 new lines verified OK; all 5 applied FIXes and 4 applied NOTEs read correctly; **2 new FIXes** (episode lines 20 and 47), both caused by where the new lines were inserted.

**Applied (2026-11-09, before the final build):** both re-check FIXes (lines 20 and 47) and all 5 first-pass FIXes. Total FIXes applied: 7 (+4 wording notes).
