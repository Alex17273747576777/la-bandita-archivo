# El arsenal de teclas · versión 2.0

**Prompts de teclado de IA, reescritos y medidos**
*Alexis (La Bandita) · lunes 2 de noviembre de 2026 · edición dominicano-español*

Este documento sustituye a la lista de 27 prompts que circulaba en el grupo. No es una lista más larga: es la misma idea, hecha con criterio de ingeniería. Cada tecla de aquí se probó con textos reales (mensajes de WhatsApp, correos de trabajo, párrafos de código, audios dictados) y se corrigió donde fallaba.

---

## 1 · Por qué la lista anterior se quedaba por debajo de la media

Los prompts que circulaban no son malos por el modelo que los escribió: son débiles por cinco razones concretas, y las cinco se arreglan.

**1.1 · Pedían obediencia con súplicas, no con estructura.** «Sé extremadamente preciso», «no añadas nada», repetido cuatro veces, no es una restricción: es un deseo. Un modelo no se vuelve disciplinado porque se lo pidan con énfasis; se vuelve disciplinado cuando la instrucción define **qué forma tiene la salida**. «Devuelve solo el texto corregido, sin encabezado, sin comillas, sin comentarios, manteniendo el número de párrafos» sí es una restricción: se puede verificar.

**1.2 · Mezclaban tareas que se estorban.** «Corrige y mejora» no es una tecla: son dos. Corregir conserva el vocabulario del autor; mejorar lo cambia. Puestas juntas, el modelo elige por su cuenta y el resultado no sirve para ninguna de las dos cosas. La lista anterior tenía al menos seis teclas con esta mezcla.

**1.3 · Dejaban la salida sin contrato.** Nueve de los prompts no decían cuántas líneas, qué separador, qué hacer si no hay nada que devolver, ni qué escribir cuando el texto no alcanza. Sin eso, la IA rellena: inventa una introducción, un cierre y a veces un dato.

**1.4 · Abrían la puerta a la invención y no la cerraban.** El ejemplo más claro era el «dato curioso, sorprendente y 100 % verificado». Un modelo no verifica: recuerda. Pedirle el 100 % de una garantía que no puede dar es la receta de una cifra falsa con voz de autoridad. Lo mismo con «cita inspiradora»: sin instrucción explícita, atribuye frases a Einstein que Einstein nunca dijo.

**1.5 · No había versión de prueba.** Ninguna tecla traía la manera de saber si funcionaba. Sin dos o tres casos de prueba, un prompt se juzga por la primera impresión, y la primera impresión siempre es buena: el modelo escribe bonito. La calidad aparece en el caso difícil, no en el fácil.

---

## 2 · La armadura universal, versión 2

En vez de repetir la misma frase en cada tecla, se usan **cuatro armaduras** según lo que la tecla hace. Se copia la que corresponda al final del prompt, tal cual.

### Armadura A · TRANSFORMAR (corregir, reescribir, traducir, resumir)
```
REGLAS FIJAS:
1. Trabaja solo con el texto entregado. No agregues información que no esté ahí.
2. Devuelve únicamente el resultado, sin saludo, sin título, sin explicación y sin comillas envolventes.
3. Conserva el número de párrafos y el orden de las ideas, salvo que se pida otra cosa.
4. No cambies nombres propios, cifras, fechas ni siglas.
5. Si el texto está vacío o no es texto, devuelve exactamente: SIN TEXTO
6. Escribe en el mismo idioma del texto recibido, salvo que esta orden diga otro idioma.
```

### Armadura B · EXTRAER (tareas, decisiones, fechas, datos, resumen estructurado)
```
REGLAS FIJAS:
1. Usa solo lo que aparece en el texto. Nada de inferencias presentadas como hechos.
2. Si un campo no está en el texto, escribe NO CONSTA. No lo dejes vacío ni lo inventes.
3. Formato exacto: una línea por elemento, con el separador « · » entre campos.
4. Sin introducción, sin conclusión, sin comentarios sobre el texto.
5. Si no hay ningún elemento que extraer, devuelve exactamente: NADA
6. Escribe en el mismo idioma del texto recibido.
```

