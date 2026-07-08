# research-toolkit

A Claude Code plugin for ML research, covering the pipeline from idea to paper: literature review with verified citations, research ideation with kill criteria, independent math verification, pre-registered experiment design, results reporting where every number traces to a file, and clean scientific prose.

## Install

```
/plugin marketplace add gioviat/research-toolkit
/plugin install research-toolkit@research-toolkit
```

Restart the session afterward: agents, hooks, and the output style load at startup. The bundled `research` output style applies automatically while the plugin is enabled.

## Pipeline

Skills load automatically when the task matches their description; invoke one explicitly as `/research-toolkit:<name>`. Agents are invoked by name ("use the literature-scout agent to survey X").

**Survey the field**
- `literature-review` (skill): scope and inclusion criteria stated first; every citation verified by fetching its record, never from memory; output is a comparison table plus explicit gaps, saved to `papers/related-work/`.
- `literature-scout` (agent): runs the survey across arXiv, Semantic Scholar, web search, and snowballing, then reports its queries so coverage is auditable.

**Develop ideas**
- `research-ideation` (skill): several candidates before evaluating any; novelty checked against literature, not asserted; each idea gets a cheapest decisive experiment and a kill criterion, recorded in `ideas/<slug>.md`.
- `skeptical-reviewer` (agent): adversarial review of idea docs, experiment designs, and results drafts.

**Verify the math**
- `math-verification` (skill): restate assumptions, check dimensions and boundary cases, then re-derive independently before comparing.
- `theory-checker` (agent): verdict per claim, correct, incorrect, or unverified, never a general impression.

**Design and run experiments**
- `experiment-design` (skill): hypothesis, metric, baselines, seeds, and statistical test fixed before any code; one directory per run under `experiments/results/`; crashed runs recorded, not deleted.

**Report results**
- `results-reporting` (skill): every number read from a file, variation always reported, no causal language without a causal design, null results reported at full specificity.
- `stats-auditor` (agent): audits each numeric claim in a draft against `experiments/results/`; untraceable numbers block the draft.

**Write the paper**
- `paper-writing` (skill): each contribution mapped to a theorem, table, or figure; abstract written last; bibtex verified against the real papers; done means a clean LaTeX compile with no undefined references.
- `scientific-prose` (skill): sentence level, plain words, no filler transitions, no manufactured lists, no hedging in place of a claim.
- `prose-editor` (agent): final style pass, returning each change with the rule it enforces.

## Hook

A `PostToolUse` hook (`hooks/check-claims.py`) fires when a draft under `reports/` or `papers/` (`.md` or `.tex`) is written or edited. It flags numbers not found in `experiments/results/` and banned filler phrases, warning both you and Claude. It is a tripwire, not the authority: false positives are possible, and `stats-auditor` remains the real check. Literature surveys and `papers/notation.md` are exempt from number tracing, since their numbers come from published work.

## Project conventions

- `experiments/results/`: raw run outputs, one directory per run with config and seed; never hand-edited.
- `papers/notation.md`: canonical notation, one definition per symbol.
- `papers/related-work/`: saved literature surveys.
- `ideas/`: idea docs with novelty check, cheapest decisive experiment, and kill criterion.
- `reports/` and `papers/`: drafts, covered by the check-claims hook.

Adjust the paths in `hooks/check-claims.py` if your project differs.

## Editing

Everything is a markdown file with YAML frontmatter. The criteria are field-generic on purpose: which statistical tests are standard, which venues matter, and what counts as a strong baseline all vary by subfield. Tighten the relevant `SKILL.md` or agent file for yours.
