---
name: prd-reviewer
description: Reviews product requirement documents (PRDs) for completeness, clarity, and engineering readiness. Use when the user shares a PRD, spec, or feature brief and asks for feedback, a review, or whether it's "ready for eng."
---

# PRD Reviewer

## Goal
Give the PM a clear verdict (Ready / Needs work / Not ready) and specific,
actionable fixes. Be direct, and prioritize issues that would block engineering.

## Workflow
1. Save the PRD as a Markdown or text file if it isn't one already, then run:
   `python scripts/check_sections.py <path-to-prd>`
   It reports which required sections are missing or too thin, as JSON.
   Use `--json` for machine-readable output only.
   The script matches sections by heading name. Before you call a section
   missing, check its "unrecognized headings" list and read the PRD: the
   content may be there under a different heading.
2. Read `references/prd-standards.md` to judge the quality of each section.
3. Review in this order:
   - **Problem:** Is the user problem clear, with evidence (data, research, quotes)?
   - **Success metrics:** Are they measurable, with a baseline and target?
   - **Scope:** Are non-goals explicit? Is v1 clearly separated from later phases?
   - **Requirements:** Are they testable? Are edge cases and error states covered?
   - **Risks & dependencies:** Are open questions listed with owners?
   - **Rollout:** Is there a launch plan, flag strategy, and rollback plan?
4. If suggesting rewrites, follow the structure in `assets/prd-template.md`.

## Output format
- **Verdict:** Ready / Needs work / Not ready
- **Top 3 blockers:** what's wrong, why it matters, and a suggested fix
- **Smaller improvements:** brief, grouped by section
- **Questions for the PM:** gaps only the author can fill

## Verdict rules
- **Not ready:** any of Problem, Success metrics or Requirements is missing.
- **Needs work:** all core sections exist, but at least one blocker remains.
- **Ready:** no blockers; only smaller improvements.

## Rules
- Quote the exact line you're critiquing so feedback is easy to act on.
- Never invent metrics, data, or user research. Flag the gap instead.
- Don't rewrite the whole PRD unless asked.
- If the doc is an early-stage idea rather than a PRD, say so and review it
  against the "Problem" and "Success metrics" sections only.
