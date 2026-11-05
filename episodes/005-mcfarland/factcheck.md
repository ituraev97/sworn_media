# Fact-check: SWORN Case 005, U.S. v. William McFarland

I am an independent checker and did not write the script. Every spoken line (`say`), subtitle (`show`) and on-screen text field was checked against the primary documents, not against the author's notes:

- Court texts in /home/claude/research/mcf/txt and /ocr. Dkt 98 was re-OCR'd from p98-1.png.
- The two SDNY releases, SEC release 2018-141 and the SEC complaint ¶44–46, the KSAT/WPLG story, NPR/KPBS and Fortune, all fetched with WebFetch.

Page numbers for the memo (Dkt 63) are PDF pages ("Page X of 37"). Transcript citations are page:line.

Legend: **OK** = verified. **FIX** = a real discrepancy, with a replacement. **NOTE** = minor or stylistic, no change required.

---

## episode.json

- **[0] OK.** Memo p.5: "only 60 bookings … confirmed and paid … totaled only $57,443". The words match the digits.
- **[1] OK.** Memo p.6: "$1.459 million … for the month of January 2017" vs "$34.79 million". The bar labels and displays are correct.
- **[2] OK.** Memo p.5 quotes "[S]prinkle in a couple of higher offer amounts". The cite correctly says "As quoted in…", and "FEBRUARY 2017" is correct.
- **[3] OK.**
  - Plea Tr. 2:19–20: "how old are you?" / "26."
  - Memo p.11: pretrial release ran Jul 1, 2017 to Jun 12, 2018, and NYC VIP Access ran from late 2017, so it was on bail.
- **[4] OK.** Title card.
- **[5] OK.** Chapter card.
- **[6] OK.** Memo p.18: founded 2013, club for millennials, "black metal credit card", "approximately $3 million from at least 24 investors", and inflated membership (p.18–19).
- **[7] OK.**
  - Complaint ¶3: "In 2016 … bid for artist and celebrity bookings".
  - S1 Information (Dkt 30, OCR): "COUNT ONE (Wire Fraud)".
- **[8] OK.** Memo p.26 quotes this verbatim: "400 of the biggest names in music, sports, and entertainment." (Ex. B email). The "As quoted in" cite is correct.
- **[9] FIX: attribution of a quoted email.**
  - **Problem:** "$2.5mm in accepted offers!" is verbatim (memo p.26, Ex. C, an email from McFarland to an investor) and $11,100 is correct (memo p.27). But this is a stat card with no memo image on screen, and its `src` names only the memo. Under the channel rule, an email quoted through the memo needs "As quoted in".
  - **Replace `scene.src` with:** `McFarland email, Aug 1, 2016, as quoted in the Government's Sentencing Memorandum, S.D.N.Y. 17 Cr. 600, Oct 3, 2018`
- **[10] OK.** Memo p.5:
  - The PPM was "widely distributed … in early 2017" and claimed "thousands of offers representing tens of millions of dollars …".
  - Real estate "worth approximately $8 million".
  - "never acquired any real estate in the Bahamas."
- **[11] OK.** Chapter card.
- **[12] OK.** Memo p.4: Dec 2016 PowerPoint, "on track to achieve $160M [in] completed bookings by Q4 2017".
- **[13] OK.** Memo p.4: "A few days later", an email drafted by the Chief Revenue Officer. The changes were $50M→$150M and 200→1,200.
- **[14] FIX: date in the kicker.**
  - **Problem:** Memo p.5 says McFarland gave the contractor the real report on Feb 2, 2017, and the instructions came "Shortly thereafter". The card is titled "The instructions" but its kicker dates them "FEBRUARY 2, 2017". The memo does not date the instructions to Feb 2. The `say`/`show` text ("In February 2017") is correct.
  - **Replace `scene.kicker` with:** `FEBRUARY 2017`
