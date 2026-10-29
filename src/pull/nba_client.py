"""One shared function for every stats.nba.com call.

Why a wrapper instead of calling nba_api directly in each script?
  1. Caching: each response is saved to data/raw/. Re-running a script skips
     anything already downloaded, so a crash halfway through costs nothing.
  2. Retries: stats.nba.com times out often. We retry with a growing wait
     (exponential backoff) instead of failing the whole run.
  3. Raw data stays untouched. All cleaning happens later, in SQL, where it is
     visible and repeatable. That is also an easy thing to explain in interviews.
"""

import time
from pathlib import Path

import pandas as pd

from src.config import MAX_RETRIES, RAW_DIR, SLEEP_SECONDS, TIMEOUT_SECONDS


def fetch_cached(endpoint_cls, out_path: Path, dataset_index: int = 0, **params) -> pd.DataFrame:
    """Call an nba_api endpoint once and cache the result as Parquet.

    endpoint_cls   an nba_api class, e.g. LeagueDashPlayerStats
    out_path       where to save, relative to data/raw/
    dataset_index  some endpoints return several tables; pick one (0 = first)
    **params       passed straight to the endpoint (season=..., etc.)
    """
    path = RAW_DIR / out_path
    if path.exists():
        return pd.read_parquet(path)

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = endpoint_cls(timeout=TIMEOUT_SECONDS, **params)
            df = response.get_data_frames()[dataset_index]
            break
        except Exception as err:  # timeouts, connection resets, 429s
            wait = SLEEP_SECONDS * 2 ** attempt
            print(f"  attempt {attempt} failed ({type(err).__name__}); retrying in {wait:.0f}s")
            time.sleep(wait)
    else:
        raise RuntimeError(f"Gave up after {MAX_RETRIES} attempts: {out_path}")

    # Record what was asked for, so every raw file explains itself.
    for key, value in params.items():
        if isinstance(value, (str, int)):
            df[f"_param_{key}"] = value

    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(path, index=False)
    time.sleep(SLEEP_SECONDS)
    return df
