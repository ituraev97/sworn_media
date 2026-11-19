# SWORN 019 — Backward Hat Capital — Independent fact-check

Checked 2026-11-19 against: criminal complaint (U.S. v. Williams & Johnson, S.D.N.Y., sworn Nov 17, 2026; `/home/claude/dl/bh/doj/complaint.txt`), USAO S.D.N.Y. press release 26-330 (Nov 18, 2026; `pr.txt`), and the secondary sources in sources.md, fetched with WebFetch: WRTV (fetched), The Indiana Lawyer/IBJ (fetched), Minkow Substack (fetched).
Scope: episode.json (say/show/scene), short1-3.json, thumb2.json, meta.json, zoomcard.js and the rendered img/t_*, h_*, z_* cards.
Index = 0-based index into `lines`.

## FIX items

### episode.json

1. **episode.json [0] say/show.** Current: "...the man who runs a six-hundred-million-dollar investment fund." Problem: this is unattributed and comes before the presumption-of-innocence line. The $600M was raised across more than 12 funds (C ¶9, ¶12). It is not the size of one fund.
   - say: "May fourteenth, twenty twenty-six. According to federal prosecutors, a text message arrives for the man running an investment firm that raised more than six hundred million dollars. Aggressive fund, ten point oh one percent. Does this sound right?"
   - show: "May 14, 2026. According to federal prosecutors, a text message arrives for the man running an investment firm that raised more than $600 million. \"Aggressive fund 10.01% / Does this sound right?\""

2. **episode.json [1] say/show.** Current show: "...he answers: \"Let's do 9.91. Bumped it up a bit.\"" Problem: the quote is not verbatim. The original has no period after 9.91 and starts with an ellipsis. The complaint also leaves out part of the exchange ("..."), so "and then he answers" suggests a reply that came right away.
   - say: "He asks what it was last month. Nine point five one, the employee says. Later in the exchange, according to federal prosecutors, he writes: Let's do nine point nine one, bumped it up a bit."
   - show: "He asks what it was last month. \"9.51% last month,\" the employee says. Later in the exchange, according to federal prosecutors, he writes: \"… Let's do 9.91 bumped it up a bit.\""

3. **episode.json [3] say/show.** Current: "More than two thousand investors put in more than six hundred million dollars." Problem: a complaint figure is stated as fact before the disclaimer.
   - say: "According to prosecutors, more than two thousand investors put in more than six hundred million dollars. They were told the fund typically made more than six percent a month."
   - show: "According to prosecutors, more than 2,000 investors put in more than $600 million. They were told the fund typically made more than 6% a month."

4. **episode.json [4] scene.big.** Current: "Securities & wire fraud". Problem: there is no substantive wire-fraud count. The counts are securities fraud, conspiracy to commit wire fraud and conspiracy to commit securities fraud (C counts 1–3; PR). Replacement: "Securities fraud & conspiracy"

5. **episode.json [8] say/show.** Current: "Williams was fifty-one... Johnson was twenty-nine..." Problem: this is a chronology error. The ages (51 and 29) are from the PR as of Nov 2026. Using "was" inside the 2022 founding chapter suggests those were their ages at founding.
   - say: "Today Williams is fifty-one, of Kokomo. Johnson is twenty-nine, of Zionsville, outside Indianapolis. The audit reports investors later received called Williams the Managing Partner and C.E.O., and Johnson the Managing Director of Algorithmic Strategy."
   - show: "Today Williams is 51, of Kokomo. Johnson is 29, of Zionsville, outside Indianapolis. The audit reports investors later received called Williams the \"Managing Partner/CEO\", and Johnson the \"Managing Director, Algorithmic Strategy.\""

6. **episode.json [13] scene.label.** Current: "a year — money doubled in 12 months". Problem: this reads as a fact that money doubled. The complaint says an investor "would more than double their money" at the reported rate. Replacement: "a year, on paper: money would more than double"

