═══════════════════════════════════════════════════════════════════
VOLUMEN 02 — FICHAS VIVAS F-081…F-086: los seis descuidos paridos
al ritmo del taller entre el 22-sep y el 27-sep de 2026
(ARCHIVO-3 · Guía de acción · taxonomía para el control · 27-sep-2026
Forma declarada: VAPOR QUE YA LLOVIÓ — lluvia con medida y acta.)
═══════════════════════════════════════════════════════════════════

───────────────────────────────────────────────────────────────────
F-081 · EL NOMBRE QUE EXISTÍA EN LA MEMORIA PERO NO EN EL DISCO
───────────────────────────────────────────────────────────────────
SÍNTOMA: un documento se invoca por el nombre con el que se formó
en la conversación, y el nombre nunca existió en el padrón del
disco: archivo que no existe, ruta derivada de memoria, extensión
inventada.
CASO REAL (27-sep-2026): ejecutando la batería E-1 el taller llamó
a «ARCHIVO-4-LADOS-DE-ALEXIS.md»; el filename real es
«ARCHIVO-4-LECCIONES-DE-ALEXIS.md». El intento abortó (FileNotFound
Error) y el taller recuperó el nombre con ls antes de continuar.
Cero daño — y una ficha que creció.
CAUSA RAÍZ: la memoria del taller es generosa con los nombres
formales que suenan bien; el disco es exacto y tacaño.
DETECTOR MÁQUINA: cero nombres se escriben de memoria: cada nombre
sale de ls/glob directo antes de un open.
DETECTOR HUMANO: cuando una ruta cae, preguntar primero «¿de dónde
salió este nombre?» antes de inventar la siguiente.
PREVENCIÓN: la regla «ls antes de nombres» pasa a formar parte de
la estación E2 del motor de autoría.
LECCIÓN: el nombre bonito nunca sustituye al nombre verdadero.

───────────────────────────────────────────────────────────────────
F-082 · LA VARA DE BYTES QUE SE CREYÓ CARACTERES
───────────────────────────────────────────────────────────────────
SÍNTOMA: una medida leída en bytes se cita como si fuese caracteres;
o la inversa. Las cifras parecen plausibles pero pertenecen a
paralelas.
CASO REAL (22-27-sep-2026): el TALLER heredó medidas hechas con
wc -c (bytes); con UTF-8, los caracteres multibyte (emojis, Ō,
flechas) elevan la cuenta. La vara definitiva quedó fijada: len()
de caracteres en UTF-8, única vara, declarada en el padrón del
proyecto cuatro archivos y aplicada desde entonces a cada número.
CAUSA RAÍZ: una vara cambiada sin aviso y dos instrumentos que
piensan distinto.
DETECTOR MÁQUINA: assert de que la vara declarada se usa con
len(archivo) — jamás os.path.getsize, jamás wc -c.
DETECTOR HUMANO: el pulso de la paridad: los números grandes de una
misma pieza no deben sumar diferencias oscuras de un día a otro;
si lo hacen, la vara cambió.
PREVENCIÓN: D-16 actada: «len() UTF-8 única vara» — ninguna otra
medida entra a decisiones.
LECCIÓN: el número honesto empieza por la vara honesta.

───────────────────────────────────────────────────────────────────
F-083 · LA COMILLA QUE PARECÍA LA MISMA (edición por tramos)
───────────────────────────────────────────────────────────────────
SÍNTOMA: una reparación por find-and-replace falla sin error visible
porque la comilla del texto era tipográfica («») y la del patrón
era recta (''), o porque un salto de línea fantasma partía la
frase supuesta.
CASO REAL (22/27-sep-2026): el fix de FB 10 abortó dos veces sin
escritura — el taller suponía una línea continua que el disco
tenía envuelta. La red de seguridad (assert count >= 1 por tramo;
la escritura va al final) avisó a tiempo en las dos ocasiones:
cero daño y mayor confianza.
CAUSA RAÍZ: los `old` derivados de la memoria en vez del archivo
literal.
DETECTOR MÁQUINA: todo `old` se imprime a partir del archivo
abierto (repr) antes de usarlo; el assert falla limpio si no
cuadra.
DETECTOR HUMANO: cuando un tramo no se halla, las guías son:
saltos, comillas, espacios — imprimir el contexto exacto con
slice de 100 caracteres alrededor.
PREVENCIÓN: doc en la estación E4 del motor: assert por tramo,
nada persiste hasta que todos los tramos cierran.
LECCIÓN: el aborto limpio es un éxito de la arquitectura, no un
fracaso de la pluma.

