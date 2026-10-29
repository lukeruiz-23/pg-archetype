"""YOUR TURN #2: player-tracking stats that define the archetype's style.

Endpoint: LeagueDashPtStats
  Loop over seasons AND over measure types, like player_seasons.py does.

  pt_measure_type   what you get                           used for
  ---------------   ------------------------------------   ------------------------
  "Drives"          DRIVES, DRIVE_PTS, DRIVE_PASSES, ...     drive frequency (cluster)
  "PullUpShot"      PULL_UP_FGA, PULL_UP_FG3A, ...           pull-up 3PA rate (cluster)
  "Passing"         POTENTIAL_AST, AST_POINTS_CREATED, ...   secondary-creator feature

Required params:
  season=..., season_type_all_star="Regular Season",
  player_or_team="Player", per_mode_simple="Totals",
  pt_measure_type=<one of the above>

Output: data/raw/tracking/{measure}/{season}.parquet

Think about this before you run it: "pull-up 3PA rate" in the brief is a RATE.
Rate of what? Per 100 possessions? Share of all FGA? Write down your choice;
it is a decisions-log entry. (You'll compute it later in SQL, not here.)
"""

from nba_api.stats.endpoints import LeagueDashPtStats

from src.config import SEASONS
from src.pull.nba_client import fetch_cached

MEASURES = ["Drives", "PullUpShot", "Passing"]


def main() -> None:
    raise NotImplementedError


if __name__ == "__main__":
    main()
