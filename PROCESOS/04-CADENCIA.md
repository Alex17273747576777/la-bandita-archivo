# 04 · Cadencia y turnos

La cadencia existe para que el proyecto avance sin depender de la memoria de nadie y para que un corte
de luz o una desconexión no destruyan el trabajo.

## El turno de trabajo

1. **Abrir:** `git status` + `git log -3` (¿en qué quedó el árbol?).
2. **Comprobar estado:** `vara.py` (¿sigue todo verde antes de tocar nada?).
3. **Hacer una unidad de trabajo cerrada**: una pieza, o un lote, o una corrección. No tres cosas a
   medias.
4. **Cerrar:** compuerta → envíos → acta → sello → commit → push → CI.
5. **Dejar memoria:** la línea de estado en `docs/` (qué quedó hecho, qué quedó pendiente y por qué).

## Reglas de continuidad

- El estado se escribe **en archivos**, no en la cabeza: cualquier reanudación debe poder empezar
  leyendo `docs/PENDIENTES.md` y el último acta.
- Ante una interrupción (luz, conexión, sesión), al retomar: **no rehacer lo hecho**; verificar el
  árbol y seguir desde el último punto confirmado.
- Los datos viejos se marcan, no se ocultan: un registro con más de 180 días se declara rancio.
- Un día sin publicar no rompe nada; un día con publicación sin compuerta sí.

## Ritmo esperado

| Unidad | Tamaño | Nota |
|---|---|---|
| Pieza Facebook | 40.000–45.000 caracteres | el trabajo pesado del ciclo |
| Lote | 5 piezas | cierre con acta y sello |
| Revisión del registro | semanal | frescura y duplicados |
| Mantenimiento de documentos | mensual | este repositorio |

## Lo que nunca se hace por prisa

Sellar sin acta · publicar sin CI verde · medir una sola vez · reciclar una pieza.
