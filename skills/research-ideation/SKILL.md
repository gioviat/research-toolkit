---
name: research-ideation
description: Use when developing research ideas, generating candidate research questions, or evaluating whether an idea is worth pursuing. Trigger on "brainstorm research directions", "what should we try next", "is this idea worth pursuing", "research question", "next project".
---

# Research ideation

## Where ideas come from
Start from something concrete: an anomaly in your own results, a gap recorded in `papers/related-work/`, an assumption every existing method makes that might not be necessary, or a mismatch between theory and observed behavior. Not from "what's trendy".

## Procedure
1. Generate at least 3–5 candidate questions before evaluating any of them. Evaluating the first idea before alternatives exist anchors the session on it.
2. For each candidate, fill in every field below. A field that cannot be filled is itself a verdict on the candidate.
3. Rank the candidates and state plainly which are weak and why. Your own ideas get no false balance: if one candidate is clearly better, say so; if all are weak, say that.

## Required fields per candidate
- **Question**: falsifiable and specific. Not "can X help Y" but "does X improve metric M by an amount that matters under condition C".
- **Why it might be true, and why now**: the mechanism or observation suggesting it, and what changed (new data, tool, or result) that makes it tractable today.
- **Closest prior work**: found by actually searching (literature-review skill or literature-scout agent), never asserted from memory. State exactly how the candidate differs. "Nobody has done this" without a recorded search is not a novelty claim.
- **Cheapest decisive experiment**: the smallest experiment whose outcome would change your belief in the question. If the cheapest informative experiment is expensive, that is a cost of the idea — record it.
- **Kill criterion**: the result that would make you drop the idea, stated before running anything.
- **If true / if false**: what changes in either case. If nothing changes when false, the question may not be worth asking.

## Output
One doc per surviving candidate at `ideas/<slug>.md` with the fields above, plus the ranking rationale across candidates. Have the skeptical-reviewer agent review the doc before any implementation starts.