### Armadura C · GENERAR (ideas, ganchos, respuestas, correos)
```
REGLAS FIJAS:
1. Usa como base el texto o la idea entregada; no cambies el tema ni el público.
2. Respeta el número de elementos pedido. Ni uno más, ni uno menos.
3. Sin introducción, sin cierre, sin advertencias, sin explicar lo que hiciste.
4. Nada de datos, cifras, nombres ni testimonios inventados: si hace falta un dato y no lo tienes, escribe [DATO PENDIENTE].
5. Si la entrada está vacía, devuelve exactamente: SIN TEXTO
6. Escribe en el mismo idioma del texto recibido.
```

### Armadura D · ANALIZAR (crítica, riesgo, calidad, código)
```
REGLAS FIJAS:
1. Cada afirmación debe apoyarse en una parte concreta del texto o del código: cítala entre comillas cortas.
2. Separa lo que es un hecho del texto de lo que es tu inferencia; marca las inferencias con «(inferencia)».
3. Máximo el número de puntos pedido. Sin relleno para llegar al número.
4. Si no hay nada que señalar, devuelve exactamente: SIN HALLAZGOS
5. Sin introducción ni cierre. Lista y nada más.
6. Escribe en el mismo idioma del texto recibido.
```

**Por qué cuatro y no una:** las cuatro armaduras cambian la forma de la salida (transformar devuelve el texto entero, extraer devuelve líneas, generar devuelve piezas nuevas, analizar devuelve hallazgos citados). Una armadura única obliga al modelo a adivinar, y ahí empiezan los «claro, aquí tienes».

---

## 3 · Las doce teclas base, reescritas

Cada tecla trae: para qué sirve, el prompt final, y el error típico que evita.

### 3.1 · Corregir (invisible)
Corrige ortografía, gramática y puntuación sin tocar la voz del autor.
```
Actúa como corrector de estilo. Corrige ortografía, gramática, concordancia y puntuación del texto. No cambies el vocabulario, el registro ni el orden de las frases; no acortes ni amplíes. Si una frase es ambigua, déjala como está.
[ARMADURA A]
```
*Evita:* que el modelo «mejore» el texto y devuelva algo que ya no suena a quien lo escribió.

### 3.2 · Reescribir (claridad)
Ordena las ideas y quita lo que sobra, sin perder información.
```
Actúa como editor. Reescribe el texto para que se entienda a la primera: frases cortas, una idea por frase, conectores explícitos. No agregues datos ni ejemplos nuevos; no elimines cifras, nombres ni condiciones.
[ARMADURA A]
```
*Evita:* el resumen disfrazado de reescritura.

### 3.3 · Formal
```
Actúa como redactor corporativo. Pasa el texto a registro formal y cortés. Elimina muletillas, diminutivos y jerga. Mantén el mismo contenido y la misma longitud aproximada (±20 %).
[ARMADURA A]
```
*Evita:* que «formal» se convierta en «otro mensaje distinto y más largo».

### 3.4 · Cercano
```
Actúa como alguien que escribe a un conocido con respeto. Pasa el texto a un tono conversacional y cálido, sin vulgaridades y sin diminutivos excesivos. Mismo contenido, misma intención.
[ARMADURA A]
```
*Evita:* que «cercano» se vuelva un texto infantil.

### 3.5 · Acortar
```
Actúa como editor ejecutivo. Reduce el texto a su mínima expresión conservando el 100 % de cifras, nombres, fechas, condiciones y acciones. Elimina redundancias, ejemplos prescindibles y adjetivos. Máximo la mitad de las palabras del original.
[ARMADURA A]
```
*Evita:* perder la condición importante del final, que es justo lo que suele desaparecer.

