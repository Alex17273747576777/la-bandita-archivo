#!/usr/bin/env bash
# Aplica la licencia elegida por el dueño. NO se ejecuta sola: requiere la letra A como argumento.
# Uso: bash LEGAL/aplicar-licencia.sh A
set -euo pipefail
RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OPCION="${1:-}"

if [ "$OPCION" != "A" ]; then
  echo "Este script solo aplica la opción A (CC BY-SA 4.0 contenido · MIT código · CC BY 4.0 datos)."
  echo "Las opciones B, C y D no se automatizan: cambian el régimen de propiedad y se redactan a mano."
  echo "Ver LEGAL/PROPUESTA-LICENCIA.md"
  exit 1
fi

fecha="$(date +%Y)"
read -r -p "Titular del copyright (nombre o marca): " titular
titular="${titular:-Titular por definir}"

cat > "$RAIZ/LICENSE" <<TXT
MIT License

Copyright (c) ${fecha} ${titular} — código de La Bandita (tools/, mcp-labandita-registro/, .github/)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
TXT

cat > "$RAIZ/LICENSE-CONTENIDO" <<TXT
Contenido editorial de La Bandita — ${titular}
Licencia: Creative Commons Atribución-CompartirIgual 4.0 Internacional (CC BY-SA 4.0)
Texto completo: https://creativecommons.org/licenses/by-sa/4.0/legalcode.es

Usted es libre de compartir y adaptar el contenido para cualquier propósito, incluso comercial,
siempre que: (1) atribuya a La Bandita indicando el título de la pieza y su fecha de verificación;
(2) enlace a la licencia; (3) indique si se hicieron cambios; y (4) distribuya las obras derivadas
bajo esta misma licencia.

La marca «La Bandita» y la certificación de verificación NO se ceden por esta licencia.
TXT

cat > "$RAIZ/LICENSE-DATOS" <<TXT
Datos del registro (registry/, censos, mapas de recursos) — ${titular}
Licencia: Creative Commons Atribución 4.0 Internacional (CC BY 4.0)
Texto completo: https://creativecommons.org/licenses/by/4.0/legalcode.es

La atribución debe incluir la fecha de medición declarada en cada ficha (campo medido_en).
Un dato citado sin su fecha no cumple esta atribución.
TXT

cat > "$RAIZ/NOTICE" <<TXT
La Bandita · aviso de licencias y terceros

1. Este repositorio mezcla tres regímenes: contenido (LICENSE-CONTENIDO, CC BY-SA 4.0),
   datos (LICENSE-DATOS, CC BY 4.0) y código (LICENSE, MIT). En caso de duda, la licencia más
   próxima al archivo manda.

2. Los metadatos de repositorios de terceros (estrellas, licencias, fechas de actividad) se citan
   con fines de verificación y conservan la licencia de su proyecto de origen. La Bandita no
   relicencia código ajeno.

3. Las marcas, nombres comerciales y logotipos de terceros pertenecen a sus dueños y se mencionan
   de forma descriptiva.

4. «La Bandita», su firma y su certificación de verificación no se ceden por ninguna de las
   licencias anteriores.

5. Los datos se ofrecen tal como fueron medidos y con su fecha. Si un dato envejece, la licencia
   sigue vigente pero la frescura no: verifique la fecha antes de citarlo.
TXT

echo "Licencia aplicada: MIT (código) · CC BY-SA 4.0 (contenido) · CC BY 4.0 (datos) · titular: ${titular}"
echo "Falta el commit y el push: nada se publica sin que el dueño lo ordene."
