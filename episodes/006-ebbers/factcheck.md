# Fact-check — Episode 006 (Ebbers / WorldCom)

Checker: independent pass, 2026-11-06. JSON and py files were not edited.

**Source abbreviations**
- **OPP** = U.S. Brief in Opposition, No. 06-590 (opp_l.txt), printed pp. 1–6, 24
- **CA2** = 2d Cir. opinion, Pet. App. 1a–41a (pet.txt ~l.1990–3690)
- **SDNY** = Jones order of Jul 9, 2005, Pet. App. 42a+ (pet.txt l.3696+)
- **CFTF** = DOJ CFTF First Year Report, pp. 2.4–2.5 and 3.26
- **GOV19** = Gov't letter of Oct 4, 2019 (Dkt. 354), pp. 1–11
- **TR** = sentencing transcript of Jul 13, 2005 (Dkt. 354 Ex. B). Pages 58–62 (PDF pp. 72–76) are missing from transcript_2005_ocr.txt, so I re-OCR'd them from sdny_1216821.pdf.
- **AG** = AG remarks of Mar 2, 2004 (ag.htm; ag_remarks_2004.txt is empty)
- **SECC** = SEC complaint, ¶¶1, 7
- **SECPR** = SEC press release 2002-94
- **HFSC** = House hearing of Jul 8, 2002
- **TIME** = "The Night Detective"
- **AP-BK** = LJWorld, Jul 22, 2002
- **AP-V** = SE Missourian, Mar 16, 2005
- **AP-S** = SE Missourian, Aug 12, 2005
- **AP-P** = CBS, Sep 26, 2006
- **AP-SC** = Fox, Mar 5, 2007
- **WLBT** = WDAM family statement
- **VLEX** = 432 F. Supp. 3d 421

I fetched every web source with WebFetch, and each fetch succeeded. Nothing is UNVERIFIED.

## Long episode (episode.json)

