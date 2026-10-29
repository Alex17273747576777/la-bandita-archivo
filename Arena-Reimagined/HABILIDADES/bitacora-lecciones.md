# BITÁCORA DE LECCIONES · LA BANDITA
_Cada lección costó tiempo real. Leerla antes de trabajar ahorra el próximo tropiezo._

## L-01 · 2026-10-29
- **Contexto:** Cambio de turno del entorno.
- **Fallo/experiencia:** El snapshot del workspace se comió publicaciones, datos y hasta scripts en /tmp (la «mordida»).
- **Regla que queda:** Nada se afirma sin inventario primero; el suelo se verifica con hash (verificar-suelo) y se restaura en este orden: GitHub > espejo > proyecto. Las herramientas vivas viven DENTRO del proyecto, jamás en /tmp.

## L-02 · 2026-10-29
- **Contexto:** Medición masiva de repos.
- **Fallo/experiencia:** ráfagas HTTP devolvieron 429/403 y casi se declaran muertos repos vivos; un 451 (bloqueo legal, p. ej. Dantotsu/Miru) parece 404 y no lo es.
- **Regla que queda:** 404 = muerto · 451 = existe bloqueado · 403/429 = cuota o bot, se reintenta con calma y guardado incremental. Nunca se declara muerto un repo por un error de cuota.

## L-03 · 2026-10-29
- **Contexto:** Licencias de cientos de repos.
- **Fallo/experiencia:** GitHub no siempre resuelve el SPDX (NOASSERTION) y su endpoint de licencia a veces no ve un LICENSE válido (caso SeedVault).
- **Regla que queda:** Orden de verdad de licencias: SPDX de GitHub → endpoint `/license` → lectura directa del LICENSE en las rutas comunes → si no hay archivo, se firma «sin archivo LICENSE en la raíz (verificado)». Jamás se inventa un SPDX.

## L-04 · 2026-10-29
- **Contexto:** Guardado en GitHub con token.
- **Fallo/experiencia:** El token como literal en la terminal lo transforma la redacción automática y los push fallan «sin usuario»; cada shell nueva pierde las variables del askpass.
- **Regla que queda:** Un solo procedimiento contenido (herramientas/guardar.py): entorno completo dentro del proceso, askpass temporal, push, ls-remote y clonación fresca byte por byte. El token nunca se imprime ni se guarda.

## L-05 · 2026-10-29
- **Contexto:** Piezas generadas en masa en octubre.
- **Fallo/experiencia:** La máquina inflaba piezas repitiendo párrafos (70.011 caracteres de eco) y un carácter corrupto sobrevivió semanas en WhatsApp 10.
- **Regla que queda:** Toda hornada pasa dedupe de párrafos exactos, escaneo de mojibake y lupa antes de hornear el catálogo; el corpus se re-hashea (manifiesto) tras cualquier cirugía.

## L-06 · 2026-10-29
- **Contexto:** Cifras impresas a mitad de camino.
- **Fallo/experiencia:** Al resolverse las licencias, 65 placas ya publicadas seguían diciendo «sin resolver».
- **Regla que queda:** Cerrar un dato global obliga a barrer el corpus por la frase vieja y aplicar fe de cierre pieza por pieza: el dato nuevo persigue al texto, no al revés.

## L-07 · 2026-10-29
- **Contexto:** Push final de la entrega (29-oct)
- **Fallo/experiencia:** La sesión demostró que el conocimiento sin herramienta se pierde entre turnos: cada vara tuvo que re-inventarse al cambiar de contexto
- **Regla que queda:** Todo procedimiento que se use dos veces se convierte en herramienta ejecutable dentro de HABILIDADES/, con su lección en la bitácora
