# Per-Market Reference Cards

Authoritative per-market rule cards. The `market-context` skill loads the
relevant card and emits structured data for downstream skills.

> Notes: Always verify regulator URLs and disclosure rules against the
> primary source before publishing client-facing material — regulations
> change. The information here is a starting set, not legal advice.

---

## United States — NYSE / Nasdaq

- **Country**: US
- **Currency**: USD
- **Accounting**: US GAAP (FPIs may file IFRS via 20-F)
- **Fiscal year**: Calendar year is most common; tech often Jun/Sep
- **Quarterly reporting**: Yes (10-Q for Q1-Q3, 10-K for FY)
- **Filings**:
  - Annual: **10-K** (or **20-F** for foreign private issuers)
  - Quarterly: **10-Q**
  - Material: **8-K**
  - Proxy: **DEF 14A**
- **Primary source**: https://www.sec.gov/edgar (EDGAR full-text search)
- **Regulator**: SEC
- **Consensus sources**: Bloomberg, FactSet, Refinitiv, S&P CapitalIQ,
  Visible Alpha
- **Disclosure regime**: Reg FD (selective disclosure prohibited),
  insider trading: Section 10(b)/Rule 10b-5, MNPI rules
- **Quiet period**: Typically 2-4 weeks pre-earnings (varies by issuer)
- **Earnings call**: Usually same day as release; many before-market
  (BMO) or after-market (AMC) US Eastern

---

## Taiwan — TWSE / TPEx

- **Country**: TW
- **Currency**: TWD
- **Accounting**: TIFRS (IFRS as endorsed by FSC)
- **Fiscal year**: Almost all calendar year (Dec-31)
- **Quarterly reporting**: Yes since 2013
- **Filings**:
  - Annual: **年報 / Annual Report** (45-day rule for consolidated FS)
  - Quarterly: **季報 / Quarterly Report** (Q1, Q3)
  - Semi-annual: **半年報** (Q2 / interim)
  - Material: **重大訊息 / Material Information** (T+0 disclosure)
- **Primary source**: https://mops.twse.com.tw/ (公開資訊觀測站 / MOPS)
- **Regulator**: 金管會 (FSC)
- **Consensus sources**: TEJ (台灣經濟新報), Bloomberg, Refinitiv, MoneyDJ
- **Disclosure regime**: Securities and Exchange Act Art. 157-1
  (insider trading); selective-disclosure prohibited per FSC rules
- **Earnings call**: Investor conferences; transcripts often Chinese-only
  with select English summaries
- **Reporting deadlines**: Q1/Q3 within 45 days of quarter-end; semi-annual
  60 days; annual 4 months

---

## Hong Kong — HKEX

- **Country**: HK
- **Currency**: HKD (many issuers report in CNY, USD)
- **Accounting**: HKFRS (substantively converged with IFRS) — Mainland
  enterprises listed in HK may also prepare CASBE statements
- **Fiscal year**: Often Dec-31; some Mar-31 (esp. for issuers with
  Mainland parents)
- **Quarterly reporting**: NO — semi-annual is standard
- **Filings**:
  - Annual: **Annual Report**
  - Interim: **Interim Report** (semi-annual)
  - Material: **Inside Information / Voluntary Announcement** via HKEXnews
  - Quarterly is only required for **GEM** (formerly Growth Enterprise
    Market) issuers
- **Primary source**: https://www.hkexnews.hk/ (披露易)
- **Regulator**: SFC (Securities and Futures Commission); HKEX (listing)
- **Consensus sources**: Bloomberg, Refinitiv, S&P CapIQ, Wind (for
  Mainland-cross), HSBC and CICC research
- **Disclosure regime**: Securities and Futures Ordinance (SFO) Pt XIVA
  (inside information); MMT (Market Misconduct Tribunal)

---

## Mainland China — Shanghai SSE / Shenzhen SZSE

- **Country**: CN
- **Currency**: CNY (RMB)
- **Accounting**: CASBE (China GAAP — substantively IFRS-converged but
  not identical; some standards differ on consolidation, related-party,
  fair value)
- **Fiscal year**: Calendar year (Dec-31)
- **Quarterly reporting**: Yes
- **Filings**:
  - Annual: **年度报告**
  - Quarterly: **季度报告** (Q1, Q3)
  - Semi-annual: **半年度报告**
  - Material: **临时公告 / Interim Announcement**
