---
description: Draft a global morning meeting note across the coverage universe
argument-hint: "[optional: region focus, e.g. 'asia', 'europe', 'us']"
---

Draft a concise multi-region morning note covering overnight developments
across the coverage universe.

## Workflow

1. If a region focus is supplied, scope the note accordingly. Otherwise
   produce a global note ordered by market-close timing
   (Asia close → Europe → US overnight).
2. For each named issuer mentioned, invoke the `market-context` skill
   to resolve currency, exchange, and quarter convention before
   reporting numbers.
3. Load the `morning-note` skill for the structured format.

Sections to cover:
- **Overnight macro** — index moves, FX, rates, commodities (state TZ)
- **Earnings reactions** — yesterday's prints, post-market AMC moves
- **Pre-market / pre-open events** — guidance updates, M&A, regulatory
- **Asia recap** (for non-Asia readers) — TWSE, HKEX, TSE, KRX, ASX
- **Coverage actions** — rating/PT changes, model updates
- **Trade ideas** — long/short, hedge ideas, pair trades

Always state quotes in the issuer's reporting currency with USD or
local-currency conversion only where it aids the reader.
