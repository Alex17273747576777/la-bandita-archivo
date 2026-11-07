#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
demolicion-contenido.py v2 — ETAPA 1: demolición de contenido (solo lectura, determinístico).
v2: detector de DEFINICIONES con las 4 formas reales del canon:
  (1) encabezado Art./Artículo N-###/N  (2) lista/cita/negrita al inicio de línea
  (3) encabezado SOLO-NUMÉRICO «## 95.» (4) variante con sufijo «27-A» / prefijo «N-602».
Clasifica refs sin definición local en: cita-a-norma-madre (evidencia verbatim) vs colgante real.
Mide: TOC-fantasma, cifras vs bandas, fechas fuera de rango, D-007 (derogaciones sin fecha),
promesas de futuro, párrafos duplicados (plantillas), espejos T↔M finos.
Salida: 00-CANON/_mapa-canon/DEMOLICION-CONTENIDO.json + resumen impreso (cifras del acta).
"""
import re, os, json, hashlib, unicodedata
from collections import Counter

HERE = os.path.dirname(__file__)
CANON = os.path.join(HERE, "..", "..", "00-CANON")
PIEZAS = [
    ("TRATADO", "TRATADO.md", "md"),
    ("MANUAL", "MANUAL-COMPLETO.md", "md"),
    ("LECCIONES", "LECCIONES-ALEXIS.md", "md"),
    ("CIMIENTO", "CANON-CIMIENTO-V28sep.html", "html"),
    ("COMPENDIO", "COMPENDIO-INTEGRAL-LibroE-V26sep.html", "html"),
]
DEF_ART = re.compile(r"^[ \t]*(?:#{1,6}[ \t]+|[-*+][ \t]+|>[ \t]*)?\*{0,2}Art(?:s?\.|ículo)[ \t]*"
                     r"(?:([A-Z])-(\d+)|(\d+))(?:-([A-Z]))?", re.I)
DEF_NUM = re.compile(r"^#{1,6}[ \t]+(\d+)(?:\.\d+)*[ \t]*[\.\)—\-:]?", re.M)
REF = re.compile(r"Art(?:s?\.|ículo)[ \t]*(?:([A-Z])-(\d+)|(\d+))(?:-([A-Z]))?", re.I)
CITA = re.compile(r"véase|del tratado|del art\.|manual art|tratado [GF]|norma madre", re.I)
ISO = re.compile(r"\b20\d{2}-\d{2}-\d{2}\b")
DMY = re.compile(r"\b(\d{1,2})-(ene|feb|mar|abr|may|jun|jul|ago|sep|oct|nov|dic)-(\d{4})\b", re.I)
FIG = re.compile(r"\b[46]\d\.\d{3}\b")
NEG = re.compile(r"ni derogad|no (?:las|lo|la|se) ?deroga|no pueden ser derogad|no se deroga|"
                 r"sin derogar|aplicada a la propia casa", re.I)
PROM = ["añadirá", "agregará", "se incorporará", "se publicará", "próximas versiones",
        "próxima versión", "futura revisión", "futuras revisiones", "quedará pendiente",
        "queda pendiente", "pendiente de revisión"]

def fold(s):
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if not unicodedata.combining(c)).lower()

def key(m):
    pre, n1, n2, suf = m.groups()
    return ("%s-%d" % (pre.upper(), int(n1))) if pre else ("*-%s%s" % (n2, ("-" + suf.upper()) if suf else ""))

R = {}
for k, fn, kind in PIEZAS:
    d = open(os.path.join(CANON, fn), encoding="utf-8").read()
    html = kind == "html"
    lines = d.split("\n")
    defs = set()
    if not html:
        for l in lines:
            m = DEF_ART.match(l)
            if m: defs.add(key(m))
        for m in DEF_NUM.finditer(d):
            defs.add("*-%s" % m.group(1))
    refs_tot = 0; sin_def = Counter(); sin_ej = {}; citas = Counter(); colg = Counter()
    for l in lines:
        ll = re.sub(r"<[^>]+>", " ", l) if html else l
        if not html and (l.startswith("#") or l.strip().startswith(("- [", "* ["))):
            continue
        for m in REF.finditer(ll):
            refs_tot += 1; kk = key(m)
            if kk not in defs:
                if CITA.search(ll):
                    citas[kk] += 1; sin_ej.setdefault(kk, re.sub(r"\s+", " ", ll.strip())[:85])
                else:
                    colg[kk] += 1; sin_ej.setdefault(kk, re.sub(r"\s+", " ", ll.strip())[:85])
    pend_t = pend_sf = prop_t = prop_sf = 0
    fechas = set()
    for l in lines:
        low = l.lower()
        if "pendiente" in low:
            pend_t += 1
            if not (ISO.search(l) or DMY.search(l)): pend_sf += 1
        if "propuesta" in low:
            prop_t += 1
            if not (ISO.search(l) or DMY.search(l)): prop_sf += 1
        for mm in ISO.finditer(l): fechas.add(mm.group(0))
        dm = DMY.search(l)
        if dm: fechas.add("%s-%02d-%02d" % (dm.group(3), {"ene":1,"feb":2,"mar":3,"abr":4,"may":5,"jun":6,"jul":7,"ago":8,"sep":9,"oct":10,"nov":11,"dic":12}[dm.group(2).lower()], int(dm.group(1))))
    fuera = sorted(x for x in fechas if not ("2026-02-10" <= x <= "2026-12-31"))
    figs = Counter(FIG.findall(d))
    proms = Counter()
    for p in PROM: proms[p] = len(re.findall(re.escape(p), d, flags=re.I))
    txt = d if not html else re.sub(r"<[^>]+>", " ", d)
    paras = Counter()
    for p in re.split(r"\n\s*\n", txt):
        n = re.sub(r"[^a-z0-9ñ]+", " ", fold(p)).strip()
        if len(n) >= 80: paras[n] += 1
    dup_extra = sum(c - 1 for c in paras.values() if c > 1)
    dup_dist = sum(1 for c in paras.values() if c > 1)
    top = sorted(((c, p) for p, c in paras.items() if c > 1), reverse=True)[:2]
    # TOC-fantasma (md): números prometidos por el TOC sin definición local
    fant = []
    if not html:
        prom = {int(m.group(1)) for m in re.finditer(r"^-[ \t]*\[(?:Art(?:s?\.|ículo)?[ \t]*)?(\d+)[\.\s\]]", d, flags=re.M)}
        defn = {int(m.group(1)) for m in re.finditer(r"^[ \t]*(?:#{1,6}[ \t]+|[-*+][ \t]+|>[ \t]*)?\*{0,2}Art(?:s?\.|ículo)[ \t]*(?:[A-Z]-)?(\d+)", d, flags=re.M)}
        defn |= {int(m.group(1)) for m in DEF_NUM.finditer(d)}
        fant = sorted(prom - defn)
    der = []
    for l in lines:
        ll = re.sub(r"<[^>]+>", " ", l) if html else l
        if not html and (l.startswith("#") or l.strip().startswith(("- [", "* ["))): continue
        if "deroga" in ll.lower() and not NEG.search(ll):
            if not (ISO.search(ll) or DMY.search(ll)):
                der.append(re.sub(r"\s+", " ", ll.strip())[:95])
    R[k] = {
        "defs_locales": len(defs), "refs_prosa": refs_tot,
        "sin_def_local": {"total": sum(sin_def.values()),
                          "cita_a_norma_madre": {"total": sum(citas.values()), "claves": dict(citas.most_common(8)),
                                                  "evidencia": {a: sin_ej[a] for a in list(citas)[:3]}},
                          "colgante_real": {"total": sum(colg.values()), "claves": dict(colg.most_common(8)),
                                             "evidencia": {a: sin_ej[a] for a in list(colg)[:3]}}},
        "toc_fantasma": fant,
        "pendiente": {"lineas": pend_t, "sin_fecha": pend_sf},
        "propuesta": {"lineas": prop_t, "sin_fecha": prop_sf},
        "figuras_distintas": dict(sorted(figs.items())),
        "fechas_distintas": len(fechas), "fechas_fuera_rango": fuera,
        "promesas_futuro": dict(proms),
        "parrafos_duplicados": {"distintos": dup_dist, "ocurrencias_extra": dup_extra,
                                 "top": [{"n": c, "texto": p[:70]} for c, p in top]},
        "derogaciones_sin_fecha": der,
    }

T = open(os.path.join(CANON, "TRATADO.md"), encoding="utf-8").read()
Ma = open(os.path.join(CANON, "MANUAL-COMPLETO.md"), encoding="utf-8").read()
def bodyby(d, title):
    m = re.search(r"^#{1,4}[ \t]+%s[^\n]*\n" % re.escape(title), d, flags=re.M)
    if not m: return None
    n = re.search(r"^#{1,4}[ \t]+", d[m.end():], flags=re.M)
    return re.sub(r"\s+", " ", d[m.end():m.end() + (n.start() if n else 4000)]).strip()
esp = []
for num in [191, 192, 205, 243, 244, 245, 246, 247]:
    mt = re.search(r"^#{1,4}[ \t]+(Artículo %s\.[^\n]*)" % num, T, flags=re.M)
    t = mt.group(1).strip()
    bt, bm = bodyby(T, t), bodyby(Ma, t)
    nrm = re.sub(r"(?:-[ \t]*)+$", "", bt or "") == re.sub(r"(?:-[ \t]*)+$", "", bm or "")
    esp.append({"art": num, "crudo": "idéntico" if bt == bm else "diverge",
                "sin_---_final": "idéntico" if nrm else "DIVERGE REAL"})
R["espejos_finos"] = esp

j = (json.dumps(R, ensure_ascii=False, indent=1, sort_keys=False) + "\n").encode("utf-8")
out = os.path.join(CANON, "_mapa-canon", "DEMOLICION-CONTENIDO.json")
open(out, "wb").write(j)
sello = hashlib.sha256(j).hexdigest()[:16]

print("═══ ETAPA 1 v2 · DEMOLICIÓN DE CONTENIDO (solo lectura) ═══")
for k, fn, kind in PIEZAS:
    r = R[k]
    sd = r["sin_def_local"]
    print("— %s: defs %d · refs %d → citas-norma-madre %d · COLGANTES %d · TOC-fantasma %s · fechas-fuera %d · deroga-sf %d · dups +%d" % (
        k, r["defs_locales"], r["refs_prosa"], sd["cita_a_norma_madre"]["total"], sd["colgante_real"]["total"],
        r["toc_fantasma"] or "0", len(r["fechas_fuera_rango"]), len(r["derogaciones_sin_fecha"]),
        r["parrafos_duplicados"]["ocurrencias_extra"]))
    for a, ev in list(sd["cita_a_norma_madre"]["evidencia"].items())[:2]:
        print("   cita [%s] %s" % (a, ev))
    for a, ev in list(sd["colgante_real"]["evidencia"].items())[:2]:
        print("   COLGANTE [%s] %s" % (a, ev))
    for x in r["derogaciones_sin_fecha"][:3]:
        print("   deroga-sf:", x)
for e in R["espejos_finos"]:
    print("espejo %d: %s / sin-—-: %s" % (e["art"], e["crudo"], e["sin_---_final"]))
print("SELLO JSON: %s → %s" % (sello, os.path.normpath(out)))
