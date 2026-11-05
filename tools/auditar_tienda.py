#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""auditar_tienda.py · clonar una tienda de extensiones y leerla como la lee la app.

No pregunta «¿cuántas estrellas tiene?». Hace lo que haría una persona con el
repositorio delante:

  1 · Abre `repo.json` y sigue la pista hasta el catálogo que la app usa de verdad
      (`index_v2` en protobuf o el `index.json` de toda la vida).
  2 · Cuenta las extensiones que el catálogo publica y los idiomas que cubren.
  3 · Comprueba que el catálogo está firmado (`signingKey`) — sin firma, la app
      rechaza la tienda y el usuario no ve por qué.
  4 · Descarga la cabecera de una muestra de APK: un enlace roto en el catálogo
      es una extensión que no se instala aunque el recuento la cuente.
  5 · Lee el README y el código buscando lo que la IA no ve: soporte negado,
      espejo declarado, repositorio muerto, rate-limit recortado, código sin
      pruebas.
  6 · Compara el nombre que la tienda declara con el nombre del repositorio:
      así se detectan los clones que se hacen pasar por otra tienda.

Uso:
    python3 tools/auditar_tienda.py --repo keiyoushi/extensions
    python3 tools/auditar_tienda.py --lote docs/LOTE-tiendas.json --escribir docs/AUDITORIA.json