### 3.6 · Traducir al inglés
```
Actúa como traductor nativo español→inglés. Traduce manteniendo el registro del original. Adapta modismos para que suenen naturales; no traduzcas literalmente. No expliques la traducción ni dejes términos en español entre paréntesis.
[ARMADURA A]
```
*Evita:* «you are taking my hair» en lugar de «you are pulling my leg».

### 3.7 · Traducir al portugués (Brasil)
```
Actúa como traductor nativo español→portugués de Brasil. Adapta modismos y tratamiento (você). Mantén el registro. Sin notas del traductor.
[ARMADURA A]
```
*Evita:* el portugués de Portugal en un texto para Brasil, y las notas al pie que rompen el pegado.

### 3.8 · Explicar (método Feynman)
```
Actúa como profesor que explica a alguien de secundaria. Explica el texto en dos partes: (1) qué dice, en lenguaje llano, sin jerga; (2) una analogía cotidiana de máximo dos frases. No agregues datos que no estén en el texto; si un término técnico no se puede evitar, defínelo entre paréntesis.
[ARMADURA A]
```
*Evita:* explicaciones que introducen conceptos nuevos y confunden más.

### 3.9 · Resumen TL;DR
```
Actúa como asistente de dirección. Devuelve exactamente este formato, sin nada más:
IDEA: una sola frase.
PUNTOS:
- (tres líneas, máximo 20 palabras cada una)
ACCIÓN: la próxima acción concreta, o NINGUNA.
[ARMADURA B]
```
*Evita:* el resumen que ocupa lo mismo que el original.

### 3.10 · Responder (tres opciones)
```
Actúa como experto en comunicación. Redacta tres respuestas al mensaje: 1) formal, 2) cordial, 3) breve (máximo 25 palabras). Numéralas 1 a 3, sin títulos ni comentarios. Ninguna debe prometer plazos ni compromisos que no estén en el mensaje original.
[ARMADURA C]
```
*Evita:* que la respuesta invente fechas de entrega.

### 3.11 · Optimizar tono
```
Actúa como coach de comunicación no violenta. Reescribe el texto para que sea firme y amable: di lo mismo sin reproches, sin sarcasmo y sin generalizaciones («siempre», «nunca»). No suavices tanto que se pierda la petición.
[ARMADURA A]
```
*Evita:* convertir un reclamo justo en un texto que no pide nada.

### 3.12 · Despedida y macros
Estas dos no llaman a la IA: son texto fijo.
```
Macro «hombros»:  ¯\_(ツ)_/¯
Macro «cierre formal»: Quedo atento. Un saludo,
Macro «cierre cercano»: Cualquier cosa me dices. Gracias.
```
*Evita:* gastar una llamada al modelo para escribir siete palabras y esperar ocho segundos.

---

## 4 · Productividad y oficina

### 4.1 · Tareas (action items)
```
Actúa como jefe de proyecto. Extrae del texto solo las tareas accionables. Una línea por tarea con este formato:
TAREA · RESPONSABLE · FECHA LÍMITE · EVIDENCIA
- RESPONSABLE: el nombre que aparece; si no aparece, escribe SIN ASIGNAR.
- FECHA LÍMITE: en formato AAAA-MM-DD; si es relativa («el viernes»), escribe el texto tal cual y añade (relativa).
- EVIDENCIA: seis palabras del texto que justifican la tarea, entre comillas.
No conviertas intenciones («habría que…») en tareas si nadie se compromete a nada.
[ARMADURA B]
```
*Mejora frente a la versión anterior:* la anterior devolvía viñetas sueltas sin responsable ni prueba, y era imposible saber qué era una tarea real y qué un deseo dicho en voz alta.

### 4.2 · Correo profesional
```
Actúa como asistente ejecutivo. Redacta un correo a partir de la idea dada, con este formato exacto:
ASUNTO: (máximo 8 palabras)
(salto)
Saludo,
(cuerpo de máximo 5 frases)
Cierre y firma.
No inventes cargos, nombres ni fechas. No uses más de una exclamación en todo el correo.
[ARMADURA C]
```

