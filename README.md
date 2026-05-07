# Finece — Global Equity Research Plugin

Multi-market equity research toolkit for institutional analysts, packaged
as a Claude Cowork plugin. Forked and customized from
[Anthropic's `financial-services` repo](https://github.com/anthropics/financial-services)
(Apache 2.0).

The original Anthropic plugin assumes US-listed issuers, SEC EDGAR, US
GAAP, calendar quarters, and USD reporting. This fork generalizes the
workflow to handle the full institutional coverage universe — US,
EU/UK, Japan, Greater China (TW/HK/CN), Korea, ASEAN, Australia, India,
Canada, LatAm — with market-aware filing sources, accounting standards,
fiscal calendars, and disclosure regimes.

## Audience

Buy-side and sell-side analysts at institutions with global mandates,
multi-region coverage teams, and any desk where defaulting to "10-Q +
EDGAR + USD" is wrong.

## What's in the plugin

```
plugins/global-equity-research/
├── .claude-plugin/plugin.json
├── .mcp.json                       # placeholder for commercial data MCPs
├── commands/
│   ├── earnings.md                 # market-aware earnings update
│   ├── morning-note.md             # multi-region morning note
│   ├── cross-listing.md            # NEW: ADR / A+H analysis
│   ├── initiate.md
│   ├── earnings-preview.md
│   ├── catalysts.md
│   ├── model-update.md
│   ├── screen.md
│   ├── sector.md
│   └── thesis.md
└── skills/
    ├── market-context/             # NEW: ticker → market rules
    │   ├── SKILL.md
    │   └── references/markets.md
    ├── cross-listing-analysis/     # NEW: ADR / A+H / dual-primary
    │   └── SKILL.md
    ├── earnings-analysis/          # forked, multi-market
    ├── initiating-coverage/
    ├── morning-note/
    ├── earnings-preview/
    ├── catalyst-calendar/
    ├── sector-overview/
    ├── idea-generation/
    ├── model-update/
    └── thesis-tracker/
```

## What's different from upstream

| Area | Upstream `equity-research` | `global-equity-research` |
|------|----------------------------|--------------------------|
| Filing source | SEC EDGAR | Per-market (EDGAR, MOPS, EDINET, HKEXnews, CNINFO, RNS, OAM, DART, SEDAR+, B3, BMV) |
| Accounting | US GAAP | + IFRS, TIFRS, J-GAAP, K-IFRS, China CASBE, Ind AS, etc. |
| Fiscal calendar | Calendar Q1-Q4 | + Apr-Mar (JP), Jul-Jun (AU), variable UK |
| Reporting frequency | Quarterly | + Semi-annual (HK Main, UK, EU, AU) |
| Currency | USD | Multi-currency, FX-aware |
| Consensus source | Bloomberg/FactSet | + TEJ, Wind, Choice, QUICK, Refinitiv regional |
| Cross-listings | Not modeled | Dedicated `cross-listing-analysis` skill |
| Pre-flight | Implicit | Explicit `market-context` skill mandatory |

## Quick start (Claude Cowork)

1. Clone this repo or add it as a marketplace source in Cowork.
2. Enable the `global-equity-research` plugin from the Finece marketplace.
3. Try a command:
   - `/global-equity-research:earnings 2330.TW Q3 2024`
   - `/global-equity-research:earnings 7203.T Q1 FY25`
   - `/global-equity-research:earnings 0700.HK 1H 2024`
   - `/global-equity-research:cross-listing BABA`
   - `/global-equity-research:morning-note asia`
4. Claude will:
   - Run `market-context` first to resolve the ticker
   - Pull filings from the correct primary regulatory source
   - Use the right accounting standard, fiscal calendar, and currency
   - Cite local consensus sources where appropriate

## Roadmap (next steps for customization)

- **Commercial MCP connectors** in `.mcp.json`:
  Refinitiv Workspace, FactSet, S&P CapitalIQ, Wind, TEJ, QUICK
- **Additional skills**:
  - `regulatory-filings` — direct fetch from EDGAR / EDINET / MOPS APIs
  - `fx-translation` — automated multi-currency reporting
  - `peer-mapping` — global peer construction across exchanges
- **Localized output**: zh-TW / zh-CN / ja / ko report templates
- **Dual-language reports**: side-by-side EN + local press release

## Compliance disclaimer

Outputs from this plugin are analyst work product **for review by
qualified professionals**. Nothing here constitutes investment, legal,
tax, or accounting advice. The plugin does not make investment
recommendations, execute transactions, or approve onboarding — all
outputs require human sign-off.

Per-market disclosure rules vary; analysts must independently verify
compliance with FINRA / FCA / FSA / FSC / SFC / CSRC / SEBI / etc. when
publishing externally.

## License & attribution

Apache License 2.0 — see [`LICENSE`](LICENSE). Derivative-work
attribution and modifications are documented in [`NOTICE`](NOTICE).
The original upstream is Anthropic's
[`financial-services`](https://github.com/anthropics/financial-services).
