from Src.Core.engine import (calculate_xg, calculate_match_probabilities)

def predict_match(home_team, away_team, league="epl"):

    # Expected goals
    home_xg, away_xg = calculate_xg(home_team, away_team, league)

    # Match probabilities
    probs = calculate_match_probabilities(home_team, away_team, league)

    print(f"\n{home_team} vs {away_team}")
    print("-" * 40)

    print(f"Expected {home_team} Goals: {home_xg:.2f}")
    print(f"Expected {away_team} Goals: {away_xg:.2f}")

    print("\n===== MATCH PROBABILITIES =====")

    print(f"{home_team} Win: {probs['home_win']:.3f}")
    print(f"Draw: {probs['draw']:.3f}")
    print(f"{away_team} Win: {probs['away_win']:.3f}")

# =========================
# TEST
# =========================

predict_match("Barcelona", "Real Madrid", league="laliga")