- **[15] OK.** Memo p.6:
  - Offeror accounts "(which, in fact, did not exist)" and "arbitrarily selected venues".
  - April 2017: "continue the trend" → "yes let's increase them".
  - $1.459M → $34.79M.
  - NOTE: the email quote is shown with the memo page on screen. Optionally add "as quoted in" to the `src`.
- **[16] OK.** Complaint ¶6(e): on Apr 24, 2017 the investor asked for "the latest on bookings". McFarland replied "$44 for march and April will be just under $50 !", which the investor understood as $44M / $50M. The complaint was sworn by FBI SA Racz on Jun 30, 2017.
- **[17] OK.**
  - Memo p.8: "$2.56 million" vs "$1,499", so it would "appear that McFarland could personally guarantee the investment".
  - SEC complaint ¶44: "fake brokerage statement … $1,499 worth of Facebook shares".
- **[18] OK.** Memo p.9: "approximately $40 million", Saddleback Media, "had not sold Magnises", and a fake retainer agreement with the "electronic signature of Saddleback Media's purported President, a certain 'G. Smythe,' an individual who does not exist."
- **[19] OK.** Chapter card.
- **[20] FIX: timeline event text.**
  - **What checks out:**
    - Announced Dec 12, 2016 (memo p.26).
    - Two weekends in the Bahamas (memo p.2).
    - "In an attempt to promote the digital application, I conceived and launched the idea for a music festival" (Plea Tr. 12:7–9).
    - Complaint filed Jun 30, 2017.
  - **Problem:** `events[1].text` reads "First weekend begins, Exuma". The weekend never began. WPLG/KSAT (Apr 28, 2017) says it was "Scheduled to take place over two weekends beginning Friday" and that organizers "canceled the event on Friday morning". Line [23] itself correctly says "was set to begin".
  - **Replace `scene.events[1].text` with:** `First weekend set to begin, Exuma`
- **[21] OK.** Memo p.7: overstated receivables; told investors top musicians would perform "when, in fact, no such agreements were ever reached"; payouts from cancellation insurance when "no event cancellation insurance policies had been executed".
- **[22] OK.**
  - Memo p.10: Vendor-1 paid $2M for "advance tickets for future Festivals" in about April 2017, and was given a "fraudulent income statement".
  - Plea Tr. 12:22–13:2: the false information was given before the guaranty.
- **[23] FIX: overstatement.**
  - **Problem:** Memo p.7–8 says "Patrons, **some of which** paid thousands of dollars for admission, were disappointed to find that the luxury villas and gourmet meals they were promised were limited to tents and prepackaged meals." The script says all patrons "had paid thousands". The rest checks out: the KSAT schedule, Friday Apr 28, Exuma, and the cancellation.
  - **Replace `say` with:** "The first weekend was set to begin on Friday, April twenty-eighth, on Exuma. Patrons, some of whom had paid thousands of dollars, found that the luxury villas and gourmet meals were tents and prepackaged meals. The festival was canceled."
  - **Replace `show` with:** "The first weekend was set to begin on Friday, April 28, on Exuma. Patrons, some of whom had paid thousands of dollars, found that the luxury villas and gourmet meals were tents and prepackaged meals. The festival was canceled."
