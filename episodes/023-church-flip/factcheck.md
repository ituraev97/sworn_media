# Fact-check: SWORN 023 "The Church Flipping Pastor" (United States v. Garcia, N.D. Tex. 4:26-cr-146-P)

Independent check, 2026-11-23. Sources:
- **PR**: USAO N.D. Tex. press release, Nov 20, 2026 (`/home/claude/dl/doj/prv.txt`)
- **IND**: Superseding Indictment, Dkt. 35 (`/home/claude/work/023/src/ind.txt`, page images `img/ind_pN.jpg`)
- **EX**: Government trial exhibits, DRAFT summary charts (`foa_exhibits.pdf`, pages viewed as images: p2, p4, p6, p8, p9, p11, plus text of all 29 pages)

Line index = 0-based position in the file's `lines` array. When `show` is the same as `say`, one verdict covers both.

## Source facts that matter for the fixes

- **Chronology (IND ¶14(b)–(c); EX p4, p8, p11):** Hazel St agreement Oct 6, 2023. Wires of $125,000 on **Oct 18** and $100,000 on **Oct 26** (8 days apart). Lubbock transfer **Nov 3** (8 days after Oct 26); Lubbock agreement dated Nov 6. EX p9 (the $6,000, Mercedes $1,204.18, Rangers $289.22) covers **Oct 30–31**.
- **Lubbock chart (EX p11):** 11/3/2023 beginning balance **$14,531.70**; 11/10/2023 ending **$6,158.24**. The balance was never "about six thousand" before the deposit, so it did not go "back to" that figure.
- **Count Five (IND pp.17–18):** the aggravated identity theft count charges the use of Individual E's name and address on a **Certificate of Formation for World Hotel Solutions-Texas LLC filed 12/12/2023**. It does **not** charge the $2.4M Commercial Contract (¶17). The script's "That allegation was also charged as aggravated identity theft" is wrong.
- **¶17:** the Commercial Contract named **Individual E himself** (the person Garcia asked for money) as the purported buyer. It describes "the real property at 1700 New York Ave", not a "church property". (The source text has a typo, "Individual I: did not agree", in a sentence that is otherwise entirely about Individual E.)
- **¶19:** lulling payments are "designed to address their specific victim request for payment of profits". Nothing in IND or EX labels the chart's "payments to others including to other investor" as lulling payments.
- **¶10(a), ¶14:** investors' Partnership Agreement money was "to improve and then resell" properties Garcia "had purportedly purchased" or owned. It was **not** money "to buy them". The church-flipping contracts promised a **specific ROI amount**. Profit-sharing appears only in the concert deals (¶10(b)).
- **EX p2:** "Investment: $225,000 / $168,000 / $290,000", "NEVER PURCHASED" in each address box, "PROCEEDS FROM SALE: $0" on each arrow. The chart shows **no total**, so $683,000 is SWORN's sum. The $290,000 matches EX pp.15–27 (59,800 + 130,000 + 60,000 + 40,000 = $289,800, Jan–Feb 2023). IND Count Four lists **$210,000** for Ryan Ave (Individual H). The $683,000 is accurate only when presented as the sum of the chart's three figures and attributed to the chart.
- **PR:** "Garcia served as a pastor during the scheme". It does **not** say "during the entire scheme". The PR gives the date range as "from at least August 2021 through April 2025" and attributes it to "evidence presented at trial". It says "Garcia and others solicited funds".
- **EX p4:** the account also took in $15,000 + $15,000 + $10,000 + $2,618.31 + $12,386 from other sources during Oct 18–25. Outflows therefore came from the account as a whole, not traceably from the $125,000 alone.
- **Private names:** EX p2/p4/p6/p9/p11 name two private investors and two other signors. All are blacked out in `img/f_*.jpg` and appear in no text field. No private victim's name appears in any checked text. **OK.**
- **Quotes:** Raybould (L60) and Rothrock (L61) quotes, and "a very quick decision by the jury" (L57), match the PR word for word. **OK.**

## Line-by-line table

### episode.json

