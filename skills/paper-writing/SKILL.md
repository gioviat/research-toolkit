---
name: paper-writing
description: Use when structuring or drafting a paper or assembling sections into a submission. Trigger on "write the paper", "draft the intro", "draft the abstract", "related work section", "structure the paper". The scientific-prose skill governs the sentence level and applies simultaneously.
---

# Paper writing

Structure-level rules; scientific-prose covers the sentence level. 

## Structure 
A paper should be self-contained, well organized and with a clear structure. Use the template below as a guide. Don't follow it blindly: it is a general guide rather than a strict constraint. Maintain the structure, but adapt each section to the specific content if it helps in conveying the idea without sacrificing rigor. If something cannot be satisfied for a specific paper, just skip it. 

### Abstract 
The abstract is a short, standalone summary of the paper, typically around 250 words. It must concisely convey: 
- **Context:** the general domain or problem
- **Gap:** specific limitations in existing work
- **Method:** The proposed approach to solve the problem 
- **Results:** The primary empirical and/or theoretical findings
- **Impacts:** Why this results matter to the field

### Introduction 
The introduction serves as the narrative foundation of the paper. It should convince the reader that the problem is significant and the proposed solution is sound, while maintaining scientific rigor and objectivity. 
- **Motivation:** establish the problem setting and why it is challenging
- **Existing limitations:** briefly highlight why current state-of-the-art method fall short 
- **Proposed approach:** provide a high-level overview of your method, without excessive notation 
- **Explicit contributions:** conclude the introduction with a bulleted list of 3-4 specific, verifiable contributions (e.g. a new theoretical bound, a novel architecture, or a definitive empirical benchmark). Make sure the contributions are supported by the rest of the paper, and perfectly match the results described later. 

### Related work
This section gives context to the contribution withing the broader literature. It is not a chronological list of paper, but a thematic categorization. 
- Group related papers by methodology or problem setting
- Explicitly contrast the proposed work with the closest existing baselines, highlighting structural, theoretical, or empirical differences. 

### Methodology / Approach
The technical core of the paper. It must mathematically rigorous and self-contained. 
- **Problem formulation:** when appliable, define the mathematical setting, objective function, and notation. For more empirical works, describe the setting, why it is interesting, and what is our goal. 
- **Proposed method:** detail the algorithm, architecture, or theoretical framework. 
- **Theoretical guarantees (if applicable):** present formalized definitions, lemmas, and theorems. If necessary, provide only brief proof sketches here, and defer full proofs to the appendix. 

### Experiments 
The experimental section must provide empirical validation of the claims made in the introduction. Every experiment should serve a specific purpose. 
- **Experimental setup:** specify datasets, evaluation metrics, and baseline methods
- **Main results:** present quantitative results using tables or figures. Highlight where the proposed method outperforms baselines and where it does not. 
- **Ablation studies:** isolate individual components of the proposed method to demonstrate that each part is necessary for the final performance. 
- **Computational cost:** report training time, memory footprint, and hardware requirements to ensure reproducibility. 

### Conclusions and Limitations
Summarize the main takeaways. Don't limit to repeat the abstract.
- **Summary:** briefly restate the core contribution
- **Limitations:** honestly discuss assumptions, edge cases, or scenarios where the method fails.

### References
Provide comprehensive and accurate citations. Use consistent formatting, e.g. resolving arXiv preprints to their formal conference or journal publications when available. 

### Appendix / Supplementary Material
The appendix is unlimited in lenght and used for content that disrupts the flow of the main narrative. 
- **Mathematical proofs:** complete derivations of all theorem stated in the main text 
- **Implementation details:** exact hyperparameter configurations, network architectures, data processing steps, and hardware specifications. 
- **Extended results:** Additional tables, visual samples, or exploratory experiments that support the main claims. 


## Claims and evidence
- Every contribution listed in the introduction maps to specific evidence in the paper: a theorem, a table, a figure. Write the pointer next to each contribution while drafting; a contribution without one gets cut or downgraded.
- The introduction claims nothing stronger than what the results section states. After drafting, check each introduction claim against the results text, not against what the results were hoped to be.
- Limitations state the actual bounds on the claims — sample sizes, compute, dataset scope, proof assumptions — not token caveats.

## Section-specific rules
- **Abstract**: written last. It states what was found, with numbers, not what was attempted or why the area matters.
- **Related work**: positions the contribution — for each cluster of prior work, what this paper does that it doesn't and why the difference matters. A list of citations with one-line summaries is not a related-work section.
- **Methodology / Approach**: checked by the theory-checker agent before submission, not after.
- **Experiments**: follow the results-reporting skill (variation, statistical tests, traceable numbers).

## LaTeX and citations
- Every `\cite` key exists in the `.bib` file. Compile and check the log for undefined citations and references before calling a draft done (`latexmk`, or `pdflatex` + grep the log for "undefined").
- Every `.bib` entry is verified against the real paper (title, authors, venue, year) by fetching its record, never written from memory. Fabricated bibtex is the writing equivalent of an untraceable number.
- Notation matches `papers/notation.md`; each macro is defined once.

## Final pass, in order
1. theory-checker on any math.
2. stats-auditor on every number.
3. prose-editor for style.
4. Clean compile with no undefined references.
