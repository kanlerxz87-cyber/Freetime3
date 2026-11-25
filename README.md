# Free Time Vacation — Bay Area Sports Radio Planner

A source-first planning dashboard for finding vacation windows in the San Francisco Bay Area (Outer Sunset 94122, AM/FM radio context) that avoid live sports you want to hear on the radio.

## Executive summary

**No modeled 7+ day contiguous vacation window with zero tracked conflicts was found for 2027, 2028, or 2029** under the current conservative model. 

Why: the tracked categories cover most of the year. NFL season/postseason runs roughly Sep-Feb, MLB spring training + regular season + postseason runs roughly mid-Feb through early Nov, and Stanford/Cal NCAAF runs late Aug-late Nov. When these estimated season windows are treated as busy (because game-by-game 2027-2029 schedules are largely unreleased), no 7+ day gap remains. **This is a modeled planning result, not a certified "no vacation possible" fact.** Actual off-days, bye weeks, and unbroadcast windows may exist; verify official schedules as they are released.

### Important correction
An earlier draft window (2027-02-15 to 2027-03-23) was **invalid** because [MLB announced 2027 Spring Training begins Feb 19, 2027](https://www.mlb.com/press-release/press-release-mlb-announces-2027-spring-training-schedule) and the user rule includes MLB preseason. The model and site have been corrected to include MLB Spring Training windows.

## Tracked "busy" categories

A minute is **free** when none of these are on air:

- **MLB** — San Francisco Giants and Athletics flagged high priority; **all 30 MLB clubs shown** (preseason/spring training, regular season, postseason, All-Star/special games as applicable).
- **NFL — San Francisco 49ers** (preseason, regular season, postseason) — **high priority**.
- **NCAAF — Stanford Cardinal and California Golden Bears** — **high priority**.
- **Westwood One Sports national NFL radio broadcasts** (TNF/SNF/MNF/Thanksgiving/holiday packages/postseason as carried).

## Site

The GitHub Pages dashboard lives in [`docs/`](docs/index.html):

- [Dashboard / Executive Summary](docs/index.html)
- [Calendar / Scoreboard](docs/calendar.html)
- [Games & Schedule](docs/games.html)
- [Sources & Verification](docs/sources.html)
- [Flagged for Review](docs/flagged.html)

Legacy/supplemental pages retained from prior integration work are also in the repo (`site/`, `source-dashboard.html`, etc.) and should be read with the same caution: missing data is not free.

## Data honesty

- **Verified** = backed by an official/primary source URL recorded in `docs/data/schedule-data.js`.
- **Estimated** = modeled from typical season patterns because official game-level schedules are unreleased. Clearly labeled and listed on Flagged for Review.
- **No hallucinated values.** Missing/unknown times are left TBA/blank and flagged.

## Key official sources

- MLB 2027 schedule release: https://www.mlb.com/news/mlb-2027-schedule-released
- MLB 2027 Spring Training announcement: https://www.mlb.com/press-release/press-release-mlb-announces-2027-spring-training-schedule
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
