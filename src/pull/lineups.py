"""YOUR TURN #5: lineup data, for Methodology step 5 (same guard, with vs.
without a rim protector).

Endpoint: LeagueDashLineups
  group_quantity=2   two-man combos (guard + big). Larger samples than
                     5-man lineups, so start here.
  group_quantity=5   full lineups. Very noisy; pull them, but expect to lean
                     on the 2-man data.

Params: season=..., season_type_all_star="Regular Season",
        measure_type_detailed_defense="Advanced", per_mode_detailed="Totals",
        group_quantity=2 (then 5)

Output: data/raw/lineups/{2|5}man/{season}.parquet

Question to answer before Phase 4 (decisions log): what is the minimum
minutes for a lineup to count? Lineup net ratings swing wildly under ~200
minutes. Look at the distribution of MIN once you have the data, then pick.
"""

from nba_api.stats.endpoints import LeagueDashLineups

from src.config import SEASONS
from src.pull.nba_client import fetch_cached


def main() -> None:
    raise NotImplementedError


if __name__ == "__main__":
    main()
