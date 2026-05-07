---
name: earnings-analysis
description: Create professional multi-market equity research earnings update reports (8-12 pages, 3,000-5,000 words) for companies already under coverage. Fast-turnaround format focusing on beat/miss analysis, key metrics, updated estimates, and revised thesis. Market-aware - adapts filing sources, accounting standard, fiscal calendar, currency, and disclosure language to the issuer's home market (US, EU/UK, Japan, Greater China, APAC). Includes 1-3 summary tables and 8-12 charts. Use when user requests "earnings update", "quarterly update", "earnings analysis", "Q1/Q2/Q3/Q4 results", "interim results", post-earnings report, or local-language equivalents.
---

# Multi-Market Equity Research Earnings Update

Create professional **EARNINGS UPDATE REPORTS** analyzing quarterly or
interim results for companies already under coverage, following
institutional standards (JPMorgan, Goldman Sachs, Morgan Stanley,
Nomura, CICC, Citi) — adapted to the issuer's home market.

## ⚠️ MANDATORY PRE-FLIGHT: Run market-context skill FIRST

Before any other step, invoke the **`market-context`** skill to resolve
home exchange, reporting currency, accounting standard, fiscal-year
convention, filing nomenclature, primary filing source, and local
consensus sources. Do NOT proceed with the report until you have a
`market_context` object. Using US-centric defaults for a non-US issuer
is a quality failure.

**Key Characteristics:**
- **Length**: 8-12 pages
- **Word Count**: 3,000-5,000 words
- **Tables**: 1-3 summary tables (NOT comprehensive)
- **Figures**: 8-12 charts
- **Turnaround**: 1-2 days (within 24-48 hours of earnings)
- **Audience**: Clients already familiar with the company
- **Focus**: What's NEW - beat/miss, updated estimates, thesis impact
- **Font**: Times New Roman throughout (unless user specifies otherwise)

## When to Use

Use when the user requests:
- "Create an earnings update for [Company] Q3 2024"
- "Analyze [Company]'s quarterly results"
- "Post-earnings report for [Company]"
- "Q1/Q2/Q3/Q4 update for [Company]"

**Do NOT use if:**
- User requests "initiation report" → Use different skill
- User requests "flash note" or "quick take" → Different format
- Company is not already covered → Need initiation first

## Critical Requirements

### 1. Speed & Timeliness
- Publish within 24-48 hours of earnings release
- Focus on NEW information only
- Don't rehash company background extensively

### 2. Beat/Miss Analysis
- Lead with whether company beat or missed estimates
- Quantify variances (e.g., "Revenue beat by $120M or 3%")
- Explain WHY results differed from expectations

### 3. Summary Format
- Keep tables to 1-3 (summary only, not comprehensive)
- No full P&L/Cash Flow/Balance Sheet (just key metrics)
- Assume reader has seen initiation report

### 4. Citations & Source Attribution ⭐⭐⭐ MANDATORY

**CRITICAL**: Properly cite all data with SPECIFIC sources and CLICKABLE HYPERLINKS.

**Include specific citations WITH CLICKABLE LINKS in every figure and table:**

```
Source: Q3 2024 10-Q filed November 8, 2024; Company earnings release
        [Hyperlink "10-Q" to: https://www.sec.gov/cgi-bin/viewer?accession=...]
        [Hyperlink "earnings release" to: https://investor.company.com/news/q3-2024]
```

**HOW HYPERLINKS SHOULD APPEAR IN WORD:**
- Document names appear as blue, underlined clickable links
- Reader can Ctrl+Click to open source directly
- Not plain text URLs - formatted hyperlinks with display text

**REQUIRED SOURCES LIST (market-adjusted):**

Cite in every earnings update — substitute the local equivalent based on
`market_context.filings`:

- ✅ Earnings release / press release / 決算短信 (JP) / 業績公告 (HK) /
  重大訊息 (TW) (with date and URL)
