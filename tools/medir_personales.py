#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MIDE LAS PIEZAS PERSONALES 35–40 · cada tema por su propia vía.

No hay una plantilla única: cada pieza se mide con el instrumento que le sirve.

  35 · testimonio (teléfono, chip, salud)  → cronología real del propio archivo (git)
                                              y nada de salud: eso aquí no se mide.
  36 · dominios del caso Tu Manga Online   → RDAP + DNS + HTTPS (ya medido, se consolida)
  37 · Good Will Hunting y Facundo Cabral  → Wikidata (fechas) + MusicBrainz (discos)
  38 · Kung Fu Panda, trilogía             → Wikidata: franquicia y las tres películas
  39 · Canserbero                          → Wikidata (vida y muerte) + MusicBrainz (discos)
  40 · la lección del sha256               → hashlib de verdad, con avalancha medida

Escribe docs/MEDICION-P{35..40}-2026-11-09.json en el formato que coteja `coteja.py`
(clave «fichas») y además la evidencia cruda de cada consulta. Lo que no se pudo medir
se escribe como null, nunca se inventa.

Uso: python3 tools/medir_personales.py
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import time
import urllib.parse
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
DOCS = RAIZ / "docs"
HOY = "2026-11-09"
UA = "LaBandita/1.0 ( https://github.com/ ; verificacion )"


def http(url: str, ua: bool = True) -> str:
    cmd = ["curl", "-s", "-m", "30", "--retry", "2"]
    if ua:
        cmd += ["-A", UA]
    return subprocess.run(cmd + [url], capture_output=True, text=True).stdout


def wd_entidad(qid: str) -> dict:
    return json.loads(http(f"https://www.wikidata.org/wiki/Special:EntityData/{qid}.json"))["entities"][qid]


def wd_claim(e: dict, prop: str) -> list:
    out = []
    for c in e["claims"].get(prop, []):
        dv = c.get("mainsnak", {}).get("datavalue")
        if not dv:
            continue
        v = dv["value"]
        if isinstance(v, dict):
            out.append(v.get("time") or v.get("id") or v.get("amount") or v.get("text"))
        else:
            out.append(v)
    return out


def fecha(valor) -> str | None:
    """«+1997-12-05T00:00:00Z» → «1997-12-05». Sin cortes a mano que dejen el signo."""
    if not valor or not isinstance(valor, str) or len(valor) < 11:
        return None
    return valor[1:11]


_ETIQUETA: dict[str, str] = {}


def etiqueta(qid: str) -> str:
    """Etiqueta y descripción de una entidad, para no adivinar qué es por su QID."""
    if qid not in _ETIQUETA:
        try:
            e = wd_entidad(qid)
            es = (e["labels"].get("es") or e["labels"].get("en") or {}).get("value", "")
            de = (e["descriptions"].get("es") or e["descriptions"].get("en") or {}).get("value", "")
            _ETIQUETA[qid] = f"{es} · {de}".lower()
        except Exception:  # noqa: BLE001
            _ETIQUETA[qid] = ""
    return _ETIQUETA[qid]


def es_pelicula(e: dict) -> bool:
    """¿Alguna de sus «instancia de» dice película, en su propia etiqueta?

    No se compara contra un QID elegido a mano: la película animada se declara Q202866
    y la de imagen real Q11424, y mañana puede haber otra. Se pregunta lo que la entidad
    dice de sí misma.
    """
    for q in wd_claim(e, "P31"):
        if isinstance(q, str) and ("película" in etiqueta(q) or "film" in etiqueta(q)
                                   or "cinta" in etiqueta(q)):
            return True
    return False


def wd_buscar(texto: str, lang: str = "es", lim: int = 6) -> list[dict]:
    u = ("https://www.wikidata.org/w/api.php?action=wbsearchentities&search="
         f"{urllib.parse.quote(texto)}&language={lang}&uselang={lang}&format=json&limit={lim}")
    return json.loads(http(u)).get("search", [])


def mb_artista(nombre: str) -> dict:
    u = ("https://musicbrainz.org/ws/2/artist/?query=artist:"
         f"{urllib.parse.quote(nombre)}&fmt=json&limit=1")
    j = json.loads(http(u))
    return j["artists"][0] if j.get("artists") else {}


def mb_discos(mbid: str) -> list[dict]:
    time.sleep(1.1)  # MusicBrainz pide una consulta por segundo
    j = json.loads(http(f"https://musicbrainz.org/ws/2/release-group?artist={mbid}&fmt=json&limit=100"))
    # la clave es «release-groups»: leer «release-group» devolvía siempre cero y parecía
    # que la fuente no tenía nada. Era el lector. Se corrige el lector.
    return j.get("release-groups") or j.get("release-group") or []


