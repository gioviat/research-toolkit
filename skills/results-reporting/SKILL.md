---
name: results-reporting
description: Use when writing up experimental results, a results section, a table of numbers, or any summary of what an experiment found. Trigger on "write up the results", "summarize the experiment", "draft the results section".
---

# Results reporting

## Non-negotiable rules
- Every number reported must be read from a file under `experiments/results/`. Never state a number from memory or by extrapolation. If the number isn't there, run the script that produces it, or say explicitly that it is missing.
- Every reported result includes: the metric definition, the number of seeds/runs, a measure of variation (std, CI, or range across seeds) — not a bare mean.
- State the statistical test used for any claim of one condition beating another, along with the test statistic or p-value / CI. "Significant" alone is not a result.
- Distinguish correlation from causation in wording. Do not use causal language ("X improves Y", "X causes Y") unless the experiment design supports a causal claim (controlled intervention, not observational comparison).
- Report negative and null results with the same specificity as positive ones. A hypothesis that was not supported is reported as such, not omitted or softened into "inconclusive."

## Structure for a results section
1. Restate the hypothesis and metric being evaluated.
2. Report the primary result with variation and statistical test.
3. Report relevant ablations/controls.
4. State limitations of the experiment as run (sample size, compute budget, scope of the claim) — not as a token caveat at the end, but as a real bound on what the result supports.
5. If the result differs from what related work would predict, say so explicitly rather than smoothing over the discrepancy.

## What not to do
- Do not round a "trend" into a "finding." If the effect is within the noise given the variation across seeds, say that plainly.
- Do not present a single anecdotal example as if it were the aggregate result.
- Do not omit failed configurations or runs that didn't work, if they are relevant to interpreting the reported result.
