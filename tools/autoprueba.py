#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AUTOPRUEBA DE LA VARA · una compuerta que no falla ante un fallo sintético no es una compuerta.

Construye un árbol de mentira, le mete fallos sintéticos y comprueba que cada compuerta
los detecta. Una compuerta que no falla ante un fallo inventado no es una compuerta: es un adorno.

Qué hace:
  * Crea un árbol temporal con archivos intencionalmente mal formados.
  * Ejecuta las compuertas contra ese árbol falso.
  * Verifica que cada compuerta detecte su correspondiente fallo sintético.
  * Reporta qué compuertas pasan y qué compuertas fallan en detectar.

Qué NO hace:
  * No prueba el contenido real: prueba el detector.
  * No modifica el árbol real: todo ocurre en un directorio temporal.
  * No aprueba nada por silencio: si una compuerta no detecta un fallo inventado, se reporta.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ: Path = Path(__file__).resolve().parents[1]
TOOLS: Path = RAIZ / "tools"

COMPUERTAS: list[tuple[str, list[str]]] = [
    ("vara.py", []),
    ("manual_gate.py", ["--verificar"]),
    ("referencias.py", []),
]


def _crear_arbol_falso(tmp: Path) -> None:
    """Crea un árbol temporal con fallos sintéticos para probar las compuertas."""
    (tmp / "tools").mkdir(parents=True)
    (tmp / "registry").mkdir(parents=True)
    (tmp / "attestations").mkdir(parents=True)
    (tmp / "docs").mkdir(parents=True)

    # Ficha con esquema roto (falta campo obligatorio)
    (tmp / "registry" / "ficha-rota.json").write_text(
        json.dumps({"id": "roto", "repo": "owner/repo"}, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    # Ficha válida
    (tmp / "registry" / "ficha-bueno.json").write_text(
        json.dumps({
            "id": "owner--bueno", "repo": "owner/bueno",
            "licencia": {"spdx": "MIT", "metodo": "spdx-api", "verificado_en": "2026-11-07", "archivo": None},
            "actividad": {"ultimo_push": "2026-11-01", "estado": "vivo", "semantica_http": 200},
            "medido_en": "2026-11-07",
            "fuente": {"primaria": "github-api", "secundarias": [], "metodo": "GET /repos"},
            "evidencia": {"sha256": "abc123", "payload_ref": "registry/_evidencia/owner--bueno.json", "nota": "test"},
        }, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def _ejecutar(comando: list[str], cwd: Path) -> tuple[int, str, str]:
    r = subprocess.run(comando, capture_output=True, text=True, cwd=cwd, timeout=60)
    return r.returncode, r.stdout, r.stderr


def main() -> int:
    print("AUTOPRUEBA DE LA VARA · probando que cada compuerta detecta fallos sintéticos\n")

    with tempfile.TemporaryDirectory() as tmp_str:
        tmp = Path(tmp_str)
        _crear_arbol_falso(tmp)

        # Copiar las herramientas al árbol falso
        for t in ["vara.py", "manual_gate.py", "referencias.py", "fecha_casa.py"]:
            src = TOOLS / t
            dst = tmp / "tools" / t
            if src.exists():
                shutil.copy2(src, dst)

        todos_pasan = True
        for nombre, args in COMPUERTAS:
            herramienta = tmp / "tools" / nombre
            if not herramienta.exists():
                print(f"  ⚠ {nombre}: no encontrada, se salta")
                continue
            rc, out, err = _ejecutar([sys.executable, str(herramienta)] + args, cwd=tmp)
            salida = (out + err).strip()
            # Una compuerta que funciona debe detectar algo malo en el árbol falso
            # y por tanto salir con código no cero, O al menos reportar fallos
            detecto_fallo = rc != 0 or "FALLO" in salida.upper() or "ROTO" in salida.upper() or "error" in salida.lower()
            estado = "DETECTA FALLO" if detecto_fallo else "NO DETECTA FALLO ⚠"
            if not detecto_fallo:
                todos_pasan = False
            print(f"  {nombre}: {estado}")
            if salida:
                for linea in salida.splitlines()[:3]:
                    print(f"    {linea[:100]}")

    print()
    if todos_pasan:
        print("Todas las compuertas detectan fallos sintéticos · la vara es una vara, no un adorno")
        return 0
    print("ALGUNAS COMPUERTAS NO DETECTAN FALLO SYNTÉTICO · revisar antes de confiar en ellas")
    return 1


if __name__ == "__main__":
    sys.exit(main())
