export const sources={mlb:'https://www.mlb.com/news/mlb-2027-schedule-released',spring:'https://www.mlb.com/press-release/press-release-brewers-announce-2027-spring-training-schedule',nfl:'https://media.nfl.com/football-information/2026/news/2026-nfl-schedule-announced',dates:'https://www.nfl.com/news/2026-27-national-football-league-important-dates',ww:'https://www.westwoodonesports.com/nfl-schedule/',stan:'https://gostanford.com/news/2026/09/16/acc-announces-2027-conference-opponents',cal:'https://calbears.com/news/2026/9/16/california-football-announces-2027-conference-opponents',war:'https://www.nba.com/warriors/news/warriors-announce-2026-27-television-radio-broadcast-schedules-20260824',duration:'https://www.mlb.com/news/mlb-average-game-time-under-three-hours-third-straight-year'};
export const radio=[['Giants','KNBR 680 AM / 104.5 FM; Spanish: KSFN 1510 AM','Team network; verify individual listings','https://www.mlb.com/giants/schedule/tv'],['Athletics','KNEW 960 AM','Team lists Bay Area affiliate; check specific games','https://www.mlb.com/athletics/schedule/affiliates'],['49ers','KSAN 107.7 FM / KNBR 104.5 FM / 680 AM','Listed on team schedule','https://www.49ers.com/schedule/2026/'],['Stanford football','KTCT 1050 AM','2026 team announcement','https://gostanford.com/news/2026/07/30/2026-football-radio-broadcast-team-announced'],['Cal football','KNBR 680 AM / 104.5 FM','Listed for the 2026 Big Game; check game-by-game','https://calbears.com/sports/football/schedule/2026'],['Westwood One NFL','KNBR 680 AM','Affiliate listing ≠ individual game clearance','https://www.westwoodonesports.com/station-finder-source-nfl/'],['Warriors','KGMZ 95.7 FM','2026–27 preseason and regular season; daily rows not imported',sources.war]];
export const broadcasts=`2026-11-25|16:30|548511|Green Bay Packers at Los Angeles Rams
2026-11-26|09:30|548512|Chicago Bears at Detroit Lions
2026-11-26|13:15|548513|Philadelphia Eagles at Dallas Cowboys
2026-11-26|17:00|548514|Kansas City Chiefs at Buffalo Bills
2026-11-27|11:30|548515|Denver Broncos at Pittsburgh Steelers
2026-11-29|16:30|548502|Las Vegas Raiders at Cleveland Browns
2026-11-30|16:00|548544|Carolina Panthers at Tampa Bay Buccaneers
2026-12-03|16:30|548566|Kansas City Chiefs at Los Angeles Rams
2026-12-06|16:30|548503|Houston Texans at Pittsburgh Steelers
2026-12-07|16:00|548545|Dallas Cowboys at Seattle Seahawks
2026-12-10|16:30|548567|Minnesota Vikings at New England Patriots
2026-12-13|16:30|548505|Buffalo Bills at Green Bay Packers
2026-12-14|16:00|548546|Pittsburgh Steelers at Jacksonville Jaguars
2026-12-17|16:30|548568|San Francisco 49ers at Los Angeles Chargers
2026-12-19|13:30|548517|Seattle Seahawks at Philadelphia Eagles
2026-12-19|17:00|548518|Chicago Bears at Buffalo Bills
2026-12-20|16:30|548506|Detroit Lions at Minnesota Vikings
2026-12-21|16:00|548548|New England Patriots at Kansas City Chiefs
2026-12-24|16:30|548569|Baltimore Ravens at Cincinnati Bengals
2026-12-25|09:30|548528|Green Bay Packers at Chicago Bears
2026-12-25|13:15|548531|Buffalo Bills at Denver Broncos
2026-12-25|17:00|548534|Los Angeles Rams at Seattle Seahawks
2026-12-26|13:00|548519|Saturday doubleheader — teams TBD
2026-12-26|17:00|548520|Saturday doubleheader — teams TBD
2026-12-27|16:30|548507|Jacksonville Jaguars at Dallas Cowboys
2026-12-28|16:00|548550|New York Giants at Detroit Lions
2026-12-31|16:30|548570|Baltimore Ravens at Cincinnati Bengals
2027-01-02|13:00|548521|Saturday doubleheader — teams TBD
2027-01-02|17:00|548522|Saturday doubleheader — teams TBD
2027-01-03|16:30|548509|Philadelphia Eagles at San Francisco 49ers
2027-01-04|16:00|548552|Houston Texans at Green Bay Packers
2027-01-09|09:30|548523|Saturday tripleheader — teams TBD
2027-01-09|13:15|548524|Saturday tripleheader — teams TBD
2027-01-09|17:00|548526|Saturday tripleheader — teams TBD
2027-01-10|16:30|548510|Sunday Night Football — teams TBD`.split('\n').map(line=>{const [date,time,id,name]=line.split('|');return {date,time,name,cat:'Westwood One',high:true,minutes:210,source:`https://www.westwoodonesports.com/events/${id}`,radio:'National listing; local carriage unverified'}});
export const fixed=[...broadcasts,{date:'2026-11-28',time:'16:30',name:'Pittsburgh at California',cat:'College football',high:true,minutes:210,source:'https://calbears.com/sports/football/schedule/2026'},...['2027-01-31','2027-02-14'].map((date,i)=>({date,name:i?'Super Bowl LXI':'AFC and NFC Championship Games',cat:'NFL',source:sources.dates})),...['2027-08-28','2027-09-04','2027-09-11'].map((date,i)=>({date,name:['Sacramento State at California','California at UCLA','Old Dominion at California'][i],cat:'College football',high:true,source:sources.cal}))];
const sf='San Francisco 49ers';
const sfSource='https://www.49ers.com/schedule/2026/';
const sfRadio='KSAN 107.7 FM / KNBR 104.5 FM / 680 AM';
const sfGames=[['08-13','','Tennessee Titans',false],['08-20','','Los Angeles Chargers',true],['08-27','','Las Vegas Raiders',true],['09-10','','Los Angeles Rams',true],['09-20','','Miami Dolphins',false],['09-27','','Arizona Cardinals',false],['10-04','','Denver Broncos',false],['10-11','','Seattle Seahawks',true],['10-19','','Washington Commanders',false],['10-25','','Atlanta Falcons',true],['11-08','','Las Vegas Raiders',false],['11-15','','Dallas Cowboys',true],['11-22','','Minnesota Vikings',false],['11-29','13:25','Seattle Seahawks',false],['12-06','10:00','New York Giants',true],['12-13','13:25','Los Angeles Rams',false],['12-17','17:15','Los Angeles Chargers',true],['12-27','13:25','Kansas City Chiefs',true],['01-03','17:20','Philadelphia Eagles',false]];
fixed.push(...sfGames.map(([day,time,team,away],i)=>({date:`${day==='01-03'?2027:2026}-${day}`,time,name:away?`${sf} at ${team}`:`${team} at ${sf}`,cat:'NFL',phase:i<3?'Preseason':'Regular season',radio:time?sfRadio:'',high:true,minutes:210,source:sfSource})));
