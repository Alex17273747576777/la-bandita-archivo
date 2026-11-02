# 03 · Licencias y raya legal

## Lo que se cede

| Pieza | Licencia | Archivo |
|---|---|---|
| Prosa y guías | **CC BY-SA 4.0** | `LICENSE-CONTENIDO` |
| Cifras, tablas y censos | **CC BY 4.0** | `LICENSE-DATOS` |
| Código de las herramientas | **MIT** | `LICENSE` |

Se puede copiar, mezclar, publicar y vender lo que salga de esas tres, citando la fuente y su fecha.
La marca **«Alexis (La Bandita)»**, el nombre de la casa y el sello de autenticidad **no viajan con
ninguna de las tres** y quedan reservados (`NOTICE`).

## La raya que no se cruza

1. **No se reparten enlaces de descarga de obras con derechos.** Ni discografías, ni películas, ni
   libros, ni listas de canales que redistribuyen señal ajena. Se nombran los programas con su
   licencia, su fecha y los caminos legales; nada más.
2. **No se publican paquetes de origen desconocido como si fueran del autor.** Si el autor no
   publica el archivo instalable, se dice, y se explica qué implica usar el que publicó un tercero.
3. **No se enseñan atajos que comprometan a un tercero**: credenciales compartidas, listas de pago
   redistribuidas, APK de mods con enlaces directos.
4. **Datos personales:** no se publican capturas, números ni diagnósticos de nadie. Si un caso real
   ilustra la pieza, se cuenta sin identificar.

## Cómo se aplica en la práctica

- Cada pieza con software lleva **columna de licencia**; si hay discrepancia entre la ficha
  automática y el archivo del repositorio, se publican **las dos versiones** (ej.: ficha
  `NOASSERTION` / archivo `MIT`).
- Cuando una licencia no es libre al uso —por ejemplo la del teclado de FUTO— se nombra **textual**,
  no se resume como «libre».
- Cuando un programa es libre pero el contenido que lee no lo es, se separa: **el programa es libre,
  la obra tiene dueño**.

## Verificación

`tools/vara.py` G3 comprueba el método de cada licencia; G7 revisa que no se recete ningún binario;
`tools/manual_gate.py` M15 rechaza enlaces directos a APK de mods y secretos en el texto.
