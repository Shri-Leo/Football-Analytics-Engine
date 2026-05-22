import pandas as pd
import numpy as np

# =========================
# LOAD DATA
# =========================

matches = pd.read_csv("Data/Processed/epl_clean.csv")

strengths = pd.read_csv("Data/Processed/epl_team_strengths.csv", index_col=0)

# =========================
# LEAGUE AVERAGES
# =========================

LEAGUE_HOME_GOALS = 1.531
LEAGUE_AWAY_GOALS = 1.164

# =========================
# USE CURRENT EPL SEASON
# =========================

latest_season = "season-2425"

fixtures = matches[matches["season"] == latest_season].copy()

# =========================
# SIMULATE MATCH
# =========================

def simulate_match(home_team, away_team):

    home_xg = (
        strengths.loc[home_team, "home_attack_strength"]
        * strengths.loc[away_team, "away_defense_strength"]
        * LEAGUE_HOME_GOALS
    )

    away_xg = (
        strengths.loc[away_team, "away_attack_strength"]
        * strengths.loc[home_team, "home_defense_strength"]
        * LEAGUE_AWAY_GOALS
    )

    home_goals = np.random.poisson(home_xg)
    away_goals = np.random.poisson(away_xg)

    return home_goals, away_goals

# =========================
# SIMULATE ONE SEASON
# =========================

def simulate_season():

    teams = pd.unique(
        fixtures[["home_team", "away_team"]].values.ravel()
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

        # Result Logic
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

    # Final table sorting
    table = table.sort_values(
        by=["points", "gd", "gf"],
        ascending=False
    )

    return table

# =========================
# MONTE CARLO SIMULATION
# =========================

num_simulations = 1000

title_counts = {}

for i in range(num_simulations):

    season_table = simulate_season()
    champion = season_table.index[0]

    if champion not in title_counts:
        title_counts[champion] = 0

    title_counts[champion] += 1

    # Progress tracker
    if (i + 1) % 50 == 0:
        print(f"Completed {i + 1} simulations") 

# =========================
# TITLE PROBABILITIES
# =========================

results = []

for team, titles in title_counts.items():

    probability = (titles / num_simulations) * 100

    results.append({
        "team": team,
        "titles_won": titles,
        "titles_probability": probability
    })

results_df = pd.DataFrame(results)

results_df = results_df.sort_values(
    by="titles_probability",
    ascending=False
)

print("\n===== EPL TITLE PROBABILITIES =====\n")

print(results_df)
