# -*- coding: utf-8 -*-
"""Pulso fresco lunes 19-oct-2026: API GitHub sin token (60/h). Selección prioritaria:
top-35 del censo 18-oct + pabellón de dormidos (>30d) citados en la 101 en curso."""
import urllib.request, json, time, sys
SRC="/home/user/Arena-Reimagined/02-ARCHIVO/_rearm-18oct/censo-fresco-18oct-tarde.tsv"
rows=[]
for ln in open(SRC,encoding="utf-8").read().splitlines():
    c=ln.split("\t")
    if len(c)>=5: rows.append(c)
top=sorted(rows,key=lambda c:-int(c[1]))[:35]
dorm=[c for c in rows if c[3]<"2026-09-19"]
sel={}
for c in top+dorm: sel[c[0]]=c
print(f"selección: {len(sel)} (top35={len(top)} dormidos={len(dorm)})")
out=[]; fallos=[]
for slug in sorted(sel, key=lambda s:-int(sel[s][1])):
    req=urllib.request.Request(f"https://api.github.com/repos/{slug}",headers={"User-Agent":"LaBandita-pulso-19oct","Accept":"application/vnd.github+json"})
    try:
        with urllib.request.urlopen(req,timeout=30) as r:
            d=json.load(r); rem=r.headers.get("X-RateLimit-Remaining")
        out.append([slug,str(d["stargazers_count"]),d["created_at"][:10],(d.get("pushed_at") or "")[:10],(d.get("license") or {}).get("spdx_id") or "NOASSERTION", (d.get("description") or "").replace("\t"," ").replace("\n"," ")])
        print(f"OK {slug} ★{d['stargazers_count']} push {out[-1][3]} rem={rem}")
        if rem and int(rem)<=2: print("RATE casi agotado, paro"); break
    except Exception as e:
        fallos.append((slug,str(e))); print(f"FALLO {slug}: {e}")
    time.sleep(0.3)
with open("/home/user/Arena-Reimagined/02-ARCHIVO/_rearm-19oct/censo-fresco-19oct-parcial.tsv","w",encoding="utf-8") as f:
    for r in out: f.write("\t".join(r)+"\n")
print("guardados:",len(out),"fallos:",fallos)
