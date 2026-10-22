# Field Visit Check-In PRD

## Problem
Managers of field sales teams can't confirm whether reps visited customer sites. Reps log visits manually, and in an audit of 400 logged visits at three customers, 18% had no matching calendar event or customer confirmation. Field-sales customers listed "visit verification" as a top-three request in 6 of 10 QBRs this year.

**Why now:** Field sales is our fastest-growing segment, and a competitor launched visit verification in August.

## Users
Field sales reps (mobile) and their managers (web).

## Success metrics
| Metric | Baseline | Target | Timeframe |
| --- | --- | --- | --- |
| Visits logged with a verified check-in | 0% | 70% | 60 days after GA |
| Manager weekly active usage of the visit report | n/a, new | 50% of field-sales managers | 60 days after GA |
| Mobile app battery-related complaints (guardrail) | 3 per month | Stays under 6 per month | Ongoing |

## Scope
**In scope:** Reps check in at a customer site from the mobile app; the app records GPS location and time; managers see a map and report of check-ins.

**Non-goals:** Continuous location tracking, route optimization, mileage reimbursement.

## Requirements
| ID | Requirement | Priority | Acceptance criteria |
| --- | --- | --- | --- |
| R1 | Rep taps "Check in" and the app records GPS coordinates and timestamp | P0 | Location accurate within 100 m in field tests |
| R2 | Check-in is marked verified if within 500 m of the customer's address | P0 | Verification matches manual review for 95% of test cases |
| R3 | Managers see a map and table of their team's check-ins | P0 | Report loads under 2 s for 50 reps |
| R4 | Check-in history is stored for 3 years | P1 | Records retrievable for audits |

**Edge cases:** If GPS is unavailable, the check-in saves as "unverified" with a reason. Customer addresses that fail geocoding are flagged to the admin.

## Risks, dependencies and open questions
| Item | Type | Owner | Due |
| --- | --- | --- | --- |
| Geocoding API cost at scale | Risk | Pia (Platform) | Nov 15 |
| Offline check-ins | Open question | Leo (Mobile) | Nov 9 |

## Rollout
- **Sequence:** Two design-partner customers, then all field-sales accounts.
- **Feature flag:** `field_checkin`.
- **Rollback:** Disable the flag; existing check-in records remain viewable.