7. **episode.json [16] scene.title.** Current: "The same return, every fund, every month". Problem: this is false as written. ¶16 makes an exception for the "aggressive" fund, which earned more. Replacement: "The same return, every fund but one"

8. **episode.json [22] show.** Current: "\"10.01%, does this sound right?\" \"What was it last month?\" \"9.51%.\" \"Let's do 9.91, bumped it up a bit.\"" Problem: the quotes are not verbatim. Words are dropped without marks and commas are added.
   - say (unchanged is acceptable): "And then the exchange from May. Aggressive fund, ten point oh one, does this sound right. What was it last month. Nine point five one last month. Let's do nine point nine one, bumped it up a bit."
   - show: "And then the exchange from May. \"Aggressive fund 10.01% / Does this sound right?\" \"What was it last month?\" \"9.51% last month …\" \"… Let's do 9.91 bumped it up a bit\""

9. **episode.json [23] say.** Current: "...The bank records tell that part." Problem: this presents the agent's reading of the bank records as established.
   - say/show: "If the returns were set by text, what happened to the money itself? The complaint points to bank records."

10. **episode.json [27] say/show.** Current: "...to what Backward Hat called G.P.s: people enlisted to bring in more investors." Problem: "GPs" is the complaint's defined term (¶19(c)). Nothing in the record shows what Backward Hat called them.
    - say: "More than about two hundred million went to the founders and to general partners, or G.P.s, whom the complaint describes as people Backward Hat enlisted to bring in more investors."
    - show: "More than about $200 million went to the founders and to general partners, or \"GPs\", whom the complaint describes as people Backward Hat enlisted to bring in more investors."

11. **episode.json [30] say/show.** Current: "an employee noticed that Johnson had moved..." Problem: the complaint says the employee "learned". The first sentence is also unattributed.
    - say: "One more detail. On February twelfth, twenty twenty-six, according to the complaint, an employee learned that Johnson had moved about three hundred thousand dollars from a Backward Hat account into his personal account. Confronted, the complaint says, he put it back."
    - show: "One more detail. On February 12, 2026, according to the complaint, an employee learned that Johnson had moved about $300,000 from a Backward Hat account into his personal account. Confronted, the complaint says, he put it back."

12. **episode.json [31] say + scene.lines.** Current: "...keep raising money for three years?" with the card "Three years." Problem: the time span is wrong. Backward Hat was founded in July 2022, and the complaint (¶27) says it was still raising money in Oct/Nov 2026. That is more than four years.
    - say/show: "So how did Backward Hat keep raising money for more than four years? Investors had a document that seemed to answer every doubt. An independent audit."
    - scene.lines: ["Four-plus years.", "One document:|“Independent.”"]

13. **episode.json [34] say/show.** Current say: "...average gross return of six point three percent a month..." Problem: "a month" is not in the source. ¶14(b) says "an average gross return of 6.3% from 2023 through mid-2025". The spoken line also does not match the subtitle, which has no "a month".
    - say: "The audit reported an average gross return of six point three percent from twenty twenty-three through mid twenty twenty-five, and concluded that the fund exhibits strong financial integrity, sound governance, and consistent performance across all audited periods."
    - show: "The audit reported an average gross return of 6.3% from 2023 through mid-2025, and concluded that the fund \"exhibits strong financial integrity, sound governance, and consistent performance across all audited periods.\""

14. **episode.json [39] say/show.** Current: "The auditor, prosecutors say, had his own stake in the fund he was auditing." Problem: this overstates the complaint. The complaint says the Auditor's CEO had "personal interests in Backward Hat that were not disclosed to investors". It does not mention a "stake" in a fund he personally audited. The $2M commitments had "not yet materialized", and the audit was done by the firm. The line also implies wrongdoing by a third party who is not charged.
    - say: "He wrote that if those commitments had been honored as represented, he would have accumulated no less than two million dollars in his personal Backward Hat account. They had not yet materialized, he wrote. Prosecutors say the auditor's C.E.O. had personal interests in Backward Hat that investors were never told about. The complaint does not name the auditor or its C.E.O., and neither is charged."
    - show: "He wrote that if those commitments had been honored as represented, he would have \"accumulated no less than $2,000,000\" in his personal Backward Hat account. They had \"not yet materialized,\" he wrote. Prosecutors say the auditor's CEO had personal interests in Backward Hat that investors were never told about. The complaint does not name the auditor or its CEO, and neither is charged."

