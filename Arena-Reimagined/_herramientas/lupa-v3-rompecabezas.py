# -*- coding: utf-8 -*-
"""
LUPA v3 del rompecabezas — La Bandita (15-oct-2026)
Regla de cero absoluto de falsas aprobaciones:
  1) Detectores ANCHOS (atrapan de más, jamás de menos).
  2) Toda unidad >280c se lista COMPLETA: cada alerta recibe veredicto
     por CONTENIDO (registrado en acta), nunca por clase de patrón.
  3) La lupa se prueba por MUTACIÓN: defectos inyectados deben ser
     cazados 100%. Si uno escapa, la lupa está PROHIBIDA hasta corregirla.
Uso:
  python3 lupa-v3-rompecabezas.py PIEZA.md            # audita
  python3 lupa-v3-rompecabezas.py PIEZA.md --mutate   # prueba la propia lupa
"""
import re, sys, hashlib

def detect(d, quiz_keys=(), header_min=None):
    L = d.split("\n")
    flags = []
    fences = [i for i, l in enumerate(L) if l.strip() == "```"]
    def infence(i):  # i 0-based
        return sum(1 for f in fences if f < i) % 2 == 1
    # A) unidades >280c (prosa, balas, numeradas) — lista completa
    for i, l in enumerate(L, 1):
        if infence(i - 1):
            if len(l) > 64:
                flags.append(("C mono>64", "L%d %dc" % (i, len(l))))
            continue
        if len(l) > 280:
            kind = "bala" if l.startswith("• ") else "num" if l[:2] in ("1.", "2.", "3.", "4.", "5.", "6.", "7.") else "prosa"
            flags.append(("A unidad>280", "L%d %dc [%s] %s" % (i, len(l), kind, l[:60])))
    # B) balas apiladas sin aire (ambas >120c)
    for i in range(1, len(L)):
        if L[i].startswith("• ") and L[i-1].startswith("• ") and len(L[i]) > 120 and len(L[i-1]) > 120:
            flags.append(("B apilada", "L%d/L%d (%dc+%dc)" % (i, i + 1, len(L[i-1]), len(L[i]))))
    # C) durezas carácter-a-carácter
    for i, l in enumerate(L, 1):
        if infence(i - 1):
            continue
        if '"' in l:
            flags.append(("C recta", "L%d" % i))
        if l.strip() != "```" and l.count("`") % 2:
            flags.append(("C backtick", "L%d" % i))
        if re.match(r"^#{1,6}\s", l):
            flags.append(("C meta", "L%d" % i))
        if "](" in l:
            flags.append(("C linkmd", "L%d" % i))
        if l.strip().startswith("|"):
            flags.append(("C tabla", "L%d" % i))
        if re.search(r"<br|<!--|<b>", l, re.I):
            flags.append(("C html", "L%d" % i))
    if "\n\n\n" in d:
        flags.append(("C triple blank", "x%d" % d.count("\n\n\n")))
    if "───────────────────\n\n───────────────────" in d:
        flags.append(("C sep doble", "sí"))
    # D) rancios y erratas conocidas
    for pat in ["bañquitos", " numero ", "enseñarnos", "honesty",
                "v2.1.5, la última", "hoy entregó dos", "hoy: v2.1.",
                "fix del import local de hoy"]:
        if pat in d:
            flags.append(("D rancio", repr(pat)))
    # E) racha de PROSA sin aire (>12 líneas sin bala/valla/numerada)
    run = 0; rs = 0
    for i, l in enumerate(L, 1):
        if infence(i - 1) or l.startswith("• ") or l[:2] in ("1.", "2.", "3.", "4.", "5.", "6.", "7."):
            if run > 12:
                flags.append(("E racha>%d" % run, "desde L%d" % rs))
            run = 0
            continue
        if l.strip() and l.strip() != "───────────────────":
            if run == 0:
                rs = i
            run += 1
        else:
            if run > 12:
                flags.append(("E racha>%d" % run, "desde L%d" % rs))
            run = 0
    # F) árbol → cuerpo: cada título de rama con minutos debe existir en el cuerpo
    body_only = [l for l in L if not l.strip().startswith(("├──", "└──"))]
    STOP = set("de la el los las que y en a con por para un una al lo se su sin es".split())
    def stems(txt):
        txt = re.sub(r"[^\wÁÉÍÓÚáéíóúñÑüÜ]+", " ", txt)
        return [w.lower()[:6] for w in txt.split() if w.lower() not in STOP and len(w) > 3]
    last_idx = -1
    for t in [l for l in L if l.strip().startswith(("├──", "└──")) and "~" in l]:
        title = re.sub(r"^[├└]── ", "", t).split("  · ")[0].strip()
        pend = list(stems(title))
        hit = -1
        for j in range(last_idx + 1, len(body_only)):
            bs = stems(body_only[j])
            m = [p for p in pend if any(w.startswith(p) or p.startswith(w) for w in bs)]
            for p in m:
                pend.remove(p)
            if not pend:
                hit = j
                break
        if hit < 0:
            flags.append(("F árbol↛cuerpo", repr(title[:30])))
        else:
            last_idx = hit
    # I) emojis de rama del árbol: únicos (dos ramas, un emoji = confusión)
    ems = []
    for t in [l for l in L if l.strip().startswith(("├──", "└──"))]:
        e = re.findall(r"[\U0001F300-\U0001FAFF\u2600-\u27BF]", t)
        ems += e
    for e in set(ems):
        if ems.count(e) > 1:
            flags.append(("I emoji doble", "%s x%d" % (e, ems.count(e))))
    # G) quiz: cada respuesta invertida debe recobrar su clave al girarla
    qs = [l for l in L if l.startswith("`") and len(l) > 3 and l[1] in "123456789" and l[2] == "."]
    for k in quiz_keys:
        if not any(k in q.strip("`")[::-1] for q in qs):
            flags.append(("G quiz", "clave no recobrada: %r" % k))
    # H) Σ minutos del árbol = header
    mins = [int(x) for x in re.findall(r"· ~(\d+) min", d)]
    h = header_min if header_min else (int(re.search(r"Lectura total: (\d+) min", d).group(1)) if re.search(r"Lectura total: (\d+) min", d) else -1)
    if sum(mins) != h:
        flags.append(("H Σ≠header", "Σ=%d header=%d" % (sum(mins), h)))
    return flags

