import pandas as pd

INPUT_PATH = "Data/Processed/epl_clean.csv"

df = pd.read_csv(INPUT_PATH)

# =========================
# BASIC DATASET INFO
# =========================

print("\n===== DATASET INFO =====")
print(df.info())

print("\n===== FIRST 5 ROWS =====")
print(df.head())

# =========================
# TOTAL MATCHES
# =========================

print("\n===== TOTAL MATCHES =====")
print(len(df))

# =========================
# RESULT DISTRIBUTION
# =========================

print("\n===== MATCH RESULTS =====")
print(df["result"].value_counts())

# H = Home Win
# D = Draw
# A = Away Win

# =========================
# GOALS ANALYSIS
# =========================

df["total_goals"] = df["home_goals"] + df["away_goals"]

print("\n===== GOALS STATS =====")
print(df["total_goals"].describe())

# =========================
# HOME VS AWAY GOALS
# =========================

print("\n===== AVERAGE HOME GOALS =====")
print(df["home_goals"].mean())

print("\n===== AVERAGE AWAY GOALS =====")
print(df["away_goals"].mean())

# =========================
# GOALS PER SEASON
# =========================

season_goals = df.groupby("season")["total_goals"].mean()

print("\n===== GOALS PER MATCH BY SEASON =====")
print(season_goals)

# =========================
# TOP SCORING TEAMS
# =========================

home_goals = df.groupby("home_team")["home_goals"].sum()
away_goals = df.groupby("away_team")["away_goals"].sum()

total_team_goals = home_goals.add(away_goals, fill_value=0)

print("\n===== TOP 10 SCORING TEAMS =====")
print(total_team_goals.sort_values(ascending=False).head(10))