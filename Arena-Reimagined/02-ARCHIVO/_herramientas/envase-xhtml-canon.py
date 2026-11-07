# -*- coding: utf-8 -*-
"""
ENVASE XHTML CANON — herramienta de la casa (10-oct-2026)
Convierte la familia raíz de 00-CANON a envases XHTML bien formados (XML validado),
mismo diseño familiar del envase RFC v2. La fuente NUNCA se toca: se sella (sha16).
"""
import re, sys, hashlib, unicodedata, html as H
from xml.etree import ElementTree as ET
import lxml.html
from lxml import etree as LET

ROOT = "00-CANON/"
OUT = "00-CANON/_envases-xhtml/"
FECHA = "10-oct-2026"
STATS = {"huerfanos": 0}

# ───────────────────────── CSS (familia RFC, edición canon) ─────────────────────────
CSS = """
:root{--bg:#fff;--bg2:#f8f6f1;--bg3:#f0ece2;--ink:#1c1917;--mut:#6b6255;--line:#e5dfd2;
--acc:#8a6d1d;--acc2:#6b5416;--accsoft:#f6efdc;--ok:#0a7d55;--oksoft:#e7f6ef;--warnsoft:#fdf3e0;
--sans:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;
--serif:Georgia,"Iowan Old Style","Times New Roman",serif;
--mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;--rad:12px;
--shadow:0 1px 2px rgba(28,25,23,.05),0 8px 28px -18px rgba(28,25,23,.25)}
html[data-theme="dark"]{--bg:#14110b;--bg2:#1a1610;--bg3:#221d13;--ink:#ece5d4;--mut:#a89a82;
--line:#332c1e;--acc:#d4af4e;--acc2:#e5c877;--accsoft:#25200f;--ok:#3ecf9a;--oksoft:#0e2b22;
--warnsoft:#2d2210;--shadow:0 1px 2px rgba(0,0,0,.4),0 10px 32px -18px rgba(0,0,0,.7)}
@media (prefers-color-scheme:dark){html[data-theme="auto"]{--bg:#14110b;--bg2:#1a1610;--bg3:#221d13;
--ink:#ece5d4;--mut:#a89a82;--line:#332c1e;--acc:#d4af4e;--acc2:#e5c877;--accsoft:#25200f;
--ok:#3ecf9a;--oksoft:#0e2b22;--warnsoft:#2d2210;--shadow:0 1px 2px rgba(0,0,0,.4),0 10px 32px -18px rgba(0,0,0,.7)}}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.7 var(--sans);-webkit-font-smoothing:antialiased}
::selection{background:var(--accsoft)}:focus-visible{outline:2px solid var(--acc);outline-offset:2px}
a{color:var(--acc);text-decoration:none;border-bottom:1px solid color-mix(in srgb,var(--acc) 35%,transparent)}
code,kbd{font-family:var(--mono);font-size:.9em}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
.skip{position:fixed;top:-48px;left:16px;z-index:99;background:var(--acc);color:#fff;padding:8px 14px;border-radius:8px;transition:top .2s}
.skip:focus{top:12px}
#progress{position:fixed;top:0;left:0;right:0;height:3px;z-index:60}#progress i{display:block;height:100%;width:0;background:linear-gradient(90deg,var(--acc),var(--acc2))}
.mast{border-bottom:1px solid var(--line);background:var(--bg2);background-image:linear-gradient(180deg,color-mix(in srgb,var(--acc) 8%,var(--bg2)),var(--bg2) 72%)}
.mast-in{max-width:1240px;margin:0 auto;padding:32px 24px 24px}
.rfc-badge{display:inline-flex;align-items:center;gap:10px;font:600 12px/1 var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--acc);border:1px solid color-mix(in srgb,var(--acc) 45%,transparent);padding:7px 12px;border-radius:999px;background:var(--accsoft)}
.rfc-badge .dot{width:7px;height:7px;border-radius:50%;background:var(--ok);box-shadow:0 0 0 3px color-mix(in srgb,var(--ok) 25%,transparent)}
h1{font-family:var(--serif);font-size:clamp(25px,3.8vw,40px);line-height:1.15;letter-spacing:-.015em;margin:16px 0 8px;font-weight:800}
.subtitle{font-size:clamp(15px,2vw,19px);color:var(--mut);margin:0 0 10px;font-style:italic;font-family:var(--serif)}
.metagrid{display:flex;flex-wrap:wrap;gap:10px;margin-top:18px}
.meta{border:1px solid var(--line);background:var(--bg);border-radius:10px;padding:9px 13px}
.meta b{display:block;font:700 10.5px/1.3 var(--mono);letter-spacing:.13em;text-transform:uppercase;color:var(--mut);margin-bottom:3px}
.meta span{font-size:13.5px;line-height:1.5;display:block}
.toolbar{display:flex;gap:8px;flex-wrap:wrap;margin-top:20px}
.btn{appearance:none;border:1px solid var(--line);background:var(--bg);color:var(--ink);font:600 13px/1 var(--sans);padding:9px 14px;border-radius:9px;cursor:pointer;display:inline-flex;align-items:center;gap:7px}
.btn:hover{border-color:var(--acc);color:var(--acc)}
.btn kbd{font:600 10.5px/1 var(--mono);border:1px solid var(--line);border-bottom-width:2px;border-radius:5px;padding:2.5px 5px;color:var(--mut)}
.btn.icon{padding:9px 11px}
.shell{max-width:1240px;margin:0 auto;padding:32px 24px 80px;display:grid;grid-template-columns:270px minmax(0,1fr);gap:44px;align-items:start}
nav.toc{position:sticky;top:20px;max-height:calc(100vh - 40px);overflow:auto;font-size:13px;scrollbar-width:thin}
nav.toc h2{font:700 11px/1 var(--mono);letter-spacing:.15em;text-transform:uppercase;color:var(--mut);margin:4px 0 12px}
nav.toc ol{list-style:none;margin:0;padding:0;border-left:1px solid var(--line)}
nav.toc li a{display:block;padding:5px 14px;border-left:2px solid transparent;margin-left:-1.5px;color:var(--mut);border-bottom:none;line-height:1.4}
nav.toc li a:hover{color:var(--ink);background:var(--bg2)}
nav.toc li a[aria-current="true"]{color:var(--acc);border-left-color:var(--acc);font-weight:650;background:linear-gradient(90deg,var(--accsoft),transparent)}
nav.toc ol ol{padding-left:12px}nav.toc ol ol li a{font-size:12px;padding:3px 10px}
.toc-foot{margin-top:14px;font-size:12px;color:var(--mut);line-height:1.6;border-top:1px solid var(--line);padding-top:12px}
main{min-width:0;overflow-wrap:break-word}
section.sec{scroll-margin-top:18px;margin:0 0 44px}
section.flash{animation:flash 1.6s ease-out}
@keyframes flash{0%{box-shadow:0 0 0 3px var(--accsoft);background:var(--accsoft);border-radius:14px}100%{background:transparent}}
.sechead{display:flex;align-items:baseline;gap:12px;border-bottom:1px solid var(--line);padding-bottom:9px;margin-bottom:15px}
.kick{font:700 11.5px/1 var(--mono);letter-spacing:.1em;color:var(--acc);text-transform:uppercase;white-space:nowrap}
.sechead h2{font-family:var(--serif);font-size:clamp(18px,2.2vw,23px);margin:0;letter-spacing:-.01em;font-weight:750}
.sechead .al{margin-left:auto;font:700 13px/1 var(--mono);color:var(--mut);border:none}
.sechead .al:hover{color:var(--acc)}
h3{font-family:var(--serif);font-size:17px;margin:22px 0 8px}h4{font-size:15px;margin:18px 0 6px;color:var(--ink)}
.sec-body{font-family:var(--serif);font-size:16.5px;line-height:1.78}
.sec-body p{margin:0 0 13px}
.sec-body ul,.sec-body ol{margin:0 0 14px;padding-left:26px}
.sec-body li{margin:4px 0}
.sec-body blockquote{border:1px solid var(--line);border-left:3px solid var(--acc);background:var(--bg2);padding:12px 16px;border-radius:0 var(--rad) var(--rad) 0;margin:14px 0;color:var(--ink)}
.sec-body blockquote p{margin:0 0 8px}.sec-body blockquote p:last-child{margin:0}
.sec-body pre{background:#171310;color:#e9dfc8;border:1px solid #2e2618;border-radius:var(--rad);padding:14px 16px;overflow-x:auto;font-size:13px;line-height:1.6;margin:14px 0}
.sec-body pre code{background:none;border:none;padding:0;color:inherit}
.sec-body code{background:var(--bg3);border:1px solid var(--line);border-radius:5px;padding:1px 5px}
.sec-body hr{border:none;border-top:1px solid var(--line);margin:22px auto;width:60%}
.tw{overflow-x:auto;margin:14px 0;border:1px solid var(--line);border-radius:var(--rad);box-shadow:var(--shadow)}
table{border-collapse:collapse;width:100%;font-size:14px;font-family:var(--sans);background:var(--bg)}
th{font:700 11px/1.4 var(--mono);letter-spacing:.09em;text-transform:uppercase;color:var(--mut);text-align:left;background:var(--bg2);padding:10px 13px;border-bottom:1px solid var(--line)}
td{padding:9px 13px;border-bottom:1px solid var(--line);vertical-align:top}
tr:last-child td{border-bottom:none}tbody tr:hover td{background:var(--bg2)}
td.c,th.c{text-align:center}td.r,th.r{text-align:right}
td code{white-space:nowrap}
code{overflow-wrap:anywhere}
#searchov{position:fixed;inset:0;background:color-mix(in srgb,var(--ink) 38%,transparent);z-index:80;display:none;backdrop-filter:blur(2px)}
#searchov.open{display:block}
.searchpanel{max-width:640px;margin:9vh auto 0;background:var(--bg);border:1px solid var(--line);border-radius:16px;box-shadow:0 24px 70px -20px rgba(0,0,0,.5);overflow:hidden}
.searchpanel header{display:flex;align-items:center;gap:10px;padding:13px 16px;border-bottom:1px solid var(--line)}
.searchpanel input{flex:1;border:none;background:none;color:var(--ink);font:500 16px/1.4 var(--sans);outline:none}
.searchpanel .esc{font:600 10.5px/1 var(--mono);border:1px solid var(--line);border-radius:5px;padding:4px 7px;color:var(--mut)}
#sres{max-height:52vh;overflow:auto}
#sres .si{display:block;width:100%;text-align:left;background:none;border:none;border-bottom:1px solid var(--line);padding:11px 16px;cursor:pointer;color:var(--ink);font-family:var(--sans)}
#sres .si:hover,#sres .si:focus{background:var(--bg2)}
#sres .si b{display:block;font-size:13.5px;color:var(--acc);margin-bottom:2px}
#sres .si span{font-size:12.5px;color:var(--mut);display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
#sres .none{padding:18px 16px;color:var(--mut);font-size:13.5px;font-style:italic}
.searchpanel footer{padding:9px 16px;font-size:11.5px;color:var(--mut);border-top:1px solid var(--line);background:var(--bg2)}
mark[data-hit]{background:color-mix(in srgb,var(--acc) 34%,transparent);color:inherit;border-radius:3px;padding:0 1px}
.colophon-notes{font-family:var(--sans)!important;font-size:13.5px!important;color:var(--mut)}
footer.foot{border-top:1px solid var(--line);background:var(--bg2)}
.foot-in{max-width:1240px;margin:0 auto;padding:24px;display:flex;flex-wrap:wrap;gap:14px;align-items:center;justify-content:space-between;font-size:13px;color:var(--mut)}
.foot .seal{font-family:var(--mono);font-size:12px}
#toast{position:fixed;left:50%;bottom:26px;transform:translateX(-50%) translateY(20px);background:var(--ink);color:var(--bg);padding:10px 18px;border-radius:10px;font-size:13px;font-weight:600;opacity:0;pointer-events:none;transition:all .25s;z-index:90}
#toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
#totop{position:fixed;right:22px;bottom:22px;width:42px;height:42px;border-radius:12px;border:1px solid var(--line);background:var(--bg);color:var(--mut);font-size:17px;cursor:pointer;opacity:0;pointer-events:none;transition:opacity .2s;z-index:70}
#totop.show{opacity:1;pointer-events:auto}#totop:hover{color:var(--acc);border-color:var(--acc)}
@media (max-width:960px){.shell{grid-template-columns:1fr;gap:10px;padding-top:18px}
nav.toc{position:static;max-height:none;border:1px solid var(--line);border-radius:var(--rad);padding:14px 16px;background:var(--bg2)}
nav.toc ol{columns:2;column-gap:22px;border:none}nav.toc li{break-inside:avoid}
.sechead{flex-wrap:wrap}.kick{white-space:normal;overflow-wrap:anywhere}h1,h2{overflow-wrap:anywhere}}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*,*::before,*::after{animation:none!important;transition:none!important}}
@media print{#progress,nav.toc,.toolbar,#totop,#searchov{display:none!important}
body{font:11pt/1.5 Georgia,serif;color:#000;background:#fff}.shell{display:block;max-width:none;padding:0}
section.sec{margin:0 0 24px}.tw,.sec-body blockquote,.sec-body pre{box-shadow:none;break-inside:avoid}
a{color:#000;border:none}.mast{background:#fff}section.flash{animation:none}}
"""

