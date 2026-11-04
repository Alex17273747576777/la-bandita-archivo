# PODA DEL 3 DE NOVIEMBRE DE 2026 · acta de procedencia

Este directorio existe para que nada desaparezca sin dejar rastro. Documenta la poda de residuos
ejecutada el 3 de noviembre de 2026 sobre la raíz del archivo: **11 archivos retirados** (16,6 MB) por
ser copia exacta o artefacto generado, y **53 documentos reubicados** desde `uploads/` (14 MB).

La regla que se aplicó es la de la casa: no se borra lo firmado, no se borra la evidencia y no se borra
nada sin acta. Los retirados llevan aquí su hash y su copia exacta sigue en la historia de Git,
recuperable con `git log --all --full-history -- <ruta>`. Los 53 documentos **no se borraron**: se
movieron a `ARCHIVO-HISTORICO/subidas-2026-09/` con sus nombres originales, porque eran la carga inicial
recibida en septiembre y su sitio es la memoria, no la raíz.

## 1 · Archivos retirados (11 · 16,6 MB)

| SHA-256 | Bytes | Archivo | Motivo |
|---|---|---|---|
| `25d69347f7e7a1d50eb4699d6d84e2b886224f9db2ecacefc793f03141df98c3` | 3642766 | `Arena-Reimagined/ENTREGA-La-Bandita-29oct2026.zip` | envase comprimido cuyas 284 entradas están todas abiertas en `ENTREGA-29OCT-2026/`; se cotejó nombre por nombre y no falta ninguna |
| `df0a022562cca4ddd7c57c4b15fbbc08c6381bc81d6d053ac0238f18099a1c1c` | 6559347 | `Arena-Reimagined/ENTREGA-La-Bandita-COMPLETA.html` | artefacto generado (6,5 MB) desde el envase que sí se conserva; se regenera con `tools/html_archivo.py` |
| `fa52c6dd2525963fbc1b60e55d123e7e0ac5ab6893b8368fb21bd905854da2ef` | 3970620 | `Arena-Reimagined/canon-labandita-kit-etapa4.zip` | envase comprimido cuyas 36 entradas están todas abiertas en `02-ARCHIVO/_kit-etapa4/` |
| `f6e277838fe385e22c2b5e2e58e3d504c5220c43c09721609454e9b0ab3513fe` | 97 | `Arena-Reimagined/canon-labandita-kit-etapa4.zip.sha256` | suma de comprobación de un envase retirado en la misma pasada |
| `5b7348ac1acdb7af162f4e85c87852f801cfe19818d35fd6adaf2a75392bf136` | 65559 | `uploads/03-ADV-WhatsApp-63k-La-Bandita-2026-09-13.md` | copia exacta, byte por byte, de `ARCHIVO-HISTORICO/backup-previo-correccion-14-09/` |
| `7c764caf00f3cf24811746d7cd0fb73b7c462997422339621f5874413cca8d4c` | 42644 | `uploads/04-Extensiones-Facebook-40k-La-Bandita-2026-09-13.md` | copia exacta, byte por byte, de `ARCHIVO-HISTORICO/backup-previo-correccion-14-09/` |
| `ea408006274b8fc29e27254da6afc4ad1a23ca1e032fb60dcdaf4299b3889e04` | 39552 | `Arena-Reimagined/00-CANON/_envases-xhtml/VISTA-CANON-CIMIENTO-envase-XHTML-2026-10-10.html` | vista HTML generada desde su `.xhtml` gemelo, que se conserva en la misma carpeta |
| `6c38de3166a282d21f5f155c72fc293592d4d23f6bfe42a6943b9f60e0c388e8` | 37093 | `Arena-Reimagined/00-CANON/_envases-xhtml/VISTA-COMPENDIO-INTEGRAL-envase-XHTML-2026-10-10.html` | vista HTML generada desde su `.xhtml` gemelo, que se conserva en la misma carpeta |
| `39d12186384ccdf9ababbc2f3ecceab56b497dd69fd92a8bb4d319b6b0557147` | 66935 | `Arena-Reimagined/00-CANON/_envases-xhtml/VISTA-LECCIONES-ALEXIS-envase-XHTML-2026-10-10.html` | vista HTML generada desde su `.xhtml` gemelo, que se conserva en la misma carpeta |
| `7e86303c32b51380685f0b91ae0859ee8827aaf920c1713bc8df9dd60011f513` | 623740 | `Arena-Reimagined/00-CANON/_envases-xhtml/VISTA-MANUAL-COMPLETO-envase-XHTML-2026-10-10.html` | vista HTML generada desde su `.xhtml` gemelo, que se conserva en la misma carpeta |
| `0259ebad6e50c3381c3f4f359ed8096ebd3af739fd316f90479ac0bca7fda7d3` | 1502876 | `Arena-Reimagined/00-CANON/_envases-xhtml/VISTA-TRATADO-envase-XHTML-2026-10-10.html` | vista HTML generada desde su `.xhtml` gemelo, que se conserva en la misma carpeta |

