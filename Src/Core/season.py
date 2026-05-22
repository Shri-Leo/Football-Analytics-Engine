import pandas as pd

from Src.Core.engine import simulate_match

# =========================
# LOAD FIXTURES
# =========================

matches = pd.read_csv(
    "Data/Processed/epl_clean.csv"
)

latest_season = "season-2425"

fixtures = matches[
    matches["season"] == latest_season
].copy()

# =========================
# SIMULATE SEASON
# =========================

def simulate_season():

    teams = pd.unique(
        fixtures[["home_team", "away_team"]]
        .values
        .ravel()
    )

    table = pd.DataFrame(index=teams)

    table["played"] = 0
    table["wins"] = 0
    table["draws"] = 0
    table["losses"] = 0
    table["gf"] = 0
    table["ga"] = 0
    table["gd"] = 0
    table["points"] = 0

    for _, match in fixtures.iterrows():

        home_team = match["home_team"]
        away_team = match["away_team"]

        home_goals, away_goals = simulate_match(
            home_team,
            away_team
        )

        # Played
        table.loc[home_team, "played"] += 1
        table.loc[away_team, "played"] += 1

        # Goals
        table.loc[home_team, "gf"] += home_goals
        table.loc[home_team, "ga"] += away_goals

        table.loc[away_team, "gf"] += away_goals
        table.loc[away_team, "ga"] += home_goals

        # Goal Difference
        table.loc[home_team, "gd"] = (
            table.loc[home_team, "gf"]
            - table.loc[home_team, "ga"]
        )

        table.loc[away_team, "gd"] = (
            table.loc[away_team, "gf"]
            - table.loc[away_team, "ga"]
        )

        # Results
        if home_goals > away_goals:

            table.loc[home_team, "wins"] += 1
            table.loc[away_team, "losses"] += 1

            table.loc[home_team, "points"] += 3

        elif away_goals > home_goals:

            table.loc[away_team, "wins"] += 1
            table.loc[home_team, "losses"] += 1

            table.loc[away_team, "points"] += 3

        else:

            table.loc[home_team, "draws"] += 1
            table.loc[away_team, "draws"] += 1

            table.loc[home_team, "points"] += 1
            table.loc[away_team, "points"] += 1

    table = table.sort_values(
        by=["points", "gd", "gf"],
        ascending=False
    )

    return table