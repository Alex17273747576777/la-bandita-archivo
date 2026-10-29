// CONFORMANCE KIT v1 — runner (zero dependencies · node >= 18)
// Runs every harness with fixed seeds; exits non-zero on any violation.
const {execFileSync}=require("child_process");
const files=[["K1-spec-model.js","spec-model battery (dedup · merge order · hysteresis · packs)"],
             ["K2-kernel.js","kernel battery (restore · precedence · cache/GC · refresh storms)"]];
let total=0,bad=0;
console.log("CONFORMANCE KIT v1 — "+new Date().toISOString().slice(0,10));
for(const[f,label]of files){
  try{
    const out=execFileSync(process.execPath,[__dirname+"/"+f],{encoding:"utf8",timeout:600000});
    const m=out.match(/(\d[\d.]*)\s*checks.*?(\d+)\s*viola\w*/s);
    const c=m?parseInt(m[1].replace(/\./g,"")):-1,v=m?parseInt(m[2]):-1;
    total+=c>0?c:0;bad+=v;
    console.log("  "+f.padEnd(16)+" "+String(c).padStart(7)+" checks · "+v+" violations · "+label);
  }catch(e){
    const out=e.stdout||"",m=out.match(/(\d[\d.]*)\s*checks.*?(\d+)\s*violations/s);
    const c=m?parseInt(m[1].replace(/\./g,"")):0,v=m?parseInt(m[2]):1;
    total+=c;bad+=v;
    console.log("  "+f.padEnd(16)+" FAILED ("+(m?c+" checks · "+v+" violations":e.message.slice(0,80))+")");
  }
}
console.log("TOTAL: "+total+" checks · "+bad+" violations"+(bad===0?" — CONFORME ✓":" — NO CONFORME ✗"));
process.exit(bad?1:0);