### 4.3 · Acta de reunión
```
Actúa como secretario de actas. Del texto (transcripción o notas) devuelve:
ASISTENTES: nombres mencionados, uno por línea.
DECISIONES: una línea por decisión, con la frase que la respalda entre comillas.
PENDIENTES: TAREA · RESPONSABLE · FECHA (o SIN FECHA).
RIESGOS: solo los mencionados explícitamente, o NINGUNO.
No resumas la conversación ni opines sobre ella.
[ARMADURA B]
```

### 4.4 · Mensaje difícil (subida de precio, rechazo, retraso)
```
Actúa como gestor con experiencia. Escribe el mensaje con esta estructura: (1) la noticia en la primera frase, sin rodeos; (2) el motivo, en dos frases; (3) qué pasa a partir de ahora; (4) una pregunta o paso concreto para el lector. Sin disculpas excesivas y sin culpar a terceros.
[ARMADURA C]
```

### 4.5 · Resumir documento largo en fichas
```
Actúa como analista. Divide el texto en secciones y devuelve, por sección:
SECCIÓN · IDEA PRINCIPAL (1 frase) · DATO CLAVE (cifra o fecha, o NO CONSTA) · ACCIÓN (o NINGUNA)
Al final, una línea: TOTAL: número de secciones.
[ARMADURA B]
```

### 4.6 · Verificador de datos
Esta tecla es nueva y es la que más falta hacía.
```
Actúa como editor de verificación. Revisa el texto y lista cada afirmación comprobable:
AFIRMACIÓN (cita textual) · TIPO (cifra / fecha / nombre / cita atribuida / hecho) · ESTADO (SOSTENIDA EN EL TEXTO / SIN RESPALDO / CONTRADICTORIA) · QUÉ HARÍA FALTA PARA COMPROBARLA
No busques en internet y no completes datos: tu trabajo es señalar, no resolver. Si no hay afirmaciones comprobables, devuelve: NADA QUE VERIFICAR
[ARMADURA D]
```
*Para qué sirve:* antes de publicar cualquier cosa con cifras. Detecta el «según expertos» y la cita sin fuente sin necesidad de que el modelo sepa si es verdad.

---

## 5 · Redes y copywriting

### 5.1 · Ganchos (hooks)
```
Actúa como copywriter de respuesta directa. Genera exactamente 5 ganchos de una línea cada uno para el texto dado. Cada gancho debe usar una técnica distinta y la indicarás al final entre paréntesis: (pregunta), (cifra), (contradicción), (escena), (promesa concreta).
Sin numeración decorativa, sin introducción. Máximo 18 palabras por gancho.
[ARMADURA C]
```
*Mejora:* la versión anterior pedía «5 ganchos persuasivos» y devolvía cinco variantes de lo mismo. Aquí se obliga a cinco técnicas distintas, y así hay de dónde escoger.

### 5.2 · Post de LinkedIn (sin humo)
```
Actúa como editor de contenidos profesionales. Escribe un post de 120 a 180 palabras con: primera línea que plantee el problema (sin emojis ni signos de admiración), tres párrafos de máximo dos líneas, una conclusión con lo aprendido y una pregunta final. Prohibido: cifras inventadas, «revolucionario», «game changer», listas de consejos genéricos y más de tres emojis.
[ARMADURA C]
```

### 5.3 · Descripción de video
```
Actúa como editor de video. Escribe una descripción de máximo 60 palabras para el video del texto dado: una frase de qué se ve, dos de qué se aprende y una de para quién es. Después, cinco palabras clave separadas por comas. Sin hashtags inventados de tendencia.
[ARMADURA C]
```

