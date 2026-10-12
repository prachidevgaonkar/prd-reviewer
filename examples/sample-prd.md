# Saved Searches PRD

## Problem
Power users on the analytics plan rebuild the same filtered search every morning. In Q3, 38% of support tickets tagged "search" asked for a way to save filters, and session recordings show the median power user spends 2.5 minutes re-entering filters per session. Teams on our largest accounts have started keeping filter recipes in shared docs, which tells us the workaround cost is real.

## Success metrics
Increase the share of power-user sessions that start from a saved search from 0% to 40% within 60 days of GA. Guardrail: search latency p95 stays under 800 ms.

## Scope
In scope: saving, naming, editing and deleting personal saved searches.

Non-goals: sharing saved searches with teammates, scheduled email alerts.

## Requirements
- P0: A user can save the current query and filters with a name of up to 60 characters.
- P0: Saved searches appear in a dropdown next to the search bar, most recently used first.
- P0: Selecting a saved search applies its query and filters within 500 ms.
- P1: A user can rename or delete a saved search.
- Edge cases: duplicate names show an inline error; a saved search referencing a deleted field loads with that filter removed and a warning; users can save at most 50 searches.

## Risks
- Dependency on the search team's filter serialization API (owner: Priya, due Nov 1).
- Open question: do we migrate filters stored in the old bookmarks feature? (owner: Sam, due Oct 25)
