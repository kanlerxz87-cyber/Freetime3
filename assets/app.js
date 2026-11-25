const OFFICIAL = {
  mlb2026: 'https://www.mlb.com/press-release/press-release-mlb-announces-2026-regular-season-schedule',
  mlb2027: 'https://www.mlb.com/press-release/rays-announce-2027-regular-season-schedule',
  mlb2027Spring: 'https://www.mlb.com/press-release/press-release-mlb-announces-2027-spring-training-schedule',
  mlbApi: 'https://statsapi.mlb.com/api/v1/schedule',
  mlbFuture: 'https://www.mlb.com/schedule',
  allStar: 'https://www.mlb.com/all-star/future-locations',
  nflDates: 'https://www.nfl.com/news/2026-27-national-football-league-important-dates',
  nfl2026: 'https://media.nfl.com/content/dam/communications/football-communications/2026/news/05%2014%2026%20-%202026%20NFL%20Schedule%20-%20By%20Week.pdf',
  nflFuture: 'https://www.nfl.com/schedules/',
  stanford: 'https://gostanford.com/sports/football/schedule',
  cal: 'https://calbears.com/sports/football/schedule',
  cal2027: 'https://calbears.com/news/2026/9/16/california-football-announces-2027-conference-opponents',
  niners: 'https://www.49ers.com/schedule/',
  westwood: 'https://www.westwoodonesports.com/nfl-schedule/',
  knbr: 'https://www.thesportsleader.com/shows'
};

const teams = [
  ['Arizona Diamondbacks','dbacks','NL West'],['Atlanta Braves','braves','NL East'],['Athletics','athletics','AL West','high'],['Baltimore Orioles','orioles','AL East'],['Boston Red Sox','redsox','AL East'],['Chicago Cubs','cubs','NL Central'],['Chicago White Sox','whitesox','AL Central'],['Cincinnati Reds','reds','NL Central'],['Cleveland Guardians','guardians','AL Central'],['Colorado Rockies','rockies','NL West'],['Detroit Tigers','tigers','AL Central'],['Houston Astros','astros','AL West'],['Kansas City Royals','royals','AL Central'],['Los Angeles Angels','angels','AL West'],['Los Angeles Dodgers','dodgers','NL West'],['Miami Marlins','marlins','NL East'],['Milwaukee Brewers','brewers','NL Central'],['Minnesota Twins','twins','AL Central'],['New York Mets','mets','NL East'],['New York Yankees','yankees','AL East'],['Philadelphia Phillies','phillies','NL East'],['Pittsburgh Pirates','pirates','NL Central'],['San Diego Padres','padres','NL West'],['San Francisco Giants','giants','NL West','high'],['Seattle Mariners','mariners','AL West'],['St. Louis Cardinals','cardinals','NL Central'],['Tampa Bay Rays','rays','AL East'],['Texas Rangers','rangers','AL West'],['Toronto Blue Jays','bluejays','AL East'],['Washington Nationals','nationals','NL East']
];

const cell = (label, href, detail = '') => `<a href="${href}" target="_blank" rel="noreferrer">${label}${detail ? `<small class="cell-detail">${detail}</small>` : ''}</a>`;
const TBD = (href, detail = 'No complete schedule verified') => `<span class="table-tag">NOT VERIFIED</span> ${cell('Official source', href, detail)}`;
const rows = [
  ['MLB · all 30 clubs', cell('2026 schedule released', OFFICIAL.mlb2026, 'Official MLB release') , cell('2027 regular season published · spring begins Feb 19', OFFICIAL.mlb2027, 'All 30 club schedules released; game times subject to change') + '<br>' + cell('Spring Training source', OFFICIAL.mlb2027Spring, 'Official MLB release') , TBD(OFFICIAL.mlbFuture, '2028 schedule not verified') , TBD(OFFICIAL.mlbFuture, '2029 schedule not verified')],
  ['NFL · all games', cell('2026 schedule PDF', OFFICIAL.nfl2026, 'Official by-week schedule') , `<span class="table-tag">PARTIAL</span> ${cell('Postseason dates confirmed; regular-season schedule not verified', OFFICIAL.nflDates, '2027 Wild Card through Super Bowl LXI dates')}` , TBD(OFFICIAL.nflFuture, '2028 season schedule not verified') , TBD(OFFICIAL.nflFuture, '2029 season schedule not verified')],
  ['San Francisco 49ers', cell('Official team schedule', OFFICIAL.niners, '2026 season schedule page') , TBD(OFFICIAL.niners, '2027 schedule not verified') , TBD(OFFICIAL.niners, '2028 schedule not verified') , TBD(OFFICIAL.niners, '2029 schedule not verified')],
  ['Stanford football', cell('Official schedule', OFFICIAL.stanford, '2026 schedule page') , TBD(OFFICIAL.stanford, 'No complete 2027 date/time slate verified') , TBD(OFFICIAL.stanford, '2028 schedule not verified') , TBD(OFFICIAL.stanford, '2029 schedule not verified')],
  ['California football', cell('Official schedule', OFFICIAL.cal, '2026 schedule page') , `<span class="table-tag">PARTIAL</span> ${cell('2027 conference opponents announced', OFFICIAL.cal2027, 'Does not establish full dates/times')}` , TBD(OFFICIAL.cal, '2028 schedule not verified') , TBD(OFFICIAL.cal, '2029 schedule not verified')],
  ['Westwood One · NFL radio', cell('Current NFL broadcast list', OFFICIAL.westwood, 'Event listings change through the season') , TBD(OFFICIAL.westwood, '2027 carriage and local affiliates not verified') , TBD(OFFICIAL.westwood, '2028 broadcast schedule not verified') , TBD(OFFICIAL.westwood, '2029 broadcast schedule not verified')],
  ['MLB All-Star / special games', cell('2026 MLB schedule source', OFFICIAL.mlb2026, 'Check official league schedule') , cell('2027 MLB schedule source', OFFICIAL.mlb2027, 'Special-event times may be updated') , `<span class="table-tag">PARTIAL</span> ${cell('All-Star host announced; event day unverified', OFFICIAL.allStar, 'San Francisco / Oracle Park in July 2028')}` , TBD(OFFICIAL.mlbFuture, '2029 dates not verified')]
];