- **[24] OK.** Memo p.8: "When the Festival was canceled, these investors lost their investments in full." Memo p.10: "at least eighty victim-investors, totaling more than $24 million". NOTE: in the memo, "these investors" refers to the Fyre Festival LLC investors in that paragraph. The script's reading is reasonable.
- **[25] OK.** Complaint sworn Jun 30, 2017 by FBI SA Racz, one count of wire fraud (18 U.S.C. § 1343). Memo p.11: pretrial release from Jul 1, 2017.
- **[26] OK.** Chapter card.
- **[27] OK.** Plea Tr. 12:14–15 has the quote verbatim: "I lied to investors about various aspects of Fyre Media and my personal finances." He pleaded to two wire fraud counts on Mar 6, 2018 (memo p.2–3).
- **[28] OK.** Memo p.11: "late 2017 … March 2018", while on pretrial release. The memo lists the 2018 Met Gala, Burning Man 2018, Coachella 2018, the 2018 Grammy Awards and Super Bowl LII, "when, in fact, no such tickets existed". The Oct 11, 2018 SDNY release lists the same events.
- **[29] OK.** Memo p.13: on Dec 17, 2017 an email went from the Employee-1 account with the subject "2018 MET GALA – Red Carpet & Gala Tickets". The quoted sentence is verbatim, and the price was $2,500 per ticket. NOTE: the email text appears on the memo page shown. Optionally add "as quoted in" to the `src`.
- **[30] OK.** Memo p.16: "Later, McFarland truthfully admitted to creating a fake email purporting to be from the Gala Host". Memo p.14: "None of the victim customers … were on the guest list".
- **[31] OK.**
  - Memo p.11–12: Employee-1 and Fake Employee email accounts. Proceeds went to Employee-1's account, the Driver's account and other employees' accounts, and came back "in cash". "at least thirty victim-customers … at least approximately $150,000".
  - Oct 11 release: at least 30 customers, about $150,000, targeting "attendees of the Fyre Festival".
  - NOTE: the account details come from the memo. Optionally add the memo to the `src`.
- **[32] OK.** Memo p.15 and the Oct 11 release: about March 2018, a forged check for $25,000 on Employee-1's account, given to the Driver.
- **[33] OK.**
  - Memo p.11: pretrial release ended Jun 12, 2018. The Jun 12, 2018 release says he was charged by complaint.
  - Dkt 42 (Jun 18, 2018) has the quote verbatim: "the Court should revoke the defendant's bail".
  - Dkt 43 minute entry, Jun 18: "Bail revoked."
- **[34] OK.**
  - Jun 20 is two days after Jun 18. Memo p.16: a voluntary in-person proffer, represented by counsel. July 26 plea Tr. (Dkt 57): an FBI agent. One false statement was that Employee-1 authorized the $25,000 check.
  - Jul 26 pleas (Dkt 79 ¶7): wire fraud while on pretrial release, bank fraud while on pretrial release, and false statements.
  - The timeline is correct.
- **[35] OK.** Chapter card.
- **[36] OK.** Memo p.2/p.23: 188 to 235 months. Memo p.24 has "the consummate con artist" verbatim.
- **[37] OK.** Memo p.24: "Whenever one scheme began to falter, he hatched a newer and more elaborate one."
- **[38] OK.**
  - Memo p.23 lists the defense arguments: "flawed business plan", "young age and untreated mental illness".
  - Sent. Tr. 27:22–24 has the quote verbatim: "I know that I betrayed the trust of my investors, customers, my family, and even the Court."
- **[39] OK.**
  - Sent. Tr. 52:18: "this was not a good idea gone bad."
  - Sent. Tr. 53:3–6: "While the defendant was soliciting investments for the festival, he decided to upgrade his $8,000-a-month apartment to a three-bedroom penthouse which cost $21,000 a month."
  - Memo p.28: early 2017.
- **[40] OK.** Sent. Tr. 51:9–12 has the quote verbatim. It is said in reply to the defense argument about his lying in the proffer. Dkt 57 confirms the agent was FBI.
- **[41] OK.** Sent. Tr. 55:10–11 has the quote verbatim.
- **[42] OK.**
  - Judgment p.3: "72 months, consisting of 60 months … 12 months for Count S2: 1, consecutive".
  - Sent. Tr. 56:7–8: "one consecutive year on the 3147 counts".
  - Sent. Tr. 56:16–17: three years of supervised release.
