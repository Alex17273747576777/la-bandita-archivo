import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]


class TestVaraIdiomas(unittest.TestCase):
    def test_modo_retiro_vigente_verifica_moldes(self) -> None:
        res = subprocess.run(
            [sys.executable, "tools/vara_idiomas.py"],
            cwd=RAIZ,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(res.returncode, 0, res.stdout + res.stderr)
        self.assertIn("SIN PUBLICACIONES", res.stdout)
        self.assertIn("vara_idiomas: NINGUN ROJO", res.stdout)

    def test_ruta_explicita_inexistente_falla(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            res = subprocess.run(
                [sys.executable, "tools/vara_idiomas.py", str(Path(tmp) / "no-existe")],
                cwd=RAIZ,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertNotEqual(res.returncode, 0)
            self.assertIn("ROJOS", res.stdout)


if __name__ == "__main__":
    unittest.main()
