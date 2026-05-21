import pandas as pd
import numpy as np
from scipy.stats import poisson

# =========================
# LOAD TEAM STRENGTHS
# =========================

strengths = pd.read_csv("Data/Processed/epl_team_strengths.csv", index_col=0)

# =========================
# LEAGUE AVERAGES
# =========================

LEAGUE_HOME_GOALS = 1.531
LEAGUE_AWAY_GOALS = 1.164

# =========================
# SCORE MATRIX FUNCTION
# =========================

def generate_score_matrix(home_team, away_team):

    # Expected goals
    home_xg = (
        strengths.loc[home_team, "home_attack_strength"]
        * strengths.loc[away_team, "away_defense_strength"]
        * LEAGUE_HOME_GOALS
    )

    away_xg = (
        strengths.loc[home_team, "away_attack_strength"]
        * strengths.loc[away_team, "home_defense_strength"]
        * LEAGUE_AWAY_GOALS
    )

    print(f"\n{home_team} vs {away_team}")
    print("-" * 40)

    print(f"Expected {home_team} Goals: {home_xg:.2f}")
    print(f"Expected {away_team} Goals: {away_xg:.2f}")

    # =========================
    # SCORE MATRIX
    # =========================

    max_goals = 5

    matrix = []

    for home_goals in range(max_goals + 1):
        for away_goals in range(max_goals + 1):
            probability = (
                poisson.pmf(home_goals, home_xg) * poisson.pmf(away_goals, away_xg)
            )

            matrix.append({
                "home_goals": home_goals,
                "away_goals": away_goals,
                "probability": probability
            })

    # Convert to dataframe
    matrix_df = pd.DataFrame(matrix)

    # Sort by highest probability
    matrix_df = matrix_df.sort_values(
        by="probability",
        ascending=False
    )

    print("\n===== TOP 10 MOST LIKELY SCORES =====")
    print(matrix_df.head(10))

# =========================
# TEST
# =========================

generate_score_matrix("Arsenal", "Chelsea")