#!/usr/bin/env python3
"""
Build schedule data for FreeTime Vacation dashboard.
Generates docs/data/schedule-data.js with day-by-day entries.

RULES:
- Every entry must carry source metadata.
- If not confirmed from an official source, mark status='estimated' or 'unverified'.
- Never invent game times/scores. Estimated times/durations must be labeled.
"""
from __future__ import annotations
import json, datetime, math, os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "data" / "schedule-data.js"

# --- Sources (official/verified) ---
SOURCES = {
    "mlb_2027_release": {
        "title": "MLB releases 2027 regular-season schedule",
        "url": "https://www.mlb.com/news/mlb-2027-schedule-released",
        "publisher": "MLB.com",
        "accessed": "2026-11-25",
        "type": "official",
    },
    "mlb_schedule_2027": {
        "title": "MLB Schedule - 2027 (official schedule hub)",
        "url": "https://www.mlb.com/schedule/2027-03-23",
        "publisher": "MLB.com",
        "accessed": "2026-11-25",
        "type": "official",
    },
    "mlb_schedule_2026": {
        "title": "MLB Schedule - 2026 (official schedule hub)",
        "url": "https://www.mlb.com/schedule",
        "publisher": "MLB.com",
        "accessed": "2026-11-25",
        "type": "official",
    },
    "nfl_important_dates_2026_27": {
        "title": "2026-27 National Football League important dates",
        "url": "https://www.nfl.com/news/2026-27-national-football-league-important-dates",
        "publisher": "NFL.com",
        "accessed": "2026-11-25",
        "type": "official",
    },
    "nfl_schedule": {
        "title": "NFL Schedule (official)",
        "url": "https://www.nfl.com/schedules/",
        "publisher": "NFL.com",
        "accessed": "2026-11-25",
        "type": "official",
    },
    "nfl_49ers_schedule": {
        "title": "San Francisco 49ers Schedule (official)",
        "url": "https://www.49ers.com/schedule/",
        "publisher": "49ers.com",
        "accessed": "2026-11-25",
        "type": "official",
    },
    "westwood_one_nfl": {
        "title": "Westwood One Sports - NFL Schedule",
        "url": "https://www.westwoodonesports.com/nfl-schedule/",
        "publisher": "Westwood One Sports",
        "accessed": "2026-11-25",
        "type": "official-broadcaster",
    },
    "westwood_one_station_finder": {
        "title": "Westwood One Sports - Station Finder",
        "url": "https://www.westwoodonesports.com/station-finder",
        "publisher": "Westwood One Sports",
        "accessed": "2026-11-25",
        "type": "official-broadcaster",
    },
    "stanford_2026": {
        "title": "Stanford Football 2026 Schedule",
        "url": "https://gostanford.com/sports/football/schedule",
        "publisher": "GoStanford.com",
        "accessed": "2026-11-25",
        "type": "official",
    },
    "cal_2026": {
        "title": "California Golden Bears Football 2026 Schedule",
        "url": "https://calbears.com/sports/football/schedule",
        "publisher": "CalBears.com",
        "accessed": "2026-11-25",
        "type": "official",
    },
    "super_bowl_lxii_date": {
        "title": "NFL sets date for Super Bowl LXII at Mercedes-Benz Stadium in Atlanta",
        "url": "https://www.atlantanewsfirst.com/2026/07/24/nfl-sets-date-super-bowl-lxii-mercedes-benz-stadium-atlanta/",
        "publisher": "Atlanta News First (reporting NFL announcement)",
        "accessed": "2026-11-25",
        "type": "secondary-reporting-nfl-announcement",
    },
    "mlb_postseason_format": {
        "title": "MLB Postseason Format",
        "url": "https://www.mlb.com/postseason",
        "publisher": "MLB.com",
        "accessed": "2026-11-25",
        "type": "official",
    },
    "nfl_operations": {
        "title": "NFL Football Operations - Creating the NFL Schedule",
        "url": "https://operations.nfl.com/gameday/nfl-schedule/creating-the-nfl-schedule/",
        "publisher": "NFL Football Operations",
        "accessed": "2026-11-25",
        "type": "official",
    },
}

