# Saved Searches PRD

## Problem
Power users on the analytics plan rebuild the same filtered search every morning. In Q3, 38% of support tickets tagged "search" asked for a way to save filters, and session recordings show the median power user spends 2.5 minutes re-entering filters per session. Teams on our largest accounts keep filter recipes in shared docs, which shows the workaround cost is real.

**Why now:** The search team shipped a stable filter serialization API in September, so saved state is now cheap to build.

## Users
Analysts and power users on the analytics plan (about 4,800 weekly active users).

## Success metrics
| Metric | Baseline | Target | Timeframe |
| --- | --- | --- | --- |
| Power-user sessions starting from a saved search | 0% | 40% | 60 days after GA |
| Search latency p95 (guardrail) | 640 ms | Stays under 800 ms | Ongoing |

## Scope
**In scope:** Saving, naming, editing and deleting personal saved searches.

**Non-goals:** Sharing saved searches with teammates, scheduled email alerts.

## Requirements
| ID | Requirement | Priority | Acceptance criteria |
| --- | --- | --- | --- |
| R1 | Save the current query and filters with a name up to 60 characters | P0 | Saved search reloads identical results |
| R2 | Saved searches appear in a dropdown by the search bar, most recent first | P0 | Order updates on each use |
| R3 | Selecting a saved search applies it within 500 ms | P0 | p95 under 500 ms |
| R4 | Rename and delete saved searches | P1 | Changes persist across sessions |

**Edge cases:** Duplicate names show an inline error. A saved search referencing a deleted field loads with that filter removed and a warning. Users can save at most 50 searches; the 51st shows a limit message.

## Risks, dependencies and open questions
| Item | Type | Owner | Due |
| --- | --- | --- | --- |
| Filter serialization API stability | Dependency | Priya (Search) | Nov 1 |
| Migrate filters stored in the old bookmarks feature? | Open question | Sam (PM) | Oct 25 |

## Rollout
- **Sequence:** Internal analysts, then 10% of analytics accounts, then GA.
- **Feature flag:** `saved_searches`, per account.
- **Rollback:** Disable the flag if search p95 exceeds 800 ms for 30 minutes.
- **Enablement:** Tooltip on first visit and a changelog entry.
