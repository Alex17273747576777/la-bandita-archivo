import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
import feynman_verificar


class FeynmanNormaTest(unittest.TestCase):
    def test_repositorio_cumple_norma_feynman_completa(self):
        fallos = feynman_verificar.verificar()
        self.assertEqual(fallos, [])