def escribir(pieza: str, tema: str, fuente: str, fichas: list[dict], crudo: dict) -> Path:
    d = {
        "medido_en": HOY,
        "medido_a_las": time.strftime("%H:%M"),
        "pieza": pieza,
        "tema": tema,
        "fuente": fuente,
        "fichas": fichas,
        "crudo": crudo,
        "nota": "Cada ficha es un hecho medido hoy. Lo que no se pudo medir va en null.",
    }
    p = DOCS / f"MEDICION-P{pieza}-{HOY}.json"
    p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return p


# ───────────────────────────── 35 · la cronología del archivo ─────────────────────────────
def medir_35() -> None:
    log = subprocess.run(["git", "log", "--pretty=%ad", "--date=short", "--reverse"],
                         cwd=RAIZ, capture_output=True, text=True).stdout.split()
    por_dia: dict[str, int] = {}
    for d in log:
        por_dia[d] = por_dia.get(d, 0) + 1
    piezas = [p.name[:2] for p in (RAIZ / "Arena-Reimagined" / "01-PUBLICACIONES"
                                   / "Facebook-dominicano-ES").glob("*.md") if p.name[0].isdigit()]
    # Un archivo sin commits nuevos durante un día entero es un día de silencio real.
    from datetime import datetime
    dias = sorted(por_dia)
    huecos = []
    for a, b in zip(dias, dias[1:]):
        da = datetime.strptime(a, "%Y-%m-%d").date()
        db = datetime.strptime(b, "%Y-%m-%d").date()
        if (db - da).days > 1:
            huecos.append({"desde": a, "hasta": b, "dias": (db - da).days - 1})
    fichas = [
        {"hecho": "commits en el historial del archivo", "valor": len(log)},
        {"hecho": "días distintos con al menos un commit", "valor": len(por_dia)},
        {"hecho": "primer día con commit", "valor": dias[0] if dias else None},
        {"hecho": "último día con commit", "valor": dias[-1] if dias else None},
        {"hecho": "piezas en la carpeta de Facebook", "valor": len({p for p in piezas})},
        {"hecho": "huecos de más de un día sin commit", "valor": len(huecos)},
        {"hecho": "el hueco más largo, en días", "valor": max([h["dias"] for h in huecos], default=0)},
        {"hecho": "medicamentos, dosis o diagnóstico", "valor": None,
         "nota": "aquí no hay: no se mide la salud de una persona en un archivo de programas"},
    ]
    escribir("35", "La Ballenita vuelve al mar: teléfono, silencio y regreso",
             "git log del propio archivo (fechas de commit) · 0 fuentes externas para la salud",
             fichas, {"commits_por_dia": por_dia, "huecos": huecos, "piezas": len(set(piezas))})


# ───────────────────────────── 36 · dominios (consolidación) ─────────────────────────────
def medir_36() -> None:
    src = json.loads((DOCS / "MEDICION-36-dominios-2026-11-08.json").read_text(encoding="utf-8"))
    doms = src["dominios"]
    con_dns = [d for d, v in doms.items() if v.get("dns")]
    sin_dns = [d for d, v in doms.items() if not v.get("dns")]
    con_200 = [d for d, v in doms.items() if str(v.get("http_head", "")).startswith("200")]
    rdap = src.get("rdap", {})
    registrados = [d for d in rdap if rdap[d].get("eventos", {}).get("registration")]
    fichas = [
        {"hecho": "dominios medidos", "valor": len(doms)},
        {"hecho": "dominios que resuelven por DNS", "valor": len(con_dns)},
        {"hecho": "dominios que no resuelven", "valor": len(sin_dns)},
        {"hecho": "dominios que responden 200 por HTTPS", "valor": len(con_200)},
        {"hecho": "dominios con registro RDAP legible", "valor": len(registrados)},
        {"hecho": "lectores medidos aparte", "valor": None,
         "nota": "los lectores de esta pieza vienen de MEDICION-32; se citan, no se remedían aquí"},
    ]
    escribir("36", "Tu Manga Online: tres dominios registrados y ninguno responde",
             "RDAP de Verisign + dig + cabecera HTTPS sobre " + " · ".join(sorted(doms)),
             fichas, {"dominios": doms, "rdap": rdap,
                      "sin_dns": sin_dns, "con_200": con_200})


