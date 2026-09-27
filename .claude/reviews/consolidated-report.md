# Consolidated Report — Phase 3

*Tools, Not Theory* · beta-reader panel · 2026-09-27

**Release status: not cleared.** Reader 4 (clinician) recommends **CONDITIONAL** release, with two blockers and ten conditions. Nothing in the manuscript has been changed. The author reads this report before any edit is made.

**How to read the citations.** R1–R5 are Readers 1–5. "note 7" is a reader's line-level note 7. "Q3" is their answer to targeted question 3. "WLY 2" is item 2 in their "Where it lost you" list. "finding n" is Reader 4's numbered safety finding. "l.175" is line 175 of the reviewed manuscript file (§8).

---

## 1. Release blockers

### Blocker 1 — PHQ-9: nothing happens after the last question. This is the most urgent item in the report.

- **Where:** Chapter 00, Set a Baseline (l.175).
- **The gap:** The book tells readers to take the PHQ-9 on their own, at the start and every two weeks after that. Its last question (item 9) asks about thoughts of being better off dead or of hurting yourself. If a reader answers anything above "not at all", the book says nothing. The questionnaire raises a red flag and the book drops it.
- **Fix (R4 note 8):** "any answer above 'not at all' on the last question means go to Read This First today, whatever the total score."
- **Raised by:** R4 (finding 1, `blocker`; condition 1), R1 (note 7, `safety risk`), R5 (note 5, `safety risk`).
- **Depends on:** nothing. The fix is one sentence pointing to a page that already exists. It is step 1 of the sequence (§9).

### Blocker 2 — Five emergency-number entries are UNVERIFIED. That means unconfirmed, not wrong.

In its session, Reader 4 could not load the official site for any of these. No reader found a number that was wrong.

| Entry | Printed in Read This First | Reader 4 status | Why it wasn't confirmed |
|---|---|---|---|
| US emergency | 911 | UNVERIFIED — NEEDS CHECK | 911.gov and fcc.gov returned 403 |
| Canada emergency | 911 | UNVERIFIED — NEEDS CHECK | crtc.gc.ca returned 403 |
| India emergency (ERSS) | 112 | UNVERIFIED — NEEDS CHECK | 112.gov.in returned 503; mha.gov.in returned 403 |
| Australia emergency (Triple Zero) | 000 | UNVERIFIED — NEEDS CHECK | triplezero.gov.au's redirect target returned 503 |
| UAE police / ambulance | 999 / 998 | UNVERIFIED — NEEDS CHECK | moi.gov.ae returned 503, u.ae returned 404, and dcas.gov.ae did not resolve |

- **A site that won't load is not evidence that a number is wrong.** Don't change these numbers because of this report. Don't publish them on the strength of it either.
- **Required before release:** a person checks every crisis entry by hand on the service's own site, then records the URL and the date in this file. That includes the eight entries Reader 4 marked VERIFIED: 988 (US), 9-8-8 (Canada), Samaritans 116 123 (UK and Ireland), Lifeline 13 11 14, findahelpline.com, EU 112 and UK 999. Reader 4's web tool returns a model's summary of a page, not the page itself, so its VERIFIED still needs the human check the brief requires (see "Web tools" in `phase-0-intake.md`). Reader 4 confirmed Samaritans Ireland on samaritans.org; it did not open samaritans.ie.
- **Supporting evidence gathered while writing this report.** This is **not** the hand check. On 2026-09-27 each page was fetched and its raw text searched for the number. No model summary was involved.

  | Entry | Result | Source |
  |---|---|---|
  | India 112 | Matches | Ministry of Home Affairs, ERSS page (mha.gov.in/en/commoncontent/emergency-response-support-system-erss): "a nationwide, unified emergency response system with a single emergency number '112', for reporting and addressing all kinds of emergencies from across the country". Calls are forwarded to "Police / Health / Fire / …". The page describes a state-by-state system but doesn't list which states are live, so Reader 3's question (note 1) is still open. |
  | UAE 998 (ambulance) | Matches on one service's site | National Ambulance (nationalambulance.ae). The site header reads "Call 999 Police Call 998 Ambulance". Dubai's ambulance-service site (dcas.gov.ae) still did not resolve. |
  | UAE 999 (police) | Listed, but not on a police site | The same National Ambulance header. moi.gov.ae and dubaipolice.gov.ae could not be reached. |
  | US 911, Canada 911, Australia 000 | Not reached | 911.gov, fcc.gov, crtc.gc.ca and triplezero.gov.au (which redirects to infrastructure.gov.au) returned 403. The check confirmed that 911.gov's refusal came from the site itself, not from the review environment's network, so an ordinary browser should be able to open these pages. |

- **The other four readers had no web access.** All four said they could not confirm the numbers: R1 Q3, R2 Q3, R3 Q3 and notes 1–2, R5 Q3. Reader 4's check settles one of their doubts: 988.ca confirms that 988 takes texts in Canada as well as the US (asked by R2 and R5). The check above settles part of another: India 112 (asked by R3 and R5).

---

## 2. Headline verdict

None of the readers objected to the tools themselves. Activation, grading, the thought record, the five-minute rule and the minimum viable day all came through five different readings. Reader 4 found no passage telling a reader to stop or change their care, and no number shown to be wrong.

