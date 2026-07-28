# Mutual Fund Analytics Capstone Project
Bluestock Fintech Internship — End-to-End Data Analytics Workflow

## Project overview
This repository showcases a complete mutual fund analytics workflow built around data ingestion, live NAV retrieval, quality checks, and structured reporting. It is organized as a clean, presentation-ready project for review by a project manager or evaluator.

## What is included
- Data ingestion pipeline for the provided mutual fund datasets
- Live NAV fetching and evidence capture from the mfapi.in API
- Data quality summary and anomaly documentation
- Exploratory analysis structure in notebooks and SQL folders
- Dashboard and reporting folders ready for presentation

## Repository structure
```text
data/raw/          Source CSV/JSON files and fetched NAV data
data/processed/    Prepared datasets for analysis
notebooks/         Exploratory analysis and visualizations
sql/               SQL queries and transformations
dashboard/        Dashboard assets and app code
reports/           Summary reports and submission notes
```

## How to run
```bash
pip install -r requirements.txt
python data_ingestion.py
python live_nav_fetch.py
```

## Key files
- `data_ingestion.py` — ingests the provided fund-related CSV datasets
- `live_nav_fetch.py` — fetches live NAV information and saves output files
- `verify_nav.py` — validates fetched NAV data against the available inputs
- `data_quality_summary.txt` — summary of data quality checks and observations

## Notes for submission
The project is organized to be easy to review and explain. The repository contains the completed workflow, supporting files, and clear documentation for stakeholder presentation.

## Known anomaly observed
Scheme code 125497 is labeled as “HDFC Top 100 Direct” in the task brief, but the live API response returns a different fund identity. This discrepancy was documented and saved as part of the project evidence.
