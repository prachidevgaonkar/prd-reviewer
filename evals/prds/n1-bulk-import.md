# Bulk User Import PRD

## Problem
IT admins onboarding new customers add users one at a time. For accounts with more than 200 seats, onboarding calls with our implementation team regularly run over an hour just to add users. In Q3, 64 implementation tickets mentioned "bulk add" or "CSV import."

**Why now:** We are moving upmarket, and the average new account size doubled this year.

## Users
IT admins at accounts with 100 or more seats.

## Success metrics
- Increase seat activation within the first week to 60%.
- Reduce implementation hours per enterprise account.

## Scope
**In scope:** Upload a CSV of users with name, email, role and team.

**Non-goals:** SCIM provisioning, syncing with HR systems, bulk deactivation.

## Requirements
| ID | Requirement | Priority | Acceptance criteria |
| --- | --- | --- | --- |
| R1 | Admin uploads a CSV up to 5,000 rows | P0 | Upload accepted; progress shown |
| R2 | Preview shows parsed rows and errors before import | P0 | Invalid emails and unknown roles flagged per row |
| R3 | Import sends invitations to all valid rows | P0 | Invitations sent within 10 minutes for 5,000 rows |
| R4 | Downloadable error report for skipped rows | P1 | CSV lists row number and reason |

**Edge cases:** Duplicate emails in the file are imported once. Users who already exist are skipped and listed in the report.

## Risks, dependencies and open questions
| Item | Type | Owner | Due |
| --- | --- | --- | --- |
| Email provider rate limits for 5,000 invites | Risk | Mei (Platform) | Nov 10 |

## Rollout
Launch to all accounts at once in the November release, with a help center article.