Los cuatro envases se abrieron y se cotejó su lista de entradas contra la carpeta ya presente, nombre por
nombre: los tres retirados no contenían ni un solo archivo que no estuviera ya abierto en el árbol. Los dos
documentos de septiembre se cotejaron por SHA-256 contra el respaldo del 14 de setiembre y coinciden byte
por byte. Las cinco vistas HTML se generaron a partir de los `.xhtml` que siguen en `00-CANON/_envases-xhtml/`.

### Lo que se empezó a retirar y se devolvió

`Arena-Reimagined/ENTREGA-La-Bandita-COMPLETA.zip` (5,3 MB) estaba en la lista de candidatos y **se
restauró antes de confirmar el cambio**. El motivo: de sus 456 entradas, 454 tienen gemelo en el árbol,
pero dos no —`LEEME-ENTREGA-COMPLETA.md` y `MANIFIESTO-ENTREGA-COMPLETA.tsv`—, y esas dos son el
manifiesto interno de esa entrega: la prueba de qué se subió el 30 de octubre. Un envase que aporta un
documento único no es un residuo, es un archivo. La comprobación que lo decidió está en el punto 4.

### Entradas de manifiesto que ahora apuntan a un archivo retirado

`ENTREGA-29OCT-2026/05-Anexo-BitXBit/MANIFIESTO-BITXBIT-TOTAL.tsv` cita dos de los archivos retirados:
`ENTREGA-La-Bandita-29oct2026.zip` (línea 1152) y `canon-labandita-kit-etapa4.zip` con su `.sha256`
(líneas 1179 y 1180). El manifiesto **no se editó**: es un registro fechado y se conserva como prueba de
lo que hubo. Este párrafo es su traducción. Conviene además saber que el hash que el manifiesto declara
para el ZIP de la entrega (`19b3f4ad…`) no coincide con el del archivo que había en el árbol
(`25d69347…`): el envase se regeneró el 30 de octubre y el manifiesto conserva el valor anterior. Ese
desajuste ya existía y la poda no lo creó.

## 2 · Documentos reubicados (53 · de `uploads/` a `ARCHIVO-HISTORICO/subidas-2026-09/`)

No se borró ninguno. `uploads/` era la entrada de material nuevo, y lo que contenía era la carga inicial
del 13 de setiembre de 2026 —doce dossiers por canal, las cuatro compilaciones multilingües V25, sus
resúmenes de enlaces y las notas personales—: o sea memoria, y la memoria vive aquí. Dos de esos 53 eran
copia exacta de documentos ya archivados y se retiraron en el punto 1; los otros 53 menos dos siguen
íntegros con su nombre original. Los enlaces internos se corrigieron en el mismo cambio y
`tools/referencias.py` verifica que no quede ninguna cita por la ruta vieja.