15. **episode.json [40] say + scene.lines.** Current: "...already building a second fund" with the card "A second fund." Problem: this is false. Backward Hat had more than twelve funds (¶12). AI Capital was "a related fund".
    - say/show: "And while the audit was still being sent out, the complaint says Johnson was already building another fund. With a name built for twenty twenty-five." (show: "...built for 2025.")
    - scene.lines: ["Another fund.", "Its name:|AI Capital."]

16. **episode.json [44] say/show.** Current: "...showing profitable forex trading..." Problem: ¶23(c) says the spreadsheet "purported to show" this. As written, the line presents the trades as real.
    - say: "A data room for prospective investors held a spreadsheet titled Trades, B.H., presented as an export of executed trades from the fund that supports A.I. Capital. It purported to show profitable forex trading over about three weeks in the summer of twenty twenty-four."
    - show: "A data room for prospective investors held a spreadsheet titled \"Trades – BH\", presented as an \"[e]xport of executed trades from BH Capital, the fund that supports AI Capital.\" It purported to show profitable forex trading over about three weeks in the summer of 2024."

17. **episode.json [46] say/show + scene.lines.** Current: "Then, in the summer of 2026, investors started asking for their money back." with the card "Investors asked|for their money." Problem: investors had been redeeming all along; ¶19(b) says about $200M was paid to existing investors. What began in summer 2026 was difficulty meeting withdrawal requests (¶24).
    - say: "Then, in the summer of twenty twenty-six, according to the complaint, Backward Hat began struggling to pay investors who asked for their money back."
    - show: "Then, in the summer of 2026, according to the complaint, Backward Hat began struggling to pay investors who asked for their money back."
    - scene.lines: ["Summer 2026.", "Withdrawals|delayed."]

18. **episode.json [50] scene.title.** Current: "“Liquidity continues to arrive in increments”". Problem: the document reads "[l]iquidity". A card title in quotation marks should match the document on screen. Replacement: "“[l]iquidity continues to arrive in increments”"

19. **episode.json [56] say/show.** Current: "...swore to the complaint before Magistrate Judge Gary Stein in Manhattan." Problem: the complaint was sworn "through ... reliable electronic means (telephone)". It was not sworn in person in Manhattan.
    - say: "On November seventeenth, Homeland Security Investigations Special Agent Robert Fanesi swore to the complaint by telephone before Magistrate Judge Gary Stein of the Southern District of New York. It was filed under seal."
    - show: "On November 17, Homeland Security Investigations Special Agent Robert Fanesi swore to the complaint by telephone before Magistrate Judge Gary Stein of the Southern District of New York. It was filed under seal."

20. **episode.json [57] say/show.** Current: "The next morning, it was unsealed." Problem: the PR gives only the day of the unsealing (Nov 18). The arrests, not the unsealing, were "this morning".
    - say/show: "The next day, it was unsealed. Williams was arrested that morning in Kokomo and brought before a federal court in the Southern District of Indiana. Johnson was arrested in Gilbert, Arizona, to appear in federal court there the next day."

21. **episode.json [59] say/show.** Current: "Jamie McDonald called it, quote, alleging a $600 million investment fraud scheme." Problem: the source says "These charges—alleging a $600 million investment fraud scheme—demonstrate...". McDonald described the charges. He did not "call it" that.
    - say: "U.S. Attorney Jamie McDonald said the charges are, quote, alleging a six-hundred-million-dollar investment fraud scheme. The Homeland Security Investigations, F.B.I., and I.R.S. Criminal Investigation offices in New York, Indianapolis and Chicago worked the case."
    - show: "U.S. Attorney Jamie McDonald said the charges are \"alleging a $600 million investment fraud scheme.\" The HSI, FBI and IRS Criminal Investigation offices in New York, Indianapolis and Chicago worked the case."

