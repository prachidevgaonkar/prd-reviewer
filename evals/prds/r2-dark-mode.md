# Mobile Dark Mode PRD

## Problem
Our mobile app has no dark mode. It is the most-voted request on our public roadmap (1,240 votes) and appears in 9% of App Store reviews under 4 stars since July. Session data shows 31% of mobile sessions start between 8 pm and 2 am, when a bright interface is most uncomfortable.

**Why now:** The design system team finished semantic color tokens last month, which makes theming a contained change instead of a rewrite.

## Users
All iOS and Android users, especially evening and night users.

## Success metrics
| Metric | Baseline | Target | Timeframe |
| --- | --- | --- | --- |
| Share of App Store reviews mentioning dark mode | 9% of sub-4-star reviews | Under 2% | 90 days after GA |
| Evening session length (8 pm to 2 am) | 6.1 min median | 6.8 min median | 90 days after GA |
| Crash-free sessions (guardrail) | 99.6% | Stays at or above 99.5% | Ongoing |

## Scope
**In scope:** Light, dark and "match system" themes on iOS and Android, applied to every screen.

**Non-goals:** Custom color themes, dark mode for emails, scheduled theme switching.

## Requirements
| ID | Requirement | Priority | Acceptance criteria |
| --- | --- | --- | --- |
| R1 | Theme setting with Light, Dark and Match system | P0 | Setting persists across app restarts |
| R2 | Every screen uses semantic tokens | P0 | Automated scan finds zero hard-coded colors |
| R3 | Text meets WCAG AA contrast in both themes | P0 | Contrast audit passes on all screens |
| R4 | User-uploaded images are not inverted | P0 | Visual regression suite passes |

**Edge cases:** Charts use the dark palette from the design system. Embedded web views receive the theme through a query parameter; if a page ignores it, it renders in light mode without errors.

## Risks, dependencies and open questions
| Item | Type | Owner | Due |
| --- | --- | --- | --- |
| Third-party SDK screens (payments) may not support dark mode | Risk | Lee (Mobile) | Nov 20 |
| Marketing screenshots need updating for store listings | Dependency | Ana (Marketing) | Dec 1 |

## Rollout
- **Sequence:** Internal beta, then 5% of users, then 50%, then GA over three weeks.
- **Feature flag:** `mobile_dark_mode`, remote config by platform.
- **Rollback:** Disable the flag if crash-free sessions drop below 99.5% on either platform.
- **Enablement:** In-app announcement and release notes.
