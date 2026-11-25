# Free Time Vacation — Bay Area Sports Planner

A source-first planner for avoiding live sports conflicts while vacationing from the San Francisco Bay Area. The project includes the original multi-page schedule/scoreboard, a supplemental live-feed planner under `docs/`, and this session's source-first dashboard at [`source-dashboard.html`](source-dashboard.html).

## Executive summary — read this before booking

**No complete, verified, week-long all-sports/radio-free vacation window can currently be certified for 2027–2029.** Do not rely on the older Feb–Mar window dates shown in historical site content without checking the corrected executive summary and flagged items. The 2027 MLB schedule includes Spring Training play beginning February 19, which invalidates the earlier claim that February 15–March 23 was a verified sports-free span. Unverified league/radio coverage remains a separate blocker even between known MLB dates.

The planner does not treat missing data as free. It leaves minutes/end-times unverified where official sources do not supply complete coverage; the generated status is not a substitute for checking the linked league, team and station schedules.

## Pages

- `index.html` — landing dashboard
- `executive-summary.html` — concise decision summary
- `vacation-windows.html` — candidate window analysis and limitations
- `scoreboard.html` — day-by-day schedule view
- `schedules.html` — schedules and official sources
- `radio.html` — Bay Area radio directory
- `methodology.html` — definition and duration assumptions
- `flagged.html` — unverified items and irregularities
- `source-dashboard.html` — backwards-compatible redirect to the source-first landing dashboard
- Category links (`executive-summary.html`, `vacation-windows.html`, `scoreboard.html`, `schedules.html`, `radio.html`, `methodology.html`, `flagged.html`) redirect to the corresponding current dashboard section so older pages cannot show superseded free-window claims
- `docs/` — supplemental live MLB schedule view retained in the repository

## Verified official references

- [MLB 2027 regular-season schedule release — all 30 clubs](https://www.mlb.com/press-release/rays-announce-2027-regular-season-schedule)
- [MLB 2027 Spring Training release](https://www.mlb.com/press-release/press-release-mlb-announces-2027-spring-training-schedule)
- [MLB StatsAPI schedule](https://statsapi.mlb.com/api/v1/schedule) · [game types](https://statsapi.mlb.com/api/v1/gameTypes)
- [NFL 2026–27 important dates](https://www.nfl.com/news/2026-27-national-football-league-important-dates)
- [NFL schedules](https://www.nfl.com/schedules/)
- [Cal 2027 conference-opponent announcement](https://calbears.com/news/2026/9/16/california-football-announces-2027-conference-opponents)
- [Westwood One NFL schedule](https://www.westwoodonesports.com/nfl-schedule/)
- [KNBR programming schedule](https://www.thesportsleader.com/shows)

## Supplementary verified 2026 data (session 8ce435e1)

Additional verified 2026 rows were added in `site/assets/data.js` (49ers, Stanford, Cal, Westwood One NFL national broadcasts) with official source links in `data/sources.json` and verification notes in `docs/verification.md`. Supplementary calendar/sources pages: `site/calendar.html`, `site/sources.html`. Unverified/incomplete items remain flagged; no per-game rows were fabricated.

## Local preview

Open `index.html` or run any static HTTP server in the repository root. The live MLB view queries MLB's official StatsAPI in the browser. If that request fails, the calendar reports an unverified state and links the official source; it does not substitute guessed games.