# ───────────────────────── JS (CDATA) ─────────────────────────
JS = r"""
(function(){
"use strict";
var d=document,w=window,root=d.documentElement;
function $(s,c){return (c||d).querySelector(s)}
function $$(s,c){return Array.prototype.slice.call((c||d).querySelectorAll(s))}
function esc(s){return s.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;")}
function store(){try{return w.localStorage}catch(e){return null}}
var toastT;
function toast(m){var t=$("#toast");t.textContent=m;t.classList.add("show");clearTimeout(toastT);toastT=setTimeout(function(){t.classList.remove("show")},1900)}
var THEMES=["auto","light","dark"];
function setTheme(t){root.setAttribute("data-theme",t);var l=$("#thlab");if(l)l.textContent=t;var m=$('meta[name="theme-color"]');if(m)m.setAttribute("content",t==="light"?"#ffffff":"#14110b");var s=store();if(s)try{s.setItem("canon-theme",t)}catch(e){}}
var savedT=null,st=store();if(st)try{savedT=st.getItem("canon-theme")}catch(e){}
setTheme(THEMES.indexOf(savedT)>-1?savedT:"auto");
$("#btheme").addEventListener("click",function(){var c=root.getAttribute("data-theme")||"auto";setTheme(THEMES[(THEMES.indexOf(c)+1)%3]);toast("Tema: "+root.getAttribute("data-theme"))});
var secs=$$("main section.sec"),list=$("#toclist");
secs.forEach(function(sec){
  var li=d.createElement("li"),a=d.createElement("a");
  a.href="#"+sec.id;
  a.textContent=sec.getAttribute("data-nav")||sec.id;
  if(sec.getAttribute("data-sub")==="1"){a.style.fontSize="12px";a.style.paddingLeft="26px"}
  li.appendChild(a);list.appendChild(li);
});
var links={};$$("nav.toc a").forEach(function(a){links[a.getAttribute("href").slice(1)]=a});
function spy(id){Object.keys(links).forEach(function(k){if(links[k])links[k].setAttribute("aria-current",k===id?"true":"false")})}
if("IntersectionObserver" in w){
  var vis={};
  var io=new IntersectionObserver(function(es){
    es.forEach(function(e){vis[e.target.id]=e.isIntersecting});
    var best=null;
    secs.forEach(function(sec){if(vis[sec.id]&&best===null)best=sec.id});
    if(best)spy(best);
  },{rootMargin:"-10% 0px -76% 0px",threshold:0});
  secs.forEach(function(sec){io.observe(sec)});
}
spy(secs.length?secs[0].id:null);
var bar=$("#progress i"),tt=$("#totop"),tick=false;
function onScroll(){
  var h=d.documentElement,st2=w.scrollY||h.scrollTop;
  var max=(h.scrollHeight-h.clientHeight)||1;
  bar.style.width=Math.min(100,st2/max*100).toFixed(2)+"%";
  tt.classList.toggle("show",st2>700);
  tick=false;
}
w.addEventListener("scroll",function(){if(!tick){tick=true;requestAnimationFrame(onScroll)}},{passive:true});
onScroll();
tt.addEventListener("click",function(){w.scrollTo({top:0,behavior:"smooth"})});
var ov=$("#searchov"),inp=$("#sinput"),res=$("#sres"),INDEX=[];
secs.forEach(function(sec){
  INDEX.push({id:sec.id,label:sec.getAttribute("data-nav")||sec.id,text:sec.textContent.replace(/\s+/g," ").toLowerCase()});
});
var marks=[];
function clearMarks(){marks.forEach(function(m){var p=m.parentNode;if(p){p.replaceChild(d.createTextNode(m.textContent),m);p.normalize()}});marks=[]}
function markIn(sec,q){
  var body=$(".sec-body",sec)||sec;
  var walker=d.createTreeWalker(body,NodeFilter.SHOW_TEXT,{acceptNode:function(n){
    if(!n.nodeValue||!n.nodeValue.trim())return NodeFilter.FILTER_REJECT;
    var p=n.parentNode;return (p&&(p.nodeName==="SCRIPT"||p.nodeName==="STYLE"||p.nodeName==="MARK"))?NodeFilter.FILTER_REJECT:NodeFilter.FILTER_ACCEPT;
  }});
  var nodes=[],n;while(n=walker.nextNode())nodes.push(n);
  var ql=q.toLowerCase(),count=0;
  nodes.forEach(function(node){
    if(count>=30)return;
    var txt=node.nodeValue,low=txt.toLowerCase(),idx=low.indexOf(ql);
    if(idx<0)return;
    var frag=d.createDocumentFragment(),pos=0,hit;
    while((hit=low.indexOf(ql,pos))>-1&&count<30){
      if(hit>pos)frag.appendChild(d.createTextNode(txt.slice(pos,hit)));
      var mk=d.createElement("mark");mk.setAttribute("data-hit","");mk.textContent=txt.slice(hit,hit+q.length);
      frag.appendChild(mk);marks.push(mk);count++;
      pos=hit+q.length;
    }
    if(pos<txt.length)frag.appendChild(d.createTextNode(txt.slice(pos)));
    if(pos>0)node.parentNode.replaceChild(frag,node);
  });
}
function openSearch(){ov.classList.add("open");inp.value="";res.innerHTML='<div class="none">Escribe para buscar en '+INDEX.length+' secciones…</div>';inp.focus()}
function closeSearch(){ov.classList.remove("open");clearMarks()}
$("#bsearch").addEventListener("click",openSearch);
ov.addEventListener("click",function(e){if(e.target===ov)closeSearch()});
inp.addEventListener("input",function(){
  var q=inp.value.trim().toLowerCase();
  clearMarks();
  if(q.length<2){res.innerHTML='<div class="none">Escribe al menos 2 caracteres…</div>';return}
  var scored=[];
  INDEX.forEach(function(s){
    var hits=0,i=s.text.indexOf(q),first=-1;
    while(i>-1&&hits<50){if(first<0)first=i;hits++;i=s.text.indexOf(q,i+q.length)}
    if(s.label.toLowerCase().indexOf(q)>-1)hits+=12;
    if(hits>0)scored.push({s:s,hits:hits,first:first});
  });
  scored.sort(function(a,b){return b.hits-a.hits});
  if(!scored.length){res.innerHTML='<div class="none">Sin coincidencias para «'+esc(q)+'».</div>';return}
  res.innerHTML="";
  scored.slice(0,9).forEach(function(r){
    var pos=Math.max(0,r.first-60),snip=r.s.text.substr(pos,150).split(q).join("«"+q+"»");
    var b=d.createElement("button");b.type="button";b.className="si";
    b.innerHTML="<b>"+esc(r.s.label)+"</b><span>…"+esc(snip)+"…</span>";
    b.addEventListener("click",function(){
      closeSearch();
      var sec=d.getElementById(r.s.id);
      markIn(sec,inp.value.trim());
      sec.scrollIntoView({behavior:"smooth",block:"start"});
      sec.classList.remove("flash");void sec.offsetWidth;sec.classList.add("flash");
    });
    res.appendChild(b);
  });
});
inp.addEventListener("keydown",function(e){
  if(e.key==="Enter"){var f=$(".si",res);if(f)f.click()}
});
d.addEventListener("keydown",function(e){
  var tag=(e.target.tagName||"").toLowerCase(),typing=tag==="input"||tag==="textarea"||tag==="select";
  if(e.key==="Escape"){if(ov.classList.contains("open"))closeSearch();return}
  if(typing)return;
  if(e.key==="/"||(e.key==="k"&&(e.ctrlKey||e.metaKey))){e.preventDefault();openSearch()}
  if(e.key==="t"){$("#btheme").click()}
});
$("#bprint").addEventListener("click",function(){clearMarks();w.print()});
w.addEventListener("beforeprint",function(){clearMarks()});
})();
"""

