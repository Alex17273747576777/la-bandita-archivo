# AYUDA Y SOPORTE

*A dónde ir según lo que te pasa. Cinco puertas, cada una con su tiempo de respuesta y su límite.*

**TL;DR —** primero el `doctor`; después la guía; después el parte de avería en las incidencias. Para seguridad, en privado. Para «¿me recomendás una app?», el índice de la guía. **No hay soporte por mensaje directo**: lo que se responde en privado no le sirve al siguiente.

---

| Lo que te pasa | A dónde vas | Qué ponés | Respuesta |
|---|---|---|---|
| No sé por dónde empezar | `make doctor` y luego este README | nada | inmediata |
| Quiero una app para una tarea | [`guia-maestra/`](guia-maestra/README.md) y `docs/INDICE.md` | la tarea, no la app | inmediata |
| Un comando del `Makefile` falla | Incidencia con plantilla «Fallo» | el parte de seis líneas | 5 días |
| Una ficha tiene un dato viejo o mal | Plantilla «Dato incorrecto» | la medición nueva y su fecha | 5 días |
| Un enlace lleva a un paquete modificado | Plantilla «Enlace peligroso» o `SEGURIDAD` | la URL exacta y la fecha | 48 h |
| Un fallo de seguridad | [SECURITY.md](SECURITY.md) | privado, con ruta y reproducción | 48 h |
| Quiero aportar una pieza o una herramienta | [CONTRIBUTING.md](CONTRIBUTING.md) | el cambio y su `CHANGELOG` | según revisión |

## 1 · El parte de avería, en seis líneas

Es el mismo que la guía enseña en el capítulo 11 y sirve para todo lo que se rompe en un aparato:

```
1. Programa y versión:      Termux 0.118.3
2. Aparato y sistema:       Moto G31 · Android 12 · sin root
3. Qué hice:                copié la pieza en ~/bandita y corrí make verificar
4. Qué esperaba:            la frase "fallos: NINGUNO"
5. Qué pasó:                "permiso denegado" al escribir en docs/
6. Registro recortado:      las últimas 20 líneas, sin datos personales
```

Con esas seis líneas se puede reproducir casi cualquier cosa. Sin ellas, cualquier ayuda es una adivinanza.

## 2 · Lo que esta casa no hace

- **No resuelve dudas de configuración de un teléfono ajeno** por mensaje directo: eso es una guía, y está escrita.
- **No ayuda a saltar un bloqueo de cuenta, de operador o de pago.** Ni con método alternativo ni con rodeo.
- **No garantiza que una app siga existiendo.** Se remide y se marca lo vencido; no se vigila en tiempo real.
- **No atiende campañas de mercadeo.** No hay tarifa, ni patrocinio, ni canje de visibilidad.

## 3 · Si encontrás la respuesta vos mismo

Contalo. La mejor contribución a este repositorio no es un enlace nuevo: es la frase exacta que te habría ahorrado dos horas, escrita para el que viene detrás.

*La Bandita informa a partir de fuentes fechadas.*
