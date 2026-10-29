#!/usr/bin/env python3
# RESTAURADOR WA DESDE EL CATALOGO SELLADO (cicatriz 19/29-oct-2026).
# USO: restaurar-wa-desde-catalogo.py <dir-WA> [ruta-catalogo]
import json, hashlib, os, sys
dest = sys.argv[1]
cat = sys.argv[2] if len(sys.argv) > 2 else "/home/user/Arena-Reimagined/02-ARCHIVO/catalogo-la-bandita.html"
html = open(cat, encoding="utf-8").read()
dec = json.JSONDecoder(); i = 0; ok = escritos = 0
while True:
    i = html.find('{"idx":', i)
    if i < 0: break
    try: obj, end = dec.raw_decode(html, i)
    except Exception: i += 6; continue
    i = end
    f = obj.get("file", "") or ""
    if "-WhatsApp-" not in f or not f.endswith("-dominicano-ES.md") or not f[0].isdigit(): continue
    p = os.path.join(dest, f)
    cur = open(p, 'rb').read() if os.path.exists(p) else None
    if cur is not None and hashlib.sha256(cur).hexdigest()[:16] == obj["sha"] and len(cur.decode('utf-8')) == obj["len"]:
        ok += 1; continue
    txt = obj["text"].encode("utf-8")
    assert hashlib.sha256(txt).hexdigest()[:16] == obj["sha"] and len(obj["text"]) == obj["len"], f
    os.makedirs(dest, exist_ok=True); open(p, 'wb').write(txt); escritos += 1
print(f"intactos {ok} · restaurados {escritos} · verificados {ok+escritos}")
