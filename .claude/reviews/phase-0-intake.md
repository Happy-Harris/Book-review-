# Phase 0 — Intake and Verification Gate

**Source:** `Tools_Not_Theory___Revised_Publication_Edition.pdf` (uploaded by the author, 2026-09-27)
**Local copies (not committed):** `.claude/context/manuscript.pdf`, `.claude/context/manuscript.txt` (text extracted page by page)

## Read status

- **Read in full:** yes. All 52 PDF pages yielded text; none blank. Pages checked visually as well: front matter (1–8) and the diagram pages (12–13, 34–35).
- **Extraction warnings:** two broken internal PDF object references (objects 72 and 202). No text was lost. Every page extracted and matches its rendered image.
- **Diagrams:** the Ch 01 loop and the Ch 08 missed-day flow are drawn shapes, not images. Their labels survive in the text copy, but the arrows do not. Readers should open the PDF for those two pages.
- **Word count:** 9,283 words, excluding page markers.
- **Chapter count:** 11 numbered chapters (00–10), in four Parts.

## Structure checklist

| Item | Status | Where |
|---|---|---|
| Read This First (crisis box) | Present | PDF p. 2 |
| Orientation — Introduction: How to Use This | Present | pp. 5–6 |
| Orientation — Triage: Find Your Chapter | Present | p. 7 |
| Chapters 00–10 | All present | pp. 8–41 |
| Appendix A — The Six-Week Plan | Present | p. 42 |
| Appendix B — Quick Reference | Present | pp. 43–44 |
| Appendix C — Worksheets (C1–C4, C4 = Safety Plan) | Present | pp. 45–47 |
| Appendix D — Working With a Professional | Present | p. 48 |
| Notes; Closing Note | Present | pp. 49–52 |
| Truncated, missing or unreadable sections | None found | — |

## Items the author asked to check

| Check | Result |
|---|---|
| Chapter 03: four worked examples | **Not present.** Chapter 03 has **two**: "Worked Example One — The Author's Own" and "Worked Example Two — A Common One". |
| "When Not to Use This" boxes in Ch 01, 02, 04–08 | **Not present in any of them.** The only one in the book is in **Chapter 03**. Some chapters have related material in other forms: an escalation-line callout in Ch 08, a self-harm redirect at the top of Ch 09, and a bipolar caution in Ch 00. None is headed "When Not to Use This". |
| One-page Visual Integration Map at the front | **Not present.** The front matter runs cover → copyright → Read This First → Contents → Introduction → Triage table. The Triage table routes readers to chapters but is not a visual map. |

## Mismatches between the brief and the manuscript

1. **Crisis resources are not in Appendix D.** Reader 4's checklist says "Crisis resources (Appendix D)". In this edition, Appendix D is "Working With a Professional" and lists no helplines. The crisis numbers are in **Read This First (p. 2)**, with a findahelpline.com fallback on the copyright page (p. 1). The Safety Plan (C4) asks readers to fill in their own crisis contacts.
2. **Targeted question 1 assumes four Chapter 03 examples.** Only two exist.

## Web tools (needed for Reader 4's crisis audit)

- **WebFetch:** available and working. A test fetch of 988lifeline.org returned the service's own contact options.
- **WebSearch:** available and working. A test search returned samaritans.org pages.
- **Caveats:**
  - WebSearch is US-only, so results for non-US services may be thinner.
  - WebFetch returns a small model's summary of the page, not the raw page.

  So a `VERIFIED` status means "the service's own site, as read by a model, matched". It still needs the human check the brief already requires.

## Gate result

The document is complete and readable. **Three expected items are absent:** two of the four Ch 03 worked examples, the "When Not to Use This" boxes in Ch 01, 02 and 04–08, and the Visual Integration Map. Crisis resources are also located somewhere other than the brief assumes. Phase 2 is on hold per the author's instruction.

---

## Addendum — version check (2026-09-27)

**Is the reviewed PDF the amended draft? No.** The PDF has neither amendment:

