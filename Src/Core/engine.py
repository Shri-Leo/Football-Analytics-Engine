import pandas as pd
import numpy as np

from scipy.stats import poisson

from Src.Core.config import LEAGUE_CONFIG

# =========================
# LOAD LEAGUE DATA
# =========================

def load_league_data(league):

    config = LEAGUE_CONFIG[league]

    strengths = pd.read_csv(
        config["strengths_file"],
        index_col=0
    )

    return strengths, config

# =========================
# EXPECTED GOALS
# =========================

def calculate_xg(
    home_team,
    away_team,
    league="epl"
):

    strengths, config = load_league_data(
        league
    )

    home_xg = (
        strengths.loc[ home_team, "home_attack_strength" ]
        * strengths.loc[ away_team, "away_defense_strength" ]
        * config["home_goals_avg"]
    )

    away_xg = (
        strengths.loc[ away_team, "away_attack_strength" ]
        * strengths.loc[ home_team, "home_defense_strength" ]
        * config["away_goals_avg"]
    )

    return home_xg, away_xg

# =========================
# SIMULATE MATCH
# =========================

def simulate_match( home_team, away_team, league="epl" ):

    home_xg, away_xg = calculate_xg( home_team, away_team, league )

    home_goals = np.random.poisson( home_xg )

    away_goals = np.random.poisson( away_xg )

    return home_goals, away_goals

# =========================
# MATCH PROBABILITIES
# =========================

def calculate_match_probabilities( home_team, away_team, league="epl", max_goals=5 ):

    home_xg, away_xg = calculate_xg( home_team, away_team, league )

    home_goal_probs = [
        poisson.pmf(i, home_xg)
        for i in range(max_goals + 1)
    ]

    away_goal_probs = [
        poisson.pmf(i, away_xg)
        for i in range(max_goals + 1)
    ]

    home_win_prob = 0
    draw_prob = 0
    away_win_prob = 0

    for hg in range(max_goals + 1):
        for ag in range(max_goals + 1):

            probability = (
                home_goal_probs[hg]
                * away_goal_probs[ag]
            )

            if hg > ag:
                home_win_prob += probability

            elif hg == ag:
                draw_prob += probability

            else:
                away_win_prob += probability

    return {
        "home_win": home_win_prob,
        "draw": draw_prob,
        "away_win": away_win_prob
    }