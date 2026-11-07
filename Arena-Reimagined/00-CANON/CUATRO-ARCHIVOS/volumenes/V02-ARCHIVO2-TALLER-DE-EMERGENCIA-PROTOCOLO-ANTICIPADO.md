═══════════════════════════════════════════════════════════════════
VOLUMEN 02 — MANUAL DE USO: EL TALLER DE EMERGENCIA
(protocolo anticipado de recuperación: qué hacer cuando algo se
rompe antes de que se rompa — ARCHIVO-2 · 27-sep-2026
Forma declarada: AGUA PROSPECTIVA — el lecho de roca está puesto;
este volumen sube el primer muro del castillo: protocolos para
accidentes que aún no ocurrieron, escritos con las lecciones de
los que ya ocurrieron.)
═══════════════════════════════════════════════════════════════════

Propósito: ningún manual que vale espera a la emergencia para
escribirla. Este volumen fija, por anticipado, las operaciones
mínimas de rescate del taller; nace de la vida del taller misma
(los accidentes que ya tuvieron y se navegaron) y sube la mirada
a los que aún no llegan. Cada protocolo dice: señal de alarma,
primeros cinco minutos, rescate completo, verificación, y el
aprendizaje actado.

───────────────────────────────────────────────────────────────────
PROTOCOLO E-1 · UN DOCUMENTO GRANDE SE MODIFICÓ MAL O SE PERDIÓ
───────────────────────────────────────────────────────────────────
SEÑAL: un len() que cambió sin tren que lo explique; un sha16 del
padrón que ya no coincide; un archivo que falta en una ruta que
nada movió.
PRIMEROS CINCO MINUTOS: no escribir NADA más. Congelar la mesa.
Censar: ls del directorio afectado + git/diff si existen. Nombrar
en el acta: «E-1 activado (fecha, hora, señal)».
RESCATE: (1) si el padrón tiene sha16 del estado sano y existe un
volumen original, el contenido se recompone por fusión exacta;
(2) si existe respaldo pre-cambio (ver _auditoria-30sep/originales/
como modelo), restaurar y re-aplicar solo las planillas válidas;
(3) si no hay respaldo: reconstrucción exponencial desde los
fragmentos vivos (padrones, actas, piezas hermanas), con planilla
explícita de cada fragmento reincorporado.
VERIFICACIÓN: sha16 nuevo sellado con acta del rescate — jamás
«fingir» el sha16 viejo: el acta confiesa la herida y su cura.
APRENDIZAJE (prevención de hoy): cada fusión al cofre lleva su
sha16 en el padrón del archivo inmediato (esta regla ya vive y
fue verificada por las baterías E-1…E-3 del 27-sep-2026).

───────────────────────────────────────────────────────────────────
PROTOCOLO E-2 · EL CUADERNO DEL TALLER (EL ACTA) SE ROMPE O SE
CORROMPE
───────────────────────────────────────────────────────────────────
SEÑAL: len() del acta decrece sin tren; un encabezado de tren duplicado
o fuera de secuencia; caracteres de control donde nunca los hubo.
PRIMEROS CINCO MINUTOS: idénticos — congelar, censar, declarar E-2.
RESCATE: el acta es el documento más protegido de la casa porque es
la casa: (1) los volúmenes llevan su registro en los padrones y
pueden reconstruir el sustrato técnico; (2) los trenes vivos se
verifican uno a uno (trenes 19→39 monótonos medidos en E-1);
(3) lo irreconstruible se anota con letra expresa: «gap del acta,
de tal fecha a tal fecha, cifras de memoria» — jamás reescritura
inventada. La merma se firma con su medida.
VERIFICACIÓN: batería P4 (enumeración de trenes) verde al cierre del
rescate y declaración de fecha del acta de cura.
APRENDIZAJE: el índice-apéndice de trenes (ya actado en el compendio
de fase 30-sep como propuesta) pasa de «pendiente» a «deuda del
castillo»: el acta heterogénea de los primeros 18 trenes merece su
contenido navegable.

