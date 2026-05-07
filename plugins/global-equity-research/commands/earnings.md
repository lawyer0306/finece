---
description: Analyze quarterly or interim earnings and create a market-aware earnings update report (US/EU/UK/JP/Greater China/APAC)
argument-hint: "[ticker or company] [period, e.g. Q3 2024, 1H 2024, Q1 FY25]"
---

# Multi-Market Earnings Analysis Command

Create a professional equity research earnings update report, adapted to
the issuer's home market.

## Workflow

### Step 1: Gather Information

Parse the input for:
- Ticker (with exchange suffix preferred: `2330.TW`, `7203.T`,
  `0700.HK`, `AAPL`, `ASML.AS`, etc.) OR company name
- Period — accept any of:
  - US/CN/TW/KR style: `Q1 2024`, `Q3 2024`
  - JP style: `Q1 FY25`, `1Q FY2025`
  - HK/UK/EU style: `1H 2024`, `Interim 2024`, `HY 2024`
  - AU style: `1H FY24` (Jul-Dec)

If not provided, ask:
- "Which issuer (ticker preferred, e.g., 2330.TW, 7203.T, AAPL)?"
- "Which reporting period?"

### Step 2: Resolve Market Context (MANDATORY)

Invoke the **`market-context`** skill before any data search. Use its
output (exchange, currency, accounting standard, fiscal calendar,
filing nomenclature, primary source URL, consensus sources) for every
subsequent step. Do not guess — if the ticker is ambiguous, ask the
user which exchange.

### Step 3: Verify Timeliness

**CRITICAL**: Before proceeding, verify you have the latest data:
1. Search for "[Company] latest [period-type] results [current year]"
   in BOTH English and the issuer's primary language
2. Verify the release is within the last 3 months (or 6 months for
   semi-annual-only markets — HK Main Board, UK Main Market, most EU)
3. Confirm transcript / earnings call date matches release date
4. Pull the actual filing from the market-specific primary source
   (EDGAR / MOPS / EDINET / HKEXnews / RNS / OAM / DART / SEDAR+ /
   CNINFO etc.) — NOT just news summaries

If data is stale, inform the user and search for the latest.

### Step 4: Load Earnings Analysis Skill

Use `skill: "earnings-analysis"` to create the report:

1. **Data Collection** (search for latest, market-adjusted):
   - Earnings release / press release / local equivalent
     (e.g., 決算短信 for JP, 業績公告 for HK, 重大訊息 for TW)
   - Quarterly/interim filing from the market's primary regulatory
     source (use `market_context.filings.primary_source_url`):
     EDGAR (US), EDINET (JP), MOPS (TW), HKEXnews (HK), CNINFO (CN),
     RNS/Companies House (UK), DART (KR), SEDAR+ (CA), national OAM (EU)
   - Earnings call transcript (note primary-language constraints)
   - Investor presentation / supplemental materials
   - Consensus estimates from `market_context.consensus_sources`
     (NOT US Bloomberg by default for non-US issuers)

2. **Beat/Miss Analysis**:
   - Revenue vs consensus: Beat/Miss by $X or X%
   - EPS vs consensus: Beat/Miss by $X or X%
   - Key segment performance vs expectations
   - Explain WHY results differed

3. **Key Metrics Analysis**:
   - Revenue breakdown by segment/geography
   - Margin trends (gross, operating, net)
   - Guidance: raised/maintained/lowered
   - Updated forward estimates

4. **Generate Charts** (8-12):
   - Quarterly revenue progression
   - Quarterly EPS progression
   - Margin trends
   - Revenue by segment
   - Beat/miss summary
   - Estimate revisions
   - Valuation charts

5. **Create Report** (8-12 pages):
   - Page 1: Summary with rating and price target
   - Pages 2-3: Detailed results analysis
   - Pages 4-5: Key metrics & guidance
   - Pages 6-7: Updated investment thesis
   - Pages 8-10: Valuation & estimates
   - Sources section with clickable hyperlinks

### Step 4: Deliver Output

Provide:
1. **DOCX report** - 8-12 page earnings update
2. **Summary** highlighting:
   - Beat/miss on key metrics
   - Guidance changes
   - Thesis impact (positive/negative/neutral)

## Report Structure Reference

```
PAGE 1: EARNINGS SUMMARY
┌─────────────────────────────────────────────────────────────────┐
│ [Company] Q3 2024 Earnings Update                               │
│ Rating: BUY | Price Target: $XXX (from $XXX)                    │
├─────────────────────────────────────────────────────────────────┤
│ KEY TAKEAWAYS                                                   │
│ • Revenue beat by X% on strong [segment] performance            │
│ • EPS beat by $X.XX driven by margin expansion                  │
│ • FY guidance raised to $X.XX-$X.XX (from $X.XX-$X.XX)         │
│ • Thesis intact; maintain BUY rating                            │
├─────────────────────────────────────────────────────────────────┤
│ RESULTS SNAPSHOT                                                │
│ ┌─────────────┬──────────┬──────────┬──────────┐               │
│ │ Metric      │ Actual   │ Consensus│ Beat/Miss│               │
│ │ Revenue     │ $X.XXB   │ $X.XXB   │ +X.X%    │               │
│ │ EPS         │ $X.XX    │ $X.XX    │ +$X.XX   │               │
│ │ Gross Margin│ XX.X%    │ XX.X%    │ +XXbps   │               │
│ └─────────────┴──────────┴──────────┴──────────┘               │
└─────────────────────────────────────────────────────────────────┘

PAGES 2-3: DETAILED RESULTS
- Segment-by-segment analysis
- Geographic breakdown
- Key drivers of beat/miss

PAGES 4-5: METRICS & GUIDANCE
- Margin analysis
- Full-year guidance comparison
- Updated quarterly estimates

PAGES 6-7: THESIS UPDATE
- What's changed
- Risks and catalysts
- Investment recommendation

PAGES 8-10: VALUATION
- Updated DCF/comps if material
- Price target justification
- Scenario analysis

SOURCES SECTION (with clickable hyperlinks):
- Earnings Release: [hyperlink]
- Form 10-Q: [EDGAR hyperlink]
- Earnings Call Transcript: [hyperlink]
- Consensus estimates: Bloomberg as of [date]
```

## Quality Checklist

Before delivery:
- [ ] **Market context resolved and applied** (correct exchange,
      currency, accounting standard, fiscal calendar, filing names)
- [ ] Earnings data is from latest period (not stale, not from
      training data)
- [ ] Filings pulled from the market's primary regulatory source
      (not just news aggregators)
- [ ] Beat/miss quantified with specific numbers in REPORTING currency
      (USD-equivalent in parens if useful for cross-border audience)
- [ ] FX assumptions stated if presentation currency differs from
      reporting currency
- [ ] All charts embedded (8-12 total) with quarter/period labels
      using the issuer's actual fiscal convention
- [ ] Sources section with clickable hyperlinks pointing to PRIMARY
      regulatory source (not news republications)
- [ ] Every figure/table has source citation including filing date
- [ ] Guidance changes clearly documented (note guidance-disclosure
      conventions vary — many JP/EU issuers give annual-only guidance)
- [ ] Rating and price target stated upfront, in reporting currency
- [ ] Local-language press release cross-checked for material content
      omitted from English summaries
- [ ] 8-12 pages, 3,000-5,000 words
