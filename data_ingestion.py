"""
Day 1 — Data Ingestion (ETL)
Capstone Project I - Mutual Fund Analytics | Bluestock Fintech Internship

Loads the 10 provided CSV datasets, prints shape/dtypes/head for each,
explores the fund master, and validates AMFI scheme codes against
nav_history.

Usage:
    python data_ingestion.py

Expected input:
    Place all 10 provided CSVs in ./data/raw/ before running.
    (One of them must be named/contain the fund master and one must
    be named/contain nav_history — adjust FUND_MASTER_FILE and
    NAV_HISTORY_FILE below to match the actual filenames you were given.)
"""

import pandas as pd
from pathlib import Path

RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

FUND_MASTER_FILE = "01_fund_master.csv"
NAV_HISTORY_FILE = "02_nav_history.csv"


def load_all_csvs(raw_dir: Path) -> dict[str, pd.DataFrame]:
    """Load every CSV in raw_dir, printing shape/dtypes/head for each."""
    csv_paths = sorted(raw_dir.glob("*.csv"))
    if not csv_paths:
        print(f"No CSVs found in {raw_dir}/ — add the 10 provided files here first.")
        return {}

    frames = {}
    for path in csv_paths:
        df = pd.read_csv(path)
        frames[path.stem] = df
        print(f"\n=== {path.name} ===")
        print("shape:", df.shape)
        print("dtypes:\n", df.dtypes)
        print("head:\n", df.head())
    return frames


def explore_fund_master(frames: dict[str, pd.DataFrame]) -> None:
    fm = frames.get(Path(FUND_MASTER_FILE).stem)
    if fm is None:
        print(f"\nFund master file '{FUND_MASTER_FILE}' not found among loaded CSVs.")
        return

    print("\n=== Fund Master exploration ===")
    for col in ["fund_house", "category", "sub_category", "risk_category"]:
        if col in fm.columns:
            print(f"\nUnique {col}:")
            print(fm[col].unique())
        else:
            print(f"\nColumn '{col}' not present in fund master — check actual column names.")


def validate_amfi_codes(frames: dict[str, pd.DataFrame]) -> None:
    fm = frames.get(Path(FUND_MASTER_FILE).stem)
    nav = frames.get(Path(NAV_HISTORY_FILE).stem)
    if fm is None or nav is None:
        print("\nSkipping AMFI code validation — fund master or nav_history not loaded.")
        return

    code_col_fm = "amfi_code" if "amfi_code" in fm.columns else fm.columns[0]
    code_col_nav = "amfi_code" if "amfi_code" in nav.columns else nav.columns[0]

    fm_codes = set(fm[code_col_fm])
    nav_codes = set(nav[code_col_nav])
    missing = fm_codes - nav_codes

    print("\n=== AMFI code validation ===")
    print(f"Fund master codes: {len(fm_codes)}")
    print(f"NAV history codes: {len(nav_codes)}")
    print(f"Fund master codes missing from nav_history: {len(missing)}")
    if missing:
        print("Missing codes sample:", list(missing)[:10])

    print("\nData quality summary:")
    print(f"- {len(fm_codes) - len(missing)}/{len(fm_codes)} fund master codes have matching NAV history.")
    print("- Review any missing codes above for delisted/renamed schemes.")


if __name__ == "__main__":
    frames = load_all_csvs(RAW_DIR)
    explore_fund_master(frames)
    validate_amfi_codes(frames)
