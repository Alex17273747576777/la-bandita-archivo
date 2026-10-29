# MANUAL DE ESTILO VISUAL LA BANDITA — v1.0 · 15-oct-2026

Norma madre del FORMA. El Tratado (D-002 y familia) norma el FONDO y sigue intacto.
Orden que origina este manual [P] del dueño, 15-oct: «volver a recrear cada publicación
desde 0%… tiene que ser una guía no un laberinto… el cerebro humano debe analizarla casi
intuitivamente… emojis que representan el contexto como marcado sutil sin sobresaturación…
mapa fácil de seguir… contador de duración de lectura… #tags al final… un mapa completo de
piezas artesanales».

## 1. DIAGNÓSTICO DEL MEDIO (por qué existía el laberinto)
WhatsApp NO renderiza markdown: `##`, tablas, `---`, `>` y `[texto](url)` se ven como
caracteres crudos — son los muros de texto. SÍ renderiza: *negrita*, _cursiva_,
`código`/```bloques mono```, saltos de línea y emojis nativos. ⇒ Toda pieza se diseña
ÚNICAMENTE con lo que WhatsApp pinta. Nada de markdown de documento.

## 2. LOS CINCO PRINCIPIOS
1. **El ojo camina, el dedo navega.** Una pieza se recorre con el pulgar: cada pantalla
   aporta un hito visible (cabecera de estación, ficha, separador).
2. **Respirar es ley.** Párrafo ≤ 3 líneas de teléfono (≈ 220 c). Línea en blanco entre
   TODOS los bloques. Nunca dos ideas amontonadas.
3. **El emoji es señal, no adorno.** Un emoji por cabecera de estación, según taxonomía
   fija. Máximo 1 dentro de un párrafo. Jamás dos seguidos, jamás muros de emoji.
4. **Los datos van en fichas mono.** Placas, tablas y huellas viven en bloques ``` de
   ≤ 62 columnas y ≤ 12 filas; si es más grande, se parte con subtítulo.
5. **Nada sin fecha ni mapa.** Cada pieza abre con mapa de estaciones y duración; cierra
   con tags de categoría y fuentes fechadas.

## 3. ANATOMÍA DE UNA PIEZA (el mapa completo)
```
PORTADA   título (2 líneas máx) · línea de edición (fecha · nº) ·
          ⏱️ lectura total · ⚡ EN UN RESPIRO (3 líneas) ·
          🗺️ MAPA de estaciones con minutos (bloque mono)
CUERPO    estaciones numeradas, cada una:
            EMOJI *TÍTULO EN NEGRITA*
            · estación N de TOTAL · ~M min de lectura ·
            contenido (párrafos respirables + fichas + ► llamadas)
          separador entre estaciones: ──────────────── (línea fina)
CIERRE    ✍️ veredicto y despedida · línea de banda (para el acta) ·
          #tags · 📎 FUENTES fechadas (1 línea por fuente)
```

## 4. TAXONOMÍA DE EMOJIS (roles fijos en TODAS las piezas)
```
🌱 semilla/apertura      📰 noticia del día       📇 placa/censo
🧭 qué es / qué no es    🎒 funciones/cajones     🇩🇴 lo dominicano
💬 conversación honesta  🔧 instalación/vía sana  📻 canales/actualización
📊 vecindario/comparativa 🔍 verificación tú mismo 🛻 prueba de la vida real
🗣️ preguntas de la gente 📚 biblioteca/documentos  🏭 cómo funciona por dentro
🧾 boleta/veredicto      ⚖️ lo no verificado       ✍️ cierre
📎 fuentes               🗺️ mapa/índice           ⏱️ tiempos de lectura
⚠️ riesgo/letra chica     🕐 fecha/edad de datos    ⚡ resumen instantáneo
```
Semáforo de estado de casas (en placas y vecindarios):
🟢 viva y verificada hoy · 🟡 vigilada (dato fechado) · 🔴 muerta/archivada.
Dentro de párrafos (con mesura): 📍 lugar · ⭐ estrellas · 🔗 enlace · 🎯 clave.

## 5. EL HILO Y LOS MINUTOS
Constante de lectura: **1.100 caracteres/minuto** (≈200 palabras/min en español).
El script de horno mide cada estación (len() del tramo), convierte a minutos (mínimo 1),
los escribe en su cabecera y construye el 🗺️ MAPA con rangos acumulados:
```
 00-03  🌱 La semilla
 03-09  📰 La noticia del día
 ...
 54-57  ✍️ El cierre
```
Cifras medidas o no se declaran: los minutos salen del MISMO script que sella la pieza.

## 6. TAGS DE CATEGORÍA (línea final, orden fijo)
`#LaBandita` + `#Guia` + UNA categoría de estantería + app/casa + país + sellos:
```
Estanterías: #Mapas #Lectores #Musica #Herramientas #Seguridad #Tiendas
             #Llamadas #IA #Galeria #Lanzadores
Sellos:      #FOSS #FuenteFechada #LecturaVerificada #RepublicaDominicana
```
Total: 8 a 10 tags. Nada de nubes: si no identifica categoría, sobra.

## 7. LLAMADAS Y LETRA CHICA
`►` abre una llamada de una línea (dato suelto que merece verse). `⚠️` abre letra
chica obligatoria (riesgos, condiciones). Toda advertencia viaja VISIBLE, nunca escondida.

## 8. CHECKLIST DE HORNO (obligatorio por pieza)
☐ sin `##`, sin `](`, sin tablas markdown  ☐ párrafos ≤ 220 c  ☐ filas mono ≤ 62 c
☐ 1 emoji por cabecera; total emojis razonable  ☐ mapa con minutos reales del script
☐ ⏱️ total en portada  ☐ tags 8-10  ☐ fuentes fechadas  ☐ línea de banda al cierre
☐ barrido de caracteres extranjeros/corruptos  ☐ sello SHA-256 al acta
☐ SIN meta-comentarios de IA ni autorreferencias de fabricación: la
  pieza no habla de sí misma, de cómo fue hecha ni de sus herramientas
  (v1.0.1, 15-oct, orden del dueño tras revisar el prototipo WA 11)
☐ banda D-002 medida en el mismo script

## 9. VIGENCIA
Todas las piezas del catálogo (00→81) se recrean desde 0% bajo este manual, una por
turno con revisión del dueño (prototipo: WA 11). El manual es append-only: cambios de
forma se actan. Forma sin fondo no vale; fondo sin forma, tampoco.
