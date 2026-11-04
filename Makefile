.DEFAULT_GOAL := ayuda

# ─────────────────────────────────────────────────────────────────────────────
#  LA BANDITA · arranque y oficio en un solo archivo
#
#  Regla de la casa: si un comando no está aquí, no se ejecuta a mano dos veces.
#  Todo destino de este archivo es idempotente: correrlo dos veces no rompe nada.
# ─────────────────────────────────────────────────────────────────────────────

PY ?= python3

ayuda:  ## Muestra esta ayuda
	@echo ""
	@echo "  LA BANDITA · destinos disponibles"
	@echo ""
	@grep -E "^[a-zA-Z_-]+:.*?## " $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[1m%-12s\033[0m %s\n", $$1, $$2}'
	@echo ""
	@echo "  Primer día:  make doctor  y después  make verificar"
	@echo ""

doctor:  ## Revisa el entorno y dice si el archivo está en condiciones
	@$(PY) tools/doctor.py

verificar:  ## Las compuertas completas: registro, sello, vara y autoprueba
	@$(PY) tools/registro_construir.py --verificar
	@$(PY) tools/atestar.py --verificar
	@$(PY) tools/vara.py
	@$(PY) tools/autoprueba.py

ritual:  ## Verifica, sella y vuelve a verificar — el orden importa (H05, errores E16 y E23)
	-@$(MAKE) --no-print-directory libro
	-@$(PY) tools/registro_construir.py --verificar
	-@$(PY) tools/vara.py >/dev/null
	-@$(PY) tools/autoprueba.py >/dev/null
	@$(PY) tools/atestar.py
	@$(PY) tools/atestar.py --verificar
	@echo "ritual completo: la primera pasada puede fallar por archivos sin sellar; la segunda no"


remedir-pieza:  ## Remide la pieza y escribe su medición con fecha y hora (habilidad H01)
	LBT="$${LBT:?falta LBT}" $(PY) tools/remedir.py --escribir "docs/MEDICION-$$(date +%F).json" --pieza "$${PIEZA:?falta PIEZA}"

vencer:  ## Calcula qué ficha está vigente, cuál por vencer y cuál hay que remedir
	@$(PY) tools/vencimiento.py --aplicar

remedir:  ## Vuelve a medir en fuente primaria las fichas vencidas o sin respaldo (exige LBT)
	LBT="$${LBT:?falta LBT: exportá el token de lectura}" $(PY) tools/censo_medir.py --vencidas --lote 50

referencias:  ## Comprueba que ninguna carpeta movida siga citada por su ruta vieja
	@$(PY) tools/referencias.py

licencias:  ## Comprueba la licencia de cada archivo con REUSE (requiere: pip install reuse)
	@command -v reuse >/dev/null || { echo "falta reuse: pip install reuse"; exit 1; }
	@reuse lint | tail -12

sellar:  ## Re-sella el árbol con su huella SHA-256 encadenada
	@$(PY) tools/atestar.py

compuertas:  ## Solo la vara, sin registro ni autoprueba (el informe corto)
	@$(PY) tools/vara.py

generar:  ## Regenera la guía maestra (datos, textos, páginas y créditos)
	@$(PY) guia-maestra/herramientas/guia_maestra.py --compuertas --generar --estricto

sitio:  ## Regenera el frontend estático de site/
	@$(PY) tools/sitio.py

tareas:  ## Reescribe el tablero de tareas desde las piezas vivas
	@$(PY) tools/tareas.py

indice:  ## Reescribe el índice de docs y de herramientas
	@$(PY) tools/indice_docs.py

libro:  tareas indice  ## Los documentos derivados: tareas e índice

novedad:  ## Encuentra lo nuevo, lo recién publicado y lo desconocido del registro
	@$(PY) tools/novedad.py --joyas 25 --min-calidad 0.6

medir:  ## Mide los repositorios citados y regenera los envíos de canal
	LBT="$${LBT:?falta LBT: exportá el token de lectura}" $(PY) tools/envio.py --medir
	$(PY) tools/envio.py --generar --canal ambos
	$(PY) tools/envio.py --verificar

publicar:  sellar libro verificar  ## Deja el árbol listo para empujar
	@echo ""
	@echo "  Árbol sellado y verificado. Falta el empujón, que necesita el token:"
	@echo "    git add -A && git commit -m \"tipo(alcance): descripción\" && make push"

push:  ## Empuja con el token de la bóveda (nunca se imprime)
	@test -n "$${GHP_A}" || { echo "falta GHP_A"; exit 1; }
	@git push -q "https://x-access-token:$${GHP_A}@github.com/Alex17273747576777/la-bandita-archivo.git" HEAD:main
	@echo "empujado: $$(git rev-parse --short HEAD)"

.PHONY: ayuda doctor verificar vencer remedir referencias licencias sellar compuertas generar sitio tareas indice libro medir publicar push
