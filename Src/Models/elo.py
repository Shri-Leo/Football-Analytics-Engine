import pandas as pd

# =========================
# SETTINGS
# =========================

LEAGUES = [
    "epl",
    "laliga",
    "seriea",
    "bundesliga",
    "ligue1"
]

INITAL_ELO = 1500

K_FACTOR = 20

DECAY_FACTOR = 0.97

# =========================
# EXPECTED RESULT
# =========================

def expected_result(team_elo, opponent_elo):

    return 1 / (
        1 + 10 ** (
            (opponent_elo - team_elo) / 400
        )
    )

# =========================
# UPDATE ELO
# =========================

def update_elo(team_elo, opponent_elo, actual_result, weight):
    expected = expected_result(team_elo, opponent_elo)

    effective_k = (K_FACTOR * weight)

    new_elo = (
        team_elo
        +
        effective_k * (
            actual_result - expected
        )
    )

    return new_elo

# =========================
# TIME DECAY WEIGHT
# =========================

def get_time_weight(season, latest_season):

    season_year = int(season.replace("season-","")[:2])

    latest_year = int(latest_season.replace("season-","")[:2])

    years_ago = latest_year - season_year

    return DECAY_FACTOR ** years_ago

# =========================
# GENERATE ELO
# =========================

def generate_elo_ratings(league):

    input_path = (f"Data/Processed/"f"{league}_clean.csv")

    output_path = (f"Data/Processed/"f"{league}_elo.csv")

    print(f"\n===== {league.upper()} =====")

    matches = pd.read_csv(input_path)

    # Sort chronologically
    matches["date"] = pd.to_datetime(matches["date"])

    matches = matches.sort_values(by="date")

    latest_season = "season-2526"

    print("Latest season:", latest_season)

    # =========================
    # INITIALIZE TEAMS
    # =========================

    teams = pd.unique(matches[["home_team", "away_team"]].values.ravel())

    elo_ratings = {
        team: INITAL_ELO
        for team in teams
    }

    # =========================
    # PROCESS MATCHES
    # =========================

    for _, match in matches.iterrows():
        if match["season"] == "season":
            print("\nBAD ROW FOUND:")
            print(match)
            continue

        home_team = match["home_team"]
        away_team = match["away_team"]
        
        home_goals = match["home_goals"]
        away_goals = match["away_goals"]
        
        home_elo = elo_ratings[home_team]
        away_elo = elo_ratings[away_team]

        # =========================
        # ACTUAL RESULTS
        # =========================
        
        if home_goals > away_goals:

            home_result = 1
            away_result = 0

        elif home_goals < away_goals:

            home_result = 0
            away_result = 1

        else:

            home_result = 0.5
            away_result = 0.5

        # =========================
        # UPDATE ELO
        # =========================

        weight = get_time_weight(match["season"], latest_season)

        new_home_elo = update_elo(home_elo, away_elo, home_result, weight)
        
        new_away_elo = update_elo(away_elo, home_elo, away_result, weight)

        elo_ratings[home_team] = (new_home_elo)
        
        elo_ratings[away_team] = (new_away_elo)
    
    # =========================
    # SAVE RESULTS
    # =========================

    elo_df = pd.DataFrame({
        "team": elo_ratings.keys(),
        "elo": elo_ratings.values()
    })

    elo_df = elo_df.sort_values(
        by="elo",
        ascending=False
    )

    elo_df.to_csv(output_path, index=False)

    print("\n===== TOP 10 ELO RATINGS =====")

    print(elo_df.head(10))

# =========================
# RUN ALL LEAGUES
# =========================

if __name__ == "__main__":

    for league in LEAGUES:

        generate_elo_ratings(league)