───────────────────────────────────────────────────────────────────
PROTOCOLO E-3 · EL INSTRUMENTO MIENTE (FALSO POSITIVO O NEGATIVO
SISTÉMICO)
───────────────────────────────────────────────────────────────────
SEÑAL: un mismo patrón de falla del instrumento aparece por segunda
vez; dos FAILS de batería se absuelven con veredicto contextual.
PRIMEROS CINCO MINUTOS: suspender los veredictos del instrumento
cuestionado — solo lectura humana —; declarar E-3 a la vista.
RESCATE: corregir la regla del instrumento, no el taller; escribir
la nueva regla al lado de la vieja (append-only), con fecha y causa;
volver a correr la batería: el taller no se toca.
VERIFICACIÓN: correr el instrumento corregido sobre los casos
históricos conocidos: debe absolverlos a todos con su razón (28-BIS
visto como pierna; citas entrecomilladas del ledger absueltas;
expectativas calculadas, no recordadas).
APRENDIZAJE (medida del 27-sep-2026): tres reglas instrumentales
corregidas ese mismo día (sufijos de pierna · excluir citas ·
expectativas calculadas) quedaron como ficha F-087 del futuro
volumen de la guía — la lección del instrumento ya es material de
enseñanza, no vergüenza escondida.

───────────────────────────────────────────────────────────────────
PROTOCOLO E-4 · UNA PUBLICACIÓN SALE CON DEFICIENCIA VISTA DESPUÉS
───────────────────────────────────────────────────────────────────
SEÑAL: una pieza publicada recibe un hallazgo (comentario vecino, leer
al aire libre, segunda lectura del taller) — este protocolo espera
a la era publicativa (hoy la puerta está cerrada y no existe pieza
viva nueva bajo estrés).
PRIMEROS CINCO MINUTOS: foto con hora del hallazgo; ninguna edición
silenciosa; declarar en el acta la pieza, la plataforma y la falla.
RESCATE: edición con planilla R-17 (tramo, antes→después, Δ, razón,
reversa) y nota a la audiencia si la falla tocaba un hecho, con
disculpa honesta. El borrado completo se reserva al dueño: él decide
si la pieza se retira o se corrige.
VERIFICACIÓN: los hechos del par hermano (WA/FB) se re-alinean por
T4 si la corrección mueve números.
APRENDIZAJE: FB 10 (48 tramos, planilla por planilla, respaldo
conservado) es la base de este protocolo — la deficiencia pública se
corrige con la misma dignidad que la interna.

───────────────────────────────────────────────────────────────────
PROTOCOLO E-5 · EL TRABAJO SE DETIENE más de LO ESPERADO
───────────────────────────────────────────────────────────────────
SEÑAL: ningún tren nuevo en la jornada (o en las dos seguidas);
colas cerradas y pulso imposible.
PRIMEROS CINCO MINUTOS: anotar en el acta la parada — la parada
también es acta — y su causa: espera del dueño, bloqueo técnico,
cuando la señal vuelva.
RESCATE: reanudar por el lecho de piedra: abrir el índice de cauces
del motor y tomar el siguiente tema asignado (nunca el tema bonito):
la estructura garantiza que cualquier vuelta es un reanudar, no un
reiniciar.
VERIFICACIÓN: el primer tren tras el alto declara el alto en su
primer renglón (la transparencia incluye la pausa).
APRENDIZAJE: el dueño reina sobre la cadencia (la jornada avanza al
compás de su pulso, no contra él) — la pausa ordenada no es derrota,
es espera firme.

═══════════════════════════════════════════════════════════════════
Cierre del volumen: E-1…E-5 son los primeros cinco muros del
castillo: no esperan al desastre para enseñar — aprenden del desastre
para adelantarse. Próximo volumen del manual (cauce C): protocolos
del contenido (V03: matraje y planillas vivas).
═══════════════════════════════════════════════════════════════════
