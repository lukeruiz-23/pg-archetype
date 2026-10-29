# Do small score-first point guards need the right roster?

> **Status: Phase 1 (data pipeline) in progress.** The finding and headline chart go here once Phase 4 is done.

**Question.** Does the gap between a point guard's box-score production and his on-court impact depend on roster context more for small, high-usage, score-first guards than for other guards?

**Motivating case.** Darius Acuff Jr., No. 7 pick in the 2026 draft (Sacramento). The project ends with a published, testable prediction of his impact given the Kings' roster.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Pipeline

All commands run from the repo root. Each pull caches to `data/raw/`, so re-running skips anything already downloaded.

| Step | Command | Source | Status |
|---|---|---|---|
| Box score + advanced | `python -m src.pull.player_seasons` | LeagueDashPlayerStats | done (worked example) |
| Height / weight | `python -m src.pull.bio` | LeagueDashPlayerBioStats | todo |
| Tracking (drives, pull-ups, passing) | `python -m src.pull.tracking` | LeagueDashPtStats | todo |
| Rim defense + hustle | `python -m src.pull.defense` | LeagueDashPtDefend, LeagueHustleStatsPlayer | todo |
| On/off | `python -m src.pull.on_off` | TeamPlayerOnOffSummary | todo |
| Lineups | `python -m src.pull.lineups` | LeagueDashLineups | todo |
| RAPM | not in nba_api; external source | — | todo (choose source) |
| Build database | `python -m src.db.build_db` | all of the above | partial |

## Repo layout

```
src/
  config.py          seasons, paths, API politeness settings
  pull/              one script per data source -> data/raw/
  db/build_db.py     data/raw/ -> DuckDB tables
sql/                 feature-building queries (Phase 2+)
notebooks/           exploration and charts
data/                not committed; rebuilt by the pipeline
```

## Method

See the project brief. Key decisions so far: sample starts 2013-14; archetype defined by clustering (Gaussian mixture, features standardized within season); RAPM is the primary impact metric, with EPM and LEBRON as robustness checks.
