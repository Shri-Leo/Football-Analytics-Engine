import pandas as pd
import os
from glob import glob

# =========================
# LEAGUE CONFIG
# =========================

LEAGUES = {
    "epl": "Premier League",
    "laliga": "La Liga",
    "seriea": "Serie A",
    "bundesliga": "Bundesliga",
    "ligue1": "Ligue 1"
}

# =========================
# EXTRACT SEASON
# =========================

def extract_season_from_filename(filename):

    base = os.path.basename(filename)

    base = base.replace(".csv", "")

    return base.replace("_", "-")

# =========================
# MERGE FUNCTION
# =========================

def merge_league(league_code, folder_name):

    raw_path = f"Data/Raw/{folder_name}/"

    output_path = (
        f"Data/Processed/"
        f"{league_code}_masters.csv"
    )

    files = glob(f"{raw_path}*.csv")

    print(f"\n===== {league_code.upper()} =====")
    print("Files found:", len(files))

    all_dfs = []

    for file in files:

        df = pd.read_csv(file)

        season = extract_season_from_filename(file)

        df["season"] = season
        df["league"] = league_code

        all_dfs.append(df)

    master_df = pd.concat( all_dfs, ignore_index=True )

    master_df = master_df.sort_values( by="Date" )

    master_df.to_csv( output_path, index=False )

    print( f"{league_code} merged successfully." )

# =========================
# RUN ALL LEAGUES
# =========================

if __name__ == "__main__":

    for league_code, folder_name in LEAGUES.items():

        merge_league( league_code, folder_name )