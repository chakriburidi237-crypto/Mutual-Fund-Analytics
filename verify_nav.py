import pandas as pd

files = [
    "data/raw/nav_119018_HDFC_Top_100_Direct.csv",
    "data/raw/nav_119598_SBI_Bluechip.csv",
    "data/raw/nav_120586_ICICI_Bluechip.csv",
    "data/raw/nav_118632_Nippon_Large_Cap.csv",
    "data/raw/nav_120465_Axis_Bluechip.csv",
    "data/raw/nav_120152_Kotak_Bluechip.csv",
]

for f in files:
    df = pd.read_csv(f)
    print("\nFILE:", f)
    print("Scheme:", df["scheme_name"].iloc[0])
    print("Fund House:", df["fund_house"].iloc[0])
    print("Rows:", len(df))