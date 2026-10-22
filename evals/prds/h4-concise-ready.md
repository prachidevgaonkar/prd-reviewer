# CSV Export Column Picker PRD

## Problem
Customers exporting reports to CSV get all 48 columns and delete most of them in Excel. 212 Q3 tickets asked to choose export columns, and in 15 user interviews, 11 people described deleting columns as a weekly chore.

**Why now:** Export volume doubled after the September reporting launch.

## Success metrics
Share of exports with a custom column selection: 0% today, 30% within 45 days of GA. Guardrail: export error rate stays under 0.2% (0.1% today).

## Scope
In scope: choosing and ordering columns before a CSV export, remembered per report. Non-goals: Excel format, scheduled exports, computed columns.

## Requirements
- P0: A column picker opens before export, with all columns selected by default. Acceptance: export contains exactly the selected columns, in the chosen order.
- P0: The selection is saved per user per report. Acceptance: the next export of that report pre-selects the same columns.
- P1: "Reset to all columns" link. Acceptance: one click restores the default.
- Edge cases: exporting with zero columns selected is blocked with an inline message; columns removed from a report since the last export are silently dropped from the saved selection.

## Risks and open questions
Export service change is owned by Wes (Data platform), due Nov 12. No open questions.

## Rollout
Behind the `export_column_picker` flag: internal, then 25% of accounts, then GA over two weeks. Roll back by turning off the flag if the export error rate exceeds 0.2%.
