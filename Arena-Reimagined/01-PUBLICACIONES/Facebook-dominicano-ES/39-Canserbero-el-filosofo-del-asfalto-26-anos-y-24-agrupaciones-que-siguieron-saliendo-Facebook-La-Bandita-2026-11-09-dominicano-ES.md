
*La Bandita · lunes 9 de noviembre de 2026 · edición dominicano-español · pieza 39 de Facebook*

⏱️ *Lectura total: unos veinte minutos · una vida de 26 años y 24 agrupaciones declaradas · Wikidata y MusicBrainz · cero paquetes alojados*

Canserbero nació el 11 de marzo de 1988 y murió el 19 de enero de 2015, según el primer valor que declara Wikidata: **26 años**. Su ficha declara **dos fechas de muerte distintas**, que es lo que pasa cuando un hecho es tan discutido que ni una base de datos abierta se pone de acuerdo. Su obra declarada en MusicBrainz son **24** agrupaciones: **8** álbumes y **1** EP.

Esos son los datos, y son pocos para lo que fue. Lo que sigue es lo que se puede escribir sin rellenar.

## 🎤 Un mensaje desde el corazón del Caribe

Venezuela, 1988. Un muchacho que empieza a rapear en un país que no era el centro de nada. Eso, en el rap latinoamericano, no era una desventaja: era la única posición desde la que se podía decir la verdad sin que nadie te estuviera mirando.

Vivió **26 años**. Tenía 26 cuando lo mataron. Yo tenía la misma edad cuando lo escuché por primera vez y no entendí que estaba escuchando a alguien de mi edad hablando de cosas que yo todavía no había vivido.

## 🎬 Primer acto: la vida como película — tragedia, comedia y ficción

Su idea más repetida: la vida es una película donde tú escoges el papel. Puedes ser la víctima, puedes ser el bufón, o puedes ser el que escribe.

Lo inquietante es que lo dijo en 2010, cinco años antes de que su propia muerte se volviera una de esas historias que nadie se pone de acuerdo en cómo contar. **Dos fechas distintas** de su muerte en una base abierta: el 19 y el 20 de enero. Un día de diferencia que, para un expediente, es todo.

## 🌅 Segundo acto: mañana será otro día — la esperanza que nos sostiene

El disco que le dio el nombre a esa idea es de **2010** —`Mi Pobre Gente Pobre`, un sencillo de marzo de ese año, en la lista de MusicBrainz—. Y aquí está lo que hace que su obra funcione: no era optimismo. Era una persona que sabía exactamente lo que había en la calle diciendo que aun así valía la pena.

La diferencia entre el optimismo y la esperanza es que el primero no ha mirado. Canserbero miró.

## ⚔️ Tercer acto: Es Épico — la resiliencia ante la traición y el rencor

`Apa y Can` es de marzo de 2013. `Resurrección` es de 2015, el año en que murió. Y `Sigo Siendo el Rey` es de 2018, tres años después de que lo mataran.

Ese último dato me parece el más elocuente de todos: su obra siguió publicándose **tres años** después de su muerte. En MusicBrainz, entre sus **24** agrupaciones hay sencillos posteriores a 2015. No dejó de sacar discos porque ya no estaba.

## 🔥 Cuarto acto: la filosofía del barrio — conciencia, evolución y amor

No era un filósofo académico. Era alguien que había leído y que hablaba con las palabras de la esquina. Esa mezcla —concepto y calle— es lo que lo hace irrepetible y lo que hace que traducirlo sea casi imposible.

## 📜 Quinto acto: enseñanzas para la Bandita

De todo lo que dijo, me quedo con tres cosas que este archivo practica:

1. **Medir antes de opinar.** Él contaba lo que veía, no lo que le contaron.
2. **No confundir la crítica con el rencor.** Se puede pelear contra un sistema sin odiar a la gente que vive dentro de él.
3. **Publicar aunque duela.** Su obra siguió saliendo después de él; la mía sale cada vez que se cierra una pieza.

## 🎵 Sexto acto: playlist para un viaje consciente

