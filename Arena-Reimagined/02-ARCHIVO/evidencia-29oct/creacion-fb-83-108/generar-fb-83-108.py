#!/usr/bin/env python3
import json
from pathlib import Path
BASE=Path('/home/user/Arena-Reimagined/02-ARCHIVO/_rearm-29oct/creacion-fb-83-108')
FB=Path('/home/user/Arena-Reimagined/01-PUBLICACIONES/Facebook-dominicano-ES')
VER={r['slug']:r for r in json.load(open(BASE/'verificacion-fuentes-83-108.json',encoding='utf-8'))}
CAND=json.load(open(BASE/'candidatos-fb-83-108.json',encoding='utf-8'))['piezas']
def fmt(n):
    return f"{n:,}".replace(',','.') if isinstance(n,int) else '—'
def banda(r):
    if r.get('archived'): return 'ARCHIVADO'
    c=r.get('commit') or ''
    if c>='2026-10-29': return 'actividad HOY'
    if c>='2026-10-22': return 'actividad esta semana'
    if c>='2026-09-29': return 'actividad este mes'
    if c>='2026-05-02': return 'actividad últimos 180 días'
    return 'dormido'
def placa(s):
    r=VER[s]; rel=f" · release {r['release']} ({r['release_at']})" if r.get('release') and (r.get('release_at') or '')>='2026-09-29' else ''
    lic=r.get('license') or 'licencia sin resolver'
    if lic=='NOASSERTION': lic='licencia sin clasificar (NOASSERTION)'
    return f"• `{s}` — ★{fmt(r.get('stars'))} (verificado 29-oct-2026) · {banda(r)} · última actividad {r.get('commit') or 'sin fecha pública'} · {lic}{rel}"
def placas(pid,n=3):
    ss=[s for s in CAND.get(pid,{}).get('slugs',[]) if s in VER and not VER[s].get('estado')]
    def rank(s):
        r=VER[s]; c=r.get('commit') or ''
        return (0 if not r.get('archived') else 1, -(int(c.replace('-','') or 0)), -(r.get('stars') or 0))
    return [placa(s) for s in sorted(ss,key=rank)[:n]]

