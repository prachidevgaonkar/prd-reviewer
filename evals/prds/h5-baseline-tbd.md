# In-App Help Center PRD

## Problem
Users leave the product to search our help center, and many give up and file a ticket instead. 41% of "how do I" tickets in Q3 (1,904 tickets) were answered by an existing help article, which means users couldn't find it. Users who file a ticket in their first month are 1.8 times more likely to churn.

**Why now:** Support headcount is flat next year while the customer base grows about 30%.

## Users
All users, especially those in their first 30 days.

## Success metrics
| Metric | Baseline | Target | Timeframe |
| --- | --- | --- | --- |
| "How do I" tickets answered by an existing article | 1,904 per quarter | 25% reduction | One quarter after GA |
| Help searches that end with an article opened | TBD (Data team instrumenting, owner: Hana, due Nov 5) | TBD | 60 days after GA |
| Ticket CSAT (guardrail) | 4.4 / 5 | Stays at or above 4.3 | Ongoing |

## Scope
**In scope:** A help panel inside the product with search, article view and a "contact support" button.

**Non-goals:** AI chat answers, community forum, video tutorials.

## Requirements
| ID | Requirement | Priority | Acceptance criteria |
| --- | --- | --- | --- |
| R1 | Help panel opens from the "?" icon on every page | P0 | Panel opens without leaving the current page |
| R2 | Search returns help articles ranked by relevance | P0 | Top 3 results include the correct article for 80% of a 50-query test set |
| R3 | Articles render inside the panel with working links | P0 | Images, links and tables display correctly |
| R4 | "Contact support" pre-fills the ticket with the search term | P1 | Ticket form shows the last search |

**Edge cases:** No results shows suggested popular articles and the contact button. If the help center API is down, the panel shows a link to the external help site.

## Risks, dependencies and open questions
| Item | Type | Owner | Due |
| --- | --- | --- | --- |
| Help center search API rate limits | Risk | Ken (Platform) | Nov 12 |

## Rollout
- **Sequence:** 10% of new accounts, then all new accounts, then everyone.
- **Feature flag:** `in_app_help`.
- **Rollback:** Disable the flag; the "?" icon reverts to opening the external help site.
