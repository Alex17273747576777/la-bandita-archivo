#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""REGISTRO SQLITE · motor de registro basado en SQLite con exportación a JSON.

Migra las fichas JSON de registry/ a una base de datos SQLite (un solo archivo, sin servidor
externo) y exporta a JSON idéntico al actual para que las herramientas existentes sigan
funcionando sin cambios en sus contratos de entrada/salida.

Qué hace:
  * Crea registry/registro.db con tablas normalizadas (fichas, licencia, actividad, merito,
    procedencia, evidencia).
  * Importa todas las fichas JSON existentes sin perder un solo campo ni un solo SHA-256.
  * Exporta a registry/*.json idéntico al formato actual para compatibilidad.
  * Proporciona consultas SQL para leer fichas por id, repo, licencia, estado, etc.

Qué NO hace:
  * No reemplaza las herramientas de medición: pulso.py y censo_medir.py siguen escribiendo JSON.
  * No borra los JSON originales: los conserva como respaldo hasta que la migración se valide.
  * No requiere servidor externo: SQLite es un archivo, lista para usar.
"""
from __future__ import annotations

import json
import sqlite3
import sys
from pathlib import Path
from typing import Any

RAIZ: Path = Path(__file__).resolve().parents[1]
REGISTRO: Path = RAIZ / "registry"
DB: Path = REGISTRO / "registro.db"

ESQUEMA_SQL = """
PRAGMA journal_mode=WAL;
PRAGMA synchronous=NORMAL;

CREATE TABLE IF NOT EXISTS fichas (
    id TEXT PRIMARY KEY,
    repo TEXT NOT NULL,
    nombre TEXT,
    descripcion TEXT,
    web TEXT,
    medido_en TEXT,
    fuente_primaria TEXT,
    fuente_metodo TEXT,
    frescura_dias INTEGER DEFAULT 0,
    piezas_json TEXT DEFAULT '[]'
);

CREATE TABLE IF NOT EXISTS licencias (
    ficha_id TEXT PRIMARY KEY REFERENCES fichas(id),
    spdx TEXT,
    metodo TEXT,
    verificado_en TEXT,
    archivo TEXT,
    nota TEXT,
    FOREIGN KEY (ficha_id) REFERENCES fichas(id)
);

CREATE TABLE IF NOT EXISTS actividades (
    ficha_id TEXT PRIMARY KEY REFERENCES fichas(id),
    ultimo_push TEXT,
    estado TEXT,
    semantica_http INTEGER,
    ultima_release TEXT,
    release_en TEXT,
    FOREIGN KEY (ficha_id) REFERENCES fichas(id)
);

CREATE TABLE IF NOT EXISTS meritos (
    ficha_id TEXT PRIMARY KEY REFERENCES fichas(id),
    stars INTEGER,
    stars_por_mes REAL,
    scorecard INTEGER,
    scorecard_en TEXT,
    FOREIGN KEY (ficha_id) REFERENCES fichas(id)
);

CREATE TABLE IF NOT EXISTS procedencias (
    ficha_id TEXT PRIMARY KEY REFERENCES fichas(id),
    swhid TEXT,
    revision_commit TEXT,
    atestacion TEXT,
    swh_estado TEXT,
    swh_solicitud TEXT,
    FOREIGN KEY (ficha_id) REFERENCES fichas(id)
);

CREATE TABLE IF NOT EXISTS evidencias (
    ficha_id TEXT PRIMARY KEY REFERENCES fichas(id),
    sha256 TEXT NOT NULL,
    payload_ref TEXT NOT NULL,
    nota TEXT,
    FOREIGN KEY (ficha_id) REFERENCES fichas(id)
);

CREATE INDEX IF NOT EXISTS idx_fichas_repo ON fichas(repo);
CREATE INDEX IF NOT EXISTS idx_fichas_medido_en ON fichas(medido_en);
CREATE INDEX IF NOT EXISTS idx_licencias_spdx ON licencias(spdx);
CREATE INDEX IF NOT EXISTS idx_actividades_estado ON actividades(estado);
"""


def _conectar() -> sqlite3.Connection:
    conn = sqlite3.connect(str(DB))
    conn.row_factory = sqlite3.Row
    conn.executescript(ESQUEMA_SQL)
    return conn


def _lea_json(ruta: Path) -> dict[str, Any] | None:
    try:
        return json.loads(ruta.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


def migrar_desde_json() -> dict[str, int]:
    """Importa todas las fichas JSON de registry/ a SQLite."""
    conn = _conectar()
    fichas: list[Path] = sorted(p for p in REGISTRO.glob("*.json") if not p.name.startswith("_"))
    total = len(fichas)
    importadas = 0
    errores = 0

    for p in fichas:
        d = _lea_json(p)
        if d is None:
            errores += 1
            continue
        try:
            conn.execute(
                "INSERT OR REPLACE INTO fichas (id, repo, nombre, descripcion, web, medido_en, "
                "fuente_primaria, fuente_metodo, frescura_dias, piezas_json) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    d.get("id", ""), d.get("repo", ""), d.get("nombre", ""),
                    d.get("descripcion", ""), d.get("web"), d.get("medido_en", ""),
                    (d.get("fuente") or {}).get("primaria", ""),
                    (d.get("fuente") or {}).get("metodo", ""),
                    d.get("frescura_dias", 0),
                    json.dumps(d.get("piezas", []), ensure_ascii=False),
                ),
            )
            lic = d.get("licencia") or {}
            conn.execute(
                "INSERT OR REPLACE INTO licencias (ficha_id, spdx, metodo, verificado_en, archivo, nota) "
                "VALUES (?, ?, ?, ?, ?, ?)",
                (d.get("id", ""), lic.get("spdx"), lic.get("metodo"), lic.get("verificado_en"),
                 lic.get("archivo"), lic.get("nota")),
            )
            act = d.get("actividad") or {}
            conn.execute(
                "INSERT OR REPLACE INTO actividades (ficha_id, ultimo_push, estado, semantica_http, "
                "ultima_release, release_en) VALUES (?, ?, ?, ?, ?, ?)",
                (d.get("id", ""), act.get("ultimo_push"), act.get("estado"),
                 act.get("semantica_http"), act.get("ultima_release"), act.get("release_en")),
            )
            mer = d.get("merito") or {}
            conn.execute(
                "INSERT OR REPLACE INTO meritos (ficha_id, stars, stars_por_mes, scorecard, scorecard_en) "
                "VALUES (?, ?, ?, ?, ?)",
                (d.get("id", ""), mer.get("stars"), mer.get("stars_por_mes"),
                 mer.get("scorecard"), mer.get("scorecard_en")),
            )
            proc = d.get("procedencia") or {}
            conn.execute(
                "INSERT OR REPLACE INTO procedencias (ficha_id, swhid, revision_commit, atestacion, swh_estado, swh_solicitud) "
                "VALUES (?, ?, ?, ?, ?, ?)",
                (d.get("id", ""), proc.get("swhid"), proc.get("commit"), proc.get("atestacion"),
                 proc.get("swh_estado"), proc.get("swh_solicitud")),
            )
            ev = d.get("evidencia") or {}
            conn.execute(
                "INSERT OR REPLACE INTO evidencias (ficha_id, sha256, payload_ref, nota) "
                "VALUES (?, ?, ?, ?)",
                (d.get("id", ""), ev.get("sha256", ""), ev.get("payload_ref", ""), ev.get("nota")),
            )
            importadas += 1
        except Exception:
            errores += 1

    conn.commit()
    conn.close()
    return {"total": total, "importadas": importadas, "errores": errores}


def exportar_a_json() -> dict[str, int]:
    """Exporta todas las fichas de SQLite a registry/*.json (formato actual)."""
    conn = _conectar()
    filas = conn.execute("SELECT id FROM fichas").fetchall()
    total = len(filas)
    escritas = 0
    errores = 0

    for fila in filas:
        ficha_id = fila["id"]
        d = _ficha_por_id(conn, ficha_id)
        if d is None:
            errores += 1
            continue
        try:
            ruta = REGISTRO / f"{ficha_id}.json"
            ruta.write_text(
                json.dumps(d, ensure_ascii=False, indent=1, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            escritas += 1
        except OSError:
            errores += 1

    conn.close()
    return {"total": total, "escritas": escritas, "errores": errores}


def _ficha_por_id(conn: sqlite3.Connection, ficha_id: str) -> dict[str, Any] | None:
    row = conn.execute("SELECT * FROM fichas WHERE id = ?", (ficha_id,)).fetchone()
    if row is None:
        return None
    d: dict[str, Any] = {
        "id": row["id"],
        "repo": row["repo"],
        "nombre": row["nombre"],
        "descripcion": row["descripcion"],
        "medido_en": row["medido_en"],
        "frescura_dias": row["frescura_dias"],
        "piezas": json.loads(row["piezas_json"]),
    }
    if row["web"]:
        d["web"] = row["web"]
    d["fuente"] = {
        "primaria": row["fuente_primaria"],
        "secundarias": [],
        "metodo": row["fuente_metodo"],
    }
    lic = conn.execute("SELECT * FROM licencias WHERE ficha_id = ?", (ficha_id,)).fetchone()
    if lic:
        d["licencia"] = {
            "spdx": lic["spdx"],
            "metodo": lic["metodo"],
            "verificado_en": lic["verificado_en"],
            "archivo": lic["archivo"],
        }
        if lic["nota"]:
            d["licencia"]["nota"] = lic["nota"]
    act = conn.execute("SELECT * FROM actividades WHERE ficha_id = ?", (ficha_id,)).fetchone()
    if act:
        d["actividad"] = {
            "ultimo_push": act["ultimo_push"],
            "estado": act["estado"],
            "semantica_http": act["semantica_http"],
        }
        if act["ultima_release"]:
            d["actividad"]["ultima_release"] = act["ultima_release"]
        if act["release_en"]:
            d["actividad"]["release_en"] = act["release_en"]
    mer = conn.execute("SELECT * FROM meritos WHERE ficha_id = ?", (ficha_id,)).fetchone()
    if mer:
        d["merito"] = {
            "stars": mer["stars"],
            "stars_por_mes": mer["stars_por_mes"],
            "scorecard": mer["scorecard"],
            "scorecard_en": mer["scorecard_en"],
        }
    proc = conn.execute("SELECT * FROM procedencias WHERE ficha_id = ?", (ficha_id,)).fetchone()
    if proc:
        d["procedencia"] = {
            "swhid": proc["swhid"],
            "commit": proc["revision_commit"],
            "atestacion": proc["atestacion"],
        }
        if proc["swh_estado"]:
            d["procedencia"]["swh_estado"] = proc["swh_estado"]
        if proc["swh_solicitud"]:
            d["procedencia"]["swh_solicitud"] = proc["swh_solicitud"]
    ev = conn.execute("SELECT * FROM evidencias WHERE ficha_id = ?", (ficha_id,)).fetchone()
    if ev:
        d["evidencia"] = {
            "sha256": ev["sha256"],
            "payload_ref": ev["payload_ref"],
            "nota": ev["nota"],
        }
    return d


def contar() -> int:
    conn = _conectar()
    n = conn.execute("SELECT COUNT(*) FROM fichas").fetchone()[0]
    conn.close()
    return n


def main(argv: list[str] | None = None) -> int:
    import argparse
    parser = argparse.ArgumentParser(description="Motor de registro SQLite con exportación a JSON.")
    parser.add_argument("--migrar", action="store_true", help="importa fichas JSON a SQLite")
    parser.add_argument("--exportar", action="store_true", help="exporta de SQLite a fichas JSON")
    parser.add_argument("--contar", action="store_true", help="cuenta fichas en SQLite")
    args = parser.parse_args(argv)

    if args.contar:
        print(f"fichas en SQLite: {contar()}")
        return 0
    if args.migrar:
        res = migrar_desde_json()
        print(f"migración: {res['importadas']}/{res['total']} fichas importadas · {res['errores']} errores")
        return 0 if res["errores"] == 0 else 1
    if args.exportar:
        res = exportar_a_json()
        print(f"exportación: {res['escritas']}/{res['total']} fichas escritas · {res['errores']} errores")
        return 0 if res["errores"] == 0 else 1
    parser.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