───────────────────────────────────────────────────────────────────
F-084 · EL SUFIJO DE PIERNA QUE EL CONTADOR NO VEÍA (28-BIS)
───────────────────────────────────────────────────────────────────
SÍNTOMA: un instrumento de contador corrige con duplicidad dos
entradas perfectamente distinguibles porque su patrón ignora los
sufijos legítimos de pierna.
CASO REAL (27-sep-2026): la batería E-1 marcó el patrón
«## TREN 28» como duplicado; el segundo encabezado era «## TREN
28-BIS», una pierna legítima del acta que cierra el par 02 con
su propia entrada. Ciego del instrumento; el acta no se tocó.
CAUSA RAÍZ: regex sin contexto: (\d+) no deja espacio a la
arquitectura real (-BIS/-TER/-hh:mm).
DETECTOR MÁQUINA (corregido 27-sep-2026): la enumeración de
trenes acepta sufijos de pierna ordenados tras su base.
DETECTOR HUMANO: cualquier FAIL exige diagnóstico de raíz impreso
antes del toque (regla actada en el tren 37).
PREVENCIÓN: los instrumentos se prueban con su propio instrumento
antes de condenar.
LECCIÓN: el escáner puede ser incapaz de decidir; el juicio tiene
que saber mirar. (Es F-078 vestido de enumeración.)

───────────────────────────────────────────────────────────────────
F-085 · LA CITA ACORRALADA: cuando la evidencia dispara el alarma
───────────────────────────────────────────────────────────────────
SÍNTOMA: tokens documentados como evidencia («el garble era x»)
detonan el barrido anti-garble; el instrumento condena la propia
transparencia.
CASO REAL (27-sep-2026): la batería E-1 marcó «nobody»,
«monstrando», «centradote», «veasis» en la cola del acta — y
cada uno era una cita entrecomillada de la planilla de las 11
reparaciones del volumen V01-A3 sellado hoy. Todo en su sitio:
evidencia entrecomillada, reparada y datada.
CAUSA RAÍZ: el barrido de fichas no distingue uso-vivo de
cita-evidencia.
DETECTOR MÁQUINA (corregido 27-sep-2026): el barrido excluye
tokens entrecomillados o dentro de línea de ledger; cita de
reparación es evidencia, no delito.
DETECTOR HUMANO: antes de la condena, leer el entorno: cita o
síntoma.
PREVENCIÓN: el taller no produce justicia por reflexión, sino
por veredicto.
LECCIÓN: la transparencia no se paga con falsos culpables.

───────────────────────────────────────────────────────────────────
F-086 · EL LEGÍTIMO ASUSTADIZO (los glifos de la casa)
───────────────────────────────────────────────────────────────────
SÍNTOMA: el escáner de caracteres anómalos levanta pánico ante
glifos que son firmas legítimas del taller: Ō, luces •, ┄,
≠, 「」 y los zero-width joiners de los emojis compuestos.
CASO REAL (22-30-sep-2026): heredado del examen de WA 01/02:
los barridos iniciales los levantaban todos como «anómalos»;
la verificación contextual confirmó que son partes del mueble
de la casa (forman títulos, separadores, emojis de familia,
tabla de jerarquía). La lista blanca quedó cerrada y las
variantes quedan controladas.
CAUSA RAÍZ: la anomalía no la define el glifo sino la función
del glifo en su sitio.
DETECTOR MÁQUINA: lista blanca de legítimos — todo glifo fuera
de ella debe necesitar explicación.
DETECTOR HUMANO: leer el entorno antes de condenar; la misma
lección de los árboles de WhatsApp (F-078).
PREVENCIÓN: ningún barrido se presta a la hoguera sin lista
blanca detrás.
LECCIÓN: un taller que condena sus propios adornos se queda
sin casa.

═══════════════════════════════════════════════════════════════════
FIN DEL VOLUMEN 02 (ARCHIVO-3) · 6 fichas vivas, casos 22→27-sep
═══════════════════════════════════════════════════════════════════