function renderSchedules(){
  const body=document.querySelector('#schedule-table');
  body.innerHTML=rows.map(row=>`<tr>${row.map((v,i)=>i===0?`<td>${v}</td>`:`<td>${v}</td>`).join('')}</tr>`).join('');
}
function renderTeams(){
  const grid=document.querySelector('#team-grid');
  const search=document.querySelector('#team-search');
  const draw=()=>{
    const q=search.value.trim().toLowerCase();
    const filtered=teams.filter(t=>t[0].toLowerCase().includes(q)||t[2].toLowerCase().includes(q));
    grid.innerHTML=filtered.map(([name,slug,division,priority])=>`<a class="team-card ${priority?'priority':''}" href="https://www.mlb.com/${slug}/schedule/2027" target="_blank" rel="noreferrer" aria-label="${name} official 2027 schedule${priority?', high priority':''}"><span><strong>${name}${priority?'<span class="high-tag">HIGH</span>':''}</strong><small>${division} · 2027 official schedule</small></span><span class="arrow">↗</span></a>`).join('') || '<p class="muted">No matching club.</p>';
  };
  search.addEventListener('input',draw);draw();
}

const dateInput=document.querySelector('#selected-date');
const monthLabel=document.querySelector('#month-label');
const monthGrid=document.querySelector('#month-grid');
let selected=new Date();
selected.setHours(12,0,0,0);
if(selected.getFullYear()<2026||selected.getFullYear()>2029) selected=new Date(2026,0,1,12);
let displayed=new Date(selected.getFullYear(),selected.getMonth(),1,12);
const monthFmt=new Intl.DateTimeFormat('en-US',{month:'long',year:'numeric',timeZone:'UTC'});
const dateFmt=new Intl.DateTimeFormat('en-US',{weekday:'long',month:'long',day:'numeric',year:'numeric',timeZone:'UTC'});
const iso=(d)=>`${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,'0')}-${String(d.getDate()).padStart(2,'0')}`;
function clampDate(d){ if(d.getFullYear()<2026)return new Date(2026,0,1,12); if(d.getFullYear()>2029)return new Date(2029,11,31,12); return d; }
const monthCache=new Map();
const gameTypes='S,R,F,D,L,W,C,P,A,I,E';
const monthKey=(y,m)=>`${y}-${String(m+1).padStart(2,'0')}`;
const dateSource=(date)=>`${OFFICIAL.mlbApi}?sportId=1&date=${date}&gameTypes=${encodeURIComponent(gameTypes)}`;
const supportedMlbYear=(year)=>year===2026||year===2027;
const pacificTime=(value)=>{
  if(!value)return 'Time TBD';
  const dt=new Date(value);
  if(Number.isNaN(dt.getTime()))return 'Time TBD';
  return new Intl.DateTimeFormat('en-US',{hour:'numeric',minute:'2-digit',timeZone:'America/Los_Angeles',timeZoneName:'short'}).format(dt);
};
function renderCalendar(){
  monthLabel.textContent=monthFmt.format(new Date(Date.UTC(displayed.getFullYear(),displayed.getMonth(),1,12)));
  const offset=new Date(displayed.getFullYear(),displayed.getMonth(),1,12).getDay();
  const days=new Date(displayed.getFullYear(),displayed.getMonth()+1,0,12).getDate();
  const prevDays=new Date(displayed.getFullYear(),displayed.getMonth(),0,12).getDate();
  const key=monthKey(displayed.getFullYear(),displayed.getMonth());
  const cached=monthCache.get(key);
  const games=cached?.games||[];
  const counts={};
  games.forEach(game=>{const day=game.officialDate;if(day)counts[day]=(counts[day]||0)+1;});
  let html='';
  for(let i=0;i<42;i++){
    let d,outside=false;
    if(i<offset){d=new Date(displayed.getFullYear(),displayed.getMonth()-1,prevDays-offset+i+1,12);outside=true;}
    else if(i>=offset+days){d=new Date(displayed.getFullYear(),displayed.getMonth()+1,i-offset-days+1,12);outside=true;}
    else d=new Date(displayed.getFullYear(),displayed.getMonth(),i-offset+1,12);
    const disabled=d.getFullYear()<2026||d.getFullYear()>2029;
    const active=iso(d)===iso(selected);
    const date=iso(d),hasGames=(counts[date]||0)>0;
    const count=counts[date]||0;
    const known=supportedMlbYear(d.getFullYear())&&cached?.status==='ok';
    const label=`${dateFmt.format(new Date(Date.UTC(d.getFullYear(),d.getMonth(),d.getDate(),12)))} — ${known?`${count} MLB games listed; other schedule coverage unverified`:'coverage unverified'}`;
    html+=`<button class="calendar-day${outside?' outside':''}${active?' selected':''}${hasGames?' has-event':''}" role="gridcell" aria-selected="${active}" ${disabled?'disabled':''} data-date="${date}" aria-label="${label}">${d.getDate()}</button>`;
  }
  monthGrid.innerHTML=html;
  monthGrid.querySelectorAll('button[data-date]').forEach(button=>button.addEventListener('click',()=>{const [y,m,d]=button.dataset.date.split('-').map(Number);selected=new Date(y,m-1,d,12);displayed=new Date(y,m-1,1,12);paint();}));
}
async function loadMonthEvents(year,month){
  const key=monthKey(year,month);
  if(!supportedMlbYear(year)){renderMlbResults();return;}
  if(monthCache.has(key)){renderCalendar();renderMlbResults();return;}
  monthCache.set(key,{status:'loading',games:[]});
  const start=`${year}-${String(month+1).padStart(2,'0')}-01`;
  const endDay=new Date(year,month+1,0,12).getDate();
  const end=`${year}-${String(month+1).padStart(2,'0')}-${String(endDay).padStart(2,'0')}`;
  const url=`${OFFICIAL.mlbApi}?sportId=1&startDate=${start}&endDate=${end}&gameTypes=${encodeURIComponent(gameTypes)}`;
  try{
    const response=await fetch(url,{headers:{Accept:'application/json'}});
    if(!response.ok)throw new Error(`HTTP ${response.status}`);
    const payload=await response.json();
    const games=(payload.dates||[]).flatMap(day=>day.games||[]).map(game=>({...game,officialDate:game.officialDate||game.gameDate?.slice(0,10)}));
    monthCache.set(key,{status:'ok',games,source:url});
  }catch(error){monthCache.set(key,{status:'error',games:[],source:url,error:String(error)});}
  if(monthKey(displayed.getFullYear(),displayed.getMonth())===key){renderCalendar();renderMlbResults();}
}
function renderMlbResults(){
  const results=document.querySelector('#event-results');
  if(!results)return;
  const year=selected.getFullYear(),month=selected.getMonth(),date=iso(selected);
  const dateText=dateFmt.format(new Date(Date.UTC(year,month,selected.getDate(),12)));
  document.querySelector('#detail-date').textContent=dateText;
  const chip=document.querySelector('#day-chip');
  const title=document.querySelector('#day-title');
  const description=document.querySelector('#day-description');
  const cache=monthCache.get(monthKey(year,month));
  if(!supportedMlbYear(year)){
    chip.textContent='UNVERIFIED';title.textContent='Schedule coverage incomplete';
    description.textContent=`No complete official event ledger is available here for ${year}. This day cannot be called free.`;
    results.innerHTML=`<span class="empty-icon">◷</span><strong>${year} MLB game list not verified in this planner</strong><p>The official MLB schedule directory is available below. No dates or times are inferred for this season.</p>`;
    return;
  }
  if(!cache||cache.status==='loading'){
    chip.textContent='LOADING MLB';title.textContent='Checking official MLB schedule';
    description.textContent='The selected date is checked against the official MLB StatsAPI. All other sports and local radio remain unverified.';
    results.innerHTML='<span class="empty-icon">◷</span><strong>Loading official MLB game list…</strong><p>No availability conclusion is made while the source is loading.</p>';
    return;
  }
  if(cache.status==='error'){
    chip.textContent='UNVERIFIED';title.textContent='Official MLB feed could not be loaded';
    description.textContent='The selected date remains unknown. Use the linked official MLB schedule to check it manually.';
    results.innerHTML=`<span class="empty-icon">!</span><strong>MLB schedule data unavailable in this browser</strong><p>This can happen if the official feed is unreachable or blocks cross-origin requests. No “free” status is shown.</p><a class="text-link" target="_blank" rel="noreferrer" href="${dateSource(date)}">Open official MLB feed ↗</a>`;
    return;
  }
  const games=cache.games.filter(game=>game.officialDate===date).sort((a,b)=>(a.gameDate||'').localeCompare(b.gameDate||''));
  chip.textContent='PARTIAL · MLB ONLY';
  title.textContent=games.length?`${games.length} MLB ${games.length===1?'game':'games'} listed · full-day status unknown`:'No MLB game listed · full-day status unknown';
  description.textContent='This verifies only the MLB game list for this date. NFL, college football, radio carriage, and end times are not covered; the day is not labeled free.';
  const items=games.length?games.map(game=>{
    const away=game.teams?.away?.team?.name||'Away TBD',home=game.teams?.home?.team?.name||'Home TBD';
    const time=game.status?.startTimeTBD?'Time TBD':pacificTime(game.gameDate);
    const venue=game.venue?.name||'Venue not listed';
    const type=game.seriesDescription||({S:'Spring Training',E:'Exhibition',R:'Regular season',A:'All-Star',F:'Wild Card',D:'Division Series',L:'League Championship Series',W:'World Series',C:'Championship',P:'Postseason',I:'Intrasquad'}[game.gameType]||`Game type ${game.gameType||'unknown'}`);
    const gameLink=`https://www.mlb.com/gameday/${game.gamePk}`;
    return `<li><span class="event-time">${time}</span><span class="event-info"><strong>${away} at ${home}</strong><small>${type} · ${venue}</small></span><a href="${gameLink}" target="_blank" rel="noreferrer" aria-label="Official MLB game details">↗</a></li>`;
  }).join(''):'<div class="no-mlb">The official feed lists no MLB games for this selected date.</div>';
  results.innerHTML=`<div class="event-summary"><strong>${games.length?`${games.length} scheduled event${games.length===1?'':'s'}`:'0 MLB games in feed'}</strong><span>Times shown in San Francisco local time</span></div><ul class="event-list">${items}</ul><a class="text-link event-source" href="${dateSource(date)}" target="_blank" rel="noreferrer">Official MLB schedule feed for ${date} ↗</a>`;
}
function paint(){
  selected=clampDate(selected);
  displayed=new Date(displayed.getFullYear(),displayed.getMonth(),1,12);
  dateInput.value=iso(selected);
  renderCalendar();
  renderMlbResults();
  loadMonthEvents(displayed.getFullYear(),displayed.getMonth());
}
dateInput.addEventListener('change',()=>{if(!dateInput.value)return;const [y,m,d]=dateInput.value.split('-').map(Number);selected=new Date(y,m-1,d,12);displayed=new Date(y,m-1,1,12);paint();});
document.querySelector('#previous-day').addEventListener('click',()=>{selected.setDate(selected.getDate()-1);selected=clampDate(selected);displayed=new Date(selected.getFullYear(),selected.getMonth(),1,12);paint();});
document.querySelector('#next-day').addEventListener('click',()=>{selected.setDate(selected.getDate()+1);selected=clampDate(selected);displayed=new Date(selected.getFullYear(),selected.getMonth(),1,12);paint();});
document.querySelector('#previous-month').addEventListener('click',()=>{const d=new Date(displayed.getFullYear(),displayed.getMonth()-1,1,12);if(d.getFullYear()>=2026){displayed=d;paint();}});
document.querySelector('#next-month').addEventListener('click',()=>{const d=new Date(displayed.getFullYear(),displayed.getMonth()+1,1,12);if(d.getFullYear()<=2029){displayed=d;paint();}});

renderSchedules();renderTeams();paint();
const menu=document.querySelector('.menu-toggle');
menu.addEventListener('click',()=>{const side=document.querySelector('.sidebar');const open=side.classList.toggle('open');menu.setAttribute('aria-expanded',String(open));});
document.querySelectorAll('.nav-link').forEach(link=>link.addEventListener('click',()=>{document.querySelector('.sidebar').classList.remove('open');menu.setAttribute('aria-expanded','false');document.querySelectorAll('.nav-link').forEach(item=>item.classList.remove('active'));link.classList.add('active');}));
