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

    def test_g13_con_piezas_reales_cuenta_novedad(self):
        with tempfile.TemporaryDirectory() as tmp:
            pub = Path(tmp) / "01-PUBLICACIONES"
            canal = pub / "es-dominicano"
            canal.mkdir(parents=True)
            (canal / "pieza-01.md").write_text("M24 novedad 2026-11-21", encoding="utf-8")
            (canal / "pieza-02.md").write_text("sin fecha ni marca", encoding="utf-8")
            orig = vara.PUBLICACIONES
            try:
                vara.PUBLICACIONES = pub
                inf = vara.InformeVara()
                vara.g13_novedad(inf)
                c = inf.compuertas[0]
                self.assertTrue(c.pasa)
                self.assertIn("1/2 piezas", c.detalle)
            finally:
                vara.PUBLICACIONES = orig
