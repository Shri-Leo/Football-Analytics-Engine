import pandas as pd

INPUT_PATH = "Data/Processed/epl_masters.csv"
OUTPUT_PATH = "Data/Processed/epl_clean.csv"

COLUMNS_TO_KEEP = ["Date", "HomeTeam", "AwayTeam", "FTHG", "FTAG", "FTR", "season", "league"]

COLUMN_MAPPING = {
    "Date": "date",
    "HomeTeam": "home_team",
    "AwayTeam": "away_team",
    "FTHG": "home_goals",
    "FTAG": "away_goals",
    "FTR": "result"
}

def preprocess():
    df = pd.read_csv(INPUT_PATH)

    df = df[COLUMNS_TO_KEEP]

    df = df.rename(columns=COLUMN_MAPPING)

    df["date"] = pd.to_datetime(df["date"], dayfirst=True)

    df = df.sort_values(by="date")

    df = df.reset_index(drop=True)

    df = df.dropna()

    df.to_csv(OUTPUT_PATH, index=False)

    print("Clean dataset saved successfully.")
    print("Toal rows:", len(df))

if __name__ == "__main__":
    preprocess()