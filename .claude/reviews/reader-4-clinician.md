# Reader 4 — Clinician Report

Manuscript reviewed: `/home/user/Book-review-/.claude/context/manuscript.md`

## Snapshot

I read this as a CBT-trained clinician. My job was to look for harm, not for how comfortable the book feels. I read the whole manuscript in one pass, in order, from the title page through the Closing Note and colophon (958 lines). I did not stop early. It fit in context, so I kept no scratch file. After reading, I checked the crisis resources against the services' own websites using WebFetch/WebSearch in this session. Several government emergency-service sites returned 403, 503, 404 or DNS errors. The table below shows which entries I could confirm and which I could not.

## Verdict

This is a careful, conservative self-help manual. It knows its limits. It puts suicide risk first, rules out physical causes before offering behavioural fixes, tells the reader not to touch their medication, and asks them to commit to an escalation point in advance. The core problem is where the safety material sits. It is mostly in two places, Read This First and the Chapter 00 escalation table. The exercises themselves have almost no local safeguards. Specifically:
- The thought record has no carve-out for thoughts about death.
- The worry-postponement method can end up scheduling suicidal thoughts for later.
- The PHQ-9 is recommended for self-administration every two weeks, but nothing says what to do if item 9 (thoughts of death or self-harm) is positive.
- The safety plan tells readers to keep it on their phone. In the digital edition, the fields clear when the book is closed.

None of this is dangerous in the way wrong advice is dangerous. All of it is fixable with a sentence or a box. I would not release it until those fixes are in and the unverified emergency numbers have been checked.

## What worked

- Read This First (front). Correct placement, plain language, a script for telling another person, and means restriction all appear before any content.
- Chapter 00, Check the Body First and the medication sentence ("don't change or stop it because of anything in this book"). This is the right scope boundary, stated plainly.
- Chapter 00, Decide Now table. Committing to an escalation point in advance is clinically sound, and "not a verdict on your effort" removes a common barrier to seeking help.
- Chapter 00, the PHQ-9 sentence ("a signal for a conversation with a professional, not as a diagnosis you give yourself"). This framing is correct.
- Chapter 03, "When not to use this" (accurate thoughts). Correctly stops readers from challenging true thoughts.
- Chapter 05, the Five-Minute Rule. The permission to stop is real and explicitly defended.
- Chapter 08, escalation line, and Appendix A's closing paragraph. Both send non-response to escalation instead of to more effort.
- The Stanley & Brown (2012) citation in the Notes is correct for the safety plan's structure.

## Where it lost you

- **Chapter 00, Set a Baseline (PHQ-9).** Readers are told to self-administer every two weeks with no instruction for a positive item 9. This is the first place a clinician stops reading and starts writing.
- **Chapter 03, The Thought Record.** Nothing tells the reader not to run this on "I'd be better off dead" or "everyone would be better off without me". Filling in "Evidence for" on a suicidal thought, alone, is contraindicated. Worked Example Two already sits in hopelessness territory ("Nobody is going to hire me", hopelessness 75).
- **Chapter 07, Three Interrupts (items 1 and 3).** "If a loop won't convert at all, it isn't a problem, it's a mood" is a catch-all. Without a carve-out it takes in suicidal ideation, OCD obsessions and trauma intrusions. Postponement then tells the reader to "think about the list on purpose" in a scheduled slot.
- **Appendix C4, Safety Plan.** The intro says to keep it on the phone. The front-matter Privacy note says digital fields are cleared on close. A reader who fills in C4 in the EPUB loses it. There is also no instruction to use the steps in order.
- **Triage, row "The voice in my head is vicious" → Chapter 09.** Nothing distinguishes the inner critic from hearing voices. Someone with psychotic symptoms could be sent to a self-criticism chapter.
- **Chapters 01/02 and Appendix A Week 3.** Activity is increased ("go to two blocks a day") without repeating the bipolar caution. That caution appears only in Chapter 00, which the Triage table lets readers skip.

## Line-level notes

