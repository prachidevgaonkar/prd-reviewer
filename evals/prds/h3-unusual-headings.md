# Two-Factor Recovery Codes

## The pain
Users who lose their phone are locked out of two-factor authentication and must contact support to regain access. Account-recovery tickets average 4.2 days to resolve because support must verify identity manually, and they made up 14% of all support volume in Q3 (1,120 tickets). 23 customers mentioned lockouts in cancellation surveys this year.

**Why now:** Two-factor will become mandatory for admin accounts on January 15, which will multiply lockouts.

## Who it's for
Any user with two-factor authentication enabled, especially admins.

## How we'll know it worked
| Metric | Baseline | Target | Timeframe |
| --- | --- | --- | --- |
| Account-recovery support tickets per month | 373 | Under 120 | 60 days after GA |
| Users who save recovery codes at 2FA setup | n/a, new | 70% | 60 days after GA |
| Account-takeover incidents (guardrail) | 0 last quarter | Stays at 0 | Ongoing |

## What we're building and not building
**Building:** Ten single-use recovery codes generated at 2FA setup, which users can download or copy, and regenerate later.

**Not building:** SMS fallback, recovery through support chat, hardware key support.

## Detailed behavior
| ID | Behavior | Priority | How we test it |
| --- | --- | --- | --- |
| B1 | Generate 10 single-use codes at 2FA setup | P0 | Each code works exactly once |
| B2 | Users must confirm they saved codes before finishing setup | P0 | Setup cannot complete without confirmation |
| B3 | Regenerating codes invalidates all previous codes | P0 | Old codes rejected after regeneration |
| B4 | Email alert whenever a recovery code is used | P0 | Email sent within 1 minute |

**Edge cases:** After 5 failed recovery-code attempts the account locks for 30 minutes. When the last code is used, the user is prompted to regenerate. Codes are stored hashed, never in plain text.

## Watch-outs
| Item | Type | Owner | Due |
| --- | --- | --- | --- |
| Security review of code generation and storage | Dependency | Nadia (Security) | Nov 15 |
| Do existing 2FA users get prompted to create codes? | Open question | Chris (PM) | Nov 8 |

## Shipping it
- **Sequence:** Internal staff, then 10% of 2FA users, then all users before January 15.
- **Feature flag:** `recovery_codes`.
- **Rollback:** Disable the flag; generated codes remain valid but no new codes are created.
- **Enablement:** Help article and an update to support macros.
