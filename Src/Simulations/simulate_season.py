from Src.Core.season import simulate_season

table = simulate_season()

print("\n===== SIMULATED EPL TABLE =====\n")

print(table.head(20))