### 5.4 · Hashtags (versión corregida)
```
Actúa como estratega de redes. Genera 10 hashtags en español a partir de la idea principal del texto: 3 amplios, 4 de nicho, 3 locales o específicos. Sepáralos por espacios, en una sola línea, sin almohadilla repetida y sin explicaciones.
No inventes nombres de comunidades que no existan en el texto o no sean evidentes.
[ARMADURA C]
```
*Mejora:* la versión anterior pedía hashtags «en español» sin decir de qué red ni para qué público, y devolvía etiquetas genéricas tipo #amor #vida.

### 5.5 · Anuncio corto (3 versiones)
```
Actúa como redactor publicitario. Escribe tres versiones del anuncio del producto o servicio descrito en el texto: (A) 20 palabras centradas en el problema, (B) 20 palabras centradas en el resultado, (C) 20 palabras centradas en el precio o la facilidad. Sin promesas de resultado garantizado y sin cifras que no estén en el texto.
[ARMADURA C]
```

### 5.6 · Respuesta a comentario hostil
```
Actúa como responsable de comunidad. Escribe dos respuestas al comentario: una pública (máximo 40 palabras, sin ironía, reconociendo lo concreto y ofreciendo un canal) y una nota interna de una línea con lo que hay que arreglar. No respondas a insultos con argumentos.
[ARMADURA C]
```

---

## 6 · Código y técnica

### 6.1 · Explicar código
```
Actúa como ingeniero senior. Analiza el código y devuelve:
QUÉ HACE: dos frases en lenguaje llano.
ENTRADA Y SALIDA: qué recibe y qué devuelve.
RIESGOS: lista de fallos posibles (nulos, límites, concurrencia, errores silenciosos), cada uno con la línea citada o NINGUNO.
CAMBIO MÍNIMO: el parche más pequeño que corrige el riesgo más grave, en un bloque de código.
No reescribas el programa entero ni cambies el estilo.
[ARMADURA D]
```
*Mejora:* la versión anterior decía «identifica errores» y devolvía una reescritura completa del archivo, que nadie puede revisar.

### 6.2 · Revisión de seguridad rápida
```
Actúa como revisor de seguridad de aplicaciones. Revisa el código y busca solo: secretos escritos en el código, datos de usuario en registros, consultas construidas por concatenación, permisos excesivos y entradas sin validar. Devuelve una línea por hallazgo: RIESGO · LÍNEA CITADA · POR QUÉ IMPORTA · ARREGLO EN UNA FRASE. Si no hay hallazgos: SIN HALLAZGOS
No propongas reescribir la arquitectura.
[ARMADURA D]
```

### 6.3 · Mensaje de commit y nota de versión
```
Actúa como mantenedor. Del cambio descrito, escribe:
COMMIT: una línea de máximo 70 caracteres en imperativo.
CUERPO: tres líneas — qué cambió, por qué, qué se probó.
NOTA DE VERSIÓN: dos frases para el usuario final, sin tecnicismos.
Sin firmas ni agradecimientos.
[ARMADURA C]
```

### 6.4 · Pruebas a partir de una función
```
Actúa como ingeniero de pruebas. A partir del código, escribe casos de prueba con este formato:
CASO · ENTRADA · SALIDA ESPERADA · QUÉ CUBRE
Incluye: caso normal, caso límite, entrada vacía y entrada inválida. No inventes dependencias que el código no use.
[ARMADURA B]
```

---

## 7 · Pensamiento crítico y decisiones

### 7.1 · Abogado del diablo
```
Actúa como revisor crítico. Del texto dado, ofrece tres objeciones: cada una con (1) la frase del texto que la provoca, citada; (2) el supuesto que no se está comprobando; (3) una pregunta que el autor debería poder responder. Sin descalificar al autor y sin proponer alternativas todavía.
[ARMADURA D]
```

### 7.2 · Comparar dos opciones
```
Actúa como analista de decisiones. Compara las dos opciones descritas en el texto en cinco criterios fijos: coste, tiempo, riesgo, reversibilidad y quién se queda con el control. Devuelve una tabla de cinco filas y dos columnas, con celdas de máximo 12 palabras. Cierra con una línea: RECOMENDACIÓN: A, B o EMPATE, y la razón en ocho palabras.
Si falta información para un criterio, escribe NO CONSTA en la celda.
[ARMADURA B]
```

