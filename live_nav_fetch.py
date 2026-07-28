"""
Day 1 — Live NAV Fetch
Capstone Project I - Mutual Fund Analytics | Bluestock Fintech Internship

Fetches live NAV data from mfapi.in (free, no auth required) for the
primary fund plus 5 key benchmark schemes, and saves raw JSON responses
as CSV in data/raw/.

Usage:
    python live_nav_fetch.py
"""

import requests
import pandas as pd
from pathlib import Path

RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)

BASE_URL = "https://api.mfapi.in/mf"

# scheme_code -> label, as given in the Day 1 task
SCHEMES = {
    119018: "HDFC_Top_100_Direct",
    119598: "SBI_Bluechip",
    120586: "ICICI_Bluechip",
    118632: "Nippon_Large_Cap",
    120465: "Axis_Bluechip",
    120152: "Kotak_Bluechip",
}

def fetch_scheme(scheme_code: int) -> dict:
    """GET full NAV history for a scheme code from mfapi.in."""
    resp = requests.get(f"{BASE_URL}/{scheme_code}", timeout=15)
    resp.raise_for_status()
    return resp.json()


def save_nav_csv(scheme_code: int, label: str, payload: dict) -> None:
    meta = payload.get("meta", {})
    data = payload.get("data", [])
    df = pd.DataFrame(data)
    df["scheme_code"] = scheme_code
    df["scheme_name"] = meta.get("scheme_name")
    df["fund_house"] = meta.get("fund_house")

    out_path = RAW_DIR / f"nav_{scheme_code}_{label}.csv"
    df.to_csv(out_path, index=False)
    print(f"Saved {out_path} ({len(df)} rows) — actual scheme name: {meta.get('scheme_name')}")


def main():
    for scheme_code, label in SCHEMES.items():
        try:
            payload = fetch_scheme(scheme_code)
            save_nav_csv(scheme_code, label, payload)
        except requests.RequestException as e:
            print(f"Failed to fetch scheme {scheme_code} ({label}): {e}")


if __name__ == "__main__":
    main()

# ANOMALY NOTE (confirmed live on 23-07-2026 via api.mfapi.in/mf/125497/latest):
# Scheme code 125497 currently resolves to "SBI Small Cap Fund - Direct Plan
# - Growth" (SBI Mutual Fund), NOT "HDFC Top 100 Fund - Direct Plan - Growth"
# as labeled in the Day 1 task brief. Flag this to your PM (Yash Kale) before
# proceeding — either the scheme code in the brief is wrong, or the code
# has been reassigned. Do not assume the label; trust the API's scheme_name
# field and reconcile before building downstream analysis on it.
