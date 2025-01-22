# Custom College Football Season Simulator

This Python project simulates a custom college football season by ranking FBS teams based on win percentages, assigning seeds, organizing teams into conferences, and simulating games with probabilities based on seed differences.

As an avid fan of both college football and international soccer, I wanted to explore how a "Champions League" or "World Cup" format would work for American college football in order to determine the champion on the field and not by subjective rankings.

Future improvements will include scraping data for the past 3 seasons to determine win %, scraping historical data to adjust head-to-head matchup percentages, and UX for simulating full conference draws and seasons.

## Features

- **Team Ranking**: Ranks the top 128 teams by win percentage over the past three seasons.
- **Seed Assignment**: Divides teams into 8 seed groups based on rankings.
- **Conference Allocation**: Randomly assigns teams to 16 conferences with balanced seeding.
- **Game Simulation**: Determines game outcomes using a sliding scale probability based on seed differences.
- **Season Standings**: Outputs season results and team standings.

## Requirements

- Python 3.8+
- Pandas
- NumPy

## Usage

1. Run the simulation:
   ```bash
   python football_simulator.py
   ```

2. View the season results in the terminal or save to a file.

## Customization

- Replace the simulated win percentages with real data in the `win_percentages` list.
- Adjust game probabilities in the `simulate_game` function.
- Modify conference structures or scheduling as needed.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
