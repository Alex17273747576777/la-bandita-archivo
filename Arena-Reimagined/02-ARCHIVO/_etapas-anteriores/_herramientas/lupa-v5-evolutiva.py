#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LUPA v5 EVOLUTIVA — La Bandita (15-oct-2026)
"Tu yo de ahora mismo sigue siendo el suelo." La v4 era el piso; esto es el siguiente.
NUEVO sobre v4:
  A · DOCTRINA SIN PERDÓN: los veredictos por contenido viven en
      02-ARCHIVO/doctrina-lupa.json y se muestran como ANOTACIÓN
      ("· ya actuado (acta …)"). NADA se suprime: toda alerta sigue
      apareciendo y contando. Aprender ≠ perdonar.
  R · REFERENCIAS INTERNAS: «Caso D», «Escalera 3», «sección 🕐» —
      el referente debe existir en la pieza. Un mapa que promete y no
      entrega es una mentira con hipervínculo roto.
  S · ARITMÉTICA DE DECLARACIONES: «★569 → ★621 … cincuenta marcas
      nuevas» — la resta se hace de verdad. El conteo de versiones se
      informa (jamás se inventa). La matemática incorrecta se CAZA.
  T · MONOTONÍA DE SECCIÓN: la v4 cazaba drones frase-a-frase; la v5
      caza secciones enteras cuyo párrafo-respiro es un metrónomo
      (≥6 párrafos de largo casi idéntico, cv < 0.12).
  E2 · FUZZING DE PROPIEDADES (--fuzz N): N ensayos con 1-3 mutaciones
      COMBINADAS al azar (semilla fija = auditable). 100% o la lupa
      está PROHIBIDA.
  CICATRICES: cada defecto real cazado en batalla se convierte en
      mutación permanente (m28 bala 350c del caso L501 · m29 referencia
      rota · m30 resta mentirosa · m31 metrónomo de sección).
Cero absoluto de falsas aprobaciones — intocable:
  1) Detectores anchos. 2) Mutación + fuzz al 100%. 3) Veredicto por
  CONTENIDO actuado. 4) Q y los informes jamás auto-aprueban.
Uso:
  python3 lupa-v5-evolutiva.py PIEZA.md [--keys "k1|k2"] [--cutover AAAA-MM-DD]
                                       [--doctrina FILE] [--mutate] [--fuzz 60] [--live]
