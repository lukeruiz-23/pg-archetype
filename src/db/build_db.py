"""Load every raw Parquet file into one DuckDB database.

DuckDB can read a whole folder of Parquet files with a glob, so each raw
folder becomes one table with a single SQL statement. Re-running rebuilds the
tables from scratch (CREATE OR REPLACE), so the database is always a pure
function of data/raw/. Never edit the database by hand.

Run from the repo root:
    python -m src.db.build_db
"""

import duckdb

from src.config import DB_PATH, RAW_DIR


TABLES = {
    # Player-season box score
    "raw_player_base": "player_seasons/base/*.parquet",
    "raw_player_advanced": "player_seasons/advanced/*.parquet",
    "raw_bio": "bio/*.parquet",

    # Tracking (style features for clustering)
    "raw_tracking_drives": "tracking/drives/*.parquet",
    "raw_tracking_pullup": "tracking/pullupshot/*.parquet",
    "raw_tracking_passing": "tracking/passing/*.parquet",
    "raw_tracking_possessions": "tracking/possessions/*.parquet",
    "raw_tracking_catchshoot": "tracking/catchshoot/*.parquet",

    # Defense
    "raw_rim_defense": "rim_defense/*.parquet",
    "raw_hustle": "hustle/*.parquet",          # 2016-17 onward only (decisions log)

    # Team context: two folder levels (season/team)
    "raw_on_court": "on_off/on/*/*.parquet",
    "raw_off_court": "on_off/off/*/*.parquet",
    "raw_lineups_2man": "lineups/2man/*/*.parquet",
    "raw_lineups_5man": "lineups/5man/*/*.parquet",
}


def main() -> None:
    con = duckdb.connect(str(DB_PATH))
    for table, pattern in TABLES.items():
        path = RAW_DIR / pattern
        # union_by_name: tolerate a column that exists in some seasons but not
        # others (stats.nba.com adds columns over time).
        con.execute(
            f"CREATE OR REPLACE TABLE {table} AS "
            f"SELECT * FROM read_parquet('{path}', union_by_name = true)"
        )
        n = con.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
        print(f"{table:<24} {n:>7,} rows")
    con.close()


if __name__ == "__main__":
    main()
