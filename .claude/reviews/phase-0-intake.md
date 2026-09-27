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