MUTATIONS = [
    ("m1 prosa 500c",       lambda d: d + "\n" + "X" * 500 + "\n", "A unidad>280"),
    ("m2 bala 400c",        lambda d: d + "\n• " + "Y" * 400 + "\n", "A unidad>280"),
    ("m3 balas apiladas",   lambda d: d + "\n• " + "a" * 200 + "\n• " + "b" * 200 + "\n", "B apilada"),
    ("m4 comilla recta",    lambda d: d.replace("\n\n", '\n\n"treta"\n\n', 1), "C recta"),
    ("m5 backtick impar",   lambda d: d.replace("\n\n", "\n\nlinea con ` suelto\n\n", 1), "C backtick"),
    ("m6 meta ##",          lambda d: d.replace("\n\n", "\n\n## Hola\n\n", 1), "C meta"),
    ("m7 link md",          lambda d: d.replace("\n\n", "\n\n[x](y)\n\n", 1), "C linkmd"),
    ("m8 tabla",            lambda d: d.replace("\n\n", "\n\n| a | b |\n\n", 1), "C tabla"),
    ("m9 sep doble",        lambda d: d.replace("───────────────────\n\n", "───────────────────\n\n───────────────────\n\n", 1), "C sep doble"),
    ("m10 triple blank",    lambda d: d.replace("\n\n", "\n\n\n", 1), "C triple blank"),
    ("m11 rancio hoy v2.1", lambda d: d.replace("\n\n", "\n\nhoy: v2.1.5 salio\n\n", 1), "D rancio"),
    ("m12 bañquitos",       lambda d: d.replace("\n\n", "\n\nreparto de bañquitos\n\n", 1), "D rancio"),
    ("m13 mono 80c",        lambda d: d.replace("```\n", "```\n" + "Z" * 80 + "\n", 1), "C mono>64"),
    ("m14 header roto",     lambda d: re.sub(r"Lectura total: \d+ min", "Lectura total: 99 min", d), "H Σ≠header"),
    ("m15 quiz castrado",   None, "G quiz"),  # se inyecta aparte (necesita claves)
    ("m16 rama fantasma",   lambda d: d.replace("├── ", "├── 🧪 Rama fantasma inexistente — ", 1) if "├── " in d else d, "F árbol↛cuerpo"),
    ("m17 racha 15 prosa",  lambda d: d.replace("\n\n", "\n" + "p" * 90 + "\n" + "q" * 90 + "\n" + "r" * 90 + "\n" + "s" * 90 + "\n" + "t" * 90 + "\n" + "u" * 90 + "\n" + "v" * 90 + "\n" + "w" * 90 + "\n" + "x" * 90 + "\n" + "y" * 90 + "\n" + "z" * 90 + "\n" + "1" * 90 + "\n" + "2" * 90 + "\n" + "3" * 90 + "\n" + "4" * 90 + "\n\n", 1), "E racha"),
    ("m18 emoji doble",     lambda d: d.replace("├── ", "├── 🧪 ", 1).replace("└── ", "└── 🧪 ", 1) if "└── " in d else d, "I emoji doble"),
]

def run_mutate(path, quiz_keys):
    d0 = open(path, encoding="utf-8").read()
    ok = 0; total = 0
    for name, fn, expect in MUTATIONS:
        total += 1
        if fn is None:  # m15: romper la PRIMERA clave del quiz real
            dd = d0
            for q in [l for l in dd.split("\n") if l.startswith("`") and len(l) > 3 and l[2] == "."]:
                if quiz_keys and quiz_keys[0] in q.strip("`")[::-1]:
                    bad = q.strip("`")[::-1].replace(quiz_keys[0], "X")[:-2][::-1] + ".."
                    dd = dd.replace(q, "`" + bad + "`", 1)
                    break
            fn = (lambda dd: (lambda d: dd))(dd)
        dm = fn(d0)
        got = {k for k, _ in detect(dm, quiz_keys)}
        hit = any(g.startswith(expect) for g in got)
        ok += hit
        print("  %s %-20s → esperado [%s] %s" % ("✓" if hit else "✗ FUGA", name, expect, "" if hit else "obtuve %s" % sorted(got)))
    print("MUTACIÓN: %d/%d cazadas" % (ok, total))
    return ok == total

if __name__ == "__main__":
    path = sys.argv[1]
    d = open(path, encoding="utf-8").read()
    quiz_keys = []
    if "--keys" in sys.argv:
        quiz_keys = sys.argv[sys.argv.index("--keys") + 1].split("|")
    if "--mutate" in sys.argv:
        sys.exit(0 if run_mutate(path, quiz_keys) else 1)
    f = detect(d, quiz_keys)
    print("ALERTAS:", len(f))
    for k, v in f:
        print("  [%s] %s" % (k, v))
    n = len(d); s = hashlib.sha256(d.encode()).hexdigest()[:16]
    print("TOTAL: %d c · banda: %s · sello: %s" % (n, "DENTRO ✓" if 62000 <= n <= 64000 else "FUERA", s))
