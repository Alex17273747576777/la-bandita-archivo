#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LUPA v4 EXPERTO del rompecabezas — La Bandita (15-oct-2026)
Evolución más allá de lo necesario: nivel foro de élite y por encima.
4PDA modera archivos a mano y con escaneos sueltos; esta vara verifica
DECLARACIONES completas de una pieza:
  · TEXTO: respiro (unidades >280c, balas apiladas, rachas), cadencia (monotonía),
    eco (n-gramas de 7 palabras repetidos), durezas WhatsApp-nativas.
  · MATEMÁTICA: Σ minutos del árbol = header; quiz invertido round-trip.
  · ESTRUCTURA: mapa/árbol ↔ cuerpo (por tallos, en orden, en ventana).
  · CRONOLOGÍA: fechas futuras, «hoy» amarrado a fecha vieja (rancio), informe de «hoy».
  · VINTAGE: estrella/número de pulso sin fecha de constancia.
  · PULSO VIVO (--live): contraste contra la API de GitHub — informe, jamás auto-aprueba.
Cero absoluto de falsas aprobaciones:
  1) Detectores ANCHOS: atrapan de más, jamás de menos.
  2) Prueba por MUTACIÓN: 27 defectos inyectados; si uno escapa, la lupa está PROHIBIDA.
  3) Toda alerta recibe veredicto por CONTENIDO actuado, nunca por clase de patrón.
  4) Q (pulso vivo) es informe, no veredicto.
Uso:
  python3 lupa-v4-experto.py PIEZA.md [--keys "k1|k2"] [--cutover AAAA-MM-DD]
  python3 lupa-v4-experto.py PIEZA.md --mutate [--keys "..."]
  python3 lupa-v4-experto.py PIEZA.md --live [--token XXX] (o env GITHUB_TOKEN)
