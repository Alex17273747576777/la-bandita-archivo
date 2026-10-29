# INFORME DE MICROPENDIENTES — 29-oct-2026

«Esto no acaba hasta terminar hasta el mínimo pendiente.» El mínimo pendiente era este: al cerrar las licencias del censo, las piezas que habían impreso «licencia sin resolver» a mitad de camino quedaron contando una foto vieja. Se cazaron todas.

## Qué se corrigió
- **50 placas en 37 piezas** decían «licencia sin resolver» por repo. Cada una se comparó contra la verdad de cierre (SPDX de GitHub, texto del LICENSE y endpoint `/license` de la API, medidos hoy) y quedó con su dato real: Apache-2.0 donde lo es (`mihon`, `Kototoro`, `Aniyomi`, `Animiru`…), o la verdad más fina donde no hay licencia que resolver: **«sin archivo LICENSE en su repo (verificado por API 29-oct-2026)»** (`Keiyoushi/extensions`, `phhusson/treble_experimentations`, el índice de módulos Xposed, `devcaspian-hash/bokumi-app`…).
- **La línea global de la WhatsApp 00** («45 repos siguen sin licencia resuelta») quedó actualizada a la foto real de cierre: ninguna licencia «sin resolver» sin su motivo.
- **La fe de erratas de la Facebook 112** se completó con el resultado final de la caza (incluido `hrydgard/ppsspp` GPL-2.0 por texto), tras reparar el texto que la corrección automática había rozado.
- Las cifras de licencias en **la guía de publicación y el informe de cierre** quedaron alineadas con el resultado real (0 sin resolver; 62 sin archivo LICENSE; 17 no verificables).

## Verificación tras corregir
- **Lupa v6: EXIT=0 en WhatsApp y en Facebook.**
- Catálogo re-horneado tras las correcciones; textos embebidos idénticos a disco.
- `verificar-suelo.py`: **261 piezas contra el manifiesto regenerado, 0 problemas.**
- Espejo reconstruido byte por byte; push con clonación fresca comparada (0 diferencias) — el acta lo registra.

## Estado de veracidad al cierre de todo
- Ninguna pieza afirma hoy una licencia «sin resolver» que la jornada ya resolvió.
- Ninguna licencia fue inventada: donde no hay archivo, la pieza dice que no hay archivo — que también es un dato, y de los importantes antes de construir encima.
