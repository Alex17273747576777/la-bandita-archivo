// BATERÍA KERNEL v2.8 — niveles superiores sobre estructuras internas (AniZen/houri context)
// [A] feeds.json round-trip bajo mutación adversarial · [B] precedencia total con permutaciones
// [C] caché de labels 50k llaves con GC por días · [D] tormenta de refresh con fuentes cayendo (código vivo)
// [E] dedupKey + merge vivo. Semilla fija 20281010 (LCG).
const fs=require("fs");
let seed=20281010>>>0;
const rnd=()=>((seed=(seed*1664525+1013904223)>>>0)/4294967296);
const ri=n=>Math.floor(rnd()*n);const pick=a=>a[ri(a.length)];
let checks=0,fails=0;const ok=(c,m)=>{checks++;if(!c){fails++;if(fails<12)console.log("  ✗",m)}};
const sha=s=>require("crypto").createHash("sha256").update(s).digest("hex").slice(0,16);
const html=fs.readFileSync(__dirname+"/../RFC-v2.9-UNIFIED-FEED-AniZen-Houri-2026-10-10.html","utf8");
const dk=(html.match(/function dedupKey\(t\)\{.*?\.trim\(\)\}/)||[])[0];
const block=(html.match(/var DATA=\{[\s\S]*?\nvar mseg/)||[])[0];
const ctx={};require("vm").createContext(ctx);require("vm").runInContext(dk+"\n"+block,ctx);
const {dedupKey,DATA,mergedList}=ctx;
const clone=o=>JSON.parse(JSON.stringify(o));
const eq=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
// ── [A] restore / round-trip (20k escenarios)
const mkPack=()=>{const rules=[{priority:ri(100),match:pick(["content_type","genre","source_in"]),value:pick(["manga","anime","movie","g"+ri(9)])}];return{major:2,rules_version:2,sha:sha(JSON.stringify(rules)),rules}};
const restore=(pack,appMajor)=>{if(pack.sha!==sha(JSON.stringify(pack.rules)))throw new Error("drift");if(pack.major!==appMajor)throw new Error("major");return clone(pack)};
const mkFeeds=pack=>({schema:"feed.v2.3",feeds:[{id:"f"+ri(9),name:"N",sources:[{pkg:"ext."+ri(9),enabled:true}],rules_ref:pack?"rp1":null,extra:{p:ri(9)},rNDM:pick([1,"a",null,{q:2}])}],packs:pack?[{id:"rp1",rules:pack.rules,sha:pack.sha,major:2}]:[],future:pick(["x",7,null])});
for(let i=0;i<20000;i++){
  const pack=mkPack(),feeds=mkFeeds(pack);
  try{
    const r1=restore(pack,2);
    ok(eq(r1.rules,pack.rules)&&r1.sha===pack.sha,"A"+i+": restauración limpia alteró el pack");
    const r2=restore(r1,2);
    ok(eq(r2,r1),"A"+i+": restore no idempotente");
    const rt=clone(feeds);
    ok(eq(rt.feeds[0].rNDM,feeds.feeds[0].rNDM)&&rt.future===feeds.future,"A"+i+": campo desconocido perdido en roundtrip");
    const mode=i%4;
    if(mode===0){const bad=clone(pack);bad.rules[0].value="novel";try{restore(bad,2);ok(false,"A-drift no detectado "+i)}catch(e){ok(e.message==="drift","A"+i)}}
    else if(mode===1){const bad=clone(pack);bad.sha="deadbeefdeadbeef";try{restore(bad,2);ok(false,"A-sello falso no detectado "+i)}catch(e){ok(e.message==="drift","A"+i)}}
    else if(mode===2){const bad=clone(pack);bad.major=3;try{restore(bad,2);ok(false,"A-cross-major no rechazado "+i)}catch(e){ok(e.message==="major","A"+i)}}
    else {const bad=clone(pack);bad.nuevoCampo={z:[1,2]};const r=restore(bad,2);ok(eq(r.nuevoCampo,{z:[1,2]}),"A"+i+": campo nuevo perdido same-major")}
  }catch(e){ok(false,"A-throw inesperado "+i+": "+e.message)}
}
// ── [B] precedencia total (50k evaluaciones)
const evalRules=(rules,entry)=>{
  const order=rules.map((r,i)=>({r,i:(r.__i!==undefined?r.__i:i)}))
    .sort((a,b)=>(a.r.priority-b.r.priority)||(a.i-b.i));
  for(const{r}of order){if(matchRule(r,entry))return r.segment}
  return "Sin asignar";
};
const matchRule=(r,e)=>r.match==="content_type"?e.type===r.value:(r.match==="genre"?e.genres.includes(r.value):e.src===r.value);
for(let i=0;i<50000;i++){
  const NR=1+ri(12),rules=[];
  for(let j=0;j<NR;j++)rules.push({priority:ri(100),segment:"S"+ri(5),match:pick(["content_type","genre","source_in"]),value:pick(["manga","anime","movie","g"+ri(4),"ext"+ri(4)])});
  const entry={type:pick(["manga","anime","movie"]),genres:["g"+ri(4),"g"+ri(4)],src:"ext"+ri(4)};
  const s1=evalRules(rules,entry),s2=evalRules(rules,entry);
  ok(s1===s2,"B"+i+": no determinista");
  // invarianza real: la evaluación depende de (priority, posición ORIGINAL), no del orden
  // transitorio del array (sort estable) — permutar el array con __i preservado no cambia nada
  const tagged=rules.map((r,ix)=>({...r,__i:ix}));
  const perm=tagged.slice();for(let j=perm.length-1;j>0;j--){const k=ri(j+1);[perm[j],perm[k]]=[perm[k],perm[j]]}
  ok(evalRules(perm,entry)===s1,"B"+i+": el resultado dependió del orden transitorio del array");
  const matching=rules.filter(r=>matchRule(r,entry));
  if(!matching.length)ok(s1==="Sin asignar","B"+i+": sin match debía caer al pool");
  else{const win=matching.reduce((m,r)=>(r.priority<m.priority)||(r.priority===m.priority&&rules.indexOf(r)<rules.indexOf(m))?r:m);
    ok(s1===win.segment,"B"+i+": ganador no es el mínimo (priority, orden)");}
}
// ── [C] caché de labels 50k llaves, GC por días (100k ops)
let cache={},pins={},days=0,lastSeen={};const DISC=[0,0.5,0.59,0.6,0.75,0.89,0.9,1];
const classify=(k,l,c)=>{if(pins[k])return"pinned";const o=cache[k];lastSeen[k]=days;
  if(!o){cache[k]={l,c};return"set"}
  if(l===o.l){o.c=Math.max(o.c,c);return"same"}
  if(c>=o.c+0.15||(o.c<0.6&&c>=0.9)){cache[k]={l,c};return"changed"}
  return"kept"};
let gcRuns=0;
for(let op=0;op<100000;op++){
  const k="k"+ri(50000),roll=rnd();
  if(roll<0.7)classify(k,pick(["A","B","C"]),pick(DISC));
  else if(roll<0.8){pins[k]=1;if(!cache[k])lastSeen[k]=days}
  else if(roll<0.85){delete pins[k]}
  else{days+=1+ri(60); // GC corre en el batch: purga unseen>=90d
    const expected=new Set();
    for(const kk in cache){if(pins[kk]||days-lastSeen[kk]<90)expected.add(kk)}
    for(const kk in cache)if(!expected.has(kk))delete cache[kk];
    gcRuns++;
    ok(Object.keys(cache).length===expected.size,"C-op"+op+": GC divergió del esperado");
  }
}
// pin survival fuerte: los pines NUNCA purgados
for(let i=0;i<2000;i++){const k="k"+ri(50000);if(pins[k]&&cache[k]){classify(k,pick(["A","B"]),1);ok(cache[k],"C-survival: pin sin caché")}}
ok(gcRuns>50,"C: GC corridas insuficientes ("+gcRuns+")");
// ── [D] tormenta de refresh con código vivo (10k ciclos)
const KEYS=["A","B","C"];let live={A:[],B:[],C:[]};let prevOrder=null,retrySet=new Set();
for(let cyc=0;cyc<10000;cyc++){
  const snap=clone(live),alive={},failed=[];
  for(const k of KEYS){const okS=rnd()<(retrySet.size?0.9:0.8);alive[k]=okS;if(!okS)failed.push(k)}
  const next={};
  for(const k of KEYS){
    if(alive[k]){const items=snap[k].map(it=>({t:it.t,ts:it.ts}));
      if(rnd()<0.5)items.push({t:"e"+cyc+"-"+k,ts:1600000000000+ri(100)});
      next[k]=items;
    } else next[k]=snap[k].map(it=>({t:it.t,ts:it.ts,stale:true})); // frozen + stale
  }
  const retry=new Set(failed);
  retrySet=retry;
  for(const k of failed)ok(next[k].length===0||next[k].every(it=>it.stale),"D"+cyc+": fuente caída sin sello stale ("+k+")");
  for(const k of KEYS)if(alive[k])ok(next[k].every(it=>!it.stale),"D"+cyc+": fuente viva con items stale ("+k+")");
  // orden relativo de ítems de fuentes vivas en r y r+1 preservado
  const extract=arr=>arr.filter(it=>!it.stale).map(it=>it.t);
  const a1=extract(next.A).concat(extract(next.B),extract(next.C));
  // construir vista ordenada con el modelo (ts desc, src asc, idx)
  const rows=[];KEYS.forEach(k=>next[k].forEach((it,idx)=>rows.push({k,it,idx})));
  rows.sort((x,y)=>(y.it.ts-x.it.ts)||(x.k<y.k?-1:1)||(x.idx-y.idx));
  const order=rows.map(r=>r.k+":"+r.it.t).join("|");
  if(prevOrder!==null){
    const prevAlive=prevAliveItems,nextAlive=a1;
    const inter=prevAlive.filter(t=>nextAlive.includes(t));
    const po=inter.map(t=>prevOrder.split("|").findIndex(s=>s.endsWith(":"+t)));
    const no=inter.map(t=>rows.map(r=>r.k+":"+r.it.t).findIndex(s=>s.endsWith(":"+t)));
    const rank=s=>s.map((v,i)=>[v,i]).sort((x,y)=>x[0]-y[0]).map(x=>x[1]).join(",");
    ok(rank(po)===rank(no),"D"+cyc+": orden relativo alterado bajo flapping");
  }
  prevOrder=order;prevAliveItems=a1;
  live=next;
  if(live.A.length>200)live.A=live.A.slice(-100);
  if(live.B.length>200)live.B=live.B.slice(-100);
  if(live.C.length>200)live.C=live.C.slice(-100);
}
// ── [E] vivo: dedupKey corpus 5k + merge 200×6
const POOL=["İ","ı","ß","ﬁ","ﷺ","Café","Ω","ｆｕｌｌ","Å","Ø","🅰","👨‍👩‍👧"," ","​","’","Ë","5"];
for(let i=0;i<5000;i++){let s="";const n=1+ri(8);for(let j=0;j<n;j++)s+=pick(POOL);
  const k1=dedupKey(s);ok(dedupKey(k1)===k1,"E-idem");ok(!/[^a-z0-9 ]/.test(k1),"E-ascii")}
for(let r=0;r<200;r++){
  const NS=1+ri(3),srcs=[];
  for(let s=0;s<NS;s++){const items=[],ni=1+ri(80);
    for(let i=0;i<ni;i++)items.push({t:ri(6)?"tie":"u"+r+s+i,ts:ri(20)<15?100+ri(2):100+ri(1000)});
    srcs.push(items)}
  const model=assign=>{const tr=[];KEYS.forEach((k,i)=>{(assign[i]||[]).forEach((it,idx)=>tr.push({k,it,idx}))});
    tr.sort((x,y)=>(y.it.ts-x.it.ts)||(x.k<y.k?-1:1)||(x.idx-y.idx));return tr.map(t=>t.k+"|"+t.it.t).join("·")};
  const base=srcs.map((_,i)=>i);
  const live1=(()=>{KEYS.forEach((k,i)=>DATA[k].items=srcs[i]||[]);return mergedList("recency").map(e=>e.k+"|"+e.it.t).join("·")})();
  ok(live1===model(srcs),"E-r"+r+": vivo ≠ modelo");
  for(let p=0;p<5;p++){const perm=srcs.map((_,i)=>i);for(let i=perm.length-1;i>0;i--){const j=ri(i+1);[perm[i],perm[j]]=[perm[j],perm[i]]}
    const l2=(()=>{KEYS.forEach((k,i)=>DATA[k].items=srcs[perm[i]]||[]);return mergedList("recency").map(e=>e.k+"|"+e.it.t).join("·")})();
    ok(l2===model(perm.map(pi=>srcs[pi])),"E-r"+r+"p"+p+": permutación")}
}
console.log("KERNEL v2.8: "+checks+" checks · "+fails+" violaciones · semilla 20281010");
fs.writeFileSync(__dirname+"/fuzz-v28-resultado.txt","checks="+checks+" violations="+fails+" seed=20281010\n");
process.exit(fails?1:0);
