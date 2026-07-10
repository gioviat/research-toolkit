---
name: scientific-prose
description: Use whenever drafting or editing prose for a paper, report, README, or any written explanation of methods or results. Trigger on "write up", "draft the section", "explain this in the report", "polish this paragraph".
---

# Scientific prose

## Banned patterns
- Em dashes (—) and en dashes (–): em dashes are clear signs of AI writing, so remove them and replace them with more natural alternatives, like periods or commas. If not possible, restructure the sentence. This is a hard constraint. 
- Throat-clearing openers: "It is important to note that...", "It's worth mentioning..."
- Unearned transitions: "Moreover", "Furthermore", "Additionally" used as connective filler rather than because the next sentence needs that specific logical relation
- Preview sentences: "In this section, we will discuss..." — state the content directly instead
- Inflated vocabulary where a plain word means the same thing: "delve", "leverage", "robust", "multifaceted", "testament", "tapestry", "comprehensive" (as a filler adjective), "utilize" (use "use"), "load-bearing", "align with", "crucial", "emphasizing", "highlight" (verb),   
- Manufactured rule-of-three lists and uniform sentence length — vary structure the way a written derivation or argument naturally does
- Hedge words used to avoid a claim rather than to state genuine uncertainty: "may", "could potentially", "generally speaking" — either state the result or state precisely what is uncertain and why
- Generic conclusions: "This shows the importance of X" — end on the specific finding, not a platitude
- Unnecessary comparisons: "We do X rather than Y", "It is X, not Y", "What it does, what it does not". If there is no need for a direct comparison, avoid it: just state plainly the central idea. 

## Positive requirements
- One claim per sentence where possible; short sentences for results, longer sentences only where the logical structure requires subordination
- State a position where the evidence supports one. Genuine open questions are marked as open questions, not smoothed into false balance
- Define every symbol at first use; keep notation consistent with papers/notation.md
- Prefer active voice and a named subject ("We measured X" / "The model achieves Y") over passive constructions that hide who did what
- When citing related work, state what it found precisely enough to be checked, not just "prior work has shown..."

## Self-check before finalizing a draft
- Read it aloud (mentally). Any sentence that wouldn't be said aloud by a careful colleague needs rewriting.
- Could any sentence be deleted without losing information? If yes, delete it.
- Does every paragraph contain at least one piece of information not stated elsewhere in the document?



---
name: scientific-prose
description: Use whenever drafting or editing prose for a paper, report, README, or any written explanation of methods or results. Trigger on "write up", "draft the section", "explain this in the report", "polish this paragraph".
---

# Scientific prose

## Banned patterns
- Em dashes (—) and en dashes (–): em dashes are clear signs of AI writing, so remove them and replace them with more natural alternatives, like periods or commas. If not possible, restructure the sentence. This is a hard constraint. 
- Throat-clearing openers: "It is important to note that...", "It's worth mentioning..."
- Unearned transitions: "Moreover", "Furthermore", "Additionally" used as connective filler rather than because the next sentence needs that specific logical relation
- Preview sentences: "In this section, we will discuss...". State the content directly instead.
- Inflated vocabulary where a plain word means the same thing: "delve", "leverage", "robust", "multifaceted", "testament", "tapestry", "comprehensive" (as a filler adjective), "utilize" (use "use"), "load-bearing", "align with", "crucial", "emphasizing", "highlight" (verb). Additional AI-frequent terms to eliminate: "actually", "interplay", "intricacies", "landscape", "fostering", and "garner". 
- Manufactured rule-of-three lists and uniform sentence length: vary structure the way a written derivation or argument naturally does
- Hedge words used to avoid a claim rather than to state genuine uncertainty: "may", "could potentially", "generally speaking": either state the result or state precisely what is uncertain and why
- Generic conclusions: "This shows the importance of X" — end on the specific finding, not a platitude
- Unnecessary comparisons: "We do X rather than Y", "It is X, not Y", "What it does, what it does not". If there is no need for a direct comparison, avoid it: just state plainly the central idea. 
- Undue emphasis on significance and legacy: avoid framing standard methods or incremental results as a "pivotal moment" or "vital role". Avoid saying a development "marks a shift" or is "setting the stage for".
- Superficial analyses with "-ing" endings: avoid tacking present participle phrases onto sentences to add fake depth. An example of this is writing "achieving SOTA", "underscoring its efficiency".
- Promotional and advertisement-like language: avoid "groundbreaking", "renowned", or "boasts a" when describing architectures or experimental results.
- Vague attributions and weasel words: do not use "Experts argue", "Observers note", or "Industry reports". Ensure you attribute opinions or prior findings with specific sources.
- Outline-like boilerplate sections: avoid formulaic "Challenges and Future Prospects" structural framing in the discussion.
- Copula avoidance: do not substitute elaborate constructions like "serves as", "represents a", or "offers a" for simple verbs like "is" or "are".
- Negative parallelisms and tailing negations: avoid overused "Not only... but..." constructions. Do not use tacked-on fragments like "no guessing" in place of complete clauses.
- Elegant variation (synonym cycling): do not unnecessarily swap technical terms (e.g., cycling randomly through "model", "network", and "framework") just to avoid repetition.
- False ranges: avoid "from X to Y" constructions where X and Y are not placed on a meaningful scale.
- Signposting and announcements: omit meta-commentary like "Let's break this down" or "Here's what you need to know".
- Diff-anchored writing: describe the methodology or architecture as it currently is. Avoid narrating the process of changing it from a previous version unless explicitly writing a changelog.
- Aphorism formulas: avoid reducing rigorous technical claims into pseudo-profound formulas like "X is the Y of Z".

## Style and formatting patterns
- Overuse of boldface: do not mechanically emphasize phrases in boldface.
- Inline-header vertical lists: avoid lists where items start with bolded headers followed immediately by colons.
- Title case in headings: avoid capitalizing all main words in headings. Use sentence case.
- Hyphenated word pair overuse: drop hyphens in compound terms (e.g., "data-driven" or "real-time") when the compound follows the noun, such as "the approach is data driven". Keep hyphens only in attributive positions, such as "a data-driven approach".

## Positive requirements
- One claim per sentence where possible; short sentences for results, longer sentences only where the logical structure requires subordination
- State a position where the evidence supports one. Genuine open questions are marked as open questions, not smoothed into false balance
- Define every symbol at first use; keep notation consistent with papers/notation.md
- Prefer active voice and a named subject ("We measured X" / "The model achieves Y") over passive constructions that hide who did what
- When citing related work, state what it found precisely enough to be checked, not just "prior work has shown..."

## Self-check before finalizing a draft
- Read it aloud (mentally). Any sentence that wouldn't be said aloud by a careful colleague needs rewriting.
- Could any sentence be deleted without losing information? If yes, delete it.
- Does every paragraph contain at least one piece of information not stated elsewhere in the document?
- Are filler phrases minimized? Check that "In order to achieve this goal" is reduced to "To achieve this". Verify that "At this point in time" is reduced to "Now".