# 05 · Publicar el frontend

El HTML es la cara del archivo: **visualiza lo publicado y lo medido**, no inventa datos.

## De dónde salen los datos

```
registry/*.json ──────────────────────► registro_construir.py ─► site/datos/registro.json
Arena-Reimagined/01-PUBLICACIONES/ ───► sitio.py ─► site/index.html · site/piezas/ · site/redes/
04-VERSIONES-MULTIIDIOMA/<red>/<idioma> ─► sitio.py ─► site/redes/index.html · site/datos/redes.json
docs/interacciones.json (opcional) ───► sitio.py ─► tarjetas de red (interacción medida)
```

El frontend **solo lee** `site/datos/*.json`. No consulta APIs en vivo, no depende de CDN y no tiene
recursos externos: se abre y funciona sin red.

## Secuencia

1. `registro_construir.py` → reconstruye el índice del registro.
2. `sitio.py` → genera `site/` con sus datos.
3. Abrir el HTML generado y comprobar en pantalla ancha y en móvil (360 / 390 / 768 / 1440 px):
   `document.documentElement.scrollWidth` no debe superar el ancho de ventana en ninguna de las cuatro.
4. Consola sin errores, sin peticiones externas, sin scroll horizontal.
5. Commit + push; CI en verde.

## La página de redes (`site/redes/index.html`)

Es la vista que responde a la pregunta del dueño: **qué se publicó en Facebook, WhatsApp y las demás
redes, y qué interacción se ha medido**. Se genera, no se escribe.

- **Publicaciones por red:** cuenta las piezas del canal y las versiones por idioma
  (`04-VERSIONES-MULTIIDIOMA/<red>/<idioma>/*.md`), con fecha de la más reciente y caracteres sumados.
- **Interacción:** se lee de `docs/interacciones.json`. Si el archivo no existe o no cubre esa red, la
  tarjeta dice **«sin medición declarada»**. Nunca se pinta un cero: un cero es un dato y una ausencia
  es una ausencia.
- **Datos publicados:** `site/datos/redes.json`, para que otra herramienta los lea sin abrir el HTML.
- **Redes sin actividad** se agrupan en una línea al pie en lugar de ocupar tarjetas vacías.

### Contrato de `docs/interacciones.json`

```json
{"generado": "2026-11-02",
 "redes": {"facebook": {"seguidores": 1200, "publicaciones": 140, "alcance": 8400,
                        "reacciones": 310, "comentarios": 44, "compartidos": 27,
                        "medido": "2026-11-02", "fuente": "panel de Facebook"}}}
```

Se escribe **a mano, una vez por corte, desde el panel de la red**. Se admite cualquier campo numérico;
todos se muestran con su fecha y su fuente. Prohibido estimar, deducir o «aproximar».

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
