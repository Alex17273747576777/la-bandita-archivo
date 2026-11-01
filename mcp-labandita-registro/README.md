# labandita-registro · servidor MCP

Servidor **MCP de solo lectura** sobre el registro verificado de La Bandita: 5.684 fichas de
repositorios del ecosistema Android libre, medidas el 15 de octubre de 2026 contra la API oficial
de GitHub.

## Regla de honestidad

Ninguna herramienta responde una afirmación sin fecha. Cada respuesta trae `medido_en`, `fuente`
y `estado_frescura`. Si el dato supera el umbral (180 días), la respuesta dice **`rancio`** con la
edad exacta en vez de presentarlo como actual. La ausencia también se firma: un repositorio que no
está en el registro devuelve `error: no está en el registro`, nunca una ficha inventada.

## Herramientas

| Herramienta | Entrada | Devuelve |
|---|---|---|
| `buscar_recurso` | texto, límite | coincidencias ordenadas por estrellas, con fecha y licencia |
| `ficha_recurso` | `owner/name` | la ficha completa, con evidencia y sello |
| `censo_familia` | familia (opcional) | agregados: cuántas fichas, vivos, dormidos, licencias |
| `estado_frescura` | `owner/name` | edad del dato, veredicto vigente/rancio y recomendación |
| `verificar_licencia` | `owner/name` | veredicto por el orden SPDX → endpoint → texto → ausencia firmada |
| `atestacion_lote` | lote (opcional) | atestación del último lote y la cadena de huellas |

## Instalación y ejecución

```bash
pip install "mcp>=2,<3"     # SDK oficial; también funciona con mcp<2 (FastMCP)
python3 mcp-labandita-registro/servidor.py            # transporte stdio
python3 mcp-labandita-registro/probar.py              # prueba de extremo a extremo
```

## Configuración en un cliente MCP

```json
{
  "mcpServers": {
    "labandita-registro": {
      "command": "python3",
      "args": ["/ruta/al/repo/mcp-labandita-registro/servidor.py"]
    }
  }
}
```

## Política de seguridad del servidor

1. **Solo lectura.** No hay ninguna herramienta que escriba, borre ni ejecute comandos.
2. **Sin red.** Lee archivos locales del propio repositorio; no llama a ninguna API.
3. **Sin credenciales.** No pide token, no lee variables de entorno con secretos.
4. **Sin estado.** No guarda nada entre llamadas; la caché vive en memoria del proceso.
5. **Transporte local.** stdio por defecto. Exponerlo por HTTP exigiría autenticación y cuotas,
   y no se hace hasta que exista demanda pagada (fase F5 de la propuesta).

## Lo que este servidor no es

No es un buscador de Internet ni un recomendador. Es el registro de la casa servido con contrato.
Si un dato no está, no está; y si está viejo, lo dice.