22. **episode.json [61] say/show.** Current: "...he had filed a report on Backward Hat with regulators back in July, and had been asked not to discuss the case publicly." Problem: the Substack body says only that "my whistleblower counsel and I filed a detailed investigative report on Backward Hat Capital" in July 2026. It does not name a recipient. The request "came through my lawyers"; the CFTC is named only in the headline. "With regulators" is therefore unsupported.
    - say/show: "And one fraud investigator, Barry Minkow, wrote the same day that he and his lawyer had filed a detailed report on Backward Hat back in July, and that a request then came through his lawyers: do not discuss this case publicly. That is his account."
    - (show may quote: "...a request then came through his lawyers: \"Do not discuss this case publicly.\" That is his account.")

23. **episode.json [62] say/show + scene.lines.** Current: "...the Indianapolis Business Journal's calls to them got no immediate response." and the card "No public|statement|yet." Problem: IBJ wrote that it "left a phone message at numbers it believes to be Johnson's and Williams's but did not receive an immediate response." The DOJ spokesperson said they used appointed counsel "for their presentments in Arizona and Indiana". "Nothing public" is also an absolute claim the channel cannot verify.
    - say/show: "What do the defendants say? We found no public statement from either man. A Justice Department spokesperson said both were using appointed counsel for their initial court appearances, and the Indianapolis Business Journal said phone messages it left at numbers it believes are theirs got no immediate response."
    - scene.lines: ["No public", "statement|found."]

24. **episode.json [65] say/show.** Current: "the head of the I.R.S. Criminal Investigation office in Chicago, Robert Kuszynski". Problem: the PR names him as *Acting* Special Agent in Charge.
    - say: "But the acting head of the I.R.S. Criminal Investigation office in Chicago, Robert Kuszynski, left one line that works for anyone, anywhere. When someone promises extraordinary returns with little risk, ask hard questions. Easy money often comes at someone else's expense."
    - show: "But the acting head of the IRS Criminal Investigation office in Chicago, Robert Kuszynski, left one line that works for anyone, anywhere. \"When someone promises extraordinary returns with little risk, ask hard questions. Easy money often comes at someone else's expense.\""

25. **episode.json [66] say/show.** Current: "Six percent a month, every month, and an audit that said it was all real." Problem: the narrator states this as fact, and "every month" is not supported. Returns "typically exceeded" 6% (¶9). The dashboard covered only Oct 2023–Sep 2026 (¶17).
    - say: "More than six percent a month on paper, month after month, and an audit that called it sound. Would you have asked the hard questions? Tell us in the comments."
    - show: "6%+ a month on paper, month after month, and an audit that called it sound. Would you have asked the hard questions? Tell us in the comments."

### short1.json

26. **short1 [0] say/show.** Current: "Six hundred million dollars from two thousand investors." Problem: the source says *more than* $600M from *more than* 2,000 investors.
    - say: "More than six hundred million dollars from more than two thousand investors. And prosecutors say the monthly return was picked by text message."
    - show: "$600M+ from more than 2,000 investors. And prosecutors say the monthly return was picked by text message."

27. **short1 [1] say/show.** Current: "An employee asks: 10.01%, does this sound right? The founder answers: let's do 9.91, bumped it up a bit." Problem: "The founder" implies a sole founder; there were three co-founders. The quotes are not verbatim, and the exchange skipped in between is not marked.
    - say: "An employee texts: aggressive fund, ten point oh one percent, does this sound right? Later, prosecutors say, co-founder Phillip Williams replies: let's do nine point nine one, bumped it up a bit."
    - show: "An employee texts: \"Aggressive fund 10.01% / Does this sound right?\" Later, prosecutors say, co-founder Phillip Williams replies: \"… Let's do 9.91 bumped it up a bit\""