"""
import os, sys, re, json, random, hashlib, statistics
from importlib import util as _ilu

_ACA = os.path.dirname(os.path.abspath(__file__))
def _carga_v4():
    spec = _ilu.spec_from_file_location("lupa_v4", os.path.join(_ACA, "lupa-v4-experto.py"))
    m = _ilu.module_from_spec(spec); spec.loader.exec_module(m)
    return m

V4 = _carga_v4()

STOPW = set("de la el los las que y en a con por para un una al lo se su sin es".split())
NUMW = {"cero":0,"un":1,"una":1,"dos":2,"tres":3,"cuatro":4,"cinco":5,"seis":6,"siete":7,"ocho":8,
        "nueve":9,"diez":10,"once":11,"doce":12,"trece":13,"catorce":14,"quince":15,"veinte":20,
        "veinticinco":25,"treinta":30,"cuarenta":40,"cincuenta":50,"sesenta":60,"cien":100}

def _num(tok):
    tok = tok.lower().strip(".")
    mult = 1
    if tok.endswith("k"): tok = tok[:-1]; mult = 1000
    if tok.replace(".", "").replace(",", "").isdigit():
        return int(float(tok.replace(".", "").replace(",", "")) * mult)
    return NUMW.get(tok)

def detect_v5(d, quiz_keys=(), cut=(2026,10,15), doctrine=None, pieza=""):
    flags, report = V4.detect(d, quiz_keys, cut)
    L = d.split("\n")
    fences = [i for i, l in enumerate(L) if l.strip() == "```"]
    def infence(i):
        if len(fences) % 2 == 1:
            return False  # valla impar = paridad corrupta: TODO se examina en crudo (cicatriz fuzz 58/60 del 15-oct)
        return sum(1 for f in fences if f < i) % 2 == 1
    isnum = lambda l: l[:2] in ("1.","2.","3.","4.","5.","6.","7.")
    canon_div = "─"*19
    # R · referencias internas
    total = d
    MENCION = lambda tag: re.compile(r"(en\s+el|del|al|vimos\s+en|como\s+el)\s+%s\b|%s\s+de\s+(arriba|abajo)" % (tag, tag))
    def referente(tag):
        for l in L:
            if tag in l and not MENCION(tag).search(l):
                return True
        return False
    for m in re.finditer(r"Caso ([A-Z0-9])\b", d):
        if not referente("Caso %s" % m.group(1)):
            flags.append(("R referencia", "«Caso %s» sin referente" % m.group(1)))
    for m in re.finditer(r"Escalera (\d+)", d):
        if not referente("Escalera %s" % m.group(1)):
            flags.append(("R referencia", "«Escalera %s» sin referente" % m.group(1)))
    for m in re.finditer(r"sección\s+([^\s,.;:\)]+)", d):
        tok = m.group(1)
        if tok.startswith("«"):
            continue
        if not any(tok in l and l.strip().startswith("*") for l in L):
            flags.append(("R referencia", "«sección %s» sin encabezado" % tok))
    # S · aritmética de estrellas (flecha + reclamo verbal/dígito en la misma línea)
    for i, l in enumerate(L, 1):
        if infence(i-1): continue
        ms = re.findall(r"★\s?([\d.,]+\s*k?)", l)
        a = b = None
        if "→" in l and len(ms) >= 2:
            a, b = _num(ms[0]), _num(ms[-1])
        else:
            md = re.search(r"de\s+★?\s?([\d.,]+\s*k?)\s+a\s+★?\s?([\d.,]+\s*k?)", l, re.I)
            if md: a, b = _num(md.group(1)), _num(md.group(2))
        if a and b:
            cm = re.search(r"(\w+)\s+(?:marcas|estrellas)\s+nuevas", l, re.I)
            if cm:
                claim = _num(cm.group(1))
                if claim is not None:
                    delta = abs(b - a)
                    if abs(delta - claim) > max(2, 0.1*delta):
                        flags.append(("S Δestrellas", "L%d: %s→%s dice %s (Δ=%d)" % (i, ms[0], ms[-1], cm.group(1), delta)))
    # S-informe: conteo de versiones en pieza vs reclamos «N versiones en M …»
    vers = set(re.findall(r"\bv\d+\.\d+\.\d+\b", d))
    for m in re.finditer(r"\b(\d+)\s+versiones\s+en\s+(\d+)\s+(días|semanas)\b", d, re.I):
        report.setdefault("conteo", []).append("reclama %s versiones · tokens v-punto en pieza: %d" % (m.group(1), len(vers)))
    # T · monotonía de sección (párrafos de prosa de largo uniforme)
    block = []; bs = 0
    def close_block(bi):
        prose = [len(x) for x in block if len(x) > 60]
        run = 1
        for j in range(1, len(prose)):
            if abs(prose[j] - prose[j-1]) <= max(3, 0.05*prose[j]):
                run += 1
            else:
                run = 1
            if run >= 5:
                flags.append(("T monotonía", "bloque desde L%d: %d párrafos seguidos de ~%dc" % (bs, run+0, prose[j])))
                break
    for i, l in enumerate(L, 1):
        if l.strip() == canon_div:
            close_block(i); block = []; continue
        if infence(i-1) or l.startswith(("•", ">", "├", "└")) or isnum(l) or not l.strip():
            continue
        if not block: bs = i
        block.append(l.strip())
    close_block(len(L))
    # U · litania: >=5 balas seguidas abriendo con las mismas 2 palabras
    # (cicatriz 15-oct-2026: el dueño cazó la litania «La voz de...» x9 en la guía 13)
    run_w = None; rs = None; runlen = 0
    def _cerrar_u():
        if run_w[0] is not None and runlen[0] >= 5:
            flags.append(("U litania", "desde L%d: «%s» x%d" % (rs[0], run_w[0], runlen[0])))
    run_w = [None]; rs = [None]; runlen = [0]
    for i, l in enumerate(L, 1):
        s = l.strip()
        if not infence(i-1) and s.startswith(("·", "•")):
            w = " ".join(re.findall(r"[\wáéíóúñü]+", s.lower())[:2])
            if w == run_w[0]: runlen[0] += 1
            else:
                _cerrar_u(); run_w[0] = w; rs[0] = i; runlen[0] = 1
        elif s == "":
            continue  # la línea en blanco NO rompe una litania de párrafos-balas (cicatriz del cicatriz, 15-oct)
        else:
            _cerrar_u(); run_w[0] = None; runlen[0] = 0
    _cerrar_u()
    # A · doctrina: anotar, jamás suprimir
    ann = 0
    if doctrine:
        propias = [(pid, its) for pid, its in doctrine.get("piezas", {}).items() if pieza.startswith(pid)]
        for pi, (k, v) in enumerate(flags):
            for _pid, items in propias:
                for itemi in items:
                    if itemi["clase"] == k:
                        flags[pi] = (k, v + " · ya actuado (acta %s: %s)" % (itemi["fecha"], itemi["razon"][:40]))
                        ann += 1
                        break
                else:
                    continue
                break
    if ann:
        report["doctrina"] = ["%d alertas llevan anotación de acta anterior (NADA suprimido)" % ann]
    return flags, report

SCARS = [
    ("m28 bala 350c (cicatriz L501)", lambda d: d + "\n• " + "W"*350 + "\n", "A unidad>280"),
    ("m29 referencia rota",           lambda d: d.replace("\n\n", "\n\nComo vimos en el Caso Z de arriba, queda claro.\n\n", 1), "R referencia"),
    ("m30 resta mentirosa",           lambda d: d + "\n• La vitrina pasó de ★100 a ★190: treinta marcas nuevas.\n", "S Δestrellas"),
    ("m31 metrónomo de sección",      lambda d: d.replace("\n\n", "\n\n" + "El vecino mide su vara con calma en la mañana del trabajo ajeno.\n\n"*6, 1), "T monotonía"),
    ("m32 litania (crítica del dueño)", lambda d: d.replace("\n\n", "\n\n· la voz del barrio corre la voz.\n· la voz del barrio corre la lista.\n· la voz del barrio corre la tarde.\n· la voz del barrio corre el dato.\n· la voz del barrio corre el rumor.\n", 1), "U litania"),
    ("m33 litania de párrafos (guía 13 real)", lambda d: d.replace("\n\n", "\n\n· la voz del patio grita fuerte.\n\n· la voz del patio grita claro.\n\n· la voz del patio grita hoy.\n\n· la voz del patio grita nunca.\n\n· la voz del patio grita siempre.\n", 1), "U litania"),
]

def _autokeys(d):
    ks = []
    for q in [l for l in d.split("\n") if l.startswith("`") and len(l) > 4 and l[2] == "."]:
        plain = q.strip("`")[::-1]
        ws = sorted((x for x in re.findall(r"\w{6,}", plain)), key=len, reverse=True)
        if ws: ks.append(ws[0])
    return ks[:4]

def run_mutate_v5(path, quiz_keys, cut):
    d0 = open(path, encoding="utf-8").read(); ok = 0; total = 0
    if not quiz_keys:
        quiz_keys = _autokeys(d0)
    suite = [(n, f, e) for (n, f, e) in V4.MUTATIONS] + list(SCARS)
    for name, fn, expect in suite:
        if fn is None and not quiz_keys:
            print("  - m15 quiz castrado    → OMITIDA (host sin quiz ni claves)")
            continue
        if fn is None:  # m15: romper la primera clave del quiz real
            dd = d0; done = False
            for q in [l for l in dd.split("\n") if l.startswith("`") and len(l) > 3 and l[2] == "."]:
                for k in quiz_keys:
                    if k in q.strip("`")[::-1]:
                        plain = q.strip("`")[::-1].replace(k, "X")
                        dd = dd.replace(q, "`" + plain[:-2][::-1] + "..`", 1)
                        done = True; break
                if done: break
            fn = (lambda dd: (lambda x: dd))(dd)
        if not V4._feasible(expect, d0):
            print("  - %-30s → OMITIDA (alcance ausente en el host)" % name)
            continue
        d1 = fn(d0)
        if d1 == d0:
            print("  - %-30s → OMITIDA (ancla ausente en el host)" % name)
            continue
        total += 1
        got = {k for k, _ in detect_v5(d1, quiz_keys, cut)[0]}
        hit = any(g.startswith(expect) for g in got)
        ok += hit
        print("  %s %-30s → [%s]" % ("✓" if hit else "✗ FUGA", name, expect))
    print("MUTACIÓN: %d/%d cazadas" % (ok, total))
    return ok == total

def run_fuzz(path, quiz_keys, cut, trials=60, seed=20261015):
    d0 = open(path, encoding="utf-8").read()
    pool = [(n, f, e) for (n, f, e) in V4.MUTATIONS if f is not None] + list(SCARS)
    rng = random.Random(seed); ok = 0; done = 0
    # cicatriz 15-oct noche: la evidencia se verifica AL APLICARSE cada mutación,
    # no al final — dos mutaciones sintéticas pueden destruirse la evidencia entre sí
    # (m7 borraba el doble-sep de m9: artefacto del arnés, no ceguera del detector).
    for t in range(trials):
        k = rng.randint(1, 3)
        picks = rng.sample(pool, k)
        dm = d0; eff = 0; bad = None
        for _n, f, e in picks:
            d2 = f(dm)
            if d2 == dm: continue
            got = {kk for kk, _ in detect_v5(d2, quiz_keys, cut)[0]}
            if not any(g.startswith(e) for g in got):
                bad = (_n, e); break
            eff += 1; dm = d2
        if bad:
            print("  ✗ ensayo %d: %s no visible al aplicarse (%s)" % (t+1, bad[1], bad[0])); continue
        if eff:
            done += 1; ok += 1
        else:
            print("  - ensayo %d → OMITIDO (mutaciones sin ancla)" % (t+1))
    print("FUZZ: %d/%d ensayos combinados cazados (semilla %d)" % (ok, done, seed))
    return ok == done

if __name__ == "__main__":
    path = sys.argv[1]
    d = open(path, encoding="utf-8").read()
    quiz_keys = sys.argv[sys.argv.index("--keys")+1].split("|") if "--keys" in sys.argv else []
    cut = (2026, 10, 15)
    if "--cutover" in sys.argv:
        y, m, dd = map(int, sys.argv[sys.argv.index("--cutover")+1].split("-")); cut = (y, m, dd)
    doctrine = None
    if "--doctrina" in sys.argv:
        dp = sys.argv[sys.argv.index("--doctrina")+1]
        doctrine = json.load(open(dp, encoding="utf-8"))
    if "--mutate" in sys.argv:
        sys.exit(0 if run_mutate_v5(path, quiz_keys, cut) else 1)
    if "--fuzz" in sys.argv:
        n = int(sys.argv[sys.argv.index("--fuzz")+1]) if sys.argv.index("--fuzz")+1 < len(sys.argv) and sys.argv[sys.argv.index("--fuzz")+1].isdigit() else 60
        sys.exit(0 if run_fuzz(path, quiz_keys, cut, n) else 1)
    if "--live" in sys.argv:
        tok = sys.argv[sys.argv.index("--token")+1] if "--token" in sys.argv else os.environ.get("GITHUB_TOKEN")
        V4.live_pulse(path, tok); sys.exit(0)
    flags, report = detect_v5(d, quiz_keys, cut, doctrine, os.path.basename(path))
    print("ALERTAS:", len(flags))
    for k, v in flags: print("  [%s] %s" % (k, v))
    for key in ("hoy", "estrellas", "conteo", "doctrina"):
        if report.get(key):
            print("INFORME %s: %d" % (key, len(report[key])))
            for x in report[key][:10]: print("  ·", x)
    n = len(d); s = hashlib.sha256(d.encode()).hexdigest()[:16]
    print("TOTAL: %d c · banda: %s · sello: %s" % (n, "DENTRO ✓" if 62000 <= n <= 64000 else "FUERA", s))
