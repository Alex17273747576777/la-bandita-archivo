# SEGURIDAD

*Qué se considera un fallo de seguridad en este repositorio, cómo se reporta y qué se promete a cambio.*

**TL;DR —** reportá **en privado** por el buzón de avisos de seguridad de GitHub (*Security → Report a vulnerability*), no en la lista de incidencias. Respondemos en **48 horas** y damos un plazo de corrección de **90 días** antes de publicar el detalle. Hay una excepción importante: **este repositorio no distribuye software ejecutable**, así que la mayoría de los avisos que recibimos son sobre el contenido, no sobre el código.

---

## 1 · Qué entra en el alcance

| Entra | Ejemplo |
|---|---|
| **Secreto expuesto** en el árbol o en la historia | Un token, una llave, una ruta personal con nombre de usuario |
| **Enlace peligroso** en una ficha o pieza publicada | Un enlace que hoy redirige a un APK modificado o a una web con descarga automática |
| **Fallo en las herramientas** de `tools/` | Una compuerta que se puede burlar sin que la vara lo note; un sello que se puede falsificar |
| **Suplantación** | Un sitio o una cuenta que se hace pasar por este archivo |
| **Dato personal** de un tercero publicado sin necesidad | Un nombre, un correo o una captura con identificadores ajenos |

## 2 · Qué queda fuera

- Fallos de seguridad **de las aplicaciones recomendadas**. Van al proyecto de su autor; aquí se retira o se marca la ficha si el fallo es grave y no hay corrección, y se avisa en el registro de cambios.
- Peticiones de paquetes modificados, versiones «premium» o métodos de pago alternativos: no se atienden, en ninguna vía.
- Ausencia de una función o un modo de uso que alguien considere inseguro por diseño del sistema operativo.
- Informes automáticos de escáneres sin una ruta de explotación explicada.

## 3 · Cómo se reporta

1. En GitHub: pestaña **Security** → **Report a vulnerability**. Es privado y llega solo al mantenedor.
2. Si no podés usar esa vía, escribí al correo del perfil con el asunto `SEGURIDAD`.
3. Contá, en este orden: **qué** es vulnerable o incorrecto, **dónde** está (ruta de archivo o URL exacta), **cómo** se reproduce, **qué** consecuencia tiene para una persona y **qué** arreglo sugerís. Sin capturas de datos personales.

No abras una incidencia pública. Un enlace con una explicación pública se convierte en un problema para todos los que lean antes que nosotros.

## 4 · Qué se promete

| Plazo | Compromiso |
|---|---|
| **48 h** | Acuse de recibo con una persona con nombre, no un formulario |
| **7 días** | Evaluación: si entra en alcance y con qué gravedad |
| **90 días** | Corrección o retirada publicada; antes si el riesgo es alto |
| Después | Mención en el registro de cambios, si quien reporta quiere ser nombrado |

Si el fallo afecta a una persona concreta, el plazo se acorta a lo que haga falta: **primero se protege, después se explica.**

## 5 · Cómo se sella y se firma

El árbol se sella con SHA-256 encadenado (`tools/atestar.py`) y el manifiesto se firma sin llave con **Sigstore/cosign** desde la integración continua. Eso permite comprobar dos cosas: que el archivo no cambió desde el sello y que el sello lo emitió la corrida que dice emitirlo. La verificación está descrita en `docs/CODIGO.md` y se puede repetir sin instalar nada propio.

## 6 · Llaves

Las llaves viven fuera del repositorio, en `~/.boveda/tokens.env` con permisos `600`, y ninguna herramienta las escribe en el árbol ni las imprime. El patrón de llave aceptado empieza por `github_pat_`; una llave con otro prefijo se rechaza en `make push` antes de salir de la máquina.

*La Bandita informa a partir de fuentes fechadas.*