What fails is support at the points where the book asks the most of the reader:

- **Inside the exercises.** No exercise has a rule to stop if distress rises.
- **At the end of Chapter 09.** All five readers said it leaves them alone.
- **On the crisis page, for anyone outside five countries.** All five readers raised this.
- **In the Safety Plan.** The book's own privacy note says typed entries are wiped (four of five readers).

All five readers rated trust 3 out of 5. Closing the two blockers and meeting the ten conditions in §3 turns Reader 4's CONDITIONAL into a release candidate. Release then depends on the re-check in §9, step 7.

---

## 3. Reader 4's release conditions, verbatim

All ten must be closed before release. Where other readers raised the same issue, they are cross-referenced here. The conditions are not merged.

| # | Condition (Reader 4's words) | Reader 4 finding | Also raised by | Step (§9) |
|---|---|---|---|---|
| 1 | Add PHQ-9 item 9 routing to Chapter 00, Set a Baseline. | Finding 1, `blocker` | R1 note 7; R5 note 5 | 1 |
| 2 | The publisher must verify, against official sources, US 911, Canada 911, India 112, Australia 000 and UAE 999/998, and name the 988 services in the text. | Finding 2, `blocker` (verification); finding 18, `minor` (service names) | **Verification:** R1, R2, R3 and R5 (Q3) could not confirm the numbers. R1 (note 2) and R2 (Q3) ask for a printed check date. R3 (note 1) and R5 (Q3) doubt India 112 in particular. **Service names:** R4 only. | 2 (verify), 3 (names) |
| 3 | Add "if you have already harmed yourself or taken something" to Read This First. | Finding 4, `major` | Related but not the same: R5 note 3. Read This First never names self-harm without suicidal intent, yet Ch 00 and Ch 09 send self-harm there. | 3 |
| 4 | Fix the C4 persistence conflict: warn that digital entries are lost, and tell readers to copy the plan to paper or their own notes app. | Finding 3, `major` | R1 note 1; R2 note 45; R5 note 4 and WLY 7. **In tension with** R3 notes 5 and 18 on privacy in a shared home (Conflict 6). | 3 |
| 5 | Add the sequential-use instruction to C4, and make step 6 prompt for specific means. | Finding 10, `major` (also finding 17, `minor`: prompts for C4 steps 3 and 5) | R4 only. A neighbouring step drew comments from others: R2 note 46 and R5 note 26 on step 7, "One reason worth staying for". | 3 |
| 6 | Reprint the crisis numbers (or the Read This First summary) in Appendix B and Appendix C4. | Finding 5, `major` | R2 notes 38 and 43, and Q3; R1 note 4 (at the least, make Read This First a live link) | 3 |
| 7 | Add exclusions for suicidal or death-related content to Chapter 03 (thought record) and Chapter 07 (go concrete; postponement). | Findings 6 and 7, `major` | Only R4 asks for exclusions. Related: R3 (Q2) and R5 (note 13) want a Ch 03 exit line for when a record opens something larger or makes the thought louder. | 4 |
| 8 | Repeat the bipolar caution in Chapter 02 Stage 3 and Appendix A Week 3. | Finding 8, `major` | R4 only | 4 |
| 9 | Clarify the Triage row "The voice in my head is vicious" and the opening of Chapter 09 to separate the inner critic from hearing voices. | Finding 9, `major` | R4 only. The Ch 09 opening is also the subject of Conflict 1. | 5 |
| 10 | Add a distress stop rule to the exercises in Chapters 03, 05, 07 and 09, and a "do not do this alone" line to Chapter 09 for trauma-linked self-criticism. | Finding 11, `major`; finding 12, `minor` | **Stop rule:** R3 Q2 (Ch 03); R5 Q2 and notes 13 and 15 (Ch 03, Ch 05). For Ch 09 only: R1 Q4 and note 20; R2 Q4 and note 48. **"Do not do this alone":** R4 only. It lands on the passage R5 experienced as rejection (Conflict 1). | 4 (Ch 03, 05, 07); 5 (Ch 09) |

**Reader 4's open items (not conditions), verbatim:** "When Not to Use This" boxes for Chapters 01, 06 and 08; scheduling the Safety Plan in Appendix A; widening the Chapter 03 examples; confirming permission for the Stanley-Brown adaptation.

For Reader 4, widening the Ch 03 examples is only an open item. Across the panel it is a five-reader consensus finding (§4.1 D).

---

## 4. Findings by confidence

Confidence here means how many readers raised a finding independently. None of them saw another's report (§8). Confidence is not severity: five of Reader 4's single-reader findings are release conditions.

### 4.1 Consensus: all five readers. Highest confidence.

