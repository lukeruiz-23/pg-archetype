"""YOUR TURN #3: defense and hustle, for the archetype's defensive metrics
and for the team-context rim-protection feature.

Two endpoints, both one call per season:

1. LeagueDashPtDefend   (rim protection)
   defense_category="Less Than 6Ft"   -> opponent FG% at the rim when this
                                         player is the closest defender
   Params: season=..., season_type_all_star="Regular Season",
           per_mode_simple="Totals", defense_category="Less Than 6Ft"
   Output: data/raw/rim_defense/{season}.parquet

2. LeagueHustleStatsPlayer   (deflections, contests, charges)
   NOTE: hustle tracking started a few seasons after 2013-14 (around
   2015-16 / 2016-17). Run the loop, then check which seasons come back
   empty and skip those. Log the gap in the decisions log: either drop
   hustle features from clustering, or cluster on the later seasons only.
   Params: season=..., season_type_all_star="Regular Season",
           per_mode_time="Totals"
   Output: data/raw/hustle/{season}.parquet
"""

from nba_api.stats.endpoints import LeagueDashPtDefend, LeagueHustleStatsPlayer

from src.config import SEASONS
from src.pull.nba_client import fetch_cached


def main() -> None:
    raise NotImplementedError


if __name__ == "__main__":
    main()