| # | Verdict | Source | Note / fix |
|---|---|---|---|
| 0 | OK | OPP 4–5 ("As to one critical report on expenses, petitioner admitted that he received it but stated that, in 2001, he began throwing it in the trash without reading it"); highlight matches | SDNY 54a has "probably put the reports 'in the trash'", but the "PER THE GOVERNMENT" kicker covers it |
| 1 | OK | OPP 6 (instruction text); highlight matches | |
| 2 | OK | CFTF 2.5 ("the largest accounting fraud in U.S. history"); OPP 3 | |
| 3–5 | OK | CA2 | |
| 6 | OK | CA2 3a | |
| 7 | OK | OPP 2; SDNY 43a; highlight matches | |
| 8 | OK | OPP 2 (dot-com bubble burst; Q3 2000 "almost $1 billion higher than expected") | |
| 9 | **FIX** | CA2 4a–5a | See F1 |
| 10 | OK | CA2 5a; highlight matches | |
| 11 | OK | CA2 5a, verbatim "[W]e have to hit our numbers."; cite is "As quoted in" | |
| 12 | OK | — | |
| 13 | **FIX** (minor) | CA2 5a–6a; OPP 2–3 | See F2 |
| 14 | OK | CA2 6a; highlight matches | |
| 15 | **FIX** | CA2 7a; SDNY 52a | See F3 |
| 16 | OK | CA2 7a–8a; SDNY 45a–46a; OPP 3; highlight matches | |
| 17 | OK | CA2 8a; highlight matches | |
| 18 | OK | CA2 8a; highlight matches | |
| 19 | OK | CA2 9a ("lifeblood was in the stock of the company"; "about $12 per share") | |
| 20 | OK | CA2 8a–9a; highlight matches | |
| 21 | OK | CA2 7a–11a: 771 / >610 / >700 / >941 / ~818. These sum to $3.84B, consistent with OPP's ~$3.8B. SDNY 56a gives $742M for Q3, which is still ">700". | |
| 22 | OK | CA2 11a; OPP 3; highlight matches | |
| 23 | OK | — | |
| 24 | **FIX** (minor) | CA2 12a | See F4 |
| 25 | OK | CA2 12a; TIME ("late May … working late into the night, keeping their project secret") | |
| 26 | OK | TIME | TIME sources the delay request to "a WorldCom timeline of events filed with the SEC"; "According to TIME" is adequate |
| 27 | OK | CA2 12a; highlight matches | |
| 28 | OK | CFTF 3.26 ("Within 24 hours … more than $3.8 billion"); SECC ¶1 ($3.055B 2001; $797M Q1 2002) and ¶7 (loss of ~$662M) | |
| 29 | OK | SECPR, verbatim | |
| 30 | OK | HFSC: quote verbatim; Ebbers declined "on the basis of my fifth amendment privilege"; date Jul 8, 2002 | |
| 31 | OK | AP-BK (filed "Sunday night", i.e. Jul 21, 2002; $107B in assets; "largest bankruptcy in U.S. history") | |
| 32 | OK | CFTF 2.5; highlight matches | |
| 33 | OK | — | |
| 34 | OK | CFTF 2.4; AG; CA2 12a; GOV19 1–2 | Note: SDNY 43a says the trial "began on January 25, 2005", while GOV19 says Jan 24. The timeline follows its cited source (GOV19), so this is acceptable. Optional change: drop the day ("JAN 2005"). |
| 35 | OK | OPP 4; AP-V ("Only Sullivan directly implicated Ebbers.") | |
| 36 | OK | OPP 4 | |
| 37 | OK | SDNY 51a–52a (Tr. 4044) | |
| 38 | **FIX** | CA2 29a–30a; highlight matches | See F5 |
| 39 | OK | OPP 6 | |
| 40 | OK | CA2 12a; SDNY 43a; AP-V ("eight days", "all nine counts") | |
| 41 | OK | — | |
| 42 | OK | GOV19 3 (TR 31:3-6; offense level 42, range 30 years to life) | |
| 43 | OK | GOV19 3 (TR 36:23–37:13); highlight matches | |
| 44 | OK | TR 60:1-6, re-OCR'd: the quote is verbatim, and "age, his serious heart condition" is also on 60:1-3 | |
| 45 | OK | TR 61; GOV19 2 (age 63), 4 n.3 | |
| 46 | **FIX** | CA2 38a–39a; AP-S | See F6 |
| 47 | **FIX** (visual) | CA2 39a | See F7 |
| 48 | OK | — | |
| 49 | OK | CA2 39a–41a, quotes verbatim; highlight matches | |
| 50 | OK | AP-P (Sep 26, 2006; Oakdale; drove himself); AP-SC; GOV19 4 ("Good Conduct Release date is July 4, 2028"); highlight matches | |
| 51 | **FIX** (minor) | CFTF 2.4, 3.26 | See F8 |
| 52 | OK | GOV19 5–6; highlight matches | The bracket substitution in the quote is allowed |
| 53 | OK | GOV19 1, 4, 10 | The highlight is only the letter's opening, which is fine for the title "The government opposes" |
| 54 | OK | VLEX (motion Sep 5, 2019; granted Dec 18, 2019); WLBT (released Dec 21, 2019; died Feb 2, 2020, age 78) | |
| 55–57 | OK | SDNY 51a–52a | |

### F1 — long #9 (say/show)
**Problem:** "WorldCom took on the liability for his bank debts" is accurate but incomplete. CA2 5a adds that Ebbers then had to make the payments to WorldCom, still secured by his stock. Without that, viewers can hear it as WorldCom paying off his debts.

**Replacement (say):**
> "…and in October two thousand, WorldCom took on the liability for his bank debts. He now owed that money to WorldCom instead."

The show text should match, with digits.

### F2 — long #13 (say/show)
**Problem:** "The first fix came from reserves." The first fix in Q3 2000 was actually the $133M revenue adjustment (CA2 5a). The reserves were the first *line-cost* fix (OPP 2–3), and the entries were made on Sullivan's instruction.

**Replacement (say):**
> "The first line-cost fix came from reserves. On Sullivan's instructions, Controller David Myers and his staff reduced line-cost accounts and drew down reserves by the same amounts. Reported line costs fell by about eight hundred twenty-eight million dollars."

The show text should match.

### F3 — long #15 (say/show and stat label)
**Problem:** Chronology. The 78% figure is for **September 2000**, which falls in Q3 and reflects the $828M entries. The narration places it after "The next quarter… $797 million", which implies the Q4 entries produced it. CA2 also calls it an *apparent* gross margin; the December 2000 figure was 74%.

**Replacement (say):**
> "The next quarter, the staff cut the income tax reserve by four hundred seven million dollars and altered other accounts, until reported line costs were seven hundred ninety-seven million dollars lower. The monthly reports sent to Ebbers carried the reduced line costs: an apparent gross margin of seventy-eight percent in September two thousand, and seventy-four percent in December. WorldCom had never achieved margins like that."