28. **short1 [2] say/show.** Current: "On the dashboard, every month showed six to seven percent. Only minimal funds, the complaint says, went to trading." Problem: the range was 6.01–7.21%, so "six to seven" is wrong. The first sentence is unattributed. "Went to trading" overstates "appear to have been potentially used for forex trading".
    - say: "On the investor dashboard, the complaint says, the monthly rate stayed between six point oh one and seven point two one percent. Only minimal funds, it says, appear to have been potentially used for forex trading."
    - show: "On the investor dashboard, the complaint says, the monthly rate stayed between 6.01% and 7.21%. \"Only minimal funds,\" it says, \"appear to have been potentially used for forex trading.\""

29. **short1 [3] say/show.** Current: "On November eighteenth, both founders were arrested." Problem: only two of three co-founders were charged, so "both founders" is false.
    - say: "On November eighteenth, two of its co-founders were arrested. They're charged, not convicted, and presumed innocent."
    - show: "On November 18, two of its co-founders were arrested. They're charged, not convicted, and presumed innocent."

### short2.json

30. **short2 title.** Current: "$130M to One Founder: Where a $600M Fund's Money Went". Problem: a complaint allegation is stated as fact in the title, and the "+" is dropped. Replacement: "$130M+ to One Founder, Feds Allege: Where a $600M Fund's Money Went"

31. **short2 [0] say/show.** Current: "A hundred thirty million dollars..." Problem: the complaint says "more than $130 million", and the hook card shows "$130M+". "A six-hundred-million-dollar forex fund" is also loose, since that money was raised across a firm with more than 12 funds.
    - say: "More than a hundred thirty million dollars. That's how much went to one founder's accounts, federal prosecutors allege, from a forex firm that raised six hundred million."
    - show: "More than $130 million. That's how much went to one founder's accounts, federal prosecutors allege, from a forex firm that raised $600 million."

32. **short2 [1] say/show.** Current: "At least two hundred million..." Problem: the source says "at least approximately $200 million".
    - say: "At least about two hundred million, the complaint says, paid earlier investors with newer investors' money."
    - show: "At least about $200 million, the complaint says, paid earlier investors with newer investors' money."

33. **short2 [2] say/show.** Current: "Over forty million went to the other founder. And the forex trading? Only minimal funds, the agent writes." Problem: the first sentence is unattributed. "The other founder" implies only two founders. "Only minimal funds" drops the hedge "appear to have been potentially used".
    - say: "More than forty million, it says, went to accounts controlled by co-founder Devin Johnson. And the forex trading? Only minimal funds appear to have been potentially used for it, the agent writes."
    - show: "More than $40 million, it says, went to accounts controlled by co-founder Devin Johnson. And the forex trading? \"Only minimal funds appear to have been potentially used\" for it, the agent writes."

### short3.json

34. **short3 [2] say/show.** Current: "Investors were told about longer processing times. Then about a third-party identity validator." Problem: ¶25(a) describes a *proposed* email that Williams sent to a GP. The complaint does not say investors received it. The line also gives no date, so "Five days later" in [3] has nothing to anchor to.
    - say: "Williams drafted an investor email about longer processing times, the complaint says. Then, on November thirteenth, he told investors about a third-party identity validator."
    - show: "Williams drafted an investor email about longer processing times, the complaint says. Then, on November 13, he told investors about \"a third-party identity validator.\""

35. **short3 [3] say/show.** Current: "Five days later, on November eighteenth, both founders were arrested." Problem: "both founders" is false (three co-founders, two charged).
    - say: "Five days later, on November eighteenth, two of its co-founders were arrested. They are charged, not convicted, and presumed innocent."
    - show: "5 days later, on November 18, two of its co-founders were arrested. They are charged, not convicted, and presumed innocent."

### thumb2.json / thumbnail images

36. **thumb2.json A.left.q.** Current: ["WHERE'S", "THE", "$600M?"]. Problem: this implies the entire $600M is missing. The complaint traces at least about $200M paid back to investors and more than about $200M paid to founders and GPs. Replacement: ["WHERE DID", "$600M", "GO?"]

