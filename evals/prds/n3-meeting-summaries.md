# AI Meeting Summaries PRD

## Problem
Users record customer calls in our product but rarely rewatch them. Only 6% of recordings are opened after the meeting ends. In interviews with 18 account executives, 14 said they take manual notes during calls because recordings are "too long to use." Competitors launched automatic summaries this year, and we lost 3 deals in Q3 where it was cited.

**Why now:** Lost-deal reasons now name summaries specifically, and our transcription pipeline is already in place.

## Users
Sales and customer success teams who record external calls.

## Success metrics
| Metric | Baseline | Target | Timeframe |
| --- | --- | --- | --- |
| Recordings with a summary opened within 7 days | 6% opened | 35% | 60 days after GA |
| Summary thumbs-down rate (guardrail) | n/a, new | Under 10% | Ongoing |

## Scope
**In scope:** An automatic summary, action items and key questions generated after each recorded call, shown on the recording page and sent by email to the host.

**Non-goals:** Live in-call summaries, CRM field updates, summaries for internal meetings.

## Requirements
| ID | Requirement | Priority | Acceptance criteria |
| --- | --- | --- | --- |
| R1 | Generate a summary within 10 minutes of a call ending | P0 | p95 under 10 minutes |
| R2 | Summary includes overview, action items with owners, and open questions | P0 | Each section present for calls over 5 minutes |
| R3 | Host can edit the summary before sharing | P0 | Edits saved and versioned |
| R4 | Email summary to the host | P1 | Sent within 15 minutes of call end |

**Edge cases:** Calls under 2 minutes are not summarized. Calls with no detected speech show "No summary available." Non-English calls are summarized in the call's language.

## Risks, dependencies and open questions
- Which model provider do we use?
- Do we store summaries forever?
- Should external participants receive the summary?

## Rollout
- **Sequence:** 10 design-partner accounts, then all paid plans.
- **Feature flag:** `ai_summaries`.
- **Rollback:** Disable the flag if the thumbs-down rate exceeds 20%.