1. **Front matter, Privacy (l.21) vs Appendix C4 intro (l.846).** "Nothing you type is saved… cleared when you close the book" vs "Keep it on your phone and on paper." C4 has no warning of its own that digital entries are lost. `safety risk`
2. **Read This First, bullet 1 (l.33).** Covers "might act on these thoughts soon". Does not cover "have already hurt yourself or taken something". `safety risk`
3. **Read This First, bullet 2 (l.34).** Numbers are given without service names (988 Suicide & Crisis Lifeline / 9-8-8 Suicide Crisis Helpline). If a number fails, the reader has nothing to search for. `confusion risk`
4. **Read This First, bullets 1–2 (l.33–34).** Emergency numbers are listed for India and the UAE, but no crisis line for either. Readers there get only findahelpline.com. `safety risk`
5. **Triage table, row 1 (l.127) / Chapter 00 table row 1 (l.183) / Chapter 09 opening (l.663) / Appendix B row 1 (l.781).** All four redirect to Read This First, and none carries a number. In print, a reader in crisis has to find the front of the book. Appendix B says "Contact a person or service now" but names neither. `safety risk`
6. **Triage table, row "The voice in my head is vicious" (l.136).** Clarify that this means your own critical thinking. Hearing voices that seem to come from outside you is a reason to see a doctor. `safety risk`
7. **Chapter 00, Two Patterns, Bipolar (l.164).** "If this applies" asks the reader to self-identify before any assessment. The advice itself is conservative and acceptable. The problem is that the caution never appears again at the point where activity goes up (Chapter 02 Stage 3; Appendix A Week 3). `safety risk`
8. **Chapter 00, Set a Baseline (l.175).** PHQ-9 item 9 is not mentioned. Add: any answer above "not at all" on the last question means go to Read This First today, whatever the total score. `safety risk`
9. **Chapter 00, Decide Now table (l.185–187).** "Escalate" is used three times without saying escalate to whom. It depends on a sentence the reader may not have written yet. `confusion risk`
10. **Chapter 01, Where the Loop Is Breakable (l.225).** "Performed comparably to cognitive therapy, and it is considerably simpler to run yourself." The cited trials (Dimidjian 2006; Richards 2016) tested therapist-delivered BA. The second clause is not supported by them, and the sentence implies self-run BA matches therapy. `confusion risk`
11. **Chapter 02, Stage 1 (l.249–262).** Three days of hourly logging can confront a severely depressed reader with a record of empty days, which can fuel self-attack. There is no line on what to do if the log itself brings mood down. `safety risk`
12. **Chapter 03, The Thought Record (l.351–362).** No exclusion for thoughts about death, suicide or being a burden. Add a redirect to Read This First, and a line saying these should not be worked through alone. `safety risk`
13. **Chapter 03, Worked Examples Three and Four (l.392, l.402).** Emotion drops of 45 points (85→40, 80→35) against the stated "10 to 30 points is a good result" (l.406). The examples model an outcome the text then tells readers not to expect. `confusion risk`
14. **Chapter 03, Worked Example Four (l.400).** "The underlying accounts have sufficient funds." The example only works if the reader is solvent. No worked example shows a thought that is largely accurate, or a re-rate that barely moves. `confusion risk`
15. **Chapter 03, opening (l.337).** "Positive thinking, which doesn't work" is an unsupported absolute. `preference`
16. **Chapter 04, Run One Experiment (l.461).** No exclusion for work where safety is at stake: medication doses, clinical or engineering sign-off, legal filings. "Pick your current project" (l.469) invites exactly this. `safety risk`
17. **Chapter 04, Run One Experiment.** For readers with OCD-type checking, a deliberate "no third reread" experiment is a self-directed form of exposure and response prevention (ERP), with no support. It needs a line routing those readers to a professional. `safety risk`
18. **Chapter 05, Urge Surfing step 2 (l.498).** Ninety seconds of focusing on body sensations. There is no carve-out for panic-prone readers or trauma survivors (risk of dissociation or flashback), or for tasks avoided because they involve a person or place linked to trauma. `safety risk`
19. **Chapter 07, Go concrete (l.590).** "If a loop won't convert at all, it isn't a problem, it's a mood." Overreach. Some loops that won't convert are obsessions, trauma intrusions or suicidal ideation. `safety risk`
20. **Chapter 07, Postpone it (l.592).** No exclusion for suicidal thoughts or trauma memories. Readers must not put these on a list to think about deliberately later. `safety risk`
21. **Chapter 08, What a Gap Is Telling You (l.634).** "Run the minimum day and wait it out" for a low-mood stretch. The next paragraph mitigates it, but the table row stands alone in Appendix B's logic. `confusion risk`
22. **Chapter 08, Never Miss Twice (l.612–613) vs Introduction closing (l.115).** "Put it down whenever you want" sits against "by three the structure is gone". For a depressed reader, the second can become new evidence for self-attack. `confusion risk`
23. **Chapter 09, cost-benefit table (l.684).** The prefilled "It costs the years the protection was supposed to save" reads, to a depressed reader, like the self-attack it is meant to disarm. `safety risk`
24. **Chapter 09, closing (l.705).** The book calls this its "deepest chapter" but gives no distress stop rule and no support pointer (Appendix D's CFT line is 150 lines away). The top redirect only covers active self-harm. `safety risk`
25. **Chapter 10, Your Escalation Line (l.733) and field sheet (l.749–750).** No cross-reference to the C4 Safety Plan. The two plans never meet. `confusion risk`
26. **Appendix A, Week 3 (l.765).** "Go to two blocks a day" with no bipolar or sleep-disruption check. `safety risk`
27. **Appendix A, Weeks 1–6.** The Safety Plan is never scheduled, even though Read This First calls it "one of the most protective things in this book". `safety risk`
28. **Appendix A, Week 6 (l.768).** Chapters 07, 09 and 10 are bundled together. The heaviest chapter shares a week with two others. `preference`
29. **Appendix C4 (l.848–856).** No "work down the steps in order; if one doesn't help, go to the next" instruction. `safety risk`
30. **Appendix D, Questions to Ask (l.881).** "If one doesn't, that tells you something too" can be read as permission to leave care after one defensive answer. `confusion risk`
31. **Health notice (l.17) vs Closing Note (l.945).** "Does not… treat any condition" vs "can't treat on its own". The two are inconsistent. `confusion risk`
32. **Closing Note (l.949).** "Procedures work whether or not you're convinced by them" is an overclaim. `preference`

## Answers to the four targeted questions

**1. Chapter 03 worked examples: broad enough to include me?**
No, and as a clinician I care less about myself than about who is missing. All four are about work, admin or household tasks. The implied reader is employed, degree-educated, running a project, and in Example Four solvent enough to pay the fees. There is nothing on relationships, grief, caregiving, illness, loneliness, discrimination or money trouble that is real and not a distortion. All four re-rate cleanly, and two exceed the book's own "10 to 30 points" range. None shows the common clinical case where the thought is mostly accurate and the number barely moves. For a reader whose life does not look like these, the examples say that the method works for other people.

**2. Stop rules: clear, and did I feel able to stop?**
For pacing, yes. Every chapter ends with an explicit and credible "stop here", and the Five-Minute Rule's permission to stop is well defended. For distress, no. No exercise has a rule like "if this raises your distress sharply, or brings up thoughts of harming yourself, stop and go to Read This First." Chapters 03, 05, 07 and 09 need one. "Never miss twice" (Chapter 08) also works against the permission to stop. A depressed reader will hear the rule louder than the permission.

**3. Crisis resources: accurate and usable?**
I read without a fixed jurisdiction and audited every listed region. I verified these against the services' own sites this session: 988 call/text (US and Canada), Samaritans 116 123 (UK and Ireland), Lifeline 13 11 14 (Australia), findahelpline.com, EU 112, and UK 999. I could not verify these from an official source: US 911, Canada 911, India 112, Australia 000, and UAE 999/998. The official sites returned errors. Secondary sources were consistent with the printed numbers, but I have not treated them as confirmed. On usability:
- The numbers appear in only one place.
- India and the UAE get emergency numbers but no crisis line.
- Services are not named.
- Nothing covers "already harmed yourself".
- Lifeline's text option (0477 13 11 14, per lifeline.org.au) is not printed. That is optional, but it matters for readers who cannot talk aloud.

**4. Does any chapter push too far or leave me alone with something heavy?**
Yes, three:
- **Chapter 09** is the clearest. It takes self-loathing apart as a strategy that serves a purpose, prefills "It costs the years…", calls itself the deepest chapter, and closes with "Put it down." There is no check-in and no support route beyond the self-harm redirect at the top. Readers whose inner critic echoes someone who abused or controlled them should be told not to do this alone.
- **Chapter 03** can leave a reader alone with a death-related thought and an "Evidence for" column.
- **Chapter 07**'s postponement can leave a reader alone with a scheduled appointment to think about intrusive or suicidal material.

## Ratings

- Usefulness: 4
- Clarity: 4
- Trust: 3

Trust is lowest because the safety framework is sound at the front of the book but missing inside the exercises. Five printed emergency numbers could not be confirmed from an official source in this session.

## One change

Add a short, consistent "When not to use this / stop if" box to every exercise chapter (01–09). Each box should say:
- Stop if distress rises sharply or thoughts of death appear.
- Go to Read This First.
- Name the specific population for whom that chapter should not be done alone.

Print the crisis numbers again in Appendix B and Appendix C4.

## Safety findings

1. **PHQ-9 item 9 unaddressed (Chapter 00, Set a Baseline).** Readers self-administer every two weeks with no instruction for a positive answer to the self-harm/death item. **blocker**
2. **Five emergency-number entries unverified** (US 911, Canada 911, India 112, Australia 000, UAE 999/998, Read This First). None was shown to be wrong. The official sources were unreachable in this session, so the publisher must confirm them before release. **blocker**
3. **Safety plan data loss in the digital edition (front matter Privacy vs Appendix C4).** C4 says "keep it on your phone". Digital fields clear on close, and C4 carries no warning. **major**
4. **Read This First does not cover "already harmed yourself / taken an overdose".** It needs an explicit "call your emergency number or go to an emergency department now". **major**
5. **Crisis numbers appear only in Read This First.** The Triage row, Chapter 00 table, Chapter 09 opening and Appendix B row are all bare redirects. Appendix B and C4 step 5 should carry the numbers. **major**
6. **Chapter 03 thought record has no exclusion for death- or suicide-related thoughts.** **major**
7. **Chapter 07 "it's a mood" catch-all and worry postponement** can absorb suicidal ideation, obsessions and trauma intrusions. **major**
8. **Bipolar caution appears only in Chapter 00.** It is not repeated in Chapter 02 Stage 3 or Appendix A Week 3, where activity increases, and the Triage table bypasses Chapter 00. **major**
9. **Triage row "The voice in my head is vicious"** does not distinguish the inner critic from hearing voices. There is a risk of misrouting readers with psychotic symptoms. **major**
10. **Appendix C4 has no sequential-use instruction**, and step 6 is generic about means (no prompt for stored medication or other specific lethal means). **major**
11. **No distress-based stop rule in any exercise** (Chapters 03, 05, 07 and 09 in particular). **major**
12. **Chapter 09 has no "do not do this alone" advisory** for trauma-linked self-criticism. Its prefilled cost line may intensify shame. **minor**
13. **Chapter 05 urge surfing** has no carve-out for panic-prone or trauma-affected readers. **minor**
14. **Chapter 04 80% experiment** has no exclusion for safety-critical work or for OCD-type checking. **minor**
15. **The Safety Plan is not scheduled in Appendix A or cross-referenced in Chapter 10.** **minor**
16. **No crisis line listed for India or the UAE**, although their emergency numbers are listed. **minor**
17. **C4 step 3 lacks a names/numbers prompt, and step 5 lacks an urgent care / emergency department location prompt.** **minor**
18. **Service names are missing from the 988 entries** (Read This First). **minor**
19. **Stanley-Brown safety plan adaptation.** The publisher should confirm whether permission from the rights holders is needed for the adapted template. I have not verified the licensing terms. **minor**

## Crisis resource locations audited

1. **Front matter, Health notice (l.17).** A generic "seek professional help". No numbers.
2. **Front matter, crisis-resource currency note (l.19).** A generic "local emergency number" and findahelpline.com.
3. **Front matter, Privacy (l.21).** No resources. Relevant to C4 because fields do not persist.
4. **Read This First (l.29–40).** Emergency numbers for US/Canada, UK, EU/India, Australia and UAE; 988; Samaritans; Lifeline; findahelpline.com; tell-a-person script; means restriction; pointer to the Safety Plan.
5. **Introduction, Who This Is For (l.98).** Redirect to Chapter 00. No numbers.
6. **Introduction, What this is not (l.111).** Nothing.
7. **Triage, row 1 (l.127).** Redirect to Read This First.
8. **Chapter 00, Decide Now table (l.181–187).** Row 1 redirects to Read This First. The other rows say "Escalate" with no destination.
9. **Chapter 00, Care on a Budget (l.190).** Types of services, no numbers or names. Redirect to Appendix D.
10. **Chapter 01, When the Lift Doesn't Come (l.233).** Redirect to the Chapter 00 escalation table.
11. **Chapter 02.** Nothing.
12. **Chapter 03.** Nothing, and no redirect.
13. **Chapter 04.** Nothing.
14. **Chapter 05.** Nothing.
15. **Chapter 06.** Nothing.
16. **Chapter 07.** Nothing.
17. **Chapter 08, The escalation line (l.638).** Redirect to the Chapter 00 table.
18. **Chapter 09, opening (l.663).** Redirect to Read This First.
19. **Chapter 10, §3 Your Escalation Line (l.733) and field sheet (l.749–750).** Fill-in field ("who I'll contact").
20. **Appendix A, closing paragraph (l.770).** Redirect to the Chapter 00 escalation table.
21. **Appendix B, row 1 (l.781).** Redirect to Read This First plus "Contact a person or service now". No numbers.
22. **Appendix C4, steps 4 and 5 (l.853–854).** Fill-in fields (names/numbers; clinician, local emergency number, crisis line). No pre-printed numbers.
23. **Appendix D.** No crisis resources. Routes to professional care only.
24. **Notes.** Nothing (Stanley & Brown citation only).
25. **Closing Note.** Nothing.

## Crisis resource audit table

WebFetch and WebSearch were available. Official emergency-service sites for the US (911.gov, fcc.gov: 403), Canada (crtc.gc.ca: 403), India (112.gov.in: 503; mha.gov.in: 403), Australia (triplezero.gov.au → infrastructure.gov.au: 503) and the UAE (moi.gov.ae: 503; u.ae: 404; dcas.gov.ae: DNS failure; dubaipolice.gov.ae fetched but showed no number) could not be fetched. Those entries are marked UNVERIFIED — NEEDS CHECK. Search-engine snippets were consistent with the printed numbers but do not count as verification.

| Service | Jurisdiction | Number as printed | Location | Verification status | Note |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Emergency services | US | 911 | Read This First, bullet 1 | UNVERIFIED — NEEDS CHECK | 911.gov and fcc.gov returned 403. |
| Emergency services | Canada | 911 | Read This First, bullet 1 | UNVERIFIED — NEEDS CHECK | crtc.gc.ca returned 403. gnb.ca (New Brunswick provincial government) confirms 911 for that province only, not nationally. |
| Emergency services | UK | 999 | Read This First, bullet 1 | VERIFIED | https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/ — "999 is for life-threatening emergencies". The page does not address mental health crisis. |
| Emergency services | EU | 112 | Read This First, bullet 1 | VERIFIED | https://digital-strategy.ec.europa.eu/en/policies/112 — Europeans "can call the European emergency number 112 wherever they are in Europe." |
| Emergency services (ERSS) | India | 112 | Read This First, bullet 1 | UNVERIFIED — NEEDS CHECK | 112.gov.in returned 503; mha.gov.in returned 403. |
| Emergency services (Triple Zero) | Australia | 000 | Read This First, bullet 1 | UNVERIFIED — NEEDS CHECK | The official site redirect target returned 503. lifeline.org.au states "call Triple Zero (000)", which corroborates but is not the service's own site. |
| Police / general emergency | UAE | 999 | Read This First, bullet 1 | UNVERIFIED — NEEDS CHECK | moi.gov.ae returned 503; u.ae returned 404; dubaipolice.gov.ae showed no number. |
| Ambulance | UAE | 998 | Read This First, bullet 1 | UNVERIFIED — NEEDS CHECK | dcas.gov.ae returned a DNS failure. |
| 988 Suicide & Crisis Lifeline (not named in text) | US | 988 (call or text) | Read This First, bullet 2 | VERIFIED | https://988lifeline.org/ — Call and Text at 988, 24/7/365. Recommend printing the service name. |
| 9-8-8 Suicide Crisis Helpline (not named in text) | Canada | 988 (call or text) | Read This First, bullet 2 | VERIFIED | https://988.ca/ — "Call or Text 9-8-8", 24/7/365. Recommend printing the service name. |
| Samaritans | UK | 116 123 | Read This First, bullet 2 | VERIFIED | https://www.samaritans.org/how-we-can-help/contact-samaritan/ — free, any time. |
| Samaritans | Ireland | 116 123 | Read This First, bullet 2 | VERIFIED | Same URL — "branches and locations across the UK and Ireland". samaritans.ie was not fetched. |
| Lifeline | Australia | 13 11 14 | Read This First, bullet 2 | VERIFIED | https://www.lifeline.org.au/ — 13 11 14. The site also lists text 0477 13 11 14 and 24/7 chat, which are not printed. |
| Find A Helpline | International | findahelpline.com (website) | Front matter l.19; Read This First, bullet 2 | VERIFIED | https://findahelpline.com/ — "Helplines & hotlines by country", free and confidential. |

The generic "local emergency number" (front matter l.19; Appendix C4 step 5) is not a verifiable entry and is left out of the table.

## PHQ-9 and safety plan audit

**PHQ-9**
- Where it appears: Chapter 00, Set a Baseline (l.175) and Notes [0] (Kroenke, Spitzer & Williams 2001, *J Gen Intern Med* 16(9):606–613). Nowhere else. It is not in the Appendix C2 tracker, the Appendix A plan or the Chapter 10 maintenance section.
- Framing: "a signal for a conversation with a professional, not as a diagnosis you give yourself" holds. No sentence anywhere implies self-diagnosis. No cut-offs or severity bands are printed, which is correct for this framing.
- The Chapter 00 escalation row (l.184) mirrors the duration and impairment language of diagnostic criteria. It is framed as a prompt to book an appointment, not as a diagnosis. Acceptable.
- Gap (blocker): item 9 asks about thoughts of being better off dead or of self-harm, and there is no routing for a positive answer. A reader told to self-administer every two weeks needs one line: any positive response on that item goes to Read This First today, whatever the total score.
- Minor: there is no instruction on what to do with the scores except "a conversation". Consider "bring your scores to the appointment" and cross-reference Appendix D's "Bring the Paperwork".

**Safety plan (Appendix C4) against the required domains**

| Required domain | C4 step | Status |
| :--- | :--- | :--- |
| Warning signs | 1 | Present |
| Internal coping | 2 | Present |
| Social contacts and distracting settings | 3 | Present. The distraction purpose is softened to "feel less alone", and there is no names/numbers prompt. |
| Family and friends who can help | 4 | Present, with a names/numbers prompt |
| Professionals and agencies | 5 | Present as a fill-in. No urgent care / emergency department location prompt and no pre-printed numbers. |
| Means restriction | 6 | Present but generic ("what I will put out of reach"). No prompt for specific methods such as stored medication. |
| Environment safety | 6 (merged) | Partial. Merged with means restriction. There is no prompt for wider environment safety, such as not being alone or avoiding alcohol. |
| (Optional) Reason for living | 7 | Present |

Structural problems:
- (a) No instruction to work through the steps in order and move to the next if one does not help. This is central to how the Stanley-Brown plan works. Major.
- (b) The "keep it on your phone" instruction conflicts with the digital fields being cleared. Major.
- (c) The plan is reached only from Read This First. It is not scheduled in Appendix A and not linked from Chapter 00 or Chapter 10. Minor.
- (d) Confirm whether the adaptation of the copyrighted template needs rights-holder permission. Minor.

**"When Not to Use This" coverage (Chapters 01, 02, 04–08)**

| Chapter | Box present? | Genuine risk covered by absence? |
| :--- | :--- | :--- |
| 01 | Absent | No. Open item. |
| 02 | Absent | Yes. Bipolar or hypomanic risk when activity increases, and mood worsening while logging. |
| 04 | Absent | Yes. Safety-critical work; OCD-type checking. |
| 05 | Absent | Yes. Panic and trauma with the body-focused step. |
| 06 | Absent | No. Open item. |
| 07 | Absent | Yes. Suicidal ideation, obsessions and trauma intrusions handled by postponement. |
| 08 | Absent (the escalation paragraph partly covers it) | Low. Open item. |

For reference outside the checklist: Chapter 03 has an inline "When not to use this" paragraph, not a box. It covers accurate thoughts only and does not cover suicidal thoughts. Chapter 09 has a self-harm redirect at the top, which is not a box.

## Scope of practice findings

1. **Chapter 00, medication (l.158).** Within scope and correctly worded. No finding.
2. **Chapter 00, Check the Body First (l.150–156).** Framed as "ask a doctor". Within scope.
3. **Chapter 00, ADHD and Bipolar (l.162–164).** Framed as prompts to seek assessment, not as diagnoses. The bipolar advice ("keep sleep and routine regular… increase activity with professional guidance") gives a behavioural instruction based on self-identification. It is conservative and acceptable, but needs repeating where activity increases.
4. **Chapter 01 (l.225).** A treatment-equivalence claim that goes beyond the evidence. The trials cited tested therapist-delivered BA. "Considerably simpler to run yourself" is not supported by them. Reword, or cite the self-help evidence ([I], Cuijpers 2010) and note that it concerns guided self-help.
5. **Chapter 07 (l.590).** "It isn't a problem, it's a mood, and moods respond to activity, not analysis" functions as a diagnostic classification of the reader's thoughts. Overreach without exclusions.
6. **Chapter 08 (l.634).** "Wait it out" for a low-mood stretch. Borderline. The escalation line that follows mitigates it.
7. **Appendix D, Medication (l.874).** Accurate and non-directive. No finding.
8. **Appendix D (l.881).** "If one doesn't, that tells you something too" can be read as encouraging readers to leave care. Suggest adding "raise it, or ask for a second opinion" rather than leaving it implied.
9. **Health notice (l.17) vs Closing Note (l.945).** "Does not treat" vs "can't treat on its own". Harmonise the two.
10. **Chapter 03 (l.337) and Closing Note (l.949).** Absolute efficacy claims: "positive thinking… doesn't work" and "procedures work whether or not you're convinced". Low harm; soften them.

No passage tells a reader to stop or change their current care.

## Release recommendation

**CONDITIONAL**

Conditions:
1. Add PHQ-9 item 9 routing to Chapter 00, Set a Baseline.
2. The publisher must verify, against official sources, US 911, Canada 911, India 112, Australia 000 and UAE 999/998, and name the 988 services in the text.
3. Add "if you have already harmed yourself or taken something" to Read This First.
4. Fix the C4 persistence conflict: warn that digital entries are lost, and tell readers to copy the plan to paper or their own notes app.
5. Add the sequential-use instruction to C4, and make step 6 prompt for specific means.
6. Reprint the crisis numbers (or the Read This First summary) in Appendix B and Appendix C4.
7. Add exclusions for suicidal or death-related content to Chapter 03 (thought record) and Chapter 07 (go concrete; postponement).
8. Repeat the bipolar caution in Chapter 02 Stage 3 and Appendix A Week 3.
9. Clarify the Triage row "The voice in my head is vicious" and the opening of Chapter 09 to separate the inner critic from hearing voices.
10. Add a distress stop rule to the exercises in Chapters 03, 05, 07 and 09, and a "do not do this alone" line to Chapter 09 for trauma-linked self-criticism.

Open items (not conditions): "When Not to Use This" boxes for Chapters 01, 06 and 08; scheduling the Safety Plan in Appendix A; widening the Chapter 03 examples; confirming permission for the Stanley-Brown adaptation.

Sources:
- [988 Lifeline](https://988lifeline.org/)
- [9-8-8 Canada](https://988.ca/)
- [Samaritans — Contact](https://www.samaritans.org/how-we-can-help/contact-samaritan/)
- [Lifeline Australia](https://www.lifeline.org.au/)
- [Find A Helpline](https://findahelpline.com/)
- [European Commission — 112](https://digital-strategy.ec.europa.eu/en/policies/112)
- [NHS — When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/)
- [New Brunswick — 911](https://www.gnb.ca/en/topic/laws-safety/community-safety/911.html)
- Search results only, not counted as verification: [911.gov Calling 911](https://www.911.gov/calling-911/), [FCC 911](https://www.fcc.gov/general/9-1-1-and-e9-1-1-services), [CRTC 9-1-1](https://crtc.gc.ca/eng/phone/911/can.htm), [MHA ERSS](https://www.mha.gov.in/en/commoncontent/emergency-response-support-system-erss), [112.gov.in](https://112.gov.in/), [UAE MOI Emergency](https://moi.gov.ae/en/about.moi/content/emergency.contact.aspx), [TAMM Abu Dhabi](https://www.tamm.abudhabi/en/emergency-numbers)
