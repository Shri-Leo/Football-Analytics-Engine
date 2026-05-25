import pandas as pd

# =========================
# LEAGUES
# =========================

LEAGUES = [
    "epl",
    "laliga",
    "seriea",
    "bundesliga",
    "ligue1"
]

# =========================
# GENERATE TEAM STRENGTHS
# =========================

def generate_team_strengths(league):

    input_path = ( f"Data/Processed/" f"{league}_clean.csv" )

    output_path = ( f"Data/Processed/" f"{league}_team_strengths.csv" )

    print(f"\n===== {league.upper()} =====")

    matches = pd.read_csv(input_path)

    # =========================
    # LEAGUE AVERAGES
    # =========================

    avg_home_goals = matches["home_goals"].mean()

    avg_away_goals = matches["away_goals"].mean()

    print( f"Average Home Goals: " f"{avg_home_goals:.3f}" )

    print( f"Average Away Goals: " f"{avg_away_goals:.3f}" )

    # =========================
    # HOME STATS
    # =========================

    home_stats = matches.groupby("home_team").agg({ "home_goals": "mean", "away_goals": "mean" })

    home_stats.columns = [ "avg_home_scored", "avg_home_conceded" ]

    # =========================
    # AWAY STATS
    # =========================

    away_stats = matches.groupby("away_team").agg({ "away_goals": "mean", "home_goals": "mean" })

    away_stats.columns = [ "avg_away_scored", "avg_away_conceded" ]

    # =========================
    # COMBINE
    # =========================

    strengths = home_stats.join( away_stats, how="inner" )

    # =========================
    # ATTACK / DEFENSE STRENGTH
    # =========================

    strengths["home_attack_strength"] = ( strengths["avg_home_scored"] / avg_home_goals )

    strengths["home_defense_strength"] = ( strengths["avg_home_conceded"] / avg_away_goals )

    strengths["away_attack_strength"] = ( strengths["avg_away_scored"] / avg_away_goals )

    strengths["away_defense_strength"] = ( strengths["avg_away_conceded"] / avg_home_goals )

    # =========================
    # SAVE
    # =========================

    strengths.to_csv(output_path)

    print( f"{league}_team_strengths.csv created." )

    print("\n===== SAMPLE =====")

    print(strengths.head())

# =========================
# RUN ALL LEAGUES
# =========================

if __name__ == "__main__":

    for league in LEAGUES:
        generate_team_strengths(league)