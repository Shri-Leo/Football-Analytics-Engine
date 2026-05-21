import pandas as pd

INPUT_PATH = "Data/Processed/epl_clean.csv"

# =========================
# LOAD DATA
# =========================

df = pd.read_csv(INPUT_PATH)

# Convert date properly
df["date"] = pd.to_datetime(df["date"])

# =========================
# LEAGUE AVERAGES
# =========================

league_home_goals = df["home_goals"].mean()
league_away_goals = df["away_goals"].mean()

print("\n==== LEAGUE AVERAGES ====")
print(f"Average Home Goals: {league_home_goals:.3f}")
print(f"Average Away Goals: {league_away_goals:.3f}")

# =========================
# HOME TEAM STRENGTHS
# =========================

home_stats = df.groupby("home_team").agg({
    "home_goals": "mean",
    "away_goals": "mean"
})

home_stats = home_stats.rename(columns={
    "home_goals": "avg_home_scored",
    "away_goals": "avg_home_conceded"
})

# Attack strength
home_stats["home_attack_strength"] = (
    home_stats["avg_home_scored"] / league_home_goals
)

# Defense strength
home_stats["home_defense_strength"] = (
    home_stats["avg_home_conceded"] / league_away_goals
)

# =========================
# AWAY TEAM STRENGTHS
# =========================

away_stats = df.groupby("away_team").agg({
    "away_goals": "mean",
    "home_goals": "mean"
})

away_stats = away_stats.rename(columns={
    "away_goals": "avg_away_scored",
    "home_goals": "avg_away_conceded"
})

# Attack strength
away_stats["away_attack_strength"] = (
    away_stats["avg_away_scored"] / league_away_goals
)

# Defense strength
away_stats["away_defense_strength"] = (
    away_stats["avg_away_conceded"] / league_home_goals
)

# =========================
# COMBINE STATS
# =========================

team_strengths = home_stats.join(away_stats)

print("\n==== TEAM STRENGTHS ====")
print(team_strengths.head())

OUTPUT_PATH = "Data/Processed/epl_team_strengths.csv"

team_strengths.to_csv(OUTPUT_PATH)

print("\nTeam strengths saved successfully.")