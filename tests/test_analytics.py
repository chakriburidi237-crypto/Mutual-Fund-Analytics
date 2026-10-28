import pytest
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"

def test_data_directory_structure():
    assert RAW_DIR.exists(), "Raw data directory must exist"
    csv_files = list(RAW_DIR.glob("*.csv"))
    assert len(csv_files) >= 10, f"Expected at least 10 raw CSV files, found {len(csv_files)}"

def test_fund_master_schema():
    fund_master = RAW_DIR / "01_fund_master.csv"
    if fund_master.exists():
        df = pd.read_csv(fund_master)
        assert len(df) > 0
        assert "scheme_code" in df.columns or "Scheme_Code" in df.columns or "scheme_name" in df.columns

def test_nav_history_validity():
    nav_file = RAW_DIR / "02_nav_history.csv"
    if nav_file.exists():
        df = pd.read_csv(nav_file)
        assert len(df) > 0
        assert "nav" in [c.lower() for c in df.columns]

def test_single_fund_nav_format():
    sample_nav = RAW_DIR / "nav_119018_HDFC_Top_100_Direct.csv"
    if sample_nav.exists():
        df = pd.read_csv(sample_nav)
        assert "scheme_name" in df.columns
        assert "nav" in df.columns
        assert len(df) > 0
