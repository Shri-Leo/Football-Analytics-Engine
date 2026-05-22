import pandas as pd

from Src.Core.season import simulate_season

# =========================
# MONTE CARLO SETTINGS
# =========================

num_simulations = 1000

title_counts = {}

# =========================
# RUN SIMULATIONS
# =========================

for i in range(num_simulations):

    season_table = simulate_season()

    champion = season_table.index[0]

    if champion not in title_counts:
        title_counts[champion] = 0

    title_counts[champion] += 1

    # Progress tracker
    if (i + 1) % 50 == 0:
        print(f"Completed {i + 1} simulations")

# =========================
# TITLE PROBABILITIES
# =========================

results = []

for team, titles in title_counts.items():

    probability = (
        titles / num_simulations
    ) * 100

    results.append({
        "team": team,
        "titles_won": titles,
        "title_probability": probability
    })

results_df = pd.DataFrame(results)

results_df = results_df.sort_values(
    by="title_probability",
    ascending=False
)

# =========================
# OUTPUT
# =========================

print("\n===== EPL TITLE PROBABILITIES =====\n")

print(results_df)