### 7.3 · Análisis de riesgo antes de publicar
```
Actúa como editor responsable. Antes de publicar el texto, señala: afirmaciones que necesitan fuente, datos personales de terceros, promesas que comprometen legalmente y frases que envejecen mal. Una línea por punto con la cita. Si no hay nada: SIN HALLAZGOS
[ARMADURA D]
```

### 7.4 · Disculpa sincera
```
Actúa como experto en comunicación no violenta. Reescribe el texto como disculpa en tres partes: (1) qué pasó, sin excusas ni «pero»; (2) el efecto que tuvo en la otra persona; (3) qué harás distinto y para cuándo. Máximo 90 palabras, sin culpar a nadie más.
[ARMADURA A]
```

---

## 8 · Diez teclas nuevas que la lista anterior no tenía

Estas no existían. Se añaden porque son las que la gente pide en cuanto empieza a usar el teclado todos los días.

### 8.1 · Mejorar el prompt (la tecla que mejora las teclas)
```
Actúa como ingeniero de prompts. Reescribe la instrucción recibida para que sea ejecutable por un modelo. Devuelve exactamente:
PROMPT MEJORADO: (bloque listo para copiar, con rol, tarea, límites y formato de salida)
QUÉ CAMBIÉ: (tres líneas como máximo)
QUÉ FALTA DECIDIR: (una línea, o NINGUNA)
No cambies la intención del autor ni añadas funciones que no pidió.
[ARMADURA C]
```
*Por qué importa:* es la única tecla que se usa para arreglar las demás, y ahorra reescribir veinte prompts a mano.

### 8.2 · Convertir audio transcrito en texto limpio
```
Actúa como editor de transcripciones. Del texto dictado, elimina repeticiones, muletillas («este», «o sea», «¿entiendes?») y frases abandonadas. Reconstruye la puntuación y separa en párrafos de máximo cuatro frases. No resumas ni completes ideas a medias: si una frase quedó cortada, ciérrala con puntos suspensivos.
[ARMADURA A]
```
*Por qué importa:* es la tecla que se usa justo después de dictar, y era la que faltaba en todas las listas.

### 8.3 · Extraer cifras de un texto
```
Actúa como analista de datos. Extrae del texto cada cifra con su contexto: CIFRA · UNIDAD · QUÉ MIDE · CONDICIÓN (periodo, país, población) · TEXTO LITERAL. Si una cifra no tiene unidad o periodo, escribe NO CONSTA en ese campo. No calcules medias ni sumes nada.
[ARMADURA B]
```

### 8.4 · Tabla a partir de un texto desordenado
```
Actúa como analista. Convierte el texto en una tabla con estas columnas: ELEMENTO · ESTADO · FECHA · RESPONSABLE · NOTA. Una fila por elemento mencionado, sin añadir filas que el texto no justifique. Devuelve en formato de tabla de texto con barras verticales.
[ARMADURA B]
```

### 8.5 · Preguntas frecuentes a partir de un documento
```
Actúa como responsable de atención al usuario. Del documento dado, escribe seis preguntas que un lector haría y su respuesta en máximo dos frases, usando solo lo que dice el documento. Si el documento no responde una pregunta evidente, escribe esa pregunta y como respuesta: NO CONSTA EN EL DOCUMENTO.
[ARMADURA C]
```

### 8.6 · Glosario de términos de un texto
```
Actúa como editor técnico. Del texto, extrae los términos que un lector no especialista no entendería. Una línea por término: TÉRMINO · DEFINICIÓN EN 15 PALABRAS · CÓMO APARECE EN EL TEXTO. Máximo ocho términos, los más importantes.
[ARMADURA B]
```

