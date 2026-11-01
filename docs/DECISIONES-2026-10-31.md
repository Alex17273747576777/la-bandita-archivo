# DECISIONES DEL TITULAR · sábado 31 de octubre de 2026

Ocho decisiones tomadas por el dueño en conversación. Aquí queda qué decidió, qué hice yo con eso
y qué cambia en el proyecto. Nada de esto se vuelve a preguntar: está firmado.

## 1. Licencia — **decidida y aplicada** (la eligió el asistente por encargo del dueño)

**Opción A**, aplicada el 31 de octubre de 2026:

| Capa | Licencia | Archivo |
|---|---|---|
| Contenido editorial | **CC BY-SA 4.0** | `LICENSE-CONTENIDO` |
| Datos y registro | **CC BY 4.0** | `LICENSE-DATOS` |
| Código y herramientas | **MIT** | `LICENSE` |
| Marca, firma y certificación | reservadas | `NOTICE` |

**Titular del copyright:** «Alexis (La Bandita)». Es la única suposición de esta jornada: el dueño no
dictó el nombre legal. Se corrige con una línea el día que lo diga, y queda anotado aquí para que no
se olvide.

**Por qué A y no otra:** es la única mezcla que abre el archivo (para que el barrio y otros medios lo
reproduzcan), impide que un tercero lo encierre, y deja intacta la marca. La opción C (no comercial)
habría descalificado al proyecto para cualquier fondo de software libre; la D (sin licencia) lo
dejaba inutilizable por cualquiera que no fuera el dueño.

## 2. Página web propia — **descartada**

El dueño no va a montar una página: **esto es un proyecto personal**, no una empresa. Consecuencias
ejecutadas:

- No se compra dominio ni se registra marca.
- No se activa GitHub Pages como sitio público de presentación.
- El generador `tools/sitio.py` se queda como **herramienta interna**: sirve para leer el archivo y
  el registro sin depender de una plataforma, y no se publica como escaparate.
- La propuesta empresarial deja de ser un plan: pasa a **anexo de opciones** (§12 de este documento).

## 3. Canal principal — **WhatsApp**

La serie se publica principalmente en WhatsApp, que es donde está la gente del barrio y donde el
formato de la casa ya respira. Plan operativo en `docs/CANAL-WHATSAPP.md`.

## 4. Inteligencia a usar — **decidida**

Recomendación razonada en `docs/INTELIGENCIA.md`, con configuración lista para copiar.

## 5. Dinero — **no se acepta**, en ninguna forma

Sin patrocinio, sin publicidad, sin afiliados, sin servicios pagados, sin donaciones que compren
influencia. Queda escrito en el `NOTICE` (punto 6) y en la política de gobernanza. El efecto
inmediato: **las líneas L1–L5 de la propuesta quedan archivadas como opciones futuras, no como plan**.
La independencia deja de ser una promesa de marketing y pasa a ser una condición verificable.

## 6. Servidor MCP — **se publica**

Autorizado. Se publica en abierto con la licencia MIT del repositorio, con manifiesto de servidor,
versión fijada y guía de instalación. Sigue siendo de **solo lectura**, sin red y sin credenciales.

## 7. NLnet — **lo presenta el dueño**

Yo dejo el borrador completo en inglés (el formulario exige inglés), el desglose de esfuerzo, el
registro de prompts que su política obliga a entregar si se usó IA, y la lista de lo que el dueño debe
personalizar antes de enviar. **No lo envío yo.** Plazo: 3 de noviembre de 2026, 12:00 CET.

## 8. Firma sin llave (Sigstore) — **autorizada**

Se firma desde GitHub Actions con identidad OIDC del repositorio, sin llaves privadas guardadas.
La atestación de cada lote queda verificable por cualquiera con el certificado efímero de la corrida.

## Lo que sigue igual

El token no se revoca hasta terminar. La vara sigue siendo la puerta: ningún «terminado» sin
`fallos: NINGUNO`. La salud del dueño manda sobre el calendario: **si una tanda se cae porque él no
está, la tanda espera**. Este proyecto no tiene clientes, no tiene plazos de terceros y no debe una
respuesta a nadie más que a su dueño.

---

*Proyecto personal. Sin dinero, sin prisa, sin mentiras. 31 de octubre de 2026.*