# --- Average durations (researched estimates, labeled) ---
DURATIONS = {
    "mlb_game_minutes": {"value": 165, "label": "~2h 45m (recent MLB avg ~2:40; use 165m conservative)", "status": "estimated"},
    "nfl_game_minutes": {"value": 195, "label": "~3h 15m (typical NFL broadcast window)", "status": "estimated"},
    "ncaaf_game_minutes": {"value": 210, "label": "~3h 30m (typical college football broadcast window)", "status": "estimated"},
}

# --- Helper models ---
def day_iso(d):
    return d.isoformat()

def add_event(events, **kw):
    # required: date, title, category, priority, status, source_ids
    events.append(kw)

# --- Known/confirmed games from official sources ---

# Westwood One NFL 2026-27 broadcasts (from fetched westwoodonesports.com/nfl-schedule/ on 2026-11-25)
# Times shown on page as ET; convert to PST (ET-3). We record both.
WWO_NFL_2026 = [
    # date, title, time_et, note, url
    ("2026-11-25", "Green Bay Packers at Los Angeles Rams", "19:30", "Thanksgiving Wednesday / TNF package", "https://www.westwoodonesports.com/events/548511"),
    ("2026-11-26", "Chicago Bears at Detroit Lions", "12:30", "NFL Thanksgiving Day Tripleheader", "https://www.westwoodonesports.com/events/548512"),
    ("2026-11-26", "Philadelphia Eagles at Dallas Cowboys", "16:15", "NFL Thanksgiving Day Tripleheader", "https://www.westwoodonesports.com/events/548513"),
    ("2026-11-26", "Kansas City Chiefs at Buffalo Bills", "20:00", "NFL Thanksgiving Day Tripleheader", "https://www.westwoodonesports.com/events/548514"),
    ("2026-11-27", "Denver Broncos at Pittsburgh Steelers", "14:30", "NFL Black Friday Game", "https://www.westwoodonesports.com/events/548515"),
    ("2026-11-29", "Las Vegas Raiders at Cleveland Browns", "19:30", "Sunday Night Football", "https://www.westwoodonesports.com/events/548502"),
    ("2026-11-30", "Carolina Panthers at Tampa Bay Buccaneers", "19:00", "Monday Night Football", "https://www.westwoodonesports.com/events/548544"),
    ("2026-12-03", "Kansas City Chiefs at Los Angeles Rams", "19:30", "Thursday Night Football", "https://www.westwoodonesports.com/events/548566"),
    ("2026-12-06", "Houston Texans at Pittsburgh Steelers", "19:30", "Sunday Night Football", "https://www.westwoodonesports.com/events/548503"),
    ("2026-12-07", "Dallas Cowboys at Seattle Seahawks", "19:00", "Monday Night Football", "https://www.westwoodonesports.com/events/548545"),
    ("2026-12-10", "Minnesota Vikings at New England Patriots", "19:30", "Thursday Night Football", "https://www.westwoodonesports.com/events/548567"),
    ("2026-12-13", "Buffalo Bills at Green Bay Packers", "19:30", "Sunday Night Football", "https://www.westwoodonesports.com/events/548505"),
    ("2026-12-14", "Pittsburgh Steelers at Jacksonville Jaguars", "19:00", "Monday Night Football", "https://www.westwoodonesports.com/events/548546"),
    ("2026-12-17", "San Francisco 49ers at Los Angeles Chargers", "19:30", "Thursday Night Football (49ERS HIGH PRIORITY)", "https://www.westwoodonesports.com/events/548568"),
    ("2026-12-19", "Seattle Seahawks at Philadelphia Eagles", "16:30", "Week 15 Saturday NFL Doubleheader", "https://www.westwoodonesports.com/events/548517"),
    ("2026-12-19", "Chicago Bears at Buffalo Bills", "20:00", "Week 15 Saturday NFL Doubleheader", "https://www.westwoodonesports.com/events/548518"),
    ("2026-12-20", "Detroit Lions at Minnesota Vikings", "19:30", "Sunday Night Football", "https://www.westwoodonesports.com/events/548506"),
    ("2026-12-21", "New England Patriots at Kansas City Chiefs", "19:00", "Monday Night Football", "https://www.westwoodonesports.com/events/548548"),
    ("2026-12-24", "Houston Texans at Philadelphia Eagles", "19:30", "Thursday Night Football", "https://www.westwoodonesports.com/events/548569"),
    ("2026-12-25", "Green Bay Packers at Chicago Bears", "12:30", "Christmas Day NFL Tripleheader", "https://www.westwoodonesports.com/events/548528"),
    ("2026-12-25", "Buffalo Bills at Denver Broncos", "16:15", "Christmas Day NFL Tripleheader", "https://www.westwoodonesports.com/events/548531"),
    ("2026-12-25", "Los Angeles Rams at Seattle Seahawks", "20:00", "Christmas Day NFL Tripleheader", "https://www.westwoodonesports.com/events/548534"),
    ("2026-12-26", "Week 16 Saturday Doubleheader TBA", "16:00", "Week 16 Saturday NFL Doubleheader - teams TBA", "https://www.westwoodonesports.com/events/548519"),
    ("2026-12-26", "Week 16 Saturday Doubleheader TBA", "20:00", "Week 16 Saturday NFL Doubleheader - teams TBA", "https://www.westwoodonesports.com/events/548520"),
    ("2026-12-27", "Jacksonville Jaguars at Dallas Cowboys", "19:30", "Sunday Night Football", "https://www.westwoodonesports.com/events/548507"),
    ("2026-12-28", "New York Giants at Detroit Lions", "19:00", "Monday Night Football", "https://www.westwoodonesports.com/events/548550"),
    ("2026-12-31", "Baltimore Ravens at Cincinnati Bengals", "19:30", "Thursday Night Football", "https://www.westwoodonesports.com/events/548570"),
    ("2027-01-02", "Week 17 Saturday Doubleheader TBA", "16:00", "Week 17 Saturday NFL Doubleheader - teams TBA", "https://www.westwoodonesports.com/events/548521"),
    ("2027-01-02", "Week 17 Saturday Doubleheader TBA", "20:00", "Week 17 Saturday NFL Doubleheader - teams TBA", "https://www.westwoodonesports.com/events/548522"),
    ("2027-01-03", "Philadelphia Eagles at San Francisco 49ers", "19:30", "Sunday Night Football (49ERS HIGH PRIORITY)", "https://www.westwoodonesports.com/events/548509"),
    ("2027-01-04", "Houston Texans at Green Bay Packers", "19:00", "Monday Night Football", "https://www.westwoodonesports.com/events/548552"),
    ("2027-01-09", "Week 18 Saturday Tripleheader TBA", "12:30", "Week 18 Saturday NFL Tripleheader - teams TBA", "https://www.westwoodonesports.com/events/548523"),
    ("2027-01-09", "Week 18 Saturday Tripleheader TBA", "16:15", "Week 18 Saturday NFL Tripleheader - teams TBA", "https://www.westwoodonesports.com/events/548524"),
    ("2027-01-09", "Week 18 Saturday Tripleheader TBA", "20:00", "Week 18 Saturday NFL Tripleheader - teams TBA", "https://www.westwoodonesports.com/events/548526"),
    ("2027-01-10", "Week 18 Sunday Night Football - Teams TBA", "19:30", "Sunday Night Football - teams TBA", "https://www.westwoodonesports.com/events/548510"),
]