- **Primary source**: http://www.cninfo.com.cn/ (巨潮资讯) — also SSE/SZSE
  exchange sites; STAR Market and ChiNext have additional disclosure
- **Regulator**: CSRC (中国证监会)
- **Consensus sources**: Wind, Choice (东方财富), CSMAR, Bloomberg
- **Notes**: A-share filings are CN-language; many large issuers also
  publish English summaries. STAR Board (科创板) and ChiNext (创业板) have
  registration-based listing and richer R&D disclosure. Watch for SOE
  state-ownership disclosures.

---

## Japan — TSE (Prime / Standard / Growth)

- **Country**: JP
- **Currency**: JPY
- **Accounting**: J-GAAP (default), IFRS (~250+ issuers as of mid-2020s),
  US GAAP (handful of issuers)
- **Fiscal year**: Most common is **April-March** (FY ending Mar-31).
  "FY24" means year ending Mar-2024 (or Mar-2025 depending on issuer
  convention — confirm)
- **Quarterly reporting**: Yes — quarterly Tanshin (短信)
- **Filings**:
  - Annual: **有価証券報告書 (Yukashoken Houkokusho)** — comprehensive
    annual filing (~3 months after FYE)
  - Quarterly: **四半期報告書 (Shihanki Houkokusho)** — quarterly
  - Earnings flash: **決算短信 (Kessan Tanshin)** — released quickly,
    similar to 8-K earnings release
  - Material: TDnet timely disclosure
- **Primary sources**:
  - https://disclosure.edinet-fsa.go.jp/ (EDINET — official FSA filing)
  - https://www.release.tdnet.info/ (TDnet — exchange timely disclosure)
- **Regulator**: FSA (金融庁), TSE
- **Consensus sources**: Bloomberg, QUICK, Refinitiv, Toyo Keizai
- **Earnings call**: Increasingly common; many materials JA-only or
  bilingual; Tanshin format is standardized
- **Notes**: Q1 = Apr-Jun for Mar-FYE issuers — never assume calendar
  Q1 = Jan-Mar for Japanese stocks without checking

---

## Korea — KRX (KOSPI / KOSDAQ)

- **Country**: KR
- **Currency**: KRW
- **Accounting**: K-IFRS (mandatory since 2011 for listed companies)
- **Fiscal year**: Calendar year (Dec-31) for most
- **Quarterly reporting**: Yes
- **Filings**:
  - Annual: **사업보고서 (Annual Business Report)**
  - Quarterly: **분기보고서**
  - Semi-annual: **반기보고서**
  - Material: **공시 (DART disclosure)**
- **Primary source**: https://dart.fss.or.kr/ (DART — FSS regulatory
  filings)
- **Regulator**: FSS (Financial Supervisory Service), FSC, KRX
- **Consensus sources**: Bloomberg, Refinitiv, Mirae Asset, NH, Samsung
  Securities, Korea Investment

---

## United Kingdom — LSE Main Market / AIM

- **Country**: GB
- **Currency**: GBP (some report in USD/EUR)
- **Accounting**: UK-adopted IFRS (UK left EU IFRS endorsement post-Brexit
  but remains substantively IFRS); FRS 102 for some smaller issuers
- **Fiscal year**: Mixed — common year-ends include Mar-31, Jun-30,
  Dec-31
- **Quarterly reporting**: NO — semi-annual is standard (interim + final).
  Trading updates / Q1 IMS optional
- **Filings**:
  - Annual: **Annual Report and Accounts**
  - Interim: **Half-year Report**
  - Trading updates / pre-close statements (voluntary)
  - Regulatory news via **RNS** (Regulatory News Service)
- **Primary sources**:
  - https://find-and-update.company-information.service.gov.uk/ (Companies
    House)
  - https://www.londonstockexchange.com/news (LSE RNS)
  - National Storage Mechanism for prospectuses
- **Regulator**: FCA (Financial Conduct Authority)
- **Consensus sources**: Bloomberg, Refinitiv, Vuma Financial
- **Disclosure regime**: UK MAR (Market Abuse Regulation, retained EU law)

---

## Eurozone — Euronext / XETRA / Borsa Italiana / BME / etc.

- **Country**: EU member states
- **Currency**: EUR (mostly)
- **Accounting**: IFRS as adopted by EU (mandatory for listed groups'
  consolidated FS)
