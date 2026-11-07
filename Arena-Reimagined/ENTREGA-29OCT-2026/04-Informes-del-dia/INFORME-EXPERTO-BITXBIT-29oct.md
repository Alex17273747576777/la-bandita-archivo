# INFORME EXPERTO EMPRESARIAL · CHEQUEO BIT POR BIT — 29-oct-2026

Verificación y corrección de fallas a nivel experto, bit por bit, individual y comparativa en ultra extremo, **adjunta a la del chequeo universal**. Matriz de pruebas ejecutada (cada prueba con su artefacto en esta carpeta):

| Nivel | Prueba | Método | Umbral | Resultado |
|---|---|---|---|---|
| 1 | Hash total del proyecto | SHA-256 de **cada archivo existente (1.449)** y comparación contra espejo y contra cada entrada del ZIP | 0 diferencias | ✅ 261/261 corpus idénticos en espejo · ZIP entrada por entrada idéntico · CRC íntegro |
| 2 | Estrés estructural | Por pieza: UTF-8 estricto, BOM, CRLF, caracteres de control, espacios duros, vallas y negritas balanceadas, newline final | 0 hallazgos | ✅ **0 hallazgos en 261 piezas** |
| 2b | Estrés de esquema | JSON del catálogo parseado 25 veces; grupos por número; campos obligatorios; cola 💓 de WhatsApp | 109 + 132 grupos sin huecos | ✅ 25/25 parses · 109 WA · 132 FB · sin huecos ni campos vacíos |
| 3 | Comparativa bajo estrés | Los **781 repos citados** y las 109 URL re-medidos en paralelo y cruzados contra la pasada anterior | 0 cambios de estado sin firmar | ✅ 0 cambios de estado · 0 archivados nuevos · deriva máx. 6★ · 1 URL (El País) pasó a 403 de bot, la misma familia ya firmada en la casa |
| 4 | Placas vs medición fresca | Cada estrella impresa en las piezas nuevas (02, 83–131) contra la medición de esta misma batería | tolerancia 3% | ✅ **ninguna placa fuera de tolerancia** |
| 5 | Estrés de integridad | 5 pasadas paralelas de hash sobre las 261 piezas contra el manifiesto | 5/5 idénticas | ✅ 5/5 |
| 6 | Árbol de Git | Clonación fresca del remoto y comparación byte por byte del árbol comprometido | 0 diferencias | ✅ registrado en el acta de este empuje |

## Correcciones aplicadas en esta batería
La batería anterior (chequeo universal) ya había terminado lo encontrado; esta pasada a nivel bit **no encontró fallas nuevas de contenido**: encontró **cero** caracteres corruptos, cero estructuras rotas, cero placas desalineadas y cero cambios de estado en el universo citado. El único movimiento del exterior en estas horas es la deriva normal de estrellas (máx. 6) y el 403 intermitente de El País a los bots — la noticia sigue viva tras el navegador, como la casa ya firma en esos casos.

## Anexos completos (adjuntos)
En `ENTREGA-29OCT-2026/05-Anexo-BitXBit/`: el **manifiesto bit por bit de los 1.449 archivos** del proyecto (`MANIFIESTO-BITXBIT-TOTAL.tsv`), la medición universal de los 781 repos y 109 URL, la comparativa entre pasadas y los resultados de cada nivel. Cualquiera puede re-ejecutar la verificación sin fiarse de este texto: `_herramientas/verificar-suelo.py` deja el corpus en 261/261 o dice exactamente qué byte cambió.

## Conclusión experta
Integridad de datos: **íntegra** (hash total). Integridad de contenido: **íntegra** (estructura y caracteres). Integridad factual: **vigente** (comparativa sin cambios de estado; placas dentro de tolerancia con su fecha). Disponibilidad: **triple** (proyecto, espejo y GitHub privado byte por byte). Lo único que el tiempo moverá son las estrellas, y cada placa lleva impresa la fecha en que era verdad.
