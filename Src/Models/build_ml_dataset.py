import pandas as pd

LEAGUES = ["epl", "laliga", "seriea", "bundesliga", "ligue1"]

all_rows = []

for league in LEAGUES:

    print(f"\n===== {league.upper()} =====")

    matches = pd.read_csv(f"Data/Processed/{league}_clean.csv")

    strengths = pd.read_csv(f"Data/Processed/{league}_team_strengths.csv", index_col=0)

    elo = pd.read_csv(f"Data/Processed/{league}_elo.csv")

    form = pd.read_csv(f"Data/Processed/{league}_form.csv")

    for _, match in matches.iterrows():

        home_team = match["home_team"]
        away_team = match["away_team"]

        # Skip if team missing
        if (
            home_team not in strengths.index
            or
            away_team not in strengths.index
        ):
            continue

        try:

            row = {

                "league": league,

                "home_attack": strengths.loc[home_team, "home_attack_strength"],

                "home_defense": strengths.loc[home_team, "home_defense_strength"],
                
                "away_attack": strengths.loc[away_team, "away_attack_strength"],

                "away_defense": strengths.loc[away_team, "away_defense_strength"],

                "home_elo": elo.loc[elo["team"] == home_team, "elo"].iloc[0],
                
                "away_elo": elo.loc[elo["team"] == away_team, "elo"].iloc[0],

                "home_form": form.loc[form["team"] == home_team, "form_percentage"].iloc[0],
                
                "away_form": form.loc[form["team"] == away_team, "form_percentage"].iloc[0],

                "result": match["result"]

            }

            all_rows.append(row)

        except IndexError:
            continue

ml_df = pd.DataFrame(all_rows)

output_path = ("Data/Processed/ml_dataset.csv")

ml_df.to_csv(output_path, index=False)

print("\n===== DATASET CREATED =====")
print(ml_df.shape)
print("\nLeague Distribution:")
print(ml_df["result"].value_counts())
print(ml_df.head())