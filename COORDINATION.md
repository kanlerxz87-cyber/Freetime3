# COORDINATION — Freetime3 (Vacation Windows)

Session ID: `arena-f23a77a4-freetime3` · Branch: `arena/f23a77a4-freetime3` · Base: `6429edc` (main)
This session is the **final integration session** (repo was empty except README; no other sessions active).

## Task board

| # | Task | Status | Owner | Files |
|---|------|--------|-------|-------|
| 1 | Verify official schedules (MLB/NFL/NCAAF/Westwood One) + durations | needs review | arena-f23a77a4 | `data/verified-schedules.json` |
| 2 | Compute free vacation windows 2027–2029 | needs review | arena-f23a77a4 | `data/verified-schedules.json`, site pages |
| 3 | Build GitHub Pages site (landing + subpages + scoreboard) | done | arena-f23a77a4 | `site/`, `index.html` |
| 4 | PR to main + merge + confirm Pages deploy | done | arena-f23a77a4 / arena-9000e9d9 | #1, #2, #3, #4 |

## Verification log (2026-11-25)
- MLB 2026: Opening Night 2026-03-25 (NYY@SF), Opening Day 2026-03-26, regular ends 2026-09-27, postseason 2026-09-29→2026-10-31 — [MLB press release](https://www.mlb.com/press-release/press-release-mlb-announces-2026-regular-season-schedule), [USA Today postseason](https://www.usatoday.com/story/sports/mlb/2026/09/23/mlb-playoffs-schedule-2026-tv-channels-how-to-watch-stream/91901872007/)
- MLB 2027: Opening Night 2027-03-24, Opening Day 2027-03-25, ends 2027-09-26, All-Star 2027-07-13 Wrigley — [MLB 2027 release](https://www.mlb.com/news/mlb-2027-schedule-released). Postseason 2027 = ESTIMATED.
- NFL 2026: Kickoff 2026-09-09 (NE@SEA), Week 18 ends 2027-01-10, Super Bowl LXI 2027-02-14 SoFi — [NFL 2026 release](https://media.nfl.com/football-information/2026/news/2026-nfl-schedule-announced). 49ers preseason Aug 13/20/27 — [49ers.com](https://www.49ers.com/news/49ers-finalize-2026-preseason-dates-and-times)
- Stanford 2026 (12 games, Aug 29–Nov 28) — [gostanford.com schedule](https://gostanford.com/sports/football/schedule); Cal 2026 (12 games, Sep 5–Nov 28) — [calbears.com schedule](https://calbears.com/sports/football/schedule/2026)
- Westwood One NFL national radio (TNF/SNF/MNF + playoffs + Super Bowl) — [westwoodonesports.com/nfl-schedule](https://www.westwoodonesports.com/nfl-schedule/)
- Duration values from earlier work were based on third-party publications and are not retained as verified official facts; they were removed from the active data file and flagged as unverified.
- 2028/2029 MLB+NFL+NCAAF: **NOT RELEASED** as of 2026-11-25. An earlier implementation inferred estimated ranges and is superseded; the corrected source dashboard leaves these dates blank and marks coverage unverified.

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
- Rebase encountered add/add and content conflicts when the parallel integration landed. Preserved its board, README and site; the supplemental dashboard remains in `docs/`. At that time no Pages source change was requested; the later final integration updated the root landing page and Pages workflow.
- Request for the root site's owner: retract the verified February 15–March 23 window. The official spring opener above already conflicts on February 19. Update root navigation to point at the spring-aware planner; root files were not changed by this session.

- Supplemental integration PR: [#2](https://github.com/kanlerxz87-cyber/Freetime3/pull/2). See the PR timeline for the merge result.

## Current Arena session — 9000e9d9

| Task | Status | Owner | Scope |
|---|---|---|---|
| Correct the root vacation-window claim, integrate a source-first dashboard, and add Pages build/deploy checks | needs review | 9000e9d9 | `COORDINATION.md`, `README.md`, `index.html`, `source-dashboard.html`, `assets/`, `.github/workflows/pages.yml`, `.nojekyll`, category redirect pages, `data/verified-schedules.json` |

### Changes and verification

- Main advanced while this branch was active with merged PRs #1 and #2. Rebase conflicts were resolved by preserving the existing `site/`, `docs/`, model/tests and source history. The existing root content was corrected rather than discarded; category URLs now redirect into the source-first dashboard sections.
- **Correction:** the earlier root claim “verified free Feb 15–Mar 23, 2027” was wrong. MLB's official 2027 Spring Training announcement says play begins Feb 19 and includes scheduled exhibitions. The NFL source confirms Super Bowl LXI on Feb 14; that does not prove a conflict-free multi-week radio window. The current site gives no certified 1/2/3-week vacation window.
- 2027 MLB regular-season schedule: [official Rays/MLB announcement](https://www.mlb.com/press-release/rays-announce-2027-regular-season-schedule) says all 30 clubs released schedules and notes schedules subject to change; [official Spring Training announcement](https://www.mlb.com/press-release/press-release-mlb-announces-2027-spring-training-schedule) confirms Feb 19 opening and additional exhibition dates to be added.
- Official MLB data: [StatsAPI schedule endpoint](https://statsapi.mlb.com/api/v1/schedule), [official game-type reference](https://statsapi.mlb.com/api/v1/gameTypes), and [2027-03-25 example query](https://statsapi.mlb.com/api/v1/schedule?sportId=1&date=2027-03-25&gameTypes=S%2CR%2CF%2CD%2CL%2CW%2CC%2CP%2CA%2CI%2CE), which returned 14 games. Dashboard queries the official feed by selected month for 2026–2027; source failure leaves status unverified. All 30 MLB club links are present; Giants/Athletics are highlighted.
- NFL source reviewed: [official 2026–27 important dates](https://www.nfl.com/news/2026-27-national-football-league-important-dates). Only confirmed 2027 postseason milestones are reported; a full 2027 NFL regular-season slate is not claimed.
- Cal's 2027 opponent announcement is partial: [official Cal release](https://calbears.com/news/2026/9/16/california-football-announces-2027-conference-opponents). Full 2027 Stanford/Cal and 49ers slates are not verified in this integration.
- Radio sources reviewed: [Westwood One NFL schedule](https://www.westwoodonesports.com/nfl-schedule/) and [KNBR weekly programming](https://www.thesportsleader.com/shows). Dynamic schedule pages do not establish game-by-game AM/FM carriage or reception at Outer Sunset 94122.
- `data/verified-schedules.json` now contains only schedule-status/source facts, with `null` for unverified dates and no inferred season ranges or average-duration numbers. Unsupported third-party duration assumptions were removed from this official-sources record.
- Checks passed: `node --check assets/app.js`; HTML anchor/local asset validation; JSON parsing/status checks; 30-team count; `git diff --check`; local preview HTTP 200. Pages workflow validates anchors/assets and packages root HTML plus assets.

### Remaining review flags (also shown on site)

- Complete 2027–2029 NFL/49ers/Stanford/Cal event schedules and future Westwood One local carriage.
- Complete 2028–2029 MLB schedules, future postseason and specials; only current official releases are linked.
- Actual local station availability and radio end times for an Outer Sunset 94122 standard receiver.
- Official average durations and minute-level intervals. No date can be marked all-sports free until all included sources are complete; blank is not free.

- **PR #3** [Integrate verified Bay Area sports vacation dashboard](https://github.com/kanlerxz87-cyber/Freetime3/pull/3) was merged on 2026-11-25 (merge commit `19685993b0e00abcf988a459d5e42872c1294fd4`). Build and Pages deployment workflow run [45628680380](https://github.com/kanlerxz87-cyber/Freetime3/actions/runs/45628680380) succeeded.
- **PR #4** [Add official references to remaining review flags](https://github.com/kanlerxz87-cyber/Freetime3/pull/4) was merged on 2026-11-25 (merge commit `902a888997c27a73d0a9a1de8b16e2fc97b1f3ea`). Build and Pages deployment workflow run [45628952837](https://github.com/kanlerxz87-cyber/Freetime3/actions/runs/45628952837) succeeded.
- Live GitHub Pages URL: https://kanlerxz87-cyber.github.io/Freetime3/ (Pages reports `status: built`; live page was fetched after deploy and displayed the official MLB feed result for the selected date).
- All-sports schedule gaps remain `needs review` and are published under the on-site Flagged for Review page; they do not block publication.

## Arena session — 8ce435e1

| Task | Status | Owner | Scope |
|---|---|---|---|
| Supplementary verified 2026 data + calendar/schedule tables | needs review | 8ce435e1 | `data/sources.json`, `docs/verification.md`, `site/assets/data.js`, `site/assets/style.css`, `site/calendar.html`, `site/sources.html`, `site/schedules.html` (merged conflict resolved to preserve main site) |

- 2026-11-25: Added verified 2026 schedule rows from official sources (49ers 18 rows incl bye/TBD, Stanford 12, Cal 12, Westwood One NFL national 20) in `site/assets/data.js` with source URLs. Added `site/calendar.html` (day/month scoreboard with PT busy/free estimates) and `site/sources.html`. 
- Sources verified: https://www.49ers.com/schedule/, https://gostanford.com/sports/football/schedule, https://calbears.com/sports/football/schedule, https://www.westwoodonesports.com/nfl-schedule/.
- Flagged/incomplete: full all-MLB/all-NFL per-game 2026-2028 transcription not completed (no fabrication); 2027-2029 per-game schedules unreleased/ESTIMATED; SF 94122 AM/FM carriage unverified. See `site/flagged.html` and `docs/verification.md`.
- Merge resolution: accepted main's conflicted root/site pages to preserve deployed site; kept supplementary data/assets/calendar/sources files added by this session.
