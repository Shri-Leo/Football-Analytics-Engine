import pandas as pd
from scipy.stats import poisson

from Src.Core.engine import calculate_xg

# =========================
# SCORE MATRIX
# =========================

def generate_score_matrix(home_team,away_team,max_goals=5):

    # Expected goals
    home_xg, away_xg = calculate_xg(home_team,away_team)

    print(f"\n{home_team} vs {away_team}")
    print("-" * 40)

    print(f"Expected {home_team} Goals: {home_xg:.2f}")
    print(f"Expected {away_team} Goals: {away_xg:.2f}")

    # =========================
    # SCORE MATRIX
    # =========================

    matrix = []

    for home_goals in range(max_goals + 1):

        for away_goals in range(max_goals + 1):

            probability = (
                poisson.pmf(home_goals, home_xg)
                * poisson.pmf(away_goals, away_xg)
            )

            matrix.append({
                "home_goals": home_goals,
                "away_goals": away_goals,
                "probability": probability
            })

    # Convert to dataframe
    matrix_df = pd.DataFrame(matrix)

    # Sort by probability
    matrix_df = matrix_df.sort_values(by="probability",ascending=False)

    print("\n===== TOP 10 MOST LIKELY SCORES =====")

    print(matrix_df.head(10))

# =========================
# TEST
# =========================

generate_score_matrix("Liverpool","Man City")