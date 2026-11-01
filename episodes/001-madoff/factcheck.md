# Fact-check — SWORN Case 001: The Madoff Confession

Independent check of `episode.json` (70 lines, 0-based). Checked 2026-11-02.

Sources opened:
- [ARREST] SDNY press release, Dec 11, 2008 — https://www.justice.gov/archive/usao/nys/pressreleases/December08/madoffarrestpr.pdf
- [COMPLAINT] Criminal complaint, U.S. v. Madoff (sworn by FBI SA Theodore Cacioppi) — https://www.justice.gov/usao-sdny/file/762661/download
- [PLEA-PR] SDNY press release + statutory maximum chart (p.3), Mar 12, 2009 — https://www.justice.gov/archive/usao/nys/pressreleases/March09/madoffbernardpleapr.pdf
- [SENT-PR] SDNY press release, Jun 29, 2009 — https://www.justice.gov/archive/usao/nys/pressreleases/June09/madoffbernardsentencingpr.pdf
- [PLEA] Madoff plea statement — https://www.cbsnews.com/news/full-text-madoffs-court-statement and https://www.cnbc.com/id/29660154
- [AP] AP obituary via OPB, Apr 14, 2021 — https://www.opb.org/article/2021/04/14/ponzi-schemer-bernie-madoff-dies-in-prison-at-82/
- [FORTUNE] Fortune/CNN Money, Jun 29, 2009 — https://money.cnn.com/2009/06/29/magazines/fortune/bernard_madoff_faces_victims.fortune/index.htm
- [OIG] SEC OIG Report OIG-509 exec summary — https://www.sec.gov/files/oig-509-exec-summary.pdf
- [NBC] NBC New York, Dec 2024 — https://www.nbcnewyork.com/news/business/money-report/last-madoff-victim-fund-payout-brings-recovery-to-nearly-94-of-ponzi-scheme-losses-doj-says/6089400/
- [DOJ-MVF] SDNY press release on 10th MVF distribution — https://www.justice.gov/usao-sdny/pr/justice-departments-tenth-distribution-provides-over-4-billion-nearly-full-recovery
- [NBC-PETER] NBC New York on Peter Madoff plea (age 66 in 2012; worked with brother "since 1965") — https://www.nbcnewyork.com/news/local/peter-madoff-guilty-plea-expected-conspiracy-fraud/1948724/

