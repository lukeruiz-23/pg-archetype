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

# table name -> folder under data/raw/ (glob)
# The first entry is done; add one line per pull script as you finish it.
TABLES = {
    "raw_player_base": "player_seasons/base/*.parquet",
    "raw_player_advanced": "player_seasons/advanced/*.parquet",
    # TODO "raw_bio": ...
    # TODO "raw_tracking_drives": ...
    # TODO "raw_tracking_pullup": ...
    # TODO "raw_tracking_passing": ...
    # TODO "raw_rim_defense": ...
    # TODO "raw_hustle": ...
    # TODO "raw_on_court": "on_off/on/*/*.parquet"   (two levels: season/team)
    # TODO "raw_off_court": ...
    # TODO "raw_lineups_2man": ...
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
