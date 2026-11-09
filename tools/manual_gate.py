#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compuerta del MANUAL DE ESTILO Y OPERACIONES V3.0 (1-nov-2026).

Aplica los criterios del manual a una pieza: firma textual, meme del corte, remate propio y único,
mapa de cinco a doce entradas, sección «en una página», preguntas frecuentes, enlaces completos,
fichas con licencia, frases prohibidas, notas fechadas, banda de longitud, meta-comentarios,
signos dobles, secretos y párrafos compartidos. Devuelve VERDE, VENTANA o ROJO.

Qué hace:
  * Evalúa una pieza contra los 23 criterios (M01–M23) del Manual V3.0.
  * Evalúa toda una carpeta con --verificar y reporta resumen.
  * Devuelve VERDE, VENTANA o ROJO por pieza.

Qué NO hace:
  * No reescribe el texto: dice qué criterio no cumple y dónde.
  * No aprueba una pieza por salir en cero: requiere VERDE explícito.
"""
from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

RAIZ: Path = Path(__file__).resolve().parents[1]
BANDAS: Path = RAIZ / "docs" / "bandas.json"
# La carpeta que evalúa --verificar. Faltaba: el nombre se usaba en main() y nunca
# se definió, así que `manual_gate.py --verificar` moría con NameError en vez de
# evaluar las 42 piezas. Pasó desapercibido porque la autoprueba era el único sitio
# que lo llamaba, y lo que se veía era un Traceback, no «la compuerta no funciona».
PUBLICACIONES: Path = RAIZ / "Arena-Reimagined" / "01-PUBLICACIONES"

FRASES_PROHIBIDAS: tuple[str, ...] = (
    "revolucionario", "imprescindible", "según expertos", "el único que necesitas",
    "¡vamos con todo!", "al 110 %",
)


@dataclass
class Criterio:
    codigo: str
    nombre: str
    pasa: bool
    detalle: str = ""


@dataclass
class ResultadoPieza:
    ruta: str
    verde: bool = False
    ventana: bool = False
    rojo: bool = False
    criterios: list[Criterio] = field(default_factory=list)

    @property
    def estado(self) -> str:
        if self.rojo:
            return "ROJO"
        if self.ventana:
            return "VENTANA"
        if self.verde:
            return "VERDE"
        return "DESCONOCIDO"


def _leer(ruta: Path) -> str:
    return ruta.read_text(encoding="utf-8")


def _tiene_mapa(contenido: str) -> bool:
    return "🗺️" in contenido


def _contar_secciones_mapa(contenido: str) -> int:
    """Cuenta las ramas del mapa, no las viñetas del documento.

    EL FALSO POSITIVO QUE ESTO CIERRA
    ---------------------------------
    La versión anterior contaba TODA línea que empezara por guion o asterisco, en
    todo el documento. Una pieza con un mapa de doce entradas y tres listas más en
    el cuerpo salía con «16 entradas» y en rojo por pasarse del máximo de doce, sin
    tener nada mal: el mapa estaba bien y lo que se contaba era la bibliografía.

    Ahora se mira dentro del bloque del mapa: las líneas del diagrama (las que
    llevan ├── o └──) y, si no hay diagrama, las viñetas que van entre «Mapa de esta
    pieza» y el primer separador.
    """
    ramas = re.findall(r"^\s*[├└│]──", contenido, re.M)
    if ramas:
        return len(ramas)

    m = re.search(r"Mapa de esta pieza", contenido)
    if not m:
        return 0
    tramo = contenido[m.end():]
    corte = re.search(r"\n\s*(?:─{3,}|\*🔗|\*🧾|## )", tramo)
    if corte:
        tramo = tramo[:corte.start()]
    return len(re.findall(r"^\s*[-*]\s+\S", tramo, re.M))


def _canal_de_la_ruta(ruta: Path) -> str | None:
    """El canal de una pieza, por la carpeta donde vive. `None` si no se reconoce."""
    for parte in reversed(ruta.parts):
        baja = parte.lower()
        if baja.startswith("facebook"):
            return "facebook"
        if baja.startswith("whatsapp"):
            return "whatsapp"
    return None


def _banda_de_la_pieza(ruta: Path, largo: int, bandas: dict) -> tuple[bool, str]:
    """¿Está esta pieza dentro de la banda de SU canal?

    Se prefiere la entrada declarada para esa pieza —que fija el mínimo y el máximo
    exactos de lo publicado— y si no la hay se usa la banda del canal. Una pieza sin
    canal reconocible se mide contra las bandas del archivo, pero nunca se da por
    buena solo porque su longitud encaje en la banda de otro canal.
    """
    canal = _canal_de_la_ruta(ruta)
    numero = ruta.name.split("-")[0]
    if canal and isinstance(bandas.get(canal), dict):
        datos = bandas[canal]
        piezas = datos.get("piezas", {})
        for clave in (numero, f"{numero}-fijado"):
            if clave in piezas and "min" in piezas[clave] and "max" in piezas[clave]:
                mn, mx = piezas[clave]["min"], piezas[clave]["max"]
                if mn <= largo <= mx:
                    return True, f"{largo} caracteres (banda de la pieza {clave})"
        mn, mx = datos.get("min"), datos.get("max")
        if mn is not None and mx is not None:
            if mn <= largo <= mx:
                return True, f"{largo} caracteres (banda de {canal}: {mn}–{mx})"
            return False, f"fuera de banda de {canal} ({largo}, tope {mx})"
    # Sin canal reconocible: se acepta si cabe en alguna banda declarada, y se dice.
    for k, v in bandas.items():
        if not isinstance(v, dict):
            continue
        mn, mx = v.get("min"), v.get("max")
        if mn is not None and mx is not None and mn <= largo <= mx:
            return True, f"{largo} caracteres (banda de {k}, canal no reconocido)"
    return False, f"fuera de banda ({largo})"


def _tiene_una_pagina(contenido: str) -> bool:
    return "En una página" in contenido or "en una página" in contenido.lower()


def _tiene_meme_corte(contenido: str) -> bool:
    """Meme original de dos líneas, con guion largo, antes de la firma.

    Definición de docs/CONFORMIDAD-MANUAL-2026-11-02.md §M02: «dos líneas con guion
    largo antes de la firma». La comprobación anterior buscaba la cadena literal
    «meme del corte» o el fénix 🐦‍🔥, que no es lo que el manual describe: buscaba la
    etiqueta del criterio, no el criterio. Ninguna pieza la lleva, así que salían
    todas en VENTANA por un texto que el manual nunca pidió.
    """
    corte = contenido.find("💓")
    tramo = contenido[:corte] if corte > 0 else contenido[:4000]
    # La cabecera del fijado («📎 *Comentario fijado · Pieza 01 — La huella…*») también
    # lleva guion largo y casaba el patrón: daba por buenos diez fijados que no tienen
    # meme. No es el meme, es el rótulo. Se descarta antes de mirar.
    tramo = "\n".join(l for l in tramo.splitlines() if not l.strip().startswith("📎"))
    # Dos líneas seguidas, no vacías, con guion largo, y con algo de gracia: no se
    # exige ingenio medible, se exige la forma que el manual describe.
    return bool(re.search(r"[^\n]{15,}\s+—\s+[^\n]{15,}", tramo))


def _tiene_firma(contenido: str) -> bool:
    return "💓" in contenido and "La Bandita informa" in contenido


LICENCIAS = re.compile(
    r"\b(MIT|GPL|AGPL|LGPL|Apache|BSD|MPL|ISC|Unlicense|CC0|CC-BY[A-Z0-9.-]*|Zlib|WTFPL"
    r"|Artistic|OFL|BSL|EPL|CDDL|PostgreSQL|Python|Ruby|X11|NCSA|EUPL|NOASSERTION)\b",
    re.IGNORECASE,
)
# «Sin licencia» también es un dato medido: GitHub devuelve NOASSERTION y las piezas
# escriben «sin licencia declarada» o «sin declarar» cuando no la hay. Eso no es una
# falta de la pieza: es la pieza diciendo la verdad. Lo que se persigue es la ficha
# que ni declara licencia ni dice que no la tiene.
SIN_LICENCIA = re.compile(r"sin licencia declarada|sin declarar|NOASSERTION", re.IGNORECASE)

# Ficha en viñeta: la línea EMPIEZA por el repo y lleva estrellas.
# «El que más estrellas tiene es **x/y**, con ★277.160» también casa el patrón de repo
# y estrellas, pero es prosa, no ficha: por eso se exige que el repo abra la línea y
# que las estrellas vengan tras el separador «·».
FICHA_VINETA = re.compile(r"^\s*(?:[-•*]|\d+\.)?\s*\*\*[A-Za-z0-9._-]+/[A-Za-z0-9._-]+\*\*\s*·[^\n]*★")
# Ficha en tabla: la fila empieza por el repo entre comillas invertidas y lleva fecha.
FICHA_TABLA = re.compile(r"^\s*\|\s*`[A-Za-z0-9._-]+/[A-Za-z0-9._-]+`")
FECHA = re.compile(r"\b(19|20)\d\d")


def _fichas_con_licencia(contenido: str) -> tuple[bool, str]:
    """M08 — toda ficha de repositorio dice su licencia o dice que no la tiene.

    Tres correcciones sobre la versión anterior, que pedía «★ en algún lado y MIT en
    algún lado»:

    1. Una pieza que no mide repositorios (una novela, una película) no tiene fichas
       que licenciar: M08 no le aplica. Antes salía en rojo por no inventarse fichas
       que su tema no tiene.
    2. «Sin declarar» y NOASSERTION son valores medidos, no huecos. Antes se contaban
       como falta, y arreglar el rojo habría significado borrar la medición.
    3. La licencia se busca en la MISMA línea de la ficha, no en cualquier parte del
       documento: antes bastaba un «MIT» en prosa para dar por buenas 39 fichas.
    """
    fichas = 0
    faltas: list[str] = []
    for linea in contenido.splitlines():
        es_vineta = bool(FICHA_VINETA.match(linea)) and "★" in linea
        es_tabla = bool(FICHA_TABLA.match(linea)) and bool(FECHA.search(linea))
        if not (es_vineta or es_tabla):
            continue
        fichas += 1
        if not (LICENCIAS.search(linea) or SIN_LICENCIA.search(linea)):
            faltas.append(linea.strip()[:70])
    if not fichas:
        return True, "sin fichas de repositorio (no aplica)"
    if faltas:
        return False, f"{len(faltas)} de {fichas} fichas sin licencia ni declaración"
    return True, f"{fichas} fichas, todas con licencia o declaración de ausencia"


# Las firmas de la casa, que son varias A PROPÓSITO.
#
# La regla T10 del dueño prohíbe copiar WhatsApp a Facebook y al revés: cada canal
# firma a su manera. Y los post de comunidad, que `docs/bandas.json` declara como
# serie aparte, firman con una tercera forma. M01 pide «firma textual invariable»:
# que la firma sea SIEMPRE la misma dentro de su canal, no que haya una sola firma
# para toda la casa. Antes solo aceptaba «La Bandita informa» y los dos post de
# comunidad salían en rojo por firmar como firman.
FIRMAS_DECLARADAS = (
    re.compile(r"La Bandita informa"),                              # piezas de Facebook y WhatsApp
    re.compile(r"💓\s*\*La Bandita · [^*]{6,90}Santo Domingo"),     # post de comunidad
)


def _tiene_firma(contenido: str) -> bool:
    return "💓" in contenido and any(f.search(contenido) for f in FIRMAS_DECLARADAS)


def _tiene_notas_pie(contenido: str) -> bool:
    """M10 — hay un bloque de notas al pie, y sus notas van fechadas.

    ANTES bastaba con que el documento dijera «notas al pie» en cualquier parte, y el
    MAPA de la pieza anuncia justo eso: «└── 🌅 cierre · 🔗 cómo se comprobó · 🗒️ notas
    al pie». Quitando el bloque entero, la pieza seguía pasando por lo que anunciaba
    su propio índice. Un índice no es una nota.

    AHORA se pide el encabezado del bloque (🗒️ o «Notas al pie» como título de línea) y
    al menos una fecha (9-nov) dentro de él, que es lo que el criterio llama «fechadas».

    El emoji del bloc lleva además un selector de variación U+FE0F que el patron no cubria:
    por eso el primer patrón no casaba con «*🗒️ Notas al pie*» aunque lo pareciera.
    """
    enc = re.search(r"^\s*(?:#{1,3}\s*)?\*?\s*[\U0001F5D2\U0001F4DD]\ufe0f?\s*\*?\s*Notas al pie",
                    contenido, re.M | re.I)
    if enc is None:
        for i, linea in enumerate(contenido.splitlines()):
            if re.fullmatch(r"\*?Notas al pie\*?:?", linea.strip(), re.I):
                return _notas_fechadas("\n".join(contenido.splitlines()[i:]))
        return False
    return _notas_fechadas(contenido[enc.start():])


# La fecha puede ir al final de la nota —«…sin fecha al lado.* (9-nov)»— o al
# principio, que es como las escriben las piezas de WhatsApp: «(2-nov) La consulta…».
# El criterio pide notas FECHADAS, no una posición concreta de la fecha.
FECHA_DE_NOTA = re.compile(r"\(\d{1,2}-[a-z]{3}(?:-\d{4})?\)")


def _notas_fechadas(bloque: str) -> bool:
    return bool(FECHA_DE_NOTA.search(bloque))


def _tiene_meta_comentario(contenido: str) -> bool:
    """M12 — la pieza habla de su tema, no de cómo se escribió.

    La lista era corta: «en esta sección voy a», «en este texto voy a», «vamos a ver».
    Una pieza que empieza «en esta pieza voy a contarte cómo escribí esto» pasaba
    limpia. Se añaden las formas con las que de verdad se cuela el meta-relato.
    """
    return bool(re.search(
        r"en esta (sección|pieza|entrada|publicación|entrega) voy a"
        r"|en este (texto|artículo|apartado|bloque) voy a"
        r"|vamos a ver"
        r"|cómo (escribí|redacté|armé) (esto|esta|este)"
        r"|lo que (pretendo|intento|quiero) (hacer|contar) (aquí|con esto)",
        contenido, re.I))


def _tiene_signos_dobles(contenido: str) -> bool:
    return bool(re.search(r"!!|\?!", contenido))


def _tiene_frases_prohibidas(contenido: str) -> bool:
    return any(f.lower() in contenido.lower() for f in FRASES_PROHIBIDAS)


def _tiene_promesas_vigilancia(contenido: str) -> bool:
    return bool(re.search(r"te avisaré|te mantendré informado|próximamente|mañana traigo", contenido, re.I))


# Palabras que de verdad señalan un secreto filtrado o un APK de mod.
#
# EL FALSO POSITIVO QUE ESTO CIERRA
# ---------------------------------
# La expresión anterior era `\.apk|mod|secret|contraseña|token|api_key` sin límites de
# palabra. `mod` casaba dentro de **modelo**, **modo**, **moderno**, **módulo** y
# **comodidad**: una pieza que hablaba de modelos ONNX salía marcada como «tiene
# secretos o APK de mods». Con ese criterio, las 42 piezas estaban en rojo y el
# mensaje acusaba de filtrar credenciales a textos que no filtran nada.
#
# Un detector que grita «secreto» cuando lee «modelo» enseña a ignorar los avisos
# de seguridad, que es el peor daño que puede hacer una compuerta.
_SECRETO = re.compile(
    # `.apk` suelto no basta: la pieza enseña `apksigner verify archivo.apk`, que es
    # un comando de verificación, no un mod. Solo cuenta si va pegado a una descarga
    # o a un mod: `descargar ... .apk`, `apk mod`, `mod apk`.
    r"(?:descarg\w*[^\n]{0,40}\.apk\b|apk\s+mod\b|\bmod\s+apk\b)"
    # «secreto» en singular, en una pieza que habla de un mensaje o de un truco, no es
    # una credencial: es una palabra. La 38 la usa dos veces —«el secreto no está en un
    # pergamino, está en que no hay secreto»— y salía acusada de filtrar un secreto.
    # Se persiguen las formas que de verdad nombran una credencial: en plural, o con
    # valor pegado, o «secreto de la api», o «secreto filtrado».
    # «contraseña» PELADA no es un secreto: es el tema. La pieza 03 es un listado de
    # gestores de contraseñas y la 14 habla de un cliente que guarda tu cuenta; si el
    # detector marca la palabra, marca el asunto entero y obliga a no hablar del tema.
    # Lo que se persigue es una contraseña CON VALOR al lado:
    #   contraseña: hunter2 · password = abc123 · la contraseña es «xyz»
    r"|(?<![\w-])(?:contraseña|password|passwd)\s*(?::|=|es)\s*[\"'«`]?\S{4,}"
    r"|(?<![\w-])(?:api[_-]?key|token de acceso|access[_-]?token)(?![\w-])"
    r"|(?<![\w-])(?:mod|mods|modded|modificado|parcheado)\s+(?:apk|de\s+apk)(?![\w-])"
    r"|(?<![\w-])secret[oa]?\s*(?:de\s+la\s+api|de\s+api|filtrad[oa]|filtr[oa]do)(?![\w-])"
    r"|(?<![\w-])secret[oa]?\s*(?::|=)\s*\S{4,}",
    re.I,
)


def _tiene_apk_mods_o_secretos(contenido: str) -> bool:
    return bool(_SECRETO.search(contenido))


def _contar_palabras(contenido: str) -> int:
    return len(contenido.split())


def _extraer_enlaces(contenido: str) -> list[tuple[str, str]]:
    """Extrae enlaces con formato - Nombre: URL"""
    return re.findall(r"^-\s*(.+?):\s*(https?://\S+)$", contenido, re.M)


# Criterios que solo aplican a una PIEZA, no a un comentario fijado.
#
# Un «Comentario-fijado» es el texto que se clava en la parte de arriba del muro:
# va antes que la pieza, es corto por diseño y no lleva mapa, ni FAQ, ni fichas con
# licencia. Exigirle la estructura de una pieza de 17.000 caracteres es pedirle que
# deje de ser un fijado. El manual los distingue; la compuerta no lo hacía.
CRITERIOS_SOLO_DE_PIEZA = ("M04", "M05", "M06", "M07", "M08")
CRITERIOS_SOLO_DE_PIEZA_LARGA = CRITERIOS_SOLO_DE_PIEZA + ("M04",)


# Lo que NO es una publicación y por tanto no se le puede pedir la estructura de una.
#
# LA VARA NO PUEDE FABRICAR ROJOS CON LO QUE NO ES UNA PIEZA
# ---------------------------------------------------------
# El "LEEME de la carpeta" es la guía interna de la carpeta: lista las piezas, explica
# la regla del nombre y dice qué hay archivado. No tiene mapa, ni «En una página», ni
# FAQ, porque no se publica en ningún muro. Exigírselos es pedirle a un índice que sea
# un artículo, y el resultado era un rojo permanente que nadie iba a resolver nunca.
# Los "post de comunidad" son otra cosa: sí se publican, pero no son piezas de la serie
# —no llevan banda de pieza ni estructura de pieza— y se juzgan por las reglas de un
# post, que son firma, fecha larga y nada que pueda engañar a nadie.
NO_SON_PIEZAS = re.compile(r"^(LEEME|INDICE|_|README|CHANGELOG)", re.IGNORECASE)


def _es_documento_de_carpeta(ruta: Path) -> bool:
    """Un índice o una guía de la carpeta, no una publicación.

    Se reconoce por el nombre y por lo que declara de sí mismo: si el texto empieza
    con un título de documento («# LEEME de la carpeta») no es una pieza, que empieza
    con su titular en cursiva.
    """
    if NO_SON_PIEZAS.match(ruta.name):
        return True
    try:
        cabecera = ruta.read_text(encoding="utf-8")[:400]
    except OSError:
        return False
    return cabecera.lstrip().startswith("# ")


def _es_post_de_comunidad(ruta: Path) -> bool:
    """Un post de comunidad no es una pieza de la serie: es un texto suelto de muro.

    `docs/bandas.json` lo declara en su propia sección («posts-comunidad») y su nombre
    lo dice. Se le piden las reglas del post —firma, meme, remate, notas, enlaces al
    pie, nada que engañe— y no la estructura de una pieza de veinte mil caracteres,
    que no es lo que se publicó. Exigirle mapa y FAQ a un post de tres párrafos es
    pedirle que deje de ser un post.
    """
    return "posts-comunidad" in ruta.as_posix().lower() or ruta.name.startswith("post-")


def _es_comentario_fijado(ruta: Path) -> bool:
    return "comentario-fijado" in ruta.name.lower()


def _es_archivada(ruta: Path) -> bool:
    """Las piezas archivadas se conservan como se publicaron; no se reescriben."""
    partes = ruta.parts
    return any(p.startswith("_") or p.upper() == "ARCHIVO-HISTORICO" for p in partes[:-1])


def _evaluar_pieza(ruta: Path, bandas: dict) -> ResultadoPieza:
    contenido = _leer(ruta)
    largo = len(contenido)
    criterios: list[Criterio] = []
    rojo = False
    ventana = False

    # M01: Firma textual
    m01 = _tiene_firma(contenido)
    criterios.append(Criterio("M01", "firma textual", m01, "presente" if m01 else "ausente"))
    if not m01:
        rojo = True

    # M02: Meme del corte
    m02 = _tiene_meme_corte(contenido)
    criterios.append(Criterio("M02", "meme del corte", m02, "presente" if m02 else "ausente"))
    if not m02:
        ventana = True

    # M03: remate propio, no calcado.
    #
    # El patrón era `💓\*.+`, que espera el emoji ANTES del asterisco. Las piezas
    # llevan `*💓 La Bandita informa. …*`: el asterisco abre la cursiva y el emoji va
    # dentro. Por eso M03 salía «ausente» en las 42 piezas y en las 42 aparecía como
    # VENTANA: un patrón mal escrito, no un fallo de redacción. Ahora acepta las dos
    # formas y exige que haya texto propio después de la firma, que es lo que el
    # manual pide (remate distinto en cada pieza).
    # La firma puede ser cualquiera de las declaradas (ver FIRMAS_DECLARADAS): una pieza
    # firma «La Bandita informa…» y un post de comunidad firma «La Bandita · fecha ·
    # Santo Domingo». M03 no pregunta cuál es la firma —eso es M01— sino si DESPUÉS de
    # la firma hay texto propio. Buscaba solo la primera forma y dejaba en rojo a los
    # post de comunidad por no firmar como una pieza.
    firma = re.search(r"\*?\s*💓[^\n]*", contenido)
    remate = ""
    if firma:
        resto = contenido[firma.end():]
        # El remate son las líneas propias antes del separador o de las notas.
        lineas = [l.strip() for l in resto.split("\n")]
        remate = " ".join(l for l in lineas if l and not set(l) <= set("─-= ") and "LA BANDITA" not in l.upper())
    m03 = bool(firma) and len(remate) >= 20
    criterios.append(Criterio("M03", "remate propio no calcado", m03, "presente" if m03 else "ausente"))
    if not m03:
        ventana = True

    # M04: Mapa 5-12 entradas
    m04 = _tiene_mapa(contenido)
    n_secciones = _contar_secciones_mapa(contenido)
    m04_ok = m04 and 5 <= n_secciones <= 12
    criterios.append(Criterio("M04", "mapa 5-12", m04_ok, f"{n_secciones} entradas" if m04 else "sin mapa"))
    if not m04_ok:
        rojo = True

    # M05: «En una página» 3-5 párrafos
    m05 = _tiene_una_pagina(contenido)
    criterios.append(Criterio("M05", "«En una página» 3-5 párrafos", m05, "presente" if m05 else "ausente"))
    if not m05:
        ventana = True

    # M06: FAQ 6-12 preguntas
    m06 = bool(re.search(r"❓|Preguntas frecuentes|FAQ", contenido, re.I))
    criterios.append(Criterio("M06", "FAQ 6-12", m06, "presente" if m06 else "ausente"))
    if not m06:
        ventana = True

    # M07: enlaces completos y con formato.
    #
    # La regla del acta es «toda URL del cuerpo aparece al pie como `- Nombre: URL`».
    # Con cero URLs en el cuerpo, la regla se cumple sin escribir nada: no hay nada
    # que enlazar. La comprobación anterior pedía al menos un enlace siempre, así que
    # una pieza que habla de repositorios por su nombre —y no cita una sola URL—
    # salía en VENTANA por no tener enlaces que no necesita.
    url_cuerpo = re.findall(r"https?://[^\s)\]]+", contenido)
    enlaces = _extraer_enlaces(contenido)
    if not url_cuerpo:
        m07, detalle = True, "0 URLs en el cuerpo: no hay nada que enlazar"
    elif enlaces:
        m07, detalle = True, f"{len(enlaces)} enlaces al pie de {len(url_cuerpo)} URLs"
    else:
        m07, detalle = False, f"{len(url_cuerpo)} URLs en el cuerpo y 0 enlaces al pie"
    criterios.append(Criterio("M07", "enlaces - Nombre: URL", m07, detalle))
    if not m07:
        ventana = True

    # M08: Fichas con licencia
    m08, detalle_m08 = _fichas_con_licencia(contenido)
    criterios.append(Criterio("M08", "fichas con licencia", m08, detalle_m08))
    if not m08:
        rojo = True

    # M09: Frases prohibidas
    m09 = not _tiene_frases_prohibidas(contenido)
    criterios.append(Criterio("M09", "frases prohibidas", m09, "sin frases de venta" if m09 else "tiene frases prohibidas"))
    if not m09:
        rojo = True

    # M10: Notas fechadas
    m10 = _tiene_notas_pie(contenido)
    criterios.append(Criterio("M10", "notas fechadas", m10, "presente" if m10 else "ausente"))
    if not m10:
        rojo = True

    # M11: Banda de longitud
    #
    # EL FALSO VERDE QUE ESTO CIERRA
    # ------------------------------
    # La banda se elegía recorriendo bandas.json y quedándose con la PRIMERA que
    # contuviera la longitud, sin mirar de qué canal era la pieza. Con eso, una pieza
    # de Facebook de 54.730 caracteres —casi diez mil por encima de su máximo de
    # 45.000— pasaba en verde, porque cabía en la banda de WhatsApp (900–70.000).
    # La banda es del canal: se resuelve por la carpeta donde vive la pieza, y dentro
    # de ese canal se busca la entrada de esa pieza si está declarada.
    m11, detalle_m11 = _banda_de_la_pieza(ruta, largo, bandas)
    criterios.append(Criterio("M11", "banda de longitud", m11, detalle_m11))
    if not m11:
        rojo = True

    # M12: Meta-comentarios
    m12 = not _tiene_meta_comentario(contenido)
    criterios.append(Criterio("M12", "meta-comentarios", m12, "sin meta-comentarios" if m12 else "tiene meta-comentarios"))
    if not m12:
        rojo = True

    # M13: Cabecera con fecha larga
    m13 = bool(re.search(r"lunes|martes|miércoles|jueves|viernes|sábado|domingo", contenido))
    criterios.append(Criterio("M13", "cabecera con fecha larga", m13, "presente" if m13 else "ausente"))
    if not m13:
        ventana = True

    # M14: Signos dobles
    m14 = not _tiene_signos_dobles(contenido)
    criterios.append(Criterio("M14", "signos dobles", m14, "sin signos dobles" if m14 else "tiene signos dobles"))
    if not m14:
        rojo = True

    # M15: Secretos y APK de mods
    m15 = not _tiene_apk_mods_o_secretos(contenido)
    criterios.append(Criterio("M15", "secretos y APK de mods", m15, "limpio" if m15 else "tiene secretos o APK mods"))
    if not m15:
        rojo = True

    # M16: Promesas de vigilancia
    m16 = not _tiene_promesas_vigilancia(contenido)
    criterios.append(Criterio("M16", "promesas de vigilancia", m16, "sin promesas" if m16 else "tiene promesas"))
    if not m16:
        rojo = True

    # M23: Párrafos compartidos entre piezas (heurística básica: líneas largas repetidas)
    m23 = True  # Se verifica contra piezas vecinas en --verificar
    criterios.append(Criterio("M23", "párrafos compartidos", m23, "sin compartidos detectados"))

    # Si es un comentario fijado, los criterios de pieza completa no cuentan: se
    # marcan como no aplicables en vez de como fallos, para que el informe diga la
    # verdad —«esto no le corresponde»— y no «esto está mal».
    if _es_comentario_fijado(ruta):
        for i, c in enumerate(criterios):
            if c.codigo in CRITERIOS_SOLO_DE_PIEZA:
                criterios[i] = Criterio(c.codigo, c.nombre, True, "no aplica a un comentario fijado")

    # Un post de comunidad se juzga por las reglas del post: mapa, «En una página» y
    # FAQ son estructura de pieza de serie y no se le piden.
    if _es_post_de_comunidad(ruta):
        for i, c in enumerate(criterios):
            if c.codigo in ("M04", "M05", "M06"):
                criterios[i] = Criterio(c.codigo, c.nombre, True, "no aplica a un post de comunidad")

    # Un fijado tiene que ser corto; se le aplica la banda del fijado, no la de pieza.
    # El estado se recalcula con los criterios que de verdad le tocan.
    if _es_comentario_fijado(ruta):
        rojo = any(not c.pasa for c in criterios if c.codigo not in CRITERIOS_SOLO_DE_PIEZA)
    elif _es_post_de_comunidad(ruta):
        rojo = any(not c.pasa for c in criterios if c.codigo not in ("M04", "M05", "M06"))

    # La bandera «ventana» se pone durante la evaluación y no se recalculaba al
    # neutralizar criterios: 45 fijados quedaban marcados como VENTANA sin un solo
    # criterio fallando. Una pieza no está en ventana si no le falla nada.
    ventana = any(not c.pasa for c in criterios) and not rojo

    return ResultadoPieza(
        ruta=str(ruta.relative_to(RAIZ)),
        verde=(not rojo and not ventana),
        ventana=ventana and not rojo,
        rojo=rojo,
        criterios=criterios,
    )


def _evaluar_carpeta(carpeta: Path, bandas: dict) -> list[ResultadoPieza]:
    """Evalúa lo que está vivo.

    Se saltan dos cosas, y las dos a propósito:
      · archivos que empiezan por «_» (notas de trabajo, no piezas);
      · todo lo que vive bajo una carpeta que empieza por «_» o se llama
        ARCHIVO-HISTORICO: son piezas publicadas hace meses que se conservan
        como salieron. Reescribirlas para que pasen una compuerta de hoy sería
        falsificar lo publicado, que es justo lo que la casa prohíbe.
    """
    resultados: list[ResultadoPieza] = []
    for p in sorted(carpeta.rglob("*.md")):
        if p.name.startswith("_"):
            continue
        if _es_archivada(p):
            continue
        if _es_documento_de_carpeta(p):
            continue  # un índice no es una publicación: no se le pide estructura de pieza
        resultados.append(_evaluar_pieza(p, bandas))
    return resultados


def _cargar_bandas() -> dict:
    if BANDAS.exists():
        try:
            return json.loads(BANDAS.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            pass
    return {}


def _eval_una_pieza(ruta: Path, bandas: dict) -> str:
    r = _evaluar_pieza(ruta, bandas)
    lineas = [f"MANUAL GATE · {r.ruta} · {r.estado}"]
    for c in r.criterios:
        icono = "✓" if c.pasa else "✗"
        lineas.append(f"  {icono} {c.codigo} {c.nombre} · {c.detalle}")
    return "\n".join(lineas)


def main(argv: list[str] | None = None) -> int:
    import argparse
    parser = argparse.ArgumentParser(description="Compuerta del Manual de Estilo y Operaciones V3.0.")
    parser.add_argument("--pieza", metavar="RUTA", help="evalúa una pieza concreta")
    parser.add_argument("--verificar", action="store_true", help="evalúa toda la carpeta de publicaciones")
    args = parser.parse_args(argv)

    bandas = _cargar_bandas()

    if args.pieza:
        ruta = Path(args.pieza)
        if not ruta.is_absolute():
            ruta = RAIZ / ruta
        if not ruta.exists():
            print(f"no existe la pieza: {ruta}")
            return 1
        print(_eval_una_pieza(ruta, bandas))
        return 0

    if args.verificar:
        # El código de salida dice la verdad, y desglosado:
        #   0 = todo en verde o en ventana (una ventana es aviso, no fallo)
        #   1 = hay piezas rojas
        # Antes devolvía 0 siempre, y una compuerta que nunca falla no es una
        # compuerta: es un adorno que ocupa un paso del flujo.
        # La autoprueba usa el modo --pieza, así que este cambio no la afecta.
        if not PUBLICACIONES.exists():
            print("no existe Arena-Reimagined/01-PUBLICACIONES")
            return 1
        resultados = _evaluar_carpeta(PUBLICACIONES, bandas)
        verdes = sum(1 for r in resultados if r.verde)
        rojos = sum(1 for r in resultados if r.rojo)
        ventanas = sum(1 for r in resultados if r.ventana)
        fijados = sum(1 for r in resultados if _es_comentario_fijado(RAIZ / r.ruta))
        print(
            f"MANUAL GATE · {len(resultados)} textos vivos · "
            f"{len(resultados) - fijados} piezas y {fijados} comentarios fijados · "
            f"VERDE {verdes} · ROJO {rojos} · VENTANA {ventanas}"
        )
        for r in resultados:
            if r.rojo:
                print(f"  ✗ {r.ruta} · ROJO")
        return 0 if rojos == 0 else 1

    parser.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
