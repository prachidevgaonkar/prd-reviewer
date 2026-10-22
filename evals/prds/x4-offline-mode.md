# Mobile Offline Mode PRD

## Problem
Field technicians use our mobile app on job sites with poor connectivity. When the connection drops, the app shows a blank screen and unsaved work is lost. In Q3, 27% of mobile support tickets (341 of 1,263) were about lost work or the app not loading offline, and two of our largest field-services customers rated mobile reliability 2 out of 5 in their QBRs.

**Why now:** Field services is now 40% of new bookings, and both QBR customers renew in Q1.

## Users
Field technicians on iOS and Android who work in low-connectivity locations.

## Success metrics
| Metric | Baseline | Target | Timeframe |
| --- | --- | --- | --- |
| Mobile tickets about lost work or offline loading | 341 per quarter | Under 80 per quarter | One quarter after GA |
| Sync conflict rate (guardrail) | n/a, new | Under 1% of synced edits | Ongoing |

## Scope
**In scope:** Viewing and editing assigned work orders offline, with sync when the connection returns.

**Non-goals:** Creating new work orders offline, offline access to reports, desktop offline mode.

## Risks, dependencies and open questions
| Item | Type | Owner | Due |
| --- | --- | --- | --- |
| Conflict resolution approach when two people edit the same order | Open question | Nils (Mobile) | Nov 14 |
| Local storage limits on older Android devices | Risk | Nils (Mobile) | Nov 14 |

## Rollout
- **Sequence:** Two design-partner customers, then all field-services accounts, then GA.
- **Feature flag:** `offline_mode`.
- **Rollback:** Disable the flag; the app reverts to online-only behavior.
