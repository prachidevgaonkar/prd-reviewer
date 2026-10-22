# Private Notes on Records PRD

## Problem
Account managers keep personal notes about customers in spreadsheets because notes in our CRM are visible to the whole team. In a survey of 160 account managers, 58% said they keep notes outside the product, and 37 support tickets in Q3 asked for private notes. Notes kept outside the CRM are lost when people change roles, which our CS leaders flagged in two churn reviews.

**Why now:** Our largest customer's renewal in February depends on reducing off-platform data.

## Users
Account managers and customer success managers.

## Success metrics
| Metric | Baseline | Target | Timeframe |
| --- | --- | --- | --- |
| Account managers who create at least one private note per week | 0% | 45% | 60 days after GA |
| Reported off-platform note-taking (survey) | 58% | Under 30% | Next quarterly survey |
| Record page load time p95 (guardrail) | 1.1 s | Stays under 1.3 s | Ongoing |

## Scope
**In scope:** Private notes on account and contact records, visible only to their author.

**Non-goals:** Sharing private notes with other users in any form, team-level notes, note templates.

## Requirements
| ID | Requirement | Priority | Acceptance criteria |
| --- | --- | --- | --- |
| R1 | Users can add a private note to any account or contact record | P0 | Note saved and visible only to its author |
| R2 | Private notes are excluded from search for other users | P0 | Other users' searches return no private note content |
| R3 | Authors can generate a read-only link to a private note to send to a colleague | P0 | Link opens the note for anyone in the workspace |
| R4 | When a user is deactivated, their private notes transfer to their manager | P1 | Manager sees transferred notes within 1 hour |

**Edge cases:** Notes are limited to 10,000 characters. Deleting a record deletes its private notes after a 30-day recovery window.

## Risks, dependencies and open questions
| Item | Type | Owner | Due |
| --- | --- | --- | --- |
| Permission model changes in the records service | Dependency | Jo (Platform) | Nov 18 |
| Do private notes appear in data exports? | Open question | Marc (Legal) | Nov 10 |

## Rollout
- **Sequence:** Internal sales team, then 20% of accounts, then GA.
- **Feature flag:** `private_notes`.
- **Rollback:** Disable the flag; notes stay stored and reappear if re-enabled.
