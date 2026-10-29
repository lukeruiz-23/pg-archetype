"""YOUR TURN #1 (easiest): height, weight, age, draft info per player-season.

Endpoint: LeagueDashPlayerBioStats
  Useful columns: PLAYER_ID, PLAYER_HEIGHT_INCHES, PLAYER_WEIGHT, AGE,
                  DRAFT_YEAR, DRAFT_NUMBER, COLLEGE

Note: this covers heights and weights without scraping Basketball-Reference.
Pulling it per season (not once) matters: listed weights change over a career.

Output: data/raw/bio/{season}.parquet

TODO
  - Copy the loop from player_seasons.py (one loop is enough here, no measures).
  - Params: season=..., season_type_all_star="Regular Season",
            per_mode_simple="Totals"
  - Run it, then open one file in pandas and check that heights look sane
    (no zeros, most between 70 and 90 inches).
"""

from nba_api.stats.endpoints import LeagueDashPlayerBioStats

from src.config import SEASONS
from src.pull.nba_client import fetch_cached


def main() -> None:
    raise NotImplementedError("Write the season loop here")


if __name__ == "__main__":
    main()
