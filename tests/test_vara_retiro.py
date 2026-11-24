import sys
import tempfile
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "tools"))

import vara  # noqa: E402


class VaraRetiroTest(unittest.TestCase):
    def test_g13_sin_piezas_no_reporta_cifra_fija(self):
        with tempfile.TemporaryDirectory() as tmp:
            orig = vara.PUBLICACIONES
            try:
                vara.PUBLICACIONES = Path(tmp) / "no-existe"
                inf = vara.InformeVara()
                vara.g13_novedad(inf)
                self.assertEqual(len(inf.compuertas), 1)
                c = inf.compuertas[0]
                self.assertTrue(c.pasa)
                self.assertIn("SIN PIEZAS", c.detalle)
                self.assertNotIn("4/7", c.detalle)
            finally:
                vara.PUBLICACIONES = orig

    def test_g13_falla_si_una_pieza_activa_no_pasa_m24_m28(self):
        with tempfile.TemporaryDirectory() as tmp:
            pub = Path(tmp) / "01-PUBLICACIONES"
            canal = pub / "es-dominicano"
            canal.mkdir(parents=True)
            (canal / "pieza-01.md").write_text("M24 novedad 2026-11-21", encoding="utf-8")
            (canal / "pieza-02.md").write_text("sin fecha ni marca", encoding="utf-8")
            orig_pub, orig_cal = vara.PUBLICACIONES, vara.CALENDARIO_NOVEDADES
            try:
                vara.PUBLICACIONES = pub
                vara.CALENDARIO_NOVEDADES = Path(tmp) / "calendario-ausente.json"
                inf = vara.InformeVara()
                vara.g13_novedad(inf)
                c = inf.compuertas[0]
                self.assertFalse(c.pasa)
                self.assertIn("2 piezas", c.detalle)
                self.assertTrue(c.fallos)
            finally:
                vara.PUBLICACIONES, vara.CALENDARIO_NOVEDADES = orig_pub, orig_cal

    def test_g13_pasa_pieza_conforme_y_calendario_vigente(self):
        with tempfile.TemporaryDirectory() as tmp:
            pub = Path(tmp) / "01-PUBLICACIONES"
            canal = pub / "es-dominicano"
            canal.mkdir(parents=True)
            contenido = ("La herramienta owner/repo tiene ★17 y madurez beta declarada. "
                         "Su empujón fue 2026-11-20 y se midió como hallazgo reciente.")
            (canal / "pieza-01.md").write_text(contenido, encoding="utf-8")
            orig_pub, orig_cal = vara.PUBLICACIONES, vara.CALENDARIO_NOVEDADES
            try:
                vara.PUBLICACIONES = pub
                vara.CALENDARIO_NOVEDADES = vara.DOCS / "CALENDARIO-DE-NOVEDADES.json"
                inf = vara.InformeVara()
                vara.g13_novedad(inf)
                c = inf.compuertas[0]
                self.assertTrue(c.pasa, c.fallos)
                self.assertIn("1/1 piezas pasan", c.detalle)
            finally:
                vara.PUBLICACIONES, vara.CALENDARIO_NOVEDADES = orig_pub, orig_cal
