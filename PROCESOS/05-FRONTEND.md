# 05 · Publicar el frontend

El HTML es la cara del archivo: **visualiza lo publicado y lo medido**, no inventa datos.

## De dónde salen los datos

```
registry/*.json ──► registro_construir.py ──► site/datos/registro.json ──► sitio.py ──► site/
docs/envios/_envios-*.json ──► (interacciones por canal)
```

El frontend **solo lee** `site/datos/*.json`. No consulta APIs en vivo, no depende de CDN y no tiene
recursos externos: se abre y funciona sin red.

## Secuencia

1. `registro_construir.py` → reconstruye el índice del registro.
2. `sitio.py` → genera `site/` con sus datos.
3. Abrir el HTML generado y comprobar en pantalla ancha y en móvil (360 / 768 / 1440 px).
4. Consola sin errores, sin peticiones externas, sin scroll horizontal.
5. Commit + push; CI en verde.

## Las piezas que se visualizan

- **Publicaciones**: una tarjeta por pieza, con canal, fecha, longitud y enlace al `.md`.
- **Interacciones**: los envíos por canal y sus métricas cuando existan; si no existen, se muestra el
  hueco declarado («sin medición»), nunca un cero falso.
- **Registro**: fichas con estrellas, licencia, empujón y frescura.

## Reglas visuales (fijas)

Grid de 12 · peso medio · `line-height: 1.5` · pastel `#f5f7fa`/`#e0e5ec` · botones `#a8d0e6`→`#6cc29b`
· fade-in / slide-up / resplandor / inercia / respuesta táctil · nada de serif pesada, nada de grises
opacos tipo `#b0b0b0`.

## Prohibiciones

- Copiar la estética de otro proyecto o sitio de referencia.
- Cargar tipografías, scripts o imágenes desde fuera.
- Mostrar una cifra que no exista en los datos generados.