**Show:** the same text with $407 million, $797 million, 78% and 74%.

**Stat label:** "apparent gross margin, Sept. 2000 report —|never achieved by WorldCom before"

### F4 — long #24 (say/show)
**Problem:** CA2 12a says the board asked at the end of April and he resigned **on April 29**. The narration says the board asked on April 29.

**Replacement (say):**
> "In March two thousand two, the S.E.C. began to investigate WorldCom. At the end of April, the board asked Ebbers to resign. He did, on April twenty-ninth. In May, he bought three million more shares of WorldCom stock."

The show text should match.

### F5 — long #38 (say vs. show mismatch)
**Problem:** The show text quotes CA2 verbatim ("using a procedure for … including the 10-Ks …"). The say text drops "using a procedure for" and changes "10-Ks" to "annual reports", so the subtitle does not match the speech.

**Replacement (say):**
> "The appeals court later summed up his own testimony: using a procedure for signing documents he didn't bother to read in full, including the ten-Ks, and tossing the management budget variance report in the trash without reading it."

Keep the show text as it is.

### F6 — long #46 (bars kicker)
**Problem:** The kicker "THE OTHER SENTENCES" sits over a chart that includes EBBERS (300), which is misleading. The chart also omits Normand (probation, 0 months), although the narration mentions him.

**Replacement kicker:** "THE SENTENCES · PER THE APPEALS COURT"

**Optional:** add the item `{"label":"ACCOUNTANT 2","value":0,"display":"0 · probation"}`.

The values themselves are correct: 60, 12+, 12+, 5, 300 (CA2 38a–39a).

### F7 — long #47 (doc image and highlight)
**Problem:** The narration ("All of them cooperated and pleaded guilty. Ebbers did not. And each was his subordinate.") is not on img/ca2_codef.jpg. That crop ends mid-list at "Betty Vinson, who received five", and its highlight covers "CFO Scott Sullivan, who received five years; Controller David Myers". The quoted passage is on CA2 page 39a.

**Fix (preferred):** make a new crop of 39a with the highlight on:
> "All of those named above cooperated and pled guilty. Ebbers did not. Moreover, each was a subordinate of Ebbers."

**Fix (alternative):** change line 47 to a big-text scene with no image: lines "They pleaded guilty.", "He|didn't.", kicker "THE APPEALS COURT".

