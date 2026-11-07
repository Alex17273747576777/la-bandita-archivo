# Acta · pieza 12 corregida de raíz (4-nov-2026, 21:37–22:05 AST)

**Motivo.** Facebook retiró la pieza 12 publicada a las 21:02 con el aviso *«No puedes compartir este
enlace — github.com/jackett/jackett — infringe nuestras Normas comunitarias»*. Captura en
`uploads/Screenshot_20261104_212624_com_facebook_katana_FbMainTabActivity.jpg`. Entra como **E40** y
deja la habilidad **H20**.

**Lo que se hizo, en orden.**

1. **Fecha en vivo antes de empezar:** `tools/fecha_viva.py --inicio` → miércoles 4-nov-2026, 21:36 AST.
2. **Remedición completa del lote 12b** (59 direcciones, nunca copiadas de la versión retirada):
   `tools/remedir.py --escribir docs/MEDICION-12b-noche-2026-11-04.json` → medido a las **21:37**,
   59 vivos, 0 archivados, 485.382 ★, 49.263.819 descargas, 44 con empujón ≤7 d, 28 hoy,
   10 nacidos ≤90 d, 5 sin licencia legible.
3. **Escrutinio rehecho** para las ocho fichas nuevas (`tools/escrutinio.py --repos …`): RepoStore 47,
   castor 77, Atrium 65, grimmory 58, simpleui 54, OwnTV 65, chimahon 62, MediaLyze 64.
4. **Cero menciones de Jackett** en el texto final (`grep -i jackett` = 0), también fuera de la tabla
   de reemplazos y del bloque de enlaces.
5. **Ocho estrenos de 2026, uno por sección:** RepoStore (base), Castor (cine), Atrium (torrentes),
   grimmory + SimpleUI (libros), OwnTV (IPTV), Chimahon (manga), MediaLyze (sincronizar).
6. **Torrentes sin enlace.** La sección entera se queda con nombre + qué hace + cómo se comprueba; las
   direcciones van solo en la versión de WhatsApp (H20).
7. **Compuertas:** `manual_gate` **VERDE** (44.979 car., banda 40.000–45.000), `novedad_gate`
   **VERDE**, `--solape` contra la pieza 11 → **0,0 %** de párrafos copiados.
8. **Envíos:** `envio.py --medir` → `--generar --canal ambos` → `--verificar` → **0 fallos**
   (5 envíos de WhatsApp y 12 de Facebook).

**Archivo.** `12-El-kit-de-reemplazo-cincuenta-y-nueve-recursos-medidos-hoy-…-Facebook-La-Bandita-2026-11-04-dominicano-ES.md`
(sustituye al de cincuenta y dos recursos, retirado por la plataforma). `docs/bandas.json` re-anotado.

**Lo que no se toca.** La APK bloqueada del meme sigue sin enlazarse, sin recomendarse y sin medirse;
el marco del meme sigue fuera de la pieza: no se defiende a ninguno de los dos «piratas», se ofrecen
recursos nuevos y verificables.
