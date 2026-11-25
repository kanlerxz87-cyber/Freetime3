export const zone='America/Los_Angeles';
const local=new Intl.DateTimeFormat('en-CA',{timeZone:zone,year:'numeric',month:'2-digit',day:'2-digit',hour:'2-digit',minute:'2-digit',hourCycle:'h23'});
export function parts(value){const p=Object.fromEntries(local.formatToParts(new Date(value)).map(x=>[x.type,x.value]));return {date:`${p.year}-${p.month}-${p.day}`,time:`${p.hour}:${p.minute}`};}
export const move=(d,n)=>new Date(Date.parse(d+'T12:00:00Z')+n*864e5).toISOString().slice(0,10);
export const minute=t=>t.split(':').reduce((h,m)=>60*Number(h)+Number(m));
export function midnight(d){const utc=Date.parse(d+'T00:00:00Z');return [7,8].map(h=>utc+h*3600000).find(v=>parts(v).date===d&&parts(v).time==='00:00');}
export function instant(d,t){const utc=Date.parse(`${d}T${t}:00Z`);return [7,8].map(h=>utc+h*3600000).find(v=>parts(v).date===d&&parts(v).time===t);}
export function intervals(day,rows){const start=midnight(day),end=midnight(move(day,1));const blocks=rows.flatMap(r=>{const t=r.instant??(r.time?instant(r.date,r.time):undefined);if(t==null||!r.minutes)return [];const a=Math.max(start,t),b=Math.min(end,t+r.minutes*60000);return a<b?[[a,b]]:[];}).sort((a,b)=>a[0]-b[0]);const merged=[];for(const [a,b] of blocks){const last=merged.at(-1);if(last&&a<=last[1])last[1]=Math.max(last[1],b);else merged.push([a,b]);}const gaps=[];let cursor=start;for(const [a,b] of merged){if(cursor<a)gaps.push([cursor,a]);cursor=b;}if(cursor<end)gaps.push([cursor,end]);return {start,end,merged,gaps};}
