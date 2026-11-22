# Reglas vigentes de publicación y archivo de La Bandita

> Corte operativo: **21 de noviembre de 2026**.  
> Precedencia: `CORAZON-LA-BANDITA.md` · `CIMIENTOS/01-PRECEDENCIA.md` · `REGLAS/INDICE-DE-REGLAS.md`.

## Método Richard Feynman (4 pasos obligatorios)

1. **Seleccionar y estudiar el concepto:** Este archivo separa con precisión lo que está **retirado** (`Arena-Reimagined/01-PUBLICACIONES/`, suprimida el 15-nov-2026 por decisión del dueño) de las **publicaciones y registros vigentes** del archivo: la Guía Maestra (`guia-maestra/`, 12 capítulos y 70 fichas verificadas), el registro medido (`registry/`, 6.838 fichas con SHA-256), los paquetes congelados de envío (`docs/envios/facebook/`, `docs/envios/whatsapp/`, `_historico/`), los moldes canónicos (`ENTORNO-DE-TRABAJO/moldes/`) y la página pública congelada (`web/`).
2. **Enseñarlo con palabras simples:** El archivo no borra su memoria histórica ni inventa actividad donde se retiró una serie: deja explícito qué sigue vivo para consulta o envío y exige que cada regla nueva pase cuatro puertas antes de existir (nota en el CORAZON, sincronización en `bandas.json`/herramientas, acta con sello encadenado SHA-256 y entrada en el índice de reglas).
3. **Identificar lagunas y volver a la fuente original:** Al ejecutar `tools/vara_idiomas.py` tras el retiro del 15-nov, la herramienta marcaba `2 ROJOS` por ausencia de `Arena-Reimagined/01-PUBLICACIONES` aunque la norma declaraba retiradas las compuertas sobre aire. Corregida en `tools/vara_idiomas.py` y verificada con `tests/test_vara_idiomas.py` para auditar los moldes canónicos en modo retiro y activar G20–G23 estrictas en cuanto exista ruta o carpeta activa.
4. **Simplificar y revisar con analogías claras:** Es como una biblioteca donde una colección temporal se retiró de la sala principal: el catálogo maestro, las actas y las ediciones modelo siguen sellados en vitrina, y el guardia de la puerta (`vara.py` / `vara_idiomas.py`) no multa por estantes vacíos declarados en acta, pero sí revisa que los modelos en vitrina y los sellos diarios sigan intactos. *Límite de la analogía:* un guardia físico mira etiquetas a ojo; aquí cada byte del repositorio se comprueba mediante sumas SHA-256 encadenadas (`tools/atestar.py`).

---

## Mapa operativo de las publicaciones del archivo

| Bloque | Ruta | Estado | Regla que lo gobierna |
| :--- | :--- | :--- | :--- |
| **Guía Maestra** | `guia-maestra/` | **Vigente (12 cap., 70 fichas)** | `make medir-guia` · 4 pasos Feynman (`tools/feynman_verificar.py`) |
| **Registro medido** | `registry/registro.db` | **Vigente (6.838 fichas)** | `python3 tools/registro_construir.py --verificar` + huella lógica en `atestar.py` |
| **Envíos congelados** | `docs/envios/` | **Congelado (259 envíos)** | 1 pieza por envío (`docs/envios/COMO-SE-MANDA.md`), tope ≤ 4.000 car. WA, firma `💓` |
| **Moldes canónicos** | `ENTORNO-DE-TRABAJO/moldes/` | **Vigente (ES + EN)** | Referencia G20–G23 verificada por `tools/vara_idiomas.py` |
| **Web pública** | `web/` | **Congelada en Pages** | Despliegue vía `.github/workflows/pagina.yml` (`HTTP 200`, 3.116 repos) |
| **Serie canal viva** | `Arena-Reimagined/01-PUBLICACIONES/` | **Retirada (15-nov-2026)** | `CORAZON-LA-BANDITA.md` Addendum de retiro · historia en git |

---

## Checklist obligatorio para reactivar o publicar una serie nueva

1. Cumplir la banda del maestro (`6.000`–`45.000` car. en `docs/bandas.json`) y la norma completa de 4 pasos de Richard Feynman.
2. Derivar por idioma/plataforma (`es-dominicano`: FB/WA/IG/TG; `en-ingles`: Reddit/X/Discord/TG) pasando **`tools/vara_idiomas.py`** sin rojos (`G20`–`G23`).
3. Verificar **`make verificar`** (`fallos: NINGUNO`), actualizar **`make libro`** y resellar con **`make sellar`** (`attestations/lote-AAAA-MM-DD.{json,tsv}`).
