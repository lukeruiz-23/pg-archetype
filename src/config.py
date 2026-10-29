"""Project-wide settings. Every script imports from here, so changing a value
(like the season range) changes it everywhere at once."""

from pathlib import Path

# --- Paths -----------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"            # untouched API responses, one file per pull
PROCESSED_DIR = ROOT / "data" / "processed"
DB_PATH = ROOT / "data" / "pg_archetype.duckdb"

# --- Sample ----------------------------------------------------------------
# Decisions log 2026-10-28: start at 2013-14, when player tracking begins.
FIRST_SEASON = 2013   # the year the season STARTS (2013 -> "2013-14")
LAST_SEASON = 2025    # last completed season; 2026-27 is the Acuff season, pulled separately


def season_str(start_year: int) -> str:
    """2013 -> '2013-14'. stats.nba.com wants seasons in this exact format."""
    return f"{start_year}-{str(start_year + 1)[-2:]}"


SEASONS = [season_str(y) for y in range(FIRST_SEASON, LAST_SEASON + 1)]

# --- API politeness ----------------------------------------------------------
# stats.nba.com throttles or blocks clients that hammer it. Waiting between
# calls is slower but means the pipeline finishes instead of getting banned.
SLEEP_SECONDS = 1.5
MAX_RETRIES = 4
TIMEOUT_SECONDS = 60