37. **img/t_130.jpg (thumb A right panel) / zoomcard.js `t_130`.** Problem: at 78px the text overflows the 720px card. The attribution footer ("U.S. v. WILLIAMS & JOHNSON · S.D.N.Y. · Criminal complaint ¶ 19(c) · allegation") is cut off, so the thumbnail shows an allegation with no source. The excerpt is also cut mid-sentence with no ellipsis. Fix: set the font to 58 and change the text to `more than <mark>$130 million</mark> to accounts under the control of PHILLIP PATRICK WILLIAMS . . .`, then re-render and confirm the footer is visible.

38. **thumb2.json C.line2.** Current: "FOUNDERS CHARGED". Problem: only two of three co-founders are charged. Replacement: "2 FOUNDERS CHARGED"

39. **thumb2.json C.right.label.** Current: "EVERY MONTH" (with "6%+"). Problem: the source does not support "every month". Returns "typically exceeded" 6% (¶9), and the 6.01–7.21% range covers only the dashboard from Oct 2023 to Sep 2026. The label also reads as fact. Replacement: "A MONTH, ON PAPER"

### zoomcard.js (excerpt verbatim marks)

40. **zoomcard.js `z_130` and `h_130`.** Problem: the excerpts stop mid-sentence with no ellipsis. The original continues ", the defendant, and more than $40 million to ...". Fix: append ` . . .`
    - z_130: `Those payments included more than <mark>$130 million</mark> to accounts under the control of PHILLIP PATRICK WILLIAMS . . .`
    - h_130: `Those payments included more than <mark>$130 million</mark> to accounts under the control of PHILLIP PATRICK WILLIAMS, the defendant . . .`
    - Re-render img/z_130.jpg and img/h_130.jpg.

### meta.json

41. **meta.json title.** Current: "Backward Hat Capital: $600M Forex Fund Founders CHARGED". Problem: "Founders" implies all the founders were charged; only two of three were. Replacement: "Backward Hat Capital: 2 Founders of $600M Forex Fund CHARGED"

42. **meta.json summary.** Problems: "charging the fund's co-founders" implies all of them were charged. "with reported returns above 6% a month" drops "typically". The keyword line states "forex Ponzi scheme" as fact.
    - Replace "charging the fund's co-founders Phillip Patrick Williams and Devin Allen Johnson" with "charging two of its three co-founders, Phillip Patrick Williams and Devin Allen Johnson,"
    - Replace "with reported returns above 6% a month" with "with reported returns that typically exceeded 6% a month"
    - Replace "forex Ponzi scheme" (keyword line) with "alleged forex Ponzi scheme"