- **[43] OK.** Sent. Tr. 56:18 and Judgment: $26,191,306.28, which rounds to $26.19M.
- **[44] OK.** Chapter card.
- **[45] OK.** SEC release 2018-141 (Jul 24, 2018): "at least $27.4 million from more than 100 investors". McFarland admitted the allegations and accepted a permanent officer-and-director bar.
- **[46] OK.** Dkt 79 ¶2:
  - (a) "Two large boxes containing Fyre-branded t-shirts, sweatshirts, shorts and other clothing items that were intended for sale at the Fyre Festival".
  - (b) funds in a Fyre Festival, L.L.C. account at First Western Trust.
  - (c) "Approximately $240,000 … in the name of William McFarland" at Hughes Hubbard and Reed, a law firm.
  - The declaration is dated Jan 10, 2019.
- **[47] OK.** Dkt 96 p.19: a USB pen, "it is used for recording", "segregated from the general population for 40 days, lost 40 days of good conduct time".
- **[48] FIX (two problems).**
  - **What checks out:**
    - The motion was filed Apr 14, 2020 (Dkt 91), and the government opposed it on Apr 28, 2020 (Dkt 96).
    - Dkt 98 (May 11, 2020): the petition was withdrawn "after Mr. McFarland's petition for compassionate release was ripe", an "existing full draft of an opinion" existed, and "this obvious effort to avoid a negative result cannot go without comment."
  - **(a) Wrong attribution.**
    - **Problem:** The sentence before is about "his lawyer", so "She wrote that…" reads as if the lawyer wrote it. The lawyer was Robert J. Hantman (Dkt 97), and the words are the judge's.
    - **Replace the last sentence of `say` with:** "The judge wrote that this obvious effort to avoid a negative result could not go without comment."
    - **Replace the last sentence of `show` with:** `The judge wrote that this "obvious effort to avoid a negative result" could not go without comment.`
  - **(b) Title quote not verbatim.**
    - **Problem:** `scene.title` “an obvious effort” is shown in quotation marks, but the letter says "this obvious effort".
    - **Replace `scene.title` with:** `“this obvious effort to avoid a negative result”`, or the shorter `“this obvious effort”`.
- **[49] OK.** NPR/KPBS, Apr 24, 2025: "released two years early in 2022"; ticket holders "settled for $2 million" in 2021. The timeline entries match NPR and Fortune.
- **[50] OK.** NPR: tickets went on sale in February 2025, "Ticket prices started at $1,400", the event was set for Isla Mujeres and then Playa del Carmen, Mexico, and it was postponed about a week before Apr 24. NOTE: the officials did not literally say they "knew nothing". Isla Mujeres said "For us, this is an event that does not exist", and Playa del Carmen said "There will be no event called 'Fyre 2'". "Local officials said the event would not take place there" would be closer.
- **[51] OK.** Fortune, Jul 16, 2025: the IP sold on eBay on Jul 15, 2025 for $245,300. NPR: "still owes $26 million in restitution".
- **[52] OK.** Closing card, numbers as above. NOTE: it sets a count of bookings over a year against a dollar figure of fabricated offers for one month. That is rhetorical but not false. See also the meta/short1 titles.
- **[53] OK.** Paraphrases Sent. Tr. 55:11. "read the paper, not the pitch" is editorial.
- **[54] OK.** End card.

## short1.json
- **title / hook OK.** Same NOTE as episode [52]: the $34.79M was fabricated *offers* for January 2017, not bookings.
- **[0] OK.** Memo p.5.
- **[1] OK.** $57,443, May 2016 to April 2017.
- **[2] OK.** Memo p.5, February 2017.
- **[3] OK.** The quote is verbatim, and the "As quoted in" cite is correct.
- **[4] OK.** Memo p.6: $1.459M rounds to about $1.46M, against $34.79M.
- **[5] OK.** He did plead to wire fraud and got six years. The verdict date of Oct 11, 2018 is correct. NOTE: the six years also covers bank fraud and false statements.
- **[6] OK.** End card.

