# CÓMO SE MANDA · reglas y mapa de los envíos

Esto no es un catálogo de archivos: es la decisión de cómo sale el archivo a la calle. Lo escribo
porque el dueño está enfermo y no puede estar recordando reglas cada vez que abra WhatsApp.

## La regla que manda

**Una pieza por envío. Nunca dos.** WhatsApp no es un feed: es una conversación. Dos piezas juntas se
leen como spam; una sola, con su 💓, se lee como el mensaje de un vecino que sabe.

Y una segunda, que aprendí el 31 de octubre a golpes: **un texto viejo no puede presentarse como de
hoy**. Por eso cada envío lleva su fecha a la vista, y lo que decía «hoy» cuando se escribió va
avisado.

## Dónde está cada cosa

| Carpeta | Qué es |
|---|---|
| `docs/envios/whatsapp/` | **112 envíos** de las guías largas (una por pieza, salvo la 01) |
| `docs/envios/facebook/` | **147 envíos** de las piezas cortas |
| `docs/envios/01-2026-10-31/` | el paquete de la pieza 01, hecho a mano antes de que existiera la herramienta: portada, 20 mensajes, plan y evidencia en JSON |
| `docs/envios/_medicion-whatsapp.json` | lo que devolvió la API hoy para cada repo y cada enlace |
| `docs/envios/_medicion-facebook.json` | lo mismo para las piezas cortas |

Cada archivo de envío trae: **portada**, **cuerpo partido en mensajes** y **cierre medido hoy**. La
pieza original **no se toca**; su sha256 va en la cabecera, así que si alguien edita la pieza, el
envío queda marcado como desactualizado y hay que regenerarlo.

## Lo que se midió para esto (31 de octubre de 2026)

| | WhatsApp | Facebook |
|---|---|---|
| Piezas | 113 | 147 |
| Envíos generados | 112 (la 01 tiene el suyo) | 147 |
| Mensajes totales | 1.056 | 647 |
| Repositorios medidos | 255 · **253 vivos, 2 muertos** | 663 · **650 vivos, 9 muertos** |
| Enlaces revisados | 456 · **445 responden** | 1.046 · **1.002 responden** |
| Mensaje más largo | 3.835 caracteres | 3.922 caracteres |

Ningún mensaje pasa de 3.960 caracteres. WhatsApp corta en 65.536, pero el tope de la casa es 4.000 y
el corte de WhatsApp **se come la firma**: partir a tiempo no es estética, es que el 💓 llegue.

### Los enlaces que no responden, contados con honestidad

Un `403` **no es un enlace muerto**: es un servidor que no deja entrar a un robot. Un `000` no es un
sitio caído: es un sitio que no contestó en 25 segundos. En los envíos se dice así, con el código
delante, y se distingue de los `404`, que sí son ausencias. Los dos únicos repositorios muertos de
WhatsApp (`droidify/client` y `neo-launcher/neo-backup`) se nombran **para esquivarlos**, no se
recomiendan.

### Lo que encontré y no oculto

Nueve piezas (12 a 20 de WhatsApp) **dejan un bloque de código sin cerrar**. El envío lo cierra al
final para que se pueda leer, y lo avisa en la cabecera; **la pieza original no se modificó**. Si
quieres que se corrija en el archivo, es una decisión tuya y son nueve líneas.

## Por dónde empezar

Por fecha, no por número. De las 260 piezas, **222 están fechadas el 29 de octubre**, 33 el 15 de
octubre, una el 31 y cuatro más viejas (entre el 15 y el 22 de septiembre). Lo más fresco primero:

1. **Pieza 109** (31-oct): OmniShizuku y el taller sin root. Es la única de hoy.
2. **Las del 29-oct**: el bloque grande. Ahí entra la 01 y casi todo lo demás.
3. **Las del 15-oct**: guías de la primera hornada; siguen valiendo, pero llevan 16 días.
4. **Las cuatro viejas**: se mandan solo si te las piden, y con el aviso de edad por delante.

## El plan corto (el que yo haría)

**Tres mensajes**: portada + primer mensaje del cuerpo + segundo. La portada ya lleva el enlace a la
guía entera en el archivo. Quien quiera los 50 minutos los tiene; quien no, se queda con lo que cabe
en un vistazo. Son unos 8 minutos de lectura y no deja la publicación a medias.

**Si el cuerpo tiene menos de tres mensajes** (la mayoría de las de Facebook), mándalo entero: dos o
tres mensajes es una publicación completa, no un fragmento.

## El plan largo

El envío entero, en tandas de tres o cuatro mensajes, una tanda por sesión. Si lo haces así, **el
último día hay que regenerar**: el cierre dice «medido hoy» y a la semana tendrá edad. Se regenera
con un comando (abajo) y la vara lo vigila sola.

## Cómo se regenera (cuando haga falta)

```bash
LBT=<token> python3 tools/envio.py --medir       # vuelve a medir repos y enlaces (3 min)
python3 tools/envio.py --generar                 # reescribe los 259 envíos
python3 tools/envio.py --verificar               # comprueba que quepan y que el cuerpo esté entero
python3 tools/envio.py --generar --pieza 47 --canal whatsapp   # solo una
```

`--verificar` no es decorativo: comprueba que ningún mensaje pase del tope, que **toda línea del
cuerpo** haya llegado al envío, que el último mensaje lleve firma, que no haya caracteres de ancho
cero y que el archivo sea **exactamente** lo que el programa produce hoy. Si alguien edita un envío a
mano, canta. Eso es la compuerta **G9** de `tools/vara.py`, y corre en cada push.

## Lo que esto no hace

- **No decide qué se recomienda.** Esa firma es del dueño y de nadie más. La herramienta mide, ordena y
  avisa; no elige.
- **No reescribe las piezas.** El cuerpo va íntegro; lo nuevo es la portada y el cierre.
- **No promete que veinte mensajes se lean.** Promete que ninguno miente y que la fecha de cada dato
  está a la vista.
