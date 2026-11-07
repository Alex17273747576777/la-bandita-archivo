# _archivo-historico · qué se guarda aquí y por qué

Este directorio es la **memoria larga** del proyecto: lo que ya no se usa pero no se puede tirar.
No es una papelera: nada entra aquí sin la línea de abajo.

## Qué se archiva

| Tipo | Ejemplo | Por qué se conserva |
|---|---|---|
| Piezas retiradas | una pieza reemplazada por censo nuevo | su acta se apoya en ella |
| Actas y conformidades viejas | `CONFORMIDAD-MANUAL-2026-10-xx.md` | cadena de sellos |
| Sondas y barridos | `BARRIDO-*.md`, `REVISION-*.md` | muestran cómo se llegó a una decisión |
| Versiones anteriores de documentos | un README o un manifiesto reemplazado | trazabilidad de la norma |
| Borradores rechazados | propuestas no aprobadas (p. ej. NLnet) | evita volver a discutirlas |

## Qué **no** entra

- Piezas vivas (su sitio es `Arena-Reimagined/01-PUBLICACIONES/`).
- Fichas del registro (siguen en `registry/` aunque estén rancias: la frescura se declara, no se
  archiva).
- Credenciales, tokens o capturas con datos personales: **se destruyen**, no se archivan.
- Duplicados exactos: si dos archivos son iguales, se queda uno y se anota cuál.

## Cómo entra un archivo

1. Comprobar que no está vivo en otra ruta (`tools/duplicados.py`).
2. Mover con `git mv` (conserva historial).
3. Añadir la línea en `_archivo-historico/INDICE.md`: fecha, archivo, motivo, quién lo retiró.
4. Si era una pieza publicada: el acta va primero (ver `CIMIENTOS/06-PROTOCOLO-DE-ERRORES.md`).

## Regla

Nada se borra sin acta; nada se archiva sin índice. El historial es parte del producto.