| # | field | claim | verdict | source | fix text |
|---|---|---|---|---|---|
| 0 | say/show | Dec 10, 2008, told two senior employees his business is a fraud | OK | ARREST; COMPLAINT ¶4d | Complaint: "his investment advisory business was a fraud" (said at his Manhattan apartment). |
| 0 | scene | kicker DECEMBER 10, 2008; src SDNY release Dec 11, 2008 | OK | ARREST | |
| 1 | say | Per prosecutors: "it's all just one big lie" / "basically, a giant Ponzi scheme" | OK | ARREST; COMPLAINT | |
| 1 | scene.q | "it's all just one big lie … basically, a giant Ponzi scheme." | OK | ARREST | Two separate quoted fragments joined by ellipsis; acceptable. |
| 2 | say/show | "He estimated the losses at about fifty billion dollars." | FIX | ARREST; COMPLAINT ¶4d | Source says "at least approximately $50 billion"; "about" drops the floor. say: "He estimated the losses at fifty billion dollars, at least." show: "He estimated the losses at $50 billion, at least." |
| 2 | scene.value/label | "$50B" — losses by his estimate | FIX | ARREST | value: "$50B+" ; label: "losses from the fraud — at least, by his estimate,\|according to the criminal complaint" |
| 3 | say | Next morning the FBI arrested him | OK | ARREST; COMPLAINT ¶5 | |
| 3 | scene.note | Charged with one count of securities fraud | OK | ARREST | |
| 4 | say | Multibillion-dollar Ponzi scheme, hidden for years, brought to court | OK | ARREST headline; PLEA-PR | |
| 5 | scene | U.S. v. Bernard L. Madoff · SDNY · 2008–2009 | OK | ARREST; SENT-PR | |
| 6 | say | Chapter title | OK | — | No factual claim. |
| 7 | say/show | Founded firm 1960; "leading international market maker"; former NASDAQ chairman | OK | ARREST; COMPLAINT ¶3 | 1960 comes from the firm's own website ("since its inception in 1960"). |
| 7 | scene | "Founded 1960"; "Former chairman of the NASDAQ Stock Market." | OK | ARREST | |
| 8 | say/show | Born 1938, Queens | OK | AP | |
| 8 | say/show | "went to Wall Street in 1960 with his brother Peter and a few thousand dollars, saved from working as a lifeguard and installing sprinklers" | FIX | AP; NBC-PETER | AP does say "with Peter in 1960", but Peter was ~14 then (66 in mid-2012) and NBC says he worked with his brother "since 1965". Avoid repeating the likely AP error. say: "...he went to Wall Street in nineteen sixty with a few thousand dollars, saved from working as a lifeguard and installing sprinklers. His younger brother Peter joined him later." show: "...he went to Wall Street in 1960 with a few thousand dollars, saved from working as a lifeguard and installing sprinklers. His younger brother Peter joined him later." |
| 8 | scene.events | 1938 born Queens; 1960 starts firm; LATER chairman of NASDAQ | OK | AP; ARREST | |
| 9 | say | Clients incl. Spielberg, Kevin Bacon, Sandy Koufax, Florida retirees, charities | OK | AP | AP: "celebrities such as film director Steven Spielberg, actor Kevin Bacon and Hall of Fame pitcher Sandy Koufax"; "Jewish charities". Living people named as victims only — not defamatory. |
| 9 | say | Elie Wiesel said he bought into a myth Madoff created around himself | OK | AP | AP: "a myth that he created around him that everything was so special…" |
| 9 | scene.lines | "a myth that he\|created around him" | OK | AP | Verbatim. |
| 10 | say/show | "The same website boasted more than $700 million ... top 1%" | FIX | ARREST | Figures and quote correct, but "The same website" has no antecedent: the website is never named in narration (line 7 says "It described itself", line 9 is AP). say: "The firm's website boasted more than seven hundred million dollars in firm capital, and said the firm ranked among the top one percent of U.S. securities firms." show: "The firm's website boasted more than $700 million in firm capital, and said the firm ranked among the top 1% of U.S. securities firms." |
| 10 | scene.q | "[w]ith more than $700 million in firm capital, Madoff currently ranks among the top 1% of US Securities firms" | OK | ARREST; COMPLAINT ¶3 | Verbatim. |
| 11 | say/scene.q | "Clients know that Bernard Madoff has a personal interest in maintaining an unblemished record of value, fair-dealing, and high ethical standards" | OK | ARREST | Verbatim; source continues "that has always been the firm's hallmark." Since line 10 is now "The firm's website", consider say: "The website also told clients..." |
| 12 | say | Per two senior employees, he ran advisory business from a separate floor | OK | ARREST; COMPLAINT ¶4a | |
| 12 | scene.lines | Kicker "ACCORDING TO TWO SENIOR EMPLOYEES" over "Statements under lock and key." | FIX | COMPLAINT ¶4a | "Lock and key" is from ONE employee (Senior Employee No. 1), and concerns "the financial statements for the firm". lines: ["A separate floor.", "The firm's statements under lock and key."] and kicker: "ACCORDING TO THE SENIOR EMPLOYEES" — or drop the second line. |
| 13 | say | "He kept its financial statements under lock and key, and he was, in their word, cryptic about it." | FIX | ARREST; COMPLAINT ¶4a | Single source (Senior Employee No. 1), and it was the firm's financial statements, not the advisory unit's. say: "According to one of them, he kept the firm's financial statements under lock and key, and he was, in that employee's word, cryptic about the advisory business." |
| 14 | say/show/scene | Jan 2008 SEC filing: 11–25 clients, ~$17.1B under management | OK | ARREST; COMPLAINT ¶4b | Form ADV filed on or about Jan 7, 2008. |
| 15 | say | Chapter title | OK | — | |
| 16 | say/scene.q | "that I would invest their money in shares of common stock, options and other securities of large well-known corporations" | OK | PLEA | Verbatim. |
| 17 | say/scene | "split strike conversion strategy" | OK | PLEA | |
| 18 | say/scene.q | "I never invested those funds in the securities, as I had promised." | OK | PLEA | Verbatim. |
| 19 | say/scene.q | "Instead, those funds were deposited in a bank account at Chase Manhattan Bank." | OK | PLEA | Verbatim. |
| 20 | say/scene.q | "I knowingly caused false trading confirmations and client account statements …" | OK | PLEA (CBS) | Full: "...that reflected the bogus transactions and positions to be created and sent to clients". |
| 21 | say/scene | Withdrawals paid from same Chase account with other clients' money | OK | PLEA | Plea: "I used the money in the Chase Manhattan bank account that belonged to them or other clients to pay the requested funds." Simplification acceptable. |
| 22 | say | Definition of Ponzi scheme | OK | COMPLAINT ¶1; AP | |
| 23 | say/show | AP: steady double-digit returns; late 2008 statements claimed ~$65B; no securities ever bought or sold | OK | AP | AP: "steady double-digit returns, even during market downturns"; "As of late 2008, the statements claimed investor accounts totaled $65 billion"; "No securities were ever bought or sold." (Attributed to AP — keep attribution.) |
| 23 | scene.items | Bar label "ACTUALLY PUT IN" $17.5B | FIX | AP | AP calls $17.5B "an estimated" figure; "ACTUALLY" overstates. label: "PUT IN (EST.)" |
| 24 | say/scene | DiPascali pleaded guilty (2009), said trade statements were "all fake" | OK | AP | AP calls him Madoff's chief financial officer; "longtime employee" is acceptable. (DiPascali is deceased.) |
| 25 | say/scene.q | "When I began the Ponzi scheme I believed it would end shortly and I would be able to extricate myself and my clients from the scheme." | OK | PLEA | Verbatim (no commas in original; spoken commas are fine). |
| 26 | say/scene.q | "However, this proved difficult, and ultimately impossible" | OK | PLEA | Verbatim. |
| 27 | say/scene.q | "To the best of my recollection, my fraud began in the early 1990s." | OK | PLEA | Verbatim. Line 28 correctly notes prosecutors disputed his assertions. |
| 28 | say/scene.title | Prosecutors did not agree with all his assertions; "We do not agree with all the assertions" | OK | PLEA-PR | Said by Acting U.S. Attorney Lev Dassin: "While we do not agree with all the assertions made by Mr. Madoff today..." |
| 29 | say | Chapter title | OK | — | |
| 30 | say/show/scene | OIG: six substantive complaints, June 1992–Dec 2008 | OK | OIG | OIG fn.1 notes "arguably eight" because three versions of one complaint. |
| 31 | say/show/scene | Markopolos versions: May 2000, March 2001, October 2005 | OK | OIG | "Analyst" is not OIG wording but a common, benign description. |
| 32 | show/scene.q | 2005 title "The World's Largest Hedge Fund is a Fraud" | OK | OIG | Verbatim. Cite "As cited in SEC OIG Report" correct. |
| 33 | say/scene | "despite three examinations and two investigations ... a thorough and competent investigation or examination was never performed" | OK | OIG | Verbatim in exec summary. |
| 34 | say | "after the last of Markopolos's submissions, the scheme kept running for more than three years" | FIX | OIG | OIG says Markopolos approached Enforcement again in Dec 2005 and e-mailed the Enforcement branch chief in June 2007. Oct 2005 was the last *version of his complaint*, not his last submission/warning. say: "And after the third version of Markopolos's complaint, in October two thousand five, the scheme kept running for more than three years." |
| 34 | scene | kicker "AFTER THE LAST WARNING"; event "Markopolos's third submission" | FIX | OIG | kicker: "AFTER THE THIRD VERSION"; event OCT 2005 text: "Third version of Markopolos's complaint". Optionally add {"date":"JUN 2007","text":"Markopolos e-mails the SEC again"}. |
| 35 | say | Chapter title | OK | — | |
| 36 | say/scene | Family lawyer contacted regulators, who alerted prosecutors and FBI | OK | AP | AP: "A lawyer for the family contacted regulators, who alerted the federal prosecutors and the FBI." |
| 37 | say/scene | Two FBI agents at his door; "There is no innocent explanation." | OK | AP; COMPLAINT ¶5 | Also in the sworn complaint (Dec 11, 2008). |
| 38 | say/scene | Dec 11 FBI special agent swore complaint; one count securities fraud | OK | COMPLAINT; ARREST | Sworn by SA Theodore Cacioppi. |
| 39 | say/show/scene | ~$200–300M left; to pay selected employees, family, friends; surrender in ~1 week | OK | ARREST; COMPLAINT ¶4e | |
| 40 | say/show/scene | Mar 12, 2009, pleaded guilty before Judge Denny Chin | OK | PLEA-PR | |
| 41 | say/show/scene | 11 counts, listed | OK | PLEA-PR (incl. p.3 chart) | |
| 42 | say/scene.q | "I am actually grateful for this first opportunity to publicly speak about my crimes, for which I am so deeply sorry and ashamed." | OK | PLEA | Verbatim. |
| 43 | say/scene.q | "As I engaged in my fraud, I knew what I was doing was wrong, indeed criminal." | OK | PLEA | Verbatim. |
| 44 | say/scene | No trial; remanded into custody same day pending sentencing | OK | PLEA-PR | |
| 45 | say | Chapter title | OK | — | |
| 46 | say/show/scene | Jun 29, 2009; Chin heard from nine victims about devastation to lives and families | OK | SENT-PR; FORTUNE | |
| 47 | say/scene.q | "I live on food stamps. At the end of the month, I sometimes scavenge in dumpsters." | OK | FORTUNE | Verbatim (victim Miriam Siegman; unnamed in script — fine). |
| 48 | say/scene.q | "I apologize to my victims. I will turn and face you … I'm sorry. I know that doesn't help you." | OK | FORTUNE | Both segments verbatim; joined by ellipsis. |
| 49 | say/scene | "a legacy of shame" to his family and grandchildren | OK | FORTUNE | |
| 50 | say/scene.q | "Objectively speaking, the fraud was staggering … the breach of trust was massive." | OK | SENT-PR | Cited to U.S. Attorney's release — correct (not in Fortune). |
| 51 | say/scene.q | "not merely a bloodless crime that takes place on paper but one that takes a staggering human toll." | OK | SENT-PR | Verbatim. |
| 52 | say/scene | "extraordinarily evil" | OK | SENT-PR; FORTUNE | |
| 53 | say/scene.q | "I do not agree that the victims are succumbing to the temptation of mob vengeance." | OK | FORTUNE | Verbatim, Judge Chin. |
| 54 | say/scene | "symbolism is important" | OK | FORTUNE | Judge Chin. |
| 55 | say | 20 yrs: securities, mail, wire fraud, 2 money laundering, false SEC filing; 10 for 3rd ML count; 5 each for rest | OK | PLEA-PR p.3 | Counts 1,3,4,5,6,10 = 20; count 7 = 10; counts 2,8,9,11 = 5. |
| 56 | say/show/scene | 6×20 + 10 + 4×5 = 150 | OK | PLEA-PR | Arithmetic correct; PLEA-PR: "statutory maximum sentence of 150 years". |
| 57 | say/show/scene | Sentenced to 150 years, the statutory maximum | OK | SENT-PR; PLEA-PR | |
| 58 | say/show/scene | Forfeit $170,799,000,000, total proceeds of and property involved in certain crimes | OK | SENT-PR | |
| 59 | say | Chapter title | OK | — | |
| 60 | say/show/scene | Est. $17.5B put in; trustees recovered >$14B by 2021 | OK | AP | AP: "court-appointed trustees have recovered more than $14 billion of an estimated $17.5 billion". |
| 61 | say/show | "More than 15,400 claims were filed by investors who said they had lost money." | FIX | AP | AP only says "More than 15,400 claims against Madoff were filed." The "who said they had lost money" clause is not in the source. say: "More than fifteen thousand four hundred claims were filed against Madoff." show: "More than 15,400 claims were filed against Madoff." scene.label: "claims filed against Madoff" |
| 62 | say/show/scene | MVF final distribution began Dec 30, 2024; total >$4.3B; >40,000 victims; nearly 130 countries | OK | NBC; DOJ-MVF | DOJ: $4.3B+ to 40,930 victims in 127 countries. Consider citing DOJ directly. |
| 63 | say/show | DOJ: recovery nearly 94% of losses | OK | DOJ-MVF; NBC | DOJ subheadline "Nearly 94% of Fraud Losses" (93.71%). |
| 63 | scene.label | "of estimated losses recovered by victims" | FIX | DOJ-MVF | DOJ figure (93.71%) refers to total recoveries of the victims receiving MVF payments, measured against their fraud losses — not all estimated losses. label: "of fraud losses recovered by eligible\|Madoff Victim Fund claimants" |
| 64 | say/show/scene | Peter Madoff sentenced to 10 years in 2012 | OK | AP | Living person; statement is accurate and neutral. |
| 65 | say/show/scene | Died in federal custody at FMC Butner, NC, Apr 14, 2021, aged 82 | OK | AP | |
| 66 | say/scene.q | "as the years went by I realized that my arrest and this day would inevitably come." | OK | PLEA | Verbatim. |
| 67 | say/scene | "The paper trail he built to hide the money became the evidence that ended it." | UNSUPPORTED | ARREST; COMPLAINT ¶4b–e; PLEA | The scheme ended because he could not meet ~$7B in redemption requests and confessed (complaint ¶4b, ¶4d). No source says the paper trail ended it. say: "The paper trail he built to hide the fraud became the record of it." scene.lines: ["The paper trail", "became the record."] |
| 68 | say | "...a famous name, and statements that always looked perfect. In the end, none of it was real, except the paperwork that proved it." | FIX | PLEA; COMPLAINT ¶4a | "None of it was real" overreaches: the famous name was real, and the plea/complaint describe separate, legitimate market-making/proprietary trading businesses. The statements were the fake part and did not "prove" the fraud. say: "Steady returns, year after year, a famous name, and statements that always looked perfect. In the end, the returns were never real. Only the paperwork was — and it was fake." |
| 68 | scene.lines | "Perfect statements. / Nothing behind them." | OK | PLEA; AP | Matches "No securities were ever bought or sold" in the advisory business. |
| 69 | say | "Real trials. Real evidence. The verdict." | OK (note) | — | Brand tagline. Note that this case had no trial (line 44); "verdict" is loose for a guilty plea. Consider "Real cases." |
