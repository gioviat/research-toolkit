---
name: experiment-design
description: Use when designing a new experiment, planning an ablation, choosing baselines or metrics, or deciding how many seeds/runs are needed before any code is written. Trigger on "design an experiment", "how should I test", "what's the right baseline", "how many seeds".
---

# Experiment design

Before any implementation, produce a written design covering the items below. If an item cannot be satisfied given the project's constraints, say which one and why, rather than silently omitting it.

## Required before writing code
- **Hypothesis**: the specific, falsifiable claim being tested. Not "does X help" but "does X improve metric M by at least an amount that matters, under condition C."
- **Metric**: the exact formula, not just its name. State how it's computed, over what set, with what aggregation.
- **Baselines**: what the result is compared against, and why those are the right baselines (not just the most convenient ones).
- **Independent variables**: what is being varied; everything else must be held fixed and stated explicitly.
- **Seeds / repetitions**: minimum 3 seeds for any result that will be reported as a comparison; state the number and justify it if fewer.
- **Statistical test**: which test will be used to compare conditions (e.g., paired t-test, bootstrap CI, Wilcoxon), decided before seeing results — not chosen post hoc to fit the data.
- **Compute/data budget**: what's affordable, and whether it's sufficient to detect an effect of the size being claimed. If underpowered, say so up front.
- **Failure criteria**: what result would count as "the hypothesis is not supported." State this before running anything.

## During implementation and while running
- One directory per run under `experiments/results/<run-id>/`, holding the full configuration (all hyperparameters, seed, code version/commit) and the raw metrics. A result with no config attached cannot be reported.
- Write outputs only to `experiments/results/`, never edited by hand afterward.
- Launch long runs in the background and check them periodically rather than blocking on them.
- A run that crashed or turned out misconfigured is recorded with its config and failure, not deleted. Runs that silently disappear are a form of cherry-picking.

## Common design errors to check for explicitly
- Comparing against a weak or outdated baseline
- Metric that doesn't match the stated hypothesis
- Cherry-picking the seed or checkpoint with the best result
- Reporting a single run as if it were representative
- Choosing the statistical test after looking at the data
