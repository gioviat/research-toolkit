---
name: literature-review
description: Use when surveying the state of the art on a topic, gathering related work, checking whether an idea has already been done, or comparing existing methods. Trigger on "what's the SOTA", "survey the literature", "related work on", "has anyone done", "find papers on", "is this novel".
---

# Literature review

## Before searching
- State the exact question the survey answers: task, setting, constraints ("parameter-efficient finetuning of sub-1B LLMs", not "efficient finetuning").
- State the recency window and why (e.g. "2023 onward; earlier work covered by survey X").
- State the inclusion criteria, so omissions are auditable.

## Search procedure
1. Query multiple sources, not one: web search where available, plus direct API queries —
   - arXiv: `curl -sL "https://export.arxiv.org/api/query?search_query=all:%22<terms>%22&max_results=20"`
   - Semantic Scholar: `curl -s "https://api.semanticscholar.org/graph/v1/paper/search?query=<terms>&fields=title,year,venue,abstract,citationCount,externalIds"` — works without a key but rate-limits (HTTP 429); back off and retry, don't drop the source silently.
2. Use several distinct query formulations; different communities name the same idea differently.
3. Snowball: for the 2–3 most relevant papers found, follow their references and their citing papers (Semantic Scholar `/paper/<id>/references` and `/citations`).
4. Record every query run; the survey reports them so coverage can be audited.

## Citation rules (non-negotiable)
- Never cite from memory. A paper appears in the survey only after its record (arXiv page, Semantic Scholar entry, or venue page) was fetched in this session. A paper that is remembered but cannot be found is reported as "recalled but unverified", not cited.
- Report what each paper shows, not what it claims: the dataset, metric, and number from its experiments, precise enough to be checked.
- Mark each entry as peer-reviewed (with venue) or preprint.
- Do not rank results that are not comparable (different datasets, metrics, or compute); say why they aren't.

## Output
Save to `papers/related-work/<topic>.md`:
1. Question, scope, recency window, inclusion criteria.
2. Comparison table: method | venue+year (or preprint) | setting | metric | result | code available.
3. Gaps and open problems: what no surveyed paper addresses, stated specifically enough to seed a research question (input to the research-ideation skill).
4. Coverage limits: queries run, sources searched, where the survey may be incomplete.