# Stanford 2026 (from gostanford.com/sports/football/schedule fetched 2026-11-25)
STANFORD_2026 = [
    ("2026-08-29", "vs Hawai'i", "16:00", "PT", "W 37-27", "https://gostanford.com/sports/football/schedule"),
    ("2026-09-04", "vs #7 Miami", "18:00", "PT", "L 6-45", "https://gostanford.com/sports/football/schedule"),
    ("2026-09-19", "at Duke", "13:00", "PT", "L 7-35", "https://gostanford.com/sports/football/schedule"),
    ("2026-09-26", "vs Georgia Tech", "19:30", "PT", "W 34-27", "https://gostanford.com/sports/football/schedule"),
    ("2026-10-03", "at Wake Forest", "09:00", "PT", "L 3-57", "https://gostanford.com/sports/football/schedule"),
    ("2026-10-10", "at Notre Dame", "12:30", "PT", "L 7-58", "https://gostanford.com/sports/football/schedule"),
    ("2026-10-17", "vs Elon (Reunion Homecoming)", "16:30", "PT", "W 34-7", "https://gostanford.com/sports/football/schedule"),
    ("2026-10-23", "vs North Carolina St.", "19:30", "PT", "W 31-28", "https://gostanford.com/sports/football/schedule"),
    ("2026-10-31", "at Louisville", "", "PT", "TBA", "https://gostanford.com/sports/football/schedule"),
    ("2026-11-14", "at Virginia Tech", "", "PT", "TBA", "https://gostanford.com/sports/football/schedule"),
    ("2026-11-21", "at California (129th Big Game)", "", "PT", "TBA", "https://gostanford.com/sports/football/schedule"),
    ("2026-11-28", "vs SMU", "", "PT", "TBA", "https://gostanford.com/sports/football/schedule"),
]

