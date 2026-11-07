#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# FORJA v2 DEL MEGA CATÁLOGO — reglas anti-bug:
#  1) template en r"""...""" (backslashes pasan intactos al JS)
#  2) JS: SIEMPRE strings dobles; HTML: atributos con comilla simple
#  3) onclick='go("p",4)'  (nunca \' anidados)
#  4) verificación obligatoria: node --check + json.loads antes de declarar éxito
import os, re, json, hashlib

BASE = "/home/user/Arena-Reimagined"
WA = os.path.join(BASE, "01-PUBLICACIONES/WhatsApp-dominicano-ES")
FBP = os.path.join(BASE, "01-PUBLICACIONES/Facebook-dominicano-ES")

CAT = {
 "00": ("🧭", "Índice"), "01": ("🏪", "Tiendas"), "02": ("📖", "Manga"), "03": ("🔍", "Verificación"),
 "04": ("📚", "Manga"), "05": ("📖", "Manga"), "06": ("🌿", "Manga"), "07": ("🌳", "Manga"),
 "08": ("🎧", "Música"), "09": ("🧰", "Herramientas"), "10": ("🎮", "Gaming"), "11": ("🗺", "Privacidad"),
 "12": ("🛡", "Privacidad"), "13": ("🧬", "Sistemas"), "14": ("🧬", "Sistemas"), "15": ("📖", "Manga"),
 "16": ("🎬", "Video"), "17": ("🧪", "Patching"), "18": ("🖥", "Sistemas"), "19": ("🤖", "IA"),
 "20": ("🎚", "Audio · Root"),
}

def health(text):
    lines = text.split("\n"); blocks = []; cur = []; inf = False
    for l in lines:
        if l.strip().startswith("```"):
            if cur: blocks.append("\n".join(cur)); cur = []
            inf = not inf; continue
        if inf: continue
        if l.strip() == "":
            if cur: blocks.append("\n".join(cur)); cur = []
            continue
        cur.append(l)
    if cur: blocks.append("\n".join(cur))
    real = [b for b in blocks if not (len(b.split("\n")) == 1 and (b.startswith("REV|") or b.startswith("(Las respuestas")))]
    over = [len(b) for b in real if len(b) > 380]
    return {"over": len(over), "max": max((len(b) for b in real), default=0)}

pieces = []
for f in sorted(os.listdir(WA)):
    if not f.endswith(".md") or f.startswith("LEEME") or "-2026-10-02" in f:
        continue
    d = open(os.path.join(WA, f), encoding="utf-8").read()
    pid = f[:2]
    L = d.split("\n"); title = tag = ""
    for l in L[:6]:
        m = re.match(r"^\*(\S? ?[^*\n]+)\*$", l.strip())
        if m and not title and len(m.group(1)) < 70: title = m.group(1).strip()
        elif m and title and not tag: tag = m.group(1).strip()
        if title and tag: break
    stars = []
    for s in re.findall(r"★\s*(\d[\d.,]*)", d):
        s2 = s.rstrip(".,")
        if s2:
            try: stars.append(float(s2.replace(".", "").replace(",", ".")))
            except ValueError: pass
    cat = CAT.get(pid, ("📄", "General"))
    pieces.append({"idx": len(pieces), "id": pid, "file": f, "title": title, "tag": tag[:170],
                   "cat": cat[1], "ico": cat[0], "len": len(d),
                   "sha": hashlib.sha256(d.encode()).hexdigest()[:16],
                   "stars": int(max(stars)) if stars else 0, "health": health(d), "text": d})

fb = []
for f in sorted(os.listdir(FBP)):
    if not f.endswith(".md") or f.startswith("LEEME"):
        continue
    d = open(os.path.join(FBP, f), encoding="utf-8").read()
    if "💓" not in d: continue
    m = re.match(r"^\*(\S? ?[^*\n]+)\*$", d.split("\n")[0].strip())
    fb.append({"file": f, "title": (m.group(1).strip() if m else f[:40]), "len": len(d), "text": d})

