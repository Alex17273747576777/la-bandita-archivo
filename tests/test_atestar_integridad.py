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


class RegistroDbHuellaTest(unittest.TestCase):
    def setUp(self):
        import sqlite3
        self.tmp = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.tmp.name)
        (self.root / "registry").mkdir()
        (self.root / "registry/dato.json").write_text('{"valor": 1}')
        self.db = self.root / "registry/registro.db"
        con = sqlite3.connect(self.db)
        con.execute("CREATE TABLE fichas (id TEXT PRIMARY KEY, repo TEXT)")
        con.execute("INSERT INTO fichas VALUES ('1', 'owner/repo')")
        con.commit()
        con.close()
        self.patches = [patch.object(atestar, "RAIZ", self.root), patch.object(atestar, "ATTESTATIONS", self.root / "attestations")]
        for p in self.patches: p.start()
        with patch.object(atestar, "_fecha_hoy", return_value=datetime.date(2020, 1, 1)):
            self.lote = atestar.sellar()

    def tearDown(self):
        for p in reversed(self.patches): p.stop()
        self.tmp.cleanup()

    def test_registro_db_vacuum_no_rompe_sello(self):
        import sqlite3
        import atestacion_verificar
        self.assertIn("registro_db", self.lote)
        self.assertEqual(self.lote["registro_db"]["tablas"], {"fichas": 1})
        con = sqlite3.connect(self.db)
        con.execute("VACUUM")
        con.close()
        self.assertEqual(atestar.verificar(), 0)
        lote_json = self.root / "attestations/lote-2020-01-01.json"
        self.assertEqual(atestacion_verificar.verificar_registro_db_lote(lote_json, db_path=self.db), [])

    def test_cambio_en_registro_db_rompe_sello(self):
        import sqlite3
        import atestacion_verificar
        con = sqlite3.connect(self.db)
        con.execute("INSERT INTO fichas VALUES ('2', 'owner/otro')")
        con.commit()
        con.close()
        self.assertEqual(atestar.verificar(), 1)
        lote_json = self.root / "attestations/lote-2020-01-01.json"
        fallos = atestacion_verificar.verificar_registro_db_lote(lote_json, db_path=self.db)
        self.assertTrue(any("registro.db" in f for f in fallos))

    def test_medir_piezas_registra_payloads_sha256_de_cache(self):
        import hashlib
        import medir_piezas_24_34
        cache_dir = self.root / "docs/_medicion-cache"
        cache_dir.mkdir(parents=True)
        url = "https://api.github.com/repos/owner/repo"
        clave = hashlib.sha256(url.encode()).hexdigest()[:24]
        raw = b'{"url": "https://api.github.com/repos/owner/repo", "codigo": 200, "cuerpo": {"stargazers_count": 5}}'
        (cache_dir / f"{clave}.json").write_bytes(raw)
        reg = {}
        with patch.object(medir_piezas_24_34, "RAIZ", self.root), patch.object(medir_piezas_24_34, "CACHE", cache_dir):
            code, body = medir_piezas_24_34.pedir(url, registro=reg)
        self.assertEqual(code, 200)
        self.assertEqual(body["stargazers_count"], 5)
        self.assertEqual(reg[f"docs/_medicion-cache/{clave}.json"], hashlib.sha256(raw).hexdigest())


class VencimientoReadOnlyTest(unittest.TestCase):
    def test_compuerta_no_altera_registro_ni_informes(self):
        import vencimiento
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            registry = root / "registry"; registry.mkdir()
            evidence = registry / "_evidencia"; evidence.mkdir()
            docs = root / "docs"; docs.mkdir()
            (evidence / "x.json").write_text('{"fecha":"2026-11-10"}')
            (registry / "x.json").write_text(json.dumps({"id":"x", "repo":"owner/repo", "medido_en":"2026-11-10", "evidencia":{"payload_ref":"registry/_evidencia/x.json"}}))
            (docs / "VENCIMIENTOS.md").write_text("informe conservado")
            (registry / "_vencimientos.json").write_text("{}")
            paths = dict(RAIZ=root, REGISTRO=registry, EVIDENCIA=evidence, DOCS=docs,
                         VENCIMIENTOS_MD=docs/"VENCIMIENTOS.md", VENCIMIENTOS_JSON=registry/"_vencimientos.json", POLITICA=docs/"ausente.json")
            before = {str(p):p.read_bytes() for p in root.rglob("*") if p.is_file()}
            with patch.multiple(vencimiento, **paths), patch.object(vencimiento, "hoy_casa", return_value="2026-11-10"):
                self.assertEqual(vencimiento.main(["--peor"]), 0)
                with self.assertRaises(SystemExit): vencimiento.main(["--peor", "--aplicar"])
            after = {str(p):p.read_bytes() for p in root.rglob("*") if p.is_file()}
            self.assertEqual(before, after)
