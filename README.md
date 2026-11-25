# Free Time Vacation

A static planning dashboard for finding vacation windows in the San Francisco Bay Area (Outer Sunset 94122, AM/FM radio context) that avoid live sports you want to hear on the radio.

## Tracked categories (high-priority rules)

A minute is **free** when none of these are on air:

- **MLB** — San Francisco Giants and Athletics flagged high priority; **all 30 MLB clubs shown** (regular season, postseason, All-Star/special games as applicable).
- **NFL — San Francisco 49ers** (preseason, regular season, postseason) — **high priority**.
- **NCAAF — Stanford Cardinal and California Golden Bears** — **high priority**.
- **Westwood One Sports national NFL radio broadcasts** (TNF/SNF/MNF/Thanksgiving/holiday packages/postseason as carried).

## Best vacation windows (modeled, verify before booking)

Based on verified anchors + estimated season windows (generated 2026-11-25):

| Year | Best modeled window | Days | Confidence note |
|------|---------------------|------|-----------------|
| 2027 | 2027-02-15 to 2027-03-23 | 37 | Super Bowl LXI is 2027-02-14 (NFL verified). MLB 2027 Opening Night is 2027-03-24 (MLB verified). Boundaries should still be rechecked for 49ers preseason/NCAAF/broadcast changes. |
| 2028 | 2028-02-14 to 2028-03-29 | 45 | Super Bowl LXII is 2028-02-13 (reported NFL announcement). MLB 2028 window is **estimated** (no official schedule). |
| 2029 | 2029-02-12 to 2029-03-28 | 45 | **Estimated** - 2028-29 NFL postseason and 2029 MLB/NCAAF schedules not officially released. |

## Site

The GitHub Pages site lives in [`docs/`](docs/index.html):

- [Dashboard / Executive Summary](docs/index.html)
- [Calendar / Scoreboard](docs/calendar.html)
- [Games & Schedule](docs/games.html)
- [Sources & Verification](docs/sources.html)
- [Flagged for Review](docs/flagged.html)

## Data honesty

- **Verified** = backed by an official/primary source URL recorded in `docs/data/schedule-data.js`.
- **Estimated** = modeled from typical season patterns because official game-level schedules are unreleased. These are clearly labeled and listed on the Flagged for Review page.
- **No hallucinated values.** Missing/unknown times are left TBA/blank and flagged.

## Key official sources

- MLB 2027 schedule release: https://www.mlb.com/news/mlb-2027-schedule-released
- MLB schedule hub: https://www.mlb.com/schedule
- NFL 2026-27 important dates: https://www.nfl.com/news/2026-27-national-football-league-important-dates
- NFL schedules: https://www.nfl.com/schedules/
- 49ers schedule: https://www.49ers.com/schedule/
- Westwood One NFL schedule: https://www.westwoodonesports.com/nfl-schedule/
- Westwood One station finder: https://www.westwoodonesports.com/station-finder
- Stanford football schedule: https://gostanford.com/sports/football/schedule
- Cal football schedule: https://calbears.com/sports/football/schedule

## Regenerating data

```bash
python3 scripts/build_schedule.py
```

This regenerates `docs/data/schedule-data.js`.
