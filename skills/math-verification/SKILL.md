---
name: math-verification
description: Use whenever asked to check, verify, derive, or re-derive a mathematical claim, proof, bound, or formula, including checking someone else's derivation, checking a step in a paper draft, or verifying that code implements a formula correctly. Trigger on words like "verify", "check the proof", "derive", "is this bound correct", "does this match the formula".
---

# Math verification

## Before checking anything
- Restate every assumption the claim depends on, explicitly, in your own words. If an assumption is implicit in the source material, name it.
- State the claim itself in a form precise enough that "true" or "false" is unambiguous. If the claim as given is ambiguous, say so and verify the most natural reading, flagging the ambiguity.
- Check that all symbols match the project's canonical notation (papers/notation.md). Flag any symbol used inconsistently with that file.

## Verification order (cheapest checks first)
1. Dimensional / type consistency: do units, shapes, or types match on both sides?
2. Boundary and limiting cases: does the claim reduce to a known result at an edge case (n=1, t=0, d→∞, etc.)?
3. A small numeric or symbolic example, computed independently (SymPy, a script, or a proof assistant where applicable) — not by re-reading the existing derivation and agreeing with it.
4. Full independent re-derivation of the result, without looking at the given derivation step-by-step. Only after finishing, compare against the original to see where they diverge.

## Rules
- Never state that a derivation is correct because it "looks standard" or "follows the usual pattern." Redo the steps.
- If a step cannot be verified with available tools (e.g., it requires a proof assistant you don't have, or relies on an unavailable reference), say exactly that: "unverified — requires X." Never round this up to "likely correct."
- If you find an error, state the exact line/step where it occurs and what the correct expression should be, rather than a general "there may be an issue here."
- Distinguish clearly between "I verified this is correct," "I verified this is incorrect," and "I could not verify this."

## Output format
For each claim checked, report:
- Claim (restated precisely)
- Assumptions used
- Method of verification (dimensional check / limiting case / independent derivation / symbolic computation)
- Verdict: correct / incorrect / unverified, with the specific reason
