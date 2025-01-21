import pandas as pd
import numpy as np
import random

# Step 1: Simulate team win percentages
np.random.seed(42)  # For reproducibility
teams = [f"Team {i+1}" for i in range(128)]
win_percentages = np.random.uniform(0.3, 1.0, size=128)  # Random win %
data = pd.DataFrame({"Team": teams, "Win %": win_percentages})
data = data.sort_values(by="Win %", ascending=False).reset_index(drop=True)
data['Rank'] = data.index + 1

# Step 2: Assign seeds
data['Seed'] = pd.cut(data['Rank'], bins=8, labels=list(range(1, 9)), right=False)

# Step 3: Draw conferences
conferences = {f"Conference {i+1}": [] for i in range(16)}
for seed in range(1, 9):
    seed_teams = data[data['Seed'] == seed]['Team'].tolist()
    random.shuffle(seed_teams)  # Shuffle teams within the seed
    for i, team in enumerate(seed_teams):
        conferences[f"Conference {(i % 16) + 1}"].append(team)

# Step 4: Simulate games
def simulate_game(seed_a, seed_b):
    probability = max(0.5 - 0.05 * (seed_a - seed_b), 0.1)  # Sliding scale
    return np.random.random() < probability

schedule = []
for conf, teams in conferences.items():
    for i, team_a in enumerate(teams):
        for team_b in teams[i + 1:]:
            seed_a = data[data['Team'] == team_a]['Seed'].iloc[0]
            seed_b = data[data['Team'] == team_b]['Seed'].iloc[0]
            result = simulate_game(seed_a, seed_b)
            winner = team_a if result else team_b
            loser = team_b if result else team_a
            schedule.append({
                "Conference": conf,
                "Team A": team_a,
                "Team B": team_b,
                "Winner": winner,
                "Loser": loser
            })

# Step 5: Summarize and Output Results
results = pd.DataFrame(schedule)
standings = results.groupby('Winner').size().reset_index(name='Wins')
standings = standings.sort_values(by='Wins', ascending=False)

print(standings)
