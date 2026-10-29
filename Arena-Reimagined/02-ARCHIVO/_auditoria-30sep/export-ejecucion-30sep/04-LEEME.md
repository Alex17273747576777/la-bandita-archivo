# LÉEME — Exportación de la ejecución del 30-sep-2026
**Proyecto:** La Bandita · **Generado:** 30-sep-2026 (America/Santo_Domingo) · **Emitido por:** taller de La Bandita

## Qué contiene este paquete
| archivo | contenido |
|---|---|
| `00-REPORTE-EJECUCION-30sep.html` | **Informe principal autocontenido** (sin recursos externos; imprimible). Léalo primero. |
| `01-censo-bandas-WA-FB-30sep.csv` | Censo completo de las 25 piezas contra las bandas del dueño (FB 40.000–45.000 c; WA ≥63.000 c). Abrible en cualquier hoja de cálculo. |
| `02-diff-FB10-PRE-post-30sep.txt` | Evidencia integral de las 48 reparaciones quirúrgicas de la pieza FB 10 (formato diff unificado: texto antes → texto después). |
| `03-extracto-acta-tren-28-y-28bis-30sep.txt` | La sección del acta oficial que registra la palabra del dueño, el censo, y la ejecución del par 02 (trenes 28 / 28-bis). |
| `consultas/05-…06-…07-…` | COPIAS DE CONSULTA de las piezas trabajadas hoy: WA 02 y FB 02 (cerradas en banda, con su inserción datada) y FB 10 (texto íntegro reparado). |

## Qué archivo es canónico (regla de la casa)
Los canónicos **viven:** las piezas en `01-PUBLICACIONES/<plataforma>/`; el acta en `02-ARCHIVO/estado-expansion-ES-2026-09-22.md`; el respaldo pre-auditoría en `02-ARCHIVO/_auditoria-30sep/originales/`. **Todo lo de esta carpeta es copia fiel para descarga y análisis; no edite aquí.**

## Cómo verificar (comandos reproducibles)
- Medida de caracteres (única vara — `len()` UTF-8):
  `python3 -c "print(len(open('RUTA',encoding='utf-8').read()))"`
- Integridad de los archivos del paquete: compare contra `04-MANIFIESTO-SHA256.txt` con
  `cd <carpeta extraída> && sha256sum -c 04-MANIFIESTO-SHA256.txt` (las rutas del manifiesto ya vienen listas).

## Estado contable del régimen nuevo (foto 30-sep)
- WA: 4/12 piezas en banda (01 · 02 · 10 · 81) — cola de segunda pasada: 03, 05, 06, 07, 08, 09, y las dos variantes de la 04.
- FB: 3/13 en banda (01 · 02 · 04-Extensiones) — cola: cerradas (03, 07, 81) y copas cortas (05, 06, 08, 09, 10, 04-Almacenes, 15).
- Decisiones abiertas del dueño: heredero canónico de la pieza 04; expansión de fondo de las copas cortas FB.
