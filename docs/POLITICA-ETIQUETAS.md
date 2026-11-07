# Política de etiquetas estratégicas · «#pings»

**Decisión del dueño, 4-nov-2026:** «es crucial que añadas etiquetas estratégicas a cada publicación, pues los
#pings son esenciales en redes como Facebook y deben ser 100 % específicas, no genéricas».

Esta política convierte esa decisión en una regla medible. Se aplica a toda pieza de Facebook y de WhatsApp, y la
comprueba la compuerta **M29** de `tools/manual_gate.py`.

## 1 · Qué es una etiqueta específica

Una etiqueta es específica cuando **nombra lo que la pieza trae** y no la categoría donde cabría. El criterio
práctico: si al buscar esa etiqueta en la red aparecen millones de publicaciones, no sirve; si aparecen decenas y
todas hablan del mismo asunto, sirve.

| Sirve (específica) | No sirve (genérica) |
|---|---|
| `#KeePassDX` · `#AegisAuthenticator` · `#Shizuku` | `#Android` · `#Apps` · `#Tecnologia` |
| `#SegundoFactor` · `#Passkeys` · `#Debloat` | `#Gratis` · `#OpenSource` · `#Software` |
| `#HuellaSHA256` · `#FirmaDeDepuracion` · `#KDBX` | `#Tips` · `#Recomendaciones` · `#Util` |
| `#ProyectoNacidoEnOctubre` · `#CeroPaquetesAlojados` | `#Movil` · `#Celular` · `#Internet` |

## 2 · Las ocho reglas

1. **Entre ocho y doce por pieza.** Menos de ocho no cubre el tema; más de doce diluye y parece relleno.
2. **Cada etiqueta se gana en el texto.** Al menos el setenta por ciento de las etiquetas tienen que aparecer,
   con sus palabras, en el cuerpo de la pieza. No se etiqueta lo que no se cuenta.
3. **Sin genéricas.** La lista negra del §3 es obligatoria y no admite excepciones «porque esta vez encaja».
4. **Sin acentos, sin ñ, sin espacios y sin guiones.** CamelCase en español: `#SegundoFactor`, `#LlavesDeAcceso`.
5. **Nombre propio primero.** Si el programa tiene nombre, la etiqueta es el nombre: `#KeePassDX`, `#Shizuku`.
6. **El hallazgo también se etiqueta.** La cifra o el hecho que sostiene la pieza tiene su etiqueta:
   `#QuinientosCuatroDias`, `#MilSeiscientosTresDias`.
7. **Como máximo dos etiquetas compartidas** con la pieza anterior del mismo canal. Si dos piezas seguidas
   comparten cinco, no son dos piezas: son una repetida.
8. **El bloque va al final, con su rótulo**, para que viaje en el último mensaje del envío y no se pierda en el
   reparto: `🏷️ Etiquetas estratégicas` y debajo la línea de etiquetas separadas por espacio.

## 3 · Lista negra

`android` · `apps` · `aplicaciones` · `tecnologia` · `gratis` · `opensource` · `software` · `libre` · `movil` ·
`celular` · `internet` · `tips` · `recomendaciones` · `util` · `novedades` · `actualidad` · `seguridad` ·
`privacidad` · `productividad` · `descarga` · `apk` · `androidapp` · `sincostos`

Son genéricas porque no distinguen esta pieza de otras cien mil. La lista se puede ampliar con acta; no se puede
reducir sin decisión del dueño.

## 4 · Cómo se comprueba (M29)

```
python3 tools/manual_gate.py --pieza <ruta-de-la-pieza>
```

M29 falla si: no hay bloque con el rótulo; hay menos de ocho o más de doce; alguna etiqueta está en la lista
negra; alguna lleva acento, ñ, espacio o guion; hay repetidas; o menos del setenta por ciento aparece en el cuerpo.

## 5 · Por qué esto no es cosmético

En Facebook la etiqueta es la única forma de que alguien que busca «KeePassDX» encuentre la pieza. Una pieza sin
etiquetas es una pieza que solo llega a quien ya la estaba esperando, y esa es la mitad del público. Con etiquetas
específicas, cada ficha de esta serie se vuelve encontrable por el nombre exacto de lo que recomienda.

## 6 · Acta

- **4-nov-2026** · se detecta que las piezas 01, 02, 03 y 04 se publicaron sin etiquetas. Se crea esta política,
  se añade la compuerta M29 y se rehace la pasada desde la 01, en el orden que pidió el dueño.
