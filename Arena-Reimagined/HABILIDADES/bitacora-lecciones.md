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

## L-08 · 2026-10-29
- **Contexto:** Primera corrida real de guardar.py tras su nacimiento
- **Fallo/experiencia:** Empujó bien pero su verificación ls-remote corría fuera del clon y murió con 128: la herramienta no se había probado a sí misma entera
- **Regla que queda:** Toda herramienta de guardado se prueba de punta a punta en su primera corrida, incluida la verificación posterior al push; si una vara no se prueba entera, no está terminada

## L-09 · 2026-10-29
- **Contexto:** Reorden de carpetas del 29-oct
- **Fallo/experiencia:** La carpeta _rearm-29oct solo se entendía con contexto y las herramientas apuntaban a ella: renombrar sin actualizar herramientas habría roto el arranque
- **Regla que queda:** Todo renombrado de carpeta exige: actualizar las rutas en las herramientas el mismo día, dejar mapa de traducción para las actas históricas (que no se reescriben) y verificar arranque+chequeo tras el cambio

## L-10 · 2026-10-29
- **Contexto:** Reorden de carpetas + rescate mezclando eras (29-oct)
- **Fallo/experiencia:** El manifiesto quedó de una era anterior al corpus (135 distintos): cada rescate parcial puede dejar artefactos de eras distintas conviviendo
- **Regla que queda:** Tras cualquier rescate o reorden: regenerar el manifiesto desde el corpus vigente y correr arranque antes de empujar; una verificación que muere por red se reintenta antes de declarar fallo

## L-11 · 2026-10-29
- **Contexto:** Reorden + entrega truncada (29-oct)
- **Fallo/experiencia:** La carpeta gemela de la entrega quedó en 2 archivos por la mordida y el espejo la propagó; el ZIP, en cambio, estaba íntegro
- **Regla que queda:** Del paquete manda el ZIP verificado: la carpeta se restaura DESDE el ZIP. Y la verificación tras push se hace por blobs del árbol remoto, sin segunda clonación que la red pueda tumbar

## L-12 · 2026-10-29
- **Contexto:** Publicación real en el compositor de Facebook (29-oct)
- **Fallo/experiencia:** El contenido verificado pegado en Facebook se veía como una pared: mapas mentales de una línea por familia y placas con todo en una sola línea nadie las puede leer en el móvil
- **Regla que queda:** Toda pieza de Facebook pasa el formato respirable (mapa en dos líneas, placa por bloque, licencia en su línea) y la reorganización se prueba con secuencia de palabras idéntica: cero falsos positivos

## L-13 · 2026-10-29
- **Contexto:** Reorganización respirable v3 (29-oct)
- **Fallo/experiencia:** La v2 dio aire entre bloques pero dejó párrafos largos y líneas eternas: en el móvil seguía siendo pared; y la dueña enseñó la captura en el compositor como prueba
- **Regla que queda:** Antes de reorganizar se investiga la plataforma (párrafos 1-3 frases, un blanco entre ideas, móvil manda) y se mide el antes/después: la respirabilidad se demuestra con cifras de párrafos y líneas, no con adjetivos

## L-14 · 2026-10-29
- **Contexto:** Fallos de la vara del catálogo en el teléfono de la dueña (29-oct)
- **Fallo/experiencia:** El envolvido respirable partió las líneas REV| de los quices (72 piezas), la salud de la forja no replicaba al navegador y la vara esperaba un muro de 15 con tokens sin reemplazar
- **Regla que queda:** Zonas REV| intocables en toda reorganización; la salud de la forja replica exacta al motor JS; ningún token __X__ llega al HTML (aserción en forja); y la vara se simula offline antes de entregar cualquier catálogo

## L-15 · 2026-10-29
- **Contexto:** Clones fallando con 128 (29-oct)
- **Fallo/experiencia:** Era /tmp al 100% por los clones acumulados del día, no la credencial: el error 128 disfrazaba un disco lleno
- **Regla que queda:** Ante un 128 de clonación, mirar disco antes que credenciales; las herramientas de guardado trabajan en el disco del workspace, no en /tmp