| Amendment | In the PDF? | In `Revised Sections (Orientation + Chapter 03).md`? |
|---|---|---|
| Orientation, Operating Rule 2: voice-memo / dictation sentence | No. Rule 2 ends at "it isn't just a record of it." | Yes |
| Chapter 03, Worked Examples Three and Four | No. Only One and Two. | Yes: Three (domestic accumulation), Four (administrative debt) |
| Chapter 03 closing line, "in both examples" → "across all four examples" | No. The PDF says "in both examples". | Yes |

Word-level comparison of the two sections, ignoring punctuation and markdown formatting, found one other difference:

- The revised Orientation has **no citation marker** after "…better with some professional support than without it." The PDF has `[i]`, which points to the Cuijpers et al. (2010) entry in Notes. Either this was intended or it was lost in the move to markdown. The author should check.

The rest of both sections is word-for-word the same as the PDF.

**The revised-sections file is not a full draft.** It has Orientation and Chapter 03 only (1,612 words). Phase 0 cannot pass on it. It is not being spliced into the PDF text, because building a manuscript is the author's job, not the reviewer's. **Phase 0 must be re-run against a complete amended draft.**

## Carry-forward for the Phase 2 session

These were decided by the author and must be applied in the next session:

1. **Re-run Phase 0** against the complete amended draft. Confirm that both amendments above are present before going any further.
2. **Then amend Reader 4's brief** (`.claude/agents/reader-4-clinician.md`). It currently audits crisis resources in "Appendix D" only. Change it to audit crisis resources **wherever they appear in the manuscript**, and require Reader 4 to **list which locations it audited**. Do not make this change before the correct draft is confirmed.
3. **Log that amendment** in `.claude/reviews/consolidated-report.md`: what changed, why (Appendix D holds no crisis resources in this edition), and when.
4. `.claude/context/` stays gitignored. The author re-uploads the manuscript each session.
5. Dispatch readers by name from a fresh session, so each agent's tool list is enforced.

---

## Phase 0 re-run — complete amended draft (2026-09-27)

**Source:** `Tools, Not Theory - Complete Manuscript.md` (uploaded by the author, 2026-09-27)
**Local copy (not committed):** `.claude/context/manuscript.md`, SHA-256 `6961514b…7fdceaf41`. This is the path to give the readers.

### Read status

- **Read in full:** yes. The file is 958 lines of Markdown (the last line has no trailing newline) and nothing is truncated. It ends with the closing colophon.
- **Word count:** 9,663 words with the Markdown syntax removed. The PDF had 9,283. The difference is mostly Examples Three and Four in Ch 03.
- **Chapter count:** 11 numbered chapters (00–10) in four Parts, the same as the PDF.
- **Format:** this is Markdown, not a laid-out PDF. Readers will see these rendering details:
  - The **Ch 01 loop** is one line of text with `->` arrows. It does not show the loop closing back on itself. The caption underneath ("The loop runs on its own") does the work.
  - The **Ch 08 missed-day flow** is box-drawing text in a code block. It reads correctly in a monospace font but may wrap on a narrow screen.
  - The **Ch 02 field sheet** labels use LaTeX (`$(P\ge4)$`, `$(A\ge4)$`). A viewer that doesn't render maths shows the raw source.
  - The **Appendix C4** table uses `<br>` inside cells.

### Amendment check

| Amendment | In this draft? | Where |
|---|---|---|
| Orientation, Operating Rule 2: voice-memo / dictation sentence | **Yes** | Introduction, Three Operating Rules, rule 2 |
| Chapter 03, Worked Example Three (domestic accumulation) | **Yes** | Ch 03, The Thought Record |
| Chapter 03, Worked Example Four (administrative debt) | **Yes** | Ch 03, The Thought Record |
| Ch 03 closing line: "across all four examples" | **Yes** | "The shape is identical across all four examples." |
| Citation marker after "…better with some professional support than without it." (flagged as possibly lost) | **Restored** as `[I]` | Introduction, "What this is not". It matches the `INTRODUCTION [I]` heading in Notes. |