# Cal 2026 (from calbears.com fetched 2026-11-25)
CAL_2026 = [
    ("2026-09-05", "vs UCLA", "19:30", "PT", "L 24-45", "https://calbears.com/sports/football/schedule"),
    ("2026-09-12", "at Syracuse", "12:30", "PT", "W 21-18", "https://calbears.com/sports/football/schedule"),
    ("2026-09-19", "vs Wagner", "12:30", "PT", "W 49-7", "https://calbears.com/sports/football/schedule"),
    ("2026-09-25", "vs Clemson", "19:30", "PT", "L 10-24", "https://calbears.com/sports/football/schedule"),
    ("2026-10-03", "at UNLV", "12:30", "PT", "L 31-39", "https://calbears.com/sports/football/schedule"),
    ("2026-10-10", "vs Virginia Tech", "12:30", "PT", "W 25-20", "https://calbears.com/sports/football/schedule"),
    ("2026-10-17", "vs Wake Forest", "19:30", "PT", "L 7-41", "https://calbears.com/sports/football/schedule"),
    ("2026-10-24", "at SMU", "09:00", "PT", "L 20-59", "https://calbears.com/sports/football/schedule"),
    ("2026-10-31", "at NC State", "09:00", "PT", "L 10-31", "https://calbears.com/sports/football/schedule"),
    ("2026-11-14", "at Virginia", "12:30", "PT", "TBD/TBA on site", "https://calbears.com/sports/football/schedule"),
    ("2026-11-21", "vs Stanford (129th Big Game)", "", "PT", "TBA", "https://calbears.com/sports/football/schedule"),
    ("2026-11-28", "vs Pittsburgh", "", "PT", "TBA", "https://calbears.com/sports/football/schedule"),
]

def et_to_pt(time_et):
    # simple ET->PT -3h for fixed times; DST edge cases exist but for schedule display this is acceptable if labeled
    if not time_et:
        return ""
    hh, mm = map(int, time_et.split(":"))
    pt_h = (hh - 3) % 24
    return f"{pt_h:02d}:{mm:02d}"

def build_events():
    events = []

    # Westwood One NFL 2026
    for date, title, time_et, note, url in WWO_NFL_2026:
        is_49ers = "49ers" in title
        cats = ["westwood_one_nfl"]
        if is_49ers:
            cats.append("nfl_49ers")
        add_event(events,
            date=date,
            title=title,
            time_pt=et_to_pt(time_et),
            time_et=time_et,
            duration_minutes=DURATIONS["nfl_game_minutes"]["value"],
            duration_label=DURATIONS["nfl_game_minutes"]["label"],
            category="NFL / Westwood One",
            categories=cats,
            priority="high" if is_49ers else "high",  # WWO national NFL is high priority per user
            status="verified",
            note=note,
            source_ids=["westwood_one_nfl"],
            source_url=url,
        )

    # Stanford 2026
    for date, matchup, time_pt, tz, result, url in STANFORD_2026:
        add_event(events,
            date=date,
            title=f"Stanford Football {matchup}",
            time_pt=time_pt,
            time_et="",
            duration_minutes=DURATIONS["ncaaf_game_minutes"]["value"],
            duration_label=DURATIONS["ncaaf_game_minutes"]["label"],
            category="NCAAF Stanford",
            categories=["ncaaf_stanford"],
            priority="high",
            status="verified" if time_pt else "verified-tba-time",
            note=f"Result/Status: {result}. Time {'TBA' if not time_pt else time_pt+' PT'} per official schedule.",
            source_ids=["stanford_2026"],
            source_url=url,
        )

    # Cal 2026
    for date, matchup, time_pt, tz, result, url in CAL_2026:
        add_event(events,
            date=date,
            title=f"California Football {matchup}",
            time_pt=time_pt,
            time_et="",
            duration_minutes=DURATIONS["ncaaf_game_minutes"]["value"],
            duration_label=DURATIONS["ncaaf_game_minutes"]["label"],
            category="NCAAF California",
            categories=["ncaaf_cal"],
            priority="high",
            status="verified" if time_pt else "verified-tba-time",
            note=f"Result/Status: {result}. Time {'TBA' if not time_pt else time_pt+' PT'} per official schedule.",
            source_ids=["cal_2026"],
            source_url=url,
        )

    return events

