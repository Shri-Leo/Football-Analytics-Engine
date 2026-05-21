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
# SIMULATE MATCH
# =========================

def simulate_match(home_team, away_team):

    # Expected goals
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

    # Random goals using Poisson
    home_goals = np.random.poisson(home_xg)
    away_goals = np.random.poisson(away_xg)

    print(f"\n{home_team} vs {away_team}")
    print("-" * 40)

    print(f"Expected {home_team} Goals: {home_xg:.2f}")
    print(f"Expected {away_team} Goals: {away_xg:.2f}")

    print("\n===== SIMULATED RESULT =====")

    print(f"{home_team} {home_goals} - {away_goals} {away_team}")

# =========================
# TEST
# =========================

simulate_match("Liverpool", "Man City")