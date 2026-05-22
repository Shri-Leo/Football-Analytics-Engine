from Src.Core.engine import (
    calculate_xg,
    simulate_match
)

home_team = "Liverpool"
away_team = "Man City"

# Expected goals
home_xg, away_xg = calculate_xg(
    home_team,
    away_team
)

# Simulated result
home_goals, away_goals = simulate_match(
    home_team,
    away_team
)

print(f"\n{home_team} vs {away_team}")
print("-" * 40)

print(f"Expected {home_team} Goals: {home_xg:.2f}")
print(f"Expected {away_team} Goals: {away_xg:.2f}")

print("\n===== SIMULATED RESULT =====")

print(
    f"{home_team} "
    f"{home_goals} - {away_goals} "
    f"{away_team}"
)