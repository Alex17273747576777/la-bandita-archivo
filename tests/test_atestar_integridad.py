import contextlib, datetime, io, json, pathlib, sys, tempfile, unittest
from unittest.mock import patch
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
import atestar

class IntegridadTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.tmp.name)
        (self.root / "registry").mkdir()
        (self.root / "registry/dato.json").write_text('{"valor": 1}')
        self.patches = [patch.object(atestar, "RAIZ", self.root), patch.object(atestar, "ATTESTATIONS", self.root / "attestations")]
        for p in self.patches: p.start()
        with patch.object(atestar, "_fecha_hoy", return_value=datetime.date(2020, 1, 1)):
            atestar.sellar()
    def tearDown(self):
        for p in reversed(self.patches): p.stop()
        self.tmp.cleanup()
    def test_cambio_de_dia_no_rompe_integridad(self):
        with patch.dict("os.environ", {}, clear=True), patch.object(atestar, "_fecha_hoy", return_value=datetime.date(2020, 1, 2)):
            self.assertEqual(atestar.verificar(), 0)
    def test_contenido_alterado_falla(self):
        (self.root / "registry/dato.json").write_text('{"valor": 2}')
        self.assertEqual(atestar.verificar(), 1)
    def test_manifiesto_viejo_falla(self):
        (self.root / "registry/_manifiesto-sha256.tsv").write_text("viejo")
        self.assertEqual(atestar.verificar(), 1)
    def test_huella_global_alterada_falla(self):
        p = atestar.lote_actual(); data = json.loads(p.read_text()); data["huella"] = "0" * 64; p.write_text(json.dumps(data))
        self.assertEqual(atestar.verificar(), 1)
    def test_bundle_no_se_confunde_con_lote(self):
        (self.root / "attestations/lote-2099-01-01.sigstore.json").write_text("{}")
        self.assertEqual(atestar.lote_actual().name, "lote-2020-01-01.json")
    def test_fecha_invalida_no_se_ignora(self):
        with patch.dict("os.environ", {"LOTE_FECHA": "ayer"}):
            with self.assertRaises(ValueError): atestar._fecha_hoy()