# --- Season windows (for vacation analysis) ---
# These are modeled windows. Where official dates exist, mark verified; otherwise estimated with basis.
SEASON_WINDOWS = [
    # 2026 MLB - season is ongoing; regular season ends late Sep 2026 typically; postseason follows.
    {
        "id": "mlb_2026_regular",
        "label": "MLB 2026 Regular Season (all 30 teams)",
        "start": "2026-03-25", "end": "2026-09-27",
        "category": "MLB", "priority": "high",
        "status": "estimated-window",
        "note": "Window is approximate for planning. 2026 regular season began with traditional Opening Day period; end date approximate. Verify exact dates/game times on MLB official schedule.",
        "source_ids": ["mlb_schedule_2026"],
    },
    {
        "id": "mlb_2026_postseason",
        "label": "MLB 2026 Postseason (potential games)",
        "start": "2026-09-29", "end": "2026-11-01",
        "category": "MLB", "priority": "high",
        "status": "estimated-window",
        "note": "Postseason window is estimated; actual games depend on teams/series. Treat as potential busy period until confirmed.",
        "source_ids": ["mlb_postseason_format"],
    },
    # 2027 MLB - verified key dates from MLB.com release
    {
        "id": "mlb_2027_regular",
        "label": "MLB 2027 Regular Season (all 30 teams)",
        "start": "2027-03-24", "end": "2027-09-26",
        "category": "MLB", "priority": "high",
        "status": "verified-window",
        "note": "Opening Night Mar 24 (Netflix, matchup TBD). Traditional Opening Day Mar 25. Regular season ends Sun Sep 26. All 30 teams in action on key dates including Apr 15, May 31, Jun 2, Jul 4, Sep 6, Sep 15. Game-by-game times not all released; treat most days in window as having MLB games.",
        "source_ids": ["mlb_2027_release", "mlb_schedule_2027"],
    },
    {
        "id": "mlb_2027_postseason",
        "label": "MLB 2027 Postseason (potential games, estimated)",
        "start": "2027-09-28", "end": "2027-11-01",
        "category": "MLB", "priority": "high",
        "status": "estimated-window",
        "note": "Postseason dates not officially released. Estimated based on typical MLB postseason calendar following regular season end Sep 26, 2027. Treat as potential busy period.",
        "source_ids": ["mlb_2027_release", "mlb_postseason_format"],
    },
    # 2028 MLB - no official schedule
    {
        "id": "mlb_2028_regular",
        "label": "MLB 2028 Regular Season (all 30 teams) - ESTIMATED",
        "start": "2028-03-30", "end": "2028-10-01",
        "category": "MLB", "priority": "high",
        "status": "estimated-window",
        "note": "ESTIMATE ONLY - official 2028 MLB schedule not released. Window estimated from typical late-March opening / late-Sep or early-Oct end pattern. Verify against MLB.com when released.",
        "source_ids": ["mlb_schedule_2026"],
    },
    {
        "id": "mlb_2028_postseason",
        "label": "MLB 2028 Postseason (potential games, estimated)",
        "start": "2028-10-03", "end": "2028-11-05",
        "category": "MLB", "priority": "high",
        "status": "estimated-window",
        "note": "ESTIMATE ONLY - postseason dates not released. Estimated window.",
        "source_ids": ["mlb_postseason_format"],
    },
    # 2029 MLB
    {
        "id": "mlb_2029_regular",
        "label": "MLB 2029 Regular Season (all 30 teams) - ESTIMATED",
        "start": "2029-03-29", "end": "2029-09-30",
        "category": "MLB", "priority": "high",
        "status": "estimated-window",
        "note": "ESTIMATE ONLY - official 2029 MLB schedule not released. Window estimated from typical pattern. Verify against MLB.com when released.",
        "source_ids": ["mlb_schedule_2026"],
    },
    {
        "id": "mlb_2029_postseason",
        "label": "MLB 2029 Postseason (potential games, estimated)",
        "start": "2029-10-02", "end": "2029-11-04",
        "category": "MLB", "priority": "high",
        "status": "estimated-window",
        "note": "ESTIMATE ONLY - postseason dates not released. Estimated window.",
        "source_ids": ["mlb_postseason_format"],
    },
    # NFL 2026 season (2026-27) - official key dates exist
    {
        "id": "nfl_2026_regular",
        "label": "NFL 2026 Regular Season (includes 49ers + Westwood One national windows)",
        "start": "2026-09-09", "end": "2027-01-10",
        "category": "NFL", "priority": "high",
        "status": "verified-window",
        "note": "Kickoff Weekend Sep 9-10,13-14, 2026; Week 18 Jan 9-10, 2027 per NFL important dates. 49ers games and Westwood One national broadcasts fall within/around this window.",
        "source_ids": ["nfl_important_dates_2026_27", "westwood_one_nfl"],
    },
    {
        "id": "nfl_2026_postseason",
        "label": "NFL 2026 Postseason / Super Bowl LXI",
        "start": "2027-01-16", "end": "2027-02-14",
        "category": "NFL", "priority": "high",
        "status": "verified-window",
        "note": "Wild Card Jan 16-18 2027, Divisional Jan 23-24, Conference Championships Jan 31, Super Bowl LXI Feb 14 2027 at SoFi Stadium. Westwood One typically carries postseason/national games; verify specific broadcasts.",
        "source_ids": ["nfl_important_dates_2026_27", "westwood_one_nfl"],
    },
    # NFL 2027 season (2027-28) - no full schedule, but Super Bowl LXII date announced
    {
        "id": "nfl_2027_regular",
        "label": "NFL 2027 Regular Season (49ers + Westwood One) - ESTIMATED",
        "start": "2027-09-09", "end": "2028-01-09",
        "category": "NFL", "priority": "high",
        "status": "estimated-window",
        "note": "ESTIMATE ONLY - official 2027 NFL schedule not released. Start estimated as Thursday after Labor Day 2027 (Labor Day Sep 6, 2027 => Thu Sep 9). End estimated as ~Week 18 early Jan 2028. Verify on NFL.com when released.",
        "source_ids": ["nfl_operations", "nfl_schedule"],
    },
    {
        "id": "nfl_2027_postseason",
        "label": "NFL 2027 Postseason / Super Bowl LXII - partially confirmed",
        "start": "2028-01-15", "end": "2028-02-13",
        "category": "NFL", "priority": "high",
        "status": "estimated-window",
        "note": "Super Bowl LXII confirmed Feb 13, 2028 at Mercedes-Benz Stadium, Atlanta (NFL announcement reported). Other postseason dates estimated from typical pattern. Verify on NFL.com.",
        "source_ids": ["super_bowl_lxii_date", "nfl_schedule"],
    },
    # NFL 2028 season (2028-29)
    {
        "id": "nfl_2028_regular",
        "label": "NFL 2028 Regular Season (49ers + Westwood One) - ESTIMATED",
        "start": "2028-09-07", "end": "2029-01-07",
        "category": "NFL", "priority": "high",
        "status": "estimated-window",
        "note": "ESTIMATE ONLY - official 2028 NFL schedule not released. Start estimated as Thursday after Labor Day 2028 (Labor Day Sep 4, 2028 => Thu Sep 7). End estimated. Verify on NFL.com when released.",
        "source_ids": ["nfl_operations", "nfl_schedule"],
    },
    {
        "id": "nfl_2028_postseason",
        "label": "NFL 2028 Postseason - ESTIMATED",
        "start": "2029-01-13", "end": "2029-02-11",
        "category": "NFL", "priority": "high",
        "status": "estimated-window",
        "note": "ESTIMATE ONLY - postseason dates not released. Estimated from typical pattern (Super Bowl usually mid-Feb). Verify on NFL.com.",
        "source_ids": ["nfl_schedule"],
    },
    # NFL 2029 season (partial, for vacation planning into 2029)
    {
        "id": "nfl_2029_regular",
        "label": "NFL 2029 Regular Season (49ers + Westwood One) - ESTIMATED",
        "start": "2029-09-06", "end": "2030-01-06",
        "category": "NFL", "priority": "high",
        "status": "estimated-window",
        "note": "ESTIMATE ONLY - official 2029 NFL schedule not released. Start estimated as Thursday after Labor Day 2029 (Labor Day Sep 3, 2029 => Thu Sep 6). End estimated. Verify on NFL.com when released.",
        "source_ids": ["nfl_operations", "nfl_schedule"],
    },
    # NCAAF Stanford/Cal - seasons typically late Aug through late Nov, bowls/postseason possible
    {
        "id": "ncaaf_2026",
        "label": "NCAAF 2026 Season (Stanford & California) - verified games listed",
        "start": "2026-08-29", "end": "2026-11-28",
        "category": "NCAAF", "priority": "high",
        "status": "verified-window",
        "note": "Regular season window based on official 2026 schedules for Stanford and Cal. Bowl/postseason not included unless scheduled; verify.",
        "source_ids": ["stanford_2026", "cal_2026"],
    },
    {
        "id": "ncaaf_2027",
        "label": "NCAAF 2027 Season (Stanford & California) - ESTIMATED",
        "start": "2027-08-28", "end": "2027-11-27",
        "category": "NCAAF", "priority": "high",
        "status": "estimated-window",
        "note": "ESTIMATE ONLY - 2027 NCAAF schedules not released. Typical season: last Sat of Aug through Sat after Thanksgiving. Verify on gostanford.com and calbears.com when released.",
        "source_ids": ["stanford_2026", "cal_2026"],
    },
    {
        "id": "ncaaf_2028",
        "label": "NCAAF 2028 Season (Stanford & California) - ESTIMATED",
        "start": "2028-08-26", "end": "2028-11-25",
        "category": "NCAAF", "priority": "high",
        "status": "estimated-window",
        "note": "ESTIMATE ONLY - 2028 NCAAF schedules not released. Typical season window estimated. Verify on official athletic sites when released.",
        "source_ids": ["stanford_2026", "cal_2026"],
    },
    {
        "id": "ncaaf_2029",
        "label": "NCAAF 2029 Season (Stanford & California) - ESTIMATED",
        "start": "2029-08-25", "end": "2029-11-24",
        "category": "NCAAF", "priority": "high",
        "status": "estimated-window",
        "note": "ESTIMATE ONLY - 2029 NCAAF schedules not released. Typical season window estimated. Verify on official athletic sites when released.",
        "source_ids": ["stanford_2026", "cal_2026"],
    },
]

