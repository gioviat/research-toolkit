#!/usr/bin/env python3
"""
PostToolUse hook for Write|Edit on drafts under reports/ and papers/ (.md, .tex).
Heuristic tripwire (the stats-auditor agent is the authoritative check):
- Flags numeric-looking claims that don't appear in any file under the results
  directory: $CHECK_CLAIMS_RESULTS_DIR if set, else experiments/results/ and results/.
- Flags banned AI-writing phrases from the scientific-prose skill.
Numbers that read as scholarly cross-references (eq. 3.4, §2.1, bare "(3.7)",
"\\tag{3.11}", arXiv ids, version numbers) are skipped, not traced.
Extra trace-exempt paths (e.g. a proposal quoting literature values) can be added
via $CHECK_CLAIMS_TRACE_EXEMPT, colon-separated.
Warns via systemMessage (user) and additionalContext (Claude); does not block,
since the heuristic has false positives (e.g. hyperparameters quoted for context).
"""
import json
import os
import re
import sys
from pathlib import Path

BANNED_PHRASES = [
    "it is important to note",
    "it's worth noting",
    "delve into",
    "leverage",
    "multifaceted",
    "tapestry",
    "testament to",
    "in conclusion, it is clear",
]

# Paths whose numbers legitimately come from outside the results directory
# (literature surveys quote other papers' results; notation.md defines constants).
TRACE_EXEMPT = ("papers/related-work/", "papers/notation.md")

# A number preceded by one of these reads as a cross-reference, not a measurement.
REF_CONTEXT = re.compile(
    r"(?:\b(?:eq|eqs|equation|equations|sec|secs|section|sections|prop|proposition|"
    r"thm|theorem|lemma|def|definition|claim|fig|figs|figure|table|alg|algorithm|"
    r"chapter|part|phase|recommendation|version|v|python)|§)[.\s~(]*$",
    re.IGNORECASE,
)
ARXIV_ID = re.compile(r"^\d{4}\.\d{4,5}$")


def results_dirs():
    env = os.environ.get("CHECK_CLAIMS_RESULTS_DIR")
    if env:
        return [Path(env)]
    return [Path("experiments/results"), Path("results")]


def trace_exempt_paths():
    extra = os.environ.get("CHECK_CLAIMS_TRACE_EXEMPT", "")
    return TRACE_EXEMPT + tuple(p for p in extra.split(":") if p)


def is_draft(path: str) -> bool:
    p = path.replace("\\", "/")
    return p.endswith((".md", ".tex")) and ("reports/" in p or "papers/" in p)


def load_results_text() -> str:
    chunks = []
    for d in results_dirs():
        if not d.exists():
            continue
        for p in d.rglob("*"):
            if p.is_file():
                try:
                    chunks.append(p.read_text(errors="ignore"))
                except OSError:
                    pass
    return "\n".join(chunks)


def is_reference_like(draft: str, m: re.Match) -> bool:
    n = m.group(0)
    if n.endswith("%"):
        return False  # a percentage is always a value
    if ARXIV_ID.match(n):
        return True
    if REF_CONTEXT.search(draft[max(0, m.start() - 20):m.start()]):
        return True
    prev = draft[m.start() - 1] if m.start() > 0 else ""
    nxt = draft[m.end()] if m.end() < len(draft) else ""
    if prev == "{" or nxt == "}":  # \tag{3.11}, \eqref{eq:3.4}
        return True
    if prev == "(" and nxt in ")$'′":  # bare "(3.7)" or "(3.9$'$)" is an equation ref
        return True
    return False


def main() -> int:
    payload = json.load(sys.stdin)
    file_path = payload.get("tool_input", {}).get("file_path", "")
    if not is_draft(file_path):
        return 0

    try:
        draft = Path(file_path).read_text()
    except OSError:
        return 0

    warnings = []

    lower = draft.lower()
    for phrase in BANNED_PHRASES:
        if phrase in lower:
            warnings.append(f"banned phrase found: '{phrase}'")

    norm = file_path.replace("\\", "/")
    if not any(part in norm for part in trace_exempt_paths()):
        results_text = load_results_text()
        flagged = set()
        for m in re.finditer(r"\b\d+\.\d+%?\b", draft):
            n = m.group(0)
            if n in flagged or n in results_text or is_reference_like(draft, m):
                continue
            flagged.add(n)
        for n in sorted(flagged):
            warnings.append(f"number '{n}' not found verbatim in the results directory — verify it traces to a source file")

    if warnings:
        msg = "check-claims hook: " + "; ".join(warnings)
        print(json.dumps({
            "systemMessage": msg,
            "hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "additionalContext": (
                    msg
                    + ". Heuristic tripwire (see results-reporting and scientific-prose skills):"
                    " fix the draft or state why each flagged item is correct;"
                    " the stats-auditor agent is the authoritative check."
                ),
            },
        }))
    return 0


if __name__ == "__main__":
    sys.exit(main())
