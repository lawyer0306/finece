---
description: Analyze cross-listings for an issuer (ADR, A+H, dual-primary, etc.)
argument-hint: "[ticker or company name]"
---

# Cross-Listing Analysis Command

Use the `cross-listing-analysis` skill to map an issuer's listing
structure, compute premium/discount across lines, reconcile any
accounting differences, and recommend the primary line of analysis.

## Workflow

1. Resolve the issuer (use `market-context` skill on the supplied ticker
   if needed to confirm the home exchange).
2. Identify ALL listings — primary, secondary, ADR, GDR.
3. Pull current prices and 1Y price history for each line.
4. Compute premium/discount with FX and ADR-ratio adjustment.
5. For A+H pairs, reconcile net-income differences from interim/annual
   reports.
6. Output the cross-listing brief format defined in the skill.

## When NOT to use

If the issuer has only one listing, this command is unnecessary —
proceed directly to `earnings`, `initiate`, or `thesis`.
