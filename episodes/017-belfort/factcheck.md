# SWORN 017 (Belfort): fact-check

Independent check of episode.json, short1-3.json, thumb2.json and meta.json against sources.md, the local court PDFs (mtc / gil / las / l9 / l12 / l16), caldwell.txt, and the web sources (AP via Lincoln Daily News, Bloomberg 2013, Bloomberg 2018 via Fortune and BNN, CNBC, TMZ, Celebrity Net Worth, Startup Fortune, Analytics Insight, Cornell LII). Checked Nov 17, 2026.

## Summary
- **FIX items: 26** (episode 16, shorts 5, thumbnail 3, meta 2). Everything else is OK or a NOTE.
- **Most serious:**
  1. E[48]: "isn't just a con, but also a deadbeat" is **Bloomberg's own lead sentence** ("…, prosecutors say"). It is not a quote from prosecutors, but the script and the quote card attribute it to "FEDERAL PROSECUTORS". Bloomberg also does not say the $9M claim was in "court papers".
  2. Allegation labels in the 1MDB section: E[25] and E[26] state the theft as fact. Short2 [2] cuts the "according to the allegations in the complaint" qualifier out of the DOJ quote, and the short2 title answers "who paid" as if it were fact.
  3. **The expiry date is contested.** Bloomberg (May 16, 2018) says Belfort "was released from prison in April 2008", which would put the § 3613(b) end date in 2028. TMZ's sources and Celebrity Net Worth (release Apr 28, 2006) put it at April 28, 2026. The narration attributes the date correctly ("per TMZ's sources"). But the title "Then It EXPIRED", thumbnail B "THEN THE CLOCK RAN OUT", the first comment, and the E[4] kicker state it without attribution.
  4. E[55] "Dismissed.": the April 8, 2022 letter only *requests* dismissal ("subject to dismissal"). No dismissal order is in the sources. (The RECAP docket at archive.org could not be fetched.)
  5. E[10] "testify … against other defendants": not in AP or Bloomberg. AP says "agreed to become a government witness".
  6. Short3 hook tag "GUILTY" sits on the 2017–18 company-expenses ($9.19M) matter. That implies a crime where there was only a civil collection motion and no finding.
- **Doc images:** every "hl" band covers the passage being narrated (two optional widenings are noted below). Private names (partner, bookkeeper) are blacked out on gil_1, gil_2 and mtc_6. Children's names do not appear on any shown page; they appear only on gil p.3, which is not used. No DOJ seal is visible on l9_2, l12_1 or l16_1, where the header area is cleaned. cald.jpg is a re-typeset page with no seal.
- **Say vs show:** the numbers match in every line that has both fields. Several lines have no "show" field, so their subtitles would carry spelled-out numbers (see NOTE N-show).

## Table
Index = 0-based position in "lines". E = episode.json, S1/S2/S3 = short1/2/3.json.

