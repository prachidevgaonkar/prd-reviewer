# Team Spaces PRD

## Problem
Large workspaces become cluttered because every project is visible to everyone. In workspaces with more than 50 members, the median user can see 140 projects but works in 6. Admins at 9 enterprise accounts have asked for a way to group projects by team, and "too much noise" is the top theme in our Q3 NPS comments from enterprise users (112 mentions).

**Why now:** Enterprise is our fastest-growing segment, and clutter scales with workspace size.

## Users
Members and admins of workspaces with more than 50 members.

## Scope
**In scope:** Team spaces that group projects, with membership managed by workspace admins and team leads.

**Non-goals:** Per-space billing, separate permissions models, guest access to spaces.

## Requirements
| ID | Requirement | Priority | Acceptance criteria |
| --- | --- | --- | --- |
| R1 | Admins can create a team space with a name and members | P0 | Space appears in sidebar for members |
| R2 | Projects can be moved into a space | P0 | Project shows under the space for members |
| R3 | Sidebar shows the user's spaces first, then "All projects" | P0 | Order verified for members of 0, 1 and 5 spaces |
| R4 | Team leads can add or remove members of their space | P1 | Changes reflected within 5 seconds |

**Edge cases:** Projects not in any space stay under "All projects." Deleting a space moves its projects back to "All projects" rather than deleting them.

## Risks, dependencies and open questions
| Item | Type | Owner | Due |
| --- | --- | --- | --- |
| Sidebar redesign needed to fit spaces | Dependency | Joy (Design) | Nov 6 |
| Search scoping to spaces | Open question | Ben (Search) | Nov 13 |

## Rollout
- **Sequence:** 5 enterprise design partners, then all workspaces over 50 members, then GA.
- **Feature flag:** `team_spaces`.
- **Rollback:** Disable the flag; spaces are hidden and projects remain intact.