data = {"wa": pieces, "fb": fb}
js = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")

TPL = r"""<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>LA BANDITA · Mega Catálogo</title>
<style>
:root{--bg:#050505;--card:#0a0a0a;--card2:#101418;--line:rgba(255,255,255,.07);--line2:rgba(255,255,255,.13);--txt:#e2e8f0;--mut:#94a3b8;--mut2:#64748b;--acc:#10b981;--acc2:#34d399;--amber:#f59e0b;--bad:#f87171;--blue:#38bdf8}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--txt);font:15px/1.65 system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;-webkit-font-smoothing:antialiased}
#glow{position:fixed;top:0;left:0;right:0;height:420px;background:linear-gradient(180deg,rgba(16,185,129,.14),rgba(16,185,129,.04) 55%,transparent);pointer-events:none;z-index:0}
#pbar{position:fixed;top:0;left:0;height:2px;background:linear-gradient(90deg,#10b981,#34d399);width:0;z-index:60}
header{position:sticky;top:0;z-index:50;background:rgba(5,5,5,.85);backdrop-filter:blur(14px);border-bottom:1px solid var(--line)}
.hwrap{max-width:1100px;margin:0 auto;padding:10px 16px;display:flex;gap:12px;align-items:center;flex-wrap:wrap}
.logo{display:flex;gap:10px;align-items:center;cursor:pointer;user-select:none}
.logo .tile{width:38px;height:38px;border-radius:12px;background:linear-gradient(135deg,#34d399,#047857);display:grid;place-items:center;font-size:19px;box-shadow:0 4px 18px rgba(16,185,129,.35)}
.logo b{font-size:14px;letter-spacing:.06em}.logo small{display:block;color:var(--mut2);font-size:10px;letter-spacing:.22em;text-transform:uppercase}
#q{flex:1;min-width:180px;max-width:430px;background:var(--card);border:1px solid var(--line2);border-radius:999px;padding:8px 16px;color:var(--txt);font-size:13.5px;outline:none}
#q:focus{border-color:var(--acc)}
.tab{background:none;border:1px solid var(--line2);color:var(--mut);border-radius:999px;padding:7px 14px;cursor:pointer;font-size:12.5px}
.tab:hover{color:var(--txt)}.tab.on{background:var(--acc);border-color:var(--acc);color:#032e22;font-weight:700}
main{position:relative;z-index:1}
.wrap{max-width:1100px;margin:0 auto;padding:26px 16px 90px}
.read{max-width:800px;margin:0 auto}
.kicker{color:var(--acc);font-size:11.5px;letter-spacing:.28em;text-transform:uppercase;font-weight:700}
.crumbs{display:flex;gap:7px;align-items:center;color:var(--mut2);font-size:12.5px;margin-bottom:20px;flex-wrap:wrap}
.crumbs a{color:var(--mut);cursor:pointer}.crumbs a:hover{color:var(--acc2)}
.crumbs .ch{opacity:.4}
.hero{display:flex;gap:20px;align-items:center;margin:4px 0 18px}
.hero .tile{width:96px;height:96px;border-radius:24px;background:var(--card);border:1px solid var(--line);display:grid;place-items:center;font-size:44px;flex-shrink:0;box-shadow:0 10px 40px rgba(0,0,0,.55)}
.hero h1{margin:0;font-size:26px;letter-spacing:-.02em;line-height:1.22}
.hero .sub{color:var(--mut);font-size:13.5px;margin-top:6px}
.vline{display:flex;gap:7px;align-items:center;margin-top:9px;font-size:12.5px;color:var(--acc2);font-weight:600}
.chips{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin:18px 0}
.chip{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:12px 14px}
.chip .l{font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--mut2);font-weight:700}
.chip .v{font-size:15px;font-weight:700;margin-top:3px;word-break:break-all}
.chip .v.ok{color:var(--acc2)}.chip .v.warn{color:var(--amber)}
.acts{display:flex;gap:10px;flex-wrap:wrap;margin:4px 0 24px}
.btn{border:0;border-radius:999px;padding:11px 22px;font-size:13.5px;font-weight:700;cursor:pointer;transition:.2s}
.btn.pri{background:linear-gradient(135deg,#34d399,#059669);color:#022c22;box-shadow:0 6px 24px rgba(16,185,129,.3)}
.btn.pri:hover{transform:translateY(-1px)}
.btn.gho{background:var(--card);border:1px solid var(--line2);color:var(--txt)}
.btn.gho:hover{border-color:var(--acc);color:var(--acc2)}
.btn.gho.on{border-color:var(--bad);color:var(--bad)}
.card{background:var(--card);border:1px solid var(--line);border-radius:20px;padding:18px 20px;margin:16px 0}
.card h4{margin:0 0 12px;font-size:11.5px;letter-spacing:.22em;text-transform:uppercase;color:var(--mut)}
.toc{columns:2;column-gap:26px;font-size:13.5px}
.toc a{display:block;color:var(--mut);cursor:pointer;padding:3.5px 0;break-inside:avoid}
.toc a:hover{color:var(--acc2)}
article{font-size:15px;line-height:1.72}
article h3{font-size:16.5px;margin:26px 0 8px;color:#fff;scroll-margin-top:84px}
article strong{color:#fff}
.star{color:var(--amber);font-weight:700}
.fence{background:#0b1210;border:1px solid rgba(16,185,129,.16);border-radius:14px;padding:14px 16px;overflow-x:auto;font:12.5px/1.5 ui-monospace,Menlo,Consolas,monospace;color:#a7f3d0;white-space:pre;margin:10px 0;word-break:break-word;white-space:pre-wrap}
.blk{padding:2px 0;position:relative}
.blk.big{outline:2px dashed rgba(248,113,113,.8);outline-offset:4px;border-radius:8px;background:rgba(248,113,113,.06)}
.blk.big::after{content:attr(data-n)"c > 380";position:absolute;top:-10px;right:6px;background:var(--bad);color:#111;font-size:10px;font-weight:800;padding:1px 8px;border-radius:999px}
.rel{background:rgba(245,158,11,.22);border-bottom:1px dotted var(--amber);border-radius:3px}
.quiz{border:1px solid rgba(16,185,129,.3);background:rgba(16,185,129,.05);border-radius:16px;padding:16px 18px;margin:12px 0}
.quiz .ql{color:var(--mut);font-size:11.5px;letter-spacing:.12em;text-transform:uppercase;font-weight:700;margin-bottom:8px}
.quiz .rev{font-family:ui-monospace,Menlo,monospace;font-size:12.5px;color:var(--mut);filter:blur(5px);user-select:none;transition:filter .35s;line-height:1.9;word-break:break-all}
.quiz.open .rev{filter:none;color:#a7f3d0}
.quiz .sol{display:none;font-size:13.5px;color:#d1fae5;line-height:1.7;margin-top:10px;border-top:1px dashed rgba(16,185,129,.25);padding-top:10px}
.quiz.open .sol{display:block}
.nav2{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:34px}
.nav2 .card{cursor:pointer;transition:.2s}.nav2 .card:hover{border-color:var(--acc)}
.nav2 .dir{font-size:11px;letter-spacing:.2em;color:var(--mut2);text-transform:uppercase}
.nav2 .t{font-weight:700;margin-top:4px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(258px,1fr));gap:14px;margin-top:22px}
.pcard{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:16px;cursor:pointer;transition:.22s;display:flex;flex-direction:column;gap:10px}
.pcard:hover{transform:translateY(-3px);border-color:rgba(52,211,153,.45);box-shadow:0 14px 34px rgba(0,0,0,.5)}
.pcard .top{display:flex;gap:12px;align-items:center}
.pcard .tile{width:46px;height:46px;border-radius:14px;background:var(--card2);border:1px solid var(--line);display:grid;place-items:center;font-size:22px;flex-shrink:0}
.pcard .t{font-weight:700;font-size:13.5px;line-height:1.35;color:#fff}
.pcard .d{color:var(--mut);font-size:12px;line-height:1.5;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.pcard .m{display:flex;gap:6px;flex-wrap:wrap;font-size:10.5px;color:var(--mut2)}
.badge{border:1px solid var(--line2);border-radius:999px;padding:2px 9px}
.badge.ok{border-color:rgba(16,185,129,.4);color:var(--acc2)}
.badge.wa{border-color:rgba(245,158,11,.45);color:var(--amber)}
.badge.st{border-color:rgba(56,189,248,.35);color:var(--blue)}
.fchips{display:flex;gap:8px;flex-wrap:wrap;margin-top:20px}
.fchip{background:var(--card);border:1px solid var(--line2);color:var(--mut);border-radius:999px;padding:6px 14px;font-size:12px;cursor:pointer}
.fchip:hover{color:var(--txt)}.fchip.on{background:var(--acc);border-color:var(--acc);color:#032e22;font-weight:700}
textarea{width:100%;background:#0b1210;color:#d1d5db;border:1px solid var(--line2);border-radius:12px;padding:12px;font:12px/1.5 ui-monospace,Menlo,monospace;min-height:130px;resize:vertical;margin-top:10px}
.tst{position:fixed;bottom:22px;left:50%;transform:translateX(-50%) translateY(90px);background:var(--acc);color:#022c22;font-weight:700;border-radius:999px;padding:10px 22px;font-size:13px;transition:.3s;z-index:99}
.tst.on{transform:translateX(-50%) translateY(0)}
footer{border-top:1px solid var(--line);color:var(--mut2);font-size:11.5px;text-align:center;padding:26px 16px 44px;line-height:1.8}
.empty{color:var(--mut2);text-align:center;padding:60px 0}
@media(max-width:640px){.hero{flex-direction:column;text-align:center}.toc{columns:1}.nav2{grid-template-columns:1fr}}
::selection{background:rgba(16,185,129,.35)}
::-webkit-scrollbar{width:10px;height:10px}::-webkit-scrollbar-thumb{background:#1e293b;border-radius:8px}
</style></head><body>
<div id="glow"></div><div id="pbar"></div>
<header><div class="hwrap">
<div class="logo" onclick='go("home")'><div class="tile">🎧</div><div><b>LA BANDITA</b><small>Mega Catálogo</small></div></div>
<input id="q" placeholder="Buscar en las piezas…  ( / )" autocomplete="off">
<button class="tab on" data-t="home" onclick='go("home")'>Catálogo</button>
<button class="tab" data-t="fb" onclick='go("fb")'>Muro FB · texto</button>
</div></header>
<main><div class="wrap" id="view"></div></main>
<footer>La Bandita · <b>__NWA__ piezas WhatsApp</b> convertidas de texto plano a catálogo + <b>__NFB__ piezas del muro</b> como texto para copiar · censo y sellos 15-oct-2026 ·<br>ADN de diseño medido a la referencia y reconstruido (columna 800px · glow esmeralda · cards 24px · chips uppercase) · el sello y la salud de respiro de cada pieza se recalculan al vuelo en tu navegador</footer>
<div class="tst" id="tst">OK</div>
<script>
const D = __DATA__;
function $(s){return document.querySelector(s)}
let view="home", cur=null, xray=false, cat="Todas", q="";
function cps(s){var n=0;for(const c of s)n++;return n}
function esc(s){return s.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;")}
function toast(m){const t=$("#tst");t.textContent=m;t.classList.add("on");setTimeout(()=>t.classList.remove("on"),1900)}
function blocks(text){
  const L=text.split("\n"), out=[]; let buf=[], inf=false, start=0;
  function flush(){ if(buf.length){ out.push({raw:buf.join("\n"),start:start}); buf=[]; } }
  L.forEach((l,i)=>{ if(l.trim().startsWith("```")){ flush(); out.push({raw:l,fence:true,start:i+1}); inf=!inf; return; }
    if(inf){ out.push({raw:l,fence:true,start:i+1}); return; }
    if(l.trim()===""){ flush(); return; }
    if(!buf.length) start=i+1; buf.push(l); });
  flush(); return out;
}
function health(text){
  const bs=blocks(text).filter(b=>!b.fence && !/^(REV\||\(Las respuestas)/.test(b.raw));
  return {over:bs.filter(b=>cps(b.raw)>380).length, max:Math.max(0,...bs.map(b=>cps(b.raw)))};
}
function fmtBlock(b){
  if(b.fence) return "<pre class=\"fence\">"+esc(b.raw.replace(/^```\w*\n?/,"").replace(/\n?```$/,""))+"</pre>";
  let h=esc(b.raw);
  h=h.replace(/^\*([^*\n]{2,64})\*$/,"<h3 id=\"h"+b.start+"\">$1</h3>");
  h=h.replace(/\*([^*\n]+)\*/g,"<strong>$1</strong>");
  h=h.replace(/★\s*([\d.,]+)/g,"<span class=\"star\">★$1</span>");
  if(xray) h=h.replace(/\b(hoy|mañana|ayer|este jueves|mismo jueves|MISMO jueves|esta tarde|matinal|al cierre)\b/g,"<span class=\"rel\">$1</span>");
  h=h.replace(/\n/g,"<br>");
  const isQ=/^(REV\||\(Las respuestas)/.test(b.raw);
  const big=xray && cps(b.raw)>380 && !isQ;
  return "<div class=\"blk"+(big?" big":"")+"\""+(big?(" data-n=\""+cps(b.raw)+"\""):"")+">"+h+"</div>";
}
function extractQuiz(text){
  const L=text.split("\n"), found=[];
  L.forEach((l,i)=>{ if(l.startsWith("Respuestas al rev")) found.push(i); });
  return found.map(i0=>{
    let j=i0+1;
    while(j<L.length && L[j].trim()==="") j++;
    let rev="";
    while(j<L.length && L[j].startsWith("REV|")){ rev+=(rev?"\n":"")+L[j]; j++; }
    while(j<L.length && L[j].trim()==="") j++;
    let sol="";
    while(j<L.length && !L[j].startsWith("*")){ sol+=L[j]+"\n"; j++; }
    return {line:i0, rev:rev, sol:sol.trim()};
  });
}
function renderContent(text){
  const qs=extractQuiz(text);
  let t=text;
  qs.forEach((qz,k)=>{
    t=t.replace(qz.rev,"\u0000Q"+k+"\u0000");
    t=t.replace(/\(Las respuestas correctas[^\n]*\n?/,"\u0000S"+k+"\u0000\n");
  });
  const bs=blocks(t).filter(b=>b.raw.trim()!=="");
  const quizHtml=qs.map((qz,k)=>{
    const segs=qz.rev.split("|REV|").map(s=>s.replace(/^REV\|/,"")).filter(s=>s.length>0);
    const dec=segs.map(s=>s.split("").reverse().join(""));
    return "<div class=\"quiz\" id=\"qz"+k+"\"><div class=\"ql\">🎯 Mini-quiz · respuestas cifradas al revés — tópalas y descífralas</div>"+
      "<div class=\"rev\">"+esc(segs.map((s,x)=>"REV|"+s).join("\n"))+"</div>"+
      "<div class=\"sol\">"+dec.map(d=>"<div>• "+esc(d)+"</div>").join("")+(qz.sol?"<div style=\"margin-top:8px;color:var(--mut)\">"+esc(qz.sol)+"</div>":"")+"</div>"+
      "<button class=\"btn gho\" style=\"margin-top:10px;padding:7px 16px;font-size:12px\" onclick='this.parentElement.classList.toggle(\"open\")'>🔓 Descifrar respuestas</button></div>";
  });
  return bs.map(b=>{
    const mq=b.raw.match(/\u0000Q(\d+)/);
    if(mq) return quizHtml[+mq[1]];
    if(/^\u0000S\d+$/.test(b.raw.trim())) return "";
    return fmtBlock(b);
  }).join("");
}
function chip(l,v,cls){return "<div class=\"chip\"><div class=\"l\">"+l+"</div><div class=\"v "+(cls||"")+"\">"+v+"</div></div>"}
function card(p){
  const h=health(p.text);
  return "<div class=\"pcard\" onclick='go(\"p\","+p.idx+")'>"+
    "<div class=\"top\"><div class=\"tile\">"+p.ico+"</div><div><div class=\"t\">"+esc(p.title)+"</div>"+
    "<div style=\"color:var(--mut2);font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;margin-top:2px\">"+p.cat+"</div></div></div>"+
    "<div class=\"d\">"+esc(p.tag||p.title)+"</div>"+
    "<div class=\"m\"><span class=\"badge\">"+p.len.toLocaleString()+" c</span>"+
    (p.stars?"<span class=\"badge st\">★"+p.stars.toLocaleString()+" pico</span>":"")+
    "<span class=\"badge "+(h.over===0?"ok":"wa")+"\">"+(h.over===0?"respirable ✓":h.over+" >380c")+"</span>"+
    "<span class=\"badge\">censo 15-oct</span></div></div>";
}
function goHome(){
  view="home"; cur=null;
  const cats=["Todas",...new Set(D.wa.map(p=>p.cat))];
  let list=D.wa.filter(p=>cat==="Todas"||p.cat===cat);
  const query=q.trim().toLowerCase();
  let note="";
  if(query.length>2){
    const hits={};
    D.wa.forEach(p=>{ hits[p.idx]=(p.text.toLowerCase().split(query).length-1); });
    list=list.filter(p=>p.title.toLowerCase().includes(query)||p.tag.toLowerCase().includes(query)||hits[p.idx]>0);
    const parts=Object.entries(hits).filter(([k,v])=>v>0).map(([k,v])=>"#"+D.wa[k].id+" ("+v+")");
    note="<div class=\"card\" style=\"margin-top:14px\"><h4>🔎 "+esc(q)+"</h4><div style=\"color:var(--mut)\">"+list.length+" piezas coinciden · ocurrencias en contenido: "+(parts.join(" · ")||"—")+"</div></div>";
  }
  $("#view").innerHTML="<div style=\"text-align:center;padding:16px 0 4px\">"+
    "<div class=\"kicker\">Biblioteca libre dominicana · censo 15-oct-2026</div>"+
    "<h1 style=\"font-size:34px;letter-spacing:-.03em;margin:10px 0 4px\">Mega Catálogo <span style=\"color:var(--acc)\">La Bandita</span></h1>"+
    "<div style=\"color:var(--mut);font-size:14px\">"+D.wa.length+" guías WhatsApp de texto plano a catálogo — sello, censo y salud de respiro recalculados al vuelo.</div></div>"+
    "<div class=\"chips\">"+chip("Piezas",D.wa.length)+chip("Muro FB (copia)",D.fb.length)+chip("Censo","15-oct-2026")+chip("Certificación","v4+v5+v6+fu","ok")+"</div>"+
    "<div class=\"fchips\">"+cats.map(c=>"<button class=\"fchip"+(c===cat?" on":"")+"\" onclick='setCat(\""+c+"\")'>"+c+"</button>").join("")+"</div>"+note+
    "<div class=\"grid\">"+(list.length?list.map(card).join(""):"<div class=\"empty\">Nada por aquí con ese filtro.</div>")+"</div>";
  window.scrollTo(0,0);
}
function goPiece(k){
  const p=D.wa[k]; if(p==null) return;
  view="p"; cur=p;
  const prev=D.wa[k-1], next=D.wa[k+1];
  const h=health(p.text);
  const sim=D.wa.filter(x=>x.cat===p.cat&&x.idx!==p.idx).slice(0,5);
  const tocs=p.text.split("\n").map((l,i)=>({l,i:i+1})).filter(x=>/^\*[^*\n]{3,48}\*$/.test(x.l));
  $("#view").innerHTML="<div class=\"read\">"+
    "<div class=\"crumbs\"><a onclick='go(\"home\")'>Catálogo</a><span class=\"ch\">›</span><span>"+p.cat+"</span><span class=\"ch\">›</span><span>"+p.id+"</span></div>"+
    "<div class=\"hero\"><div class=\"tile\">"+p.ico+"</div><div><h1>"+esc(p.title)+"</h1>"+
    "<div class=\"sub\">"+esc(p.tag||"")+"</div>"+
    "<div class=\"vline\">✓ Verificada · batería 24/24 · 30/30 · fuzz 60/60 · lupa-v6 aire</div></div></div>"+
    "<div class=\"chips\">"+chip("Tamaño (len)",p.len.toLocaleString()+" c")+chip("Sello SHA-256",p.sha)+
    chip("Respiro",(h.over===0?"0 >380c ✓":h.over+" bloques >380c"),(h.over===0?"ok":"warn"))+
    chip("Fama censada",p.stars?("★"+p.stars.toLocaleString()+" pico"):"—")+"</div>"+
    "<div class=\"acts\"><button class=\"btn pri\" onclick='dl("+p.idx+")'>⬇ Descargar .md</button>"+
    "<button class=\"btn gho\" onclick='cp("+p.idx+")'>📋 Copiar fuente</button>"+
    "<button class=\"btn gho"+(xray?" on":"")+"\" onclick='toggleX()'>🩻 Rayos-X</button></div>"+
    "<div class=\"card\"><h4>En esta guía · "+tocs.length+" secciones</h4><div class=\"toc\">"+
    tocs.map(x=>"<a onclick='jump(\"h"+x.i+"\")'>"+esc(x.l.replace(/^\*/,"").replace(/\*$/,""))+"</a>").join("")+"</div></div>"+
    "<article>"+renderContent(p.text)+"</article>"+
    "<div class=\"nav2\">"+(prev?"<div class=\"card\" onclick='go(\"p\","+(k-1)+")'><div class=\"dir\">← Anterior</div><div class=\"t\">"+esc(prev.title)+"</div></div>":"<div></div>")+
    (next?"<div class=\"card\" style=\"text-align:right\" onclick='go(\"p\","+(k+1)+")'><div class=\"dir\">Siguiente →</div><div class=\"t\">"+esc(next.title)+"</div></div>":"<div></div>")+"</div>"+
    (sim.length?"<div class=\"card\" style=\"margin-top:26px\"><h4>Piezas hermanas · "+p.cat+"</h4>"+sim.map(x=>"<div class=\"pcard\" style=\"margin:8px 0\" onclick='go(\"p\","+x.idx+")'><div class=\"top\"><div class=\"tile\">"+x.ico+"</div><div><div class=\"t\">"+esc(x.title)+"</div><div class=\"d\">"+esc(x.tag||"")+"</div></div></div></div>").join("")+"</div>":"")+
    "</div>";
  window.scrollTo(0,0);
}
function goFB(){
  view="fb";
  $("#view").innerHTML="<div style=\"text-align:center;padding:14px 0 4px\"><div class=\"kicker\">Para copiar y subir a la plataforma</div>"+
    "<h1 style=\"font-size:30px;letter-spacing:-.02em;margin:8px 0 4px\">Muro Facebook · texto puro</h1>"+
    "<div style=\"color:var(--mut)\">Estas NO van en HTML: se copian tal cual al muro. Las de era-vieja ya publicadas no van aquí.</div></div>"+
    "<div style=\"display:flex;flex-direction:column;gap:14px;margin-top:18px\">"+D.fb.map((p,i)=>
    "<div class=\"card\"><div style=\"display:flex;gap:10px;align-items:center;flex-wrap:wrap\"><b>💓 "+esc(p.title)+"</b>"+
    "<span class=\"badge\">"+p.len.toLocaleString()+" c</span><span class=\"badge ok\">caja de pulso viva</span>"+
    "<button class=\"btn pri\" style=\"margin-left:auto;padding:8px 18px;font-size:12px\" onclick='cpf("+i+")'>📋 Copiar pieza entera</button></div>"+
    "<details><summary style=\"cursor:pointer;color:var(--acc2);font-size:13px;margin-top:10px\">ver texto</summary>"+
    "<textarea id=\"fb"+i+"\" readonly>"+esc(p.text)+"</textarea></details></div>").join("")+"</div>";
  window.scrollTo(0,0);
}
function setCat(c){cat=c;goHome()}
function go(v,k){
  if(v==="home"){q="";$("#q").value="";goHome();}
  else if(v==="fb") goFB();
  else goPiece(k);
  document.querySelectorAll(".tab").forEach(t=>t.classList.toggle("on",(v==="p"&&t.dataset.t==="home")||t.dataset.t===v));
}
function jump(id){const el=document.getElementById(id); if(el) el.scrollIntoView({behavior:"smooth",block:"start"});}
function toggleX(){xray=!xray;if(cur)goPiece(cur.idx);}
function dl(k){const p=D.wa[k];try{const b=new Blob([p.text],{type:"text/markdown"});const a=document.createElement("a");a.href=URL.createObjectURL(b);a.download=p.file;a.click();toast("⬇ "+p.file)}catch(e){toast("Descarga bloqueada aquí — usa Copiar")}}
function cp(k){const p=D.wa[k];copy(p.text,"Fuente copiada ("+p.len.toLocaleString()+" c)")}
function cpf(i){copy(D.fb[i].text,"Pieza del muro copiada — pegar en Facebook")}
function copy(t,m){
  if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(t).then(()=>toast("📋 "+m)).catch(()=>fallbackCopy(t,m));}
  else fallbackCopy(t,m);
}
function fallbackCopy(t,m){const ta=document.createElement("textarea");ta.value=t;document.body.appendChild(ta);ta.select();let ok=false;try{ok=document.execCommand("copy")}catch(e){}
  if(ok)toast("📋 "+m);else toast("Selecciona y copia manual");ta.remove();}
$("#q").addEventListener("input",e=>{q=e.target.value;if(view!=="home"){go("home");}else goHome();});
document.addEventListener("keydown",e=>{
  if(e.target.tagName==="INPUT"||e.target.tagName==="TEXTAREA"){if(e.key==="Escape")e.target.blur();return;}
  if(e.key==="/"&&view!=="fb"){e.preventDefault();$("#q").focus();}
  if(view==="p"&&cur){if(e.key==="ArrowRight"&&D.wa[cur.idx+1])goPiece(cur.idx+1);if(e.key==="ArrowLeft"&&D.wa[cur.idx-1])goPiece(cur.idx-1);}
});
window.addEventListener("scroll",()=>{const h=document.documentElement;$("#pbar").style.width=((h.scrollTop/(h.scrollHeight-h.clientHeight)*100)||0)+"%";});
goHome();
</script></body></html>"""

html = TPL.replace("__DATA__", js).replace("__NWA__", str(len(pieces))).replace("__NFB__", str(len(fb)))
out = os.path.join(BASE, "02-ARCHIVO/catalogo-la-bandita.html")
open(out, "w", encoding="utf-8").write(html)
print("CATÁLOGO:", len(html), "bytes · WA:", len(pieces), "· FB:", len(fb))
