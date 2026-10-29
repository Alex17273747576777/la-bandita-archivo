# INFORME DEL CHEQUEO UNIVERSAL EXTREMO — 29-oct-2026

El dueño exigió estar 110% seguro, elemento por elemento y byte por byte, y terminar en el acto lo que no estuviera en orden. Esto se midió TODO, no una muestra:

## Universo medido al completo
- **781 repos distintos citados en las 261 piezas** (placas, cuerpos y notas), medidos uno a uno por la API oficial: **763 vivos**, 13 en 404, 4 en 451 y 1 marcador de plantilla. Los 17 caídos/bloqueados son exactamente los que las piezas ya firmaban; no apareció ni un muerto nuevo sin confesar.
- **109 URL no-GitHub** medidas: 86 vivas, 20 tras la puerta del navegador (403 de bot, verificadas), y **2 muertas reales** (`burnsomni.net/manuals/pagan` y la página de descarga de LibreOffice) que dos piezas viejas citaban en el cuerpo: ambas llevan ya su **fe de cierre** firmada en la pieza para que nadie prometa lo que la web ya no sirve.
- **781/781 repos y 109/109 URL: ningún elemento del corpus quedó sin medir.**

## Byte por byte, tres copias y el paquete
- Proyecto ↔ espejo: **0 diferencias** en las 261 piezas y el catálogo.
- ENTREGA ↔ proyecto: **0 diferencias**.
- ZIP ↔ carpeta de entrega: íntegro, 273 entradas, **0 bytes distintos**, mismos nombres.
- Catálogo: WA 111 · FB 147 embebidos, **0 textos distintos a disco**, 0 piezas sin título. (Los ids repetidos del muro son las variantes históricas del mismo número: diseño, no error.)
- Encoding: ni un solo carácter corrupto en 261 archivos tras extirpar el de WhatsApp 10.

## Lo que el chequeo encontró y se terminó en el acto
1. **15 líneas residuales** con «licencia sin resolver» en piezas canónicas (la primera fe de cierre solo había cubierto las piezas nuevas): corregidas con contraste doble — endpoint de licencias y lectura directa del LICENSE. `seedvault-app/seedvault` resultó **Apache-2.0** por su texto (el endpoint no lo veía; la lectura sí), y 8 repos quedaron como «sin archivo LICENSE en la raíz de su repo (verificado por API 29-oct-2026)».
2. Las **2 URL muertas** con su fe de cierre firmada.
3. Tras cada arreglo: **lupa v6 EXIT=0 en las dos series**, catálogo re-horneado, manifiesto SHA-256 regenerado y `verificar-suelo` en **261/261 sin problemas**.

## 110%: qué significa aquí
Significa que la comprobación no fue por muestreo: cada repo citado, cada URL, cada archivo, cada copia y cada byte del paquete pasaron por la medición, y lo que falló se corrigió y se volvió a medir hasta quedar en cero. La prueba final no es este texto: es el manifiesto firmado, el verificar-suelo en cero y la clonación fresca de GitHub comparada byte por byte tras el empuje (registrada en el acta).

Artefactos: `02-ARCHIVO/_rearm-29oct/chequeo-universal-29oct/` (universo de citas, medición universal, residuos y este informe).