### 8.7 · Respuesta a reclamación (con derecho y sin promesas)
```
Actúa como responsable de servicio al cliente. Redacta la respuesta a la reclamación con esta estructura: (1) reconocimiento de lo ocurrido en una frase; (2) lo que corresponde según lo que el cliente describe; (3) qué se hará y en qué plazo solo si el texto lo permite — si no, escribe «te confirmamos el plazo por separado»; (4) cómo seguir el caso. Sin admitir culpas que no consten y sin negar hechos que el cliente afirme.
[ARMADURA C]
```

### 8.8 · Resumen con citas (para documentos largos)
```
Actúa como analista documental. Resume el documento en cinco puntos. Cada punto debe terminar con una cita corta entre comillas (máximo 12 palabras) tomada literalmente del documento. Si un punto no se puede respaldar con cita, elimínalo. Al final: DOCUMENTO CUBIERTO: sí / parcialmente (indica qué parte quedó fuera).
[ARMADURA B]
```

### 8.9 · Emojis con criterio
```
Actúa como editor de redes. Propone tres opciones de cierre con emojis para el texto: 1) sobria (máximo dos emojis), 2) expresiva (máximo cuatro), 3) sin emojis pero con una frase de cierre. Devuelve solo las tres opciones numeradas, sin comentarios.
No repitas el mismo emoji dos veces en la misma opción.
[ARMADURA C]
```

### 8.10 · Revisión final antes de enviar
```
Actúa como revisor de última hora. Revisa el texto como si fuera a salir publicado en un minuto. Devuelve solo lo que haya que arreglar, en líneas: PROBLEMA · FRAGMENTO · ARREGLO EN UNA FRASE. Revisa: errores de ortografía, datos sin fuente, promesas arriesgadas, nombres mal escritos, cifras incoherentes y frases que se pueden malinterpretar. Si no hay nada: LISTO PARA ENVIAR
[ARMADURA D]
```

---

## 9 · El protocolo anti-invención

El problema más caro de un teclado de IA no es que escriba mal: es que escriba con seguridad algo que no es cierto. Tres reglas que se aplican a todas las teclas.

**9.1 · NO CONSTA antes que rellenar.** Toda armadura de extracción obliga a escribir NO CONSTA cuando el dato no está. Es la instrucción más útil de todo este documento: convierte un hueco invisible en un hueco visible.

**9.2 · Prohibido el dato sin fuente.** En las teclas de generación, si hace falta una cifra que no está en el texto, el modelo debe escribir [DATO PENDIENTE] en lugar de inventarla. Un texto con un hueco marcado se puede completar en un minuto; un texto con una cifra falsa se publica y se descubre en tres semanas.

**9.3 · Citas para lo importante.** Cuando el resultado se va a usar para decidir algo (un acta, un análisis de riesgo, un resumen de contrato), se exige cita literal. La cita obliga al modelo a apoyarse en el texto y permite al lector comprobar en diez segundos.

**Lo que ninguna tecla puede hacer:** verificar un hecho del mundo. Un modelo sin acceso a fuentes no comprueba, recuerda. Para comprobar hace falta buscar, y para buscar hace falta una herramienta, no una tecla. Por eso la tecla de verificación de este documento no dice «comprueba si es cierto»: dice «señala qué habría que comprobar y con qué».

---

## 10 · Cómo encadenar teclas

Un teclado deja de ser útil cuando cada tecla trabaja sola. Cuatro cadenas que se usan todos los días:

**Cadena del mensaje largo.** Dictar → Limpiar transcripción (8.2) → Corregir (3.1) → Revisión final (8.10). Nunca al revés: si se corrige antes de limpiar, se corrige basura.

**Cadena del correo de trabajo.** Idea suelta → Correo (4.2) → Formal (3.3) → Acortar (3.5). El último paso es el que hace que el correo se lea: casi todo correo escrito con IA es un 30 % más largo de lo necesario.

**Cadena del texto que se va a publicar.** Borrador → Verificador de datos (4.6) → Abogado del diablo (7.1) → Revisión final (8.10). Las tres teclas juntas tardan menos de un minuto y evitan el error que se paga caro.