| ID | Finding | Where | R1 | R2 | R3 | R4 | R5 |
|---|---|---|---|---|---|---|---|
| A | The cost-table row "It costs the years the protection was supposed to save" reads as a verdict, not a price. **All five labelled it `safety risk`.** | Ch 09, The Tool | note 20 | note 40 | note 6 | note 23 | note 23 |
| B | The chapter ends on "Put it down" with no route to support. The one line that would help ("particularly relevant if Chapter 09 hit hard") is in Appendix D. | Ch 09, close | note 20 | note 48; Q4 | Q4 | note 24 | note 25 |
| C | Worked Example Four works out only because "the underlying accounts have sufficient funds". For a reader who is short of money, the example falls apart. | Ch 03, Example Four | note 15 | note 23 | note 9 | note 14 | note 11 |
| D | All four worked examples are about work, admin or output. None involves another person, family, relationships or caring for someone. | Ch 03 | Q1 | Q1 | Q1 | Q1 | Q1 |
| E | India and the UAE get an emergency number but no talk line. Anyone outside the US, Canada, UK, Ireland and Australia gets only a website. | Read This First | note 3 | Q3 | note 3; WLY 1 | note 4; finding 16 | note 2 |
| F | Every reader said the printed numbers need checking before print. None found one wrong. | Read This First | Q3 | Q3 | Q3 | audit table | Q3 |

All five readers also rated trust 3 out of 5 (§7).

### 4.2 Strong: three or four readers

| ID | Finding | Where | Raised by |
|---|---|---|---|
| G | The Safety Plan gets wiped. The Privacy note says digital fields clear when the book closes, but C4 says "keep it on your phone". | Front matter vs App C4 | R1 note 1; R2 note 45; R4 finding 3; R5 note 4, WLY 7 (4 of 5). R3 raised the opposite risk, privacy (Conflict 6). |
| H | Examples Three and Four drop further than the "10 to 30 points" the chapter calls a good result, and no example shows a record that barely moves. The figures are checked in §6. | Ch 03, "Calibrate your expectations" | R1 note 13; R2 note 22; R4 notes 13–14; R5 WLY 4, note 10 (4 of 5) |
| I | The examples come from a founder's desk life: landing pages, frameworks, apps, "ship". This includes the values examples in Ch 06. | Ch 02, 04, 06 and throughout | R1 note 11; R2 WLY 5–6; R5 verdict, note 17 (3 of 5). R4 raised it for Ch 03 only (Q1). |
| J | No stop rule inside the exercises. The stop lines cover putting the book down, not stopping an exercise that has turned painful. | Ch 03, 05, 07, 09 | R3 Q2; R4 finding 11; R5 Q2, notes 13 and 15 (3 of 5). R1 (Q4) and R2 (Q4) raised the Ch 09 case only. |
| K | "Never miss twice" never says what counts as a miss (R1). It is all-or-nothing (R5), clashes with "put it down whenever you want" (R4), and claims more than the cited study found (R1, R5). | Ch 08, Never Miss Twice | R1 notes 18–19; R4 note 22; R5 note 19 (3 of 5). **R2 praised it** (Conflict 2). |
| L | Ch 05's urge surfing has no way out if the body sensation climbs instead of easing. The three readers gave three different reasons: panic or trauma (R4), an anxiety spiral (R5), and chest pressure that should be checked as a possible heart symptom first (R2). | Ch 05, Urge Surfing | R2 note 28; R4 finding 13, note 18; R5 note 15 (3 of 5) |
| M | The accurate-thought case ("two months behind on rent") gets one line and no next step. | Ch 03, "When not to use this" | R1 note 15; R2 note 24; R3 note 9 (3 of 5) |
| N | The crisis numbers aren't where readers are sent. Appendix B, C4, Ch 09 and the Ch 00 table only say "go to Read This First". | App B, C4, Ch 09, Ch 00 | R2 notes 38 and 43, Q3; R4 finding 5; R1 note 4, who asks at least for a live link (3 of 5) |
| O | The crisis page doesn't say which lines are free, which are open 24 hours, or which take texts. | Read This First | R2 Q3; R4 (Lifeline's text line isn't printed); R5 Q3 (3 of 5) |
| P | The closing line of Ch 07 treats wanting to keep reading as a symptom, and reads as a telling-off. | Ch 07, close | R1 note 17; R2 note 36; R5 WLY 6, note 18 (3 of 5) |
| Q | The Ch 01 "loop" never loops back to low mood, and the "only box you can change" sentence appears twice. | Ch 01 | R1 note 9; R2 note 12; R5 notes 6–7 (3 of 5) |
| R | PHQ-9 last question: see Blocker 1. | Ch 00 | R1 note 7; R4 finding 1; R5 note 5 (3 of 5) |

### 4.3 Two readers