- **Fiscal year**: Calendar year is most common
- **Quarterly reporting**: NO mandatory quarterly under Transparency
  Directive (since 2013 amendment) — half-year + annual is the floor.
  Many large issuers voluntarily publish quarterly trading updates or
  Q1/Q3 statements
- **Filings**:
  - Annual: **Universal Registration Document (URD)** or **Annual
    Financial Report**
  - Half-year Financial Report
  - Issuer-specific quarterly statements (voluntary)
  - Material: **Inside Information** via national OAM (Officially
    Appointed Mechanism)
- **Primary sources**:
  - National OAMs (BaFin / AMF / CONSOB / CNMV / AFM)
  - https://www.esma.europa.eu/ (ESMA — pan-EU)
  - Issuer IR sites
- **Regulator**: National regulators + ESMA at EU level
- **Disclosure regime**: EU MAR (Market Abuse Regulation, Regulation
  596/2014); MiFID II for research

---

## Singapore — SGX

- **Country**: SG
- **Currency**: SGD (many in USD)
- **Accounting**: SFRS(I) (Singapore-adopted IFRS)
- **Quarterly reporting**: Tiered — required for issuers above market-cap
  thresholds and certain risk categories; many smaller issuers
  semi-annual only (post-2020 SGX rule change)
- **Primary source**: https://www.sgx.com/securities/company-disclosures
- **Regulator**: MAS (Monetary Authority of Singapore), SGX

---

## Australia — ASX

- **Country**: AU
- **Currency**: AUD
- **Accounting**: AAS (Australian Accounting Standards, IFRS-equivalent)
- **Fiscal year**: Often **July-June** (FY ending Jun-30) for Australian
  issuers
- **Quarterly reporting**: NO mandatory — half-year + annual; quarterly
  cash-flow report (Appendix 4C) required for early-stage / mining issuers
- **Filings**:
  - Annual: **Annual Report**, Appendix 4E (preliminary final)
  - Half-year: Appendix 4D
  - Material: ASX continuous-disclosure announcements
- **Primary source**: https://www.asx.com.au/asx/v2/statistics/announcements.do
- **Regulator**: ASIC, ASX

---

## India — NSE / BSE

- **Country**: IN
- **Currency**: INR
- **Accounting**: Ind AS (IFRS-converged)
- **Fiscal year**: Apr-Mar
- **Quarterly reporting**: Yes
- **Filings**:
  - Annual report
  - Quarterly results (filed within 45 days)
  - Material: BSE/NSE announcements
- **Primary sources**: https://www.bseindia.com/, https://www.nseindia.com/
- **Regulator**: SEBI

---

## Canada — TSX / TSXV / CSE

- **Country**: CA
- **Currency**: CAD (many cross-listed report USD)
- **Accounting**: IFRS for public companies (since 2011)
- **Quarterly reporting**: Yes
- **Filings**:
  - Annual Information Form (AIF), MD&A, Annual Financial Statements
  - Interim Financial Statements (quarterly)
  - Material Change Report
- **Primary source**: https://www.sedarplus.ca/ (SEDAR+)
- **Regulator**: Provincial regulators (CSA umbrella)

---

## Brazil — B3

- **Country**: BR
- **Currency**: BRL
- **Accounting**: BR-GAAP (IFRS-converged for listed)
- **Filings**: ITR (quarterly), DFP (annual), Formulário de Referência
- **Primary source**: https://www.gov.br/cvm/ (CVM); B3 IPE
- **Regulator**: CVM

---

## Mexico — BMV

- **Country**: MX
- **Currency**: MXN
- **Accounting**: NIF (IFRS-converged for listed since 2012)
- **Filings**: Quarterly, annual; **Reporte Anual**
- **Primary source**: https://www.bmv.com.mx/, CNBV STIV-2
- **Regulator**: CNBV

---

## Universal Reminders

1. **Always verify the issuer's actual fiscal year-end** — never assume.
2. **For dual-listed issuers**, decide which line you're covering — A vs H,
   underlying vs ADR, primary vs secondary listing.
3. **Currency-of-record vs presentation currency** can differ — many
   global issuers report in USD or EUR despite domestic listing.
4. **Local-language press releases** may include material that English
   summaries omit; for non-EN markets always cross-check primary-language
   release.
5. **Translation of financial terminology** is non-trivial — e.g., 营业
   收入 (operating revenue, CN) vs 売上高 (net sales, JP) vs revenue (US)
   are not always definitionally identical.
