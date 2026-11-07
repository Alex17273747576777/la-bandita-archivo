#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mapa-canon.py — MAPA MAESTRO DEL CANON, asegurado (genera y verifica).
Genera en 00-CANON/_mapa-canon/:
  · MAPA-CANON.json  — inventario completo máquina-consumible (encabezados, slugs FINALES
    con el slugger EXACTO del convertidor, tabla de reparación slug-muerto→slug-real,
    espejos T↔M, fechas, marcadores, sellos).
  · MAPA-CANON.md    — resumen legible con veredictos.
  · sello.txt        — sha16 del JSON.
Uso:
  python3 mapa-canon.py            → genera (determinístico; misma entrada = misma salida)
  python3 mapa-canon.py --verify   → regenera en memoria y compara byte-a-byte
NUNCA muta las fuentes. El slugger aquí es COPIA EXACTA del de envase-xhtml-canon.py
(NFKD → strip combining → lower → no-alnum→'-' → strip '-' → [:48] → sufijo -2,-3…).
"""
import sys, re, os, json, hashlib, unicodedata
from collections import OrderedDict

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
CANON = os.path.join(ROOT, "00-CANON")
OUT = os.path.join(CANON, "_mapa-canon")

PIEZAS = [
    ("TRATADO",   "TRATADO.md", "TRATADO-envase-XHTML-2026-10-10.xhtml", "md"),
    ("MANUAL",    "MANUAL-COMPLETO.md", "MANUAL-COMPLETO-envase-XHTML-2026-10-10.xhtml", "md"),
    ("LECCIONES", "LECCIONES-ALEXIS.md", "LECCIONES-ALEXIS-envase-XHTML-2026-10-10.xhtml", "md"),
    ("CIMIENTO",  "CANON-CIMIENTO-V28sep.html", "CANON-CIMIENTO-envase-XHTML-2026-10-10.xhtml", "html"),
    ("COMPENDIO", "COMPENDIO-INTEGRAL-LibroE-V26sep.html", "COMPENDIO-INTEGRAL-envase-XHTML-2026-10-10.xhtml", "html"),
]

def sha16(b): return hashlib.sha256(b).hexdigest()[:16]

def slug(t, used):
    """COPIA EXACTA del slugger de envase-xhtml-canon.py — no modificar aquí."""
    s = unicodedata.normalize("NFKD", t)
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:48] or "sec"
    base, i = s, 2
    while s in used:
        s = "%s-%d" % (base, i); i += 1
    used.add(s)
    return s

def fold(s):
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if not unicodedata.combining(c)).lower()

def headings_md(d):
    return [(len(m.group(1)), m.group(2).strip()) for m in re.finditer(r"^(#{1,6}) (.+)$", d, flags=re.M)]

def headings_html(d):
    return [(int(m.group(1)), re.sub(r"<[^>]+>", "", m.group(2)).strip())
            for m in re.finditer(r"<h([1-4])[^>]*>(.*?)</h\1>", d, flags=re.S)]

def slugged(heads):
    used = set(); out = []
    for lv, t in heads:
        out.append((lv, t, slug(t, used)))
    return out

def repair_table(heads_final, links):
    """dead slug → candidatos: exacto / prefijo-único / ambiguo / sin-candidato."""
    finals = {s for _, _, s in heads_final}
    untrunc = {}
    for _, t, s in heads_final:
        u = re.sub(r"[^a-z0-9]+", "-", fold(t)).strip("-")
        untrunc.setdefault(u, s)
    table = []
    for h in sorted({l for l in links if l not in finals}):
        if h in untrunc:
            table.append({"muerto": h, "estado": "exacto-sin-truncar", "real": untrunc[h]}); continue
        cands = sorted({s for u, s in untrunc.items() if u.startswith(h) and len(h) >= 6})
        if len(cands) == 1:
            table.append({"muerto": h, "estado": "prefijo-único", "real": cands[0]})
        elif len(cands) > 1:
            table.append({"muerto": h, "estado": "ambiguo", "candidatos": cands[:6]})
        else:
            cands2 = sorted({s for u, s in untrunc.items() if u[:40] == h[:40]})
            if len(cands2) == 1:
                table.append({"muerto": h, "estado": "prefijo-40", "real": cands2[0]})
            else:
                table.append({"muerto": h, "estado": "sin-candidato"})
    return table

def build():
    M = OrderedDict()
    M["generado"] = "mapa-canon.py (determinístico; sin reloj — la fecha vive en el registro del taller)"
    piezas = {}
    for key, src, env, kind in PIEZAS:
        sb = open(os.path.join(CANON, src), "rb").read()
        eb = open(os.path.join(CANON, "_envases-xhtml", env), "rb").read()
        sd = sb.decode("utf-8"); ed = eb.decode("utf-8")
        heads = slugged(headings_md(sd) if kind == "md" else headings_html(sd))
        eheads = slugged(headings_html(ed))
        if kind == "md":
            links = re.findall(r"\]\(#([^)]+)\)", sd)
        else:
            links = re.findall(r'href="#([^"]+)"', sd)
        elinks = re.findall(r'href="#([^"]+)"', ed)
        finals = {s for _, _, s in heads}
        efinals = {s for _, _, s in eheads}
        if kind == "html":
            # FIX #28: los ids de ATRIBUTO son anclas legítimas (los navegadores las resuelven);
            # sin esto el mapa contaba muertos falsos (CIMIENTO fuente ×4, COMPENDIO envase ×2).
            finals |= set(re.findall(r'id="([^"]+)"', sd))
        # FIX #28b: en ENVASES, los ids de atributo SON las anclas reales (secciones, h3 con id,
        # UI) — el mapa nunca debe llamar muerto un target que el navegador sí resuelve.
        efinals |= set(re.findall(r'id="([^"]+)"', ed))
        p = OrderedDict()
        p["fuente"] = {"archivo": src, "bytes": len(sb), "sha16": sha16(sb)}
        p["envase"] = {"archivo": env, "bytes": len(eb), "sha16": sha16(eb)}
        p["encabezados"] = len(heads)
        p["h1"] = sum(1 for lv, _, _ in heads if lv == 1)
        p["slug_dead_fuente"] = sorted({l for l in links if l not in finals})
        p["slug_dead_envase"] = sorted({l for l in elinks if l not in efinals})
        p["reparacion"] = repair_table(heads, links)
        if kind == "md":
            iso = sorted(set(re.findall(r"\b20\d{2}-\d{2}-\d{2}\b", sd)))
            p["fechas_iso"] = iso
            p["marcadores"] = {m: len(re.findall(m, sd, flags=re.I)) for m in ("propuesta", "pendiente", "informativo")}
        piezas[key] = p
    M["piezas"] = piezas
    # espejos T↔M (definiciones por encabezado)
    tD = {}; mD = {}
    T = open(os.path.join(CANON, "TRATADO.md"), encoding="utf-8").read()
    Ma = open(os.path.join(CANON, "MANUAL-COMPLETO.md"), encoding="utf-8").read()
    for d, into in ((T, tD), (Ma, mD)):
        for m in re.finditer(r"^#{1,4}\s+(Art\.\s*([A-Z])-(\d+)[^\n]*|Artículo\s+(\d+)[^\n]*)", d, flags=re.M):
            k = ("%s-%s" % (m.group(2), m.group(3))) if m.group(2) else ("*-%s" % m.group(4))
            into.setdefault(k, m.group(1).strip())
    espejos = []
    for k in sorted(set(tD) & set(mD)):
        def body(d, pat):
            m = re.search(pat, d, flags=re.M)
            if not m: return None
            n = re.search(r"^#{1,4}\s+", d[m.end():], flags=re.M)
            return re.sub(r"\s+", " ", d[m.end():m.end() + (n.start() if n else 4000)]).strip().rstrip("-").strip()
        patT = r"^#{1,4}\s+%s\s*\.[^\n]*\n" % re.escape(tD[k].split(".")[0]) if False else None
        # cuerpo por título exacto
        def bodyby(d, title):
            m = re.search(r"^#{1,4}\s+%s[^\n]*\n" % re.escape(title), d, flags=re.M)
            if not m: return None
            n = re.search(r"^#{1,4}\s+", d[m.end():], flags=re.M)
            return re.sub(r"\s+", " ", d[m.end():m.end() + (n.start() if n else 4000)]).strip()
        bt, bm = bodyby(T, tD[k]), bodyby(Ma, mD[k])
        espejos.append({"art": k, "titulo": tD[k][:60], "cuerpo": "idéntico" if bt == bm else "diverge"})
    M["espejos_T_M"] = espejos
    # enlaces ENTRE piezas
    M["enlaces_entre_piezas"] = sum(
        len([r for r in re.findall(r"\]\((?!#)([^)#]+)\)", open(os.path.join(CANON, s), encoding="utf-8").read())
             if not r.startswith("http")])
        for _, s, _, k in PIEZAS if k == "md")
    return (json.dumps(M, ensure_ascii=False, indent=1, sort_keys=False) + "\n").encode("utf-8")

def human(j):
    M = json.loads(j.decode("utf-8"))
    L = ["# MAPA-CANON — resumen (generado; NO editar a mano)", ""]
    for k, p in M["piezas"].items():
        r = p["reparacion"]
        ok = sum(1 for x in r if "real" in x)
        amb = sum(1 for x in r if x["estado"] == "ambiguo")
        sc = sum(1 for x in r if x["estado"] == "sin-candidato")
        L.append("**%s** — fuente %d B `%s` · envase %d B `%s` · heads %d · h1 %d · slugs muertos: fuente %d, envase %d · reparación: %d resueltos, %d ambiguos, %d sin candidato" % (
            k, p["fuente"]["bytes"], p["fuente"]["sha16"], p["envase"]["bytes"], p["envase"]["sha16"],
            p["encabezados"], p["h1"], len(p["slug_dead_fuente"]), len(p["slug_dead_envase"]), ok, amb, sc))
    esp = M["espejos_T_M"]
    L.append("Espejos T↔M: %d · idénticos %d · divergen %d" % (
        len(esp), sum(1 for e in esp if e["cuerpo"] == "idéntico"), sum(1 for e in esp if e["cuerpo"] != "idéntico")))
    L.append("Enlaces ENTRE piezas: %d" % M["enlaces_entre_piezas"])
    L.append("Sello JSON: %s" % sha16(j))
    return ("\n".join(L) + "\n").encode("utf-8")

def main():
    j = build()
    os.makedirs(OUT, exist_ok=True)
    if "--verify" in sys.argv:
        for name, data in (("MAPA-CANON.json", j), ("MAPA-CANON.md", human(j)),
                           ("sello.txt", sha16(j).encode())):
            p = os.path.join(OUT, name)
            same = os.path.exists(p) and open(p, "rb").read() == data
            print("%-18s %s" % (name, "idéntico ✓" if same else "✗ DIFIERE"))
        print("MAPA ASEGURADO:", "SÍ — regeneración byte-a-byte ✓" if all(
            os.path.exists(os.path.join(OUT, n)) and open(os.path.join(OUT, n), "rb").read() == d
            for n, d in (("MAPA-CANON.json", j), ("MAPA-CANON.md", human(j)), ("sello.txt", sha16(j).encode()))
        ) else "NO")
    else:
        open(os.path.join(OUT, "MAPA-CANON.json"), "wb").write(j)
        open(os.path.join(OUT, "MAPA-CANON.md"), "wb").write(human(j))
        open(os.path.join(OUT, "sello.txt"), "w").write(sha16(j))
        print(human(j).decode())

if __name__ == "__main__":
    main()