| Finding | Where | Raised by |
|---|---|---|
| Read This First covers less than the pages that send readers to it. It has nothing for someone who has already harmed themselves or taken something (R4, condition 3). It never names self-harm without suicidal intent (R5). | Read This First | R4 finding 4; R5 note 3 |
| The Introduction calls reading end to end "the failure". | Introduction | R2 note 4, WLY 3; R5 note 1, WLY 6 |
| Ch 05's closing line, "Everything after this is refinement", contradicts Ch 09 calling itself "the deepest chapter", and undersells Ch 08–10. | Ch 05, close | R1 note 16; R5 note 16 |
| The Week 1 check-in can't be completed. "Floor days" needs the minimum viable day from Ch 08, which Appendix A has readers write in Week 2. | Ch 00; App A | R1 note 6; R2 note 7 |
| Three rows of the escalation table say only "Escalate", not to whom. R2 marks the drinking row `safety risk`. | Ch 00, Decide Now | R2 notes 9–10; R4 note 9 |
| Raw LaTeX, `$(P\ge4)$`, in the field sheet. | Ch 02 | R1 note 10; R2 note 16 |
| "Positive thinking, which doesn't work" is stated without support. | Ch 03, opening | R1 note 12; R4 note 15 |
| Week 6 bundles Ch 07, 09 and 10, putting the heaviest chapter in the busiest week. | App A | R1 note 22; R4 note 28 |
| C4 step 7, "One reason worth staying for", is asked with nothing around it. | App C4 | R2 note 46 (`safety risk`); R5 note 26 (`preference`) |
| No date on the crisis numbers. | Front matter; Read This First | R1 note 2, Q3; R2 Q3 |
| Read This First needs to be a live link in the EPUB wherever the book sends readers to it. | Ch 00, Ch 09, App B | R1 note 4; R2 note 38 |
| Idiom and jargon: "grade", "ship", "rep". | Ch 02, 04; App B | R2 notes 17, 27; R3 notes 14–15 |
| Care on a Budget assumes a health system and an employer the reader may not have. | Ch 00 | R2 note 11; R3 notes 7–8 |
| The thoughts the chapter opens with ("I've wasted years", "Everyone my age is ahead") are named but never worked through. | Ch 03 | R1 WLY; R3 note 12 |
| The evidence-against in Example Three is soft. It leans on an outside excuse (R1) and includes a reassurance rather than a fact (R5). | Ch 03, Example Three | R1 note 14; R5 note 12 |

### 4.4 Single reader: lower confidence, kept visible

Each of these was raised by one reader, and some may not apply to most readers. The first two are called out because they would be embarrassing to miss for the readers they do fit.

**Called out**

- **Shift work (R2 notes 8, 14 and 35).** The book assumes a regular day in several places:
  - The weekly check-in asks whether sleep timing was "roughly regular" (Ch 00).
  - The bipolar advice is to keep sleep and routine "regular above all" (Ch 00).
  - "Sleep timing drifts later" is an early warning sign (Ch 10).
  - Postponement needs "the same slot every day" (Ch 07).
  - The fallback log is kept "late morning, afternoon and evening" (Ch 02).

  In R2's words: "On rotating shifts my sleep is never regular, so none of this tells me anything." This may be wrong for most readers. For anyone on nights or rotating shifts, it breaks the check-in, a warning sign and the book's bipolar advice.
- **Residence tied to the employer, and confidentiality (R3 notes 7 and 10, WLY 2).** Care on a Budget calls employee assistance programmes "usually free". Where a residence visa depends on the employer, the barrier is what the employer will learn, not the price. The same pressure makes Example Two's "three weeks, not three years" a real deadline rather than a distortion. This may be wrong for most readers. For those it fits, the cheapest route to care the book offers is the one they're most likely to avoid.

**Reader 4's single-reader release conditions** are in §3: condition 5 (C4 sequential use and means), condition 7 (exclusions for suicidal content in Ch 03 and Ch 07), condition 8 (bipolar caution), condition 9 (inner critic vs hearing voices), and the "name the 988 services" part of condition 2. How many readers raised them doesn't lower their priority.

**Other single-reader findings**

| Reader | Where | Finding | Cited as |
|---|---|---|---|
| R3 | Read This First, bullet 3 | "Tell one person" assumes the nearest person is safe to tell. Add a line for readers whose closest people aren't. | note 4, `safety risk` |
| R3 | Read This First, bullet 1 | In the UAE, 999 is the police. Nothing says whether calling the police about suicidal thoughts is appropriate, or what follows. R3 suggests "ask for 998 and say you need medical help" as a clearer instruction. | note 2, `safety risk` |
| R3 | App C4 | In a shared home, a Safety Plan that someone else finds "can start its own crisis". See Conflict 6. | note 5, `safety risk` |
| R4 | Ch 02, Stage 1 | Three days of hourly logging can show a severely depressed reader a record of empty days, which can fuel self-attack. | note 11, `safety risk` |
| R4 | Ch 04, Run One Experiment | No exclusion for safety-critical work (medication doses, sign-offs, legal filings) or for OCD-type checking. | finding 14, `minor`; notes 16–17 |
| R4 | Ch 01, Where the Loop Is Breakable | The trials cited used therapist-delivered BA, so they don't support "considerably simpler to run yourself". | note 10; scope finding 4 |
| R4 | App A; Ch 10 | The Safety Plan is never scheduled in the six-week plan or linked from Ch 10's escalation line. | finding 15, `minor`; notes 25, 27 |
| R4 | App C4 | Confirm whether the adapted Stanley-Brown template needs the rights holders' permission. | finding 19, `minor` |
| R4 | App D, Questions to Ask | "If one doesn't, that tells you something too" can read as permission to leave care. | note 30; scope finding 8 |
| R4 | Health notice; Closing Note | "does not … treat any condition" contradicts "can't treat on its own". Separately, "Procedures work whether or not you're convinced" overclaims. | notes 31–32 |
| R5 | Ch 09 | Every cost in the table is about output, and the chapter ends on "ship something". Self-attack is treated as a productivity problem. See Conflict 1. | WLY 3 |
| R5 | Ch 09, The Tool | The chapter says "Fill in both columns properly", but gives only a pre-filled table, with no blank copy here or in App C. | note 24 |
| R5 | Ch 04, Run One Experiment | Nothing on what to do if the feared outcome did happen. | note 14 |
| R3 | Ch 09, "The feel of integrity" | Humility is a real virtue in many upbringings. One sentence should separate it from self-attack. | note 13 |
| R3 | Ch 02, 05, 07 | The tools assume a private room and freedom to move ("another room", "go outside"). Offer alternatives that don't need space. | WLY 4; note 17 |
| R3 | Introduction, worksheets note | In a shared home, paper is less private than a screen that saves nothing. See Conflict 6. | note 18 |
| R2 | Whole book | A plain-language pass: explain psychoeducation, declarative, CBT, ADHD, rumination, "minimum viable" and the citation markers where they first appear, or replace them. R2 gave clarity 2 out of 5, the panel's lowest rating. See Conflict 5. | One change; notes 1–2, 5–6, 34, 37, 47 |
| R2 | Ch 02, Stage 2 | "Something that dropped away" may be a person who has died, or a marriage. There's no guidance for when it can't come back. | note 18 |
| R2 | Ch 02 vs App C1 | The chapter's log has no mood column but asks when mood is lowest. C1 has a mood column, but at two-hour intervals rather than hourly. | note 15 |
| R2 | Ch 00, 02, 03 | Four different scales: 0–100, 0–100%, 0–10, and P/A out of 10. | note 20 |
| R1 | Read This First | Seven emergency numbers in one sentence are hard to scan on a phone. Put one country per line. | note 2 |
| R1 | Every chapter close | By Ch 06 the closing lines read as a tic, and each chapter calls itself the most something. See Conflict 4. | WLY; note 23 |
| R1 | Ch 09 vs Ch 07 | "The only form of avoidance that feels like a virtue" (Ch 09) clashes with "the most convincing form of avoidance there is" (Ch 07). | note 21 |
| R5 | Ch 01, 02, 08 | Wording that judges the reader: "withholding the input", "dead time", "the day counts as lost". | notes 8, 9, 20 |

