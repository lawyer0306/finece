---
name: market-context
description: Detect a security's home market from its ticker/ISIN/name and load the correct regulatory, accounting, fiscal, language, and disclosure rules for that market. ALWAYS invoke this FIRST before any equity-research workflow (earnings analysis, initiation, morning note, screen, etc.) so downstream skills use the correct filing sources, accounting standard, and fiscal calendar. Triggers on any non-US ticker, any ISIN, or whenever the user mentions a non-US company, exchange, or fiscal-year format (e.g., "FY24", "Q1 FY25", "中間期", "interim").
---

# Market Context Resolver

Resolves the home market of a security and emits a structured context object that downstream equity-research skills MUST consume before producing any deliverable.

## Why this skill is mandatory

The original Anthropic equity-research skills assume:
- US-listed company
- SEC EDGAR filings (10-K / 10-Q / 8-K)
- US GAAP
- Calendar-year quarters (Q1=Jan-Mar)
- USD reporting
- English-language materials

Outside the US, every one of those assumptions breaks. Producing a report
with the wrong filing template, wrong fiscal-quarter labeling, or wrong
accounting standard is a quality failure for institutional clients. This
skill prevents that.

## Inputs

Any one of:
- Ticker (with or without exchange suffix, e.g., `2330.TW`, `7203.T`, `0700.HK`, `AAPL`, `ASML.AS`)
- ISIN (e.g., `US0378331005`, `JP3633400001`, `TW0002330008`)
- Company legal name (English or local)
- Ticker without suffix + ambiguous → ask the user which exchange

## Resolution Procedure

### Step 1: Identify exchange / market

If suffix present, map directly:

| Suffix       | Market         | Notes                         |
|--------------|----------------|-------------------------------|
| (none) US    | US (NYSE/Nasdaq) | Default if 1-5 letter ticker |
| `.TW` / `.TWO` | Taiwan TWSE / TPEx |                          |
| `.HK`        | Hong Kong HKEX |                               |
| `.SS` / `.SH` | Shanghai SSE  |                               |
| `.SZ`        | Shenzhen SZSE  |                               |
| `.T`         | Tokyo TSE      |                               |
| `.KS` / `.KQ`  | Korea KRX / KOSDAQ |                          |
| `.L`         | London LSE     |                               |
| `.AS`        | Amsterdam Euronext |                           |
| `.PA`        | Paris Euronext |                               |
| `.DE` / `.F` | Deutsche Börse XETRA / Frankfurt |             |
| `.MI`        | Borsa Italiana |                               |
| `.MC`        | Madrid BME     |                               |
| `.SW`        | SIX Swiss      |                               |
| `.AX`        | ASX (Australia) |                              |
| `.SI`        | SGX (Singapore) |                              |
| `.NS` / `.BO` | NSE / BSE (India) |                            |
| `.TO` / `.V`  | Toronto / TSXV (Canada) |                     |
| `.MX`        | Mexico BMV     |                               |
| `.SA`        | B3 (Brazil)    |                               |

If ticker is unsuffixed and matches a US-listed name, treat as US. If
ambiguous, ask the user.

If ISIN is provided, the country code is the first two characters: `US`,
`TW`, `JP`, `HK`, `CN`, `GB`, `DE`, `FR`, `NL`, `KR`, `AU`, `SG`, `IN`,
`CA`, `BR`, `MX`, etc. Note ADRs use `US` ISIN despite foreign issuer —
in that case run cross-listing-analysis skill.

### Step 2: Emit Market Context object

Produce and surface (in your reasoning, not necessarily to the user) a
context object with these fields populated from the tables in
`references/markets.md`:

```yaml
market_context:
  ticker: "2330.TW"
  exchange: "TWSE"
  country: "TW"
  primary_listing: true
  cross_listings: ["TSM (NYSE ADR)"]
  reporting_currency: "TWD"
  accounting_standard: "TIFRS"           # IFRS as adopted in TW
  fiscal_year_end_default: "Dec-31"
  fiscal_period_labels: ["Q1","Q2","Q3","Q4"]   # or ["1H","FY"] for HK semi-annual
  filings:
    annual: "Annual Report (年報)"
    quarterly: "Quarterly Report (季報) - Q1/Q3"
    semi_annual: "Semi-Annual Report (半年報) - Q2"
    material: "Material Information (重大訊息)"
    primary_source_url: "https://mops.twse.com.tw/"
    consensus_sources: ["TEJ", "Bloomberg", "Refinitiv"]
  disclosure_regime:
    insider_trading: "Securities and Exchange Act Art. 157-1"
    selective_disclosure: "FSC selective-disclosure rule"
    quiet_period: "Per FSC and TWSE rules"
  language:
    official: "zh-TW"
    materials_typically_in: ["zh-TW", "en"]
  trading:
    timezone: "Asia/Taipei (UTC+8)"
    earnings_call_typical_time: "After-market local"
```

### Step 3: Hand off to downstream skill

Pass the `market_context` to whichever skill the user actually wants
(earnings-analysis, initiating-coverage, morning-note, etc.). Downstream
skills MUST:

1. Use `filings.primary_source_url` instead of EDGAR.
2. Use `filings.annual` / `quarterly` names instead of "10-K / 10-Q".
3. Apply `accounting_standard` to all reconciliation language.
4. Use `fiscal_period_labels` and `fiscal_year_end_default` when
   labeling charts.
5. Report all numbers in `reporting_currency`, with USD-equivalent in
   parentheses for cross-border audiences.
6. Cite consensus from `consensus_sources` (do NOT default to
   Bloomberg US sell-side).

## Common Pitfalls

- **Treating Hong Kong issuers as US**: HKEX issuers report semi-annually
  (interim + annual), NOT quarterly. Don't fabricate Q1/Q3 numbers.
- **Japanese fiscal years**: Many JP issuers have March year-end. "Q1 FY25"
  for a JP issuer means Apr-Jun 2025, not Jan-Mar.
- **A-shares vs H-shares**: Same issuer, different filings (CSRC vs HKEX),
  different accounting (China GAAP vs HKFRS), often different earnings
  release dates. Always confirm which line you're analyzing.
- **ADRs**: An ADR is US-listed but the underlying issuer reports under
  its home regime. Pull the home-country filing (e.g., 20-F is the annual
  for foreign private issuers; quarterly often via 6-K).
- **UK quarterly reporting**: Most UK Main Market issuers report
  semi-annually (interim + final) plus trading updates — not quarterly.
  Don't expect 10-Q-equivalents.
- **EU IFRS variations**: All EU issuers use IFRS as adopted by EU, but
  segment definitions and non-GAAP measures differ. Check Alt. Performance
  Measures (APM) reconciliations.

## Output to user

You don't need to dump the full context to the user. State briefly:

> "Resolving as TWSE-listed Taiwanese issuer (TIFRS, TWD reporting,
> calendar fiscal year). Sourcing filings from MOPS. Proceeding with
> earnings-analysis."

Then proceed.

## Resources

- `references/markets.md` — full per-market rule cards (filings, regulators,
  accounting, fiscal calendar, consensus sources, disclosure regime).
