# Capstone Project I - Mutual Fund Analytics
Bluestock Fintech Internship — Day 1: Project Setup + Data Ingestion (ETL)

## Structure
```
data/raw/         raw input CSVs + fetched NAV data
data/processed/   cleaned/derived datasets
notebooks/        exploratory analysis
sql/              queries
dashboard/        dashboard code/assets
reports/          write-ups, summaries
```

## Setup
```bash
pip install -r requirements.txt
```

## Day 1 tasks
1. Place the 10 provided CSVs in `data/raw/`, then run:
   ```bash
   python data_ingestion.py
   ```
2. Fetch live NAV data:
   ```bash
   python live_nav_fetch.py
   ```

## Known anomaly (flag to PM)
Scheme code **125497** is labeled "HDFC Top 100 Direct" in the task
brief, but the live mfapi.in API returns **SBI Small Cap Fund - Direct
Plan - Growth** for that code (confirmed independently on 23-07-2026
and 24-07-2026, via both the `/latest` and full-history endpoints —
ISIN `INF200K01T51`).

**Likely root cause:** the API's own documentation example (in its
OpenAPI spec) shows a hardcoded sample response for scheme_code 125497
labeled "HDFC Top..." with a NAV around 892 — but this does not match
what the live endpoint actually returns for that code (NAV ~200-210,
SBI Small Cap Fund). The task brief appears to have inherited the
scheme name from that stale/illustrative doc example rather than a
live API call. Treat the live endpoint as ground truth; raw evidence
saved in `data/raw/nav_125497_sample.csv`, `nav_125497_raw.json`, and
the docs page source itself in `data/raw/mfapi_docs_evidence.html`
(see the hardcoded example under "Response Examples" — scheme_code
125497, "HDFC Top 100 Fund", NAV 892.45600 — which does not match the
live endpoint's actual response for that code).

Reconcile with Yash Kale before treating this scheme as HDFC Top 100
in any analysis.