Single-reader `preference` notes not listed here are still in the individual reports.

---

## 5. Conflicts: kept as they are, not averaged

### Conflict 1 — Chapter 09: two different problems with two different fixes

**First, a correction to the brief's framing.** "Reader 4 saw a safety problem, Reader 5 saw tone and structure" is close, but it isn't what they wrote:

- Both labelled Chapter 09 items `safety risk`: R4 notes 23 and 24; R5 notes 21, 23 and 25.
- Reader 4 rated its one Ch 09-specific finding `minor` (finding 12). Its `major` findings that touch Ch 09 are cross-chapter: the stop rule (finding 11) and the Triage routing (finding 9).

The real disagreement is over what the risk is, and so over what fixes it.

| | Reader 4 (clinician) | Reader 5 (lived experience) |
|---|---|---|
| **The problem** | Missing guardrails:<br>• no rule to stop if distress rises (finding 11, `major`)<br>• no "do not do this alone" line for readers whose inner critic echoes someone who abused or controlled them (Q4; finding 12, `minor`)<br>• the Triage row can send someone who hears voices to a chapter about self-criticism (finding 9, `major`) | The chapter's edges and framing:<br>• the opening sends away the readers who most need it (note 21)<br>• the cost row states "wasted years" as a fact (note 23)<br>• the close leaves the reader alone (note 25)<br>• every cost is about output, and the chapter ends on "ship something" (WLY 3) |
| **Kind of fix** | Add things: a standard stop-if box, a "do not do this alone" line, and a line separating the inner critic from hearing voices in Triage and the opening. The chapter's argument stays as it is. | Rewrite the opening, the cost row and the close, and name costs that go beyond output. |
| **The opening redirect** | Keep it. Reader 4's objection is that it is too narrow: it "only covers active self-harm" (note 24). | Loosen it. "Or thinking about it" turns away readers who self-harm without being suicidal, then sends them to a page that never mentions self-harm (note 21). "That's the one place the book felt like rejection" (WLY 1). |
| **Other readers on the opening** | R1: "The self-harm gate at the top is good" (Q4). R2: "Good that it's there", though R2 wants the numbers there too (note 38). R3 wants Ch 03 to have a line like it (Q2). | No other reader raised the exclusion. |

**If only one of the fixes is made:**

- **Reader 4's fix alone** adds warnings and a "do not do this alone" line to the chapter Reader 5 already felt as rejection. The wording decides whether that line reads as care or as another door closing.
- **Reader 5's fix alone** lets a reader who is acting on thoughts of self-harm stay inside an exercise about self-attack, with no one there.

**Where they don't conflict:** the cost row (R4 note 23, R5 note 23) and the missing support at the close (R4 note 24, R5 note 25). Both are five-reader consensus items (§4.1 A and B), and they can be fixed whichever way the conflict is decided.

**Decision for the author:** whom the opening redirect sends away, and whether the "do not do this alone" line reads as exclusion or as company. Neither reader has seen a wording that tries to satisfy both. Test any such wording with both readers (§9, step 7).

### Conflict 2 — "Never miss twice": the clearest rule for one reader, among the weakest for three

