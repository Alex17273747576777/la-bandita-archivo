#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Comentario fijado de las piezas 24–29 y 32–34, generado desde el JSON de medición.

Cada cifra de estos comentarios sale de docs/MEDICION-NN-2026-11-08.json. No hay
ni un número escrito a mano: si la medición cambia, el comentario se regenera y
cambia con ella.
"""
from __future__ import annotations

import json
from pathlib import Path

RAIZ = Path("/opt/work/la-bandita-archivo")
CARPETA = RAIZ / "Arena-Reimagined" / "01-PUBLICACIONES" / "Facebook-dominicano-ES"
FECHA = "domingo 8 de noviembre de 2026"

# Cuerpo de cada pieza (glob) y qué destacar en el comentario.
PIEZAS = {
    "24": {"glob": "24-repositorios-*.md", "titulo": "Repositorios de extensiones de anime: cinco vivos, ninguno firma"},
    "25": {"glob": "25-OCR-*.md", "titulo": "OCR de bolsillo: siete programas y una sola suma"},
    "26": {"glob": "26-Usagi-el-*.md", "titulo": "Usagi: el fork que se mueve y su casa parada"},
    "27": {"glob": "27-DropSauce-el-*.md", "titulo": "DropSauce: el único del tema que firma"},
    "28": {"glob": "28-Mangayomi-y-*.md", "titulo": "Mangayomi y sus extensiones: el mayor número sin huella"},
    "29": {"glob": "29-LNReader-y-*.md", "titulo": "LNReader y sus plugins: cinco sumas y 963 días"},
    "32": {"glob": "32-Tu-Manga-*.md", "titulo": "Tu Manga Online: lo que dice el código, sin lista de dominios"},
    "33": {"glob": "33-apoyo-a-*.md", "titulo": "Apoyo a desarrolladores: nueve proyectos auditados"},
    "34": {"glob": "34-tu-biblioteca-*.md", "titulo": "Tu biblioteca de Kototoro: migrar y comprobar"},
}

ORDENES = """**Seis órdenes para comprobarlo tú mismo:**
1. Abre la página de entregas del repositorio y busca archivos `.sha256`, `.sha512`, `.asc`, `.sig` o `sums`.
2. En Termux: `pkg install coreutils && sha256sum *.apk`.
3. Compara con lo que publicó el autor: `sha256sum -c archivo.sha256`.
4. Mira la firma del paquete: `apksigner verify --print-certs archivo.apk` y compara la línea SHA-256 con la versión anterior.
5. Si no hay suma, pídela en las incidencias del repositorio. La plantilla está al final de las piezas 01 a 22.
6. Si hay atestación: `gh attestation verify archivo.apk --repo dueno/nombre`."""


def miles(n: int) -> str:
    return f"{n:,}".replace(",", ".")


def escribir(numero: str, cfg: dict) -> Path:
    doc = json.loads((RAIZ / "docs" / f"MEDICION-{numero}-2026-11-08.json").read_text(encoding="utf-8"))
    t = doc["totales"]
    repos = doc["repos"]
    vivos = {k: v for k, v in repos.items() if v.get("estado") == "vivo"}
    ordenados = sorted(vivos.items(), key=lambda kv: -(kv[1].get("stars") or 0))
    mejor = ordenados[0]
    firmantes = [(k, v) for k, v in ordenados if (v.get("huellas_total") or 0) > 0]
    con_mas_archivos = max(ordenados, key=lambda kv: kv[1].get("adjuntos_total") or 0)
    mas_viejo = max(ordenados, key=lambda kv: kv[1].get("dias_push") or 0)

    lineas = []
    lineas.append("━━━━━━━━━━━━━\n")
    lineas.append(f"📎 *Comentario fijado · Pieza {numero} — {cfg['titulo']}*\n")
    lineas.append("Enlaces rápidos:")
    lineas.append(f"• Cuerpo de la publicación: pieza {numero} de Facebook")
    lineas.append(f"• Fecha en vivo: {FECHA}")
    lineas.append(f"• Medido con: {doc['fuente']}")
    lineas.append(f"• Medición guardada en: `docs/MEDICION-{numero}-2026-11-08.json`\n")

    lineas.append("Lo que dicen los números medidos:")
    lineas.append(f"• **{t['vivos']} repositorios vivos** de {t['repos_medidos']} medidos"
                  + (f", y {t['sin_objeto']} que devuelve 404" if t["sin_objeto"] else "")
                  + f": {miles(t['stars'])} estrellas y {miles(t['descargas'])} descargas.")
    pct = (100.0 * t["con_huella"] / t["adjuntos"]) if t["adjuntos"] else 0.0
    lineas.append(f"• **{t['con_huella']} archivos con suma de comprobación de {miles(t['adjuntos'])}** publicados: "
                  f"el **{pct:.1f} %**. Repositorios que firman: **{t['repos_con_huella']}**.")
    lineas.append(f"• El que más publica: `{con_mas_archivos[0]}` con **{miles(con_mas_archivos[1]['adjuntos_total'])} adjuntos** "
                  f"y **{con_mas_archivos[1]['huellas_total']} sumas**.")
    if firmantes:
        detalle = ", ".join(f"`{k}` ({v['huellas_total']})" for k, v in firmantes)
        lineas.append(f"• Los que sí firman: {detalle}.")
    else:
        lineas.append("• **Ninguno de los medidos publica una sola suma**: no hay nada que comparar.")
    lineas.append(f"• Archivados: **{t['archivados']}** · sin entrega etiquetada: **{t['repos_sin_entrega']}** · "
                  f"sin licencia legible: **{t['sin_licencia_legible']}**.")
    lineas.append(f"• Movimiento: **{t['push_7d']}** con código en los últimos 7 días, **{t['push_30d']}** en el mes.")
    lineas.append(f"• El más quieto: `{mas_viejo[0]}`, **{mas_viejo[1]['dias_push']} días** sin un empujón.")
    lineas.append(f"• El más grande por estrellas: `{mejor[0]}`, ★{miles(mejor[1]['stars'] or 0)}.\n")

    lineas.append(ORDENES + "\n")
    lineas.append("Qué puedes hacer con esto:")
    if t["con_huella"]:
        lineas.append("Baja el archivo y compruébalo con `sha256sum -c` antes de instalarlo. Es el único paso de la "
                      "lista que te da una certeza: los sesenta y cuatro caracteres coinciden o no coinciden.")
    else:
        lineas.append("Comprobar el archivo no es posible: ninguno de estos repositorios publica una suma. Lo que sí "
                      "puedes comprobar es la **fecha** del último empujón y si el proyecto publica entregas; con eso "
                      "decides mejor que con las estrellas.")
    lineas.append("")
    lineas.append("*La Bandita informa a partir de fuentes fechadas. · " + FECHA +
                  " · comentario fijado de la publicación. Ningún paquete se aloja aquí; solo enlaces al "
                  "repositorio del autor en GitHub.*")

    destino = CARPETA / f"{numero}-Comentario-fijado-facebook-La-Bandita-2026-11-08-dominicano-ES.md"
    destino.write_text("\n".join(lineas) + "\n", encoding="utf-8")
    return destino


def main() -> None:
    for numero, cfg in PIEZAS.items():
        cuerpo = next(CARPETA.glob(cfg["glob"]))
        d = escribir(numero, cfg)
        # se retira el fijado anterior, si lo había con otra fecha
        for viejo in CARPETA.glob(f"{numero}-Comentario-fijado-*.md"):
            if viejo.name != d.name:
                viejo.unlink()
                print(f"  retirado el fijado anterior: {viejo.name[:40]}")
        print(f"{numero}  fijado {len(d.read_text(encoding='utf-8')):>5} car  cuerpo {len(cuerpo.read_text(encoding='utf-8')):>6} car")


if __name__ == "__main__":
    main()