43. **meta.json question.** Current: "6% a month, every month, with an audit to back it up — ..." Problem: "every month" is not supported (same as #25). Replacement: "6%+ a month on paper, month after month, with an audit calling it sound — would you have asked the hard questions? Tell us in the comments."

## OK-verified (brief)

- May 14, 2026 exchange: the speakers are correct (employee: 10.01% / "Does this sound right?" / "9.51% last month"; Williams: "What was it last month?" / "Let's do 9.91 bumped it up a bit"). The quote card at [22] correctly credits both quoted lines to Williams. The h_991/z_991/t_991 cards are verbatim, and the gaps are marked with "[ . . . ]" and ". . .".
- Aug 5, 2026: "For returns tomorrow. Let me know if you need anything else." / "6.62". The four-character count is correct. 6.62% was the July 2026 rate for the non-aggressive funds, per the agent (¶18).
- $600M+ from more than 2,000 investors; founded in or about July 2022; three co-founders with equal shares; Co-Founder-3 unnamed (¶9, ¶11).
- Ages 51 and 29; Kokomo and Zionsville; arrests in Kokomo and Gilbert, AZ; Williams presented in S.D. Ind. and Johnson set to appear in D. Ariz. the next day (PR; WRTV agrees).
- Titles "Managing Partner/CEO" and "Managing Director, Algorithmic Strategy" (¶14(a)); 2023 deck quotes; website wording; more than 12 funds (¶12–13).
- More than 6% a month typically; more than 100% a year compounded; "more than double" (¶9).
- Same rate across funds except the aggressive one; Jan–Aug 2026 floors of 6% and 9.5%; dashboard range 6.01%–7.21% from Oct 2023 to Sep 2026 (¶16–17).
- About $200M Ponzi-like (the complaint's term, "Ponzi scheme-like fashion"); more than $200M to founders and GPs; more than $130M to Williams; more than $40M to Johnson; "Only minimal funds appear to have been potentially used for forex trading" (¶19). The bars card is labelled "PER THE COMPLAINT".
- Feb 12, 2026: about $300,000 taken and returned after being confronted (¶20).
- Audit: "Independent Financial Audit" and "Quality of Earnings" reports for FY2023–2025; the "strong financial integrity..." quote; the opinion-letter quote with [the fund] correctly bracketed; "independent" used repeatedly; reports sent Nov 14, 2025 to an investor who later invested (¶14–15).
- Williams co-founded a company with the Auditor's CEO; the May 29, 2026 email quote; "no less than $2,000,000" (¶21).
- AI Capital: since about Aug 2025, with Williams's knowledge; "Investment Manager and Strategic Advisor"; "Trades – BH (2025.09.04)" covering July 16–Aug 4, 2024 ("about three weeks" is acceptable at 19 days); $75M claimed with no investor money received (¶22–23). Nothing implies AI Capital took money.
- Oct 12 draft ("15-25 business days", previously "10-15"); Oct 19 GP email quotes; Nov 13 "third-party identity validator"; "dissipated most investor assets" (¶24–26).
- UC-1 emailed Oct 6 and got the Oct 20 reply "[w]e are accepting new investors at the moment"; the Nov 6 "If you sent a contribution recently..." quote (¶27). "Twelve days later" (Nov 6 to Nov 18) is correct. "Five days later" in short3 (Nov 13 to Nov 18) is correct arithmetic once #34 adds the date.
- Charges and maximums (20/20/5 years); the judge determines any sentence; "merely accusations... presumed innocent" is verbatim; fbi.gov/backwardhatinvestors; the HSI NY / FBI Indianapolis / IRS-CI Chicago offices; the Kuszynski quote is verbatim (PR).
- Sworn Nov 17, 2026 by HSI SA Robert Fanesi before Magistrate Judge Gary Stein; sealed complaint (C p.1, p.9).
- WRTV (John Herrick, Nov 18, 2026): "The Securities and Exchange Commission and Commodity Futures Trading Commission have also filed civil actions against Williams and Johnson." The script correctly says only that actions were filed and describes none of their content.
- Minkow post (One Minute On Fraud, Nov 18, 2026): the July 2026 report and the request "Do not discuss this case publicly", which came "through my lawyers", are confirmed. The quote card's "describing a request relayed by his lawyers" is correct.
- "BREAKING" is acceptable: the arrests and unsealing were on Nov 18, 2026, and today is Nov 19, 2026. "CHARGED" stamps are correct. Short titles 1 and 3 and their hook labels ("PROSECUTORS ALLEGE", "PER THE COMPLAINT") are attributed. Thumbnail B ("RETURNS PICKED BY TEXT / FEDS ALLEGE", "$600M / CHARGED") is acceptable.
- Presumption of innocence is clear in the long video ([5], [64]) and in every Short's closing card. The first_comment quote is verbatim and attributed. The YouTube tags "ponzi scheme" and "600 million ponzi scheme" follow the DOJ press-release headline wording.
- Spoken and subtitle numbers match everywhere except #13, which is fixed above.
- Doc-card quoted titles appear on their documents (spot-checked against the paragraph and page mapping), except #18.

Advisory (not counted): Barry Minkow is introduced only as "one fraud investigator". He is a twice-convicted fraudster turned fraud investigator. Consider adding "a former fraudster turned fraud investigator" so viewers can weigh his account.

FIX count: 43
