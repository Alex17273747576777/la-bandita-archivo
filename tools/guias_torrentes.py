#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""guias_torrentes.py · las guías escritas a mano del racimo «torrentes» (3 recursos).

Aviso que vale para las tres: este racimo no reparte contenido ni enlaza clientes. Son las
herramientas de comprobación que se usan cuando se descargan archivos grandes de cualquier
procedencia: comprobar la huella, comprobar el disco, comprobar el archivo.
"""
import json
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
CATALOGO = RAIZ / "catalogo"
MEDIDO = CATALOGO / "medido.json"
INICIO, FIN = "<!-- GUIA:INICIO -->", "<!-- GUIA:FIN -->"
RACIMO = "torrentes"

GUIA = {}

GUIA["rhash/RHash"] = """
### Para qué sirve

Utilidad de consola que calcula y verifica huellas de archivos: CRC32, MD5, SHA-1, SHA-256, SHA-512, SHA3,
BLAKE, ED2K, TTH de DC++ y **BTIH, la huella que identifica un torrent**. Con ella se comprueba que lo que se
descargó es exactamente lo que se quería descargar.

Es el corrector de errores de la cadena entera: sirve igual para un archivo bajado de una web, para un disco
que empieza a fallar o para una copia de seguridad que quieres verificar diez años después.

### Cómo se usa

1. Se instala desde los paquetes de la distribución o se compila con `./configure && make install`.
2. Para calcular todas las huellas de un archivo: `rhash -a SHA256 archivo.iso`.
3. Para verificar contra una lista: `rhash -c lista.sha256`.
4. Para recorrer una carpeta entera: `rhash --recursive --sha256 carpeta/ > lista.sha256`.

### Lo que conviene saber antes

735 estrellas, 0BSD —una licencia permisiva sin condiciones, la más libre que se puede escribir—, C, y creado
en 2011: quince años de historia. 133 bifurcaciones y 55 incidencias abiertas. Su última entrega etiquetada es
la `v1.4.6`, del 13 de mayo de 2025, aunque los empujones son recientes.

Se distribuye como programa de consola para Windows, macOS y Linux, y hay interfaces gráficas hechas por otros.
El detalle que conviene entender: una huella sirve para comprobar **integridad**, no para saber de quién es un
archivo; si alguien cambia el archivo y la lista, las dos coinciden.

### Cuándo no vale la pena

Si nunca compruebas nada de lo que descargas, ninguna herramienta de este tipo te va a cambiar la vida. Y para
un solo archivo, casi todos los sistemas ya traen un comando que calcula SHA-256.
"""

GUIA["smartmontools/smartmontools"] = """
### Para qué sirve

Los dos programas clásicos para preguntarle a un disco cómo está: `smartctl` lee los datos internos que el
propio disco lleva contando desde el primer día —horas encendido, sectores reasignados, errores, temperatura— y
`smartd` vigila en segundo plano y avisa cuando algo se tuerce.

Para quien guarda archivos grandes de verdad, esto es lo que separa una pérdida de datos de un susto.

### Cómo se usa

1. Se instala desde los paquetes del sistema o desde el código fuente.
2. `smartctl -a /dev/sdX` muestra todo lo que el disco declara sobre sí mismo.
3. La prueba corta —`smartctl -t short /dev/sdX`— dura dos minutos y conviene hacerla de vez en cuando.
4. `smartd` se deja como servicio y manda correo cuando un valor cruza el umbral.

### Lo que conviene saber antes

1.460 estrellas, GPL-2.0, C++, con 304 bifurcaciones y 99 incidencias abiertas. Este repositorio es el sitio
oficial del proyecto desde 2017; su última entrega es `RELEASE_7_5`, del 12 de mayo de 2025, y el trabajo sigue
a diario.

Funciona con discos ATA/SATA, SCSI/SAS, NVMe y cintas, y en casi cualquier sistema operativo que exista. Dos
límites que conviene saber: **detrás de un adaptador USB barato no siempre se puede leer**, y un «disco sano»
hoy puede morir mañana; los valores sirven para ver tendencias, no para predecir.

### Cuándo no vale la pena

En un portátil con un único disco del sistema, leer sus datos una vez al año basta. Y si usas un servidor en la
nube, el disco no está a tu alcance: eso lo vigila quien te lo alquila.
"""

GUIA["uutils/coreutils"] = """
### Para qué sirve

Reescritura en Rust de las utilidades básicas de Unix: `ls`, `cp`, `mv`, `cat`, `sort`, `sha256sum`, `date` y
unas ochenta más. Nació para tener un conjunto de herramientas portátil y rápido, y hoy es una pieza que se usa
en Windows para darle un entorno parecido al de Unix.

En este racimo aparece por una razón concreta: **`sha256sum` y `cksum`**. Cuando hay que comprobar muchos
archivos a la vez, estas son las que se usan.

### Cómo se usa

1. Se instala con Cargo: `cargo install coreutils`; o desde los paquetes del sistema, que en varias
   distribuciones ya lo ofrecen como alternativa.
2. Se invocan igual que sus equivalentes de siempre: los nombres son los mismos.
3. Para comprobar una lista de huellas: `sha256sum -c lista.sha256`.
4. En Windows se añade su carpeta al `PATH` para tener los comandos a mano.

### Lo que conviene saber antes

24.331 estrellas, MIT, Rust, creado en 2013, con 2.153 bifurcaciones y 1.410 incidencias abiertas. Su entrega
`0.12.0` es del 17 de septiembre de 2026, trece años después de empezar: el proyecto avanza despacio a
propósito, porque aquí un error de `rm` cuesta caro.

Y eso es justo lo que hay que decir con claridad: **el propio proyecto avisa de que algunos programas y opciones
no se comportan exactamente igual que los originales**. Para un script de producción que depende de un detalle
raro de GNU, la diferencia puede importar.

### Cuándo no vale la pena

En Linux, macOS o cualquier Unix ya tienes estas herramientas funcionando desde el primer arranque. Sustituirlas
por estas solo tiene sentido si buscas la versión en Rust por velocidad, o si estás en Windows y quieres los
comandos de siempre.
"""


def main() -> int:
    medido = json.loads(MEDIDO.read_text(encoding="utf-8"))
    escritas = 0
    for repo, texto in GUIA.items():
        f = medido.get(repo)
        if not f or f.get("racimo") != RACIMO:
            print("  ! sin medir en el racimo:", repo)
            continue
        p = CATALOGO / repo.replace("/", "--").lower() / "FICHA.md"
        if not p.exists():
            print("  ! sin ficha:", repo)
            continue
        t = p.read_text(encoding="utf-8")
        if INICIO not in t or FIN not in t:
            print("  ! sin marcadores:", repo)
            continue
        nuevo = re.sub(re.escape(INICIO) + r".*?" + re.escape(FIN),
                       INICIO + "\n" + texto.strip() + "\n" + FIN, t, flags=re.S)
        if nuevo != t:
            p.write_text(nuevo, encoding="utf-8")
            escritas += 1
    print(f"guías escritas: {escritas} de {len(GUIA)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
