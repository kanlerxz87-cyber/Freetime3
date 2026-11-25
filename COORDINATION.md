# COORDINATION — Freetime3 (Vacation Windows)

Session ID: `arena-f23a77a4-freetime3` · Branch: `arena/f23a77a4-freetime3` · Base: `6429edc` (main)
This session is the **final integration session** (repo was empty except README; no other sessions active).

## Task board

| # | Task | Status | Owner | Files |
|---|------|--------|-------|-------|
| 1 | Verify official schedules (MLB/NFL/NCAAF/Westwood One) + durations | done | arena-f23a77a4 | `data/verified-schedules.json` |
| 2 | Compute free vacation windows 2027–2029 | done | arena-f23a77a4 | `data/verified-schedules.json`, site pages |
| 3 | Build GitHub Pages site (landing + subpages + scoreboard) | done | arena-f23a77a4 | `site/`, `index.html` |
| 4 | PR to main + merge + confirm Pages deploy | in progress | arena-f23a77a4 | — |

## Verification log (2026-11-25)
- MLB 2026: Opening Night 2026-03-25 (NYY@SF), Opening Day 2026-03-26, regular ends 2026-09-27, postseason 2026-09-29→2026-10-31 — [MLB press release](https://www.mlb.com/press-release/press-release-mlb-announces-2026-regular-season-schedule), [USA Today postseason](https://www.usatoday.com/story/sports/mlb/2026/09/23/mlb-playoffs-schedule-2026-tv-channels-how-to-watch-stream/91901872007/)
- MLB 2027: Opening Night 2027-03-24, Opening Day 2027-03-25, ends 2027-09-26, All-Star 2027-07-13 Wrigley — [MLB 2027 release](https://www.mlb.com/news/mlb-2027-schedule-released). Postseason 2027 = ESTIMATED.
- NFL 2026: Kickoff 2026-09-09 (NE@SEA), Week 18 ends 2027-01-10, Super Bowl LXI 2027-02-14 SoFi — [NFL 2026 release](https://media.nfl.com/football-information/2026/news/2026-nfl-schedule-announced). 49ers preseason Aug 13/20/27 — [49ers.com](https://www.49ers.com/news/49ers-finalize-2026-preseason-dates-and-times)
- Stanford 2026 (12 games, Aug 29–Nov 28) — [gostanford.com schedule](https://gostanford.com/sports/football/schedule); Cal 2026 (12 games, Sep 5–Nov 28) — [calbears.com schedule](https://calbears.com/sports/football/schedule/2026)
- Westwood One NFL national radio (TNF/SNF/MNF + playoffs + Super Bowl) — [westwoodonesports.com/nfl-schedule](https://www.westwoodonesports.com/nfl-schedule/)
- Durations: MLB 2h38m (2025 avg) — [Lines.com](https://www.lines.com/guides/how-long-is-baseball-game/1523); NFL 3h12m — [HuffPost](https://huffsports.com/football/how-long-is-an-nfl-game/)
- 2028/2029 MLB+NFL+NCAAF: **NOT RELEASED** as of 2026-11-25 → all marked ESTIMATED on site.

## Irregularities flagged
- 2026 NFL Kickoff is Wednesday Sep 9 (not Thursday) due to Melbourne game Sep 10 — verified, not an error.
- 2027 MLB Opening Night matchup TBD (Netflix) — flagged.
- 2028/2029 schedules don't exist yet — estimates only, clearly labeled.
- Prior sites (VacationSchedule, ScheduleFreeTime, RADIOSF) unreachable via fetch (JS-heavy) — rebuilt from official sources instead.

## Handoff log
- 2026-11-25: Session claimed all tasks (empty repo, no conflicts). Built site, verified data, opened PR.