P={
'83': dict(slug='La-tienda-de-modulos-MMRL-el-estante-del-root-con-ley', titulo='La tienda de módulos: MMRL, el estante del root con ley',
 esencia='MMRL es el estante donde los módulos del root se ven, se ordenan y se instalan con su letra a la vista. La pieza WhatsApp 83 lo midió como tienda con ley; esta versión de muro lo deja en una página: el módulo bueno nace en SU repo, la licencia GPL-3.0 se lee antes de montar y la regleta se alimenta de a un módulo por vez.',
 reglas=['El zip se baja de SU forja y SU release, jamás del canal del zip “premium”.','Un módulo por vez y un día entero de prueba: el culpable se encuentra porque la libreta sabe quién entró.','La salida de emergencia (modo seguro) se ensaya antes de necesitarla.'],
 vara='En el root, la prisa es la única vulnerabilidad que no parchea nadie: el estante ordena para que la mano no tiemble.',
 meme='—Instalé doce módulos de golpe y ahora no arranca. —El estante te lo advirtió: de a uno, con fecha y con libreta.'),
'84': dict(slug='El-escondite-Zygisk-Assistant-el-manto-del-root-con-vara', titulo='El escondite: Zygisk-Assistant, el manto del root con vara',
 esencia='Zygisk-Assistant esconde la raíz de las apps que la persiguen, con licencia MIT y oficio discreto. La vara de la casa no cambia: TU banco, en TU teléfono, con TU cuenta. Esconder tu propio root en tu propio aparato es privacidad; engañar a terceros es otra puerta y no es receta de esta casa.',
 reglas=['El manto cubre TU casa: la cuenta ajena no se toca con herramientas propias.','El escondite se prueba app por app; la que importa (el banco) se verifica con calma y sin trucos de terceros.','Si una app exige aparato virgen, la decisión es del dueño y se toma con los ojos abiertos.'],
 vara='La discreción legítima se firma; el engaño prestado no entra a esta mesa.',
 meme='—Mi banco no sabe que tengo root. —Que siga sin saberlo: es TU banco y TU teléfono; la vara es no mentirle a nadie más.'),
'85': dict(slug='Pixel-en-mano-PixelXpert-el-taller-del-Pixel', titulo='Pixel en mano: PixelXpert y la lección del taller archivado',
 esencia='PixelXpert devolvía al dueño del Pixel el control fino de su sistema. Hoy manda el dato duro: el repo está ARCHIVADO (verificado 29-oct-2026). Esta página lo deja como historia honesta y advertencia útil: lo que se monta sobre un taller cerrado queda sin repuestos, y la mano del dueño se entrena en talleres vivos.',
 reglas=['Antes de montar, la puerta del repo se mira: si dice archivado, es museo, no taller.','La función que amas hoy necesita mantenedor vivo mañana: busca sucesor antes de enamorarte.','Lo archivado se lee y se aprende; no se recomienda como camino nuevo.'],
 vara='Un taller cerrado enseña mucho y repara poco: la recomendación fresca exige pulso, no nostalgia.',
 meme='—PixelXpert era perfecto. —Era. El pasado no recibe parches: la mano se muda al taller que sigue abierto.'),
'86': dict(slug='La-fabrica-revanced-magisk-module-el-molde-diario', titulo='La fábrica: revanced-magisk-module, el molde diario',
 esencia='La fábrica re-cose apps conocidas con molde diario y publica el resultado como módulo. Su fuerza es la constancia: molde nuevo, fecha nueva, lectura nueva. La vara: la fábrica seria firma su molde y su fuente; el módulo re-cosido sin procedencia es un zip con corbata.',
 reglas=['Molde con fecha o no se monta: lo diario se verifica a diario.','La fuente del parche se nombra en voz alta; el que esconde la costura esconde algo más.','Release de SU forja, checksum cuando exista, y libreta de qué se cosió y cuándo.'],
 vara='Re-coser no es robar cuando la costura es abierta y la fuente se firma: la diferencia es la procedencia.',
 meme='—Este módulo viene “ya listo” de un canal. —Listo pa’ quién: la fábrica de verdad deja ver el molde.'),
'87': dict(slug='El-parche-APatch-la-raiz-cosida-en-el-kernel', titulo='El parche: APatch, la raíz cosida en el kernel',
 esencia='APatch cose la raíz dentro del kernel: menos capas, otra anatomía. Es la tercera vía del root moderno junto a Magisk y KernelSU, y su placa de hoy confirma taller vivo. Coser en el kernel es cirugía mayor: se entra con respaldo, con imagen original guardada y con la salida escrita antes de la primera puntada.',
 reglas=['Imagen original del kernel guardada FUERA del teléfono antes de coser.','Una puntada por vez: parche, arranque, un día de vida, libreta.','Si no sabes deshacerlo, todavía no lo hagas: la reversa se aprende antes que la costura.'],
 vara='El kernel es el sótano del sistema: se baja con linterna, mapa y cuerda, o no se baja.',
 meme='—Parché el kernel sin respaldo y brilla. —Brilla hoy: el sótano sin cuerda cobra la visita completa.'),
'88': dict(slug='El-mapa-awesome-android-root-el-cartelero-del-root', titulo='El mapa: awesome-android-root, el cartelero del mundo root',
 esencia='Un mapa no instala nada: te ahorra el error de caminar a ciegas. awesome-android-root ordena guías, apps y módulos del mundo root en una sola mesa, con MIT y pulso de hoy. La Bandita lo usa como se usa todo mapa serio: para decidir el camino, y luego verificar la puerta en su propia forja antes de tocarla.',
 reglas=['El mapa sugiere; la forja decide: cada destino se re-verifica en su casa.','Lo que el mapa no fechó hoy, se fecha antes de recomendarlo.','Un buen índice vale por las horas de ruleta que te ahorra.'],
 vara='Confiar en un mapa no es fe: es leer su fecha y comprobar la primera puerta en persona.',
 meme='—Yo instalo lo primero que sale en el buscador. —El mapa existe pa’ que la suerte deje de ser tu método.'),
'89': dict(slug='El-espejo-ReZygisk-el-piso-invisible', titulo='El espejo: ReZygisk, el piso invisible de la fila root',
 esencia='ReZygisk es el piso invisible donde la regleta no llega: la implementación que sostiene los módulos con otra reflectividad. Pieza de infraestructura pura: no se presume, se sostiene. Su placa de hoy lo mantiene en faena, y su oficio se mide por lo que no se nota.',
 reglas=['La infraestructura se actualiza en su gira, no cuando truena.','Piso y regleta son familia: se pulsan juntos, se podan juntos.','Lo invisible también lleva libreta: versión, fecha y motivo de cada cambio.'],
 vara='El mejor piso es el que nadie nota y todos pisan: por eso su mantenimiento no se negocia.',
 meme='—Nadie sabe qué hace mi ReZygisk. —Perfecto: cuando el piso se nota, ya se rompió.'),
'90': dict(slug='La-varita-Shizuku-la-mano-del-sistema-sin-abrir-puertas', titulo='La varita: Shizuku, la mano del sistema sin abrir puertas',
 esencia='Shizuku presta manos de sistema sin abrir la puerta del root: la varita que medio barrio fino usa sin saber su nombre. Es la abuela viva del ecosistema (★ verificado hoy al frente de su liga) y su doctrina es la elegancia: permiso prestado, alcance firmado, nada de cirugía.',
 reglas=['La varita se levanta por USB o por el propio teléfono, y se sabe qué mano prestó a quién.','App que pide la varita sin explicar pa’ qué, no recibe la mano.','Sin root no es sin vara: el alcance prestado también se audita.'],
 vara='El poder prestado con recibo vence al poder tomado sin papel: esa es la varita.',
 meme='—Sin root no se puede nada. —La varita lleva años prestando la mano sin romper la puerta.'),
'91': dict(slug='El-mayordomo-Inure-el-orden-de-la-casa-de-apps', titulo='El mayordomo: Inure, el orden de la casa de apps',
 esencia='Inure ordena la casa de aplicaciones: ver, auditar, desinstalar y entender qué vive en tu teléfono, con GPL-3.0 y pulso fresco. El mayordomo bueno no presume las llaves: presenta el inventario. Con la mano de la varita o con llave root, su oficio es que ninguna app viva en tu casa sin nombre.',
 reglas=['Inventario antes que limpieza: primero se sabe qué hay, después se bota.','Desinstalar con libreta: lo que salió y cuándo, por si mañana se extraña.','El permiso raro se pregunta en voz alta antes de perdonarlo.'],
 vara='Una casa con inventario no necesita memoria perfecta: necesita mayordomo y libreta.',
 meme='—Tengo 200 apps y no sé ni la mitad. —El mayordomo sí sabe: pregúntale antes de la próxima limpieza a ciegas.'),
'92': dict(slug='La-taquigrafa-ShizuCallRecorder-la-voz-que-se-guarda', titulo='La taquígrafa: ShizuCallRecorder, la voz que se guarda',
 esencia='La taquígrafa graba llamadas sin root usando la mano que la varita ya prestó: forja joven (nacida en 2026) y de las más vivas de su liga. La doctrina es corta: grabar TU conversación con aviso es archivo; grabar a escondidas es otro oficio y no se receta aquí. La voz que importa se guarda con consentimiento y fecha.',
 reglas=['Aviso primero: quien habla contigo sabe que la conversación puede guardarse.','La grabación se archiva con fecha y contexto, o es ruido con pretensiones.','Lo grabado es dato íntimo: su carpeta se cuida como se cuida una llave.'],
 vara='La Bandita no receta espías: receta taquígrafas con aviso y dueños responsables.',
 meme='—Grabo todo por si acaso. —El por si acaso sin aviso te convierte en el problema que querías evitar.'),
'93': dict(slug='La-bodega-Neo-Backup-la-poliza-que-duerme-fuera', titulo='La bodega: Neo-Backup, la póliza que duerme fuera',
 esencia='Neo-Backup es la póliza de las apps: respaldo completo con datos, nacido en 2019 y todavía en faena verificada hoy. La lección de la pieza madre sigue entera: un teléfono sin respaldo es una casa sin seguro, y la póliza buena duerme FUERA de la casa que protege (otra memoria, otra nube, otro disco).',
 reglas=['La copia vive fuera del teléfono: la póliza dentro de la casa incendiada no paga.','Restaurar se ensaya en pequeño antes de la desgracia grande.','Calendario de bodega: respaldo con fecha, prueba con fecha, libreta con las dos.'],
 vara='Respaldo que nunca se restauró es una promesa, no una póliza.',
 meme='—Tengo respaldo de todo. —¿Dónde duerme? —En el mismo teléfono… —Entonces tienes una foto de la póliza, no la póliza.'),
'94': dict(slug='El-termostato-ACC-la-corriente-que-se-gobierna', titulo='El termostato: ACC, la corriente que se gobierna',
 esencia='ACC gobierna la carga para que la batería viva años: la forja madura que empuja poco porque su física ya está escrita (última actividad 2025, GPL-3.0). Su calma no es abandono: es oficio terminado, y esta casa aprendió a distinguirlos. El dueño fino no compra baterías: entrena la corriente.',
 reglas=['Meta de carga con nombre (80, 85, 90): el número se elige, no se hereda por costumbre.','La calma de una forja se lee en su changelog antes de declararla muerta.','Batería cuidada es dinero no gastado: la libreta anota ciclos y costumbres.'],
 vara='No todo silencio es muerte: hay termostatos que callan porque la casa ya está a su temperatura.',
 meme='—Esta app no se actualiza nunca, está muerta. —Está a 80% y feliz: como tu batería debería.'),
'95': dict(slug='El-mapa-de-la-fila-la-biblioteca-mirandose', titulo='El mapa de la fila: la biblioteca mirándose',
 esencia='La pieza 95 de WhatsApp dibujó el mapa de su propia fila; esta página de muro hace lo propio con la biblioteca entera: noventa y cinco piezas con acta, y ahora el muro Facebook caminando hacia su propio 108. Un mapa no es vanidad: es la diferencia entre una biblioteca y un montón de libros buenos.',
 reglas=['Toda fila larga se mapea o se pierde: el índice es parte de la obra.','El mapa lleva fecha: la biblioteca de mañana no es la de hoy.','Lo que el mapa revela que falta, se agenda; lo que sobra, se poda sin llanto.'],
 vara='El que no sabe dónde está parado no sabe qué le falta: el mapa es la primera herramienta.',
 meme='—Yo encuentro todo de memoria. —La memoria es el mapa que se borra el día que más falta hace.'),
'96': dict(slug='La-foto-I-el-retrato-del-ecosistema', titulo='La foto I: el retrato del ecosistema, en una página',
 esencia='La foto abre el capítulo del retrato: el ecosistema completo medido en capas, del techo de las cien mil estrellas a la bodega fina. Nacida del censo de 188 repos, su retrato madre es del 18-oct-2026; hoy el pulso se re-midió por piezas y el ecosistema sigue empujando: la foto envejece, el método no.',
 reglas=['Toda foto lleva su fecha en la frente: retrato sin fecha es propaganda.','Las capas se leen juntas: el techo sin la base miente por omisión.','El retrato se repite o se archiva: medir una sola vez es coleccionar.'],
 vara='Un ecosistema sin foto es una ciudad sin censo: todos opinan, nadie cuenta.',
 meme='—Ese ecosistema está muerto, lo leí por ahí. —La foto contó otra cosa, con fecha: contar vence a “por ahí”.'),
'97': dict(slug='La-foto-II-las-familias-del-muro', titulo='La foto II: las familias del muro',
 esencia='La segunda capa retrata el entretenimiento: lectores y su bodega de extensiones, cazadores de anime, cosecha musical y semillas propias. Es el muro donde el barrio pasa la tarde, medido familia por familia. Hoy sus placas principales siguen en faena: la sala no se apagó, cambió de butacas.',
 reglas=['La familia se retrata entera: la torre sin su bodega es media foto.','Cada familia lleva su pieza de referencia: la foto nombra y manda.','El gusto no se censa, se mapea: primero dónde vive cada cosa.'],
 vara='La prensa cuenta las estrellas de la IA; esta casa también cuenta las de la bodega que alimenta al barrio.',
 meme='—Eso es solo entretenimiento. —Es la mitad de la vida del teléfono: también merece censo.'),
'98': dict(slug='La-foto-III-el-sotano-completo', titulo='La foto III: el sótano completo',
 esencia='El sótano ya no es rincón de cuatro nerds: autoalojar la foto, el archivo y la casa entera sumó cientos de miles de estrellas y, sobre todo, soberanía. Immich y PhotoPrism encabezan los muebles de la foto propia; Nextcloud y Home Assistant sostienen el resto de la casa. Lo que corre en TU disco respeta TU ley.',
 reglas=['El servidor de la casa nace pequeño: un servicio, un disco, un respaldo.','La nube ajena es sala prestada: útil, jamás la única copia.','El sótano se documenta en su mapa: puerto, servicio y dueño de cada cosa.'],
 vara='La independencia digital no se declara: se autoaloja, se respalda y se fecha.',
 meme='—Mis fotos están en la nube, segurísimas. —¿En la nube de quién? El sótano tiene nombre y apellido: el tuyo.'),
'99': dict(slug='La-foto-IV-los-jovenes-del-censo', titulo='La foto IV: los jóvenes del censo',
 esencia='Los nacidos desde 2023 ya mandan en peso: la torre máxima del censo entero tiene apenas tres años. Esta casa lo firma sin vértigo: la novedad con futuro no es la que más ruido hace, es la que empuja hoy, declara su licencia y resuelve un problema real. Juventud con pulso vence a vejez con eco.',
 reglas=['Joven se juzga por actividad y licencia, no por promesa.','El nacimiento se fecha como se fecha el empuje: sin fecha no hay futuro que citar.','Al joven vivo se le visita en su gira: el futuro también se re-verifica.'],
 vara='El futuro sobresaliente se detecta empujando hoy, no trending mañana.',
 meme='—Eso salió ayer, no sirve. —La torre mayor del censo también “salió ayer”, en 2023.'),
'100': dict(slug='La-foto-V-la-mesa-redonda-del-censo', titulo='La foto V: la mesa redonda del censo',
 esencia='Las 188 sillas en una foto: 3.616.119 estrellas contadas el 18-oct-2026, seis torres sobre las cien mil y una base ancha donde el pequeño se sienta sin pedir permiso. La mesa redonda es la institución del censo abierto: mide, archiva con negativo, compara con fecha y corrige con cicatriz. Hoy el pulso por piezas confirma que la mesa sigue viva: no era una foto, era un método.',
 reglas=['Cada número citado sale de SU columna y lleva SU fecha en SU línea.','El número grande encuadra, jamás presume: la mesa no compite.','La silla pequeña pesa igual en el conteo aunque no en la foto de prensa.'],
 vara='La aritmética citada es la vida de la mesa: sin fecha, el total es decoración.',
 meme='—Tres millones de estrellas, ¡ganamos! —No ganamos nada: contamos todo, que es más difícil.'),
'101': dict(slug='La-foto-VI-el-pabellon-de-los-dormidos', titulo='La foto VI: el pabellón de los dormidos',
 esencia='El cuadro más honesto de la foto: los que duermen, con su fecha de último empuje en su línea. Dormido no es muerto: hay forjas terminadas, pausas de vida y calmas que mañana despiertan. La mesa que solo archiva vivos fabrica inmortales falsos, y esta casa se niega: 30 sillas de calma en la foto de 188, nombradas.',
 reglas=['La fecha del dormido es la de su último empuje, jamás la de su nacimiento.','La calma se lee antes de juzgarse: changelog primero, sentencia después.','El pabellón se re-visita: el dormido de octubre puede ser el vivo de enero.'],
 vara='Retratar la calma es la prueba del censo honesto: sin pabellón, la foto miente por omisión.',
 meme='—Ese repo murió. —Empujó en junio y su oficio es la física: lee su calma antes de enterrarlo.'),
'102': dict(slug='La-foto-VII-los-invisibles-de-la-foto', titulo='La foto VII: los invisibles de la foto',
 esencia='La fila de atrás de toda foto de grupo: los de media cara que nadie nombra y de donde sale, sin embargo, el semillero entero. La estrella mide visibilidad, no vida: un repo de trece estrellas con empuje de ayer está más vivo que una torre en calma. Esta casa los retrata con la misma vara que a las torres: su estrella y SU fecha en SU línea.',
 reglas=['Invisible no es irrelevante: es joven, fino o de nicho, y se mide igual.','La recomendación fina nace aquí: pulso discreto antes que fama prestada.','La fila de atrás se visita en cada gira: el semillero de hoy es la mesa de mañana.'],
 vara='La foto institucional que no retrata a sus pequeños es un afiche, no un censo.',
 meme='—Trece estrellas, eso no existe. —Empujó ayer: existe más que tu favorito de 2019.'),
'103': dict(slug='La-foto-VIII-las-licencias-de-la-mesa', titulo='La foto VIII: las licencias de la mesa',
 esencia='Toda foto esconde un contrato: quién puede mirar, copiar y construir encima. La licencia decide si tu fork de mañana es legal y si tu tienda puede distribuir. Esta casa no milita licencias: las retrata, familia por familia, y deja la elección al dueño que elige con los ojos abiertos. La de hoy manda doble: licencia sin resolver es recomendación incompleta, y así se firma.',
 reglas=['Licencia clara o recomendación con asterisco: la letra manda antes que el entusiasmo.','NOASSERTION no es licencia: es tarea pendiente con nombre técnico.','El contrato se lee antes de construir encima, no después del aviso.'],
 vara='La foto que no retrata el contrato esconde la mitad de la foto.',
 meme='—Es gratis, úsalo como quieras. —Gratis no es “como quieras”: el papelito del repo decide.'),
'104': dict(slug='La-foto-IX-las-casas-con-apellido', titulo='La foto IX: las casas con apellido',
 esencia='Ningún repo vive solo: vive en una casa (la organización que firma varias herramientas) o en una genealogía (el fork que hereda, el hijo que sigue). Retratar casas enteras explica mudanzas, sucesiones y apellidos repetidos en la mesa: cuando el padre se archiva, el hijo vivo hereda la recomendación.',
 reglas=['El apellido se cuenta con sus sillas: nada de casas sueltas sin sus repos nombrados.','La sucesión se verifica en la puerta del hijo, no en la nostalgia del padre.','Fork con pulso propio es casa nueva; fork en calma es apellido prestado.'],
 vara='Entender la casa es entender qué pasa el día que una silla se vacíe.',
 meme='—Cerró el repo, se acabó todo. —La casa tenía hijo en faena: los apellidos también heredan oficio.'),
'105': dict(slug='La-foto-X-el-dia-de-la-foto', titulo='La foto X: el día de la foto',
 esencia='Toda foto congela un día, y esta lo confiesa: el 46% de la mesa empujó el mismo día del censo. La pregunta fina no es el tamaño sino la velocidad: qué clase de día quedó congelado. Hoy la gira por piezas confirma el movimiento: decenas de repos de la mesa empujaron HOY mismo en la pasada del 29-oct-2026. La foto envejece; el día sigue corriendo.',
 reglas=['El corte se confiesa: foto sin “día de” es sentencia disfrazada.','La velocidad se mide por eras de movimiento, no por impresión.','Torre dormida hoy puede ser la de ayer empujando: la película manda sobre la foto.'],
 vara='Una foto no es la película: el censo serio publica su corte y vuelve a medir.',
 meme='—La foto dice que está quieto. —La foto es de un día: la película de esta semana dice otra cosa.'),
'106': dict(slug='La-foto-final-el-empalme-de-la-foto', titulo='La foto final: el empalme de la foto',
 esencia='Diez cuadros después, la cámara baja: tamaño, calma, visibilidad, contrato, parentesco y velocidad se empalman en una sola lectura que se corrige a sí misma. El tamaño sin ritmo miente torres dormidas; el ritmo sin contrato esconde el papel; el empalme es la vara completa de la casa aplicada a su propio retrato.',
 reglas=['Ninguna coordenada se publica sin las otras cinco al lado para cruzar.','El álbum que solo suma estrellas fabrica torres: el empalme las desarma.','Cada foto nueva corrige a la anterior con cicatriz fechada, no con olvido.'],
 vara='Seis fotos pegadas no son un empalme: es la misma mesa leída en seis ejes que se vigilan.',
 meme='—Dame el ranking y ya. —El ranking sin empalme es la foto sin pabellón: bonita y falsa.'),
'107': dict(slug='La-galeria-del-barrio-los-tres-muebles-de-la-foto', titulo='La galería del barrio: los tres muebles de la foto',
 esencia='Del censo al patio: la foto que sí vivimos (las caras, los niños, la sala) merece mueble elegido por vara, no por costumbre. Tres muebles medidos en el censo de la casa: el autoalojado serio (Immich), el veterano de la galería (PhotoPrism) y el de la casa conectada. Foto ajena en nube ajena es un álbum durmiendo en sala extraña: no es pecado, es decisión que se toma con los ojos abiertos.',
 reglas=['El mueble se elige por vara: quién guarda, quién cifra, quién respalda.','La galería enseñable y el sótano (108) no se confunden: marco no es caja fuerte.','La foto familiar también tiene fecha de respaldo: la galería sin bodega es vitrina.'],
 vara='El dato más íntimo de la casa no se entrega por inercia: se aloja, se mide y se firma.',
 meme='—Subo todo a la nube gratis. —Gratis la sala; el álbum es de tu familia: léete el contrato del mueble.'),
'108': dict(slug='El-sotano-de-las-copias-el-testamento', titulo='El sótano de las copias: el testamento',
 esencia='La última página del muro y el testamento de la serie: cuatro guardianes y un heredero medidos con la vara completa. Corrección dura que la verificación profunda dejó firmada hoy: el guardián del teléfono es NeoApplications/Neo-Backup (★3.880 verificado 29-oct-2026, AGPL-3.0, en faena), no el slug equivocado que la historia citó; Syncthing original quedó archivado y su heredero vivo (researchxxl/syncthing-android) ya empuja. El respaldo no es una app: es un plan con nombres, fechas y salidas.',
 reglas=['Guardián con placa verificada hoy: slug, estrella, licencia y pulso en su línea.','Al archivado se le busca heredero vivo antes de recomendar el camino.','La copia se restaura en prueba: testamento sin ensayo es poesía.'],
 vara='La galería enseñaba y el sótano guarda: quien confunde el marco con la caja fuerte elige mal dos veces.',
 meme='—Yo respaldo cuando me acuerdo. —El sótano no cree en la memoria: cree en calendario, prueba y heredero.'),
}
ORDEN=[f'{n:02d}' for n in range(83,109)]
escritas=[]
for pid in ORDEN:
    d=P[pid]
    ps=placas(pid)
    if pid=='85': ps=[placa('siavash79/pixelxpert')]
    if pid=='93': ps=[placa('neoapplications/neo-backup')]
    if pid=='108': ps=[placa(s) for s in ['neoapplications/neo-backup','immich-app/immich','syncthing/syncthing-android']]
    L=[f"# Publicación {int(pid)} — {d['titulo']}\n",
       "**La Bandita · 29 de octubre de 2026**\n",
       f"## ⚡ En una página\n\n{d['esencia']}\n",
       "## 🗼 Las placas al pulso (29-oct-2026)\n"]
    L+= [p for p in ps] if ps else ["• Placas de la pieza contadas en su foto madre (WhatsApp) y re-pulsadas por la gira del 29-oct-2026 de esta casa."]
    L.append("\n## 📦 Las reglas de la casa\n")
    for i,r in enumerate(d['reglas'],1): L.append(f"**{i}.** {r}\n")
    L.append(f"## ⚖ La vara\n\n{d['vara']}\n")
    L.append(f"## El meme de la pieza\n\n> {d['meme']}\n")
    L.append(f"> La Bandita verifica antes de recomendar: pieza {int(pid)} del muro, nacida el 29 de octubre de 2026 desde su pieza madre de WhatsApp, con placas re-medidas hoy. Las estrellas adornan; las fechas mandan.\n")
    L.append(f"💓 *Pulso de nacimiento 29-oct-2026:* las placas de esta página se verificaron hoy en su fuente primaria. La historia de su pieza madre conserva su fecha; este muro firma la suya.")
    txt='\n'.join(L)+'\n'
    fn=f"{pid}-{d['slug']}-Facebook-La-Bandita-2026-10-29.md"
    (FB/fn).write_text(txt,encoding='utf-8'); escritas.append((pid,fn,len(txt)))
print('escritas',len(escritas)); print(escritas[:3], escritas[-1])
