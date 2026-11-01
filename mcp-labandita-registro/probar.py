#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prueba de extremo a extremo del servidor MCP contra su propio cliente oficial.

Arranca el servidor por stdio, enumera herramientas y llama a las seis.
Si algo de esto falla, el servidor no se publica: mismo criterio que la vara.

Uso: python3 mcp-labandita-registro/probar.py   (requiere pip install mcp)
"""
import asyncio, json, sys
from pathlib import Path
from pathlib import Path
import mcp
print('sdk:', getattr(mcp,'__version__','?'))
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    raiz = Path(__file__).resolve().parents[1]
    params = StdioServerParameters(command=sys.executable, args=[str(raiz / 'mcp-labandita-registro/servidor.py')], cwd=str(raiz))
    async with stdio_client(params) as (r, w):
        async with ClientSession(r, w) as s:
            await s.initialize()
            tools = await s.list_tools()
            nombres = [t.name for t in tools.tools]
            print('herramientas expuestas:', nombres)
            for nombre, args in [('censo_familia', {'familia': ''}),
                                 ('buscar_recurso', {'texto': 'manga', 'limite': 3}),
                                 ('estado_frescura', {'repo': 'Genymobile/scrcpy'}),
                                 ('verificar_licencia', {'repo': 'Genymobile/scrcpy'}),
                                 ('atestacion_lote', {})]:
                res = await s.call_tool(nombre, args)
                txt = res.content[0].text if res.content else '{}'
                datos = json.loads(txt)
                print(f'  {nombre}: ok · claves {list(datos)[:6]}')
    print('PRUEBA MCP: OK')
asyncio.run(main())
