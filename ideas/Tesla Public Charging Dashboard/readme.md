# Tesla Public Charging Dashboard

Personal dashboard to track public (non-home) charging sessions for my Tesla Model Y — sessions, energy added (kWh), estimated costs, and monthly summaries.

Built using Tesla Owner API (via refresh token) + TeslaFi for live state reference.  
Goal: lightweight, markdown-based reporting committed to GitHub, editable in Obsidian, with optional GitHub Actions automation.

## Features (planned)

- Fetch historical charging sessions via Tesla Owner API `/dx/charging/history`
- Filter public charging (Supercharger or location-based away from home coordinates)
- Calculate monthly totals: sessions, kWh added, spend (parsed from PDF invoices when available)
- Generate clean markdown tables → `dashboard.md`
- Secure credential handling via `.env` + GitHub Secrets

## Current Status

Early setup / proof-of-concept phase.  
API access confirmed (TeslaFi + Owner API tokens working).  
Basic data structures and endpoints identified from raw outputs.

## Prerequisites

- Python 3.10+
- Tesla Owner API refresh token (obtain via TeslaFi token page or Auth app)
- `.env` file (do **not** commit)

Example `.env`:

```env
TESLA_REFRESH_TOKEN=your_long_refresh_token_here
HOME_LAT=40.795          
HOME_LON=-73.131