| # | Field(s) | Verdict | Note |
|---|---|---|---|
| 0 | say/show, photo caption | OK | EX p2: Texarkana, Lubbock, Fort Worth. IND calls them church properties. |
| 1 | say/show | **FIX** | "to buy them" is unsupported. $683,000 is unattributed and is SWORN's sum. "A pastor called it" is unsupported (the term comes from PR/IND). See F1. |
| 2 | say/show, big | OK | EX p2 |
| 3 | say/show, verdict kicker/stamp/big/sub | OK | PR |
| 4 | say/show, doc title | OK | PR ¶1 and ¶"court documents"; band p_70 correct |
| 5 | say/show, title/sub | OK | |
| 6 | chapter | OK | |
| 7 | say | **FIX** | "during the entire scheme": the PR says "during the scheme". The show text and title are correct. See F2. |
| 8 | say/show, doc kicker/title | OK | IND ¶1; band i_entities correct |
| 9 | say/show, list items | OK | IND ¶2 (approx. Sept 2012; "previously operated using") |
| 10 | say/show, doc title | **FIX (minor)** | Indictment-only facts with no spoken attribution in this line. See F3. |
| 11 | say/show, doc title | OK | PR |
| 12 | say/show | OK | PR |
| 13 | say, big | **FIX** | "The profits were possible" is speculation. "The question the jury had to answer" misstates the jury's task, which was the charged counts. See F4. |
| 14 | chapter | OK | |
| 15 | say/show, doc title | **FIX** | Attributed to "the indictment" while the PR paragraph is on screen and says "from at least … evidence presented at trial". It also omits "and others". See F5. |
| 16 | say/show, doc title | OK | IND ¶10(a); band i_flip correct |
| 17 | say/show, doc title | OK | IND ¶10(b) |
| 18 | say/show, doc title | **FIX (minor)** | IND says he "intended to use" the funds for those expenses, not that the money "went" there. Say ("never intended") also differs from show ("did not intend"). See F6. |
| 19 | say | **FIX (minor)** | IND ¶10(d) says "offering … interest already 'owned'". It does not say "sold the same stake". Show is correct. See F7. |
| 20 | say | **FIX** | "members were asked": IND ¶10(e) says "victims", not church members. Show says "people". See F8. |
| 21 | say/show, big | OK | PR |
| 22 | chapter | OK | |
| 23 | say/show, doc title | OK | IND ¶14(a) (A and B sent the check). Attributed. |
| 24 | say/show, doc title | OK | IND ¶14(a)(i). Attributed. |
| 25 | say/show, doc title | **FIX** | Individual C's agreement is in IND only and is not attributed in speech. See F9. |
| 26 | say/show | OK | IND ¶14(b); EX p4/p8 ($125,000 Oct 18; $100,000 Oct 26) |
| 27 | say/show, doc title | **FIX** | "Two weeks later" is wrong. Lubbock money arrived Nov 3, 8 days after the Oct 26 wire. See F10. |
| 28 | say/show, doc title | OK | IND ¶14(b)(i), ¶14(c)(i). "secured title ownership" is verbatim. |
| 29 | say/show | OK | Attributed to IND |
| 30 | say/show, photo | **FIX (minor)** | The chart was released with the Nov 20 announcement, not "with the verdict" (Nov 19). See F11. |
| 31 | say, stat value/label | **FIX** | The stat presents $683,000 as a chart figure, but the chart has no total. "dollar by dollar" overstates (the charts cover a few days per deposit). See F12. |
| 32 | chapter | OK | |
| 33 | say/show, photo caption | OK | EX p4: 10/18/2023 beginning balance $1,566.03 |
| 34 | say/show, bars | **FIX** | Spoken figures ("thirty-six thousand", "eighteen thousand", "seventeen thousand") do not match the subtitle digits. "Then it goes out" implies the $125,000 itself, but the account had other inflows. Bars are OK. See F13. |
| 35 | say | **FIX** | "None of it … went to buy a church" is stronger than the chart. Say and show differ. See F14. |
| 36 | say/show, photo | **FIX (minor)** | "Sunday offerings": "Sunday" is not in the source. EX label is "INCOME FROM OTHERS, INCLUDING TITHES/OFFERINGS". See F15. |
| 37 | say/show, photo caption | OK | EX p6: $13,000 in; 10/18/2023 beginning ($2,332.49). "Week" covers a 10/18–10/27 window, acceptable. |
| 38 | say/show | **FIX** | Say "five thousand three hundred" does not match show $5,326.29. See F16. |
| 39 | say/show, photo caption | **FIX** | "Two weeks later, the second Texarkana wire" is wrong (Oct 26, 8 days later). The $6,000 and the payments are Oct 30–31. Say "one thousand two hundred" does not match $1,204.18. See F17. |
| 40 | say/show, photo caption | **FIX** | "back to about six thousand" is wrong. The balance started the window at $14,531.70. See F18. |
| 41 | say/show, doc title | **FIX** | Ties the chart's "payments to others" to "lulling payments", which no source does. "designed to keep them calm" is not the source language. Say and show differ. Title is verbatim (OK). See F19. |
| 42 | say/show, doc title | OK | PR ("often falsely claimed … reinvested") |
| 43 | chapter | OK | |
| 44 | say, big | **FIX** | The $2.4M contract allegation is unattributed in speech (show has "according to the indictment"). The big text is also unattributed. See F20. |
| 45 | say | **FIX (minor)** | Attributed to "the evidence" (PR), but the PR says "those accounts" (Ministerio Gracia, Iglesia Gracia de Texas, Gracia Church of Texas, APDT), not "accounts in the name of Gracia Church". Show is correct. See F21. |
| 46 | say/show | OK | PR |
| 47 | say/show, doc title | OK | IND ¶15(a); band correct |
| 48 | say/show, big | OK | IND ¶15 (paraphrase, attributed) |
| 49 | say/show, doc title | OK | IND ¶17 |
| 50 | say/show, doc title | **FIX** | "a church property": IND says "the real property". "the man listed as the buyer" hides that IND says the contract named Individual E himself. Title "$2,400,000" OK. See F22. |
| 51 | say/show, doc title | **FIX** | Count Five is NOT based on the contract. It charges Individual E's name on a Dec 12, 2023 LLC filing. Title "Five counts charged" is not on the highlighted band (case caption). See F23. |
| 52 | chapter | OK | |
| 53 | say/show, doc title | OK | PR |
| 54 | say, list items | OK | IND ¶23 table (Counts 2–4: dates, recipients, amounts) |
| 55 | say/show | OK | IND ¶23. $210,000 correctly attributed to IND. |
| 56 | say/show | OK | IND ¶9 (Co-Conspirator A); PR (4 counts) |
| 57 | say/show, doc title | OK | Verbatim PR |
| 58 | say/show, doc title | OK | PR |
| 59 | say/show, list | OK | PR |
| 60 | show, quote q/case/doc | OK | Verbatim PR |
| 61 | say/show, quote q/case/doc | OK | Verbatim PR |
| 62 | say/show, doc title | OK | PR |
| 63 | say/show, doc title | OK | PR |
| 64 | say/show, doc title | OK | PR |
| 65 | say, timeline events | **FIX** | "Three churches that were never bought" is unattributed. "$393,000 for Texarkana + Lubbock" = 225,000 + 168,000, correct. Other events OK. See F24. |
| 66 | say | **FIX (minor)** | "a pastor who did this" also covers uncharged and unadjudicated allegations (Kenya, the contract, Count 5). See F25. |