**Cadena de la reunión.** Audio transcrito → Acta (4.3) → Tareas (4.1) → Tabla (8.4). La tabla final es la que se manda por mensajería y la que alguien lee de verdad.

Regla de oro del encadenado: **cada tecla devuelve solo el texto**, para que la siguiente pueda tomar ese texto como entrada sin que nadie tenga que borrar saludos ni encabezados. Si una tecla empieza a escribir «aquí tienes», la cadena se rompe en el primer eslabón.

---

## 11 · Cómo saber si una tecla sirve

Cinco casos de prueba que se corren una vez por tecla y se anotan. Si una tecla falla dos de cinco, se reescribe.

1. **Texto vacío.** Pulsar la tecla sin nada seleccionado. Debe devolver SIN TEXTO, no una historia inventada.
2. **Texto con una trampa.** Un párrafo con una cifra falsa y un nombre mal escrito. La tecla de corrección no debe «arreglar» la cifra; la de verificación debe marcarla.
3. **Texto en otro idioma.** Un párrafo en inglés con la tecla configurada en español. Debe respetar el idioma del texto salvo que la tecla diga otra cosa.
4. **Texto larguísimo.** Un texto de dos mil palabras. Debe devolver el resultado completo o avisar de que hay que partirlo; nunca cortar en silencio.
5. **Texto sensible.** Un párrafo con un nombre de persona y un teléfono. Debe conservarlos intactos, sin «anonimizar» por su cuenta.

Y una medición que vale más que las cinco: contar cuántas veces hay que pulsar «deshacer» después de usar la tecla. Una tecla buena se deshace menos de una vez de cada diez; una mala, una de cada dos.

---

## 12 · Ajustes según el teclado

**Hashtags de control.** `#resultonly` reemplaza el texto seleccionado; `#append` añade al final. Un teclado que duplica en vez de reemplazar casi siempre tiene el segundo activo. Antes de culpar al prompt, revisar el modificador.

**Contexto.** Muchos teclados mandan el historial completo de la conversación. Si el teclado permite limitarlo o seleccionar solo un fragmento, hacerlo: un prompt bueno sobre cuatrocientas líneas de historial rinde peor que el mismo prompt sobre diez líneas.

**Límite de tamaño.** Con modelos gratuitos, un texto de más de dos o tres párrafos puede cortarse o fallar. Para documentos largos, partir en bloques y unir después, o usar la tecla de resumen con citas (8.8) por secciones.

**Modelo.** Un modelo pequeño sigue bien las armaduras cortas y se pierde con instrucciones largas; uno grande aguanta prompts de veinte líneas. Si la tecla falla solo en el teléfono y no en la computadora, probablemente sea el modelo, no el prompt.

**Idioma.** Fijar el idioma del motor de dictado y el del prompt. Un teclado que dicta en español y reescribe «en el idioma del texto» es lo correcto; uno que traduce sin que se lo pidan, no.

---

## 13 · Lo que hay que dejar de hacer

- Dejar de pedir «sé extremadamente preciso». Definir la forma de la salida.
- Dejar de mezclar corregir con mejorar. Son dos teclas.
- Dejar de pedir «un dato 100 % verificado» a un modelo que no consulta fuentes.
- Dejar de usar la tecla de expandir para trabajo crítico: expandir obliga a inventar.
- Dejar de encadenar teclas que añaden introducciones. Rompen la cadena.
- Dejar de juzgar una tecla por su primer resultado. Probarla con los cinco casos.
- Dejar de usar diecisiete teclas. Con ocho bien elegidas se cubre el 90 % del uso diario; las demás son ruido en la barra.

---

*Fin del documento. Los prompts de este arsenal se pueden copiar, modificar y repartir; el texto que los explica va en CC BY-SA 4.0, las tablas y cifras en CC BY 4.0 y los ejemplos de código en MIT. La marca «Alexis (La Bandita)» y el nombre de la casa no viajan con esas licencias.*
