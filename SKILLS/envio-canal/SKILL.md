---
name: envio-canal
version: 1.0.1
dominio: publicación
cuando: al cerrar un lote, antes de sellar
entradas: [piezas publicadas, medición guardada, canal]
salidas: [envíos por canal en docs/envios/, verificación sin fallos]
herramientas: [tools/envio.py, docs/envios/_medicion-*.json]
verificacion: [envios revisados N · fallos: 0 en ambos canales]
---

# Skill · generar los envíos del canal

## Propósito
Convertir cada pieza en los mensajes que se publican (WhatsApp partido en trozos, Facebook con su
texto), siempre desde la pieza: **el envío es salida, nunca fuente**.

## Uso
```bash
LBT="$PAT_FINO" python3 tools/envio.py --medir              # mide repos y enlaces (una vez por lote)
python3 tools/envio.py --generar --canal ambos              # regenera todos los envíos
python3 tools/envio.py --verificar                          # comprueba que el archivo = lo generado
```

## Pasos
1. Medir con la llave en el entorno (`LBT`), nunca escrita en un archivo.
2. Generar ambos canales.
3. Verificar: si alguien editó un envío a mano, aquí canta.
4. Comprobar que **no hay envíos huérfanos**: cada `.md`/`.json` de `docs/envios/*/` debe tener su
   pieza y cada pieza su envío.

## Reglas duras
- **Nunca editar un envío a mano.** Se corrige la pieza y se regenera.
- Al borrar o renombrar una pieza, **borrar su envío en el mismo commit** (G9).
- Un envío no puede llevar datos que la pieza no tenga: si el envío dice una cifra, la pieza la dice.

## Verificación
`envíos revisados: N · fallos: 0` en los dos canales y `vara.py` G9 en verde.