- `00-INVENTARIO.md`
- `01-Tiendas-APK-Facebook-40k-La-Bandita-2026-09-13.md`
- `01-Tiendas-APK-WhatsApp-La-Bandita-2026-09-13.md`
- `02-Kototoro-Facebook-40k-La-Bandita-2026-09-13.md`
- `02-Kototoro-WhatsApp-La-Bandita-2026-09-13.md`
- `03-ADV-Facebook-40k-La-Bandita-2026-09-13.md`
- `04-Extensiones-WhatsApp-La-Bandita-2026-09-13.md`
- `05-TMO-clones-Facebook-40k-La-Bandita-2026-09-13.md`
- `05-TMO-clones-WhatsApp-La-Bandita-2026-09-13.md`
- `06-Forks-lectores-Facebook-40k-La-Bandita-2026-09-13.md`
- `06-Forks-lectores-WhatsApp-La-Bandita-2026-09-13.md`
- `07-Usagi-Facebook-40k-La-Bandita-2026-09-13.md`
- `07-Usagi-WhatsApp-La-Bandita-2026-09-13.md`
- `08-Musica-FOSS-Facebook-40k-La-Bandita-2026-09-13.md`
- `08-Musica-FOSS-WhatsApp-La-Bandita-2026-09-13.md`
- `09-Herramientas-FOSS-Facebook-40k-La-Bandita-2026-09-13.md`
- `09-Herramientas-FOSS-WhatsApp-La-Bandita-2026-09-13.md`
- `0d41c27e-fcf8-4879-8b8d-d8de6b9e5f21.md`
- `10-GLTools-Facebook-40k-La-Bandita-2026-09-13.md`
- `10-GLTools-WhatsApp-La-Bandita-2026-09-13.md`
- `11-AniZen-Facebook-40k-La-Bandita-2026-09-13.md`
- `11-AniZen-WhatsApp-La-Bandita-2026-09-13.md`
- `12-FMHY-Facebook-40k-La-Bandita-2026-09-13.md`
- `12-FMHY-WhatsApp-La-Bandita-2026-09-13.md`
- `280863d8-8bc7-4ace-b424-90dc2f707143.md`
- `Carta-a-La-Bandita.md`
- `Fila 2 — Dossier AniZen.md`
- `LEEME.md`
- `LEEME.txt`
- `Lecciones de Alexis.md`
- `Lecciones-extraidas-de-textos-personales.md`
- `Manual de Campo La Bandita — V1.0.md`
- `NO-REPUBLICAR.md`
- `Next Tratado Bandita Open Source — Fusión Universal V.0.02.md`
- `PUBLICACION_COMPLETA_BANDITA_V25_en-US.md`
- `PUBLICACION_COMPLETA_BANDITA_V25_es-DO.md`
- `PUBLICACION_COMPLETA_BANDITA_V25_fr-FR.md`
- `PUBLICACION_COMPLETA_BANDITA_V25_pt-BR.md`
- `PUBLICACION_ENLACES_RESUMEN_en-US.md`
- `PUBLICACION_ENLACES_RESUMEN_es-DO.md`
- `PUBLICACION_ENLACES_RESUMEN_fr-FR.md`
- `PUBLICACION_ENLACES_RESUMEN_pt-BR.md`
- `README.md`
- `README_en-US.md`
- `README_fr-FR.md`
- `README_pt-BR.md`
- `SHA256SUMS.txt`
- `inventario-v25-esDO.txt`
- `musicos-vivos-15sep.txt`

## 3 · Qué pasó con las citas de la ruta vieja

`docs/ACTA-LIMPIEZA-2026-11-02.md` y `docs/ACTA-REMEDICION-2026-11-03.md` citan `uploads/` como estaba el
2 y el 3 de noviembre. **No se reescribieron**: un acta fechada que se retoca deja de ser prueba. La
traducción de la ruta vieja a la nueva está aquí, y `MAPA-DEL-ARCHIVO.md` la explica en su entrada.
`tools/referencias.py` mantiene las dos rutas en su tabla de mudanzas para que la cita histórica se lea
como cita y no como fallo.

## 4 · Cómo se comprobó cada retirada antes de retirarla

Las tres comprobaciones fueron mecánicas, no de vista. **Copias exactas:** SHA-256 del archivo contra el
del presunto gemelo, y coincidencia exacta. **Envases:** apertura del ZIP y comparación de la lista de
entradas contra los nombres del árbol, contando las que no tienen gemelo; cualquier resultado distinto de
cero detenía la retirada, y así se detuvo la del envase completo. **Artefactos generados:** lectura del
generador que los produce y comprobación de que su fuente sigue en el árbol. Después de la poda se corrió
`tools/referencias.py` (sin referencias rotas), `tools/vara.py` (G0–G17) y el sello SHA-256 se recalculó en
el mismo cambio, porque mover archivos cambia la huella y la huella es la que acredita.