# --- Vacation window computation ---
def parse_date(s):
    return datetime.date.fromisoformat(s)

def daterange(start, end):
    d = start
    while d <= end:
        yield d
        d += datetime.timedelta(days=1)

def compute_day_busy(days, events, season_windows):
    # For each day, determine if busy by any tracked category.
    # We mark 'busy-confirmed' if specific verified event, 'busy-estimated' if in estimated season window,
    # 'busy-season' if in verified season window but no specific game-level data.
    day_map = {day_iso(d): {"date": day_iso(d), "busy": False, "reasons": [], "events": [], "status": "free"} for d in days}
    for e in events:
        d = e["date"]
        if d in day_map:
            day_map[d]["events"].append(e)
            day_map[d]["busy"] = True
            day_map[d]["reasons"].append({
                "label": e["title"],
                "category": e["category"],
                "priority": e["priority"],
                "status": e["status"],
                "source_ids": e["source_ids"],
            })
    # Season windows: mark days covered as busy-season/estimated unless already has specific events
    for w in season_windows:
        ws, we = parse_date(w["start"]), parse_date(w["end"])
        for d in daterange(ws, we):
            k = day_iso(d)
            if k not in day_map: 
                continue
            entry = day_map[k]
            # add season reason (dedupe by window id)
            reason = {
                "label": w["label"],
                "category": w["category"],
                "priority": w["priority"],
                "status": w["status"],
                "window_id": w["id"],
                "source_ids": w["source_ids"],
                "note": w["note"],
            }
            # avoid duplicate window reasons
            if not any(r.get("window_id") == w["id"] for r in entry["reasons"]):
                entry["reasons"].append(reason)
            entry["busy"] = True
    # finalize status
    for k, entry in day_map.items():
        if not entry["busy"]:
            entry["status"] = "free"
        else:
            statuses = [r.get("status","") for r in entry["reasons"]]
            if any(s.startswith("verified") for s in statuses):
                # if any verified-window/reason, but also may be estimated; mark mixed carefully
                if any("estimated" in s for s in statuses):
                    entry["status"] = "busy-mixed"
                else:
                    entry["status"] = "busy-verified"
            else:
                entry["status"] = "busy-estimated"
    return day_map

