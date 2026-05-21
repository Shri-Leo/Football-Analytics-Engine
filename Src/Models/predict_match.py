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
# PREDICT MATCH FUNCTION
# =========================

def predict_match(home_team, away_team):

    # Home expected goals
    home_expected_goals = (
        strengths.loc[home_team, "home_attack_strength"]
        * strengths.loc[away_team, "away_defense_strength"]
        * LEAGUE_HOME_GOALS
    )

    # Away expected goals
    away_expected_goals = (
        strengths.loc[away_team, "away_attack_strength"]
        * strengths.loc[home_team, "home_defense_strength"]
        * LEAGUE_AWAY_GOALS
    )

    print(f"\n{home_team} vs {away_team}")
    print("-" * 40)

    print(f"Expected {home_team} Goals: {home_expected_goals:.2f}")
    print(f"Expected {away_team} Goals: {away_expected_goals:.2f}")

    # =========================
    # SCORE PROBABILITIES
    # =========================

    max_goals = 5

    home_goal_probs = [
        poisson.pmf(i, home_expected_goals)
        for i in range(max_goals + 1)
    ]    

    away_goal_probs = [
        poisson.pmf(i, away_expected_goals)
        for i in range(max_goals + 1)
    ]    

    # =========================
    # MATCH RESULT PROBABILITIES
    # =========================

    home_win_prob = 0
    draw_prob = 0
    away_win_prob = 0

    for home_goals in range(max_goals + 1):
        for away_goals in range(max_goals + 1):

            probability = (
                home_goal_probs[home_goals]
                * away_goal_probs[away_goals]
            )

            if home_goals > away_goals:
                home_win_prob += probability
            
            elif home_goals == away_goals:
                draw_prob += probability

            else:
                away_win_prob += probability
    
    print("\n===== MATCH PROBALITIES =====")

    print(f"{home_team} Win: {home_win_prob:.3f}")
    print(f"Draw: {draw_prob:.3f}")
    print(f"{away_team} Win: {away_win_prob: .3f}")

# =========================
# TEST PREDICTION
# =========================

predict_match("Liverpool", "Man City")