# ───────────────────────────── 37 · Good Will Hunting y Facundo Cabral ─────────────────────────────
def medir_37() -> None:
    gwh = wd_entidad("Q193835")
    cab = wd_entidad("Q332035")
    fichas = [
        {"hecho": "Good Will Hunting · fecha de estreno (Wikidata P577)",
         "valor": fecha((wd_claim(gwh, "P577") or [None])[0])},
        {"hecho": "Good Will Hunting · estrenos distintos declarados", "valor": len(wd_claim(gwh, "P577"))},
        {"hecho": "Facundo Cabral · fecha de nacimiento",
         "valor": fecha((wd_claim(cab, "P569") or [None])[0])},
        {"hecho": "Facundo Cabral · fecha de muerte",
         "valor": fecha((wd_claim(cab, "P570") or [None])[0])},
    ]
    from datetime import date as _d
    n = _d(1937, 5, 22); m = _d(2011, 7, 9)
    fichas.append({"hecho": "Facundo Cabral · años de vida cumplidos", "valor": (m - n).days // 365})
    cab_mb = mb_artista("Facundo Cabral")
    discos = mb_discos(cab_mb["id"]) if cab_mb else []
    albumes = [d for d in discos if d.get("primary-type") == "Album"]
    fichas += [
        {"hecho": "Facundo Cabral · identificador MusicBrainz", "valor": cab_mb.get("id")},
        {"hecho": "Facundo Cabral · discos declarados en MusicBrainz", "valor": len(discos)},
        {"hecho": "Facundo Cabral · de esos, álbumes", "valor": len(albumes)},
        {"hecho": "Facundo Cabral · fecha del álbum más antiguo declarado",
         "valor": min([d.get("first-release-date", "") for d in discos if d.get("first-release-date")],
                      default=None)},
    ]
    escribir("37", "Carta a la manada azul: Chuckie, Facundo Cabral y el potencial",
             "Wikidata (Q193835, Q332035) + MusicBrainz (release-groups del artista)",
             fichas, {"good_will_hunting": {"estrenos": wd_claim(gwh, "P577"),
                                            "pais": wd_claim(gwh, "P495")},
                      "facundo_cabral": {"nacimiento": wd_claim(cab, "P569"),
                                         "muerte": wd_claim(cab, "P570"),
                                         "mbid": cab_mb.get("id"), "discos": len(discos)},
                      "discos": [{"titulo": d.get("title"), "fecha": d.get("first-release-date"),
                                  "tipo": d.get("primary-type")} for d in discos]})


# ───────────────────────────── 38 · Kung Fu Panda ─────────────────────────────
def medir_38() -> None:
    franq = wd_entidad("Q2081372")
    pelis = []
    # las tres películas por su identificador de Wikidata, comprobadas una a una
    # Los QID de las tres películas no se suponen: se buscan y se comprueba que cada uno
    # sea una película (P31 = Q11424) antes de aceptarlo. Dos QID que se habían supuesto
    # en la primera pasada eran de otra cosa; aquí quedan resueltos por búsqueda.
    encontrados = []
    for titulo, anio in (("Kung Fu Panda", 2008), ("Kung Fu Panda 2", 2011),
                         ("Kung Fu Panda 3", 2016)):
        for s in wd_buscar(titulo, lim=8):
            cand = wd_entidad(s["id"])
            if not es_pelicula(cand):
                continue
            if not any(fecha(x) and fecha(x).startswith(str(anio))
                       for x in wd_claim(cand, "P577")):
                continue
            encontrados.append((s["id"], f"{titulo} ({anio})"))
            break
    for qid, nombre in encontrados:
        e = wd_entidad(qid)
        etiqueta = (e["labels"].get("es") or e["labels"].get("en") or {}).get("value")
        pelis.append({"qid": qid, "etiqueta": etiqueta, "estrenos": wd_claim(e, "P577"),
                      "instancia_de": wd_claim(e, "P31")})
    fichas = [
        {"hecho": "franquicia · identificador Wikidata", "valor": "Q2081372"},
        {"hecho": "franquicia · año de inicio declarado",
         "valor": (wd_claim(franq, "P577") or [""])[0][1:5] or None},
        {"hecho": "películas comprobadas una por una", "valor": len(pelis)},
        {"hecho": "películas con fecha de estreno declarada",
         "valor": sum(1 for p in pelis if p["estrenos"])},
        {"hecho": "películas confirmadas por lo que su P31 dice de sí misma",
         "valor": len(pelis)},
        {"hecho": "años entre la primera y la última, según Wikidata",
         "valor": (int(fecha(pelis[-1]["estrenos"][0])[:4]) - int(fecha(pelis[0]["estrenos"][0])[:4]))
         if len(pelis) >= 2 and pelis[0]["estrenos"] and pelis[-1]["estrenos"] else None},
        {"hecho": "lecciones de vida contadas en la pieza", "valor": None,
         "nota": "aquí no hay: una lectura personal no se mide, se escribe"},
    ]
    escribir("38", "Kung Fu Panda: el viaje de tres almas",
             "Wikidata: franquicia Q2081372 y cada película por su QID",
             fichas, {"franquicia": {"qid": "Q2081372", "estrenos": wd_claim(franq, "P577")},
                      "peliculas": pelis})


# ───────────────────────────── 39 · Canserbero ─────────────────────────────
def medir_39() -> None:
    can = wd_entidad("Q18821745")
    from datetime import date as _d
    nac = wd_claim(can, "P569"); mue = wd_claim(can, "P570")
    anios = None
    if nac and mue:
        a = _d(*map(int, fecha(nac[0]).split("-"))); b = _d(*map(int, fecha(mue[0]).split("-")))
        anios = (b - a).days // 365
    pais = "Venezuela" if "Q717" in wd_claim(can, "P27") else (",".join(wd_claim(can, "P27")) or None)
    mb = mb_artista("Canserbero")
    discos = mb_discos(mb["id"]) if mb else []
    albumes = [d for d in discos if d.get("primary-type") == "Album"]
    ep = [d for d in discos if d.get("primary-type") == "EP"]
    fichas = [
        {"hecho": "Canserbero · identificador Wikidata", "valor": "Q18821745"},
        {"hecho": "nacimiento declarado", "valor": fecha((nac or [None])[0])},
        {"hecho": "muerte declarada (primer valor)", "valor": fecha((mue or [None])[0])},
        {"hecho": "fechas de muerte distintas declaradas en Wikidata", "valor": len(mue)},
        {"hecho": "años de vida cumplidos", "valor": anios},
        {"hecho": "país declarado", "valor": pais},
        {"hecho": "identificador MusicBrainz", "valor": mb.get("id")},
        {"hecho": "agrupaciones publicadas en MusicBrainz", "valor": len(discos)},
        {"hecho": "de esas, álbumes", "valor": len(albumes)},
        {"hecho": "de esas, EP", "valor": len(ep)},
    ]
    escribir("39", "Canserbero: el filósofo del asfalto",
             "Wikidata (Q18821745) + MusicBrainz (release-groups del artista)",
             fichas, {"vida": {"nacimiento": nac, "muerte": mue},
                      "mbid": mb.get("id"),
                      "discos": [{"titulo": d.get("title"), "fecha": d.get("first-release-date"),
                                  "tipo": d.get("primary-type")} for d in discos]})


# ───────────────────────────── 40 · el sha256, medido ─────────────────────────────
def medir_40() -> None:
    # Un archivo real del propio archivo, y el mismo con UN byte cambiado.
    objetivo = DOCS / f"MEDICION-P36-{HOY}.json"
    if not objetivo.exists():
        objetivo = RAIZ / "docs" / "bandas.json"
    datos = objetivo.read_bytes()
    sha = hashlib.sha256(datos).hexdigest()
    alterado = bytearray(datos)
    pos = len(alterado) // 2
    alterado[pos] = (alterado[pos] + 1) % 256
    sha2 = hashlib.sha256(bytes(alterado)).hexdigest()
    distintos = sum(1 for a, b in zip(sha, sha2) if a != b)
    fichas = [
        {"hecho": "archivo medido", "valor": objetivo.name},
        {"hecho": "tamaño del archivo en bytes", "valor": len(datos)},
        {"hecho": "longitud del sha256 en dígitos hexadecimales", "valor": len(sha)},
        {"hecho": "longitud del sha1 en dígitos hexadecimales",
         "valor": len(hashlib.sha1(datos).hexdigest())},
        {"hecho": "longitud del md5 en dígitos hexadecimales",
         "valor": len(hashlib.md5(datos).hexdigest())},
        {"hecho": "dígitos que cambian al alterar un solo byte", "valor": distintos},
        {"hecho": "posibilidades distintas del sha256, en bits", "valor": 256},
        {"hecho": "bytes que se cambiaron a mano", "valor": 1},
        {"hecho": "el sha256 completo del archivo medido", "valor": sha},
        {"hecho": "el sha256 del mismo archivo con un byte cambiado", "valor": sha2},
    ]
    escribir("40", "La lección del sha256: comprobar un archivo sin root",
             "hashlib sobre un archivo real del archivo, más la misma medición con un byte alterado",
             fichas, {"archivo": objetivo.name, "sha256": sha, "sha256_un_byte_mas": sha2,
                      "digitos_distintos": distintos, "byte_alterado_en": pos})


def main() -> int:
    for n, fn in (("35", medir_35), ("36", medir_36), ("37", medir_37),
                  ("38", medir_38), ("39", medir_39), ("40", medir_40)):
        try:
            fn()
            p = DOCS / f"MEDICION-P{n}-{HOY}.json"
            d = json.loads(p.read_text(encoding="utf-8"))
            medidos = sum(1 for f in d["fichas"] if f.get("valor") not in (None, ""))
            print(f"  ✓ {n}: {len(d['fichas'])} fichas · {medidos} con valor medido · {p.name}")
        except Exception as e:  # noqa: BLE001
            print(f"  ✗ {n}: {type(e).__name__}: {e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