- ✅ Quarterly/interim filing — local nomenclature:
  - US: **10-Q** (EDGAR link)
  - JP: **四半期報告書** (EDINET link)
  - TW: **季報 / 半年報** (MOPS link)
  - HK: **Interim Report** (HKEXnews link)
  - CN: **季度报告** (CNINFO link)
  - UK: **Half-year Report** + RNS announcement (LSE link)
  - EU: **Half-year Financial Report** (national OAM link)
- ✅ Earnings call transcript (with date) — note that some markets
  (esp. CN, JP) may publish primary-language transcripts only
- ✅ Investor presentation / supplemental materials (if available)
- ✅ Consensus estimates source — use `market_context.consensus_sources`:
  Bloomberg/FactSet for US/EU; TEJ for TW; Wind/Choice for CN; QUICK
  for JP; Refinitiv broadly. NEVER default to "Bloomberg sell-side
  consensus" without confirming local coverage.
- ✅ Prior guidance (from previous quarter's materials)
- ✅ FX assumptions if reporting currency ≠ analyst-house presentation
  currency (state spot rate and date used)

**REFERENCE SECTION WITH CLICKABLE HYPERLINKS:**

Include "Sources" section at end of report:

```
SOURCES & REFERENCES

Earnings Materials (Q3 2024):
• Earnings Release (November 7, 2024)
  [Hyperlink entire line to: https://investor.company.com/news/q3-2024-earnings]

• Form 10-Q (Filed November 8, 2024)
  [Hyperlink to: https://www.sec.gov/cgi-bin/viewer?accession=...]

• Earnings Call Transcript (November 7, 2024)
  [Hyperlink to: https://seekingalpha.com/article/...]

• Investor Presentation (November 7, 2024)
  [Hyperlink to: https://investor.company.com/presentations/q3-2024.pdf]
```

**VERIFICATION CHECKLIST:**
- [ ] Every figure has source with specific document and date
- [ ] Every table has source with document reference
- [ ] Beat/miss analysis cites consensus source with date
- [ ] Guidance changes cite current and prior guidance sources
- [ ] Key statistics have footnotes
- [ ] Sources section lists all materials with URLs
- [ ] ALL URLs are CLICKABLE HYPERLINKS (not plain text)
- [ ] All SEC filings hyperlinked to EDGAR viewer

### 5. Updated Estimates
- Update forward estimates based on results
- Show old vs. new estimates clearly
- Explain what changed and why

## High-Level Workflow

The earnings update process follows 5 phases:

### Phase 1: Data Collection (30-60 minutes)

**🚨🚨🚨 CRITICAL: TRAINING DATA IS OUTDATED 🚨🚨🚨**

**BEFORE STARTING - COMPLETE THESE 5 STEPS IN ORDER:**
1. **CHECK TODAY'S DATE** - Write down the current date
2. **CONFIRM MARKET CONTEXT** - Verify `market_context` was emitted by
   the `market-context` skill. Check fiscal calendar — for JP/AU/UK
   issuers, "Q1 FY25" may not map to calendar Q1.
3. **SEARCH FOR LATEST** - Use web search in the issuer's primary
   language AND English: "[Company] latest [quarterly/interim] results"
4. **VERIFY THE DATE** - Confirm release is within last 3 months
   (within 6 months for semi-annual markets like HK/UK/EU)
5. **CHECK TRANSCRIPT DATE** - Verify transcript date matches release
   date; note transcript-language constraints

**COMMON MISTAKES**:
- Using outdated earnings calls from training data instead of searching
  for the latest.
- Assuming a JP issuer's "Q1" = calendar Q1 — most JP issuers run
  Apr-Mar fiscal years.
- Searching for "10-Q" for an HK/UK issuer that doesn't file one.
- Pulling consensus from US sell-side databases when the issuer is
  primarily covered locally (e.g., A-shares covered on Wind/Choice).

**REQUIREMENTS:**
- ✅ Search for latest earnings - do NOT rely on training data
- ✅ Write down today's date and the release date found
- ✅ Verify release date is within 3 months of today
- ✅ Verify transcript date matches release date
- ✅ If dates don't match or are old (>3 months), search again

**See [references/workflow.md](references/workflow.md)** for detailed search procedures and verification steps.

### Phase 2: Analysis (2-3 hours)
- Beat/miss analysis for each key metric
- Segment/geographic/product breakdown
- Margin and guidance analysis
- Update financial model and estimates

**See [references/workflow.md](references/workflow.md)** for detailed analysis framework.

### Phase 3: Chart Generation (1-2 hours)
Create 8-12 charts focusing on quarterly trends and what's new:
- Quarterly revenue progression
- Quarterly EPS progression
- Quarterly margin trends
- Revenue by segment/geography
- Key operating metrics
- Beat/miss summary
- Estimate revisions
- Valuation charts

**See [references/workflow.md](references/workflow.md)** for chart specifications.

### Phase 4: Report Creation (2-3 hours)
Create 8-12 page DOCX report with specific structure.

**See [references/report-structure.md](references/report-structure.md)** for complete page-by-page templates and formatting requirements.

**High-level structure:**
- Page 1: Earnings summary with rating and price target
- Pages 2-3: Detailed results analysis
- Pages 4-5: Key metrics & guidance
- Pages 6-7: Updated investment thesis
- Pages 8-10: Valuation & estimates
- Pages 11-12: Appendix (optional)

### Phase 5: Quality Check & Delivery (30 minutes)
Verify content, formatting, accuracy, and timeliness before delivery.

**See [references/best-practices.md](references/best-practices.md)** for quality checklist and common mistakes to avoid.

## Output Specification

**Primary Deliverable**: DOCX report (8-12 pages)
**File Name**: `[Company]_[Period]_[Year]_Earnings_Update.docx`
**Examples**:
- US: `Nike_Q2_FY24_Earnings_Update.docx`
- TW: `TSMC_Q3_2024_Earnings_Update.docx`
- HK: `Tencent_1H_2024_Interim_Update.docx`
- JP: `Toyota_Q1_FY25_Tanshin_Update.docx`
- UK: `Shell_HY_2024_Interim_Update.docx`

**Contents:**
- Page 1: Summary with rating, price target, key takeaways
- Pages 2-3: Detailed results analysis
- Pages 4-5: Key metrics and guidance
- Pages 6-7: Updated thesis assessment
- Pages 8-10: Valuation and estimates
- Pages 11-12: Appendix (optional)
- 8-12 embedded charts
- 1-3 summary tables
- Complete sources section with clickable hyperlinks

**Optional Deliverable**: XLS model update (optional for earnings updates)

## Key Differences from Initiation Report

| Aspect | Earnings Update | Initiation Report |
|--------|----------------|-------------------|
| **Length** | 8-12 pages | 30-50 pages |
| **Words** | 3,000-5,000 | 10,000-15,000 |
| **Tables** | 1-3 summary | 12-20 comprehensive |
| **Figures** | 8-12 | 25-35 |
| **Turnaround** | 1-2 days | 3-6 weeks |
| **Scope** | Quarterly results | Complete company |
| **Focus** | What's NEW | Everything |
| **Company Background** | Brief mention | 6-10 pages |
| **XLS Model** | Optional | Required |

## Resources

### references/workflow.md
Detailed Phase 1-5 instructions with step-by-step procedures for data collection, analysis, chart generation, and report creation.

### references/report-structure.md
Complete page-by-page templates, table formats, and formatting requirements for the DOCX report.

### references/best-practices.md
Examples of good/bad headlines, tips for success, common mistakes to avoid, and comprehensive quality checklist.

## Dependencies

**Required:**
- Python (matplotlib, pandas, seaborn) for chart generation
- DOCX skill for report creation

**Optional:**
- XLS skill for model updates (not required for earnings updates)
