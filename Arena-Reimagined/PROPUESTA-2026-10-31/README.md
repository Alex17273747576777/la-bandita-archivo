# PROPUESTA 2026-10-31 — de archivo verificado a empresa de verificación

Paquete de la propuesta empresarial entregada al dueño el **31 de octubre de 2026**.

| Archivo | Qué es |
|---|---|
| `PROPUESTA-LA-BANDITA-EMPRESA.md` | documento maestro (≈6.300 palabras, 13 secciones) |
| `propuesta-la-bandita.html` | presentación web autocontenida: sin CDN, sin fuentes ni imágenes remotas |
| `datos/medicion-2026-10-31.json` | la medición del repositorio que sostiene el diagnóstico |
| `datos/ejemplo-ficha.json` | ficha de ejemplo escrita contra el contrato de datos |
| `anexos/ficha.schema.json` | contrato de datos v1 (JSON Schema) del registro |
| `anexos/vara-ci.yml` | plantilla de las ocho compuertas en integración continua (no activa) |
| `anexos/construir-html.py` · `estilo.css` · `app.js` | fuentes de la presentación: se reconstruye con `python3 anexos/construir-html.py` |

## Verificación de esta entrega

- Documento y HTML generados desde la misma fuente (`PROPUESTA-LA-BANDITA-EMPRESA.md`).
- HTML sin recursos externos: `0` referencias `http(s)` en `src`/`href`.
- Revisado en Chromium a 1440×900 y 390×844: cero errores de consola, cero errores de JavaScript.
- Búsqueda interna probada: 12 coincidencias para «compuerta»; seis paletas con persistencia; sonido sintetizado apagado por defecto.
- Esquema y ficha de ejemplo validados con `jsonschema`.
- Plantilla YAML de CI validada como YAML.

## Lo que este paquete no decide

La licencia del repositorio, la marca, el canal primario, la política de patrocinio y la publicación del
servidor MCP son decisiones del dueño (§11 del documento). Nada de eso se ejecutó por cuenta propia.
