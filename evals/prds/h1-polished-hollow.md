# Workflow Automation Builder PRD

## Problem
Users need a visual automation builder. Competitors have drag-and-drop workflow builders, and our product only offers simple if-this-then-that rules. A builder will make our platform more powerful and modern.

**Why now:** It is on the annual roadmap and leadership has prioritized it for Q1.

## Users
Operations managers and admins who configure automations.

## Success metrics
| Metric | Baseline | Target | Timeframe |
| --- | --- | --- | --- |
| Builder shipped to GA | Not started | Shipped | End of Q1 |
| Number of node types available | 0 | 25 | End of Q1 |

## Scope
**In scope:** A drag-and-drop canvas with triggers, conditions, actions and branches.

**Non-goals:** Code steps, marketplace of shared workflows, mobile editing.

## Requirements
| ID | Requirement | Priority | Acceptance criteria |
| --- | --- | --- | --- |
| R1 | Users drag nodes onto a canvas and connect them | P0 | Connections persist after save |
| R2 | Support branching with up to 5 branches per condition | P0 | Each branch executes independently in tests |
| R3 | Test run mode shows each node's input and output | P0 | Test run output matches a real run |
| R4 | Version history for each workflow | P1 | Users can restore any of the last 20 versions |

**Edge cases:** Disconnected nodes block saving with an inline error. Loops are detected and rejected at save time. If an action fails during a live run, the run stops and the owner is emailed.

## Risks, dependencies and open questions
| Item | Type | Owner | Due |
| --- | --- | --- | --- |
| Execution engine must support branching | Dependency | Ravi (Platform) | Dec 1 |
| Migration of existing simple rules | Open question | Ella (PM) | Nov 20 |

## Rollout
- **Sequence:** Internal, then 10% of accounts, then GA.
- **Feature flag:** `workflow_builder`.
- **Rollback:** Disable the flag; existing simple rules keep working.