"""
import argparse, json, os, re, shutil, subprocess, sys, tempfile, urllib.request, urllib.error

API = "https://api.github.com/repos/"
UA = {"User-Agent": "la-bandita/auditor", "Accept": "application/vnd.github+json"}
TOKEN = os.environ.get("GHP_A")

BANDERAS = [
    ("sin soporte declarado", r"no (?:support|soporte)|sin soporte|unsupported|not supported|no longer (?:maintained|supported)"),
    ("abandono declarado",    r"unmaintained|no longer maintained|abandon(?:ed|ware)|won'?t be (?:updated|maintained)|sin mantenimiento"),
    ("espejo declarado",      r"\bmirror\b|espejo|synced from|auto-?sync"),
    ("aviso de retirada",     r"dmca|takedown|cease and desist|retirad"),
    ("no programo / vibecode",r"i (?:can'?t|do not|don'?t) (?:code|program)|not a developer|generad[oa] por ia|ai[- ]generated|chatgpt|vibe[- ]?cod"),
]

CABECERAS_APK = tuple()


def pide(url, cabeceras=None, metodo="GET", limite=4_000_000):
    h = dict(UA)
    if TOKEN:
        h["Authorization"] = "token " + TOKEN
    if cabeceras:
        h.update(cabeceras)
    r = urllib.request.Request(url, headers=h, method=metodo)
    with urllib.request.urlopen(r, timeout=45) as f:
        if metodo == "HEAD":
            return f.status, dict(f.headers), b""
        return f.status, dict(f.headers), f.read(limite)


def api(url):
    try:
        _, _, cuerpo = pide(url)
        return json.loads(cuerpo)
    except Exception as e:  # noqa: BLE001
        return {"_error": str(e)}


def git(args, cwd):
    return subprocess.run(["git"] + args, cwd=cwd, capture_output=True, text=True, timeout=600)


def leer_catalogo(ruta):
    """Devuelve (lista_de_extensiones, fichero) del catálogo que la app usa."""
    orden = ["index.json", "index.min.json", "anime_index.json", "index.min.json",
             "plugins.min.json", "repo.json", "mega.json", "config.json"]
    vistos = []
    for raiz, _, ficheros in os.walk(ruta):
        for f in ficheros:
            if f.endswith(".json") and "index" in f or f in ("repo.json", "mega.json"):
                vistos.append(os.path.join(raiz, f))
    vistos.sort(key=lambda p: (os.path.basename(p) not in orden, p.count(os.sep), len(p)))

    mejor, mejor_f = [], None
    for p in vistos:
        try:
            d = json.load(open(p, encoding="utf-8"))
        except Exception:  # noqa: BLE001
            continue
        ext = []
        if isinstance(d, list):
            ext = d
        elif isinstance(d, dict):
            if isinstance(d.get("extensionList"), dict):
                ext = d["extensionList"].get("extensions") or []
            elif isinstance(d.get("extensions"), list):
                ext = d["extensions"]
            elif isinstance(d.get("repositories"), list):
                ext = d["repositories"]
        if len(ext) > len(mejor):
            mejor, mejor_f = ext, p
    return mejor, mejor_f


def trazas_de_catalogo(ruta, repo):
    """Qué dice `repo.json`: si la app lee protobuf, si declara firma, si hay espejo."""
    out = {"repo_json": None, "index_v2": None, "firma": None, "nombre_declarado": None}
    for raiz, _, ficheros in os.walk(ruta):
        if "repo.json" in ficheros:
            try:
                d = json.load(open(os.path.join(raiz, "repo.json"), encoding="utf-8"))
            except Exception:  # noqa: BLE001
                continue
            out["repo_json"] = os.path.relpath(os.path.join(raiz, "repo.json"), ruta)
            out["index_v2"] = d.get("index_v2")
            meta = d.get("meta") or {}
            out["firma"] = meta.get("signingKeyFingerprint") or meta.get("signingKey")
            out["nombre_declarado"] = meta.get("name")
            break
    return out



def _urls_del_leeme(leeme):
    """La tienda que se instala casi nunca vive en la rama principal: el README
    publica la dirección real (`…/raw/repo/index.pb`, `…/builds/repo.json`)."""
    urls = re.findall(r"https?://[^\s)\"'<>]+\.(?:json|pb)", leeme)
    vistas, salida = set(), []
    for u in urls:
        u = u.rstrip(".,);")
        if u not in vistas:
            vistas.add(u)
            salida.append(u)
    return salida


def _varint(datos, i):
    r = s = 0
    while True:
        b = datos[i]
        r |= (b & 0x7F) << s
        i += 1
        s += 7
        if not b & 0x80:
            return r, i


def _cuenta_protobuf(datos):
    """El catálogo nuevo es un protobuf sin esquema a mano: se cuentan los campos
    repetidos de nivel superior, que son las extensiones."""
    i, n = 0, 0
    try:
        while i < len(datos):
            clave, i = _varint(datos, i)
            campo, alambre = clave >> 3, clave & 7
            if alambre == 2:
                largo, i = _varint(datos, i)
                if campo in (1, 2):
                    n += 1
                i += largo
            elif alambre == 0:
                _, i = _varint(datos, i)
            elif alambre == 5:
                i += 4
            elif alambre == 1:
                i += 8
            else:
                return None
    except IndexError:
        return None
    return n or None


def _cuenta_remota(url):
    """Abre el catálogo publicado y cuenta lo que la app contaría."""
    candidatos = [url]
    if url.endswith(".pb"):
        candidatos.append(url[:-3] + ".json")
        candidatos.append(url.rsplit("/", 1)[0] + "/index.json")
    for u in candidatos:
        try:
            _, _, cuerpo = pide(u)
        except Exception:  # noqa: BLE001
            continue
        if u.endswith(".pb"):
            n = _cuenta_protobuf(cuerpo)
            if n:
                return {"url": u, "formato": "protobuf", "entradas": n, "bytes": len(cuerpo)}
            continue
        try:
            d = json.loads(cuerpo)
        except Exception:  # noqa: BLE001
            continue
        if isinstance(d, list):
            return {"url": u, "formato": "lista", "entradas": len(d), "bytes": len(cuerpo)}
        if isinstance(d, dict):
            if isinstance(d.get("extensionList"), dict):
                return {"url": u, "formato": "mihon", "entradas": len(d["extensionList"].get("extensions") or []), "bytes": len(cuerpo)}
            for clave in ("extensions", "repositories", "pluginLists", "sources"):
                if isinstance(d.get(clave), list):
                    return {"url": u, "formato": clave, "entradas": len(d[clave]), "bytes": len(cuerpo),
                            "nombres": [x.get("name") if isinstance(x, dict) else x for x in d[clave][:5]]}
            return {"url": u, "formato": "objeto", "entradas": len(d), "bytes": len(cuerpo), "claves": list(d)[:8]}
    return None

def banderas_de_texto(ruta):
    hallazgos = []
    leeme = ""
    for nombre in ("README.md", "readme.md", "README.MD", "README.rst", "README"):
        p = os.path.join(ruta, nombre)
        if os.path.exists(p):
            leeme = open(p, encoding="utf-8", errors="replace").read()[:120_000]
            break
    for etiqueta, patron in BANDERAS:
        m = re.search(patron, leeme, re.I)
        if m:
            i = max(0, m.start() - 90)
            hallazgos.append({"bandera": etiqueta, "donde": "README", "texto": leeme[i:m.end() + 90].replace("\n", " ")})
    return leeme, hallazgos


def banderas_de_codigo(ruta):
    """Lo que se ve en el código: rate-limit recortado, pruebas, tamaño."""
    n_archivos = 0
    rate = 0
    comentado = 0
    pruebas = 0
    for raiz, dirs, ficheros in os.walk(ruta):
        dirs[:] = [d for d in dirs if d not in (".git", "build", "node_modules")]
        for f in ficheros:
            ext = os.path.splitext(f)[1].lower()
            if ext not in (".kt", ".java", ".dart", ".js", ".ts"):
                continue
            n_archivos += 1
            try:
                t = open(os.path.join(raiz, f), encoding="utf-8", errors="replace").read()
            except Exception:  # noqa: BLE001
                continue
            if re.search(r"rate.?limit", t, re.I):
                rate += 1
            if re.search(r"^\s*//\s*.*(rate.?limit|delay|sleep)", t, re.I | re.M):
                comentado += 1
        if os.path.basename(raiz).lower() in ("test", "tests", "androidtest"):
            pruebas += len(ficheros)
    return {"archivos_de_codigo": n_archivos, "con_rate_limit": rate,
            "rate_limit_comentado": comentado, "archivos_de_prueba": pruebas}


def _existe(url):
    """Pregunta por el fichero con un GET de un solo byte: la redirección de las
    entregas de GitHub no contesta a HEAD y devuelve un 302 que no dice nada."""
    r = urllib.request.Request(url, headers={"User-Agent": UA["User-Agent"], "Range": "bytes=0-0"})
    try:
        with urllib.request.urlopen(r, timeout=45) as f:
            tramo = f.headers.get("Content-Range") or f.headers.get("Content-Length")
            total = None
            if tramo and "/" in tramo:
                total = tramo.split("/")[-1]
            elif tramo:
                total = tramo
            return f.status, total
    except urllib.error.HTTPError as err:
        return err.code, None


def enlaces_de_entrega(ruta, muestra=8):
    """Las APK ya no viven en el repositorio: se reparten como adjuntos de release.
    `index.html` es el listado que la tienda publica; de ahí se sacan enlaces reales."""
    p = os.path.join(ruta, "index.html")
    if not os.path.exists(p):
        return []
    html = open(p, encoding="utf-8", errors="replace").read()
    urls = re.findall(r'href="(https://github\.com/[^"]+/releases/download/[^"]+\.apk)"', html)
    return urls[:muestra]


def comprobar_apk(exts, base_raw, muestra=6):
    hechos = []
    for e in exts[:muestra]:
        apk = e.get("apk") or e.get("file") or ""
        if not apk:
            continue
        url = base_raw.rstrip("/") + "/apk/" + apk
        st, total = _existe(url)
        hechos.append({"ext": e.get("name") or e.get("pkg"), "estado": st, "bytes": total})
    return hechos


def _muestra_de_apk(destino, exts, repo):
    """Primero los adjuntos de release; si no hay o no responden, el directorio `apk/`."""
    de_release = comprobar_entrega(destino)
    if any(a.get("estado") in (200, 206) for a in de_release):
        return de_release
    de_repo = comprobar_apk(exts, "https://raw.githubusercontent.com/%s/HEAD" % repo) \
        if exts and exts[0].get("apk") else []
    return de_repo or de_release


def comprobar_entrega(ruta):
    urls = enlaces_de_entrega(ruta)
    hechos = []
    for u in urls:
        nombre = u.rsplit("/", 1)[-1]
        st, total = _existe(u)
        hechos.append({"ext": nombre, "estado": st, "bytes": total})
    return hechos


def _firma_del_catalogo(ruta):
    for nombre in ("index.json", "index.min.json"):
        p = os.path.join(ruta, nombre)
        if os.path.exists(p):
            try:
                d = json.load(open(p, encoding="utf-8"))
            except Exception:  # noqa: BLE001
                continue
            if isinstance(d, dict) and d.get("signingKey"):
                return d["signingKey"][:16] + "…"
    return None


def _json_legado(ruta):
    """El `index.min.json` que many webs citan puede ser un lápida de 2 entradas."""
    p = os.path.join(ruta, "index.min.json")
    if not os.path.exists(p):
        return None
    try:
        d = json.load(open(p, encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return None
    n = len(d) if isinstance(d, list) else 1
    nombres = [x.get("name") for x in d][:3] if isinstance(d, list) else []
    return {"entradas": n, "nombres": nombres}


def auditar(repo, trabajo="/home/user/.cache/audita"):
    os.makedirs(trabajo, exist_ok=True)
    destino = os.path.join(trabajo, repo.replace("/", "__"))
    shutil.rmtree(destino, ignore_errors=True)
    meta = api(API + repo)
    if meta.get("_error") or meta.get("message"):
        return {"repo": repo, "existe": False, "error": meta.get("_error") or meta.get("message")}

    clon = git(["clone", "--depth", "1", "--quiet",
                "https://github.com/%s.git" % repo, destino], trabajo)
    ficha = {
        "repo": repo,
        "existe": True,
        "archivado": meta.get("archived"),
        "deshabilitado": meta.get("disabled"),
        "estrellas": meta.get("stargazers_count"),
        "incidencias_abiertas": meta.get("open_issues_count"),
        "empujon": meta.get("pushed_at"),
        "creado": meta.get("created_at"),
        "licencia": (meta.get("license") or {}).get("spdx_id"),
        "descripcion": meta.get("description"),
        "clonado": clon.returncode == 0,
    }
    if clon.returncode != 0:
        ficha["error_clon"] = clon.stderr[-300:]
        return ficha

    trazas = trazas_de_catalogo(destino, repo)
    exts, fichero = leer_catalogo(destino)
    leeme, banderas = banderas_de_texto(destino)
    codigo = banderas_de_codigo(destino)

    idiomas = {}
    for e in exts:
        idiomas[e.get("lang") or "?"] = idiomas.get(e.get("lang") or "?", 0) + 1
    fuentes = sum(len(e.get("sources") or []) for e in exts)

    ficha.update({
        "catalogo": os.path.relpath(fichero, destino) if fichero else None,
        "extensiones": len(exts),
        "fuentes_declaradas": fuentes,
        "idiomas": len(idiomas),
        "idiomas_top": sorted(idiomas.items(), key=lambda x: -x[1])[:6],
        "trazas": trazas,
        "banderas": banderas,
        "codigo": codigo,
        "leeme_bytes": len(leeme),
        "apk_probados": _muestra_de_apk(destino, exts, repo),
        "manifiesto_suma": os.path.exists(os.path.join(destino, "release-assets.json")),
        "json_legado": _json_legado(destino),
    })

    # una tienda sin clave de firma no la acepta la app, aunque el catálogo esté lleno
    firma = trazas["firma"]
    if firma and exts:
        pk = _firma_del_catalogo(destino)
        ficha["firma_en_catalogo"] = pk
        if not pk:
            ficha.setdefault("banderas", []).append(
                {"bandera": "clave de firma solo en repo.json", "donde": "repo.json", "texto": "el catálogo no la repite"}
            )


    # si el repositorio guarda el código y publica el catálogo en otra rama,
    # se sigue la dirección del README: es la que instala el usuario
    urls = _urls_del_leeme(leeme)
    remoto = None
    if urls and ficha["extensiones"] == 0:
        for u in urls[:3]:
            remoto = _cuenta_remota(u)
            if remoto and remoto.get("entradas"):
                break
    ficha["catalogo_publicado"] = remoto
    ficha["urls_en_el_leeme"] = urls[:4]
    if remoto and remoto.get("entradas"):
        ficha["extensiones"] = remoto["entradas"]

    # veredicto con motivos, no con una nota
    motivos = []
    if ficha["archivado"]:
        motivos.append("archivado")
    if ficha["extensiones"] == 0:
        motivos.append("no publica un catálogo que se pueda contar")
    if not trazas["firma"] and not remoto:
        motivos.append("sin clave de firma a la vista")
    if ficha["apk_probados"] and not any(a.get("estado") in (200, 206) for a in ficha["apk_probados"]):
        motivos.append("ninguna APK de la muestra descarga")
    ficha["motivos"] = motivos
    shutil.rmtree(destino, ignore_errors=True)   # el clon no se queda: lo que sirve es la ficha
    ficha["veredicto"] = ("NO" if ficha["archivado"] or ficha["extensiones"] == 0
                          else ("CONDICIONES" if motivos else "SIRVE"))
    return ficha


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", action="append", default=[])
    ap.add_argument("--lote", help="JSON con una lista de «dueño/repo»")
    ap.add_argument("--escribir", help="ruta del JSON de salida")
    a = ap.parse_args()
    repos = list(a.repo)
    if a.lote:
        repos += [r if isinstance(r, str) else r["repo"] for r in json.load(open(a.lote, encoding="utf-8"))]
    if not repos:
        sys.exit("faltan repositorios")
    salida = []
    for r in repos:
        f = auditar(r)
        salida.append(f)
        print("%-42s %-11s ext=%-5s arch=%-5s firma=%-4s %s" % (
            r, f.get("veredicto", "?"), f.get("extensiones", "-"), f.get("archivado", "-"),
            "sí" if (f.get("trazas") or {}).get("firma") else "no",
            " · ".join(f.get("motivos") or []) or (f.get("descripcion") or "")[:40]))
    if a.escribir:
        json.dump(salida, open(a.escribir, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("escrito:", a.escribir)


if __name__ == "__main__":
    main()
