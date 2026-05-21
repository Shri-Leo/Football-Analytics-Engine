from importlib.resources import files

import pandas as pd
import os
from glob import glob

RAW_PATH = "Data/Raw/Premier League/"
OUTPUT_PATH = "Data/Processed/epl_masters.csv"

def extract_season_from_filename(filename):
    base = os.path.basename(filename).replace(".csv", "")
    return base.replace("_","-")

def merge_seasons():
    files = glob(f"{RAW_PATH}*.csv")
    print("Files found:", len(files))
    all_dfs = []

    for file in files:
        df = pd.read_csv(file)

        season = extract_season_from_filename(file)
        df["season"] = season
        df["league"] = "EPL"

        all_dfs.append(df)

    master_df = pd.concat(all_dfs, ignore_index=True)

    master_df = master_df.sort_values(by="Date")

    master_df.to_csv(OUTPUT_PATH, index=False)
    print("Merged dataset saved successfully.")

if __name__ == "__main__":
    merge_seasons()
