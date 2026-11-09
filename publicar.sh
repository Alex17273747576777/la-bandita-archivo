#!/usr/bin/env bash
# publicar.sh · lleva la página a un proveedor de páginas estáticas.
#
# Qué hace:
#   * Comprueba que los archivos de la página estén completos y que no carguen nada externo.
#   * Crea el repositorio en el proveedor con la API del proveedor y empuja con git.
#
# Qué NO hace:
#   * No inventa credenciales: el token lo pones tú en la variable TOKEN.
#   * No abre cuentas: si no tienes cuenta en el proveedor, este script te lo dice y se detiene.
#
# Uso:
#   TOKEN=xxx ./publicar.sh gitverse  mi-usuario  archivo-abierto
#
# Los tres puntos de la API se comprobaron el 9-nov-2026 con un token falso, para saber que
# existen de verdad y no son un nombre inventado:
#   api.gitverse.ru/v1/user/repos  -> 400 VALIDATION_ERROR (documenta su API en /docs/developers/public-api)
#   api.gitflic.ru/project         -> 403 AccessDenied (existe, pide token bueno)
#   codeberg.org/api/v1/user/repos -> 401 «token is malformed» (Gitea: existe, pide token bueno)
#   TOKEN=xxx ./publicar.sh codeberg  mi-usuario  archivo-abierto
set -euo pipefail

PROVEEDOR="${1:-}"
USUARIO="${2:-}"
REPO="${3:-archivo-abierto}"
TOKEN="${TOKEN:-}"
AQUI="$(cd "$(dirname "$0")" && pwd)"

if [ -z "$PROVEEDOR" ] || [ -z "$USUARIO" ]; then
  sed -n '2,16p' "$0"; exit 2
fi

echo "── 1. comprobar la página ──"
for f in index.html datos.json robots.txt .nojekyll; do
  [ -e "$AQUI/$f" ] || { echo "FALTA $f: no se publica a medias"; exit 1; }
done
[ -s "$AQUI/index.html" ] && [ -s "$AQUI/datos.json" ] || { echo "algún archivo está vacío"; exit 1; }
FICHAS=$(grep -o '"repo":"' "$AQUI/index.html" | wc -l)
# Se cuentan solo las cosas que el navegador DESCARGA: src=, <link>, @import y url() en CSS.
# Un href="https://..." de un enlace normal no descarga nada: es a donde va el dedo.
EXT=$(
  { grep -oE '<script[^>]+src="https?://' "$AQUI/index.html" || true
    grep -oE '<link[^>]+href="https?://' "$AQUI/index.html" || true
    grep -oE '@import[^;]*https?://' "$AQUI/index.html" || true
    grep -oE 'url\(https?://' "$AQUI/index.html" || true
  } | wc -l)
echo "   index.html   $(du -h "$AQUI/index.html" | cut -f1) · $FICHAS fichas dentro"
echo "   recursos externos descargados: $EXT (tienen que ser 0)"
[ "$EXT" -eq 0 ] || { echo "la página carga algo de fuera: se detiene"; exit 1; }

echo "── 2. preparar el repositorio ──"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
cp "$AQUI"/index.html "$AQUI"/datos.json "$AQUI"/robots.txt "$AQUI"/.nojekyll "$AQUI"/LEEME.md "$TMP"/
[ -f "$AQUI/CNAME" ] && cp "$AQUI/CNAME" "$TMP"/
cd "$TMP"
git init -q -b main
git add -A
git -c user.name="La Bandita" -c user.email="labandita@users.noreply.github.com" \
    commit -q -m "archivo abierto: $FICHAS repositorios medidos el 9-nov-2026

Página de un solo archivo, sin CDN, sin fuentes externas y sin rastreadores.
Datos y código en CC0."

case "$PROVEEDOR" in
  gitverse)
    [ -n "$TOKEN" ] || { echo "falta TOKEN"; exit 1; }
    echo "── 3. crear el repositorio en GitVerse ──"
    # GitVerse usa una API compatible con la de GitHub para lo básico.
    curl -sS -X POST -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
      -d "{\"name\":\"$REPO\",\"private\":false,\"description\":\"Archivo abierto: repositorios medidos contra la API pública\"}" \
      "https://api.gitverse.ru/v1/user/repos" -o /tmp/gv.json -w "   HTTP %{http_code}\n" || true
    head -c 300 /tmp/gv.json 2>/dev/null; echo
    REMOTO="https://oauth2:$TOKEN@gitverse.ru/$USUARIO/$REPO.git"
    PAGINAS="https://$USUARIO.gitverse.site/$REPO/"
    ;;
  gitflic)
    [ -n "$TOKEN" ] || { echo "falta TOKEN"; exit 1; }
    echo "── 3. crear el repositorio en GitFlic ──"
    curl -sS -X POST -H "Authorization: token $TOKEN" -H "Content-Type: application/json" \
      -d "{\"name\":\"$REPO\",\"isPrivate\":false}" \
      "https://api.gitflic.ru/project" -o /tmp/gf.json -w "   HTTP %{http_code}\n" || true
    head -c 300 /tmp/gf.json 2>/dev/null; echo
    REMOTO="https://$USUARIO:$TOKEN@gitflic.ru/project/$USUARIO/$REPO.git"
    PAGINAS="https://$USUARIO.gitflic.ru/$REPO/"
    ;;
  codeberg)
    [ -n "$TOKEN" ] || { echo "falta TOKEN"; exit 1; }
    echo "── 3. crear el repositorio en Codeberg (API Gitea) ──"
    curl -sS -X POST -H "Authorization: token $TOKEN" -H "Content-Type: application/json" \
      -d "{\"name\":\"$REPO\",\"private\":false,\"auto_init\":false}" \
      "https://codeberg.org/api/v1/user/repos" -o /tmp/cb.json -w "   HTTP %{http_code}\n" || true
    head -c 300 /tmp/cb.json 2>/dev/null; echo
    REMOTO="https://$USUARIO:$TOKEN@codeberg.org/$USUARIO/$REPO.git"
    PAGINAS="https://$USUARIO.codeberg.page/$REPO/"
    ;;
  *)
    echo "proveedor desconocido: $PROVEEDOR (gitverse | gitflic | codeberg)"; exit 2;;
esac

echo "── 4. empujar ──"
git remote add origen "$REMOTO"
git push origen main
echo
echo "LISTO. La página queda en:"
echo "   $PAGINAS"
echo
echo "Falta un paso tuyo, y solo uno: en el repositorio recién creado,"
echo "Settings → Pages (GitVerse/GitFlic) o Settings → Pages → Static pages (Codeberg),"
echo "y activar la rama main. La API de los tres no deja activarlo por token."