- **R2:** "And 'Never miss twice.' I understood every word of it." (What worked)
- **R1 (notes 18–19), R4 (note 22) and R5 (note 19, Q2):** it never says what counts as a miss, and it is all-or-nothing, the same pattern Ch 03 teaches readers to catch. It claims more than Lally et al. (2010) found, and it clashes with "put it down whenever you want".
  - R4 (Q2): "A depressed reader will hear the rule louder than the permission."
  - R5 (Q2): billing it as one of the rules that carry the most weight "makes stopping the doing for a bad stretch feel like breaking a rule."
- **The stakes:** Appendix B lists it among "the three that carry most of the weight".
- **Scope of the criticism:** it targets the definition and the claim, not the plain wording R2 valued. Whether the rule stays a headline rule is the author's call.

### Conflict 3 — "Wait it out": a scope risk to the clinician, the real permission to the peer

- **R4 (scope finding 6; note 21):** "Run the minimum day and wait it out" is borderline. The paragraph after it mitigates it, but the table row stands alone in Appendix B's logic, cut off from the escalation line.
- **R5 (Q2):** it "is the real permission, and it deserves to be louder than 'never.'"
- **The two fixes pull in different directions.** R5 wants it made louder. R4 wants it tied to the escalation line. They are compatible only if the escalation line goes with it wherever it is made louder.

### Conflict 4 — The closing stop lines at the end of each chapter

- **In favour:**
  - R3: "It is the most consistent thing in the book." It mattered for a second-language reader who tires faster.
  - R4: "explicit and credible" (Q2).
  - R5: they mostly felt like real permission (Q2).
- **Against:** R1: "By Ch06 the italic sign-offs were a tic I skimmed." R1 also notes that every chapter calls itself the most something.
- **The choice:** keep them uniform, which is what R3 needs, or vary and trim them, as R1 wants.
- **A separate, agreed problem:** the Introduction's "failure" line and the closing line of Ch 07 read as a telling-off (§4.2 P; §4.3).

### Conflict 5 — Whom the book is for

- **Opposite readings of the same section, "Who This Is For":**
  - R1: "This is me."
  - R2: "By the second page I was being told this isn't for me" (WLY 1; note 3). R2 gave clarity 2 out of 5, the lowest rating anyone gave.
- **R3** sits between them: R3 can follow the book, but the idioms cost re-reading.
- **This is a positioning decision, not an edit.**
  - If R2 is outside the intended audience, the fix is one sentence.
  - If R2 is inside it, the fix is R2's plain-language pass, which touches every chapter.

### Conflict 6 — The Safety Plan: keep it, or keep it private

- **R1, R2, R4 and R5:** the in-book fields are wiped, so tell readers to keep a copy on paper or in their own notes app (R4 condition 4).
- **R3:**
  - In a shared home, "a safety plan that someone finds can start its own crisis" (note 5).
  - "A notebook of thought records is less private than a screen that saves nothing" (note 18).
  - R3 valued the design that saves nothing (What worked).
- **The tension:** condition 4, as written, moves the plan to exactly the places R3 flags, and it deals only with keeping the plan.

---

## 6. Verification: the Chapter 03 figures

My summary of the panel in chat said "Examples Three and Four drop 45 points" without saying which rating. The brief's figures (40 and 30) are the **belief** drops. The readers' figures (45) are the **emotion** drops. Each set is correct for its own rating.

