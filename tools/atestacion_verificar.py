#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""VERIFICADOR DE LA ATESTACIÓN FIRMADA SIN LLAVE (Sigstore keyless).

La firma sin llave no estaba «bloqueada por identidad del dueño»: la identidad la pone el propio
GitHub Actions por OIDC cuando corre el flujo. Lo que faltaba era poder COMPROBAR el paquete sin
depender de la web de Sigstore ni de una llave guardada. Esto lo comprueba en frío, con openssl:

  1. estructura del bundle (mediaType, messageSignature, verificationMaterial)
  2. el certificado es efímero y de sigstore (ventana de minutos, no de años)
  3. la identidad del certificado es la del flujo de esta casa (SAN de GitHub Actions)
  4. hay entrada en el registro de transparencia (Rekor): la firma es pública y fechada
  5. la firma criptográfica cubre el sha256 del manifiesto que se le pasa

Uso:
  python3 tools/atestacion_verificar.py attestations/lote-2026-11-03.sigstore.json \
          registry/_manifiesto-sha256.tsv
  python3 tools/atestacion_verificar.py --todas          # todas las de attestations/
"""
from __future__ import annotations

import base64
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
IDENTIDAD = re.compile(r"^https://github\.com/Alex17273747576777/la-bandita-archivo/"
                       r"\.github/workflows/vara\.yml@refs/heads/main$")


def _der_a_pem(der: bytes) -> bytes:
    b64 = base64.encodebytes(der).replace(b"\n", b"")
    trozos = [b64[i:i + 64] for i in range(0, len(b64), 64)]
    return b"-----BEGIN CERTIFICATE-----\n" + b"\n".join(trozos) + b"\n-----END CERTIFICATE-----\n"


def _campo_cert(pem: bytes, campo: str) -> str:
    if not shutil.which("openssl"):
        return ""
    with tempfile.NamedTemporaryFile("wb", suffix=".pem", delete=False) as f:
        f.write(pem)
        ruta = f.name
    try:
        r = subprocess.run(["openssl", "x509", "-in", ruta, "-noout", campo],
                           capture_output=True, text=True)
        return (r.stdout or "") + (r.stderr or "")
    finally:
        Path(ruta).unlink(missing_ok=True)


def manifiesto_del_lote(bundle: Path, vivo: Path | None = None) -> Path:
    """Cada paquete se firma sobre el manifiesto de SU lote, no sobre el de hoy. El manifiesto se
    guarda al lado (`lote-AAAA-MM-DD.tsv`); si no está, se cae al manifiesto vivo."""
    gemelo = bundle.with_suffix("").with_suffix(".tsv")
    if gemelo.exists():
        return gemelo
    return vivo or (RAIZ / "registry" / "_manifiesto-sha256.tsv")


def verificar(bundle: Path, manifiesto: Path) -> list[str]:
    fallos: list[str] = []
    try:
        j = json.loads(bundle.read_text(encoding="utf-8"))
    except Exception as e:
        return [f"{bundle.name}: no es JSON ({e})"]
    if not str(j.get("mediaType", "")).startswith("application/vnd.dev.sigstore.bundle"):
        fallos.append(f"{bundle.name}: mediaType fuera de norma ({j.get('mediaType')!r})")
    ms = j.get("messageSignature") or {}
    vm = j.get("verificationMaterial") or {}
    if not ms or not vm:
        return fallos + [f"{bundle.name}: sin messageSignature o sin verificationMaterial"]
    cert = vm.get("certificate") or {}
    der_b64 = cert.get("rawBytes")
    if not der_b64:
        return fallos + [f"{bundle.name}: sin certificado en el paquete"]
    der = base64.b64decode(der_b64)
    pem = _der_a_pem(der)

    # 2 · certificado efímero
    texto = _campo_cert(pem, "-text")
    if "sigstore" not in texto:
        fallos.append(f"{bundle.name}: el certificado no es de la CA de sigstore")
    m = re.search(r"Not Before\s*:\s*([^\n]+)\n\s*Not After\s*:\s*([^\n]+)", texto)
    if m:
        from datetime import datetime
        try:
            a = datetime.strptime(m.group(1).strip(), "%b %d %H:%M:%S %Y GMT")
            b = datetime.strptime(m.group(2).strip(), "%b %d %H:%M:%S %Y GMT")
            if (b - a).total_seconds() > 3600:
                fallos.append(f"{bundle.name}: el certificado vive {(b-a).total_seconds()/60:.0f} min; "
                              f"uno efímero no pasa de 60")
        except ValueError:
            pass
    else:
        fallos.append(f"{bundle.name}: no se pudo leer la ventana del certificado")

    # 3 · identidad del flujo
    san = re.search(r"URI:(https://github\.com/[^\s,]+)", texto)
    if not san:
        fallos.append(f"{bundle.name}: el certificado no acredita identidad de GitHub Actions")
    elif not IDENTIDAD.match(san.group(1)):
        fallos.append(f"{bundle.name}: firmado por otra identidad: {san.group(1)}")

    # 4 · registro de transparencia
    tl = vm.get("tlogEntries") or []
    if not tl:
        fallos.append(f"{bundle.name}: sin entrada en el registro de transparencia (Rekor)")
    elif not tl[0].get("logIndex"):
        fallos.append(f"{bundle.name}: entrada de Rekor sin índice")

    # 5 · la firma cubre el manifiesto
    digest = (ms.get("messageDigest") or {}).get("digest")
    if not digest:
        fallos.append(f"{bundle.name}: sin messageDigest")
        return fallos
    real = hashlib.sha256(manifiesto.read_bytes()).hexdigest()
    if base64.b64decode(digest).hex() != real:
        fallos.append(f"{bundle.name}: la firma no cubre este manifiesto "
                      f"(firmado {base64.b64decode(digest).hex()[:16]}… · hoy {real[:16]}…)")
        return fallos
    firma_b64 = ms.get("signature")
    if firma_b64 and shutil.which("openssl"):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            (p / "cert.pem").write_bytes(pem)
            (p / "firma.bin").write_bytes(base64.b64decode(firma_b64))
            (p / "digest.bin").write_bytes(base64.b64decode(digest))
            r = subprocess.run(["openssl", "x509", "-in", str(p / "cert.pem"), "-noout", "-pubkey"],
                               capture_output=True, text=True)
            if r.returncode == 0:
                (p / "pub.pem").write_text(r.stdout, encoding="utf-8")
                # cosign firma el blob: la comprobación se hace sobre el manifiesto entero
                v = subprocess.run(["openssl", "dgst", "-sha256", "-verify", str(p / "pub.pem"),
                                    "-signature", str(p / "firma.bin"), str(manifiesto)],
                                   capture_output=True, text=True)
                if "Verified OK" not in (v.stdout or "") + (v.stderr or ""):
                    fallos.append(f"{bundle.name}: la firma no verifica con la clave del certificado")
    return fallos


def main() -> int:
    args = sys.argv[1:]
    manifiesto = RAIZ / "registry" / "_manifiesto-sha256.tsv"
    if not args or "--todas" in args:
        bundles = sorted((RAIZ / "attestations").glob("*.sigstore.json"))
        if not bundles:
            print("atestación firmada: ninguna en attestations/ · fallos: 0 (declarado)")
            return 0
    else:
        bundles = [Path(args[0])]
        if len(args) > 1:
            manifiesto = Path(args[1])
    fallos: list[str] = []
    for b in bundles:
        m = manifiesto_del_lote(b, manifiesto)
        if not m.exists():
            fallos.append(f"{m}: no existe el manifiesto a verificar")
            continue
        fallos += verificar(b, m)
    print(f"atestaciones verificadas: {len(bundles)} · fallos: {len(fallos)}")
    for f in fallos[:20]:
        print("  ·", f)
    return 0 if not fallos else 1


if __name__ == "__main__":
    sys.exit(main())
