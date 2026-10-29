#!/usr/bin/env python3
# PULSO 29-OCT-2026 por tandas. USO: pulso-29oct.py <inicio> <n> [lista_extra.tsv-opcional]
import json, sys, urllib.request, time
data=json.load(open("02-ARCHIVO/_rearm-29oct/mapa-recursos-29oct.json"))
mapa, censo = data["mapa"], data["censo18oct"]
orden=sorted(mapa.keys(), key=lambda s:(-len(mapa[s]), -censo.get(s,0)))
ini, n = int(sys.argv[1]), int(sys.argv[2]); sal=f"02-ARCHIVO/_rearm-29oct/pulso-29oct-{ini:03d}.tsv"
lote=orden[ini:ini+n]
if len(sys.argv)>3: lote=[l.strip() for l in open(sys.argv[3]) if l.strip()]
f=open(sal,"w",encoding="utf-8"); f.write("slug\tstars_hoy\tpush_hoy\tlic_hoy\tstars_18oct\tpiezas\n"); ok=err=0
for s in lote:
    try:
        req=urllib.request.Request(f"https://api.github.com/repos/{s}", headers={"Accept":"application/vnd.github+json","User-Agent":"labandita-pulso"})
        d=json.load(urllib.request.urlopen(req, timeout=20)); lic=(d.get("license") or {}).get("spdx_id") or "sin-licencia"
        f.write(f"{s}\t{d['stargazers_count']}\t{d['pushed_at'][:10]}\t{lic}\t{censo.get(s,'-')}\t{len(mapa.get(s,[]))}\n"); ok+=1
    except Exception as e: f.write(f"{s}\tERROR\t{e}\t\t\t\n"); err+=1
    f.flush(); time.sleep(0.3)
f.close(); print(f"{sal}: ok {ok} · errores {err}")