def find_free_windows(day_map, start, end, min_days=7):
    # find contiguous free days
    windows = []
    cur_start = None
    cur_len = 0
    for d in daterange(start, end):
        k = day_iso(d)
        entry = day_map.get(k)
        is_free = entry and entry["status"] == "free"
        if is_free:
            if cur_start is None:
                cur_start = d
                cur_len = 1
            else:
                cur_len += 1
        else:
            if cur_start is not None and cur_len >= min_days:
                windows.append({"start": day_iso(cur_start), "end": day_iso(cur_start + datetime.timedelta(days=cur_len-1)), "days": cur_len})
            cur_start = None
            cur_len = 0
    if cur_start is not None and cur_len >= min_days:
        windows.append({"start": day_iso(cur_start), "end": day_iso(cur_start + datetime.timedelta(days=cur_len-1)), "days": cur_len})
    windows.sort(key=lambda w: (-w["days"], w["start"]))
    return windows

def main():
    events = build_events()
    # Day range: cover 2026-11-25 through 2029-12-31 for vacation analysis; calendar can show this range
    start = datetime.date(2026, 11, 25)
    end = datetime.date(2029, 12, 31)
    days = list(daterange(start, end))
    day_map = compute_day_busy(days, events, SEASON_WINDOWS)

    vacation = {
        "2027": find_free_windows(day_map, datetime.date(2027,1,1), datetime.date(2027,12,31), min_days=7),
        "2028": find_free_windows(day_map, datetime.date(2028,1,1), datetime.date(2028,12,31), min_days=7),
        "2029": find_free_windows(day_map, datetime.date(2029,1,1), datetime.date(2029,12,31), min_days=7),
    }

    payload = {
        "meta": {
            "generated_at": "2026-11-25",
            "timezone_display": "America/Los_Angeles (PST/PDT)",
            "definition_of_free": "A minute is free when none of these are on air: MLB (Giants and A’s flagged high priority; all 30 MLB clubs shown), NFL San Francisco 49ers (preseason/regular/postseason, high priority), Stanford NCAAF and California NCAAF (high priority), Westwood One Sports national NFL radio broadcasts.",
            "coverage_note": "Day-by-day status is computed from verified events where available and season windows otherwise. 2027-2029 game-level schedules are largely unreleased; season windows are marked ESTIMATED. Verify against official sources before booking travel.",
        },
        "sources": SOURCES,
        "durations": DURATIONS,
        "season_windows": SEASON_WINDOWS,
        "events": events,
        "days": day_map,
        "vacation_windows": vacation,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    js = "window.SCHEDULE_DATA = " + json.dumps(payload, indent=2) + ";\n"
    OUT.write_text(js, encoding="utf-8")
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")
    # summary
    for yr in ["2027","2028","2029"]:
        wins = vacation[yr][:5]
        print(yr, "top windows:")
        for w in wins:
            print(" ", w)

if __name__ == "__main__":
    main()
