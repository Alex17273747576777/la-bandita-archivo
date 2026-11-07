// BATERÍA HIPEREXTREMA v2.6 — código vivo del HTML + modelo del spec
// Semilla fija 20261010 (LCG). [1] dedupKey vivo 35k · [2] sort/union 400×6 perms ·
// [3] histéresis 600×300 ops · [4] packs/restore 200 · [5] diferencial JS↔Python (mitad Python aparte)
const fs=require("fs");
let seed=20261010>>>0;
const rnd=()=>((seed=(seed*1664525+1013904223)>>>0)/4294967296);
const ri=n=>Math.floor(rnd()*n);
const pick=a=>a[ri(a.length)];
let checks=0,fails=0;
const ok=(c,m)=>{checks++;if(!c){fails++;if(fails<15)console.log("  ✗",m)}};
const html=fs.readFileSync(__dirname+"/../_sugerencias/RFC-v2.7-UNIFIED-FEED-AniZen-Houri-2026-10-10.html","utf8");
const dk=(html.match(/function dedupKey\(t\)\{.*?\.trim\(\)\}/)||[])[0];
const block=(html.match(/var DATA=\{[\s\S]*?\nvar mseg/)||[])[0];
if(!dk||!block){console.error("EXTRACCIÓN FALLIDA",!!dk,!!block);process.exit(1)}
const ctx={};require("vm").createContext(ctx);require("vm").runInContext(dk+"\n"+block,ctx);
const {dedupKey,DATA,mergedList}=ctx;
// ── [1a] 25k strings del pool adversarial
const POOL=["İ","i","ı","I","ß","ﬁ","ﬀ","ﷺ"," café","Café","Ω","Ω","ｆｕｌｌ","ﾊﾝ","Å","Åbegun","Ø","Ó","ء","ي","🅰","👨‍👩‍👧","b","Æ","𝕏"," ","​","­","’","Ａ","ë","ëa","«x»","5","½","Ⅴ","İstanbul","ۖ"," chia","\t","\n","0","00"];
for(let i=0;i<25000;i++){
  const n=1+ri(9);let s="";for(let j=0;j<n;j++)s+=pick(POOL);
  const k1=dedupKey(s);
  ok(dedupKey(k1)===k1,"idempotencia: "+JSON.stringify(s));
  ok(!/[^a-z0-9 ]/.test(k1),"ASCII-out: "+JSON.stringify(s));
  ok(k1===k1.trim()&&!/ {2}|^ | $/.test(k1),"canónica: "+JSON.stringify(s));
}
// ── [1b] 10k strings de codepoints aleatorios hostiles
const RANGES=[[0x20,0x2fff],[0x300,0x36f],[0x1e00,0x1fff],[0xff00,0xffef],[0x1f300,0x1faff],[0xa0,0xa1],[0x345,0x345]];
for(let i=0;i<10000;i++){
  const n=1+ri(12);let s="";
  for(let j=0;j<n;j++){const[lo,hi]=pick(RANGES);s+=String.fromCodePoint(lo+ri(hi-lo+1))}
  const k1=dedupKey(s);
  ok(dedupKey(k1)===k1,"idem-rnd:"+JSON.stringify(s.slice(0,20)));
  ok(!/[^a-z0-9 ]/.test(k1),"ascii-rnd:"+JSON.stringify(k1.slice(0,20)));
}
// ── [2] sort vivo vs modelo canónico independiente: 400 rondas × 6 permutaciones
// (la deduplicación vive en la capa render según el spec; aquí se prueba la capa de ORDEN)
const KEYS=["A","B","C"];
const model=assign=>{ // orden canónico del spec: ts desc → src asc → in-source idx
  const tr=[];
  KEYS.forEach((k,i)=>{(assign[i]||[]).forEach((it,idx)=>tr.push({k,it,idx}))});
  tr.sort((x,y)=>(y.it.ts-x.it.ts)||(x.k<y.k?-1:(x.k>y.k?1:0))||(x.idx-y.idx));
  return tr.map(t=>t.k+"|"+t.it.t).join("·");
};
for(let r=0;r<400;r++){
  const NS=1+ri(3),srcs=[];
  for(let s=0;s<NS;s++){
    const items=[],ni=1+ri(150);
    for(let i=0;i<ni;i++){
      const t=ri(8)===0?("uniq-"+r+"-"+s+"-"+i):("tie-"+ri(6));
      items.push({t,ts:ri(100)<85?(1600000000000+ri(3)):1600000000000+ri(10**6)});
    }
    srcs.push(items);
  }
  const keysUsed=KEYS.slice(0,NS);
  const keysDist=new Set();srcs.forEach(s=>s.forEach(it=>keysDist.add(dedupKey(it.t))));
  for(let p=0;p<6;p++){
    const perm=srcs.map((_,i)=>i);
    for(let i=perm.length-1;i>0;i--){const j=ri(i+1);[perm[i],perm[j]]=[perm[j],perm[i]]}
    const assign=KEYS.map((_,i)=>perm[i]!==undefined?srcs[perm[i]]:null);
    const live=(()=>{KEYS.forEach(k=>DATA[k].items=[]);assign.forEach((a,i)=>{if(a)DATA[KEYS[i]].items=a});return mergedList("recency").map(e=>e.k+"|"+e.it.t).join("·")})();
    ok(live===model(assign),"r"+r+" p"+p+": orden vivo ≠ modelo canónico");
    const live2=(()=>{return mergedList("recency").map(e=>e.k+"|"+e.it.t).join("·")})();
    ok(live===live2,"r"+r+" p"+p+": no determinista (doble llamada)");
  }
  const full=(()=>{KEYS.forEach(k=>DATA[k].items=[]);srcs.forEach((a,i)=>{DATA[KEYS[i]].items=a});return mergedList("recency")})();
  const seen=new Set();let kept=0;
  full.forEach(e=>{const k=dedupKey(e.it.t);if(!seen.has(k)){seen.add(k);kept++}});
  ok(kept===keysDist.size,"r"+r+": vista canónica "+kept+"≠"+keysDist.size);
}
// ── [3] histéresis (regla fija v2.5) 600 × 300 ops, grid de confinamiento en fronteras
const GRID=[0,0.5,0.59,0.599,0.6,0.601,0.74,0.75,0.751,0.89,0.9,0.901,1];
let cache={},pins={},days=0;
const reset=()=>{cache={};pins={};days=0};
function classify(key,label,conf){
  if(pins[key])return "pinned"; // el pin manda SIEMPRE, incluso sin caché
  const old=cache[key];
  if(!old){cache[key]={label,conf};return "set"}
  if(label===old.label){old.conf=Math.max(old.conf,conf);return "same"}
  if(conf>=old.conf+0.15||(old.conf<0.60&&conf>=0.90)){cache[key]={label,conf};return "changed"}
  return "kept";
}
for(let run=0;run<600;run++){
  reset();const labels=["A","B","C"];
  for(let op=0;op<300;op++){
    const key="k"+ri(40),roll=rnd();
    if(roll<0.62){
      const label=pick(labels),conf=pick(GRID)+(rnd()<0.3?rnd()*0.1:0);
      const old=cache[key];
      const res=classify(key,label,conf);
      if(res==="changed"){
        const nc=cache[key];
        ok(nc.conf>=old.conf+0.15||(old.conf<0.60&&nc.conf>=0.90),"run"+run+"op"+op+": cambio sin regla");
        ok(nc.label!==old.label,"run"+run+"op"+op+": 'cambio' con misma etiqueta");
      } else if(res==="kept"){
        ok(!(conf>=old.conf+0.15||(old.conf<0.60&&conf>=0.90)),"run"+run+"op"+op+": keep ilegal");
      }
      ok(!pins[key]||!cache[key]||cache[key].label===pins[key],"run"+run+"op"+op+": pin violado");
    } else if(roll<0.75){const l=pick(labels);pins[key]=l;if(cache[key])cache[key].label=l}
    else if(roll<0.85){delete pins[key];if(cache[key])delete cache[key]}
    else if(roll<0.95){
      const d=ri(120);days+=d;
      if(d>=90){const had=Object.keys(pins).filter(k=>cache[k]);
        for(const k in cache)if(!pins[k])delete cache[k];
        had.forEach(k=>ok(!!cache[k],"run"+run+"op"+op+": GC borró un pin ("+k+")"));}
    } else { // cold-start: caché vacía clasifica de cero
      cache={};const fk="k"+ri(40);
      ok(classify(fk,pick(labels),1)===(pins[fk]?"pinned":"set"),"run"+run+"op"+op+": cold-start inconsistente");
    }
  }
}
// ── [4] packs content-addressed + feeds.json roundtrip: 200 escenarios honestos
const sha=s=>require("crypto").createHash("sha256").update(s).digest("hex").slice(0,16);
const restore=(pack,appMajor)=>{
  if(pack.sha!==sha(JSON.stringify(pack.rules)))throw new Error("drift");
  if(pack.major!==appMajor)throw new Error("major");
  return pack;
};
for(let i=0;i<200;i++){
  const rules=[{f:"content_type",v:pick(["manga","anime","movie"])},{f:"genre",v:"g"+ri(9)}];
  const pack={major:2,rules_version:2,sha:sha(JSON.stringify(rules)),rules};
  const mode=ri(3);
  try{
    if(mode===0){restore(pack,pack.major);ok(true,"limpio restaura "+i)}
    else if(mode===1){const bad=JSON.parse(JSON.stringify(pack));bad.rules[0].v="novel";
      try{restore(bad,2);ok(false,"drift NO detectado "+i)}catch(e){ok(e.message==="drift","drift lanza "+i)}}
    else {const bad=JSON.parse(JSON.stringify(pack));bad.sha="deadbeefdeadbeef";
      try{restore(bad,2);ok(false,"sello falso NO detectado "+i)}catch(e){ok(e.message==="drift","sello falso lanza "+i)}}
    const feeds={feeds:[{id:"f1",name:"Movies",rules_ref:"rp1",extraCampo:{p:1}}],packs:[{id:"rp1",rules}],future:"x"};
    const rt=JSON.parse(JSON.stringify(feeds));
    ok(rt.feeds[0].extraCampo.p===1&&rt.future==="x","campos desconocidos intactos "+i);
    const cross=JSON.parse(JSON.stringify(pack));cross.major=3;
    try{restore(cross,2);ok(false,"cross-major NO rechazado "+i)}catch(e){ok(e.message==="major","cross-major rechaza "+i)}
  }catch(e){ok(false,"throw inesperado "+i+": "+e.message)}
}
console.log("TOTAL: "+checks+" checks · "+fails+" violaciones · semilla 20261010");
fs.writeFileSync(__dirname+"/fuzz-v26-resultado.txt","checks="+checks+" violations="+fails+" seed=20261010 date=2026-10-10\n");
process.exit(fails?1:0);