Both amendments are present and the missing citation question is settled.

### Structure checklist

| Item | Status |
|---|---|
| Read This First (crisis box) | Present |
| Orientation: Introduction and Triage | Present |
| Chapters 00–10 | All present |
| Appendices A–D, Notes, Closing Note | All present |
| Citation markers | Every marker used in the text (`[I]`, `[0]`–`[10]`, `[C]`) has a matching Notes entry, and every Notes entry is cited |
| Truncated, missing or unreadable sections | None found |

**New front matter not recorded in the PDF intake:** a Health notice, a Privacy note (the worksheet fields save nothing), and a Composite examples note. The composite note says every example except Ch 03's first is a composite, which is consistent with the four examples. I can't say whether these were in the PDF, because the PDF copy was not kept between sessions.

### Items the author asked to check (status now)

| Check | Result |
|---|---|
| Chapter 03: four worked examples | **Present:** One (the author's own), Two (job applications), Three (domestic accumulation), Four (administrative debt). |
| "When Not to Use This" boxes in Ch 01, 02, 04–08 | **Still not present.** The only one is in Ch 03, and it is now a plain paragraph that starts "When not to use this." rather than a headed box. Related material is still where it was: the escalation line in Ch 08, the self-harm redirect at the top of Ch 09, and the bipolar caution in Ch 00. Reader 4 already treats this as an open item. |
| One-page Visual Integration Map at the front | **Still not present.** The Triage table is the only routing device. |

### Where crisis resources appear in this draft

This list is for Reader 4's widened audit (see below).

| Location | What is there |
|---|---|
| Copyright page | Note that resources were current at publication. Fallback: local emergency number or findahelpline.com |
| Read This First | Emergency numbers (US/Canada 911, UK 999, EU and India 112, Australia 000, UAE 999, with 998 for an ambulance) and helplines (988 US/Canada; Samaritans 116 123 UK and Ireland; Lifeline 13 11 14 Australia; findahelpline.com elsewhere) |
| Introduction, Who This Is For | Crisis readers are routed to Ch 00 |
| Triage | "I'm not sure I'm safe" → Read This First |
| Ch 00, Decide Now (escalation table) | Thoughts of death, suicide or self-harm → Read This First |
| Ch 09, opening | Self-harm redirect → Read This First |
| Appendix B, first row | Thoughts of harming yourself → Read This First; contact a person or service |
| Appendix C4, Safety Plan step 5 | The reader fills in their own professionals and crisis lines |
| Appendix D | **No crisis resources**, as in the PDF |

These numbers have **not** been verified here. Verification is Reader 4's job.

### Other observations (not blockers; for the author)

- **ISBN check digit.** `979-8-89214-000-0` fails the ISBN-13 checksum. For these first twelve digits the check digit would be 3. If this is a placeholder, ignore this.
- **Naming.** The Composite examples note says "Chapter 3". Everywhere else the book says "Chapter 03".

### Gate result (re-run)

**PASS.** The draft is complete and readable, and both amendments are confirmed. Two items are still absent: the "When Not to Use This" boxes in Ch 01, 02 and 04–08, and the Visual Integration Map. Reader 4's brief already treats the boxes as an open item. Targeted question 1 (four Ch 03 examples) now matches the manuscript.

### Carry-forward status

1. Re-run Phase 0 against the complete amended draft: **done**. See above.
2. Amend Reader 4's brief to audit crisis resources wherever they appear and to list the locations it audited: **done**.
3. Log that amendment in `.claude/reviews/consolidated-report.md`: **done**.
4. `.claude/context/` stays gitignored: **confirmed**. The manuscript copy is local only.
5. Dispatch readers by name, with Reader 4 first: **done** (2026-09-27). Reports and the Phase 3 consolidation are in `.claude/reviews/`.
