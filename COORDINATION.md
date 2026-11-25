# COORDINATION.md

Shared task board for parallel agent sessions. Read before starting; claim before working.

## Session

- **Session ID**: 9987b915
- **Branch**: `arena/9987b915-freetime3`
- **Base**: `6429edc60fdfb4b0af5d7e80bcb181310ec3b64a` (main)
- **Started**: 2026-11-25 (session)

## Tasks

| Task | Status | Owner | Files/Scope | Notes |
|------|--------|-------|-------------|-------|
| Repo audit & coordination setup | done | 9987b915 | COORDINATION.md | Initial claim committed. |
| Research official schedules (MLB/NFL/NCAAF/Westwood One) | done | 9987b915 | data/sources.md, docs/data/schedule-data.js, scripts/build_schedule.py | Official sources gathered; unreleased 2027-2029 schedules marked estimated. |
| Data model & schedule generation (2026-2029) | done | 9987b915 | scripts/build_schedule.py, docs/data/schedule-data.js | Generated 1133 day entries, 59 verified/specific events, 19 season windows. |
| Site build (GitHub Pages, dashboard/calendar/scoreboard) | done | 9987b915 | docs/, index.html, README.md | Static site in docs/ with dashboard, calendar/scoreboard, games table, sources, flagged review. |
| Verification pass & flagged irregularities | done | 9987b915 | docs/sources.html, docs/flagged.html, data/sources.md | No hallucinated values; TBA/estimated labeled; 12 flagged items published. |
| Final integration, PR, merge, deploy | in progress | 9987b915 | all | Will commit, PR to main, merge, configure Pages, verify deploy. |

## Sources used (primary/official)

- MLB 2027 schedule release: https://www.mlb.com/news/mlb-2027-schedule-released (accessed 2026-11-25)
- MLB schedule hub: https://www.mlb.com/schedule (accessed 2026-11-25)
- NFL 2026-27 important dates: https://www.nfl.com/news/2026-27-national-football-league-important-dates (accessed 2026-11-25)
- NFL schedules: https://www.nfl.com/schedules/ (accessed 2026-11-25)
- 49ers schedule: https://www.49ers.com/schedule/ (accessed 2026-11-25)
- Westwood One NFL schedule: https://www.westwoodonesports.com/nfl-schedule/ (accessed 2026-11-25)
- Westwood One station finder: https://www.westwoodonesports.com/station-finder (accessed 2026-11-25)
- Stanford football 2026 schedule: https://gostanford.com/sports/football/schedule (accessed 2026-11-25)
- Cal football 2026 schedule: https://calbears.com/sports/football/schedule (accessed 2026-11-25)
- NFL Operations schedule creation: https://operations.nfl.com/gameday/nfl-schedule/creating-the-nfl-schedule/ (accessed 2026-11-25)
- MLB postseason: https://www.mlb.com/postseason (accessed 2026-11-25)
- Super Bowl LXII date report (secondary, NFL announcement reported): https://www.atlantanewsfirst.com/2026/07/24/nfl-sets-date-super-bowl-lxii-mercedes-benz-stadium-atlanta/ (accessed 2026-11-25)

## Verification performed

- `python3 scripts/build_schedule.py` executed successfully; generated `docs/data/schedule-data.js`.
- Node sanity check: `days 1133 events 59 windows 19 vac [ '2027','2028','2029' ]`.
- Local HTTP smoke test: `docs/index.html` returned HTTP 200.
- Manual data rule check: no invented game times; TBA left as TBA; 2027-2029 unreleased schedules marked estimated; every row in UI renders source link(s) from source registry.
- Known limitation: local AM/FM affiliate reception for 94122 not fully verified via station finder; flagged.

## Flagged irregularities (published on docs/flagged.html)

- F-001 MLB 2028 schedule unreleased (estimated window).
- F-002 MLB 2029 schedule unreleased (estimated window).
- F-003 MLB 2027 postseason/game times partially unreleased.
- F-004 NFL 2027-28 season schedule unreleased (estimated; SB LXII date anchored).
- F-005 NFL 2028-29, 2029-30 schedules unreleased (estimated).
- F-006 49ers 2027-2029 game dates unreleased.
- F-007 Stanford/Cal 2027-2029 schedules unreleased.
- F-008 Westwood One SF 94122 AM/FM affiliate reception not fully verified.
- F-009 Super Bowl LXII date confirmed via secondary reporting; manual NFL.com confirmation recommended.
- F-010 Average game durations are estimates.
- F-011 Some 2026 Stanford/Cal times TBA.
- F-012 MLB.com 2027 release page fetch anomaly during automated extraction; key dates corroborated.

## Handoff / log

- 2026-11-25 9987b915: Built static site and data generator. Preparing commit, PR, merge, and Pages deployment.
