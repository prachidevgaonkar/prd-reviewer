# PRD standards: our bar for "ready for eng"

Use this to judge quality, not just presence. A section can exist and still fail.

## Problem
**Ready when:**
- It names a specific user and a specific pain, in one or two sentences.
- It includes evidence: usage data, support tickets, research quotes, or revenue impact.
- It explains why now (what changed, or what it costs to wait).

**Common failures:**
- Describes the solution instead of the problem ("Users need a dashboard").
- No evidence, only opinion ("Users are frustrated").
- Problem is so broad that any solution would fit.

## Success metrics
**Ready when:**
- There is one primary metric, with a current baseline and a target.
- There is a timeframe ("within 60 days of GA").
- There is at least one guardrail metric that must not get worse.

**Common failures:**
- Output metrics instead of outcomes ("ship feature X").
- Vanity metrics with no link to the problem (page views for a retention problem).
- Target with no baseline, so success can't be judged.

## Scope and non-goals
**Ready when:**
- v1 is clearly separated from later phases.
- Non-goals are explicit and include at least one thing a reader might reasonably expect.

**Common failures:**
- No non-goals, which invites scope creep.
- "Phase 2" items mixed into v1 requirements.

## Requirements
**Ready when:**
- Each requirement is testable: an engineer or QA could write a check for it.
- Priorities are marked (must / should / could, or P0 / P1 / P2).
- Edge cases, empty states, error states and permissions are covered.
- Non-functional needs are stated where they matter (performance, accessibility, privacy, localization).

**Common failures:**
- Vague verbs ("support", "handle", "improve") with no acceptance criteria.
- Only the happy path.
- Design decisions left implicit ("see Figma") with no stated behavior.

## Risks, dependencies and open questions
**Ready when:**
- Dependencies on other teams or systems are named, with an owner.
- Each open question has an owner and a date it must be answered by.
- Key risks have a mitigation or a fallback.

**Common failures:**
- "TBD" with no owner.
- Legal, privacy or security review not mentioned for features touching user data.

## Rollout
**Ready when:**
- There is a launch sequence (internal, beta, percentage ramp, GA).
- Feature flag strategy is stated.
- There is a rollback plan and a clear trigger for using it.
- Support, docs and sales enablement are accounted for if users will notice the change.

**Common failures:**
- "Launch to everyone" with no ramp.
- No owner for monitoring after launch.

## Severity guide
- **Blocker:** engineering would build the wrong thing, or couldn't start, or success can't be measured.
- **Improvement:** the PRD works, but clarity or completeness could be better.
