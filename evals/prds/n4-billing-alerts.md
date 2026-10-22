# Usage-Based Billing Alerts PRD

## Problem
Customers on usage-based plans are surprised by large invoices. In Q3, 19% of billing disputes (58 of 305) came from customers who said they did not know their usage had spiked. Each dispute takes our billing team about 45 minutes, and 11 disputed accounts churned within 60 days.

**Why now:** Usage-based plans grew from 15% to 32% of revenue this year, so the problem is growing fast.

## Users
Billing owners on usage-based plans.

## Success metrics
| Metric | Baseline | Target | Timeframe |
| --- | --- | --- | --- |
| Billing disputes citing unexpected usage per quarter | 58 | Under 20 | Two quarters after GA |
| Accounts setting at least one alert | 0% | 50% of usage-based accounts | 90 days after GA |

## Scope
**In scope:** Email alerts when usage crosses a threshold the billing owner sets.

**Non-goals:** Hard spending caps that stop service, SMS alerts, forecasting.

## Requirements
| ID | Requirement | Priority | Acceptance criteria |
| --- | --- | --- | --- |
| R1 | Billing owner sets up to 3 thresholds as a dollar amount | P0 | Thresholds saved per account |
| R2 | Email sent when month-to-date usage crosses a threshold | P0 | Email sent within 1 hour of crossing |
| R3 | Email shows current usage, threshold and top 3 usage drivers | P0 | Values match the billing dashboard |
| R4 | Billing owner can edit or delete thresholds | P1 | Changes take effect immediately |

## Risks, dependencies and open questions
| Item | Type | Owner | Due |
| --- | --- | --- | --- |
| Usage data is delayed up to 6 hours for some meters | Risk | Ivan (Billing eng) | Nov 9 |
| Should we pre-set a default alert for new accounts? | Open question | Lena (PM) | Nov 2 |