## L-16 · 2026-10-29
- **Contexto:** Desmeta del corpus (29-oct)
- **Fallo/experiencia:** La primera desmeta se comió la nota de 64 piezas porque el barrido de secciones no la reconocía como frontera
- **Regla que queda:** Toda limpieza por secciones declara sus zonas intocables ANTES de correr (nota 💓, líneas REV, placas) y se verifica contando lo intocable al final: si el conteo cambió, el pase no terminó

## L-17 · 2026-10-29
- **Contexto:** Corrección final del 29-oct: la vara aprobaba mientras faltaban notas y sobraban duplicados
- **Fallo/experiencia:** La reparación de quices truncó la nota 💓 de 41 piezas WA porque su zona no usa el marcador de soluciones, y la vara no comprobaba la nota en WhatsApp; el chequeo daba OK a una lupa que solo imprime medidas y prometía un L3 inexistente; el catálogo ordenaba lexicográfico (09→100) y titulaba Facebook con nombres de archivo
- **Regla que queda:** Toda reparación por zonas cuenta lo intocable (💓/REV) antes y después en AMBAS series; la vara comprueba nota, orden numérico y títulos reales; ninguna herramienta declara OK por correr: o mide y publica cifras, o es puerta y puede fallar

## L-18 · 2026-10-29
- **Contexto:** Reescritura total 29-oct-2026: el snapshot del entorno volvió a comerse parte del proyecto a mitad de la jornada, y al reconstruir la ENTREGA se crearon dos carpetas con nombre inventado (01-Canal-WhatsApp/02-Muro-Facebook) junto a las reales (01-WhatsApp-00-108/02-Facebook-00-131), duplicando el paquete hasta detectarlo por conteo de entradas.
- **Fallo/experiencia:** La mordida del snapshot es recurrente y puede repetirse en cualquier turno; y al tocar una estructura existente, crear carpetas nuevas sin mirar primero la estructura real duplica contenido en silencio.
- **Regla que queda:** Dos reglas quedan: (1) ante cualquier duda sobre el estado del proyecto, la primera respuesta es inventario + arranque.py; el orden de verdad es remoto GitHub, luego espejo, luego proyecto, y la restauración desde el remoto precede a cualquier trabajo nuevo — sin autopsia prolongada. (2) Antes de crear o renombrar cualquier carpeta o archivo dentro de una estructura que ya existe, se lista la estructura real y se escribe sobre ella; el conteo de entradas del paquete final se compara contra el contrato vigente y toda desviación se explica o se corrige en el acto.

## L-19 · 2026-10-29
- **Contexto:** Rehechura del 31-oct-2026 tras el reclamo del dueño: la reescritura del 29 había cambiado fechas y datos dentro del mismo molde ritual (nota idéntica en 259/259 piezas medida por autopsia), y la vara aprobada no lo veía porque ninguna vara contaba repetición de prosa.
- **Fallo/experiencia:** Un corpus puede tener todos los datos frescos y seguir siendo plantilla: dato fresco dentro de frase ritual = cambio semi verdadero. Y un generador nuevo sin lectura humana de su muestra esconde defectos que ninguna vara caza (release elegida por nombre de versión, capitalize() aplastando slugs, titular duplicado, NOASSERTION crudo).
- **Regla que queda:** Queda la PUERTA ANTI-PLANTILLA como pieza permanente del circuito: normaliza líneas largas y bloquea el push si una línea de prosa supera el 12% del corpus; sus exenciones (dateline, pie de procedencia, fichas, mecanismo del quiz) se declaran por escrito en su código. Antes de escalar cualquier generador: (1) demostrar que la puerta caza el molde viejo, (2) generar muestra chica y LEERLA buscando datos falsos, no solo formato, (3) corregir el generador —nunca las piezas a mano—, (4) re-medir. Frescura de datos y frescura de redacción se auditan por separado.
