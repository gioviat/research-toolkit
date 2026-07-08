---
name: paper-writing
description: Use when structuring or drafting a paper — abstract, introduction, related work, contributions, limitations — or assembling sections into a submission. Trigger on "write the paper", "draft the intro", "draft the abstract", "related work section", "structure the paper". The scientific-prose skill governs the sentence level and applies simultaneously.
---

# Paper writing

Structure-level rules; scientific-prose covers the sentence level.

## Claims and evidence
- Every contribution listed in the introduction maps to specific evidence in the paper: a theorem, a table, a figure. Write the pointer next to each contribution while drafting; a contribution without one gets cut or downgraded.
- The introduction claims nothing stronger than what the results section states. After drafting, check each introduction claim against the results text, not against what the results were hoped to be.
- Limitations state the actual bounds on the claims — sample sizes, compute, dataset scope, proof assumptions — not token caveats.

## Section-specific rules
- **Abstract**: written last. It states what was found, with numbers, not what was attempted or why the area matters.
- **Related work**: positions the contribution — for each cluster of prior work, what this paper does that it doesn't and why the difference matters. A list of citations with one-line summaries is not a related-work section.
- **Results**: follow the results-reporting skill (variation, statistical tests, traceable numbers).
- **Derivations**: checked by the theory-checker agent before submission, not after.

## LaTeX and citations
- Every `\cite` key exists in the `.bib` file. Compile and check the log for undefined citations and references before calling a draft done (`latexmk`, or `pdflatex` + grep the log for "undefined").
- Every `.bib` entry is verified against the real paper — title, authors, venue, year — by fetching its record, never written from memory. Fabricated bibtex is the writing equivalent of an untraceable number.
- Notation matches `papers/notation.md`; each macro is defined once.

## Final pass, in order
1. theory-checker on any math.
2. stats-auditor on every number.
3. prose-editor for style.
4. Clean compile with no undefined references.