RESERVED={"progress","contenido","toclist","colofon","searchov","sinput","sres","toast",
"totop","bsearch","btheme","bprint","thlab","foot","mast","shell"}

def slug(t, used):
    s = unicodedata.normalize("NFKD", t)
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:48] or "sec"
    base, i = s, 2
    while s in used:
        s = "%s-%d" % (base, i); i += 1
    used.add(s)
    return s

def esc(t): return H.escape(t, quote=True)

def inline(t):
    out, parts = [], t.split("`")
    for i, chunk in enumerate(parts):
        c = esc(chunk)
        if i % 2 == 1:
            out.append("<code>%s</code>" % c); continue
        c = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", c)
        c = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", c)
        if "**" in c:  # huérfanos del autor: se limpian del envase (la fuente no se toca)
            STATS["huerfanos"] += c.count("**")
            c = c.replace("**", "")
        c = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+|#[^)\s]*)\)", r'<a href="\2">\1</a>', c)
        out.append(c)
    return "".join(out)

def render_md(text):
    """markdown de la casa → lista de secciones (id, kick, título, sub, html) + título doc."""
    lines = text.split("\n")
    used, secs, title = set(RESERVED), [], None
    cur = None  # [titulo, html_list, sub]
    def close():
        nonlocal cur
        if cur is not None:
            sid = slug(cur[0], used)
            secs.append({"id": sid, "kick": cur[3], "title": cur[0], "sub": cur[4],
                         "html": "".join(cur[1])})
        cur = None
    i, n = 0, len(lines)
    sec_n = 0
    while i < n:
        ln = lines[i]
        m = re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", ln)
        if m:
            lvl = len(m.group(1)); txt = m.group(2).strip()
            if lvl == 1 and title is None:
                title = txt; i += 1; continue
            if lvl == 1:  # h1 posterior → cierre y trátalo como h2
                close()
            if lvl <= 2:
                close()
                sec_n += 1
                cur = [txt, [], "", "%02d" % sec_n, "0"]
            else:
                if cur is None:
                    close(); sec_n += 1
                    cur = ["Apertura", [], "", "%02d" % sec_n, "0"]
                # FIX 2.4: los h3-h6 interiores TAMBIÉN llevan id (mismo slugger, mismo `used`
                # en orden de documento) → el envase resuelve TODOS los targets del fuente.
                cur[1].append('<h3 id="%s">%s</h3>' % (slug(txt, used), inline(txt)))
            i += 1; continue
        if cur is None:
            sec_n += 1
            cur = ["Apertura", [], "", "%02d" % sec_n, "0"]
        # bloque de código
        if re.match(r"^```", ln):
            buf = []
            i += 1
            while i < n and not re.match(r"^```", lines[i]):
                buf.append(lines[i]); i += 1
            i += 1
            cur[1].append("<pre><code>%s</code></pre>" % esc("\n".join(buf)))
            continue
        # tabla
        if re.match(r"^\s*\|.*\|\s*$", ln) and i + 1 < n and re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
            rows = []
            while i < n and re.match(r"^\s*\|.*\|\s*$", lines[i]):
                rows.append(lines[i]); i += 1
            head = [c.strip() for c in rows[0].strip().strip("|").split("|")]
            aligns = []
            for c in rows[1].strip().strip("|").split("|"):
                c = c.strip()
                aligns.append("c" if c.startswith(":") and c.endswith(":") else ("r" if c.endswith(":") else ""))
            body_rows = rows[2:]
            x = ['<div class="tw"><table><thead><tr>']
            for k, cell in enumerate(head):
                x.append('<th%s scope="col">%s</th>' % (' class="%s"' % aligns[k] if aligns[k] else "", inline(cell)))
            x.append("</tr></thead><tbody>")
            for r in body_rows:
                cells = [c.strip() for c in r.strip().strip("|").split("|")]
                x.append("<tr>")
                for k, cell in enumerate(cells):
                    a = aligns[k] if k < len(aligns) else ""
                    x.append('<td%s>%s</td>' % (' class="%s"' % a if a else "", inline(cell)))
                x.append("</tr>")
            x.append("</tbody></table></div>")
            cur[1].append("".join(x))
            continue
        # hr
        if re.match(r"^\s*([-*_])\1{2,}\s*$", ln):
            cur[1].append("<hr/>"); i += 1; continue
        # cita
        if re.match(r"^\s*>\s?", ln):
            buf = []
            while i < n and re.match(r"^\s*>\s?", lines[i]):
                buf.append(re.sub(r"^\s*>\s?", "", lines[i])); i += 1
            paras, acc = [], []
            for b in buf:
                if not b.strip():
                    if acc: paras.append(" ".join(acc)); acc = []
                else: acc.append(b.strip())
            if acc: paras.append(" ".join(acc))
            cur[1].append("<blockquote>%s</blockquote>" % "".join("<p>%s</p>" % inline(p) for p in paras))
            continue
        # listas (anidadas por sangría)
        m2 = re.match(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$", ln)
        if m2:
            def close_stack(stack, depth):
                while stack and len(stack) > depth:
                    t_ = stack.pop()
                    cur[1].append("</li></%s>" % t_[0])
            stack = []  # [(tipo, indent)]
            def open_item(type_, depth, content):
                cur[1].append("<%s><li>%s" % (type_, inline(content)))
            while i < n:
                mm = re.match(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$", lines[i])
                if not mm:
                    # continuación con sangría del ítem abierto (lazy continuation)
                    ln2 = lines[i]
                    if stack and ln2.strip() and not re.match(r"^(#{1,6}\s|```|\s*>|\s*\||\s*([-*_])\2{2,}\s*$)", ln2):
                        cur[1][-1] += " " + inline(ln2.strip())
                        i += 1
                        continue
                    break
                ind = len(mm.group(1))
                type_ = "ol" if mm.group(2)[0].isdigit() else "ul"
                depth = ind // 2 + 1
                if not stack:
                    carry = False
                    if cur[1]:
                        mlast = re.search(r"</li></(ol|ul)>\Z", cur[1][-1])
                        if mlast and mlast.group(1) == type_:
                            cur[1][-1] = re.sub(r"</%s>\Z" % type_, "", cur[1][-1])
                            carry = True
                    if not carry:
                        cur[1].append("<%s>" % type_)
                    stack.append((type_, depth))
                elif depth > stack[-1][1]:
                    stack.append((type_, depth)); cur[1].append("<%s>" % type_)
                elif depth < stack[-1][1]:
                    close_stack(stack, depth)
                    if stack and stack[-1][0] != type_:
                        cur[1].append("</li></%s><%s>" % (stack.pop()[0], type_))
                        stack.append((type_, depth))
                    cur[1].append("</li>")
                else:
                    if stack[-1][0] != type_:
                        cur[1].append("</li></%s><%s>" % (stack.pop()[0], type_))
                        stack.append((type_, depth))
                    else:
                        cur[1].append("</li>")
                cur[1].append("<li>%s" % inline(mm.group(3)))
                i += 1
            close_stack(stack, 0)
            if stack: cur[1].append("</li></%s>" % stack.pop()[0])
            continue
        # párrafo
        buf = []
        while i < n and lines[i].strip() and not re.match(r"^(#{1,6}\s|```|\s*>|\s*[-*+]\s|\s*\d+[.)]\s|\s*\||\s*([-*_])\2{2,}\s*$)", lines[i]):
            buf.append(lines[i].strip()); i += 1
        if buf:
            cur[1].append("<p>%s</p>" % inline(" ".join(buf)))
        else:
            i += 1
    close()
    return title or "Documento", secs

def tidy_old_html(path):
    """HTML viejo → (título, html interno con ids en headings)."""
    raw = open(path, encoding="utf-8").read()
    doc = lxml.html.fromstring(raw)
    title = doc.findtext(".//title") or "Documento"
    used = set(RESERVED)
    # FIX 3.x (batería móvil): tablas del HTML legacy reciben el MISMO wrapper .tw que las
    # tablas md → overflow-x interno, el documento nunca se expande (nada se oculta ni trunca).
    for t in list(doc.iter("table")):
        div = t.makeelement("div", {"class": "tw"})
        t.addprevious(div)
        div.append(t)
    for h in doc.iter("h1", "h2", "h3", "h4"):
        txt = h.text_content().strip()
        if not txt: continue
        if h.get("id"):
            # FIX H#2 (nano-lote 2.4): id nativo del fuente SE PRESERVA (p.ej. pillars/ops/puerta)
            used.add(h.get("id"))
            continue
        h.set("id", "h-" + slug(txt, used))
    body = doc.body if doc.body is not None else doc
    inner = []
    for child in body:
        inner.append(LET.tostring(child, method="xml", encoding="unicode"))
    return title.strip(), "".join(inner)

def build_doc(fname, badge, subtitle_label):
    path = ROOT + fname
    raw = open(path, "rb").read()
    sha16 = hashlib.sha256(raw).hexdigest()[:16]
    text = raw.decode("utf-8")
    if fname.endswith(".md"):
        title, secs = render_md(text)
    else:
        title, inner = tidy_old_html(path)
        text = re.sub(r"<[^>]+>", " ", text)  # palabras sobre texto visible
        sid = slug(title, set())
        secs = [{"id": sid, "kick": "01", "title": title, "sub": "0", "html": inner}]
    nwords = len(re.findall(r"\S+", text))
    ntables = len(re.findall(r"(?m)^\s*\|.*\|\s*$", text))
    toc_sub = len(secs) <= 26  # h3 anidados solo en docs pequeños
    used = {s["id"] for s in secs}
    # TOC
    toc = []
    for s in secs:
        toc.append('<li><a href="#%s">%s</a></li>' % (s["id"], esc(s["title"][:90])))
    # cuerpo
    body = []
    for s in secs:
        body.append(
            '<section class="sec" id="%s" data-nav="%s" data-sub="%s">'
            '<div class="sechead"><span class="kick">%s · %s</span><h2>%s</h2>'
            '<a class="al" href="#%s" aria-label="Enlace a sección">#</a></div>'
            '<div class="sec-body">%s</div></section>'
            % (s["id"], esc(s["title"][:90]), s["sub"], s["kick"],
               esc(subtitle_label), esc(s["title"]), s["id"], s["html"]))
    nsec = len(secs)
    colophon = (
        '<p><strong>Fuente sellada:</strong> <code>%s</code> — SHA-256 <code>%s</code>. '
        'El envase no toca la fuente: el texto va íntegro y verbatim.</p>'
        '<p><strong>Edición:</strong> XHTML bien formado (validado XML, espacio de nombres '
        '<code>http://www.w3.org/1999/xhtml</code>), autocontenido: cero recursos externos, cero '
        'peticiones de red; rinde offline y en impresión/PDF. Navegación: <code>/</code> busca, '
        '<code>t</code> tema, <code>Esc</code> cierra.</p>'
        '<p><strong>Cifras medidas:</strong> %s secciones · %s palabras · %s líneas de tabla · '
        'envase del %s.</p>'
        % (fname, sha16, nsec, "{:,}".format(nwords).replace(",", "."), "{:,}".format(ntables).replace(",", "."), FECHA))
    body.append(
        '<section class="sec" id="colofon" data-nav="Colofón del envase" data-sub="0">'
        '<div class="sechead"><span class="kick">✦ · Colofón</span><h2>Sobre este envase</h2>'
        '<a class="al" href="#colofon">#</a></div>'
        '<div class="sec-body colophon-notes">%s</div></section>' % colophon)
    doc = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="es" xml:lang="es">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<meta name="color-scheme" content="light dark"/>
<meta name="robots" content="noindex"/>
<meta name="theme-color" content="#14110b"/>
<title>%s — Canon La Bandita</title>
<style type="text/css">/* <![CDATA[ */%s/* ]]> */</style>
</head>
<body>
<a class="skip" href="#contenido">Saltar al contenido</a>
<div id="progress" role="progressbar" aria-label="Progreso de lectura"><i></i></div>
<header class="mast">
  <div class="mast-in">
    <span class="rfc-badge"><span class="dot"></span>%s</span>
    <h1>%s</h1>
    <p class="subtitle">%s</p>
    <div class="metagrid">
      <div class="meta"><b>Fuente sellada</b><span><code>%s</code> · sha16 <code>%s</code></span></div>
      <div class="meta"><b>Edición</b><span>XHTML bien formado · validado XML · %s</span></div>
      <div class="meta"><b>Corpus</b><span>%s secciones · %s palabras · texto verbatim íntegro</span></div>
      <div class="meta"><b>Red</b><span>0 recursos externos · 0 peticiones · offline</span></div>
    </div>
    <div class="toolbar">
      <button class="btn" id="bsearch" type="button">⌕ Buscar <kbd>/</kbd></button>
      <button class="btn icon" id="btheme" type="button" title="Tema: auto / claro / oscuro">◐ <span id="thlab">auto</span></button>
      <button class="btn icon" id="bprint" type="button" title="Imprimir / PDF">⎙</button>
    </div>
  </div>
</header>
<div class="shell">
<nav class="toc" aria-label="Índice">
  <h2>Índice</h2>
  <ol id="toclist">%s</ol>
  <p class="toc-foot">Envase autocontenido — 0 peticiones de red.<br/>Teclado: <code>/</code> buscar · <code>t</code> tema · <code>Esc</code> cerrar</p>
</nav>
<main id="contenido">
%s
</main>
</div>
<footer class="foot"><div class="foot-in">
<span><strong>Canon La Bandita</strong> — %s · envase %s</span>
<span class="seal">sha256:<code>%s</code></span>
</div></footer>
<div id="searchov" role="dialog" aria-modal="true" aria-label="Buscar en el documento">
  <div class="searchpanel">
    <header><span>⌕</span><input id="sinput" type="search" placeholder="Buscar en este tomo…" autocomplete="off" aria-label="Búsqueda"/><span class="esc">Esc</span></header>
    <div id="sres" aria-live="polite"></div>
    <footer>Enter — ir a la primera coincidencia · las coincidencias se resaltan en el sitio</footer>
  </div>
</div>
<div id="toast" role="status" aria-live="polite"></div>
<button id="totop" type="button" aria-label="Volver arriba">↑</button>
<script type="text/javascript">//<![CDATA[%s//]]></script>
</body>
</html>
""" % (esc(title), CSS, badge, esc(title), subtitle_label, fname, sha16, FECHA,
       nsec, "{:,}".format(nwords).replace(",", "."), "".join(toc), "".join(body),
       esc(subtitle_label), FECHA, sha16, JS)
    # veredicto CDATA: sin "]]>" accidental
    assert "]]>" not in doc.replace("]]>", ""), "CDATA roto"
    assert doc.count("]]>") == 2, "CDATA wrappers != 2: %d" % doc.count("]]>")
    # FIX 2.4b: el TÍTULO del documento lleva id de ancla (el TOC del fuente puede apuntarle);
    # si la pieza html ya lo trae como id de su sección única, no se duplica.
    tsid = slug(title, set())
    if 'id="%s"' % tsid not in doc:
        doc = doc.replace("<h1>%s</h1>" % esc(title), '<h1 id="%s">%s</h1>' % (tsid, esc(title)), 1)
    return doc, sha16, nsec

def validate(doc, sha16, name):
    root = ET.fromstring(doc.encode("utf-8"))  # XML bien formado o aborta
    ns = "{http://www.w3.org/1999/xhtml}"
    ids = [e.get("id") for e in root.iter() if e.get("id")]
    assert len(ids) == len(set(ids)), "ids duplicados en " + name
    # recursos externos prohibidos
    for e in root.iter():
        for attr in ("src", "href"):
            v = e.get(attr, "")
            if v.startswith(("http://", "https://", "//")) and e.tag != ns + "a":
                raise AssertionError("recurso externo %s en %s" % (v[:60], name))
    # fugas markdown en texto visible (excluye pre/code/style/script: ahí el marcado es literal)
    SKIP={ns+"pre",ns+"code",ns+"style",ns+"script"}
    parts=[]
    def walk(e):
        if e.tag in SKIP: return
        if e.text: parts.append(e.text)
        for ch in e:
            walk(ch)
            if ch.tail: parts.append(ch.tail)
    walk(root)
    text = " ".join(t.strip() for t in parts)
    leaks = re.findall(r"\*\*[^*]+\*\*|^#{1,6} ", text, re.M)
    assert not leaks, "fuga markdown en %s: %s" % (name, leaks[:3])
    assert sha16 in doc, "sello ausente en " + name
    # R-01: sin metadatos de generación en la PLUMA del envase (el corpus verbatim habla de IA por doctrina propia)
    colo = root.find(".//%ssection[@id='colofon']" % ns)
    ct = " ".join(colo.itertext()).lower() if colo is not None else text.lower()
    assert "generado por" not in ct and "generated by" not in ct, "metadato IA en colofón"
    return len(ids)

SPECS = [
    ("TRATADO.md", "TRATADO.md", "CANON LA BANDITA · TRATADO · V.0.05 · EDICIÓN XHTML",
     "Fusión Universal — Edición Dominicana Revisada"),
    ("MANUAL-COMPLETO.md", "MANUAL-COMPLETO.md", "CANON LA BANDITA · MANUAL DE CAMPO · V2.1 · EDICIÓN XHTML",
     "Manual de Campo — Edición Completa"),
    ("LECCIONES-ALEXIS.md", "LECCIONES-ALEXIS.md", "CANON LA BANDITA · LECCIONES DE ALEXIS · EDICIÓN XHTML",
     "Para recordar entre sesiones"),
    ("CANON-CIMIENTO-V28sep.html", "CANON-CIMIENTO.html", "CANON LA BANDITA · CANON-CIMIENTO · EDICIÓN XHTML",
     "Canon-Cimiento — re-envasado desde la edición V28sep"),
    ("COMPENDIO-INTEGRAL-LibroE-V26sep.html", "COMPENDIO-INTEGRAL.html", "CANON LA BANDITA · COMPENDIO INTEGRAL · EDICIÓN XHTML",
     "Compendio Integral Libro E — re-envasado desde la edición V26sep"),
]

def main():
    import os
    os.makedirs(OUT, exist_ok=True)
    print("%-40s %10s %9s %8s %6s  %s" % ("DOC", "bytes", "sha16", "secc", "ids", "veredicto"))
    total = 0
    for fname, outname, badge, sub in SPECS:
        doc, sha16, nsec = build_doc(fname, badge, sub)
        nids = validate(doc, sha16, outname)
        out = OUT + outname.replace(".md", "").replace(".html", "") + "-envase-XHTML-2026-10-10.xhtml"
        open(out, "w", encoding="utf-8").write(doc)
        nbytes = len(doc.encode("utf-8"))
        total += nbytes
        print("%-40s %10d %9s %8d %6d  OK ✓" % (out.split("/")[-1], nbytes, sha16, nsec, nids))
    print("TOTAL envases: %d bytes en %d piezas" % (total, len(SPECS)))

if __name__ == "__main__":
    main()