## short2.json
- **title / hook OK.** $2.56M vs $1,499 (memo p.8; SEC ¶44).
- **[0] OK.**
- **[1] OK.** Memo p.8.
- **[2] OK.** Memo p.8: "a snapshot of an email purporting to be from a Bank-1 banker … approving a $3 million dollar loan … Not only had Banker-1 not sent that email". NOTE: "An email, supposedly from a banker, approving…" would be more precise.
- **[3] FIX: unsupported and contradicted detail.**
  - **Problem:** "the sale of his first company, Magnises". Nothing in the record calls Magnises his first company. The memo itself (p.25 n.4) records McFarland at Spling from 2011 to 2015, before Magnises in 2013. The $40M sale and Saddleback figures are correct (memo p.9).
  - **Replace `say` with:** "And the sale of his earlier company, Magnises, for about forty million dollars, to Saddleback Media. There was no sale."
  - **Replace `show` with:** "And the sale of his earlier company, Magnises, for about $40 million, to Saddleback Media. There was no sale."
- **[4] OK.** Memo p.9: "G. Smythe", "an individual who does not exist".
- **[5] OK.** SEC 2018-141, Jul 24, 2018: he admitted the allegations.
- **[6] OK.** End card.

## short3.json
- **title / hook OK.**
- **[0] OK.** Dec 12, 2016 (memo p.26); two weekends in the Bahamas.
- **[1] OK.** Memo p.5.
- **[2] OK.** Memo p.7.
- **[3] OK.** Memo p.7: "no such agreements were ever reached".
- **[4] OK.** Memo p.7–8 and KSAT. It does not claim that all patrons paid thousands.
- **[5] OK.** Memo p.10.
- **[6] OK.** End card.

## short4.json
- **title / hook OK.** Memo p.11–14.
- **[0] OK.** Complaint Jun 30, 2017; released Jul 1, 2017.
- **[1] OK.** Memo p.11 and the Oct 11 release.
- **[2] OK.** Memo p.13.
- **[3] OK.** Memo p.13–14 and p.16.
- **[4] OK.** Oct 11 release: Fyre Festival attendees; at least 30 customers; about $150,000.
- **[5] FIX: chronology.**
  - **Problem:** "His bail was revoked. The judge called him unique in the court's memory." This makes it sound as if the remark came at the bail revocation (Jun 18, 2018). It was made at sentencing on Oct 11, 2018 (Sent. Tr. 51:2), as the cite says. The quote is verbatim.
  - **Replace `say` with:** "His bail was revoked. At sentencing, the judge called him unique in the court's memory."
- **[6] OK.** End card.

## short5.json
- **title / hook OK.** Sent. Tr. 55:11, verbatim fragment.
- **[0] OK.** Five counts: two in S1 and three in S2. Sentencing was Oct 11, 2018.
- **[1] OK.** Sent. Tr. 51:23–52:1 ("well-intentioned enthusiastic young man") and memo p.23 ("flawed business plan"). Sent. Tr. 52:18 has the quote verbatim.
- **[2] FIX: misstated figure.**
  - **Problem:** "an eight thousand dollar apartment" / "an $8,000 apartment". The rent was $8,000 *a month*. Sent. Tr. 53:5: "$8,000-a-month apartment"; memo p.28: "approximately $8,000 in monthly rent".
  - **Replace `say` with:** "While raising money for the festival, she noted, he moved from an eight thousand dollar a month apartment to a twenty-one thousand dollar a month penthouse."
  - **Replace `show` with:** "While raising money for the festival, she noted, he moved from an $8,000-a-month apartment to a $21,000-a-month penthouse."