| Example | Emotion, before → after | Emotion drop | Belief, before → after | Belief drop |
|---|---|---|---|---|
| One (the author's) | Shame 80 → 55 | 25 | 90% → 65% | 25 |
| Two (job search) | Hopelessness 75 → 50 | 25 | 85% → 60% | 25 |
| Three (domestic) | Overwhelm 85 → 40 | **45** | 90% → 50% | **40** |
| Four (admin) | Dread 80 → 35 | **45** | 85% → 55% | 30 |

Source: the Ch 03 re-rate lines, l.366–402.

- **The readers' figures:**
  - R1 note 13: "Emotion drops of 45 and 45". Correct.
  - R4 note 13: "Emotion drops of 45 points (85→40, 80→35)". Correct.
  - R5 note 10: "25 to 45 points". Correct.
  - R2 note 22: "25 to 50 points". **A slip.** The pairs R2 lists (80→55, 85→40, 80→35) give 25, 45 and 45, and no rating in any example drops 50.
  - R3 gave no figures.
- **The book doesn't say which rating its range refers to.** l.406 says "A drop of 10 to 30 points is a good result… You're trying to get the thought down to the size the evidence supports", which sounds like belief. l.362 says "The emotion rating is the one that actually matters."
- **What the finding comes to:**
  - Example Three is outside the range whichever rating is meant (emotion 45, belief 40).
  - Example Four is outside it on emotion (45) and at the upper limit on belief (30).
  - The book should also say which rating the 10–30 range means. That is a separate fix.

---

## 7. Ratings (context only; they don't drive the decisions above)

| Reader | Usefulness | Clarity | Trust | Their lowest score, in their words |
|---|---|---|---|---|
| R1, core audience | 4 | 4 | 3 | Trust: "the things I check are the ones that slip" |
| R2, non-professional | 3 | **2** | 3 | Clarity: "I hit a word I didn't know, or an example about laptops and apps, on nearly every page" |
| R3, non-Western | 4 | 4 | 3 | Trust: "When I followed the book's own safety path from my country, it ended at the police number and a website" |
| R4, clinician | 4 | 4 | 3 | Trust: "the safety framework is sound at the front of the book but missing inside the exercises" |
| R5, lived experience | 4 | 4 | 3 | Trust: "the most safety-critical places are the least carefully joined up" |

---

## 8. Method and provenance

- **Manuscript reviewed:** `.claude/context/manuscript.md`.
  - It is a byte-identical copy of the author's upload, `Tools, Not Theory - Complete Manuscript.md` (2026-09-27).
  - SHA-256 `6961514bbefc1c17953de46604a8430358d64d12eae391c10bece7f7fdceaf41`. The hash was checked again after all five reviews and has not changed.
  - 958 lines (the last line has no trailing newline) and 9,663 words with Markdown syntax removed. The file is gitignored and not committed. Every "l." citation in the reports refers to this file.
- **Both amendments were confirmed before any reader was dispatched.** The Phase 0 re-run (commit `adc92a1`, 02:46 UTC) found:
  - Operating Rule 2's voice-memo / dictation sentence;
  - Chapter 03 Worked Examples Three and Four, with the closing line "across all four examples";
  - the `[I]` citation restored in the Introduction.
- **The readers saw the amended text.** All five answered targeted question 1 about four Ch 03 examples, and R2 cites the Rule 2 dictation sentence directly ("the option to use voice memos").
- **The earlier PDF was not used.** `Tools_Not_Theory___Revised_Publication_Edition.pdf` predates both amendments, and no reader was given it.
- **Dispatch and independence:**
  - Reader 4 ran first and alone, starting at 02:47 UTC. It handed back its report before Readers 1, 2, 3 and 5 were sent out together at 02:52 UTC.
  - Each reader's only input was the manuscript path.
  - The session transcripts show that each reader opened only the manuscript: one read of `.claude/context/manuscript.md` each. Reader 4 also ran two searches confined to that file, plus 30 web requests.
  - No reader opened the intake report, another reader's report or this file.
- **Tools:** each agent's definition in `.claude/agents/` sets its tools.
  - Only Reader 4 had WebFetch and WebSearch.
  - Readers 1, 2, 3 and 5 commented on the crisis numbers from memory, and each said so.
- **Reader 4's widened brief worked** (see the log below). Reader 4 listed 25 locations it checked, including all nine recorded at Phase 0.
- **Reports:** each was saved verbatim from the reader's final output:
  - `reader-1-core-audience.md` (`33e5a86`)
  - `reader-2-non-professional.md` (`373ee11`)
  - `reader-3-non-western.md` (`49b6498`)
  - `reader-4-clinician.md` (`0cce65b`)
  - `reader-5-lived-experience.md` (`a4b121d`)
- **Limitations:**
  - **The readers are simulated personas, not people.** Their reactions are hypotheses about how such readers would respond. The safety findings stand on their own merits. The reception findings (who feels shut out, what reads as a telling-off) should be checked with real readers before they are treated as settled.
  - **Reader 4's VERIFIED entries rest on model summaries.** WebFetch returns a model's summary of a page, not the page. The supporting check in §1 used raw page text instead.
  - **Only Reader 3 read from a fixed region** (the UAE / South Asia). Readers 1, 2 and 5 read without a fixed country.
- **Correction to the Phase 0 record:** the re-run gave the file as 957 lines. That was a counting error, because the last line has no trailing newline. The correct figure is 958, and `phase-0-intake.md` has been corrected.

### Brief amendment log

| Date | Brief | What changed | Why |
|---|---|---|---|
| 2026-09-27 | Reader 4 (`.claude/agents/reader-4-clinician.md`) | **Audit checklist:** "Crisis resources (Appendix D)" became "Crisis resources (wherever they appear)". Reader 4 now searches the whole manuscript and audits every crisis resource it finds. **Output:** added a "Crisis resource locations audited" section, and added a Location column to the audit table. | In this edition, Appendix D ("Working With a Professional") holds no crisis resources. The numbers are in Read This First and on the copyright page, and redirects appear in Triage, Ch 00, Ch 09, Appendix B and Appendix C4. An audit limited to Appendix D would have audited nothing. Found at Phase 0 intake. The author approved the change once the complete amended draft passed Phase 0 (see `phase-0-intake.md`, re-run section). |

---

## 9. The fix sequence

This is an order to work in, not a list. Each step says what it depends on, so the author can see why it sits where it does. Nothing here should start until the author has read this report.

### Step 1 — Close the PHQ-9 gap

- **Closes:** Blocker 1; condition 1.
- **Edit:** one sentence in Ch 00, Set a Baseline.
- **Depends on:** nothing. Do it first. It shouldn't wait for anything below.
- **Done when:** a reader who answers above "not at all" on the last question is sent to Read This First that day, whatever the total score.

### Step 2 — Verify every crisis number by hand

- **Closes:** Blocker 2; the verification half of condition 2.
- **This is not a manuscript edit,** and it can run alongside step 1.
- **The check:** a person checks every crisis entry on the service's own website and records the URL and date in this file. Start with the five UNVERIFIED entries, then the eight Reader 4 marked VERIFIED. §1 lists the pages to start from.
- **In the same pass:** source verified talk lines for India and the UAE, if the author wants to print them (consensus E). If not, say plainly on the page that none was verified.
- **It must finish before step 3,** which prints these numbers in three places. Verify once, then copy.
- **Done when:** every entry in this file has a URL and a date beside it.

### Step 3 — Rebuild the crisis page and its copies as one change

- **Closes:**
  - the naming half of condition 2, and conditions 3, 4, 5 and 6;
  - consensus E; strong G, N and O;
  - the two-reader items on a check date and a live link;
  - R3's two Read This First lines;
  - Conflict 6.
- **Read This First:**
  - name the 988 services;
  - add "if you have already harmed yourself or taken something";
  - name self-harm (R5);
  - add talk lines for India and the UAE, or a plain statement of the gap;
  - say which lines are free, which run 24 hours and which take texts;
  - print a check date;
  - put one country per line;
  - add R3's line for readers whose closest people aren't safe to tell, and R3's line on asking for medical help rather than the police.
- **Appendix B and C4:** reprint the numbers, or a summary of Read This First, from the same verified record.
- **C4:**
  - a persistence warning, with a privacy line beside it (Conflict 6);
  - the instruction to use the steps in order;
  - step 6 prompting for specific means;
  - the prompts for steps 3 and 5 (finding 17).

  Two optional additions: a note on step 7 (R2, R5), and a link to the Safety Plan from Ch 10 and Appendix A (R4, finding 15).
- **Also:** make "Read This First" a live link wherever it appears.
- **Why one change:** three copies of the same numbers have to match. Fixing them separately invites drift, and the check date should be printed once.
- **Depends on:** step 2.
- **Done when:** all three places agree with each other and with the record from step 2.

### Step 4 — Standardise the stop-if box, then apply it to Ch 03, 05 and 07 (and Ch 02 and 04)

- **Closes:**
  - condition 7, condition 8, and the Ch 03, 05 and 07 parts of condition 10;
  - strong J and L;
  - Reader 4's "One change";
  - the "When Not to Use This" boxes found missing at Phase 0.
- **Design the box once.** It says: stop if distress rises sharply or thoughts of death appear; go to Read This First. It then names the group who shouldn't do that chapter's exercise alone.
- **Apply it to:**
  - Ch 03: thoughts about death (condition 7);
  - Ch 07: "go concrete" and postponement (condition 7);
  - Ch 05: panic and trauma, what to do if the sensation climbs, and R2's check for chest pressure;
  - Ch 02 Stage 3 and Appendix A Week 3: the bipolar caution (condition 8);
  - Ch 04: safety-critical work and OCD-type checking.
- **Decide here whether the box goes in every chapter.** Reader 4's "One change" says Ch 01–09. The boxes for Ch 01, 06 and 08 are Reader 4's open items.
- **Depends on:** step 3. Every box sends readers to Read This First, and until step 3 that page doesn't cover self-harm or someone who has already harmed themselves.
- **Done when:** one box design is used in every chapter it is applied to.

### Step 5 — Rewrite Chapter 09, using the standard box

- **Closes:** condition 9, the Ch 09 part of condition 10, and consensus A and B.
- **First, the author decides Conflict 1:** whom the opening redirect sends away, and how "do not do this alone" is worded.
- **Then:**
  - the Ch 09 opening and the Triage row, together, because one sends readers to the other. This is where the inner critic is separated from hearing voices (condition 9).
  - the standard box, plus the line on trauma-linked self-criticism (condition 10);
  - the cost row;
  - a close that routes the reader to a person, to Read This First, and to Appendix D's CFT line.
- **Depends on:** step 4, because the box should be settled before the chapter where it matters most. Also step 3, because the opening sends readers to Read This First.
- **Done when:** conditions 9 and 10 are met and the Conflict 1 decision is recorded in this file.

### Step 6 — The remaining consensus and strong findings

- **These are not release conditions.**
- **Ch 03 examples** (consensus C and D; strong H and M; Reader 4's open item):
  - say which rating the 10–30 range means, and bring the examples inside it;
  - add a record that barely moves;
  - add one example with another person in it;
  - write a version of Example Four where the money is short;
  - work through the thoughts the chapter opens with.
- **Ch 08:** "Never miss twice" (strong K, Conflict 2) and "wait it out" (Conflict 3).
- **Other strong items:**
  - the Ch 01 loop (Q);
  - the founder-life examples (I);
  - the closing line of Ch 07 and the Introduction's "failure" line (P; Conflict 4).
- **The audience decision (Conflict 5).** It decides how big the plain-language pass is.
- **Then** the §4.3 and §4.4 items the author chooses to act on: the LaTeX in Ch 02, the Week 1 check-in, "Escalate" to whom, shift work, and the visa and confidentiality point.
- **Ride-along rule:** if one of these touches a chapter already open in steps 3–5, it can go in the same edit. It must never hold one of those steps up.

### Step 7 — Check again before release

- Re-run Phase 0 on the revised draft: record the new hash and confirm that steps 1–5 landed.
- Send Reader 4 out again, with its brief unchanged, to confirm each of the ten conditions is closed.
- Send Reader 5 out again with the full manuscript, because the Conflict 1 decision is exactly what Reader 5 would test.
- **Release** when Reader 4 returns CLEAR (or confirms every condition closed) and the record from step 2 is complete in this file.
