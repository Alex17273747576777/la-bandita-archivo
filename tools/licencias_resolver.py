#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""RESUELVE LAS LICENCIAS QUE NO CONCLUYEN · cierra la deuda de las fichas NOASSERTION.

El orden de la casa es SPDX de la API → endpoint de licencia → texto del archivo → ausencia
firmada. Esta herramienta recorre las fichas que quedaron sin veredicto (spdx nulo o
«NOASSERTION»), pregunta a la API por el endpoint de licencia y, si la API tampoco concluye, lee
el texto del archivo y lo casa con las firmas literales de las licencias conocidas. Lo que no se
puede resolver se queda como ausencia firmada, con la fecha: no se inventa un SPDX.

Uso:
  LBT=<token> python3 tools/licencias_resolver.py            # resuelve y escribe
  LBT=<token> python3 tools/licencias_resolver.py --seco     # solo informa, no escribe
"""
from __future__ import annotations

import base64
import glob
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
API = "https://api.github.com"

# Firmas literales: se buscan en el TEXTO de la licencia, no en el nombre del archivo.
FIRMAS = [
    ("AGPL-3.0-only", "GNU AFFERO GENERAL PUBLIC LICENSE"),
    ("LGPL-3.0-only", "GNU LESSER GENERAL PUBLIC LICENSE"),
    ("GPL-3.0-only", "GNU GENERAL PUBLIC LICENSE"),
    ("GPL-2.0-only", "GNU GENERAL PUBLIC LICENSE"),          # se distingue por «Version 2»
    ("Apache-2.0", "Apache License"),
    ("MPL-2.0", "Mozilla Public License Version 2.0"),
    ("EPL-2.0", "Eclipse Public License"),
    ("CC-BY-SA-4.0", "Attribution-ShareAlike 4.0 International"),
    ("CC-BY-4.0", "Attribution 4.0 International"),
    ("CC0-1.0", "CC0 1.0 Universal"),
    ("Unlicense", "This is free and unencumbered software released into the public domain"),
    ("OFL-1.1", "SIL OPEN FONT LICENSE"),
    ("Artistic-2.0", "The Artistic License 2.0"),
    ("BSD-3-Clause", "Redistribution and use in source and binary forms"),
    ("MIT", "Permission is hereby granted, free of charge"),
    ("ISC", "Permission to use, copy, modify, and/or distribute this software for any purpose"),
    ("Zlib", "This software is provided 'as-is'"),
    ("BSL-1.0", "Boost Software License"),
]


def _get(url: str, tok: str) -> tuple[int, dict]:
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {tok}", "Accept": "application/vnd.github+json",
        "User-Agent": "la-bandita-licencias"})
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            return r.status, json.loads(r.read().decode() or "{}")
    except urllib.error.HTTPError as e:
        return e.code, {}
    except Exception:
        return 0, {}


def por_texto(texto: str) -> str | None:
    for spdx, firma in FIRMAS:
        if firma.lower() in texto.lower():
            if spdx == "GPL-2.0-only" and "Version 2" not in texto and "version 2" not in texto.lower():
                continue
            return spdx
    return None


def resolver(ficha: dict, tok: str) -> tuple[str | None, str, str | None]:
    """Devuelve (spdx, método, archivo) o (None, motivo, None)."""
    repo = ficha["id"].replace("--", "/", 1) if ficha.get("repo") is None else ficha["repo"]
    repo = ficha.get("repo") or repo
    cod, lic = _get(f"{API}/repos/{repo}/license", tok)
    if cod == 200:
        spdx = ((lic.get("license") or {}) or {}).get("spdx_id")
        nombre = lic.get("name")
        if spdx and spdx != "NOASSERTION":
            return spdx, "endpoint-license", nombre
        contenido = ((lic.get("content") or "").strip())
        if contenido:
            try:
                texto = base64.b64decode(contenido).decode("utf-8", "replace")
            except Exception:
                texto = ""
            hallado = por_texto(texto)
            if hallado:
                return hallado, "texto-license", nombre
    # segundo intento: el árbol, por si hay LICENSE en otra ruta
    cod2, arbol = _get(f"{API}/repos/{repo}/contents/", tok)
    if cod2 == 200 and isinstance(arbol, list):
        for x in arbol:
            if re.fullmatch(r"(LICEN[CS]E|COPYING)(\.(md|txt))?", x.get("name", ""), re.I):
                cod3, obj = _get(f"{API}/repos/{repo}/contents/{x['name']}", tok)
                if cod3 == 200 and obj.get("content"):
                    texto = base64.b64decode(obj["content"]).decode("utf-8", "replace")
                    hallado = por_texto(texto)
                    return (hallado, "texto-license", x["name"]) if hallado else (None, "texto sin firma conocida", x["name"])
    return None, "sin licencia concluyente", None


PROPIETARIA = ("all rights reserved", "source-available", "source available", "proprietary",
               "non-commercial", "noncommercial", "no se permite", "viewing only",
               "unauthorized copying", "todos los derechos reservados")


def clasificar_restantes(tok: str, seco: bool = False) -> dict:
    """Segunda pasada: las que el endpoint no concluye y el texto no casa con ninguna licencia
    libre conocida. Se lee el archivo entero y se dicta veredicto con la frase que lo prueba:
    si dice «all rights reserved» o «source-available», no es licencia libre y la ficha lo dice.

    No se inventa un SPDX: se deja `spdx` en NOASSERTION, se cita el archivo y se escribe en
    `nota` el veredicto con su frase. Así la deuda deja de ser «no se sabe» y pasa a ser
    «es propietaria, y aquí está la línea que lo prueba»."""
    hoy = date.today().isoformat()
    resumen = {"propietaria": 0, "libre-sin-firma": 0, "ilegible": 0}
    for f in sorted(glob.glob(str(RAIZ / "registry" / "*.json"))):
        if Path(f).name.startswith("_"):
            continue
        d = json.loads(Path(f).read_text(encoding="utf-8"))
        lic = d.get("licencia") or {}
        if (lic.get("spdx") not in (None, "", "NOASSERTION") or lic.get("nota")
                or lic.get("metodo") == "ausencia-firmada"):
            continue
        repo = (d.get("repo") or d["id"].replace("--", "/", 1))
        arch = lic.get("archivo")
        cod, j = _get(f"{API}/repos/{repo}/contents/{arch}", tok) if arch else _get(f"{API}/repos/{repo}/license", tok)
        if cod != 200 or not isinstance(j, dict) or not j.get("content"):
            if arch:  # el «archivo» citado era una carpeta: se pide el endpoint de licencia
                cod, j = _get(f"{API}/repos/{repo}/license", tok)
        if cod != 200 or not isinstance(j, dict) or not j.get("content"):
            resumen["ilegible"] += 1
            continue
        try:
            texto = base64.b64decode(j["content"]).decode("utf-8", "replace")
        except Exception:
            resumen["ilegible"] += 1
            continue
        bajo = " ".join(texto.lower().split())
        frase = next((x for x in PROPIETARIA if x in bajo), None)
        if frase:
            lic["nota"] = (f"Texto leído el {hoy}: licencia propietaria o de código disponible "
                           f"(«{frase}»). No es licencia libre: no se recomienda para uso del "
                           f"lector, y si se cita es solo como referencia.")[:400]
            resumen["propietaria"] += 1
            if not seco:
                Path(f).write_text(json.dumps(d, ensure_ascii=False, indent=1, sort_keys=True) + "\n",
                                   encoding="utf-8")
        else:
            lic["nota"] = (f"Texto leído el {hoy}: {len(texto)} caracteres sin firma de licencia "
                           f"libre conocida ni cláusula de reserva de derechos. Queda citado el "
                           f"archivo y pendiente de lectura humana.")[:400]
            resumen["libre-sin-firma"] += 1
            if not seco:
                Path(f).write_text(json.dumps(d, ensure_ascii=False, indent=1, sort_keys=True) + "\n",
                                   encoding="utf-8")
    return resumen


def main() -> int:
    seco = "--seco" in sys.argv
    tok = os.environ.get("LBT") or os.environ.get("PAT_FINO") or ""
    if not tok:
        print("falta el token (LBT o PAT_FINO)")
        return 1
    hoy = date.today().isoformat()
    candidatas = []
    for f in sorted(glob.glob(str(RAIZ / "registry" / "*.json"))):
        if Path(f).name.startswith("_"):
            continue
        d = json.loads(Path(f).read_text(encoding="utf-8"))
        lic = d.get("licencia") or {}
        # las ausencias firmadas NO son deuda de licencia: ya tienen veredicto y fecha
        if lic.get("spdx") in (None, "", "NOASSERTION") and lic.get("metodo") != "ausencia-firmada":
            candidatas.append(Path(f))
    print(f"fichas sin licencia concluyente: {len(candidatas)}")
    resueltas: dict[str, int] = {}
    acta = []
    for i, f in enumerate(candidatas, 1):
        d = json.loads(f.read_text(encoding="utf-8"))
        lic = d.setdefault("licencia", {})
        if lic.get("metodo") == "ausencia-firmada":
            continue  # ya está firmada como ausencia: no se toca sin motivo
        spdx, metodo, archivo = resolver(d, tok)
        if spdx:
            lic.update(spdx=spdx, metodo=metodo, archivo=archivo, verificado_en=hoy)
            resueltas[spdx] = resueltas.get(spdx, 0) + 1
            acta.append({"id": d["id"], "spdx": spdx, "metodo": metodo, "archivo": archivo})
            if not seco:
                f.write_text(json.dumps(d, ensure_ascii=False, indent=1, sort_keys=True) + "\n",
                             encoding="utf-8")
        else:
            acta.append({"id": d["id"], "spdx": None, "motivo": metodo})
        if i % 25 == 0:
            print(f"  … {i}/{len(candidatas)} · resueltas {sum(resueltas.values())}")
        time.sleep(0.14)
    print(f"resueltas: {sum(resueltas.values())} de {len(candidatas)}")
    for k, v in sorted(resueltas.items(), key=lambda kv: -kv[1]):
        print(f"   {k:<16} {v}")
    clas = clasificar_restantes(tok, seco)
    print("clasificación de las que quedaban sin veredicto:", clas)
    if not seco:
        salida = RAIZ / "docs" / f"ACTA-LICENCIAS-{hoy}.json"
        salida.write_text(json.dumps({"fecha": hoy, "candidatas": len(candidatas),
                                      "resueltas": sum(resueltas.values()),
                                      "por_licencia": resueltas, "detalle": acta,
                                      "clasificacion_restantes": clas},
                                     ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print("acta:", salida.relative_to(RAIZ))
    return 0


if __name__ == "__main__":
    sys.exit(main())
