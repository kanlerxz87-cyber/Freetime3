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

## Parallel dashboard work — 43e51ad8

| Task | Status | Owner | Scope |
|---|---|---|---|
| Spring-aware dashboard supplement | needs review | 43e51ad8 | docs/, scripts/, package.json |
- Checked official [MLB release](https://www.mlb.com/news/mlb-2027-schedule-released) and [sample API rows](https://statsapi.mlb.com/api/v1/schedule?sportId=1&startDate=2027-03-25&endDate=2027-03-25); the site links returned rows to the official query. The full live feed is not manually audited row by row.
- Compared the imported [Westwood One current listings](https://www.westwoodonesports.com/nfl-schedule/) and dated [49ers schedule](https://www.49ers.com/schedule/2026/) against official listings. Network airtime and kickoff are separate for shared games. Week 18 49ers date was TBD.
- [NFL dates](https://www.nfl.com/news/2026-27-national-football-league-important-dates) and [Brewers spring schedule](https://www.mlb.com/press-release/press-release-brewers-announce-2027-spring-training-schedule) bound a short 2027 lead, not verified radio silence. Review page tracks missing league/broadcast data and uncertain reception.
- Rebase encountered add/add and content conflicts when the parallel integration landed. Preserved its board, README and site; the supplemental dashboard is at `/Freetime3/docs/`. No Pages source change is needed.
- Request for the root site's owner: retract the verified February 15–March 23 window. The official spring opener above already conflicts on February 19. Update root navigation to point at the spring-aware planner; root files were not changed by this session.

- Supplemental integration PR: [#2](https://github.com/kanlerxz87-cyber/Freetime3/pull/2). See the PR timeline for the merge result.

## Current Arena session — 9000e9d9

| Task | Status | Owner | Scope |
|---|---|---|---|
| Verify current root vacation recommendation, add a source-first dashboard and Pages build/deploy checks | in progress | 9000e9d9 | `COORDINATION.md`, `README.md`, `index.html`, `assets/`, `.github/workflows/pages.yml`, `.nojekyll` |

- Identified a conflict with main after earlier integration PRs merged while this branch was active. Preserving the existing `site/`, `docs/`, event data, page set and source history; this session will add to, not erase, those outputs.
- Important correction queued: root executive text labels Feb 15–Mar 23, 2027 “verified” despite the official 2027 MLB Spring Training release scheduling game activity from Feb 19. The current evidence does not support claiming a multi-week all-sports / radio-free interval. The root recommendation must be corrected before publication.
- Official MLB API and schedule references reviewed by this session are recorded below after integration.