### short1.json

| # | Field(s) | Verdict | Note |
|---|---|---|---|
| title | title | **FIX** | "The Pastor Never Bought Them" is an unattributed chart assertion. See F26. |
| 0 | say/show, hook number/label/tag | OK | Attributed to the chart; $683,000 presented as the chart's three figures. |
| 1 | say/show, doc kicker | **FIX** | "split the profit": church-flipping contracts promised a specific ROI amount (IND ¶10(a)). Kicker lacks "ALLEGATIONS". See F27. |
| 2 | say/show, photo | OK | IND ¶14(b)(i)/(c)(i) plus EX p2 |
| 3 | say/show, verdict | OK | PR |
| 4 | say, end | OK | |

### short2.json

| # | Field(s) | Verdict | Note |
|---|---|---|---|
| title | title | OK | EX p4 → p6 (#2450 → #4494 → Mercedes Benz Financial Services) |
| 0 | say/show, hook | OK | EX p4. Attributed to "the government". |
| 1 | say/show, photo | OK | EX p6 |
| 2 | say/show, photo | OK | EX p6, p9 ("Later" covers the p9 window) |
| 3 | say/show, verdict | **FIX** | "The church he was supposed to buy": no source says Garcia was supposed to buy it with this money (IND: money to improve and resell). Unattributed. See F28. |
| 4 | say, end | OK | |

### short3.json

| # | Field(s) | Verdict | Note |
|---|---|---|---|
| title | title | OK | |
| 0 | say/show, hook | **FIX (minor)** | "his pastor" implies the investor was a member of Garcia's church. No source says that. See F29. |
| 1 | say/show, doc | OK | PR (U.S. Attorney kicker on screen; continues "prosecutors say") |
| 2 | say/show, doc | OK | IND ¶15(a), attributed |
| 3 | say/show, verdict | OK | PR |
| 4 | say | OK | |

### meta.json

| Field | Verdict | Note |
|---|---|---|
| title | **FIX** | "$6M 'Church Flipping' Fraud" implies the whole $6M was church flipping. The PR covers church flipping and concerts ("real estate and investment fraud scheme"). See F30. |
| summary | OK | PR. "from 2021 to 2025" OK. "used the money for other expenses" OK. |
| docs_note | OK | Redactions confirmed in img/f_*.jpg. PR re-typeset confirmed in prv_p1.jpg. |
| question | **FIX** | "Three churches never purchased" is unattributed. "a jury that took a 'very quick decision'" is the U.S. Attorney's characterization. See F31. |
| first_comment | **FIX (minor)** | Unattributed. See F32. |
| sources | CHECK | Could not verify the NBC headline wording (URL slug reads "north-texas-pastor-found-guilty…"), the Star-Telegram date (sources.md says Nov 22, 2026 UTC; meta says Nov 21), or the FBI form URL (not in the saved PR text). Verify before publishing. |

### thumb2.json, cards.js, thumbnail images

| Item | Verdict | Note |
|---|---|---|
| A q "WHERE / DID $6M / GO?" | OK | A question. PR says >$6M lost. |
| A tag "BREAKING" / stamp "GUILTY" | OK | |
| B tag "GUILTY" | OK | |
| B line1 "PASTOR'S $6M CHURCH SCHEME" | OK | PR (convicted; pastor; church-related entities) |
| B line2 "3 CHURCHES NEVER BOUGHT" | **FIX** | Unattributed chart assertion, not a jury finding. See F33. |
| C line1 "PASTOR'S ACCOUNT PAID MERCEDES" | OK | EX p6/p9: Richard R Garcia BOA #4494 → "Mercedes Benz Financial Services" ($1,645.23, $1,204.18). |
| C line2 "GUILTY ON 4 COUNTS" | OK | PR |
| img/t_never.jpg (cards.js box()) | **FIX** | Labeled "GOV'T TRIAL CHART (DRAFT)", but it is a re-typeset that drops the chart's "Investment:" label. A bare $225,000 next to "NEVER PURCHASED" reads like a purchase price. Figures and addresses match EX p2. See F34. |
| img/t_merc.jpg | **FIX (minor)** | $1,204.18, MBFS, #4494, Oct 2023 all match EX p9, but it is a re-typeset labeled as the chart. See F35. |
| cards.js header comment "re-typeset verbatim" | note | Layout, colors and labels differ from the chart. The comment is not on screen. |

---

## FIX details

**F1, episode L1**
- Current say: `Investors put in six hundred eighty-three thousand dollars to buy them, fix them up, and sell them at a profit. A pastor called it church flipping.`
- Current show: `Investors put in $683,000 to buy them, fix them up, and sell them at a profit. A pastor called it "church flipping."`
- Problem: IND ¶10(a)/¶14 says the money was to improve and resell properties Garcia purportedly owned or had purchased, not "to buy them". $683,000 is SWORN's sum of EX p2's three figures and is unattributed. No source says the pastor coined "church flipping" (PR: purported "church flipping" ventures; IND: "Church Flipping" contracts).
- New say: `According to the government's chart, investors put in a combined six hundred eighty-three thousand dollars to fix them up and sell them at a profit. Prosecutors call it church flipping.`
- New show: `According to the government's chart, investors put in a combined $683,000 to fix them up and sell them at a profit. Prosecutors call it "church flipping."`

**F2, episode L7 (say only)**
- Current: `…he served as a pastor during the entire scheme, and he used that position.`
- New say: `Richard Garcia is fifty-three. According to the U.S. Attorney's Office, he served as a pastor during the scheme, and he used that position.`
- Source: PR "served as a pastor during the scheme".

**F3, episode L10**
- New say: `Iglesia Gracia de Texas, registered in twenty twenty-two, had previously used the names Gracia Church Atlanta and Gracia Church, according to the indictment. And Gracia Church of Texas, registered in twenty eighteen, had once been called Richard Garcia Ministries.`
- New show: `Iglesia Gracia de Texas, registered in 2022, had previously used the names Gracia Church Atlanta and Gracia Church, according to the indictment. And Gracia Church of Texas, registered in 2018, had once been called Richard Garcia Ministries.`

**F4, episode L13 (say=show)**
- Current: `That is what made the pitch work. The churches existed. The renovations happened. The profits were possible. The question the jury had to answer was what happened to the investors' money.`
- New say/show: `That is what made the pitch work. The churches existed. Some renovations happened. Some properties did sell at a profit. The question was what happened to the investors' money.`
- Source: PR "Properties were improved and later sold for profit". The jury decided the charged counts, not this question.

**F5, episode L15**
- Current say: `From about August twenty twenty-one to April twenty twenty-five, the indictment says, Garcia sold two kinds of deals.`
- New say: `From at least August twenty twenty-one through April twenty twenty-five, according to the trial evidence, Garcia and others solicited money for two kinds of deals.`
- New show: `From at least August 2021 through April 2025, according to the trial evidence, Garcia and others solicited money for two kinds of deals.`
- Source: PR paragraph on screen (band p_scheme).

**F6, episode L18**
- New say: `The grand jury charged that he did not intend to host the concerts as scheduled, or to share the profits. Instead, it says, he intended to use the money for operating costs, unrelated business, and personal expenses.`
- New show: `The grand jury charged that he did not intend to host the concerts as scheduled, or to share the profits. Instead, it says, he intended to use the money for operating costs, unrelated business, and personal expenses.`
- Source: IND ¶10(b).

**F7, episode L19 (say)**
- New say: `There was more. The indictment says some investors were offered an interest already "owned" by other investors.` (same as show)

**F8, episode L20 (say)**
- Current say: `And members were asked for money for trips to Kenya…`
- New say: `And people were asked for money for trips to Kenya, typically two thousand dollars a person, for church programs there. According to the indictment, Garcia would cancel or never book those trips.`
- Show unchanged.

**F9, episode L25**
- New say: `Then came the big ones. According to the indictment, in October twenty twenty-three, an investor from Arizona, called Individual C, signed a partnership agreement for a church property on Hazel Street in Texarkana.`
- New show: `Then came the big ones. According to the indictment, in October 2023, an investor from Arizona, called Individual C, signed a partnership agreement for a church property on Hazel Street in Texarkana.`

**F10, episode L27**
- Current say: `Two weeks later, a second deal. A church property on East Queens Street in Lubbock. One hundred sixty-eight thousand dollars.`
- New say: `About a week after that second wire, on November third, a second deal, the indictment says. A church property on East Queens Street in Lubbock. One hundred sixty-eight thousand dollars.`
- New show: `About a week after that second wire, on November 3, a second deal, the indictment says. A church property on East Queens Street in Lubbock. $168,000.`
- Source: IND ¶14(c) (transfer Nov 3, 2023); EX p11.

**F11, episode L30**
- Replace `the chart prosecutors released with the verdict` with `the chart prosecutors released when they announced the verdict` in both say and show. Everything else unchanged.

**F12, episode L31**
- Current say: `So if the churches were never bought, where did the money go? The government followed it, dollar by dollar.`
- New say/show: `So if the churches were never bought, where did the money go? The government's charts follow it, account by account.`
- Stat label current: `three church deals · proceeds from sale: $0`
- New label: `the chart's three investments, added together · proceeds from sale: $0`

**F13, episode L34**
- Current say: `Then it goes out. Thirty-six thousand to payments to others, including to another investor. Twenty-two thousand to a title company, later reversed. Eighteen thousand in travel. Seventeen thousand in debt payments. Thirteen thousand to Richard Garcia's own account.`
- New say: `Then, the chart shows, money goes out of that account. About thirty-six thousand dollars in payments to others, including to another investor. Twenty-two thousand to a title company, later reversed. About eighteen thousand in travel. About seventeen thousand in debt payments. Thirteen thousand to Richard Garcia's own account.`
- New show: `Then, the chart shows, money goes out of that account. About $36,000 in payments to others, including to another investor. $22,000 to a title company, later reversed. About $18,000 in travel. About $17,000 in debt payments. $13,000 to Richard Garcia's own account.`
- Bars may keep the exact figures.

**F14, episode L35**
- New say: `One week later, the account was down to about thirteen thousand nine hundred dollars. According to the government's chart, the property was never purchased.`
- New show: `One week later, the account was down to about $13,900. According to the government's chart, the property was never purchased.`

**F15, episode L36 (say)**
- Replace `Investor money and Sunday offerings went into one account, and out of it.` with `Investor money and offerings went into one account, and out of it.`
- Also change "On the same days" to "That same week" in both say and show (chart window Oct 18–25).

**F16, episode L38**
- New say: `Out of it: five thousand three hundred twenty-six dollars in international transactions, in Panama. Utilities. And one thousand six hundred forty-five dollars to Mercedes-Benz Financial Services.`
- New show: `Out of it: $5,326 in international transactions, in Panama. Utilities. And $1,645 to Mercedes-Benz Financial Services.`

**F17, episode L39**
- Current say opening: `Two weeks later, the second Texarkana wire, one hundred thousand dollars. Another six thousand goes from the church account to Garcia.`
- New say: `On October twenty-sixth, the second Texarkana wire, one hundred thousand dollars, lands in the church account. A few days later, another six thousand goes from the church account to Garcia. Out of his account, according to the chart: debt payments. One thousand two hundred four dollars more to Mercedes-Benz. Two hundred eighty-nine dollars at the Texas Rangers, baseball and concessions. And smaller charges, labeled Jackpocket, Apple and Audible.`
- New show: `On October 26, the second Texarkana wire, $100,000, lands in the church account. A few days later, another $6,000 goes from the church account to Garcia. Out of his account, according to the chart: debt payments. $1,204 more to Mercedes-Benz. $289 at the Texas Rangers, "baseball & concessions." And smaller charges, labeled Jackpocket, Apple and Audible.`
- Source: IND ¶14(b); EX p8 (10/26–10/31); EX p9 (10/30–10/31).

**F18, episode L40**
- New say: `Then Lubbock. November third, one hundred sixty-eight thousand dollars into the same church account. One week later, the balance is down to about six thousand one hundred.`
- New show: `Then Lubbock. November 3, $168,000 into the same church account. One week later, the balance is down to $6,158.24.`
- Source: EX p11 (start $14,531.70, end $6,158.24).

**F19, episode L41**
- Current say: `Remember the payments to other investors. The indictment has a name for that: lulling payments. Money paid to victims who asked for their profits, designed to keep them calm.`
- New say: `The indictment also describes what it calls lulling payments: payments to victims, designed to address their requests to be paid their profits.`
- New show: `The indictment also describes what it calls "lulling payments": payments to victims, designed to address their requests to be paid their profits.`

**F20, episode L44**
- New say: `So far: the deals, the money trail, the Mercedes payments. But the strangest part of this case is a single word on the bank records. And then, according to the indictment, a two point four million dollar contract with someone else's name on it.`
- New show: `So far: the deals, the money trail, the Mercedes payments. But the strangest part of this case is a single word on the bank records. And then, according to the indictment, a $2.4 million contract with someone else's name on it.`
- Big lines: `["A $2.4 million contract.", "Someone else's|name on it, per the indictment."]`

**F21, episode L45 (say)**
- New say: `Here is the word from chapter two. According to the evidence, Garcia told victims to send their money to church-related accounts, and to call the payments donations to Gracia Church.`

**F22, episode L50**
- New say: `It showed Ministerio Gracia selling the property at seventeen hundred New York Avenue, Arlington, for two point four million dollars, to a buyer: Individual E himself. The indictment says he did not agree to buy it, did not know about the contract, and did not consent to his name and digital signature being put on it.`
- New show: `It showed Ministerio Gracia selling the property at 1700 New York Ave, Arlington, for $2,400,000, to a buyer: Individual E himself. The indictment says he did not agree to buy it, did not know about the contract, and did not consent to his name and digital signature being put on it.`
- Source: IND ¶17 (p.13 band i_24m shows "$2,400,000").

**F23, episode L51**
- Current say: `That allegation was also charged as aggravated identity theft. The U.S. Attorney's announcement of the verdict lists four counts of conviction, and does not mention that fifth count.`
- New say/show: `The indictment also charged a fifth count, aggravated identity theft, over the use of Individual E's name and address on a Texas business filing in December twenty twenty-three. The U.S. Attorney's announcement of the verdict lists four counts of conviction, and does not mention that fifth count.` (show: `…in December 2023. …`)
- Doc title current `Five counts charged` (band = case caption only). New title: `The superseding indictment`.

**F24, episode L65 (say=show)**
- New: `Three churches that, according to the government's chart, were never bought. Donations that were really investments. And, according to the government's own charts, a pastor's personal account that paid Mercedes-Benz.`

**F25, episode L66 (say=show)**
- New: `The judge will decide his sentence in March. What sentence do you think he should get? Tell us in the comments.`

**F26, short1 title**
- Current: `$683,000 for 3 Churches. The Pastor Never Bought Them.`
- New: `$683,000 for 3 Churches. Gov't Chart: "Never Purchased."`

**F27, short1 L1**
- New say: `Pastor Richard Garcia sold church flipping deals: renovate a church, sell it, pay the investor a set return.`
- New show: `Pastor Richard Garcia sold "Church Flipping" deals: renovate a church, sell it, pay the investor a set return.`
- Kicker: `SUPERSEDING INDICTMENT · ALLEGATIONS`

**F28, short2 L3**
- New say: `The Texarkana church in his deal? According to the government's chart, never purchased. Pastor Richard Garcia was found guilty on November nineteenth.`
- New show: `The Texarkana church in his deal? According to the government's chart, never purchased. Pastor Richard Garcia was found guilty on November 19.`

**F29, short3 L0**
- New say: `Why would an investor call his money a donation? Because, prosecutors say, the pastor told him to.`
- New show: `Why would an investor call his money a "donation"? Because, prosecutors say, the pastor told him to.`

**F30, meta title**
- New: `Pastor Richard Garcia GUILTY: “Church Flipping” Deals in a $6M Fraud`

**F31, meta question**
- New: `Three churches the government's chart says were never purchased, more than $6 million lost, and what the U.S. Attorney called "a very quick decision by the jury." What sentence should he get? Tell us in the comments.`

**F32, meta first_comment**
- New: `Prosecutors say investors were told to call their money "donations" to the church. Would that have made you suspicious — or made you trust it more?`

**F33, thumb2 B line2**
- New: `3 CHURCHES: "NEVER PURCHASED"`
- Alternative: keep the words, but the right panel must be labeled as the gov't chart (see F34).

**F34, cards.js / img/t_never.jpg**
- Header text `GOV'T TRIAL CHART (DRAFT)` → `RE-TYPESET FROM GOV'T TRIAL CHART (DRAFT)`.
- In `box()`, label the amount as an investment, as on the chart. Render `INVESTMENT: $225,000` (etc.), or add a small `INVESTMENT` line above the amount.
- Regenerate t_never.jpg.

**F35, cards.js / img/t_merc.jpg**
- Header text `GOV'T TRIAL CHART (DRAFT) · OCT 2023` → `RE-TYPESET FROM GOV'T TRIAL CHART (DRAFT) · OCT 2023`. Regenerate.

---

## FIXES

1. **ep L1**: say → "According to the government's chart, investors put in a combined six hundred eighty-three thousand dollars to fix them up and sell them at a profit. Prosecutors call it church flipping." / show → "According to the government's chart, investors put in a combined $683,000 to fix them up and sell them at a profit. Prosecutors call it "church flipping.""
2. **ep L7**: say "during the entire scheme" → "during the scheme".
3. **ep L10**: add ", according to the indictment," after "Gracia Church Atlanta and Gracia Church" (say and show).
4. **ep L13**: say/show → "That is what made the pitch work. The churches existed. Some renovations happened. Some properties did sell at a profit. The question was what happened to the investors' money."
5. **ep L15**: say → "From at least August twenty twenty-one through April twenty twenty-five, according to the trial evidence, Garcia and others solicited money for two kinds of deals." / show → "From at least August 2021 through April 2025, according to the trial evidence, Garcia and others solicited money for two kinds of deals."
6. **ep L18**: say/show → "The grand jury charged that he did not intend to host the concerts as scheduled, or to share the profits. Instead, it says, he intended to use the money for operating costs, unrelated business, and personal expenses."
7. **ep L19**: say → "There was more. The indictment says some investors were offered an interest already "owned" by other investors."
8. **ep L20**: say "And members were asked" → "And people were asked".
9. **ep L25**: say → "Then came the big ones. According to the indictment, in October twenty twenty-three, an investor from Arizona, called Individual C, signed a partnership agreement for a church property on Hazel Street in Texarkana." / show same with "October 2023".
10. **ep L27**: say → "About a week after that second wire, on November third, a second deal, the indictment says. A church property on East Queens Street in Lubbock. One hundred sixty-eight thousand dollars." / show → "About a week after that second wire, on November 3, a second deal, the indictment says. A church property on East Queens Street in Lubbock. $168,000."
11. **ep L30**: "the chart prosecutors released with the verdict" → "the chart prosecutors released when they announced the verdict" (say and show).
12. **ep L31**: say/show → "So if the churches were never bought, where did the money go? The government's charts follow it, account by account." Stat label → "the chart's three investments, added together · proceeds from sale: $0".
13. **ep L34**: say → "Then, the chart shows, money goes out of that account. About thirty-six thousand dollars in payments to others, including to another investor. Twenty-two thousand to a title company, later reversed. About eighteen thousand in travel. About seventeen thousand in debt payments. Thirteen thousand to Richard Garcia's own account." / show → "Then, the chart shows, money goes out of that account. About $36,000 in payments to others, including to another investor. $22,000 to a title company, later reversed. About $18,000 in travel. About $17,000 in debt payments. $13,000 to Richard Garcia's own account."
14. **ep L35**: say → "One week later, the account was down to about thirteen thousand nine hundred dollars. According to the government's chart, the property was never purchased." / show → "One week later, the account was down to about $13,900. According to the government's chart, the property was never purchased."
15. **ep L36**: say "Sunday offerings" → "offerings". "On the same days" → "That same week" (say and show).
16. **ep L38**: say → "Out of it: five thousand three hundred twenty-six dollars in international transactions, in Panama. Utilities. And one thousand six hundred forty-five dollars to Mercedes-Benz Financial Services." / show → "Out of it: $5,326 in international transactions, in Panama. Utilities. And $1,645 to Mercedes-Benz Financial Services."
17. **ep L39**: say → "On October twenty-sixth, the second Texarkana wire, one hundred thousand dollars, lands in the church account. A few days later, another six thousand goes from the church account to Garcia. Out of his account, according to the chart: debt payments. One thousand two hundred four dollars more to Mercedes-Benz. Two hundred eighty-nine dollars at the Texas Rangers, baseball and concessions. And smaller charges, labeled Jackpocket, Apple and Audible." / show → "On October 26, the second Texarkana wire, $100,000, lands in the church account. A few days later, another $6,000 goes from the church account to Garcia. Out of his account, according to the chart: debt payments. $1,204 more to Mercedes-Benz. $289 at the Texas Rangers, "baseball & concessions." And smaller charges, labeled Jackpocket, Apple and Audible."
18. **ep L40**: say → "Then Lubbock. November third, one hundred sixty-eight thousand dollars into the same church account. One week later, the balance is down to about six thousand one hundred." / show → "Then Lubbock. November 3, $168,000 into the same church account. One week later, the balance is down to $6,158.24."
19. **ep L41**: say → "The indictment also describes what it calls lulling payments: payments to victims, designed to address their requests to be paid their profits." / show → "The indictment also describes what it calls "lulling payments": payments to victims, designed to address their requests to be paid their profits."
20. **ep L44**: say → "…And then, according to the indictment, a two point four million dollar contract with someone else's name on it." / show → "…And then, according to the indictment, a $2.4 million contract with someone else's name on it." Big line 2 → "Someone else's|name on it, per the indictment."
21. **ep L45**: say → "Here is the word from chapter two. According to the evidence, Garcia told victims to send their money to church-related accounts, and to call the payments donations to Gracia Church."
22. **ep L50**: say → "It showed Ministerio Gracia selling the property at seventeen hundred New York Avenue, Arlington, for two point four million dollars, to a buyer: Individual E himself. The indictment says he did not agree to buy it, did not know about the contract, and did not consent to his name and digital signature being put on it." / show → "It showed Ministerio Gracia selling the property at 1700 New York Ave, Arlington, for $2,400,000, to a buyer: Individual E himself. The indictment says he did not agree to buy it, did not know about the contract, and did not consent to his name and digital signature being put on it."
23. **ep L51**: say → "The indictment also charged a fifth count, aggravated identity theft, over the use of Individual E's name and address on a Texas business filing in December twenty twenty-three. The U.S. Attorney's announcement of the verdict lists four counts of conviction, and does not mention that fifth count." / show same with "December 2023". Doc title "Five counts charged" → "The superseding indictment".
24. **ep L65**: say/show → "Three churches that, according to the government's chart, were never bought. Donations that were really investments. And, according to the government's own charts, a pastor's personal account that paid Mercedes-Benz."
25. **ep L66**: say/show → "The judge will decide his sentence in March. What sentence do you think he should get? Tell us in the comments."
26. **short1 title** → "$683,000 for 3 Churches. Gov't Chart: "Never Purchased.""
27. **short1 L1**: say → "Pastor Richard Garcia sold church flipping deals: renovate a church, sell it, pay the investor a set return." / show → "Pastor Richard Garcia sold "Church Flipping" deals: renovate a church, sell it, pay the investor a set return." Kicker → "SUPERSEDING INDICTMENT · ALLEGATIONS".
28. **short2 L3**: say → "The Texarkana church in his deal? According to the government's chart, never purchased. Pastor Richard Garcia was found guilty on November nineteenth." / show → same with "November 19."
29. **short3 L0**: "his pastor told him to" → "the pastor told him to" (say and show).
30. **meta title** → "Pastor Richard Garcia GUILTY: “Church Flipping” Deals in a $6M Fraud"
31. **meta question** → "Three churches the government's chart says were never purchased, more than $6 million lost, and what the U.S. Attorney called "a very quick decision by the jury." What sentence should he get? Tell us in the comments."
32. **meta first_comment** → "Prosecutors say investors were told to call their money "donations" to the church. Would that have made you suspicious — or made you trust it more?"
33. **thumb2 B line2** → `3 CHURCHES: "NEVER PURCHASED"`
34. **cards.js / t_never.jpg**: header → "RE-TYPESET FROM GOV'T TRIAL CHART (DRAFT)". Label each amount "INVESTMENT: $225,000" / "$168,000" / "$290,000". Regenerate.
35. **cards.js / t_merc.jpg**: header → "RE-TYPESET FROM GOV'T TRIAL CHART (DRAFT) · OCT 2023". Regenerate.
36. **meta sources (verify, not a text error)**: confirm the NBC headline wording, the Star-Telegram date (Nov 21 vs sources.md "Nov 22 UTC") and the FBI form URL before publishing.
