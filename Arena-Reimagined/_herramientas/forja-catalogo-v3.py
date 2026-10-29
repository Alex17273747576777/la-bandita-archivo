#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# FORJA v3 DEL MEGA CATÁLOGO — ADN del MÓDULO REAL (MOsPremiumV15, despiece en _referencia/)
# Arquitectura: plantilla en archivo propio (plantilla-v3.html, escrita byte-exacto)
#               + esta forja solo construye el DATA y lo inyecta.
# Leyes heredadas de v2:
#  1) verificación obligatoria: node --check + json.loads antes de declarar éxito
#  2) JS del catálogo mide caracteres con cps() (puntos de código), JAMÁS .length
#  3) WA: 23 piezas actuales (excluye era-vieja «-2026-10-02») · FB: solo actuales con 💓
#  4) health() espejo exacto de la lupa v6 (exime REV| y «(Las respuestas»)
import os, re, json, hashlib, datetime

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

TPL = open(os.path.join(BASE, "_herramientas/plantilla-v3.html"), encoding="utf-8").read()
for ph in ("__DATA__", "__NWA__", "__NFB__", "__BUILD__"):
    assert TPL.count(ph) == 1, "placeholder " + ph + " aparece " + str(TPL.count(ph)) + " veces"

BUILD = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
html = (TPL.replace("__DATA__", js)
           .replace("__NWA__", str(len(pieces)))
           .replace("__NFB__", str(len(fb)))
           .replace("__BUILD__", BUILD))
out = os.path.join(BASE, "02-ARCHIVO/catalogo-la-bandita.html")
open(out, "w", encoding="utf-8").write(html)
print("CATÁLOGO v3:", len(html), "chars ·", os.path.getsize(out), "bytes · WA:", len(pieces), "· FB:", len(fb), "· build:", BUILD)
