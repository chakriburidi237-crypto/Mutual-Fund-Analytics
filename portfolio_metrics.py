"""
Portfolio Analytics & Quantitative Metrics Engine
Calculates cumulative returns, rolling volatility, and Sharpe Ratios for ingested funds.
"""
from pathlib import Path
import pandas as pd
import numpy as np

BASE_DIR = Path(__file__).resolve().parent
RAW_DIR = BASE_DIR / "data" / "raw"

def compute_fund_metrics():
    nav_files = sorted(RAW_DIR.glob("nav_*.csv"))
    results = []

    for file_path in nav_files:
        try:
            df = pd.read_csv(file_path)
            if "nav" not in df.columns or len(df) < 5:
                continue

            df["date"] = pd.to_datetime(df["date"], errors="coerce")
            df = df.sort_values("date").reset_index(drop=True)
            df["returns"] = df["nav"].pct_change()

            total_return = (df["nav"].iloc[-1] - df["nav"].iloc[0]) / df["nav"].iloc[0] * 100
            annualized_vol = df["returns"].std() * np.sqrt(252) * 100
            sharpe_ratio = (df["returns"].mean() / df["returns"].std()) * np.sqrt(252) if df["returns"].std() != 0 else 0

            results.append({
                "Scheme": df["scheme_name"].iloc[0] if "scheme_name" in df.columns else file_path.stem,
                "Data Points": len(df),
                "Total Return (%)": round(total_return, 2),
                "Annualized Volatility (%)": round(annualized_vol, 2),
                "Sharpe Ratio": round(sharpe_ratio, 2)
            })
        except Exception as e:
            continue

    summary_df = pd.DataFrame(results)
    return summary_df

if __name__ == "__main__":
    print("=" * 70)
    print("MUTUAL FUND QUANTITATIVE PERFORMANCE SUMMARY")
    print("=" * 70)
    summary = compute_fund_metrics()
    print(summary.to_string(index=False))
