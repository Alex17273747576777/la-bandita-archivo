#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""REFERENCIAS · comprueba que ninguna carpeta movida siga citada por su ruta vieja.

Guarda la tabla de carpetas movidas y audita el árbol contra ella, distinguiendo
dos cosas que no son lo mismo:

* una ruta vieja citada por un archivo que hoy se lee o se ejecuta → FALLO (detiene la línea);
* una ruta vieja citada por un acta o un registro histórico → CITA (se conserva y el mapa la traduce).

Qué hace:
  * Lee la tabla de mudanzas (carpetas antes → después).
  * Recorre todos los archivos de texto del árbol buscando citas a rutas viejas.
  * Distingue citas en archivos vivos vs. actas/histórico.
  * Reporta 0 rutas vivas rotas si todo está bien.

Qué NO hace:
  * No corrige rutas por su cuenta: corregir una ruta exige saber qué quería decir la frase.
  * No modifica actas ni registros históricos: esas citas se conservan a propósito.
"""
from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

RAIZ: Path = Path(__file__).resolve().parents[1]
MAPA: Path = RAIZ / "MAPA-DEL-ARCHIVO.md"

# Tabla de mudanzas conocidas (antes → después). Se actualiza con cada reestructura del árbol.
MUDANZAS: dict[str, str] = {
    "uploads/": "ARCHIVO-HISTORICO/subidas-2026-09/",
    "Arena-Reimagined/_versiones/": "Arena-Reimagined/02-ARCHIVO/_etapas-anteriores/_versiones/",
    "Arena-Reimagined/packs/": "Arena-Reimagined/02-ARCHIVO/_etapas-anteriores/packs/",
    "Arena-Reimagined/_herramientas/": "Arena-Reimagined/02-ARCHIVO/_etapas-anteriores/_herramientas/",
    "Arena-Reimagined/_herramientas-casa/": "Arena-Reimagined/02-ARCHIVO/_etapas-anteriores/_herramientas-casa/",
    "Arena-Reimagined/_referencia/": "Arena-Reimagined/02-ARCHIVO/_etapas-anteriores/_referencia/",
    "_archivo-historico/": "ARCHIVO-HISTORICO/",
}

EXTENSIONES_TEXTO: tuple[str, ...] = (
    ".md", ".py", ".json", ".tsv", ".csv", ".yaml", ".yml", ".txt", ".html", ".css", ".js",
)


@dataclass
class Cita:
    archivo: Path
    linea: int
    texto: str
    ruta_vieja: str


# Archivos que son registro por naturaleza, estén donde estén.
#
# POR QUÉ ESTA LISTA EXISTE
# -------------------------
# El criterio anterior era «si vive bajo docs/ o bajo ARCHIVO-HISTORICO, es
# histórico», y eso fallaba en los dos sentidos:
#
#   · declaraba VIVO un CHANGELOG que cuenta lo que pasó — y un registro de
#     cambios que cita ``uploads/`` no está roto: está contando que en su día
#     estuvo ahí;
#   · declaraba VIVO el MAPA-DEL-ARCHIVO, que es exactamente la tabla que
#     traduce los nombres viejos a los nuevos. Acusar al traductor de citar el
#     nombre viejo es absurdo: para eso está.
#
# Marcar 67 rutas como rotas cuando ninguna lo estaba es peor que no comprobar:
# un rojo que se sabe falso enseña a ignorar los rojos.
ARCHIVOS_DE_REGISTRO = {
    "CHANGELOG.md",          # cuenta lo que pasó, fechado
    "MAPA-DEL-ARCHIVO.md",   # es la tabla de mudanzas
    "INDICE.md",
    "LECCIONES.md",
    "DEPRECADOS.md",
    "referencias.py",          # contiene la tabla MUDANZAS: los nombres viejos están a propósito
    "mapa-de-mudanzas.json",   # ES la tabla: traduce los nombres viejos a los nuevos
}

# Carpetas cuyo contenido es acta, no documento vivo.
# `corpus-la-bandita/` son manuales de campo y traspasos de sesión, fechados: cuentan
# lo que se hizo en su día y sus rutas son las de entonces. Se conservan como actas.
# `00-CANON` es el canon congelado: ediciones fechadas que dicen de qué original
# se derivaron y dónde estaba ese original ese día. Retocar esa frase para que
# apunte a la carpeta de hoy sería falsificar el canon, que es justo lo que el
# canon prohíbe. La traducción de nombres vive en MAPA-DEL-ARCHIVO.md, que sí se
# actualiza.
CARPETAS_DE_REGISTRO = (
    "ARCHIVO-HISTORICO", "02-ARCHIVO", "_ARCHIVO-HISTORICO", "attestations",
    "corpus-la-bandita", "00-CANON",
)


def _es_acta_o_historico(ruta: Path) -> bool:
    partes = ruta.parts
    if any(p in CARPETAS_DE_REGISTRO for p in partes):
        return True
    if ruta.name in ARCHIVOS_DE_REGISTRO:
        return True
    # Bajo docs/ hay actas, cierres e informes con fecha en el nombre: se conservan.
    # Lo que NO se perdona es un documento vivo en la raíz citando una ruta muerta.
    return "docs" in partes


_CACHE_MUDANZAS: dict[str, str] | None = None
_CACHE_PATRONES: list[tuple[str, "re.Pattern[str]"]] | None = None


def _patrones_mudanzas() -> list[tuple[str, "re.Pattern[str]"]]:
    """Los patrones de las rutas viejas, compilados una sola vez.

    `re.escape` se llamaba 17.756.319 veces (una por ruta vieja y por línea auditada)
    y costaba 75 segundos. Los patrones no dependen del texto que se audita.
    """
    global _CACHE_PATRONES
    if _CACHE_PATRONES is None:
        _CACHE_PATRONES = [
            # Borde de ruta por delante: no puede venir pegado a una letra o un dígito.
            (rv, re.compile(r"(?<![\w./-])" + re.escape(rv.rstrip("/")) + r"/"))
            for rv in _mudanzas_del_arbol()
        ]
    return _CACHE_PATRONES


def _mudanzas_del_arbol() -> dict[str, str]:
    """Las mudanzas del árbol que se está auditando, no las de la máquina de quien corre.

    ANTES: `MUDANZAS` era una tabla fija en el código, copiada a todas partes. En la
    autoprueba, el árbol falso se audita con las mudanzas de la casa: busca rutas
    viejas que ese árbol nunca tuvo, no encuentra ninguna y declara «G17 en verde».
    La compuerta probaba el código equivocado y se aprobaba a sí misma.

    AHORA: se leen de `mapa-de-mudanzas.json` en la raíz del árbol auditado. La casa
    tiene el suyo; el árbol falso de la autoprueba, el suyo, con una mudanza
    sintética que SÍ existe. Si el archivo no está, se cae a la tabla del código,
    para no romper una corrida suelta.
    """
    # Con caché: antes esta función se llamaba 2.536.617 veces en una corrida, una por
    # cada mención candidata de cada línea de cada archivo, y cada llamada releía el
    # JSON del disco. Medido: 154 de los 192 segundos que tardaba la compuerta entera.
    # El árbol no cambia mientras se audita, así que se lee una vez.
    global _CACHE_MUDANZAS
    if _CACHE_MUDANZAS is not None:
        return _CACHE_MUDANZAS
    archivo = RAIZ / "mapa-de-mudanzas.json"
    if archivo.exists():
        try:
            d = json.loads(archivo.read_text(encoding="utf-8"))
            if isinstance(d, dict) and d:
                _CACHE_MUDANZAS = {str(k): str(v) for k, v in d.items()}
                return _CACHE_MUDANZAS
        except (json.JSONDecodeError, OSError):
            pass
    _CACHE_MUDANZAS = MUDANZAS
    return _CACHE_MUDANZAS


def _buscar_citas(contenido: str) -> list[str]:
    """Busca menciones a rutas viejas, entendiendo «ruta» como ruta.

    TRES FALSOS POSITIVOS QUE ESTA FUNCIÓN TENÍA, Y CÓMO SE CIERRAN
    --------------------------------------------------------------
    1. **La palabra inglesa.** `uploads/` casaba con la descripción de una app
       («This is an Android Spyware App, which uploads user data…») porque
       `re.escape` protege el texto pero nadie pedía que fuera una ruta. Una
       ruta empieza en un borde: principio de línea, espacio, comilla, paréntesis,
       barra o backtick. «which uploads» no empieza así.
    2. **La tabla de mudanzas.** `tools/referencias.py` contiene `MUDANZAS`, con
       los nombres viejos escritos a propósito. Se acusaba a sí misma; ahora está
       en la lista de excluidos.
    3. **La frase que explica la mudanza.** «la carpeta que se llamaba
       ``uploads/`` dejó de estar en la raíz» es la corrección, no el error.
       Citar el nombre viejo para decir que cambió es justo lo que se pide.
    """
    encontradas: list[str] = []
    for ruta_vieja, patron in _patrones_mudanzas():
        for m in patron.finditer(contenido):
            contexto = contenido[max(0, m.start() - 90):m.end() + 20].lower()
            if any(palabra in contexto for palabra in PALABRAS_DE_MUDANZA):
                continue  # cuenta la mudanza: no es una cita rota
            encontradas.append(ruta_vieja)
            break
    return encontradas


# Si el contexto de la cita dice que la ruta cambió, la cita es la explicación del
# cambio y no un enlace muerto.
PALABRAS_DE_MUDANZA = (
    "se llamaba", "se mudó", "se mudaron", "se movió", "se movieron", "dejó de estar",
    "antes era", "ya no existe", "renombr", "se traslad", "pasó a llamarse",
    "antiguo", "otrora", "histórico", "histórica",
)


def _auditar_archivo(ruta: Path) -> list[Cita]:
    if not ruta.suffix in EXTENSIONES_TEXTO:
        return []
    try:
        contenido = ruta.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return []
    citas: list[Cita] = []
    for i, linea in enumerate(contenido.splitlines(), 1):
        for rv in _buscar_citas(linea):
            citas.append(Cita(archivo=ruta, linea=i, texto=linea.strip(), ruta_vieja=rv))
    return citas


def main() -> int:
    citas_vivas: list[Cita] = []
    citas_historicas: list[Cita] = []

    for p in RAIZ.rglob("*"):
        if not p.is_file():
            continue
        if ".git" in p.parts:
            continue
        if p.name == ".gitignore":
            continue
        for c in _auditar_archivo(p):
            if _es_acta_o_historico(p):
                citas_historicas.append(c)
            else:
                citas_vivas.append(c)

    print(f"referencias: {len(citas_vivas)} rutas vivas rotas · {len(citas_historicas)} citas históricas")
    if citas_vivas:
        print("  ⚠ rutas vivas rotas (deben corregirse):")
        for c in citas_vivas[:20]:
            print(f"    {c.archivo.relative_to(RAIZ)}:{c.linea} · cita a {c.ruta_vieja}")
        print("  G17 impide que la próxima mudanza se olvide de esto.")
        return 1
    print("  0 rutas vivas rotas · G17 en verde")
    return 0


if __name__ == "__main__":
    sys.exit(main())