- **[3] FIX: chronology, bail vs. custody.**
  - **Problem:** "He had also lied to a federal agent while on bail." The false statements were made at the Jun 20, 2018 proffer (memo p.16). By then his pretrial release had ended (Jun 12, 2018, memo p.11) and his bail had been revoked (Jun 18, Dkt 43). The judge did group the lying with his on-release crimes (Sent. Tr. 55:21–23), but the dates show he was not on bail when he lied. The quote is verbatim (Sent. Tr. 51:12).
  - **Replace `say` with:** "After his second arrest, he had also lied to a federal agent. The judge's words: white-collar obstruction."
- **[4] OK.** Sent. Tr. 55:10–11, verbatim.
- **[5] OK.** Six years; $26,191,306.28.
- **[6] OK.** End card.

## short6.json
- **title / hook OK.** Fortune: $245,300.
- **[0] OK.** Oct 11 release. NOTE: "$26.19M forfeited" means *ordered* forfeited. "$26.19M forfeiture" would be more precise.
- **[1] OK.** Dkt 79 ¶2(a).
- **[2] OK.** Dkt 96 p.19.
- **[3] OK.** NPR: released in 2022; postponed in April 2025.
- **[4] OK.** Fortune.
- **[5] OK.** NPR: $26 million in restitution.
- **[6] OK.** End card.

## meta.json
- **title OK.** Same NOTE as episode [52].
- **summary OK.**
  - 60 bookings and $57,443 (memo p.5).
  - "tens of millions" (PPM).
  - "serial fraudster" is verbatim from the judge (Sent. Tr. 55:10).
  - Six years.
- **tags / sources OK.** The URLs match sources.md.

## thumb.json
- **A OK.** "FAKE NUMBERS"; "60 BOOKINGS · $34.79M". Same NOTE as [52].
- **C OK.** "6 YEARS", "FYRE FESTIVAL FRAUD", "SENTENCED".

## Privacy check
No private victim, employee, driver or contractor is named in any file. The pseudonym "Vendor-1" is fine. The SEC release names the contractor, but the script does not.

---

## Summary
**10 FIX items:**
1. episode [9]: the `src` for the quoted email needs "as quoted in".
2. episode [14]: the kicker "FEBRUARY 2, 2017" should be "FEBRUARY 2017"; the instructions came "shortly thereafter".
3. episode [20]: the timeline says "First weekend begins"; it should be "set to begin", because the festival was canceled Friday morning.
4. episode [23]: "Patrons who had paid thousands" should be "some of whom".
5. episode [48]: "She wrote" reads as the lawyer; change to "The judge wrote".
6. episode [48]: the title “an obvious effort” is not verbatim; the letter says "this obvious effort".
7. short2 [3]: "his first company, Magnises" is unsupported; change to "his earlier company".
8. short4 [5]: the "unique" remark was made at sentencing, not at the bail revocation; add "At sentencing".
9. short5 [2]: "$8,000 apartment" should be "$8,000-a-month".
10. short5 [3]: he did not lie to the agent "while on bail"; the proffer was Jun 20, 2018, after release ended Jun 12 and bail was revoked Jun 18.

## Fixes applied (2026-11-05, before the final build)
All 10 FIX items were applied in make_spec.py / make_shorts.py and the json regenerated: [9] src now "McFarland email, Aug 1, 2016, as quoted in the Government's Sentencing Memorandum"; [14] kicker "FEBRUARY 2017"; [20] "First weekend set to begin, Exuma"; [23] "Patrons, some of whom had paid thousands of dollars"; [48] "The judge wrote…" and title "“this obvious effort”"; short2 [3] "his earlier company"; short4 [5] "At sentencing, the judge called him…"; short5 [2] "$8,000-a-month apartment"; short5 [3] "After his second arrest, he had also lied to a federal agent."
NOTEs acted on: the "60 bookings vs $34.79M" framing was replaced everywhere (episode closing card, meta title, short1 title/hook, thumb A hook) with the like-for-like January 2017 comparison "$1.46M real / $34.79M on paper" (memo p.6); episode [50] now "Local officials denied it." (NPR); short6 "$26.19M forfeiture".
