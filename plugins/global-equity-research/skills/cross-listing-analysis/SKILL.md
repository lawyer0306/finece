---
name: cross-listing-analysis
description: Analyze issuers with multiple listings (ADR, A+H, dual-primary, secondary listings, GDRs). Identifies which line is being analyzed, reconciles differences in accounting standards / fiscal periods / disclosure timing between listings, computes premium/discount between listings, and flags arbitrage / fungibility constraints. Use whenever the user mentions an ADR, GDR, an A+H share pair, a secondary HK listing of a US-listed Chinese ADR, or any issuer with more than one ticker.
---

# Cross-Listing Analysis

Many institutional names trade on multiple venues with materially
different filings, accounting, holders, and prices. This skill ensures
the analyst is unambiguous about which line is being covered and
captures the implications of the parallel listing(s).

## Trigger Examples

- "Analyze BABA" — ADR (NYSE: BABA) AND HK primary (9988.HK) since 2019
- "Cover Tencent" — primary HK listing (0700.HK), no US listing
- "Cover Shell" — dual-primary historically (LON / AMS / NYSE ADR);
  consolidated 2022
- "Analyze ICBC" — A-share (601398.SS) AND H-share (1398.HK)
- "Cover ASML" — primary AMS (ASML.AS) + NASDAQ secondary (ASML)
- "Analyze TSMC" — primary TWSE (2330.TW) + NYSE ADR (TSM, 1 ADR = 5 TW)

## Core Procedure

### Step 1: Map the listing structure

For the issuer, document:
- Primary listing (exchange, ticker, ISIN)
- All secondary / cross listings (exchanges, tickers, ISINs)
- Listing type for each: primary, dual-primary, secondary, ADR (Level
  I/II/III), GDR
- ADR ratio if applicable (e.g., 1 ADR = 5 TW shares for TSM/2330.TW)
- Fungibility: are shares freely convertible between lines? Subject to
  daily quota? Stock Connect eligible?

### Step 2: Identify accounting/filing differences

| Listing pair                   | Likely differences                                  |
|--------------------------------|------------------------------------------------------|
| US ADR + foreign primary       | Foreign issuer files 20-F annual (US) + home filings |
| A-share + H-share (China + HK) | China GAAP (CASBE) vs HKFRS — net income can differ |
| US + dual-primary HK           | Identical financials, differing disclosure timing    |
| London + AMS / Frankfurt       | Same IFRS group accounts; presentation may differ    |

For A+H pairs, always reconcile the published net-income difference
(typically disclosed in the H-share interim/annual report).

### Step 3: Compute premium/discount

For each parallel pair, compute:
```
Premium/Discount (%) = (Price_A in CCY_B − Price_B) / Price_B × 100%
```
Use spot FX as of the same observation moment. For A+H, the
**Hang Seng Stock Connect China AH Premium Index** is the common
benchmark — quote it alongside the issuer-specific premium.

For ADRs:
```
Implied parity = Underlying price × ADR ratio × FX(local→USD)
ADR premium  = (ADR price − Implied parity) / Implied parity × 100%
```
Persistent ADR premium/discount may indicate fungibility constraints,
withholding tax, or sanctions/regulatory risk.

### Step 4: Disclosure-timing analysis

- **A+H**: Material announcements must be released to A and H markets
  simultaneously per CSRC/HKEX rules, but earnings dates may differ in
  practice — confirm both regulatory disclosure and practice.
- **US ADR + home market**: 20-F filed within 4 months of FYE; home
  filings typically faster. Watch for information arbitrage windows.
- **EU dual-listings**: ESMA/MAR requires inside information disclosure
  to all venues simultaneously.

### Step 5: Holder base and liquidity

- Identify approximate split of shares outstanding by listing
- Compare ADV (average daily volume) on each line
- Note index inclusions (S&P, MSCI, FTSE, CSI, HSI, etc.) — drives flow
- ADR cancellation/issuance trends signal cross-border flow direction

## Output

A short cross-listing brief (1-2 pages) including:
1. Listing structure table (exchange, ticker, ISIN, type, ratio)
2. Current premium/discount with 1Y range chart
3. Accounting reconciliation summary (for A+H or where relevant)
4. Disclosure-timing notes
5. Liquidity/ADV comparison
6. Recommended primary line for analysis (and why)

## Common Pitfalls

- **Mixing prices across lines** without FX/ratio adjustment.
- **Treating ADR financials as separate** — they reflect the same
  underlying issuer; pull the home filings for full disclosure.
- **Ignoring withholding tax / dividend treatment** differences (e.g.,
  H-share dividends to mainland investors via Stock Connect have
  withholding implications).
- **Assuming Stock Connect fungibility** without checking the eligible-
  securities list (some shares are Connect-eligible but with caps).
- **Treating Cayman / Bermuda incorporation as irrelevant** — VIE
  structures (common for US-listed Chinese ADRs) are a material
  governance factor.
