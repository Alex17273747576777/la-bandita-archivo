#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cifras.py · todas las cifras de la pieza 19 v2, sacadas de los datos, no de la memoria."""
import json, pathlib

RAIZ = pathlib.Path(__file__).resolve().parents[3]
TIENDAS = json.loads((RAIZ / "docs/AUDITORIA-TIENDAS-2026-11-05.json").read_text(encoding="utf-8"))
APPS = json.loads((RAIZ / "docs/MEDICION-19b-apps-2026-11-05.json").read_text(encoding="utf-8"))

print("TIENDAS · %d repositorios clonados" % len(TIENDAS))
total = 0
for t in sorted(TIENDAS, key=lambda x: -x["extensiones"]):
    firma = "sí" if (t.get("trazas") or {}).get("firma") else ("catálogo" if t.get("firma_en_catalogo") else "no")
    total += t["extensiones"] if t["veredicto"] != "NO" else 0
    print("  %-42s %-12s ext=%-5s firma=%-8s %s" % (t["repo"], t["veredicto"], t["extensiones"], firma,
                                                     " · ".join(t["motivos"])))
print("  suma de las que sirven:", total, "(la pieza usa 2.382 con LNReader contado por archivos)")

print("\nAPLICACIONES")
for k, v in APPS.items():
    if k.startswith("_"):
        print("  " + k, v)
        continue
    print("  %-32s ★%-6s %-5s push=%s" % (k, v["stargazers_count"], v["archived"], v["pushed_at"][:10]))
