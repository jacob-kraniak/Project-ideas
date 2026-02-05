# Project: Self-Hosted Personal Finance Dashboard and Reporting System

## Origin
- Grok conversation: https://grok.com/c/9358fe2c-8314-4a35-a4b8-c3cdc124cac2?rid=d2737c70-c21d-41e5-9eb3-aa9e47c1151c
- Date brainstormed: 2026-02-05
- Tags: #finance #self-hosted #privacy #dashboard #automation #data-pipeline #home-lab

## Problem / Goal
Current tools like Fidelity FullView provide consolidated visibility into bank accounts, credit cards, and investments but lack reliability, robustness, and full customization. Manual spreadsheets require excessive data entry. The goal is to create a personally managed single source of truth for all financial data sources, enabling business-like reporting (balance sheet, income statement, budgets, SG&A, investments) with monthly/quarterly family reviews, while prioritizing data privacy and ownership.

## Proposed Solution
Build a local-first or self-hosted personal finance system starting with desktop/local deployment, ingesting transaction data via periodic CSV exports from institutions (Capital One, Fidelity, Chase, Citibank). Use data processing tools for standardization, categorization, and reporting. Explore Actual Budget for core budgeting and reporting, with optional future server self-hosting (via Docker) for multi-device sync and automation bridges (e.g., SimpleFIN). Emphasize privacy through local data storage, no third-party cloud dependencies for core functionality, and secure storage (e.g., Proton Drive sync).

## Tech Stack (planned)
- Language(s): JavaScript/TypeScript (Actual Budget core); optional Python for custom processing
- Core libraries / frameworks: Actual Budget (desktop/server), pandas (Python alternative for CSV ETL if extending beyond Actual)
- Deployment target / environment: Local Linux desktop (desktop app); future Docker container on local server
- Data sources / integrations (if any): Manual CSV exports from Capital One 360, Fidelity, Chase, Citibank; optional SimpleFIN bridge for automated imports

## Key Features / Scope
**Must-have:**
- Local/offline storage and operation of all financial data
- Import and standardization of transaction CSVs from multiple institutions
- Custom views/reports: balance sheet, income statement, budgets, investment tracking
- Envelope-style budgeting and categorization rules

**Nice-to-have / future:**
- Docker-based self-hosted server for multi-device access
- Automated daily transaction sync via SimpleFIN or similar
- Advanced analytics/visualizations (e.g., Python + Matplotlib/Plotly exports)
- Family-shared read-only views or PDF reports

## Challenges & Open Questions
- Reliability and completeness of manual CSV exports across institutions
- Mapping inconsistent transaction descriptions to consistent categories
- Balancing simplicity of Actual Budget vs. need for custom business-style financial statements
- Feasibility and cost of automated bridges like SimpleFIN for U.S. banks

## Next Steps
- [ ] Install and evaluate Actual Budget desktop app on Linux (Flathub)
- [ ] Export sample CSVs from all accounts and test import/categorization
- [ ] Build prototype reports (balance sheet, income statement) within Actual or via Python/pandas
- [ ] Create dedicated repo (when POC is validated)

## Priority / Effort
- Priority: High (addresses ongoing financial visibility and manual effort pain points for family management)
- Estimated effort to minimal POC: 1–2 weekends (10–20 hours)

## Updates / Log
- [2026-02-05]: Initial brainstorm with Grok – core concept defined, focus on Actual Budget local deployment and CSV-based ingestion

## GitHub Tracking
- Issue: (create in repo and link here after commit, e.g. [#1](https://github.com/jacob-kraniak/Project-ideas/issues/1))
- Project board card: (add to Grok Ideas Pipeline board and link here)
