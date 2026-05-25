import pandas as pd

# =========================
# LEAGUE CONFIG
# =========================

LEAGUES = ["epl", "laliga", "seriea", "bundesliga", "ligue1"]

# =========================
# COLUMNS
# =========================

COLUMNS_TO_KEEP = ["Date", "HomeTeam", "AwayTeam", "FTHG", "FTAG", "FTR", "season", "league"]

COLUMN_MAPPING = {
    "Date": "date",
    "HomeTeam": "home_team",
    "AwayTeam": "away_team",
    "FTHG": "home_goals",
    "FTAG": "away_goals",
    "FTR": "result",
}

# =========================
# PREPROCESS FUNCTION
# =========================

def preprocess_league(league):
    input_path = (f"Data/Processed/"f"{league}_masters.csv")
    output_path = (f"Data/Processed/"f"{league}_clean.csv")

    print(f"\n===== {league.upper()} =====")

    df = pd.read_csv(input_path)

    df = df[COLUMNS_TO_KEEP]

    df = df.rename(columns=COLUMN_MAPPING)

    df["date"] = pd.to_datetime(df["date"], dayfirst=True)

    df = df.sort_values(by="date")

    df = df.reset_index(drop=True)

    df = df.dropna()

    df.to_csv(output_path, index=False)

    print(f"{league}_clean.csv created.")

    print("Total rows:", len(df))

# =========================
# RUN ALL LEAGUES
# =========================   

if __name__ == "__main__":

    for league in LEAGUES:
        preprocess_league(league)