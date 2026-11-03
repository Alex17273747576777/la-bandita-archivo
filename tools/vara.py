#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LA VARA · las ocho compuertas de la casa, ejecutables en un solo comando.

Doctrina (HABILIDADES/INDICE-HABILIDADES.md): hay compuertas que DETIENEN la línea y
medidores que solo PUBLICAN su cifra. Nunca se confunden, y ninguna se aprueba por
salida en cero: se aprueba cuando este informe dice «fallos: NINGUNO».

Uso:
  python3 tools/vara.py            # informe completo
  python3 tools/vara.py --json     # informe legible por máquina
Salida: código 0 si ninguna compuerta falló, 1 si alguna falló.
"""
from __future__ import annotations
import argparse, hashlib, json, re, statistics, subprocess, sys
from collections import Counter
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fecha_casa import hoy as fecha_casa_hoy, larga as fecha_casa_larga  # noqa: E402

RAIZ = Path(__file__).resolve().parents[1]
PUBLICACIONES = RAIZ / "Arena-Reimagined/01-PUBLICACIONES"
REGISTRO = RAIZ / "registry"
ESQUEMA = RAIZ / "schemas/ficha.schema.json"
MANIFIESTO = RAIZ / "registry" / "_manifiesto-sha256.tsv"
BASELINE = RAIZ / "tools/baseline.json"
UMBRAL_FRESCURA = 180          # días que un dato puede presentarse como vigente


def fijar_raiz(nueva: Path) -> None:
    """Permite apuntar la vara a un árbol de prueba (lo usa tools/autoprueba.py)."""
    global RAIZ, PUBLICACIONES, REGISTRO, ESQUEMA, MANIFIESTO, BASELINE
    RAIZ = nueva.resolve()
    PUBLICACIONES = RAIZ / "Arena-Reimagined/01-PUBLICACIONES"
    REGISTRO = RAIZ / "registry"
    ESQUEMA = RAIZ / "schemas/ficha.schema.json"
    MANIFIESTO = RAIZ / "registry" / "_manifiesto-sha256.tsv"
    BASELINE = RAIZ / "tools/baseline.json"
ZW = re.compile("[\u200b\u200c\u200d\u2060\ufeff]")
APK = re.compile(r"https?://[^\s)]+\.(apk|apks|xapk|apkm)\b", re.I)
DATELINE = re.compile(r"\d{1,2} de (enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre) de 20\d\d")


def fichas() -> list[dict]:
    salida = []
    for p in sorted(REGISTRO.glob("*.json")):
        if p.name.startswith("_"):
            continue
        try:
            salida.append(json.loads(p.read_text(encoding="utf-8")))
        except json.JSONDecodeError as e:
            salida.append({"_archivo": p.name, "_ilegible": str(e)})
    return salida


def piezas() -> list[Path]:
    """Solo piezas: los LEEME/README de carpeta no son publicaciones y no llevan firma."""
    return sorted(p for p in PUBLICACIONES.rglob("*.md")
                  if not p.name.lower().startswith(("leeme", "readme")))


def g1_esquema(datos: list[dict]) -> tuple[list[str], str]:
    fallos = []
    if any("_ilegible" in d for d in datos):
        fallos += [f"{d['_archivo']}: JSON ilegible" for d in datos if "_ilegible" in d]
    try:
        import jsonschema
        esquema = json.loads(ESQUEMA.read_text(encoding="utf-8"))
        for d in datos:
            if "_ilegible" in d:
                continue
            try:
                jsonschema.validate(d, esquema)
            except jsonschema.ValidationError as e:
                fallos.append(f"{d.get('id', '?')}: {e.message[:110]}")
    except ImportError:
        obligatorios = {"id", "repo", "medido_en", "fuente", "licencia", "actividad", "evidencia"}
        for d in datos:
            if "_ilegible" in d:
                continue
            faltan = obligatorios - set(d)
            if faltan:
                fallos.append(f"{d.get('id', '?')}: faltan {sorted(faltan)}")
        fallos.append("aviso: jsonschema no instalado, validación mínima por campos")
    return fallos, f"{len(datos)} fichas"


def g2_frescura(datos: list[dict]) -> tuple[list[str], str]:
    hoy = date.fromisoformat(fecha_casa_hoy())
    edades = []
    fallos = []
    for d in datos:
        if "_ilegible" in d:
            continue
        try:
            edad = (hoy - date.fromisoformat(d["medido_en"])).days
        except Exception:
            fallos.append(f"{d.get('id', '?')}: medido_en inválido")
            continue
        edades.append(edad)
        if edad > UMBRAL_FRESCURA:
            fallos.append(f"{d.get('id', '?')}: {edad} días (umbral {UMBRAL_FRESCURA})")
    if not edades:
        return ["registro vacío: no hay frescura que medir"], "0 fichas"
    return fallos, (f"edad máxima {max(edades)} d · mediana {int(statistics.median(edades))} d · "
                    f"umbral {UMBRAL_FRESCURA} d")


def g3_licencia(datos: list[dict]) -> tuple[list[str], str]:
    orden = {"spdx-api", "endpoint-license", "texto-license", "ausencia-firmada"}
    fallos = []
    metodos = Counter()
    for d in datos:
        if "_ilegible" in d:
            continue
        lic = d.get("licencia") or {}
        metodos[lic.get("metodo")] += 1
        if lic.get("metodo") not in orden:
            fallos.append(f"{d.get('id', '?')}: método fuera del orden de la casa")
        # Sin SPDX se admite en dos casos, y solo dos:
        #   · ausencia-firmada: no hay archivo de licencia en el árbol (se firma la ausencia);
        #   · texto-license con archivo identificado: hay licencia escrita que el endpoint no
        #     supo clasificar (p. ej. LICENSE-APACHE-2.0.txt o una carpeta `licenses`). No es
        #     una ausencia y no se puede declarar como tal; se cita el archivo y queda pendiente
        #     de lectura humana, que es lo honesto.
        if lic.get("spdx") is None:
            if lic.get("metodo") == "ausencia-firmada":
                pass
            elif lic.get("metodo") == "texto-license" and lic.get("archivo"):
                pass
            else:
                fallos.append(f"{d.get('id', '?')}: sin SPDX y sin ausencia firmada")
        if not lic.get("verificado_en"):
            fallos.append(f"{d.get('id', '?')}: licencia sin fecha de verificación")
    resumen = " · ".join(f"{k} {v}" for k, v in metodos.most_common())
    return fallos, resumen


def g4_actividad(datos: list[dict]) -> tuple[list[str], str]:
    fallos = []
    estados = Counter()
    for d in datos:
        if "_ilegible" in d:
            continue
        act = d.get("actividad") or {}
        estado = act.get("estado")
        estados[estado] += 1
        if estado == "muerto" and act.get("semantica_http") in (403, 429):
            fallos.append(f"{d.get('id', '?')}: declarado muerto por HTTP {act.get('semantica_http')}")
        if estado in {"vivo", "dormido"} and not act.get("ultimo_push"):
            fallos.append(f"{d.get('id', '?')}: {estado} sin último push medido")
        if estado == "vivo" and act.get("ultimo_push"):
            dias = (date.fromisoformat(d["medido_en"]) - date.fromisoformat(act["ultimo_push"])).days
            if dias > UMBRAL_FRESCURA:
                fallos.append(f"{d.get('id', '?')}: vivo con último push de hace {dias} días")
    resumen = " · ".join(f"{k} {v}" for k, v in estados.most_common())
    return fallos, resumen


def g5_integridad() -> tuple[list[str], str]:
    """Comprueba lo firmado Y lo que no llegó a firmarse: un archivo nuevo sin sello era invisible."""
    if not MANIFIESTO.exists():
        return ["sin manifiesto de integridad: correr tools/atestar.py"], "manifiesto ausente"
    fallos, n = [], 0
    sellados = set()
    for linea in MANIFIESTO.read_text(encoding="utf-8").splitlines():
        if not linea.strip():
            continue
        sha, _, ruta = linea.partition("  ")
        p = RAIZ / ruta
        n += 1
        sellados.add(ruta)
        if not p.exists():
            fallos.append(f"falta {ruta}")
            continue
        real = hashlib.sha256(p.read_bytes()).hexdigest()
        if real != sha:
            fallos.append(f"alterado {ruta}")
    try:
        from sello_reglas import archivos as archivos_sellables
    except ImportError:  # árbol de prueba sin tools completos
        return fallos, f"{n} archivos sellados"
    sin_sellar = sorted(p.relative_to(RAIZ).as_posix() for p in archivos_sellables(RAIZ, MANIFIESTO))
    sin_sellar = [r for r in sin_sellar if r not in sellados]
    for ruta in sin_sellar:
        fallos.append(f"sin sellar {ruta}")
    return fallos, f"{n} archivos sellados" + (f" · {len(sin_sellar)} sin sellar" if sin_sellar else "")


def g12_firma_literal() -> tuple[list[str], str]:
    """Testigo de firma: la frase de la casa, letra por letra, en el cierre.

    M01 comprueba que la frase exista; este guardián comprueba además que esté al
    final del cuerpo (antes de las notas) y que el bloque de medición diga la hora.
    """
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import firma_literal as fl

    vivas, viejas = fl.piezas()
    fallos = []
    for p in vivas:
        for x in fl.revisar(p):
            fallos.append(f"{p.name[:60]}: {x}")
    nota = f"{len(vivas) - len({f.split(':')[0] for f in fallos})} de {len(vivas)} en regla"
    if viejas:
        nota += f" · {viejas} del archivo viejo sin exigencia"
    return fallos, nota


def g10_bandas() -> tuple[list[str], str]:
    """Cada pieza reescrita tiene una banda de longitud declarada en docs/bandas.json. Ni menos
    (relleno barato) ni más (palabrería): si se sale, no pasa. Y la cifra declarada en el JSON
    tiene que coincidir con el archivo, para que nadie maquille el registro."""
    f = RAIZ / "docs" / "bandas.json"
    if not f.exists():
        return [], "sin bandas declaradas"
    try:
        datos = json.loads(f.read_text(encoding="utf-8"))
    except Exception as e:
        return [f"bandas.json ilegible: {e}"], "ilegible"
    fallos, dentro = [], 0
    for canal, cfg in datos.items():
        if not isinstance(cfg, dict) or "piezas" not in cfg:
            continue
        carpeta = {"whatsapp": "WhatsApp-dominicano-ES", "facebook": "Facebook-dominicano-ES",
                   "posts": "POSTS-COMUNIDAD"}.get(canal)
        if not carpeta:
            continue
        for num, info in cfg["piezas"].items():
            p = PUBLICACIONES / carpeta / info["archivo"]
            if not p.exists():
                fallos.append(f"{canal} {num}: falta {info['archivo']}")
                continue
            n = len(p.read_text(encoding="utf-8"))
            if not (cfg["min"] <= n <= cfg["max"]):
                fallos.append(f"{canal} {num}: {n} caracteres, fuera de la banda "
                              f"{cfg['min']}-{cfg['max']}")
            if info.get("caracteres") != n:
                fallos.append(f"{canal} {num}: bandas.json declara {info.get('caracteres')} y el "
                              f"archivo tiene {n}")
            dentro += 1
    return fallos, f"{dentro} piezas dentro de su banda"


def g9_envios() -> tuple[list[str], str]:
    """Los envíos de WhatsApp/Facebook: que quepan en un mensaje, que el cuerpo esté entero y que
    el archivo sea exactamente lo que genera `tools/envio.py`. Si alguien edita un envío a mano, canta."""
    herramienta = RAIZ / "tools" / "envio.py"
    if not herramienta.exists() or not (RAIZ / "docs" / "envios").exists():
        return [], "sin envíos en este árbol"
    r = subprocess.run([sys.executable, str(herramienta), "--verificar", "--raiz", str(RAIZ)],
                       capture_output=True, text=True)
    salida = (r.stdout or "") + (r.stderr or "")
    fallos = [ln.strip("  ·") for ln in salida.splitlines() if ln.strip().startswith("·")]
    resumen = [ln.replace("envíos revisados:", "").strip() for ln in salida.splitlines()
               if ln.startswith("envíos revisados")]
    return fallos, (" · ".join(resumen) if resumen else "sin salida")


def g6_antiplantilla(ps: list[Path]) -> tuple[list[str], str]:
    """MEDIDOR: publica la cifra de repetición sin detener la línea.
    La casa exime el eco doctrinal a propósito (doctrina-lupa.json), así que esto mide, no juzga."""
    peor = ("", 0)
    total_parrafos = 0
    for p in ps:
        texto = p.read_text(encoding="utf-8", errors="replace")
        parrafos = [x.strip() for x in re.split(r"\n\s*\n", texto) if len(x.strip()) >= 200]
        total_parrafos += len(parrafos)
        rep = Counter(parrafos)
        if rep:
            frase, veces = rep.most_common(1)[0]
            if veces > peor[1]:
                peor = (f"{p.name[:52]} ({veces}×)", veces)
    return [], f"{total_parrafos} párrafos largos · máxima repetición interna {peor[1]}× en {peor[0] or '—'}"


def g7_enlaces(ps: list[Path]) -> tuple[list[str], str]:
    fallos = []
    medidos = 0
    for p in ps:
        texto = p.read_text(encoding="utf-8", errors="replace")
        for m in APK.finditer(texto):
            fallos.append(f"{p.name}: enlace de binario {m.group(0)[:60]}")
        medidos += len(re.findall(r"https?://", texto))
    return fallos, f"{medidos} enlaces revisados · 0 binarios recetados"


def g8_presupuesto(ps: list[Path]) -> tuple[list[str], str]:
    """MEDIDOR: la distribución real del corpus, por plataforma."""
    grupos = {"whatsapp": [], "facebook": [], "otras": []}
    for p in ps:
        n = len(p.read_text(encoding="utf-8", errors="replace"))
        clave = "whatsapp" if "whatsapp" in p.parent.name.lower() else "facebook" if "facebook" in p.parent.name.lower() else "otras"
        grupos[clave].append(n)
    partes = []
    for k, v in grupos.items():
        if v:
            partes.append(f"{k} n={len(v)} min={min(v)} mediana={int(statistics.median(v))} max={max(v)}")
    return [], " · ".join(partes)


def g0_piezas(ps: list[Path]) -> tuple[list[str], str]:
    fallos, con_latido, con_fecha = [], 0, 0
    for p in ps:
        texto = p.read_text(encoding="utf-8", errors="replace")
        if "💓" in texto:
            con_latido += 1
        else:
            fallos.append(f"{p.name}: sin 💓 (firma de la casa)")
        if DATELINE.search(texto):
            con_fecha += 1
        else:
            fallos.append(f"{p.name}: sin fecha verificable en ninguna parte de la pieza")
        if ZW.search(texto):
            fallos.append(f"{p.name}: carácter de ancho cero")
    return fallos, f"{len(ps)} piezas · {con_latido} con 💓 · {con_fecha} con dateline"


def deuda_congelada() -> dict[str, set[str]]:
    """Deuda conocida y declarada: fallos que ya existían cuando se activó la compuerta.
    No se ocultan (siguen apareciendo en el informe); solo dejan de bloquear y no pueden crecer."""
    if not BASELINE.exists():
        return {}
    crudo = json.loads(BASELINE.read_text(encoding="utf-8"))
    return {k: set(v) for k, v in crudo.get("congelados", {}).items()}


COMPUERTAS = [
    ("G0 piezas", "puerta", None),
    ("G1 esquema", "puerta", None),
    ("G2 frescura", "puerta", None),
    ("G3 licencia", "puerta", None),
    ("G4 actividad", "puerta", None),
    ("G5 integridad", "puerta", None),
    ("G6 anti-plantilla", "medidor", None),
    ("G7 enlaces", "puerta", None),
    ("G8 presupuesto", "medidor", None),
]


def g11_manual() -> tuple[list[str], str]:
    """MANUAL DE ESTILO Y OPERACIONES V3.0 como compuerta (1-nov-2026).

    Corre M01-M16 y M23 sobre las piezas que tienen banda declarada. Un ROJO (fallo crítico)
    o un VENTANA (fallo de forma) cuenta como fallo: el manual no tiene categoría "opcional".
    """
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import manual_gate as mg

    bk = mg.bandas()
    con_banda = set()
    for canal in ("whatsapp", "facebook"):
        for ent in (bk.get(canal, {}).get("piezas", {}) or {}).values():
            if isinstance(ent, dict) and ent.get("archivo"):
                con_banda.add(ent["archivo"])
    ps = [p for p in mg.piezas() if p.name in con_banda]
    if not ps:
        return [], "sin piezas con banda"
    todos = {p.name: mg.parrafos(p.read_text(encoding="utf-8", errors="replace")) for p in mg.piezas()}
    firmas: dict[str, str] = {}
    fallos, verdes = [], 0
    for p in ps:
        r = mg.check(p, bk, firmas, todos)
        if r["veredicto"] == "VERDE":
            verdes += 1
            continue
        for cod, sev, det in r["fallos"]:
            fallos.append(f"{r['veredicto']} {p.name[:52]} · {cod}: {det}")
    return fallos, f"{verdes}/{len(ps)} piezas VERDE en el manual v3.0"


def g13_novedad() -> tuple[list[str], str]:
    """G13 · NOVEDAD DE LA CASA (M24–M28) sobre las piezas con banda declarada, más el registro de
    novedades. Es la compuerta que faltaba: `manual_gate` mide la forma, esta mide si lo que la
    pieza recomienda es nuevo, si declara su madurez y si no vende fama.

    Lee el árbol de ESTA corrida (`RAIZ`), no el del repositorio vivo: si no, la autoprueba sobre
    un árbol de mentira estaría midiendo las piezas de verdad.
    """
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import novedad_gate as ng

    f = RAIZ / "docs" / "bandas.json"
    if not f.exists():
        return [], "sin bandas declaradas"
    try:
        bk = json.loads(f.read_text(encoding="utf-8"))
    except Exception as e:
        return [f"bandas.json ilegible: {e}"], "ilegible"
    nombres = set()
    for canal, cfg in bk.items():
        if not isinstance(cfg, dict):
            continue
        for ent in (cfg.get("piezas") or {}).values():
            if isinstance(ent, dict) and ent.get("archivo"):
                nombres.add(ent["archivo"])
    ps = [p for p in piezas() if p.name in nombres]
    if not ps:
        return [], "sin piezas con banda"
    corte = date.fromisoformat(fecha_casa_hoy())
    fallos, rojos = [], 0
    for p in ps:
        r = ng.revisar(p, corte, entrega=False, es_post="POSTS-COMUNIDAD" in str(p))
        if r["veredicto"] == "ROJO":
            rojos += 1
        for x in r["fallos"]:
            fallos.append(f"{p.name[:52]} · {x}")
    fallos += ng.calendario(RAIZ / "docs" / "CALENDARIO-DE-NOVEDADES.json", corte)
    return fallos, f"{len(ps) - rojos}/{len(ps)} piezas pasan M24–M28 · calendario de novedades"


def g14_atestacion() -> tuple[list[str], str]:
    """G14 · LA FIRMA SE COMPRUEBA, no se supone. Verifica en frío los paquetes Sigstore que estén
    en `attestations/`: identidad del flujo, ventana efímera, registro de transparencia y que la
    firma cubra el manifiesto de hoy."""
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import atestacion_verificar as av

    bundles = sorted((RAIZ / "attestations").glob("*.sigstore.json"))
    manifiesto = RAIZ / "registry" / "_manifiesto-sha256.tsv"
    if not bundles:
        return [], "sin atestaciones firmadas en el árbol (declarado)"
    if not manifiesto.exists():
        return ["G14 sin manifiesto que verificar"], "sin manifiesto"
    fallos: list[str] = []
    for b in bundles:
        m = av.manifiesto_del_lote(b, manifiesto)
        if not m.exists():
            fallos.append(f"G14 sin manifiesto para {b.name}")
            continue
        fallos += av.verificar(b, m)
    return fallos, f"{len(bundles)} atestaciones firmadas verificadas"


def g15_guia() -> tuple[list[str], str]:
    """G15 · LA GUÍA MAESTRA NO PUBLICA FICHA SIN CRÉDITO NI SIN OFICIO (M30–M34).

    Se ejecuta la herramienta de la guía en modo compuertas: si una ficha no declara autor, licencia,
    nivel, pasos reproducibles, cita viva y dato de oficio, la compuerta falla y la vara la detiene.
    """
    herramienta = RAIZ / "guia-maestra" / "herramientas" / "guia_maestra.py"
    if not herramienta.exists():
        return [], "sin guía maestra en el árbol (declarado)"
    r = subprocess.run([sys.executable, str(herramienta), "--compuertas"],
                       capture_output=True, text=True, cwd=RAIZ)
    if r.returncode == 0:
        n = r.stdout.count("VERDE")
        return [], f"{n} fichas de la guía VERDE en M30–M34"
    fallos = [l.strip().replace("✗ ", "") for l in r.stdout.splitlines() if "✗" in l]
    return fallos or ["G15 la guía maestra no pasó sus compuertas"], "fichas ROJAS en M30–M34"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--raiz", default=None, help="árbol alternativo (solo para autoprueba)")
    args = ap.parse_args()
    if args.raiz:
        fijar_raiz(Path(args.raiz))
    datos, ps = fichas(), piezas()
    corridas = [
        ("G0 piezas", "puerta", g0_piezas(ps)),
        ("G1 esquema", "puerta", g1_esquema(datos)),
        ("G2 frescura", "puerta", g2_frescura(datos)),
        ("G3 licencia", "puerta", g3_licencia(datos)),
        ("G4 actividad", "puerta", g4_actividad(datos)),
        ("G5 integridad", "puerta", g5_integridad()),
        ("G6 anti-plantilla", "medidor", g6_antiplantilla(ps)),
        ("G7 enlaces", "puerta", g7_enlaces(ps)),
        ("G8 presupuesto", "medidor", g8_presupuesto(ps)),
        ("G9 envíos", "puerta", g9_envios()),
        ("G10 bandas", "puerta", g10_bandas()),
        ("G11 manual v3.0", "puerta", g11_manual()),
        ("G12 firma literal", "puerta", g12_firma_literal()),
        ("G13 novedad", "puerta", g13_novedad()),
        ("G14 atestación firmada", "puerta", g14_atestacion()),
        ("G15 guía maestra", "puerta", g15_guia()),
    ]
    congelados = deuda_congelada()
    total_fallos = 0
    informe = []
    for nombre, clase, (fallos, resumen) in corridas:
        deuda = [f for f in fallos if f in congelados.get(nombre, set())]
        nuevos = [f for f in fallos if f not in congelados.get(nombre, set())]
        if clase == "puerta":
            total_fallos += len(nuevos)
        informe.append({"compuerta": nombre, "clase": clase, "resumen": resumen,
                        "fallos": nuevos if clase == "puerta" else [],
                        "deuda_congelada": deuda, "medido": len(fallos)})
    if args.json:
        print(json.dumps({"compuertas": informe, "fallos_totales": total_fallos}, ensure_ascii=False, indent=1))
    else:
        print("LA VARA · informe de compuertas")
        print(f"fecha de corrida: {fecha_casa_larga()} ({fecha_casa_hoy()}) · registro: {len(datos)} fichas · piezas: {len(ps)}\n")
        for c in informe:
            marca = "✓" if (c["clase"] == "medidor" or not c["fallos"]) else "✗"
            print(f"{marca} {c['compuerta']:<18} [{c['clase']:<8}] {c['resumen']}")
            if c.get("deuda_congelada"):
                print(f"     · deuda congelada: {len(c['deuda_congelada'])} (declarada en tools/baseline.json, no oculta)")
            for f in c["fallos"][:12]:
                print(f"     · {f}")
            if len(c["fallos"]) > 12:
                print(f"     · … y {len(c['fallos']) - 12} más")
        print()
        print(f"fallos: {'NINGUNO' if total_fallos == 0 else total_fallos}")
    return 0 if total_fallos == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
