# -*- coding: utf-8 -*-
"""Pulso 19-oct batch 2: dormidos restantes + no pulsados por estrellas desc. Cuota 60/h."""
import urllib.request, json, time
BASE="/home/user/Arena-Reimagined"
rows=[]
for ln in open(f"{BASE}/02-ARCHIVO/_rearm-18oct/censo-fresco-18oct-tarde.tsv",encoding="utf-8"):
    c=ln.rstrip("\n").split("\t")
    if len(c)>=5: rows.append(c)
ya=set()
for ln in open(f"{BASE}/02-ARCHIVO/_rearm-19oct/censo-fresco-19oct-parcial.tsv",encoding="utf-8"):
    ya.add(ln.split("\t")[0])
pend=[c for c in rows if c[0] not in ya]
dorm=[c for c in pend if c[3]<"2026-09-19"]
resto=sorted([c for c in pend if c[3]>="2026-09-19"], key=lambda c:-int(c[1]))
sel=dorm+resto
print(f"pendientes: {len(pend)} · dormidos cola: {len(dorm)} · tanda: {len(sel[:57])}")
out=[]; fallos=[]
for c in sel[:57]:
    slug=c[0]
    req=urllib.request.Request(f"https://api.github.com/repos/{slug}",headers={"User-Agent":"LaBandita-pulso-19oct-b2","Accept":"application/vnd.github+json"})
    try:
        with urllib.request.urlopen(req,timeout=30) as r:
            d=json.load(r); rem=r.headers.get("X-RateLimit-Remaining")
        out.append([slug,str(d["stargazers_count"]),d["created_at"][:10],(d.get("pushed_at") or "")[:10],(d.get("license") or {}).get("spdx_id") or "NOASSERTION",(d.get("description") or "").replace("\t"," ").replace("\n"," ")])
        print(f"OK {slug} ★{d['stargazers_count']} push {out[-1][3]} rem={rem}")
        if rem and int(rem)<=2: print("RATE casi agotado"); break
    except Exception as e:
        fallos.append((slug,str(e))); print("FALLO",slug,e)
    time.sleep(0.3)
with open(f"{BASE}/02-ARCHIVO/_rearm-19oct/censo-19oct-b2.tsv","w",encoding="utf-8") as f:
    for r in out: f.write("\t".join(r)+"\n")
print("guardados:",len(out),"fallos:",fallos)