"""
import re, sys, hashlib, statistics, datetime

MESES = {"ene":1,"feb":2,"mar":3,"abr":4,"may":5,"jun":6,"jul":7,"ago":8,"sep":9,"oct":10,"nov":11,"dic":12}
MESES_L = {"enero":1,"febrero":2,"marzo":3,"abril":4,"mayo":5,"junio":6,"julio":7,"agosto":8,
           "septiembre":9,"setiembre":9,"octubre":10,"noviembre":11,"diciembre":12}

def parse_dates(txt):
    out = []
    for m in re.finditer(r"\b(\d{1,2})-(ene|feb|mar|abr|may|jun|jul|ago|sep|oct|nov|dic)(?:-(\d{4}))?\b", txt, re.I):
        y = int(m.group(3)) if m.group(3) else None
        out.append(((int(m.group(1)), MESES[m.group(2).lower()], y), m.group(0), m.start()))
    for m in re.finditer(r"\b(\d{1,2}) de (enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|setiembre|octubre|noviembre|diciembre)(?: de (\d{4}))?\b", txt, re.I):
        y = int(m.group(3)) if m.group(3) else None
        out.append(((int(m.group(1)), MESES_L[m.group(2).lower()], y), m.group(0), m.start()))
    return out

def detect(d, quiz_keys=(), cut=(2026, 10, 15)):
    L = d.split("\n"); flags = []; report = {"hoy": [], "estrellas": []}
    fences = [i for i, l in enumerate(L) if l.strip() == "```"]
    def infence(i):
        if len(fences) % 2 == 1:
            return False  # valla impar = paridad corrupta: TODO en crudo (cicatriz fuzz 58/60 del 15-oct)
        return sum(1 for f in fences if f < i) % 2 == 1
    isnum = lambda l: l[:2] in ("1.","2.","3.","4.","5.","6.","7.")
    # A · respiro: unidades >280c completas
    for i, l in enumerate(L, 1):
        if infence(i-1):
            if len(l) > 64: flags.append(("C mono>64", "L%d %dc" % (i, len(l))))
            continue
        if len(l) > 280:
            kind = "bala" if l.startswith("• ") else "num" if isnum(l) else "prosa"
            flags.append(("A unidad>280", "L%d %dc [%s] %s" % (i, len(l), kind, l[:60])))
    # B · balas apiladas sin aire (ambas >120c)
    for i in range(1, len(L)):
        if L[i].startswith("• ") and L[i-1].startswith("• ") and len(L[i]) > 120 and len(L[i-1]) > 120:
            flags.append(("B apilada", "L%d/L%d (%dc+%dc)" % (i, i+1, len(L[i-1]), len(L[i]))))
    # C · durezas
    for i, l in enumerate(L, 1):
        if infence(i-1): continue
        if '"' in l: flags.append(("C recta", "L%d" % i))
        if l.strip() != "```" and l.count("`") % 2: flags.append(("C backtick", "L%d" % i))
        if re.match(r"^#{1,6}\s", l): flags.append(("C meta", "L%d" % i))
        if "](" in l: flags.append(("C linkmd", "L%d" % i))
        if l.strip().startswith("|"): flags.append(("C tabla", "L%d" % i))
        if re.search(r"<br|<!--|<b>", l, re.I): flags.append(("C html", "L%d" % i))
    if "\n\n\n" in d: flags.append(("C triple blank", "x%d" % d.count("\n\n\n")))
    if "───────────────────\n\n───────────────────" in d: flags.append(("C sep doble", "sí"))
    # D · rancios y erratas conocidas
    for pat in ["bañquitos", " numero ", "enseñarnos", "honesty", "v2.1.5, la última",
                "hoy entregó dos", "hoy: v2.1.", "fix del import local de hoy"]:
        if pat in d: flags.append(("D rancio", repr(pat)))
    # E · racha de PROSA sin aire (>12)
    run = 0; rs = 0
    for i, l in enumerate(L, 1):
        if infence(i-1) or l.startswith("• ") or isnum(l):
            if run > 12: flags.append(("E racha>%d" % run, "desde L%d" % rs))
            run = 0; continue
        if l.strip() and l.strip() != "───────────────────":
            if run == 0: rs = i
            run += 1
        else:
            if run > 12: flags.append(("E racha>%d" % run, "desde L%d" % rs))
            run = 0
    # F · árbol ↔ cuerpo: tallos de cada rama, en orden, en ventana
    body_only = [l for l in L if not l.strip().startswith(("├──", "└──"))]
    STOP = set("de la el los las que y en a con por para un una al lo se su sin es este esta esto ese esa esos esas eso todo toda todos todas más mas pero como cuando donde quien son hay sobre entre desde hasta cada dos tres cuatro cinco seis siete ocho nueve diez once doce veinte".split())
    def stems(txt):
        txt = re.sub(r"[^\wÁÉÍÓÚáéíóúñÑüÜ]+", " ", txt)
        return [w.lower()[:6] for w in txt.split() if w.lower() not in STOP and len(w) > 3]
    headers_b = [l for l in body_only if re.match(r"^\*[\U0001F300-\U0001FAFF\u2600-\u27BF]", l)]
    last_idx = -1
    for t in [l for l in L if l.strip().startswith(("├──", "└──")) and "~" in l]:
        title = re.sub(r"^[├└]── ", "", t).split("  · ")[0].strip()
        pend = list(stems(title)); hit = -1
        for j in range(last_idx+1, len(headers_b)):
            bs = stems(headers_b[j])
            m = [p for p in pend if any(w.startswith(p) or p.startswith(w) for w in bs)]
            for p in m: pend.remove(p)
            if not pend: hit = j; break
        if hit < 0: flags.append(("F árbol↛cuerpo", repr(title[:30])))
        else: last_idx = hit
    # G · quiz round-trip
    qs = [l for l in L if l.startswith("`") and len(l) > 3 and l[2] == "."]
    for k in quiz_keys:
        if not any(k in q.strip("`")[::-1] for q in qs):
            flags.append(("G quiz", "clave no recobrada: %r" % k))
    # H · Σ minutos = header
    mins = [int(x) for x in re.findall(r"· ~(\d+) min", d)]
    mh = re.search(r"Lectura total: (\d+) min", d)
    h = int(mh.group(1)) if mh else -1
    if sum(mins) != h: flags.append(("H Σ≠header", "Σ=%d header=%d" % (sum(mins), h)))
    # I · emoji doble en ramas del árbol
    ems = []
    for t in [l for l in L if l.strip().startswith(("├──", "└──"))]:
        ems += re.findall(r"[\U0001F300-\U0001FAFF\u2600-\u27BF]", t)
    for e in set(ems):
        if ems.count(e) > 1: flags.append(("I emoji doble", "%s x%d" % (e, ems.count(e))))
    # J · cronología: fechas futuras y «hoy» amarrado a fecha vieja
    cy, cm, cd = cut
    for i, l in enumerate(L, 1):
        if infence(i-1): continue
        dts = parse_dates(l)
        if not dts: continue
        for (dd, mm, yy), tok, _sp in dts:
            if (yy and yy > cy) or ((yy in (None, cy)) and (mm, dd) > (cm, cd)):
                flags.append(("J fecha futura", "L%d %s" % (i, tok)))
        for hm in re.finditer(r"\bhoy\b", l, re.I):
            near = any(((dd, mm) == (cd, cm)) and abs(sp - hm.start()) <= 60 for (dd, mm, yy), _t, sp in dts)
            old = any(((dd, mm) != (cd, cm)) and abs(sp - hm.start()) <= 60 for (dd, mm, yy), _t, sp in dts)
            if old and not near:
                flags.append(("J hoy rancio", "L%d: %s" % (i, l[:55])))
        if re.search(r"\bhoy\b", l, re.I): report["hoy"].append("L%d: %s" % (i, l[:60]))
    # K · vintage: estrella de pulso sin fecha de constancia en su línea
    for i, l in enumerate(L, 1):
        if infence(i-1) or l.strip().startswith(("├──", "└──")): continue
        if re.search(r"★\s?[0-9][\d.,]*\s*k?", l):
            dateish = re.search(r"\b\d{1,2}-(?:ene|feb|mar|abr|may|jun|jul|ago|sep|oct|nov|dic)|\b\d{4}\b|\bhoy\b|constad", l, re.I)
            if not dateish:
                flags.append(("K sin vintage", "L%d: %s" % (i, l[:55])))
            report["estrellas"].append("L%d %s: %s" % (i, "✓" if dateish else "SIN FECHA", l[:50]))
    # L · eco: n-grama de 7 palabras repetido en ≥2 líneas (fuera de vallas/árbol/tags)
    grams = {}
    for i, l in enumerate(L, 1):
        if infence(i-1) or l.strip().startswith(("├──", "└──", "`", "#")): continue
        w = re.findall(r"\w+", l.lower())
        seen_in_line = set()
        for g in zip(*(w[k:] for k in range(7))):
            if g not in seen_in_line:
                grams.setdefault(g, set()).add(i); seen_in_line.add(g)
    for g, ls in grams.items():
        if len(ls) >= 2:
            flags.append(("L eco", "%s… en L%s" % (" ".join(g)[:48], ",".join(map(str, sorted(ls)[:4])))))
    # M · cadencia: párrafo con ≥4 frases de largo casi idéntico (dron)
    para = []; ps = 0
    def close_para():
        if len(para) >= 4:
            lens = [len(s) for s in para]; mu = statistics.mean(lens)
            if mu > 30 and statistics.pstdev(lens)/mu < 0.18:
                flags.append(("M cadencia", "L%d dron de %d frases (cv=%.2f)" % (ps, len(para), statistics.pstdev(lens)/mu)))
    for i, l in enumerate(L, 1):
        if infence(i-1) or l.startswith(("•", ">")) or isnum(l) or not l.strip() or l.strip() == "───────────────────" or l.strip().startswith(("├", "└")):
            close_para(); para = []; continue
        if not para: ps = i
        para += [s for s in re.split(r"(?<=[.!?»])\s+", l) if len(s) > 12]
    close_para()
    # N · marcadores: asteriscos impares por línea; vallas ``` en número impar
    for i, l in enumerate(L, 1):
        if infence(i-1): continue
        if l.count("*") % 2: flags.append(("N aster", "L%d: %s" % (i, l[:45])))
    if len(fences) % 2: flags.append(("N fence", "vallas ``` impares (%d)" % len(fences)))
    # O · #tags solo al final (ventana de 12 líneas)
    for i, l in enumerate(L):
        if infence(i) : continue
        if i < len(L)-12 and re.search(r"(?<![\w/#])#[A-Za-zÁÉÍÓÚáéíóúñÑ]\w+", l):
            flags.append(("O tag", "L%d (no es final): %s" % (i+1, l[:45])))
    # P · separadores homogéneos (la casa manda un largo canónico)
    divs = [len(l.strip()) for l in L if re.fullmatch(r"─+", l.strip())]
    if divs:
        canon = max(set(divs), key=divs.count)
        for i, l in enumerate(L, 1):
            if re.fullmatch(r"─+", l.strip()) and len(l.strip()) != canon:
                flags.append(("P separador", "L%d len=%d (canon=%d)" % (i, len(l.strip()), canon)))
    return flags, report

# ─── MUTACIONES: 27 defectos inyectados. Si uno escapa, la lupa no se usa. ───
def _feasible(expect, d):
    """Cicatriz 15-oct: una mutación sin alcance real en el host no es fuga, se declara."""
    if expect.startswith("C mono"):
        return d.count("```") >= 2
    if expect.startswith("N fence"):
        return "```" in d
    if expect.startswith("C sep doble"):
        return re.search(r"^─{2,}$", d, 8) is not None
    if expect.startswith("I emoji") or expect.startswith("F árbol"):
        return any(re.match(r"^├── |^└── ", l) for l in d.split("\n"))
    return True

def _echo_src(d):
    for ln in d.split("\n"):
        if "dueño conocido" in ln:
            w = re.findall(r"\w+", ln.lower())
            if len(w) >= 8: return " ".join(w[:9])
    for ln in d.split("\n"):
        if ln.strip() and not ln.strip().startswith(("├","└","```","|","#","•","![",">")):
            w = re.findall(r"\w+", ln.lower())
            if len(w) >= 9: return " ".join(w[:9])
    return "la vara de esta casa mide con fecha y con hora puesta"

MUTATIONS = [
    ("m1 prosa 500c",      lambda d: d + "\n" + "X"*500 + "\n", "A unidad>280"),
    ("m2 bala 400c",       lambda d: d + "\n• " + "Y"*400 + "\n", "A unidad>280"),
    ("m3 balas apiladas",  lambda d: d + "\n• " + "a"*200 + "\n• " + "b"*200 + "\n", "B apilada"),
    ("m4 comilla recta",   lambda d: d.replace("\n\n", '\n\n"treta"\n\n', 1), "C recta"),
    ("m5 backtick impar",  lambda d: d.replace("\n\n", "\n\nlinea con ` suelto\n\n", 1), "C backtick"),
    ("m6 meta ##",         lambda d: d.replace("\n\n", "\n\n## Hola\n\n", 1), "C meta"),
    ("m7 link md",         lambda d: d.replace("\n\n", "\n\n[x](y)\n\n", 1), "C linkmd"),
    ("m8 tabla",           lambda d: d.replace("\n\n", "\n\n| a | b |\n\n", 1), "C tabla"),
    ("m9 sep doble",       lambda d: d.replace("───────────────────\n\n", "───────────────────\n\n───────────────────\n\n", 1), "C sep doble"),
    ("m10 triple blank",   lambda d: d.replace("\n\n", "\n\n\n", 1), "C triple blank"),
    ("m11 rancio hoy v2.1",lambda d: d.replace("\n\n", "\n\nhoy: v2.1.5 salio\n\n", 1), "D rancio"),
    ("m12 bañquitos",      lambda d: d.replace("\n\n", "\n\nreparto de bañquitos\n\n", 1), "D rancio"),
    ("m13 mono 80c",       lambda d: d.replace("```\n", "```\n" + "Z"*80 + "\n", 1), "C mono>64"),
    ("m14 header roto",    lambda d: re.sub(r"Lectura total: \d+ min", "Lectura total: 99 min", d), "H Σ≠header"),
    ("m15 quiz castrado",  None, "G quiz"),
    ("m16 rama fantasma",  lambda d: __import__("re").sub(r"^(├── [^\n]*· ~\d+ min)$", r"├── 🧪 Rama fantasma inexistente — \1", d, count=1, flags=re.M), "F árbol"),
    ("m17 racha 15 prosa", lambda d: d.replace("\n\n", "\n" + "\n".join(c*90 for c in "pqrstuvwxy1234") + "\n\n", 1), "E racha"),
    ("m18 emoji doble",    lambda d: re.sub(r"^└── ", "└── 🧪 ", re.sub(r"^├── ", "├── 🧪 ", d, count=1, flags=re.M), count=1, flags=re.M), "I emoji"),
    ("m19 fecha futura",   lambda d: d + "\n• Corre que llega: la entrega es el 20-nov-2026.\n", "J fecha"),
    ("m20 hoy rancio",     lambda d: d + "\n• Abierto hoy 22-sep-2026 para probar.\n", "J hoy"),
    ("m21 star sin fecha", lambda d: d + "\n• Sube ya: ★40.000.\n", "K sin vintage"),
    ("m22 eco 7 palabras", lambda d: d + "\n\n" + _echo_src(d) + "\n", "L eco"),
    ("m23 dron cadencia",  lambda d: d + "\n\nEl vecino mide su vara con calma cada mañana de trabajo.\nEl vecino guarda su vara en el cajón cada noche serena.\nEl vecino pide su vara prestada al vecino del quinto piso.\nEl vecino devuelve su vara pulida al dueño del taller del barrio.\n", "M cadencia"),
    ("m24 aster impar",    lambda d: d.replace("\n\n", "\n\n• linea con * impar sin cerrar\n\n", 1), "N aster"),
    ("m25 fence impar",    lambda d: d.replace("```", "```\n```", 1), "N fence"),
    ("m26 tag temprano",   lambda d: d.replace("\n\n", "\n\n#Infrito en el cuerpo\n\n", 1), "O tag"),
    ("m27 separador raro", lambda d: d if not __import__("re").search(r"^─{2,}$", d, 8) else d.replace("\n\n", "\n\n────────\n\n", 1), "P separador"),
]

def _autokeys(d):
    ks = []
    for q in [l for l in d.split("\n") if l.startswith("`") and len(l) > 4 and l[2] == "."]:
        plain = q.strip("`")[::-1]
        ws = sorted((x for x in re.findall(r"\w{6,}", plain)), key=len, reverse=True)
        if ws: ks.append(ws[0])
    return ks[:4]

def run_mutate(path, quiz_keys, cut):
    d0 = open(path, encoding="utf-8").read(); ok = 0; skipped = 0
    if not quiz_keys:
        quiz_keys = _autokeys(d0)
    for name, fn, expect in MUTATIONS:
        if fn is None and not quiz_keys:
            print("  - m15 quiz castrado    → OMITIDA (host sin quiz ni claves)")
            skipped += 1; continue
        if fn is None:
            dd = d0
            done = False
            for q in [l for l in dd.split("\n") if l.startswith("`") and len(l) > 3 and l[2] == "."]:
                for k in quiz_keys:
                    if k in q.strip("`")[::-1]:
                        plain = q.strip("`")[::-1].replace(k, "X")
                        dd = dd.replace(q, "`" + plain[:-2][::-1] + "..`", 1)
                        done = True; break
                if done: break
            fn = (lambda dd: (lambda x: dd))(dd)
        if not _feasible(expect, d0):
            print("  - %-20s → OMITIDA (alcance ausente en el host)" % name)
            skipped += 1; continue
        d1 = fn(d0)
        if d1 == d0:
            print("  - %-20s → OMITIDA (ancla ausente en el host)" % name)
            skipped += 1; continue
        got = {k for k, _ in detect(d1, quiz_keys, cut)[0]}
        hit = any(g.startswith(expect) for g in got)
        ok += hit
        print("  %s %-20s → [%s] %s" % ("✓" if hit else "✗ FUGA", name, expect, "" if hit else "obtuve %s" % sorted(got)))
    print("MUTACIÓN: %d/%d cazadas" % (ok, len(MUTATIONS)-skipped))
    return ok == len(MUTATIONS)-skipped

def live_pulse(path, token):
    import json, urllib.request, os, traceback
    d = open(path, encoding="utf-8").read(); L = d.split("\n")
    fences = [i for i, l in enumerate(L) if l.strip() == "```"]
    def infence(i):
        if len(fences) % 2 == 1:
            return False  # valla impar = paridad corrupta: TODO en crudo (cicatriz fuzz 58/60 del 15-oct)
        return sum(1 for f in fences if f < i) % 2 == 1
    repos = []
    for i, l in enumerate(L):
        if infence(i): continue
        for m in re.finditer(r"github\.com/([\w.-]+)/([\w.-]+)", l):
            r = (m.group(1), m.group(2))
            if r not in repos: repos.append(r)
    hdr = {"User-Agent": "lupa-bandita-v4"}
    if token: hdr["Authorization"] = "token " + token
    print("Q · PULSO VIVO (informe; jamás auto-aprueba) — %d repos:" % min(len(repos), 6))
    err_shown = False
    for owner, name in repos[:6]:
        try:
            req = urllib.request.Request("https://api.github.com/repos/%s/%s" % (owner, name), headers=hdr)
            with urllib.request.urlopen(req, timeout=10) as resp:
                j = json.loads(resp.read().decode("utf-8"))
            est = "★%s" % format(int(j.get("stargazers_count", 0)), ",")
            push = (j.get("pushed_at") or "")[:10]
            claim = "?"
            for i2, l2 in enumerate(L):
                if ("%s/%s" % (owner, name)) in l2:
                    mc = re.search(r"★\s?([\d.,]+)", "\n".join(L[max(0, i2-3):i2+4]))
                    if mc: claim = "★" + mc.group(1)
                    break
            print("  %s/%s — vivo %s · push %s · pieza dice %s" % (owner, name, est, push, claim))
        except Exception as e:
            print("  %s/%s — sin pulso (%s)" % (owner, name, str(e)[:60]))
            if not err_shown:
                traceback.print_exc(); err_shown = True

if __name__ == "__main__":
    path = sys.argv[1]
    d = open(path, encoding="utf-8").read()
    quiz_keys = sys.argv[sys.argv.index("--keys")+1].split("|") if "--keys" in sys.argv else []
    cut = (2026, 10, 15)
    if "--cutover" in sys.argv:
        y, m, dd = map(int, sys.argv[sys.argv.index("--cutover")+1].split("-")); cut = (y, m, dd)
    if "--mutate" in sys.argv:
        sys.exit(0 if run_mutate(path, quiz_keys, cut) else 1)
    if "--live" in sys.argv:
        tok = None
        if "--token" in sys.argv: tok = sys.argv[sys.argv.index("--token")+1]
        import os
        live_pulse(path, tok or os.environ.get("GITHUB_TOKEN"))
        sys.exit(0)
    flags, report = detect(d, quiz_keys, cut)
    print("ALERTAS:", len(flags))
    for k, v in flags: print("  [%s] %s" % (k, v))
    if report["hoy"]:
        print("INFORME «hoy» (para la pasada fluida): %d" % len(report["hoy"]))
        for x in report["hoy"][:12]: print("  ·", x)
    if report["estrellas"]:
        sinv = [x for x in report["estrellas"] if "SIN FECHA" in x]
        print("INFORME estrellas: %d líneas · %d sin fecha" % (len(report["estrellas"]), len(sinv)))
    n = len(d); s = hashlib.sha256(d.encode()).hexdigest()[:16]
    print("TOTAL: %d c · banda: %s · sello: %s" % (n, "DENTRO ✓" if 62000 <= n <= 64000 else "FUERA", s))
