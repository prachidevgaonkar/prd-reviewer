# Invoice PDF Export PRD

## Problem
Finance admins at mid-market customers cannot download invoices as PDFs. They screenshot the billing page or email support for copies. In Q3, invoice-copy requests were 22% of all billing support tickets (412 of 1,873), and two enterprise renewals listed "invoice self-service" as a requirement in procurement checklists.

**Why now:** Our support team is moving to a smaller billing pod in Q1, and the renewal checklists come due in February.

## Users
Billing admins and finance owners on Team and Enterprise plans.

## Success metrics
| Metric | Baseline | Target | Timeframe |
| --- | --- | --- | --- |
| Invoice-copy support tickets per month | 137 | Under 30 | 60 days after GA |
| Billing page error rate (guardrail) | 0.4% | Stays under 0.5% | Ongoing |

## Scope
**In scope:** Download a single invoice as PDF; download all invoices for a date range as a ZIP.

**Non-goals:** Custom invoice branding, editing invoice line items, sending invoices to third-party accounting tools.

## Requirements
| ID | Requirement | Priority | Acceptance criteria |
| --- | --- | --- | --- |
| R1 | Billing admins can download any past invoice as a PDF | P0 | PDF matches the on-screen invoice totals and tax lines exactly |
| R2 | Bulk download for a date range up to 24 months | P0 | ZIP contains one PDF per invoice, named by invoice number |
| R3 | Non-admin members cannot see the download control | P0 | Control hidden; direct URL returns 403 |
| R4 | PDF is generated within 3 seconds for a single invoice | P1 | p95 under 3 s in load test |

**Edge cases:** Voided invoices download with a "VOID" watermark. Invoices in non-USD currencies show the original currency. If generation fails, the user sees a retry message and the failure is logged.

## Risks, dependencies and open questions
| Item | Type | Owner | Due |
| --- | --- | --- | --- |
| PDF rendering service capacity for bulk downloads | Dependency | Arjun (Platform) | Nov 15 |
| Do EU invoices need a VAT-specific layout? | Open question | Dana (Finance) | Nov 8 |

## Rollout
- **Sequence:** Internal finance team, then 10% of Team accounts, then GA.
- **Feature flag:** `invoice_pdf_export`, ramped by account.
- **Rollback:** Turn the flag off if PDF totals mismatch in any audit sample or error rate exceeds 0.5%.
- **Enablement:** Help center article and a note in the monthly billing email.