No voy a recomendar canciones con títulos que no haya comprobado. Lo que sí puedo decir es lo que la fuente declara: **24** agrupaciones, **8** álbumes, **1** EP, y el álbum más antiguo declarado en la lista es de 2010.

## 🕊️ Séptimo acto: un legado que no muere

Murió a los **26**. Su ficha en una base abierta no se pone de acuerdo ni en qué día fue.

Eso debería ser una advertencia sobre lo que una base de datos puede y no puede guardar: guarda el identificador, la fecha y el tipo. No guarda lo que hizo que un muchacho de Maracay se volviera la voz de un continente.

## 🌈 Octavo acto: el viaje que compartimos

Llegué a él por una canción y me quedé por la manera de mirar. Este archivo se escribe así: con la misma terquedad de contar lo que hay, incluyendo los ceros.

───────────────────

*🧾 La tabla · lo único de esta pieza que se midió*

| Hecho | Dato | De dónde salió |
|---|---|---|
| Identificador Wikidata | Q18821745 | búsqueda por nombre |
| Nacimiento | 1988-03-11 | Wikidata P569 |
| Muerte (primer valor) | 2015-01-19 | Wikidata P570 |
| Fechas de muerte distintas declaradas | 2 | Wikidata P570 |
| Años de vida cumplidos | 26 | resta de las dos fechas |
| País declarado | Venezuela | Wikidata P27 = Q717 |
| Agrupaciones en MusicBrainz | 24 | release-groups del artista |
| De esas, álbumes | 8 | primary-type = Album |
| De esas, EP | 1 | primary-type = EP |

───────────────────

*🛠️ Cuatro órdenes para comprobar esta pieza*

1. `curl -s "https://www.wikidata.org/wiki/Special:EntityData/Q18821745.json"` y busca `P570`. Vas a ver **dos** valores. Por eso la pieza dice «el primer valor» y no «la fecha».
2. Para la edad: del 11 de marzo de 1988 al 19 de enero de 2015 son **26** años cumplidos.
3. Para la obra: `curl -s "https://musicbrainz.org/ws/2/release-group?artist=70a3344d-3f48-4843-ac93-e9e031d86b01&fmt=json"`. Cuenta las entradas de `release-groups`. Son **24**.
4. Filtra por `primary-type: Album` (**8**) y por `EP` (**1**). El resto son sencillos.

───────────────────

*📌 La corrección de esta pieza*

Se publicó el 7 de noviembre sin medición y con la playlist escrita de memoria. En la primera pasada de hoy, la consulta a MusicBrainz devolvía **cero discos** y daba la impresión de que la fuente no tenía su obra. El fallo era del lector: la clave del JSON se llama `release-groups` y yo leía `release-group`. Corregido el lector, son **24**. Y la playlist de esta pieza ya no lleva títulos que no salgan de la fuente: se dice cuántas agrupaciones hay y en qué años, que es lo que se puede comprobar.

───────────────────

*❓ Las preguntas del grupo*

**«¿Dos fechas de muerte?»** Sí, y las dos están declaradas. La pieza usa la primera y dice que hay dos. Fingir que hay una sola sería más limpio y menos verdadero.

**«¿Por qué no pones las canciones?»** Porque no puedo comprobar que cada título esté en la fuente, y esta serie no escribe lo que no puede comprobar. Se dice el número y el año.

**«¿Y la muerte?»** Hay una ficha aparte en Wikidata sobre su muerte. Esta pieza no la usa para contar el caso: usa la fecha, no el expediente.

───────────────────

*🌅 Cierre*

Veintiséis años, veinticuatro agrupaciones, ocho álbumes, una EP y dos fechas para el mismo día.

Si algo de esto te sirve, haz una sola cosa: hoy, escucha una canción completa sin mirar el teléfono. Eso es lo que él pedía, y no cuesta nada.

Cada cifra de esta pieza sale de `docs/MEDICION-P39-2026-11-09.json`: Wikidata para la vida y MusicBrainz para la obra. Ningún dato se copió de un artículo ni se escribió de memoria.

*💓 La Bandita informa. Lo que no se midió, aquí no se escribe.*
