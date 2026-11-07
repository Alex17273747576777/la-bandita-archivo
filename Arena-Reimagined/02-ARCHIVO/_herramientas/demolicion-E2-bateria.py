#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
demolicion-E2-bateria.py — batería A de demolición (solo lectura) para la campaña del canon.
Uso: python3 demolicion-E2-bateria.py <pieza>
Mide: duplicados de encabezado (slug plegado), artículos duplicados (Art. X-### / Artículo ###),
inventario de marcadores (propuesta/pendiente/informativo) y doble-portada (más de un h1).
NO muta nada. Exit 1 si hay hallazgos.
"""
import sys, re, unicodedata, os, hashlib
from collections import Counter, defaultdict

CANON = os.path.join(os.path.dirname(__file__), "..", "..", "00-CANON")
PIEZAS = {
    "TRATADO": "TRATADO.md", "MANUAL": "MANUAL-COMPLETO.md", "LECCIONES": "LECCIONES-ALEXIS.md",
}
def fold(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return s.lower()
def slug(h):
    return re.sub(r"[^a-z0-9]+", "-", fold(h)).strip("-")

def main():
    pieza = sys.argv[1].upper()
    path = os.path.join(CANON, PIEZAS[pieza])
    d = open(path, encoding="utf-8").read()
    print("═══ E2 batería A · %s · %d B · %s ═══" % (pieza, len(d.encode()), hashlib.sha256(d.encode()).hexdigest()[:16]))
    heads = [(len(m.group(1)), m.group(2).strip()) for m in re.finditer(r"^(#{1,6}) (.+)$", d, flags=re.M)]
    print("encabezados:", len(heads))
    # h1 múltiples (doble portada)
    h1 = [h for lv, h in heads if lv == 1]
    print("h1:", len(h1), "→", [h[:60] for h in h1] if len(h1) > 1 else "único ✓")
    # duplicados por slug
    byslug = defaultdict(list)
    for lv, h in heads:
        byslug[slug(h)].append((lv, h))
    dups = {s: v for s, v in byslug.items() if len(v) > 1}
    nitems = sum(len(v) for v in dups.values())
    print("encabezados duplicados (por slug plegado): %d slugs · %d encabezados afectados" % (len(dups), nitems))
    for s in sorted(dups, key=lambda x: -len(dups[x]))[:20]:
        print("   ×%d  %s" % (len(dups[s]), s[:70]))
    # artículos duplicados por número
    arts = defaultdict(list)
    for lv, h in heads:
        m = re.match(r"Art\.\s*([A-Z])[- ](\d+)", h) or re.match(r"Art(?:ículo)?\s+(\d+)", h)
        if m:
            pre = (m.group(1) + "-") if m.lastindex == 2 and m.group(1).isalpha() else ""
            arts[(pre + m.groups()[-1])].append(h)
    darts = {k: v for k, v in arts.items() if len(v) > 1}
    print("artículos numerados:", len(arts), "· duplicados por número:", len(darts))
    for k in sorted(darts)[:20]:
        print("   ×%d  %s → %s" % (len(darts[k]), k, " || ".join(h[:40] for h in darts[k])))
    # marcadores de estado
    for mk in ["propuesta", "pendiente", "informativo"]:
        print("marcador «%s»:" % mk, len(re.findall(mk, d, flags=re.I)))
    sys.exit(0)

if __name__ == "__main__":
    main()
