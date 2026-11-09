# LECCIONES · los fallos que hicieron estas habilidades

*Cada lección tiene tres partes: **síntoma** (lo que se vio), **causa** (lo que había de verdad) y
**regla** (lo que se hace distinto). Una lección sin regla es una anécdota.*

*Se añade una con `corregir-a-la-vista`. La numeración no se recicla.*

---

## Bloque 1 · del archivo viejo (HABILIDADES/bitacora-lecciones.md)

**L-01 · La ficha automática da la fecha de versión vacía.**
Síntoma: se publicaba «actualizado hoy» con el empujón. Causa: el campo de versión llega vacío casi
siempre y se confundió empujón con entrega. Regla: **empujón ≠ paquete**, se publican los dos.

**L-02 · Contar cuotas como muertes.**
Síntoma: repositorios «muertos» que al día siguiente estaban vivos. Causa: 403 y 429 son cuota, no
muerte. Regla: **404 muerte · 451 bloqueo · 403/429 cuota**.

**L-03 · Licencias inventadas.**
Síntoma: «probablemente MIT». Causa: se rellenaba el hueco en vez de resolverlo. Regla: **orden SPDX →
endpoint → texto del LICENSE → ausencia firmada**.

**L-04 · La reorganización disfrazada de formato.**
Síntoma: una pieza «reorganizada» con palabras cambiadas. Causa: se editó y se llamó maquetación.
Regla: **la secuencia de palabras debe ser idéntica antes y después**; lo que cambie se declara.

**L-05 · Push dado por bueno sin verificar.**
Síntoma: «subido» y el remoto no lo tenía. Regla: **no hay push bueno sin su verificación**, y
`git rev-list --count origin/main..HEAD` tiene que dar 0.

**L-06 · El commit con `$` dentro.**
Síntoma: mensajes de commit corruptos. Causa: heredoc expande `$`. Regla: **`git commit -F archivo`**.

**L-07 · La mordida del arranque.**
Síntoma: se trabajó sobre un árbol que no era el esperado. Regla: **inventario → hash → restaurar →
recién trabajar**.

---

## Bloque 2 · del archivo de la bandita (9 de noviembre de 2026)

**L-08 · El detector se equivocó siete veces antes que la pieza.**
Síntoma: cifras «sin respaldo» que estaban bien. Causa, una por una:
1. años contados como cifras;
2. números en palabras no reconocidos;
3. la ventana de atribución cruzaba al repositorio vecino;
4. coincidencia por subcadena: `1.665` dentro de `11.665`;
5. la guía 05 cotejada contra su solo agregado en vez de contra la unión;
6. `3.116` fuera del universo de constantes;
7. **un UUID leído como cifra**: `70a3344d-3f48-4843-…` aportaba «4843».
Regla: **se arregla el detector, nunca se baja el listón.** Y antes de publicar un cero: **comprobar
si el cero es del dato o del lector**.

**L-09 · Un archivo de medición que solo existía en la cita.**
Síntoma: cuatro piezas citaban JSON que nunca se habían creado. Causa: se escribió la cita antes que la
medición. Regla: **no se cita un archivo que no existe**; si falta, se mide y la corrección se publica
**dentro** de la pieza.

**L-10 · Veinte repositorios mudados tomados por fantasma.**
Síntoma: 16 falsos positivos diciendo que a FMHY le faltaban repositorios. Causa: se comparó con el
nombre de hoy contra una lista con el nombre de ayer. Regla: **antes de decir que falta, comprobar con
el nombre viejo**; la API da el número del repositorio y por el número se llega al nombre actual.

**L-11 · Dos QID supuestos.**
Síntoma: dos películas «sin fecha». Causa: se escribieron de memoria y eran un videojuego y una banda
sonora. Regla: **jamás suponer un identificador**; se busca, se comprueba qué dice de sí mismo y solo
entonces se acepta.

**L-12 · La clave del JSON no era la que se leía.**
Síntoma: MusicBrainz devolvía **0 discos** para dos artistas con obra. Causa: se leía `release-group`
donde la fuente publica `release-groups`. Regla: **una fuente que parece vacía es la mentira más fácil
de creerse**; comprobar el lector antes de publicar el cero.

**L-13 · El archivo trampa.**
Síntoma: `index.min.json` daba **2** extensiones donde hay **1.554**. Regla: **medir el archivo bueno y
nombrar el malo** dentro de la pieza.

**L-14 · El nombre del archivo sin título.**
Síntoma: piezas generadas como `NN--Facebook-…`. Causa: el alma no llevaba `TITULO:`. Regla: **el
encabezado es parte del contrato del alma**.

**L-15 · La cita añadida al alma y no renderizada.**
Síntoma: el archivo publicado no tenía la cita que sí estaba en el alma. Causa: se editó el alma y no
se volvió a correr el motor. Regla: **editar el alma no es publicar**; hay que renderizar.

**L-16 · El registro escrito a mano.**
Síntoma: 18 piezas fuera de banda sin que se supiera por qué. Causa: `docs/bandas.json` se editaba a
mano y nadie lo cuadraba. Regla: **el registro se rehace leyendo los archivos, no al revés**.

**L-17 · La comparación con el prefijo que faltaba.**
Síntoma: 33 piezas «sin citar su JSON» que sí lo citaban. Causa: el chequeo buscaba
`docs/MEDICION-…` en un texto que lo tenía, pero se comparaba contra una cadena sin `docs/`. Regla:
**cuando el detector acusa a 33 de 40, el sospechoso es el detector**.

---

## Bloque 3 · de la app

**L-18 · 519 errores de compilación por nombres de memoria.**
Síntoma: la compilación no cerraba. Causa: nombres de paquete y dependencia copiados de memoria.
Regla: **prohibido inventar nombres de paquete**; si no está en el manifiesto, no existe.

**L-19 · El emulador sin aceleración.**
Síntoma: se intentó una y otra vez. Causa: no hay `/dev/kvm` y el hardware no lo permite. Regla: **se
dice y se continúa**; la RAM no es la objeción, la virtualización lo es.

**L-20 · Un `assembleDebug` presentado como «la app funciona».**
Regla: **compila ≠ arranca ≠ funciona**; cada cosa se mide donde se mide y se dice dónde.

---

## Bloque 4 · del propio sistema

**L-21 · Dos sistemas de habilidades incompletos.**
Síntoma: `SKILLS/` con 7 y `HABILIDADES/` con 7, capacidades distintas, ninguna completa. Causa: se
construyeron en momentos distintos y nadie los miró juntos. Regla: **fusionar por capacidades, no por
archivos**, y no borrar el viejo sin reemplazo declarado.

**L-22 · El catálogo clavado en el código.**
Síntoma: el framework listaba 6 habilidades con versión 2.0.0 mientras el frontmatter decía 1.0.1.
Causa: la lista vivía en el `.py` y el documento en el disco. Regla: **una sola fuente de verdad**, y
es el disco.

**L-23 · El turno que se murió por gastar llamadas en lo pequeño.**
Síntoma: «tool-call limit reached» a mitad de un trabajo que iba bien. Causa: cuarenta llamadas para
cosas que cabían en una. Regla: **un bloque de trabajo = un script = una llamada**; los comandos
sueltos son para preguntar, no para construir.

---

*Última: L-23, 9 de noviembre de 2026.*
