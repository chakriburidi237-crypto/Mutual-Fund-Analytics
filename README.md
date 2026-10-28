# Mutual Fund Analytics

> **"Data-Driven Wealth Management. Automated ETL. Quantitative Portfolio Intelligence."**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.2%2B-150458.svg)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.26%2B-013243.svg)](https://numpy.org/)

Mutual Fund Analytics is a comprehensive financial data engineering, quantitative analysis, and reporting pipeline developed as an executive capstone project for the Bluestock Fintech Internship. It automates end-to-end investment data ingestion, integrates live Net Asset Value (NAV) retrieval from the official AMFI/mfapi APIs, executes multi-dimensional data quality audits, and computes key quantitative risk/return metrics (CAGR, Annualized Volatility, Sharpe Ratios, and SIP inflow trends).

---

## 🚀 Key Features

1. **Automated ETL Pipeline (`data_ingestion.py`)**: Seamlessly ingests, normalizes, and validates 10 heterogeneous financial datasets covering fund master catalogs, historical NAV records, AUM by fund house, category allocations, and portfolio holdings.
2. **Live AMFI NAV Ingestion (`live_nav_fetch.py`)**: Connects asynchronously to the `mfapi.in` REST API to fetch authoritative real-time daily Net Asset Values across leading asset management firms (HDFC, SBI, ICICI, Nippon, Axis, Kotak).
3. **Quantitative Metrics Engine (`portfolio_metrics.py`)**: Computes total returns, annualized volatility, risk-adjusted Sharpe Ratios, and tracking statistics to enable empirical fund ranking.
4. **Data Quality & Anomaly Audit (`data_quality_summary.txt`)**: Comprehensive anomaly logging identifying missing records, date discontinuities, and upstream scheme code discrepancies (such as Scheme Code `125497` naming conflicts in public registries).
5. **Reproducible Validation Suite (`verify_nav.py`)**: Programmatic integrity checks confirming scheme codes, fund houses, record lengths, and timestamp continuity.
6. **Executive Reporting Ready**: Structured storage architecture separating `data/raw/` immutable sources from clean downstream analytics for auditor and stakeholder review.

---

## 🛠 Tech Stack

- **Language**: Python 3.10+
- **Data Engineering & Analytics**: Pandas, NumPy, SciPy, SQLAlchemy
- **Data Visualization**: Matplotlib, Seaborn, Plotly
- **API & Networking**: Requests (REST API client with SSL validation)
- **Testing**: Pytest automated data validation test suite

---

## 🏗 Architecture & Directory Structure

```
Mutual-Fund-Analytics/
├── data/
│   ├── raw/                  # Ingested fund catalogs & live NAV timeseries
│   └── processed/            # Normalized datasets and analytics outputs
├── tests/
│   └── test_analytics.py     # Automated data schema and pipeline tests
├── data_ingestion.py         # Multi-dataset ETL ingestion script
├── live_nav_fetch.py         # Real-time AMFI API NAV fetcher
├── verify_nav.py             # NAV validation and sanity check script
├── portfolio_metrics.py      # Quantitative risk and Sharpe ratio calculator
├── data_quality_summary.txt  # Audit observations and anomaly disclosures
├── requirements.txt          # Python dependencies
├── .gitattributes            # Language definition ensuring Python attribution
├── .gitignore                # Ignored cache and virtualenv files
├── LICENSE                   # MIT License
└── README.md                 # Project documentation
```

---

## ⚡ Getting Started

### Prerequisites

- Python `3.10`, `3.11`, or `3.12`
- `pip` package manager

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/chakriburidi237-crypto/Mutual-Fund-Analytics.git
   cd Mutual-Fund-Analytics
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute the pipeline:
   ```bash
   # Run initial ETL ingestion
   python data_ingestion.py

   # Fetch live NAV data
   python live_nav_fetch.py

   # Validate ingested files
   python verify_nav.py

   # Compute quantitative portfolio metrics
   python portfolio_metrics.py
   ```

---

## 🧪 Automated Testing

Run the automated test suite to verify dataset schemas, record integrity, and columns:

```bash
pytest tests/ -v
```

Expected output:
```
tests/test_analytics.py::test_data_directory_structure PASSED
tests/test_analytics.py::test_fund_master_schema PASSED
tests/test_analytics.py::test_nav_history_validity PASSED
tests/test_analytics.py::test_single_fund_nav_format PASSED
======================== 4 passed in 0.38s ========================
```

---

## 📊 Sample Quantitative Output

```
======================================================================
MUTUAL FUND QUANTITATIVE PERFORMANCE SUMMARY
======================================================================
Scheme                     Data Points  Total Return (%)  Ann. Volatility (%)  Sharpe Ratio
HDFC Top 100 Direct               2982            318.45                14.82          1.24
SBI Bluechip Direct               2840            287.12                13.91          1.18
ICICI Bluechip Direct             2950            304.80                14.20          1.21
Nippon Large Cap Direct           2890            342.15                15.40          1.30
```

---

## 📄 License

MIT License © 2026 Chakradhar Buridi. Developed for the Bluestock Fintech Capstone Internship.
