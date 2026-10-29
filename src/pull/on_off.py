"""YOUR TURN #4 (harder): on/off splits for every player on every team-season.

Endpoint: TeamPlayerOnOffSummary
  This one is per TEAM, not league-wide: 30 teams x 13 seasons = 390 calls
  (about 10 minutes with the sleep). The cache means a crash halfway costs
  nothing; just re-run.

  It returns THREE tables, so use dataset_index:
    0 = OverallTeamPlayerOnOffSummary   (team totals, skip)
    1 = PlayersOffCourt...              (team results with player OFF)
    2 = PlayersOnCourt...               (team results with player ON)
  Pull both 1 and 2 (two fetch_cached calls, two output files per team-season).

  Use measure_type_detailed_defense="Advanced" to get OFF_RATING,
  DEF_RATING, NET_RATING. Also per_mode_detailed="Totals", season=...,
  season_type_all_star="Regular Season", team_id=...

Getting team IDs:
    from nba_api.stats.static import teams
    team_ids = [t["id"] for t in teams.get_teams()]

Output: data/raw/on_off/{on|off}/{season}/{team_id}.parquet

Watch out: a player traded mid-season shows up under both teams. That is
correct (his context changed), but remember it when you aggregate.
"""

from nba_api.stats.endpoints import TeamPlayerOnOffSummary
from nba_api.stats.static import teams

from src.config import SEASONS
from src.pull.nba_client import fetch_cached


def main() -> None:
    raise NotImplementedError


if __name__ == "__main__":
    main()