| item | text (abridged) | verdict | source | replacement (FIX) / note |
|---|---|---|---|---|
| E[0] say/show | $110,362,993.87 … ordered … in 2003 | OK | MTC ECF 1 p.2 (sentenced Jul 18, 2003; restitution $110,362,993.87) | |
| E[0] caption/src | JORDAN BELFORT · 2017 / Tai Lopez CC BY 3.0 | OK | Wikimedia | |
| E[1] say | "Here is that number, in a Justice Department filing." | OK | MTC p.2, filed by U.S. Attorneys | hl 0.2163–0.4256 covers p.2 lines 4–10, which include $110,362,993.87. OK |
| E[1] title/kicker/src | Restitution: $110,362,993.87 / MARCH 2018 | OK | MTC | |
| E[2] say/show | paid ~$12.8M, mostly property given up at sentencing; still owed ~$97M (prosecutors) | OK | Bloomberg/Fortune & BNN 5/16/18 ("they say") | |
| E[2] bars | 110.4 / 12.8 | OK | Bloomberg: "$110.4 million in restitution and other penalties" | |
| E[3] say/show/q | "Today, I can finally say that I completed my court-ordered restitution." given to TMZ, "this year" | OK | TMZ 7/13/26 ("Jordan tells TMZ") | |
| E[4] say/show | TMZ, citing sources, expired Apr 28, 2026; Monday Nov 16 launch per tech press | OK | TMZ; Startup Fortune (Nov 16 per TokenPost) | |
| E[4] kicker | "APRIL 28, 2026 → NOVEMBER 16, 2026" (with "The clock ran out.") | **FIX** | TMZ ("According to sources"); conflicts with Bloomberg 2018 "released from prison in April 2008" | kicker → `APRIL 28, 2026 (PER TMZ'S SOURCES) → NOV 16, 2026` |
| E[4] src | "… Startup Fortune / Analytics Insight (Nov 17, 2026), citing TechCrunch" | **FIX** | Analytics Insight does not cite TechCrunch; Startup Fortune cites TechCrunch and dates the launch per TokenPost | src → `TMZ (Jul 13, 2026) · Startup Fortune (Nov 17, 2026, citing TechCrunch and TokenPost) · Analytics Insight (Nov 17, 2026)` |
| E[5] say/show | "So where did the $110 million go?" | NOTE | | Rhetorical. It slightly implies that $110M was paid and then went somewhere. Acceptable because the video answers it. |
| E[5] title/sub | United States v. Jordan Ross Belfort · E.D.N.Y. · CR-98-0859 | OK | MTC p.1 | |
| E[7] say + big | ran Stratton Oakmont, Long Island penny-stock brokerage; per AP a few desks and phones in a former auto shop | OK | AP 11/11/13 ("a few desks and phones set up in a former Long Island auto shop"); Bloomberg 2013 ("Long Island penny-stock boiler room") | |
| E[8] say | high-pressure sales at inflated prices; once pumped, Belfort and others sold own shares | OK | AP ("deceptive, high-pressure tactics…"; "After artificially pumping the value up, Belfort and others would dump their own shares before prices crashed") | |
| E[8] items[3] | "the customers are left holding them" | **FIX** | Not in AP. AP says shares were dumped "before prices crashed" | items[3] → `["4", "then the prices crash"]` |
| E[9] say + stat | 1,000+ brokers at peak; FBI arrest 1998 | OK | Bloomberg 11/7/13 | see N-show |
| E[10] say | "…and agreed to testify as a government witness against other defendants." | **FIX** | AP: "pleaded guilty in 1999 and agreed to become a government witness". Bloomberg 2013 says nothing about testifying. | say → `He pleaded guilty in nineteen ninety-nine, and agreed to become a government witness.` / show → `He pleaded guilty in 1999, and agreed to become a government witness.` |
| E[10] timeline | 1998 arrested; 1999 pleads guilty, agrees to cooperate; JULY 18, 2003 sentenced | OK | Bloomberg; AP; MTC | |
| E[11] say/show | sentenced Jul 18, 2003; four convictions | OK | MTC p.2 lines 4–7 | hl covers lines 4–10. OK |
| E[12] say/show | served 22 months, Bloomberg reported; 1,513 investors, >$200M per Bloomberg | OK / NOTE | Bloomberg 2013 ("served only 22 months"); Bloomberg 2018 (1,513; >$200M) | Attributed, and TMZ and CNW also say 22 months. But Bloomberg 2018 gives release as "April 2008" and the sentence as "four years" (AP says 3 1/2). The script correctly avoids asserting sentence length or release year; keep it that way. |
| E[12] stat | 1,513 · more than $200 million lost, per Bloomberg | OK | Bloomberg 2018 | |
| E[13] say + big | after release, ordered to pay 50% of gross income | OK | Bloomberg 2018 ("50 percent of his gross income to victims after he was freed"); AP ("50 percent of his future earnings") | see N-show |
| E[14] say | "the next twenty years are a fight over what it covered, and for how long" | NOTE | AP (probation/50% dispute); Bloomberg 2018 (speaking-income dispute) | Framing is supported in substance. |
| E[16] say/show + list | learned of memoir deal Apr 2007; restraining orders vs Bantam Books, Warner Brothers, Appian Way | OK | Bloomberg 2018 (verbatim match) | Kicker "· 2007": Bloomberg ties the orders to learning of the deal in April 2007 without dating the orders themselves. Acceptable. |
| E[17] say/show + stat | agreed to pay half of movie earnings to U.S.; ~$700,000 from book sales 2007–2009 per court papers cited by AP | OK | Bloomberg 2018; AP ("Book sales resulted in payments of about $700,000 from 2007 to 2009, court papers say.") | |
| E[18] say + stat | 2010 paid nothing, prosecutors later said | OK | Bloomberg 2018 (prosecutors, court papers) | see N-show |
| E[19] say + big | probation ended 2010; lawyers argued 50% ended with it | OK | AP | see N-show |
| E[20] say/show + stat | earned $940,500 from movie-rights sale (AP); payments fell sharply after probation (prosecutors) | OK | AP ("made $940,500 off the sale"; "prosecutors claim Belfort's payments have slowed to a trickle") | |
| E[21] say/show | "In October 2013, about two months before the film's release…" | **FIX** | AP: "In early October"; release "Christmas Day". Early October to Dec 25 is about 11–12 weeks. | say → `In October twenty thirteen, less than three months before the film's release, prosecutors asked a federal judge in Brooklyn to find Belfort in default. They said he had paid only eleven point six million of the hundred and ten million he owed. They later withdrew the request, to allow settlement talks.` / show → `In October 2013, less than three months before the film's release, prosecutors asked a federal judge in Brooklyn to find Belfort in default. They said he had paid only $11.6 million of the $110 million he owed. They later withdrew the request, to allow settlement talks.` |
| E[21] bars | OWED 110 / PAID 11.6 | OK | AP | |
| E[22] say/show/q | offered 100% of book and movie profits; "I don't want to make any money from the books or the movie." | OK | AP (verbatim) | AP: "he claims he's repeatedly offered". "Belfort told the AP" is fine. |
| E[23] say | film made about $100 million (Bloomberg) | OK | Bloomberg 2018 ("The 2013 film made about $100 million") | see N-show |
| E[23] big | "The question nobody asked: who paid for it?" | NOTE | | Rhetorical. The financing was widely reported after 2016. Optional softening. |
| E[25] say/show | "…announced its largest kleptocracy case, against money stolen from a Malaysian state investment fund called 1MDB." | **FIX** | Caldwell: "largest single action ever brought by the Kleptocracy Initiative"; the theft is an allegation in a civil forfeiture complaint | say → `July twentieth, twenty sixteen. The Justice Department announced the largest action ever brought by its Kleptocracy Initiative, over money it alleged was stolen from a Malaysian state investment fund called one M.D.B.` / show → `July 20, 2016. The Justice Department announced the largest action ever brought by its Kleptocracy Initiative, over money it alleged was stolen from a Malaysian state investment fund called 1MDB.` |
| E[25] hl | [0, 0.0263, 1, 0.1459] = headline block | NOTE | cald.jpg | Headline covers "Kleptocracy Enforcement Action … Malaysian Sovereign Wealth Fund". Optional: extend to the first paragraph ("largest single action ever…") with hl `[0.0, 0.0263, 1.0, 0.2000]`. |
| E[26] say | "described where some of that money went, including to a California motion picture company" | **FIX** | Caldwell: "My remarks will focus on the allegations in the complaint…"; "a California-based motion picture company" | say → `In her remarks, Assistant Attorney General Leslie Caldwell described where, according to the complaint, some of that money went, including to a California-based motion picture company, Red Granite Pictures.` (hl 0.6528–0.716 covers the "California-based motion picture company, Red Granite Pictures" sentence. OK) |
| E[27] say/show/title | Red Granite quote | OK | caldwell.txt (verbatim) | hl 0.7226–0.7656 covers exactly that sentence. NOTE: the page says "Remarks as prepared for delivery"; "Then she said this" is standard but could be "Her prepared remarks continued". |
| E[28] say/q | "According to the allegations in the complaint, this is a case where life imitated art." | OK | caldwell.txt | |
| E[29] say/show + stat | Belfort not accused; March 2018 Red Granite $60M to settle forfeiture suit; not an admission of wrongdoing or liability | OK | CNBC 3/7/18 (settlement "stipulates" no "admission of wrongdoing or liability on the part of Red Granite") | Settlement in principle was announced Sept 2017; terms were filed March 2018. Fine. |
| E[30] say/show + bars | "prosecutors alleged"; $60M ≈ "almost five times" $12.8M | OK | 60/12.8 = 4.69 | |
| E[31] say | "And in twenty seventeen, prosecutors started digging into Belfort's own companies." | **FIX** | Record shows a deposition Sept 15, 2017 (Gilsen ¶6), garnishment proceedings, and subpoenas Nov 2017. When the inquiry *started* is not established. | say → `But the victims were still waiting. And by twenty seventeen, prosecutors were digging into Belfort's own companies.` / show → `But the victims were still waiting. And by 2017, prosecutors were digging into Belfort's own companies.` |
| E[33] say/show | Nov 2017 subpoenas; three companies "it said were jointly owned by Belfort"; books and records | OK | MTC p.2 ("three Nevada entities jointly owned by Belfort"); p.5 ("books and records") | hl 0.4028–0.4907 covers lines 10–12. OK |
| E[34] say | deadline Dec 1; "failed to produce any documents, or respond to the subpoenas in any manner" | OK | Laserna ¶10 (verbatim) | hl covers ¶10. OK. NOTE: las_3 is the declaration in the California-entities case (18-mc-1033), not the Nevada motion; the src label says so. Fine. |
| E[35] say | letter in December, no response; letters in March, no response | OK | Laserna ¶¶11–16 | hl covers ¶12 ("have not responded to my December 20, 2017, letter"). Acceptable. |
| E[36] say/show | Mar 29, 2018, federal court in Nevada, motion to compel | OK | MTC p.1 (stamp MAR 29 2018; D. Nev.); ECF 9 | hl covers the caption and title. OK |
| E[37] say | forensic accountant, former IRS criminal investigator, hired by USAO, went through the books | OK / NOTE | Gilsen ¶¶1–3 ("contracted by the USAO"; "24 years … Special Agent … IRS, Criminal Investigation") | "Former" is inferred, which is reasonable. "Attached to it": the motion relies on the "Gilsen Decl."; the copy shown is ECF 4-1 filed Mar 31, 2018. hl covers ¶1 only. Optional: `[0.0, 0.1549, 1.0, 0.3000]` to include ¶2 (IRS). |
| E[38] say | Distributions account; personal expenses of Belfort and business partner paid by company | OK | Gilsen ¶4 | hl covers lines 19–21. Partner's name blacked out. OK |
| E[39] say/show | Aug 5, 2017 balance $9,188,876.06 | OK | Gilsen ¶5 | hl covers lines 24–25. OK |
| E[40] say | no documentation of promise/agreement to repay; deposition "No." / "Not to my knowledge." | OK | Gilsen ¶¶5,7 (Belfort was asked about "loan agreements or promissory notes") | hl covers ¶7. OK |
| E[42] say/show | 2013/14/15: $1.4M, $2.8M, $3.7M, Belfort and partner together | OK | Gilsen ¶9 ($1,422,632.42; $2,792,004.21; $3,722,580.89) | hl covers ¶9 lines 15–17. Name blacked out. |
| E[43] say/show | income reported ≈ $893,000, $1.9M, $1.8M | OK | Gilsen ¶10 ($892,843; $1,867,140; $1,774,778) | |
| E[43] bars | 1.42/0.89/2.79/1.87/3.72/1.77 + "*Belfort and his partner together" | OK | Gilsen ¶¶9–10 | The footnote makes the two-person vs one-person comparison fair. |
| E[44] say | "those personal expenses were not reported as income on the returns, as standard accounting principles require" | **FIX** | Gilsen ¶10: "Belfort's personal expenses, which were paid by GMI … were not reported as income on the respective tax returns". It covers Belfort's returns only, not the partner's share. | say → `The accountant's conclusion: Belfort's personal expenses paid by the company were not reported as income on his tax returns, as standard accounting principles require.` (hl covers ¶10 lines 22–24. OK) |
| E[45] say/show/title | "At least a portion [of] these funds could have been applied to the defendant's restitution liability." | OK | MTC p.6 lines 7–8 (original lacks "of"; the bracket is correct) | hl covers lines 7–8. Partner's name on lines 2 and 4 blacked out. OK |
| E[46] say | "…salary to two of Belfort's children…" | **FIX** (minor) | MTC p.7: "the defendant's two children, neither of whom actually worked for Global Motivation"; p.6: "alter ego and/or nominee of the defendant" | say → `The government went further. It said the company also paid hundreds of thousands of dollars in salary to Belfort's two children, neither of whom, it said, actually worked there. And it argued the companies were his alter egos.` (hl covers lines 8–11. No children's names on page. OK) |
| E[47] say/show/title | lawyer; QuickBooks "only partially responsive"; May 2018 "extensive and seemingly willful" | OK | ECF 9 (5/23/18) | hl covers the sentence. OK |
| E[48] say/show | "That same month, in court papers, prosecutors said … at least $9M … kept all of it. Bloomberg reported their words: he 'isn't just a con, but also a deadbeat.'" | **FIX** | Bloomberg/BNN lead: "…isn't just a con, but also a deadbeat, prosecutors say" (Bloomberg's sentence, not a quotation); "$9 million" is attributed to "Prosecutors say", not to court papers | say → `That same month, prosecutors said, as Bloomberg reported, that Belfort had earned at least nine million dollars from speaking engagements from twenty thirteen to twenty fifteen, and kept all of it. Bloomberg summed up their position: he isn't just a con, but also a deadbeat, prosecutors say.` / show → `That same month, prosecutors said, as Bloomberg reported, that Belfort had earned at least $9 million from speaking engagements from 2013 to 2015, and kept all of it. Bloomberg summed up their position: he "isn't just a con, but also a deadbeat, prosecutors say."` |
| E[48] scene q/case/doc | q "isn't just a con, but also a deadbeat" / case FEDERAL PROSECUTORS / doc COURT PAPERS · AS QUOTED BY BLOOMBERG | **FIX** | same | q → `…isn't just a con, but also a deadbeat, prosecutors say.` · case → `BLOOMBERG NEWS` · doc → `SUMMING UP PROSECUTORS' POSITION · MAY 2018` |
| E[49] say + big | Belfort and lawyer dispute numbers; "cash-strapped" | OK | Bloomberg 2018 (Sharon Cohen Levin) | |
| E[50] say/show/q | absent, in Lithuania for a motivational speech; "It seems like he has some spare change lying around." | OK | Fortune (Wednesday hearing; Donnelly) | |
| E[51] say/q | "He's going to have to come here so we can get a grip on what's going on." | OK | Fortune (verbatim) | |
| E[53] say + big | "Not a trial. Not a contempt finding. Paperwork." | OK / NOTE | ECF 9/12/16 | No contempt finding appears in the record reviewed. |
| E[54] say/show/title | Oct 2021: no outstanding disputes; asked to dismiss | OK | ECF 16 (verbatim "no outstanding disputes") | hl covers the sentence. OK. No seal visible. |
| E[55] say/show | "…had complied with the subpoenas. Dismissed." | **FIX** | ECF 12: "have complied with the relevant subpoenas and therefore this action is subject to dismissal"; "respectfully requests that this case be dismissed". No dismissal order in the sources. | say → `And in April twenty twenty-two, in the other case, it wrote that Belfort and his companies had complied with the subpoenas, and asked the court to dismiss the case.` / show → `And in April 2022, in the other case, it wrote that Belfort and his companies had complied with the subpoenas, and asked the court to dismiss the case.` (hl covers the sentence. OK. No seal.) |
| E[56] say + list | public record doesn't show what records showed / deal / final accounting | OK | ECF 12; CNW ("No final public accounting…") | |
| E[57] say/show/q | § 3613(b) quote | OK | Cornell LII (verbatim; the show closes the quote before the paraphrase "or 20 years after release from prison") | |
| E[58] say/show + big | Apr 28, 2026 per TMZ's sources; trustee distributed much lower amount to 1,513 victims | OK | TMZ | NOTE: Bloomberg 2018 says released April 2008, which would mean 2028. The attribution here is correct and must stay. |
| E[59] say/show + stat | no final accounting; CNW estimate ≈$13.75M ≈12.5¢ | OK | CNW 7/14/26 ("most defensible estimate"); 13.75/110.36 = 12.46¢ | Labeled as an estimate. |
| E[60] say/q | "For nearly three decades, I've lived with the consequences…" | OK | TMZ (verbatim) | |
| E[61] say/show + list | "this week"; Tone co-founded with Pishevar; "tonalities"; ~$10M raised and $700K–$1M revenue, Belfort says | OK / NOTE | Analytics Insight ("Belfort co-founded Tone with investor Shervin Pishevar"; "about USD10 million … according to Belfort"); Startup Fortune (revenue per Belfort, via TokenPost) | Startup Fortune describes Straightline.AI as the company co-founded with Pishevar, with Tone as its platform. "Tech press reports say" covers this. "This week" is correct (Mon Nov 16, today Nov 17). |
| E[61] src | "Startup Fortune / Analytics Insight (Nov 17, 2026), citing TechCrunch" | **FIX** | as E[4] | src → `Startup Fortune (Nov 17, 2026, citing TechCrunch and TokenPost) · Analytics Insight (Nov 17, 2026)` |
| E[62] say/show | "…and told reporters: once everyone is paid back…" | **FIX** | Bloomberg 2018: in 2014, during his speaking tour, "…," he said at the time. It does not say "told reporters". | say → `In twenty fourteen, he said he hoped to earn north of a hundred million dollars from his speeches, and said: once everyone is paid back, believe me, I will feel a lot better.` / show → `In 2014, he said he hoped to earn "north of $100 million" from his speeches, and said: "Once everyone is paid back, believe me I will feel a lot better."` |
| E[62] q/doc | quote; 2014 · AS QUOTED BY BLOOMBERG | OK | Bloomberg 2018 | |
| E[63] say/show | "The prosecutors' last public count said twelve point eight." | **FIX** | Bloomberg 2018 is the latest count *in our sources*; later filings could exist | say → `The order said one hundred ten million dollars. The last count from prosecutors that we found said twelve point eight million. The law said twenty years.` / show → `The order said $110 million. The last count from prosecutors that we found said $12.8 million. The law said 20 years.` |
| E[63] list | $110.4M ordered 2003 / $12.8M paid by 2018, prosecutors said / 20 YRS then the liability ends | OK | MTC; Bloomberg; § 3613(b) | |
| E[64] say/cta | question | OK | | |
| S1 title | "$12.8 Million of $110 Million: The Wolf's Restitution" | **FIX** | $12.8M is the prosecutors' 2018 figure, not a total | title → `$12.8 Million of $110 Million by 2018, Prosecutors Said: The Wolf's Restitution` |
| S1[0] say/show + hook | $12.8M paid by 2018 per prosecutors; tag GUILTY; "PAID OF $110M / BY 2018, FEDS SAID" | OK / NOTE | Bloomberg 2018 | GUILTY is true (1999 plea) and the restitution flows from that conviction. |
| S1[1] say/show | 2003 order, 1,513 investors | OK | MTC; Bloomberg 2018; TMZ | hl = E[1]. OK |
| S1[2] say/show + stat | half his income; kept at least $9M from speeches (2013–2015) | OK | Bloomberg 2018 ("Prosecutors say … pocketed it all") | |
| S1[3] say/show | TMZ reported expired this year under 20-year limit; Belfort says he completed it | OK | TMZ; § 3613(b) | |
| S1[3] q | "I completed my court-ordered restitution." | **FIX** (minor) | TMZ: "Today, I can finally say that I completed…" | q → `…I completed my court-ordered restitution.` |
| S2 title | "\"Life Imitated Art\": Who Paid for The Wolf of Wall Street" | **FIX** | Presents a DOJ allegation as an answer. Red Granite settled with no admission. | title → `"Life Imitated Art": What the DOJ Alleged About The Wolf of Wall Street's Money` |
| S2[0] say/show + hook | >$100M from a theft, DOJ alleged; tag DOJ ALLEGED | OK | caldwell.txt | |
| S2[1] say/show | "It said Red Granite Pictures financed the film with money involved in the theft from Malaysia's 1MDB fund." | OK | caldwell.txt | hl = E[27]. OK |
| S2[2] say + q | "Its words: a case where life imitated art." / q "…a case where life imitated art." | **FIX** | caldwell.txt: "According to the allegations in the complaint, this is a case where life imitated art." The cut removes the allegation qualifier. | say → `Its words: according to the allegations in the complaint, this is a case where life imitated art.` · q → `According to the allegations in the complaint, this is a case where life imitated art.` |
| S2[3] say/show + stat | 2018, $60M, no admission; Belfort not accused | OK | CNBC | |
| S2[4] say | "A movie about fraud, funded by theft, prosecutors alleged." | OK | | |
| S3 title | "$9,188,876.06 in \"Distributions\": The Wolf's Company Books" | OK | Gilsen ¶5 | |
| S3[0] say/show | $9.19M personal expenses of Belfort and partner, paid by his company | OK / NOTE | Gilsen ¶¶4–5 | The company is 50% his; "his company" is acceptable ("their company" would be more precise). |
| S3[0] hook tag | "GUILTY" | **FIX** | The 2017–18 matter was a civil collection motion with no finding; the tag implies a crime connected to the $9.19M | tag → `COURT FILING` |
| S3[1] say | "He found no agreement to pay it back." | OK / NOTE | Gilsen ¶5 ("not found any documentation to substantiate any form of a promise or agreement to reimburse") | Optional, more precise: "He found no documentation of any agreement to pay it back." hl covers ¶5 lines 24–25. OK |
| S3[2] say | under oath, loan agreements, "No." | OK | Gilsen ¶7 | hl OK |
| S3[3] say/show | some could have gone to victims, owed ~$97M | OK | MTC p.6; Bloomberg 2018 | hl OK |
| Thumb A | $110M / ORDERED TO REPAY / GUILTY / THE REAL WOLF | OK | MTC | |
| Thumb A line2 | "$97M UNPAID IN 2018" | **FIX** | The government's figure; Belfort disputed the numbers (Bloomberg 2018) | line2 → `FEDS: $97M UNPAID IN 2018` (check that size2 fits) |
| Thumb B | $12.8M / PAID BY 2018, FEDS SAID / JORDAN BELFORT | OK | Bloomberg 2018 | |
| Thumb B line2 | "THEN THE CLOCK RAN OUT" | **FIX** | The expiry date comes only from TMZ's sources and conflicts with Bloomberg's April 2008 release date. Belfort's own claim is that he "completed" it. | line2 → `NOW HE SAYS HE'S DONE` |
| Thumb C | 20 YRS / THEN IT EXPIRES / $110M RESTITUTION | OK | § 3613(b) (true as a general rule) | |
| Thumb C line2 | "WHERE DID IT GO?" | **FIX** | Implies $110M was paid and vanished; prosecutors said ~$12.8M was paid by 2018 | line2 → `HOW MUCH GOT PAID?` |
| meta title | "Jordan Belfort: $110M Restitution — Then It EXPIRED" | **FIX** | Contested date (TMZ sources vs Bloomberg 2018 release April 2008) | title → `Jordan Belfort: $110M Restitution — Then It EXPIRED, Per TMZ` |
| meta summary | 2003 order; 2018 $12.8M / $97M per prosecutors; TMZ reported expiry; pleaded guilty 1999; sentenced Jul 18, 2003; Red Granite no admission; Belfort not accused | OK / NOTE | all sources | Optional: "Tone (launched Nov 16, 2026, per tech press)". |
| meta docs_note | names blacked out; seals removed; CNW = estimate | OK | verified on images | |
| meta first_comment | "…Then the 20-year clock ran out. …" | **FIX** | as above | → `Ordered: $110.4M. Paid by 2018, per prosecutors: $12.8M. Then, per TMZ's sources, the 20-year clock ran out. Should restitution to fraud victims ever expire?` |
| meta question | Should restitution … expire? | OK | | |

### N-show (NOTE, not an accuracy error)
These lines have no "show" field, so their subtitles would carry spelled-out numbers. The channel style is digits in "show". Suggested show texts:
- E[9]: `Bloomberg reported that at its peak, the firm employed more than 1,000 brokers. The FBI arrested Belfort in 1998.`
- E[13]: `And the plan for paying them back was simple. After his release, he was ordered to pay 50 percent of his gross income to his victims.`
- E[14]: `Remember that number. 50 percent. Because the next 20 years are a fight over what it covered, and for how long.`
- E[18]: `In 2010, prosecutors later said, he paid nothing.`
- E[19]: `2010 was also the year his probation ended. And Belfort's lawyers argued that the 50 percent obligation ended with it.`
- E[23]: `And then the film came out. Bloomberg reported that it made about $100 million. But the strangest part of the movie's money was not what it earned. It was where it came from.`
- E[34]: `The deadline was December 1. According to the prosecutor's sworn declaration, the companies failed to produce any documents, or respond to the subpoenas in any manner.`
- E[41]: `Chapter five. $9 million.`
- S2[3] already has a show; S3[3] has a show.

### Image check
- mtc_2, mtc_6, mtc_7, gil_1, gil_2, las_3, mtc_1, l9_2, l12_1, l16_1, cald: all hl bands were checked visually against the narration and are correct.
- Partner name: blacked out on mtc_6 (lines 2 and 4), gil_1 (line 20), gil_2 (line 15).
- Bookkeeper name: blacked out on gil_2 (lines 25–28).
- Children's names: not on any page used.
- AUSA and agency attorney names (Laserna, Price, Klar, Giese, Woolf) are public officials or counsel of record. They are not private parties.
- No DOJ seal is visible on any letter. The header area of l12_1 and l16_1 is partly cleaned, but the case number is still legible enough.
- Hook crops: S2 (cald, 74%) and S3 (gil_1, 84%) show no private names.
