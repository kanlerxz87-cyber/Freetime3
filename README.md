# 🏖️ Free Time Vacation — Bay Area Sports Planner

**Live site:** https://kanlerxz87-cyber.github.io/Freetime3/

Tells you exactly when there are **no games on the radio** — no MLB, no NFL, no Stanford/Cal football — so you can plan a vacation with zero scheduling conflicts.

## The answer
**Mid-February → late March is the only multi-week free window each year** (day after the Super Bowl → day before MLB Opening Day).

| Year | Free window | Confidence |
|------|-------------|------------|
| 2027 | Feb 15 – Mar 23 (37 days) | ✅ VERIFIED (official MLB + NFL) |
| 2028 | Feb 14 – Mar 28 (44 days) | ⚠️ ESTIMATED (not released) |
| 2029 | Feb 12 – Mar 27 (44 days) | ⚠️ ESTIMATED (not released) |

## Pages
- `index.html` — landing dashboard
- `executive-summary.html` — bottom line up front
- `vacation-windows.html` — every 1/2/3-week trip option
- `scoreboard.html` — day-by-day scoreboard (yesterday/today/tomorrow + month calendar)
- `schedules.html` — verified schedule tables with official source links
- `radio.html` — Bay Area AM/FM radio guide (KNBR, KSFO, Westwood One)
- `methodology.html` — how "free" is defined
- `flagged.html` — unverified items & irregularities for review

## Data
`data/verified-schedules.json` — every date with its official source URL. Anything not confirmed by an official source is marked `ESTIMATED`, never guessed.

## Sources (official)
- MLB: https://www.mlb.com/press-release/press-release-mlb-announces-2026-regular-season-schedule · https://www.mlb.com/news/mlb-2027-schedule-released
- NFL: https://media.nfl.com/football-information/2026/news/2026-nfl-schedule-announced
- 49ers: https://www.49ers.com/news/49ers-finalize-2026-preseason-dates-and-times
- Stanford: https://gostanford.com/sports/football/schedule
- Cal: https://calbears.com/sports/football/schedule/2026
- Westwood One: https://www.westwoodonesports.com/nfl-schedule/

See `COORDINATION.md` for the verification log.
