# Protocolo de corrección profunda (orden del dueño, 1-nov-2026)

Regla nueva, y manda sobre las anteriores: **no se admiten parches menores**. Cada fallo
que aparezca se trabaja en cinco tiempos y, cuando el fallo es de método, se reinicia el
reloj y se vuelve a pasar la lista de Facebook desde la 01 con la fecha viva del día.

## Los cinco tiempos

1. **Análisis de detalle.** No «falla el gate»: qué regla, qué línea, por qué existe la
   regla, qué quería evitar, y si el fallo es de la pieza o de la regla.
2. **Ejemplares del mismo fallo.** Dónde más aparece lo mismo: en esta pieza, en las
   hermanas, en el archivo viejo, en las herramientas. Un fallo que se arregla en un solo
   sitio vuelve por otro.
3. **Variables.** Qué cambia entre un caso y otro: canal, numeración, longitud, emoji,
   versión de la herramienta, hora de medición.
4. **Tres soluciones distintas, ninguna genérica.** Cada fallo se resuelve por tres vías y
   se aplica la que aguanta la próxima pasada; las otras dos quedan escritas por si la
   primera se rompe.
5. **Reinicio.** Se re-mide la fecha y la hora en vivo, se vuelve a leer cada recurso tres
   veces con métodos distintos y se reescribe desde la 01 hasta que todas queden parejas.

## Los fallos ya catalogados y sus tres salidas

| Fallo | Ejemplares | Variables | Salidas no genéricas |
|---|---|---|---|
| Párrafo compartido entre piezas hermanas (M23) | línea de licencia repetida entre 08 y 09; párrafo «No dicen cuánto va a durar» entre 07 y 08 | canal, redacción de cierre, orden de los bloques finales | (a) redactar la línea de licencia distinta en cada pieza; (b) cambiar el orden de los bloques finales para que la coincidencia desaparezca por estructura; (c) mover el dato compartido a una nota al pie propia de la pieza |
| Recuento de FAQ (M06) | preguntas en cursiva que no eran FAQ; respuestas largas que se leían como párrafo | formato de la pregunta, número | (a) renombrar encabezados que no son FAQ; (b) pasar a pregunta en negrita con «¿…?» solo en la sección; (c) bajar a 11 y dejar la doceava como nota |
| Meta-comentarios (M12) | «voy a contar», «en esta sección» | exenciones de método | (a) reescribir en presente de medición; (b) sustituir por el dato medido; (c) mover el método al bloque de método, que está exento |
| Sello roto (G5) | cualquier edición posterior al último `atestar.py` | orden de la tubería | (a) sellar al final; (b) sellar y acta en la misma corrida; (c) comprobar con `vara.py` antes de cada commit |
| Repositorio ilegible (422 / 451 / sin README) | Phocid, parches de ReVanced, dos kernels | nombre del README, rama, código HTTP | (a) ampliar nombres y ramas; (b) preguntar por el endpoint del repositorio en vez del buscador; (c) excluir la ficha y anotar el hueco — nunca rellenar de memoria |
| Datos viejos presentados como frescos | TMO con material de hace 4-5 meses | fecha de corte, dominios | (a) re-medir el día con hora; (b) censar todos los espejos vivos, no el que se recordaba; (c) publicar la tabla de tres lecturas por sitio (`docs/TMO-2026-11-01.md`) |

## Tubería obligatoria de cada pieza

- Tres lecturas por recurso, **en orden rotado** entre recursos (`tools/tres_lecturas.py`),
  ahora con la llave local: sin esperas y con cupo de 5.000 peticiones por hora.
- `envio.py --generar` → `--verificar` (0 fallos) → `manual_gate.py --verificar` (VERDE).
- `vara.py` (G0–G12) sin fallos → `acta_conformidad.py` → `atestar.py` → commit → push con
  la llave clásica A → CI en verde → `cosign verify-blob` → copia a `/home/user/PIEZAS-2026-11-01/`.

## Dónde viven las llaves

`/home/user/.boveda/tokens.env` (permisos 600, fuera del repositorio y en `.gitignore`) y
una copia en `/tmp/.lbt` para el empuje por `http.extraHeader`. Nunca se imprimen, nunca se
commitean, nunca se citan en una pieza.