(Short5 #1 uses the same image correctly, because its narration is about the sentences.)

### F8 — long #51 (say/show and stat label)
**Problem:** CFTF (Jul 2003) says the $2.25B penalty "shall be deemed to be satisfied" by $500M in cash plus $250M in stock *if* a reorganization plan is confirmed, and that it remained subject to bankruptcy-court approval. The narration states the satisfaction as an accomplished fact, which the cited source does not show.

**Replacement (say):**
> "WorldCom itself had settled with the S.E.C.: a civil penalty of two point two five billion dollars, to be satisfied in bankruptcy with seven hundred fifty million dollars in cash and stock for defrauded investors."

**Show:** the same text with $2.25 billion and $750 million.

**Stat label:** "to investors, to satisfy|a $2.25 billion penalty"

## Shorts

**short1** — title and hook OK (CA2 5a).

| # | Verdict | Source | Note / fix |
|---|---|---|---|
| 0 | **FIX** (minor) | OPP 2 | See F9 |
| 1 | OK | CA2 5a | Highlight matches |
| 2 | OK | CA2 5a | Quote verbatim, cite honest |
| 3 | OK | CA2 4a | |
| 4 | OK | OPP 3 | Highlight matches |
| 5–6 | OK | CA2 12a–13a | |

**F9 — short1 #0 (say/show).** "Fall 2000" is imprecise: the source says the *third quarter* of 2000. Also, in CA2 the earnings-warning exchange came before Sullivan learned of the ~$1B line-cost overrun, so opening with the overrun implies the warning was a response to it.

Replacement (say):
> "Third quarter, two thousand. WorldCom can't meet Wall Street's expectations, and its line costs come in almost one billion dollars higher than expected."

The show text should match.

**short2** — title and hook OK (OPP 4–5).

| # | Verdict | Source | Note / fix |
|---|---|---|---|
| 0 | OK | SDNY 45a, 51a | |
| 1 | OK | SDNY 51a–52a | |
| 2 | **FIX** (minor) | OPP 4–5 | See F10 |
| 3 | OK | OPP 6 | |
| 4 | OK | OPP 6 | Verbatim, "As quoted in" |
| 5 | OK | CA2 | |
| 6 | OK | — | |

**F10 — short2 #2 (say/show).** The second sentence presents the trash claim as fact rather than as his testimony.

Replacement (say):
> "At his trial, he said he simply did not notice. And he said that in two thousand one, he began throwing the report in the trash without reading it."

The show text should match, keeping "did not notice" in quotes.

**short3** — title and hook OK (OPP 3).

| # | Verdict | Source | Note / fix |
|---|---|---|---|
| 0 | OK | OPP 2 | |
| 1 | OK | OPP 3 | |
| 2 | OK | CA2 8a | |
| 3 | **FIX** (minor) | CA2 7a–11a | See F11 |
| 4 | OK | CA2 11a | |
| 5 | OK | OPP 3; CA2 13a | |
| 6 | OK | — | |

**F11 — short3 #3 (bars display).** The displays "610", "700" and "941" drop the "more than" that the narration says. Change them to "610+", "700+" and "941+".

**short4** — title and hook OK (TIME; CA2 12a).

| # | Verdict | Source | Note |
|---|---|---|---|
| 0 | OK | CA2 12a | Resigned Apr 29; "May … has just resigned" is fine |
| 1 | OK | CA2 12a; TIME | |
| 2 | OK | TIME | |
| 3 | OK | TIME | |
| 4 | OK | CA2 12a; CFTF 3.26 | |
| 5 | OK | CA2 12a–13a | |
| 6 | OK | — | |

**short5** — title and hook OK (CA2 38a).

| # | Verdict | Source | Note |
|---|---|---|---|
| 0 | OK | AP-S (Judge Jones: "Mr. Sullivan was the architect of the fraud at WorldCom"); CA2 6a | |
| 1 | OK | CA2 38a; AG | Highlight matches |
| 2 | OK | GOV19 3 | |
| 3 | OK | GOV19 3–4 | |
| 4 | OK | CA2 39a ("culpability and cooperation", "subordinate") | Optional wording: "cooperation, and culpability" |
| 5 | OK | CA2 41a | |
| 6 | OK | — | |

**short6**

| # | Verdict | Source | Note / fix |
|---|---|---|---|
| 0 | OK | TR 61 | |
| 1 | **FIX** (minor) | TR 60:3-6 | See F12 |
| 2 | OK | GOV19 4–5 | |
| 3 | OK | GOV19 5 | |
| 4 | OK | VLEX | |
| 5 | OK | WLBT; GOV19 4 | Sep 2006 to Dec 2019 is about 13 years |
| title | OK | GOV19 5 | |
| hook | **FIX** (minor) | TR 61 | See F13 |

**F12 — short6 #1 (say).** The judge said "would not *sufficiently* reflect the seriousness of this crime", and dropping "sufficiently" strengthens her words.

Replacement:
> "She said it was likely to be a life sentence, but that anything less would not sufficiently reflect the seriousness of the crime."

**F13 — short6 hook.** "Sentenced for life?|Then 2019." can read as if he received a life sentence; the sentence was 25 years. Replacement: "Likely a life sentence.|Then 2019."

## meta.json
- **title** — OK (OPP 3).
- **summary** — OK (OPP 4–5; CA2 5a, 12a–13a). SEC LR 19301 is listed but not used in the script, which is harmless.

## Highlight spot-check
I OCR'd all 24 doc-scene highlight crops and viewed 9 of them as images: #0, 10, 14, 28, 32, 38, 47, 50 and 52.
- All match the narration except **long #47** (F7).
- **short6 #1** also checked (gl_jones second band, the "likely to be a life sentence" passage): it matches.

## Summary
- **FIX: 13 items in total.**
  - Long episode, 8: #9, 13, 15, 24, 38, 46, 47, 51.
  - Shorts, 5: s1 #0, s2 #2, s3 #3, s6 #1, s6 hook.
- **UNVERIFIED: 0.**
- All other lines are OK.

## Applied (by the script author, 2026-11-06)
All 13 FIX items applied before the final build: F1–F5, F8 (say/show/labels as recommended); F6 kicker changed to "THE SENTENCES · PER THE APPEALS COURT" and Vinson/Normand bars added (Normand 0 = probation); F7 new crop `img/ca2_why.jpg` (2d Cir. 39a, highlight "All of those named above cooperated and pled guilty. Ebbers did not. Moreover, each was a subordinate of Ebbers."); F9–F13 in make_shorts.py. Note on long #34 also applied (timeline date "JAN 2005").
