#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CONEXIÓN REAL A SERVIDORES MCP · handshake, listado de herramientas y llamada de prueba.

Lo que este programa NO hace: inventar conectores. Habla el protocolo tal cual —JSON-RPC 2.0 sobre
Streamable HTTP— con los servidores que publican un endpoint abierto, y deja acta de lo que cada uno
contestó: si abrió sesión, cuántas herramientas ofrece y cuáles. Un servidor que pide credenciales se
declara como tal y no se simula: la credencial la pone el dueño, no este programa.

Uso:
  python3 tools/mcp_conectar.py --probar
  python3 tools/mcp_conectar.py --llamar URL TOOL '{"arg":"valor"}'
  python3 tools/mcp_conectar.py --registro
"""
from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request
from datetime import date, datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
REGISTRO = "https://registry.modelcontextprotocol.io/v0/servers?limit=100"
UA = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream",
      "User-Agent": "la-bandita-mcp/1.0"}

ENDPOINTS = [
    "https://mcp.deepwiki.com/mcp",
    "https://mcp.context7.com/mcp",
    "https://gitmcp.io/docs",
    "https://huggingface.co/mcp",
    "https://api.inference.sh/mcp",
    "https://mcp.snag.ac/mcp",
    "https://tandem.ac/mcp",
    "https://mcp.linear.app/mcp",
    "https://mcp.notion.com/mcp",
    "https://api.githubcopilot.com/mcp/",
]


def _parsear(cuerpo: str, tipo: str) -> list[dict]:
    if "text/event-stream" in tipo:
        out = []
        for bloque in cuerpo.split("\n\n"):
            for linea in bloque.splitlines():
                if linea.startswith("data:"):
                    try:
                        out.append(json.loads(linea[5:].strip()))
                    except Exception:
                        pass
        return out
    try:
        d = json.loads(cuerpo)
        return d if isinstance(d, list) else [d]
    except Exception:
        return []


def _post(url: str, carga: dict, sesion: str | None = None) -> tuple[int, list[dict], str | None]:
    cab = dict(UA)
    if sesion:
        cab["Mcp-Session-Id"] = sesion
    req = urllib.request.Request(url, data=json.dumps(carga).encode(), headers=cab, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            cuerpo = r.read().decode("utf-8", "replace")
            sid = r.headers.get("Mcp-Session-Id") or r.headers.get("mcp-session-id")
            return r.status, _parsear(cuerpo, r.headers.get("Content-Type", "")), sid
    except urllib.error.HTTPError as e:
        return e.code, [], None
    except Exception:
        return 0, [], None


def _init(url: str):
    cod, msgs, sid = _post(url, {"jsonrpc": "2.0", "id": 1, "method": "initialize",
                                 "params": {"protocolVersion": "2025-06-18", "capabilities": {},
                                            "clientInfo": {"name": "la-bandita", "version": "1.0"}}})
    init = next((m.get("result") for m in msgs if m.get("result")), None)
    if init:
        _post(url, {"jsonrpc": "2.0", "method": "notifications/initialized", "params": {}}, sid)
    return cod, init, sid


def handshake(url: str) -> dict:
    e = {"url": url, "protocolo": None, "servidor": None, "herramientas": [], "nota": ""}
    cod, init, sid = _init(url)
    if cod in (401, 403):
        e["nota"] = f"exige credenciales (HTTP {cod})"
        return e
    if cod == 404:
        e["nota"] = "sin endpoint MCP en esa ruta (404)"
        return e
    if not init:
        e["nota"] = f"sin respuesta de initialize (HTTP {cod})"
        return e
    e["protocolo"] = init.get("protocolVersion")
    e["servidor"] = (init.get("serverInfo") or {}).get("name")
    cod2, msgs2, _ = _post(url, {"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}}, sid)
    for m in msgs2:
        for t in ((m.get("result") or {}).get("tools") or []):
            e["herramientas"].append({"nombre": t.get("name"),
                                      "descripcion": (t.get("description") or "")[:120]})
    if not e["herramientas"]:
        e["nota"] = e["nota"] or f"initialize OK pero tools/list vacio (HTTP {cod2})"
    return e


def llamar(url: str, tool: str, args: dict) -> dict:
    cod, init, sid = _init(url)
    if not init:
        return {"error": f"initialize falló (HTTP {cod})"}
    cod2, msgs2, _ = _post(url, {"jsonrpc": "2.0", "id": 3, "method": "tools/call",
                                 "params": {"name": tool, "arguments": args}}, sid)
    for m in msgs2:
        if m.get("result") or m.get("error"):
            return m
    return {"error": f"sin respuesta de tools/call (HTTP {cod2})"}


def registro() -> dict:
    with urllib.request.urlopen(urllib.request.Request(REGISTRO,
                                headers={"User-Agent": UA["User-Agent"]}), timeout=40) as r:
        d = json.loads(r.read().decode())
    s = d.get("servers") or []
    remotos: dict[str, str] = {}
    for x in s:
        sv = x.get("server", x)
        for rm in (sv.get("remotes") or []):
            if rm.get("url"):
                remotos.setdefault(sv.get("name"), rm["url"])
    return {"total_pagina": len(s), "con_remoto": len(remotos),
            "ejemplos": list(remotos.items())[:20]}


def main() -> int:
    a = sys.argv[1:]
    hoy = date.today().isoformat()
    if "--registro" in a:
        print(json.dumps(registro(), ensure_ascii=False, indent=1)[:2500])
        return 0
    if "--llamar" in a:
        i = a.index("--llamar")
        args = json.loads(a[i + 3]) if len(a) > i + 3 else {}
        print(json.dumps(llamar(a[i + 1], a[i + 2], args), ensure_ascii=False)[:4000])
        return 0
    if "--probar" not in a:
        print(__doc__)
        return 2
    acta = []
    for url in ENDPOINTS:
        e = handshake(url)
        acta.append(e)
        print(f"{url[:42]:<42} {'sesion' if e['herramientas'] else 'sin herramientas':<16} "
              f"{len(e['herramientas']):>3} tools  {e.get('servidor') or ''} {e['nota'][:50]}")
    vivas = [x for x in acta if x["herramientas"]]
    salida = RAIZ / "docs" / f"MCP-{hoy}.json"
    salida.write_text(json.dumps({"fecha": hoy,
                                  "medido_en": datetime.now().astimezone().isoformat(timespec="seconds"),
                                  "probados": len(acta), "con_herramientas": len(vivas),
                                  "herramientas_totales": sum(len(x["herramientas"]) for x in acta),
                                  "servidores": acta}, ensure_ascii=False, indent=1) + "\n",
                      encoding="utf-8")
    print(f"\nMCP: {len(vivas)} de {len(acta)} servidores abiertos · "
          f"{sum(len(x['herramientas']) for x in acta)} herramientas listadas · acta en {salida.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
