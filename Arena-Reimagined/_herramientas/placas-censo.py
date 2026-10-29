#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PLACAS DEL CENSO — genera el bloque de placas (s02-style) desde el TSV fechado.
# Ley: dato del TSV viaja FECHADO («censo de la tarde del 15-oct-2026»). Nada inventado.
import sys, csv, csv
csv.field_size_limit(10_000_000)
TSV="/home/user/Arena-Reimagined/02-ARCHIVO/censo-ecosistema-2026-10-15.tsv"
def placas(repos, nombres=None):
    rows={}
    with open(TSV,encoding='utf-8') as f:
        for r in csv.DictReader(f,delimiter='\t'):
            rows[r['repo'].lower()]=r
    out=[]
    for repo in repos:
        r=rows.get(repo.lower())
        if not r:
            print(f"NO ESTÁ EN TSV: {repo}",file=sys.stderr); continue
        nombre=(nombres or {}).get(repo, repo.split('/')[1].replace('-',' '))
        stars=int(r['stars']); push=r['push']; lic=r['licencia']
        lic_txt = lic if lic not in ('-','') else 'sin licencia declarada'
        quiet = ""
        if push < "2025-06":
            quiet=" · QUIETUD LARGA (sin empuje desde "+push+")"
        out.append((nombre,repo,stars,push,lic_txt,quiet,r.get('descripcion','')[:90]))
    return out
if __name__=="__main__":
    for p in placas(sys.argv[1:]):
        print(f"{p[0]} ({p[1]}) · ★{p[2]:,} (censo 15-oct-2026) · push {p[3]} · {p[4]}{p[5]} · {p[6]}")
