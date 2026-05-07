# Finece — Repo Guidance for Claude

This is a customized Claude Cowork plugin for **multi-market equity
research**, forked from Anthropic's
[`financial-services`](https://github.com/anthropics/financial-services)
under Apache 2.0.

## Repo Structure

```
.claude-plugin/marketplace.json     # Cowork marketplace manifest
plugins/
└── global-equity-research/         # The customized plugin
    ├── .claude-plugin/plugin.json
    ├── .mcp.json                   # data-connector placeholder
    ├── commands/                   # /global-equity-research:<cmd>
    └── skills/
        ├── market-context/         # NEW — must run first for any analysis
        ├── cross-listing-analysis/ # NEW — ADR / A+H / dual-primary
        ├── earnings-analysis/      # forked, market-aware
        └── ...                     # other forked skills
LICENSE                             # Apache 2.0 (preserved from upstream)
NOTICE                              # attribution + modification log
README.md
```

## Editing Workflow

1. **Edit markdown directly** — no build step. Changes take effect on
   next plugin reload in Cowork.
2. **Always run `market-context` first** in any command flow that
   touches a specific issuer. Downstream skills depend on its output.
3. **When adding a new market** (e.g., Vietnam HOSE, Indonesia IDX):
   - Add a rule card to
     `plugins/global-equity-research/skills/market-context/references/markets.md`
   - Add the ticker suffix to the suffix table in `SKILL.md`
   - Add any market-specific filing/transcript URLs to `.mcp.json`
     when wiring connectors
4. **When adding a new skill**: create `skills/<name>/SKILL.md` with
   YAML frontmatter (`name`, `description`). Description must be
   specific enough that Claude auto-loads it on the right triggers.
5. **When adding a new command**: create `commands/<name>.md` with
   `description` and `argument-hint`. The body is the prompt template.
6. **Cite primary regulatory sources** in any client-facing output —
   never just news aggregators.

## Important Conventions

- **Do not assume US/USD/GAAP** anywhere. The plugin's value
  proposition is being correct on non-US issuers; defaulting to US
  conventions is a quality failure.
- **Currency** in all charts/tables: reporting currency is primary,
  USD-equivalent only where it aids cross-border comparison. Always
  state spot FX and date.
- **Fiscal periods**: use the issuer's actual labeling
  (e.g., "Q1 FY25 (Apr-Jun 2024)" for a Mar-FYE Japanese issuer).
- **Local language**: cross-check primary-language press releases for
  material content omitted from English summaries.

## Compliance

Every report includes a disclaimer: outputs are analyst work product
requiring qualified-professional review. Do not produce material that
could be construed as investment recommendations to retail audiences
without proper regulatory review (FINRA Rule 2241, MiFID II, FCA COBS,
local equivalents).
