"""WORKED EXAMPLE: box-score stats for every player-season, 2013-14 onward.

This one is complete so you can see the pattern end to end. The other pull
scripts in this folder follow the same shape; you write their loops.

Run from the repo root:
    python -m src.pull.player_seasons

Output: data/raw/player_seasons/{measure}/{season}.parquet
"""

from nba_api.stats.endpoints import LeagueDashPlayerStats

from src.config import SEASONS
from src.pull.nba_client import fetch_cached

# "Base" = traditional box score (PTS, AST, ...).
# "Advanced" = USG%, AST%, TS%, net rating, PIE, ...
MEASURES = ["Base", "Advanced"]


def main() -> None:
    for measure in MEASURES:
        for season in SEASONS:
            print(f"{measure} {season}")
            df = fetch_cached(
                LeagueDashPlayerStats,
                out_path=f"player_seasons/{measure.lower()}/{season}.parquet",
                season=season,
                season_type_all_star="Regular Season",
                measure_type_detailed_defense=measure,
                # Totals, not per-game: you can always divide later, but you
                # cannot recover totals from rounded per-game numbers.
                per_mode_detailed="Totals",
            )
            print(f"  {len(df)} rows")


if __name__ == "__main__":
    main()
