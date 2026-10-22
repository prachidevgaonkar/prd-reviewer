# Onboarding Checklist PRD

## Problem
New workspace owners don't discover our core features. Only 28% of new workspaces create a second project in their first week, and accounts that do are 2.3 times more likely to convert to paid (Q2 cohort analysis, 9,400 workspaces). In exit surveys, "didn't know where to start" is the top reason for churn among trial users (34%).

**Why now:** Trial-to-paid conversion fell from 11% to 9% this year, and onboarding is the largest controllable driver.

## Users
Owners of new workspaces in their first 14 days.

## Success metrics
| Metric | Baseline | Target | Timeframe |
| --- | --- | --- | --- |
| New workspaces creating a second project in week 1 | 28% | 40% | 60 days after GA |
| Trial-to-paid conversion | 9% | 10.5% | 90 days after GA |

## Scope
A checklist for new workspace owners that helps them get started.

## Requirements
- The checklist should make onboarding easier and more engaging.
- Support the key steps a new user needs to take.
- Handle different types of users appropriately.
- Should feel delightful and on-brand.
- Integrate with analytics.

## Risks, dependencies and open questions
| Item | Type | Owner | Due |
| --- | --- | --- | --- |
| Which steps go on the checklist? | Open question | Rae (PM) | Nov 4 |
| Analytics events for each step | Dependency | Tom (Data) | Nov 11 |

## Rollout
- **Sequence:** A/B test with 50% of new workspaces for four weeks, then GA if the primary metric improves.
- **Feature flag:** `onboarding_checklist`.
- **Rollback:** Turn off the flag if trial conversion drops in the test group.
