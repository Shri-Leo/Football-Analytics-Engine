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

CURRENT_SEASON = "season-2526"

# =========================
# FORM ENGINE
# =========================

def generate_form_table(league):

    input_path = (f"Data/Processed/{league}_clean.csv")

    output_path = (f"Data/Processed/{league}_form.csv")

    print(f"\n===== {league.upper()} =====")

    matches = pd.read_csv(input_path)

    # Current season only
    matches = matches[matches["season"] == CURRENT_SEASON]

    # Sort by date
    matches["date"] = pd.to_datetime(matches["date"])

    matches = matches.sort_values(by="date")

    # Team list
    teams = sorted(
        set(matches["home_team"])
        |
        set(matches["away_team"])
    )

    results = []

    # =========================
    # TEAM LOOP
    # =========================

    for team in teams:

        team_matches = matches[
            (matches["home_team"] == team)
            |
            (matches["away_team"] == team)
        ]

        last_5 = team_matches.tail(5)

        form_points = 0

        for _, match in last_5.iterrows():

            # Team played at home
            if match["home_team"] == team:
                
                if match["result"] == "H":
                    form_points += 3

                elif match["result"] == "D":
                    form_points += 1

            else:
                
                if match["result"] == "A":
                    form_points += 3

                elif match["result"] == "D":
                    form_points += 1

        form_percentage = ( form_points / 15) * 100

        results.append({
            "team": team,
            "form_points": form_points,
            "form_percentage": round(form_percentage, 2)
        })

    # =========================
    # SAVE RESULTS
    # =========================

    form_df = pd.DataFrame(results)

    form_df = form_df.sort_values(
        by="form_percentage",
        ascending=False
    )

    form_df.to_csv(output_path, index=False)

    print("\n===== TOP 10 FORM TEAMS =====")
    print(form_df.head(10))

# =========================
# RUN ALL LEAGUES
# =========================

if __name__ == "__main__":

    for league in LEAGUES:
        generate_form_table(league)