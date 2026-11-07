#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CENSO DE UN TEMA · contar sin pedir permiso a la memoria (error E12).

Una pieza decía «ciento doce proyectos de audio nacidos en el último año» y no
había forma de repetir esa cuenta: la consulta no estaba escrita. Este programa
la escribe. Filtra las fichas del registro por palabras declaradas y cuenta lo
que la pieza necesita, con el registro entero como denominador.

Uso:
    python3 tools/censo_tema.py --tema audio
    python3 tools/censo_tema.py --tema seguridad --palabras "vault,cifrado,2fa,totp" --dias 365 --json docs/CENSO-seguridad.json

Devuelve, sobre las fichas cuya descripción o nombre casan con las palabras:
  total · nacidas en la ventana · de ellas en el mes en curso · por debajo de
  500★ · sin licencia · con entrega en los últimos 30 días · mediana de edad.
"""
from __future__ import annotations

import json
import re
import statistics
import sys
from datetime import date, timedelta
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
EVID = RAIZ / "registry" / "_evidencia"
TEMAS = {
    "audio": "audio,sonido,sound,music,musica,música,dsp,equaliz,ecualiz,reproductor,player,podcast,mp3,flac,spotify,a2dp",
    "seguridad": "vault,cifrado,encrypt,2fa,totp,password,contraseña,keystore,clave",
    "descargas": "download,descarga,torrent,magnet,streaming,seed",
    "sistema": "root,shizuku,adb,kernel,su,permiso,permission,magisk",
    # añadidos el 4-nov-2026 para que los censos de las piezas 06 y 07 se repitan con una orden
    # y no con una tarde contando a mano (error E35, habilidad H15)
    "parches": "patch,parche,patches,parches,revanced,morphe,reseam,patcher,apk-mods",
    "televisor": "tv,televisor,television,android-tv,google-tv,roku,chromecast,cast,launcher,media-center,smarttube,kodi",
    "casa": "home-assistant,domotica,esphome,zigbee,mqtt,sensor,smart-home,kiosk,dashboard,homekit",
    # pieza 08: la red. Se declaran pocas palabras a propósito (H15): vpn, proxy, wireguard,
    # tailscale, dns, firewall, adblock, adblocker, tunnel, sing-box, xray, doh, dot, mesh
    "red": "vpn,proxy,wireguard,tailscale,dns,firewall,adblock,adblocker,tunnel,sing-box,xray,doh,dot,mesh",
    # pieza 09: archivos, copias y nubes propias
    "archivos": "archivo,file,sync,sincroniz,backup,copia,nube,cloud,storage,almacenamiento,sftp,ftp,nextcloud,immich,rclone,restic,rsync,drive",
    # pieza 10: repositorios de extensiones, parsers y plugins (solo tiendas, no aplicaciones).
    # Palabras declaradas a la vista: extension, plugin, parser, source, repo, addon, provider, index.
    "extensiones": "extension,extensions,plugin,plugins,parser,parsers,source,sources,repo,repositorio,addon,addons,provider,providers,tachiyomi,mihon,aniyomi,cloudstream,mangayomi,kotatsu,lnreader,aidoku,seanime,hayase,nuvio",
}


def contar(palabras: list[str], dias: int) -> dict:
    hoy = date.today()
    rx = re.compile(r"(?<![a-záéíóúñ])(" + "|".join(map(re.escape, palabras)) + r")(?![a-záéíóúñ])", re.I)
    total = dentro = mes = anterior = pobres = sin_lic = con_entrega = 0
    mes_previo = (hoy.replace(day=1) - timedelta(days=1)).isoformat()[:7]
    edades = []
    for f in EVID.glob("*.json"):
        try:
            d = json.loads(f.read_text(encoding="utf-8", errors="replace"))
        except Exception:
            continue
        if not isinstance(d, dict):
            continue
        if not rx.search(f"{d.get('description') or ''} {d.get('name') or ''}"):
            continue
        total += 1
        cre = (d.get("created_at") or "")[:10]
        if not cre:
            continue
        edad = (hoy - date.fromisoformat(cre)).days
        edades.append(edad)
        if edad > dias:
            continue
        dentro += 1
        if cre[:7] == hoy.isoformat()[:7]:
            mes += 1
        if cre[:7] == mes_previo:
            anterior += 1
        if (d.get("stargazers_count") or 0) < 500:
            pobres += 1
        if ((d.get("license") or {}).get("spdx_id") in (None, "NOASSERTION")):
            sin_lic += 1
        push = (d.get("pushed_at") or "")[:10]
        if push and (hoy - date.fromisoformat(push)).days <= 30:
            con_entrega += 1
    pct = round(100 * pobres / dentro) if dentro else 0
    return {"fecha": hoy.isoformat(), "palabras": palabras, "ventana_dias": dias,
            "total_del_tema": total, "nacidas_en_la_ventana": dentro, "en_el_mes_en_curso": mes, "en_el_mes_anterior": anterior,
            "por_debajo_de_500": pobres, "porcentaje": pct, "sin_licencia": sin_lic,
            "con_empujon_en_30_dias": con_entrega,
            "mediana_edad_dias": round(statistics.median(edades)) if edades else None}


def main() -> int:
    a = sys.argv[1:]
    tema = a[a.index("--tema") + 1] if "--tema" in a else "audio"
    palabras = [x.strip().lower() for x in
                (a[a.index("--palabras") + 1].split(",") if "--palabras" in a else TEMAS[tema].split(","))]
    dias = int(a[a.index("--dias") + 1]) if "--dias" in a else 365
    r = contar(palabras, dias)
    if "--json" in a:
        Path(a[a.index("--json") + 1]).write_text(json.dumps(r, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"CENSO DE {tema.upper()} · {r['fecha']} · ventana de {dias} días")
    print(f"  del tema, en todo el registro: {r['total_del_tema']}")
    print(f"  nacidas en la ventana: {r['nacidas_en_la_ventana']} · en el mes en curso: {r['en_el_mes_en_curso']}"
          f" · en el mes anterior: {r['en_el_mes_anterior']}")
    print(f"  por debajo de 500★: {r['por_debajo_de_500']} ({r['porcentaje']} %) · sin licencia: {r['sin_licencia']}")
    print(f"  con empujón en 30 días: {r['con_empujon_en_30_dias']} · mediana de edad: {r['mediana_edad_dias']} días")
    return 0


if __name__ == "__main__":
    sys.exit(main())
