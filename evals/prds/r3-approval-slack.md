# Slack Notifications for Expense Approvals PRD

## Problem
Managers approve expenses slowly because they only learn about pending requests from a daily email digest. Median time to approval is 3.4 days, and in a September survey of 210 employees, 46% said late reimbursement was their top complaint about the product. Customers with Slack connected already use it for 70% of their other notifications.

**Why now:** Two of our top 20 accounts have flagged approval delays in QBRs this quarter.

## Users
Approving managers at companies with the Slack integration enabled. Employees submitting expenses benefit indirectly.

## Success metrics
| Metric | Baseline | Target | Timeframe |
| --- | --- | --- | --- |
| Median time to approval | 3.4 days | 1.5 days | 60 days after GA |
| Notification mute rate (guardrail) | n/a, new | Under 15% of managers | 60 days after GA |

## Scope
**In scope:** A Slack direct message for each new approval request, with Approve and Reject buttons.

**Non-goals:** Approvals in Microsoft Teams, editing an expense from Slack, channel-level notifications.

## Requirements
| ID | Requirement | Priority | Acceptance criteria |
| --- | --- | --- | --- |
| R1 | Manager receives a Slack DM within 1 minute of a request | P0 | 99% of DMs delivered within 60 s in staging |
| R2 | DM includes amount, merchant, submitter and receipt link | P0 | Fields match the request record |
| R3 | Approve and Reject buttons work without leaving Slack | P0 | Status updates in the app within 5 s |
| R4 | Managers can mute these DMs in notification settings | P1 | Muted users receive no DMs |

**Edge cases:** If the manager has left the company, the request routes to their manager's DM. If an expense is already approved in the web app, the Slack buttons are disabled and show "Already approved." If the Slack token is revoked, we fall back to email.

## Risks, dependencies and open questions
| Item | Type | Owner | Due |
| --- | --- | --- | --- |
| Slack app review for new interactive scopes | Dependency | Kim (Integrations) | Nov 12 |
| Should reject require a reason? | Open question | Omar (PM) | Nov 5 |

## Rollout
- **Sequence:** Our own company, then 20 opted-in customers, then GA.
- **Feature flag:** `slack_approvals`, per workspace.
- **Rollback:** Disable the flag if duplicate approvals or failed status updates exceed 0.1%.
- **Enablement:** Admin email, help article, and a short Loom for CSMs.
