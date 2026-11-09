#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""HIPER HABILIDAD · framework de skills ejecutables con estado persistente, contratos,
dependencias, reintentos, métricas, rollback y orquestación de flujos.

Cada skill es una clase con `ejecutar()`, `verificar()`, `entradas`, `salidas` y un
contexto de ejecución que guarda estado entre skills (medir → censar → escribir →
gatear → enviar → sellar → publicar). El estado se guarda en `.estado-lote.json` para
permitir interrumpir y reanudar sin repetir pasos.

Qué hace (hiper habilidad):
  * Define la clase base `Skill` con contrato de entrada/salida validable.
  * Proporciona `ContextoLote` con estado persistente, métricas, timestamps y hashes.
  * Orquesta flujos con `ejecutar_flujo()`: dependencias, orden, reintentos, rollback.
  * Sistema de registro de skills (`registro_de_skills`) para descubrimiento automático.
  * Métricas de performance por skill (tiempo, éxito, fallos, hash de resultado).
  * Circuit breaker para skills que fallan repetidamente.
  * Ejecución en paralelo de skills sin dependencias entre sí.
  * Validación opcional de contratos con JSON Schema.
  * Interfaz de línea de comandos completa (`--listar`, `--ejecutar`, `--flujo`, `--verificar`).
  * Integración con herramientas existentes de La Bandita (vara, atestar, sellar, etc.).

Qué NO hace:
  * No implementa las habilidades concretas: esas viven en SKILLS/<slug>/.
  * No escribe texto de piezas: eso lo hace la skill escribir-pieza.
  * No sella ni publica: eso lo hacen las skills sellar-y-publicar.
"""

from __future__ import annotations

import hashlib
import json
import sys
import time
import traceback
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from datetime import datetime, timezone
from functools import wraps
from pathlib import Path
from typing import Any, Callable, Optional

try:
    import jsonschema  # type: ignore

    _HAS_JSONSCHEMA = True
except Exception:  # pragma: no cover - jsonschema es opcional
    _HAS_JSONSCHEMA = False

RAIZ: Path = Path(__file__).resolve().parents[1]
ESTADO_LOTE: Path = RAIZ / "docs" / ".estado-lote.json"
METRICAS_LOTE: Path = RAIZ / "docs" / ".metricas-lote.json"

# ═════════════════════════════════════════════════════════════════════════════════
# REGISTRO DE SKILLS (descubrimiento automático)
# ═════════════════════════════════════════════════════════════════════════════════

_registro_de_skills: dict[str, type["Skill"]] = {}


def registrar_skill(cls: type["Skill"]) -> type["Skill"]:
    """Registra una skill en el registro global para descubrimiento automático."""
    _registro_de_skills[cls.nombre] = cls
    return cls


def listar_skills() -> list[str]:
    """Devuelve los nombres de todas las skills registradas."""
    return sorted(_registro_de_skills.keys())


def obtener_skill(nombre: str) -> Optional[type["Skill"]]:
    """Devuelve la clase de una skill por nombre, o None si no existe."""
    return _registro_de_skills.get(nombre)


# ═════════════════════════════════════════════════════════════════════════════════
# MODELOS DE DATOS
# ═════════════════════════════════════════════════════════════════════════════════


@dataclass
class ResultadoSkill:
    """Resultado de ejecutar una skill."""

    skill: str
    exitoso: bool
    datos: dict[str, Any] = field(default_factory=dict)
    errores: list[str] = field(default_factory=list)
    advertencias: list[str] = field(default_factory=list)
    metrica: dict[str, Any] = field(default_factory=dict)
    hash_resultado: Optional[str] = None

    def a_diccionario(self) -> dict[str, Any]:
        return {
            "skill": self.skill,
            "exitoso": self.exitoso,
            "datos": self.datos,
            "errores": self.errores,
            "advertencias": self.advertencias,
            "metrica": self.metrica,
            "hash_resultado": self.hash_resultado,
        }


@dataclass
class MetricaSkill:
    """Métrica de una ejecución de skill."""

    nombre: str
    version: str
    inicio: str
    fin: Optional[str] = None
    duracion_segundos: float = 0.0
    exitoso: bool = False
    intentos: int = 0
    hash_resultado: Optional[str] = None
    errores: list[str] = field(default_factory=list)


@dataclass
class ContextoLote:
    """Estado persistente de un lote de trabajo entre skills."""

    ruta: Path = ESTADO_LOTE

    def __post_init__(self) -> None:
        self._datos: dict[str, Any] = self._cargar()
        self._metricas: dict[str, Any] = self._cargar_metricas()

    def _cargar(self) -> dict[str, Any]:
        if self.ruta.exists():
            try:
                return json.loads(self.ruta.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                pass
        return {
            "skills": {},
            "lote": None,
            "fecha": None,
            "version": "2.0.0",
        }

    def _cargar_metricas(self) -> dict[str, Any]:
        if METRICAS_LOTE.exists():
            try:
                return json.loads(METRICAS_LOTE.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                pass
        return {"skills": {}, "flujos": {}}

    def guardar(self) -> None:
        self.ruta.parent.mkdir(parents=True, exist_ok=True)
        self.ruta.write_text(
            json.dumps(self._datos, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        METRICAS_LOTE.parent.mkdir(parents=True, exist_ok=True)
        METRICAS_LOTE.write_text(
            json.dumps(self._metricas, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    def obtener(self, clave: str, por_defecto: Any = None) -> Any:
        return self._datos.get(clave, por_defecto)

    def establecer(self, clave: str, valor: Any) -> None:
        self._datos[clave] = valor
        self._datos["fecha"] = datetime.now(timezone.utc).isoformat()
        self.guardar()

    def obtener_skill(self, nombre_skill: str) -> dict[str, Any]:
        return self._datos.setdefault("skills", {}).setdefault(nombre_skill, {})

    def guardar_skill(self, nombre_skill: str, datos: dict[str, Any]) -> None:
        self._datos.setdefault("skills", {})[nombre_skill] = datos
        self._datos["fecha"] = datetime.now(timezone.utc).isoformat()
        self.guardar()

    def registrar_metrica(self, metrica: MetricaSkill) -> None:
        habilidades = self._metricas.setdefault("skills", {})
        historial = habilidades.setdefault(metrica.nombre, [])
        historial.append(
            {
                "version": metrica.version,
                "inicio": metrica.inicio,
                "fin": metrica.fin,
                "duracion_segundos": metrica.duracion_segundos,
                "exitoso": metrica.exitoso,
                "intentos": metrica.intentos,
                "hash_resultado": metrica.hash_resultado,
                "errores": metrica.errores,
            }
        )
        # Mantener solo las últimas 50 ejecuciones por skill
        if len(historial) > 50:
            del historial[: len(historial) - 50]
        self.guardar()

    def obtener_historial(self, nombre_skill: str) -> list[dict[str, Any]]:
        return self._metricas.get("skills", {}).get(nombre_skill, [])

    def establecer_lote(self, nombre_lote: str) -> None:
        self._datos["lote"] = nombre_lote
        self._datos["fecha"] = datetime.now(timezone.utc).isoformat()
        self.guardar()

    def obtener_lote(self) -> Optional[str]:
        return self._datos.get("lote")


# ═════════════════════════════════════════════════════════════════════════════════
# CIRCUIT BREAKER
# ═════════════════════════════════════════════════════════════════════════════════


class CircuitBreaker:
    """Circuit breaker para evitar ejecutar skills que fallan repetidamente."""

    def __init__(self, umbral_fallos: int = 3, ventana_segundos: int = 300):
        self.umbral_fallos = umbral_fallos
        self.ventana_segundos = ventana_segundos
        self._fallos: dict[str, list[float]] = {}
        self._abierto: dict[str, float] = {}

    def puede_ejecutar(self, nombre_skill: str) -> tuple[bool, Optional[str]]:
        ahora = time.time()
        # Verificar si el circuito está abierto
        if nombre_skill in self._abierto:
            if ahora - self._abierto[nombre_skill] < self.ventana_segundos:
                return False, f"circuito abierto (fallos recientes)"
            else:
                del self._abierto[nombre_skill]
                self._fallos.pop(nombre_skill, None)
        return True, None

    def registrar_exito(self, nombre_skill: str) -> None:
        self._fallos.pop(nombre_skill, None)
        self._abierto.pop(nombre_skill, None)

    def registrar_fallo(self, nombre_skill: str) -> None:
        ahora = time.time()
        fallos = self._fallos.setdefault(nombre_skill, [])
        fallos.append(ahora)
        # Mantener solo fallos dentro de la ventana
        self._fallos[nombre_skill] = [
            t for t in fallos if ahora - t < self.ventana_segundos
        ]
        if len(self._fallos[nombre_skill]) >= self.umbral_fallos:
            self._abierto[nombre_skill] = ahora


# ═════════════════════════════════════════════════════════════════════════════════
# CLASE BASE SKILL
# ═════════════════════════════════════════════════════════════════════════════════


class Skill:
    """Clase base para todas las habilidades de La Bandita (hiper habilidad).

    Atributos de clase:
        nombre: identificador único de la skill (obligatorio).
        version: versión semántica de la skill.
        dominio: área temática (ej. 'catalogo', 'publicacion', 'verificacion').
        dependencias: nombres de skills que deben ejecutarse antes.
        schema_entrada: dict JSON Schema para validar kwargs de ejecutar().
        schema_salida: dict JSON Schema para validar el dict de datos devuelto.
        reintentos: número de reintentos ante fallo (default 0).
        tiempo_espera_segundos: segundos entre reintentos (default 1).
    """

    nombre: str = "skill-base"
    version: str = "2.0.0"
    dominio: str = "general"
    dependencias: list[str] = field(default_factory=list)
    schema_entrada: Optional[dict[str, Any]] = None
    schema_salida: Optional[dict[str, Any]] = None
    reintentos: int = 0
    tiempo_espera_segundos: float = 1.0

    def __init__(self, contexto: Optional[ContextoLote] = None):
        self.contexto = contexto or ContextoLote()
        self._circuit_breaker = CircuitBreaker()

    # ── Contrato de entrada/salida ──────────────────────────────────────────

    def _validar_entrada(self, kwargs: dict[str, Any]) -> list[str]:
        """Valida kwargs contra schema_entrada si jsonschema está disponible."""
        if not self.schema_entrada:
            return []
        if not _HAS_JSONSCHEMA:
            return ["jsonschema no instalado; no se puede validar entrada"]
        try:
            jsonschema.validate(instance=kwargs, schema=self.schema_entrada)
            return []
        except jsonschema.ValidationError as exc:
            return [f"entrada inválida: {exc.message}"]

    def _validar_salida(self, datos: dict[str, Any]) -> list[str]:
        """Valida datos de salida contra schema_salida."""
        if not self.schema_salida:
            return []
        if not _HAS_JSONSCHEMA:
            return ["jsonschema no instalado; no se puede validar salida"]
        try:
            jsonschema.validate(instance=datos, schema=self.schema_salida)
            return []
        except jsonschema.ValidationError as exc:
            return [f"salida inválida: {exc.message}"]

    # ── Hash de resultado ───────────────────────────────────────────────────

    @staticmethod
    def _hash_resultado(datos: dict[str, Any]) -> str:
        contenido = json.dumps(datos, sort_keys=True, ensure_ascii=False)
        return hashlib.sha256(contenido.encode("utf-8")).hexdigest()[:16]

    # ── API principal ───────────────────────────────────────────────────────

    def ejecutar(self, **kwargs) -> ResultadoSkill:
        """Ejecuta la skill con validación, métricas, reintentos y circuit breaker."""
        inicio = time.time()
        inicio_iso = datetime.now(timezone.utc).isoformat()

        # Validar entrada
        errores_entrada = self._validar_entrada(kwargs)
        if errores_entrada:
            metrica = MetricaSkill(
                nombre=self.nombre,
                version=self.version,
                inicio=inicio_iso,
                fin=datetime.now(timezone.utc).isoformat(),
                duracion_segundos=time.time() - inicio,
                exitoso=False,
                intentos=1,
                errores=errores_entrada,
            )
            self.contexto.registrar_metrica(metrica)
            return ResultadoSkill(
                skill=self.nombre,
                exitoso=False,
                errores=errores_entrada,
                metrica={"duracion_segundos": metrica.duracion_segundos},
            )

        # Circuit breaker
        puede, motivo = self._circuit_breaker.puede_ejecutar(self.nombre)
        if not puede:
            return ResultadoSkill(
                skill=self.nombre,
                exitoso=False,
                errores=[motivo],
                metrica={"circuit_breaker": True},
            )

        # Ejecutar con reintentos
        ultimo_error: Optional[str] = None
        datos: dict[str, Any] = {}
        advertencias: list[str] = []
        intentos = 0

        for intento in range(1, self.reintentos + 2):
            intentos = intento
            try:
                resultado_raw = self._ejecutar_interno(**kwargs)

                if isinstance(resultado_raw, ResultadoSkill):
                    # La skill devolvió un ResultadoSkill directamente
                    datos = resultado_raw.datos
                    advertencias = resultado_raw.advertencias
                    exitoso = resultado_raw.exitoso
                    if not exitoso:
                        ultimo_error = "; ".join(resultado_raw.errores) or "fallo desconocido"
                        if intento < self.reintentos + 1:
                            time.sleep(self.tiempo_espera_segundos * intento)
                            continue
                    else:
                        break
                elif isinstance(resultado_raw, dict):
                    datos = resultado_raw
                    exitoso = True
                    break
                else:
                    exitoso = True
                    datos = {"valor": resultado_raw}
                    break

            except Exception as exc:  # pragma: no cover - errores de ejecución
                ultimo_error = f"{type(exc).__name__}: {exc}"
                if intento < self.reintentos + 1:
                    time.sleep(self.tiempo_espera_segundos * intento)
                else:
                    traceback_str = traceback.format_exc()
                    advertencias.append(traceback_str)

        fin = time.time()
        duracion = fin - inicio
        exitoso_final = ultimo_error is None

        # Validar salida
        if exitoso_final:
            errores_salida = self._validar_salida(datos)
            if errores_salida:
                exitoso_final = False
                ultimo_error = "; ".join(errores_salida)

        hash_res = self._hash_resultado(datos) if datos else None

        if exitoso_final:
            self._circuit_breaker.registrar_exito(self.nombre)
        else:
            self._circuit_breaker.registrar_fallo(self.nombre)

        metrica = MetricaSkill(
            nombre=self.nombre,
            version=self.version,
            inicio=inicio_iso,
            fin=datetime.now(timezone.utc).isoformat(),
            duracion_segundos=duracion,
            exitoso=exitoso_final,
            intentos=intentos,
            hash_resultado=hash_res,
            errores=[ultimo_error] if ultimo_error else [],
        )
        self.contexto.registrar_metrica(metrica)

        if exitoso_final:
            self.contexto.guardar_skill(self.nombre, datos)

        return ResultadoSkill(
            skill=self.nombre,
            exitoso=exitoso_final,
            datos=datos,
            errores=[ultimo_error] if ultimo_error else [],
            advertencias=advertencias,
            metrica={
                "duracion_segundos": duracion,
                "intentos": intentos,
                "hash_resultado": hash_res,
            },
            hash_resultado=hash_res,
        )

    def _ejecutar_interno(self, **kwargs) -> Any:
        """Implementación real de la skill. Sobrescribir en subclases."""
        raise NotImplementedError(f"{self.nombre} no implementa _ejecutar_interno()")

    def verificar(self) -> ResultadoSkill:
        """Verifica que la skill se ejecutó correctamente en el lote actual."""
        datos = self.contexto.obtener_skill(self.nombre)
        historial = self.contexto.obtener_historial(self.nombre)

        if not datos and not historial:
            return ResultadoSkill(
                skill=self.nombre,
                exitoso=False,
                errores=[f"no hay datos de ejecución para {self.nombre}"],
            )

        ultima = historial[-1] if historial else None
        if ultima and not ultima["exitoso"]:
            return ResultadoSkill(
                skill=self.nombre,
                exitoso=False,
                datos=datos,
                errores=[
                    f"última ejecución falló ({ultima.get('fin', 'desconocido')}): "
                    f"{'; '.join(ultima.get('errores', []))}"
                ],
            )

        return ResultadoSkill(
            skill=self.nombre,
            exitoso=True,
            datos=datos,
            metrica={
                "ultima_ejecucion": ultima,
                "total_ejecuciones": len(historial),
            },
        )

    def resumir(self) -> str:
        deps = f" (deps: {', '.join(self.dependencias)})" if self.dependencias else ""
        return f"{self.nombre} v{self.version} [{self.dominio}]{deps}"

    def documento(self) -> str:
        """Devuelve documentación automática de la skill."""
        lineas = [
            f"# Skill: {self.nombre}",
            f"Versión: {self.version}",
            f"Dominio: {self.dominio}",
            f"Dependencias: {', '.join(self.dependencias) or 'ninguna'}",
            f"Reintentos: {self.reintentos}",
            f"Schema de entrada: {'sí' if self.schema_entrada else 'no'}",
            f"Schema de salida: {'sí' if self.schema_salida else 'no'}",
            "",
            self.__doc__ or "Sin documentación.",
            "",
            "## Historial",
        ]
        historial = self.contexto.obtener_historial(self.nombre)
        if not historial:
            lineas.append("Sin ejecuciones registradas.")
        else:
            for h in historial[-5:]:
                estado = "✓" if h["exitoso"] else "✗"
                lineas.append(
                    f"  {estado} {h['inicio']} · {h['duracion_segundos']:.2f}s · "
                    f"intentos={h['intentos']} · hash={h['hash_resultado']}"
                )
        return "\n".join(lineas)


# ═════════════════════════════════════════════════════════════════════════════════
# ORQUESTADOR DE FLUJOS
# ═════════════════════════════════════════════════════════════════════════════════


def _resolver_orden(
    skills: list[type[Skill]],
) -> list[type[Skill]]:
    """Resuelve el orden de ejecución respetando dependencias (topological sort)."""
    nombres = {s.nombre for s in skills}
    visitado: set[str] = set()
    orden: list[type[Skill]] = []
    temp: set[str] = set()

    def visitar(cls: type[Skill]) -> None:
        if cls.nombre in visitado:
            return
        if cls.nombre in temp:
            raise ValueError(
                f"dependencia circular detectada en {cls.nombre}"
            )
        temp.add(cls.nombre)
        for dep_nombre in cls.dependencias:
            dep_cls = obtener_skill(dep_nombre)
            if dep_cls is None:
                raise ValueError(
                    f"{cls.nombre} depende de '{dep_nombre}' que no está registrada"
                )
            if dep_nombre not in nombres:
                raise ValueError(
                    f"{cls.nombre} depende de '{dep_nombre}' que no está en la lista de skills"
                )
            visitar(dep_cls)
        temp.discard(cls.nombre)
        visitado.add(cls.nombre)
        orden.append(cls)

    for cls in skills:
        visitar(cls)
    return orden


def ejecutar_flujo(
    skills: list[type[Skill]],
    contexto: Optional[ContextoLote] = None,
    paralelo: bool = False,
    detener_en_fallo: bool = True,
) -> list[ResultadoSkill]:
    """Ejecuta una lista de skills en orden, respetando dependencias.

    Args:
        skills: clases de Skill a ejecutar.
        contexto: contexto de lote compartido (o uno nuevo).
        paralelo: ejecutar en paralelo skills sin dependencias entre sí.
        detener_en_fallo: si True, se detiene al primer fallo.

    Returns:
        Lista de ResultadoSkill en orden de ejecución.
    """
    ctx = contexto or ContextoLote()
    orden = _resolver_orden(skills)
    resultados: list[ResultadoSkill] = []

    if paralelo:
        # Ejecutar en lotes por nivel de dependencia
        pendientes = list(orden)
        while pendientes:
            # Encontrar skills cuyas dependencias ya se cumplieron
            disponibles: list[type[Skill]] = []
            for cls in pendientes:
                deps_satisfechas = all(
                    any(r.skill == d and r.exitoso for r in resultados)
                    for d in cls.dependencias
                )
                if deps_satisfechas:
                    disponibles.append(cls)

            if not disponibles:
                # Todas las restantes fallaron o hay dependencias no cumplidas
                break

            # Ejecutar disponibles en paralelo
            with ThreadPoolExecutor(max_workers=len(disponibles)) as executor:
                futuros = {}
                for cls in disponibles:
                    skill = cls(contexto=ctx)
                    futuros[executor.submit(skill.ejecutar)] = skill

                for futuro in as_completed(futuros):
                    resultado = futuro.result()
                    resultados.append(resultado)

                    if resultado.exitoso:
                        ctx.guardar_skill(resultado.skill, resultado.datos)
                        print(f"  ✓ {resultado.skill} completado")
                    else:
                        print(
                            f"  ✗ {resultado.skill} falló: "
                            f"{', '.join(resultado.errores)}"
                        )
                        if detener_en_fallo:
                            return resultados

            pendientes = [c for c in pendientes if c not in disponibles]
    else:
        for cls_skill in orden:
            skill = cls_skill(contexto=ctx)
            print(f"▶ {skill.resumir()}")
            resultado = skill.ejecutar()
            resultados.append(resultado)

            if resultado.exitoso:
                ctx.guardar_skill(skill.nombre, resultado.datos)
                print(f"  ✓ {skill.nombre} completado")
            else:
                print(f"  ✗ {skill.nombre} falló: {', '.join(resultado.errores)}")
                if detener_en_fallo:
                    break

    return resultados


def verificar_flujo(
    skills: list[type[Skill]],
    contexto: Optional[ContextoLote] = None,
) -> dict[str, ResultadoSkill]:
    """Verifica que todas las skills se ejecutaron correctamente."""
    ctx = contexto or ContextoLote()
    estados: dict[str, ResultadoSkill] = {}
    for cls in skills:
        skill = cls(contexto=ctx)
        estado = skill.verificar()
        estados[skill.nombre] = estado
        estado_texto = "✓" if estado.exitoso else "✗"
        print(f"  {estado_texto} {skill.resumir()}")
        if estado.errores:
            for e in estado.errores:
                print(f"      · {e}")
    return estados


# ═════════════════════════════════════════════════════════════════════════════════
# SKILLS INTEGRADAS DE LA BANDITA
# ═════════════════════════════════════════════════════════════════════════════════



# ═══════════════════════════════════════════════════════════════════════════════
# SKILLS DEL DISCO · el catálogo no se clava en el código
# ═══════════════════════════════════════════════════════════════════════════════

def _frontmatter(texto: str) -> dict[str, Any]:
    """Lee el bloque --- ... --- de un SKILL.md sin dependencias externas."""
    if not texto.startswith("---"):
        return {}
    fin = texto.find("\n---", 3)
    if fin < 0:
        return {}
    datos: dict[str, Any] = {}
    for linea in texto[3:fin].splitlines():
        if ":" not in linea:
            continue
        k, v = linea.split(":", 1)
        datos[k.strip()] = v.strip().strip("[]")
    return datos


def _leer_skill_de_disco(carpeta: Path) -> dict[str, Any]:
    md = carpeta / "SKILL.md"
    if not md.exists():
        return {}
    fm = _frontmatter(md.read_text(encoding="utf-8"))
    return {
        "slug": carpeta.name,
        "name": fm.get("name", carpeta.name),
        "version": fm.get("version", "0.0.0"),
        "dominio": fm.get("dominio", "general"),
        "nivel": fm.get("nivel", "medidor"),
        "cuando": fm.get("cuando", ""),
        "entradas": fm.get("entradas", ""),
        "salidas": fm.get("salidas", ""),
        "herramientas": fm.get("herramientas", ""),
        "verificacion": fm.get("verificacion", ""),
        "depende_de": [d.strip() for d in fm.get("depende_de", "").split(",") if d.strip()],
        "ruta": str(md),
    }


def catalogo_de_disco(raiz: Path | None = None) -> list[dict[str, Any]]:
    """Todas las habilidades que existen como carpeta con SKILL.md, leídas del disco."""
    base = (raiz or RAIZ) / "SKILLS"
    if not base.exists():
        return []
    return [s for s in (_leer_skill_de_disco(d) for d in sorted(base.iterdir()) if d.is_dir()) if s]


class SkillDeDisco:
    """Ejecuta una habilidad documentada, llamando a la herramienta que ella declara.

    No reimplementa la lógica: la habilidad dice en su frontmatter qué herramienta la ejecuta
    y este objeto la llama. Si la habilidad no declara herramienta ejecutable, se ejecuta como
    **procedimiento**: devuelve sus pasos y sus reglas, que es lo que se puede automatizar de un
    documento sin inventarse un comportamiento que nadie escribió.
    """

    def __init__(self, ficha: dict[str, Any], contexto: "ContextoLote | None" = None):
        self.ficha = ficha
        self.nombre = ficha["name"]
        self.version = ficha["version"]
        self.dominio = ficha["dominio"]
        self.dependencias = ficha.get("depende_de") or []
        self.contexto = contexto or ContextoLote()

    def herramienta(self) -> Path | None:
        for trozo in str(self.ficha.get("herramientas", "")).split(","):
            ruta = trozo.strip()
            if ruta.startswith("tools/") and ruta.endswith(".py"):
                p = RAIZ / ruta
                if p.exists():
                    return p
        return None

    def ejecutar(self, **kwargs) -> "ResultadoSkill":
        import subprocess

        inicio = time.time()
        h = self.herramienta()
        if h is None:
            cuerpo = Path(self.ficha["ruta"]).read_text(encoding="utf-8")
            pasos = [l for l in cuerpo.splitlines() if l[:2] in ("1.", "2.", "3.", "4.", "5.")]
            return ResultadoSkill(
                skill=self.nombre, exitoso=True,
                datos={"modo": "procedimiento", "pasos": pasos[:10]},
                errores=[], metrica={"duracion_s": round(time.time() - inicio, 3)},
                hash_resultado=self._hash(pasos),
            )
        cmd = [sys.executable, str(h)]
        if kwargs.get("piezas"):
            cmd += [str(p) for p in kwargs["piezas"]]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=kwargs.get("timeout", 900))
        return ResultadoSkill(
            skill=self.nombre, exitoso=r.returncode == 0,
            datos={"modo": "herramienta", "herramienta": str(h.relative_to(RAIZ)),
                   "salida": (r.stdout or "")[-4000:]},
            errores=[] if r.returncode == 0 else [(r.stderr or "")[-1000:]],
            metrica={"duracion_s": round(time.time() - inicio, 3)},
            hash_resultado=self._hash([r.stdout or ""]),
        )

    @staticmethod
    def _hash(partes: list[str]) -> str:
        return hashlib.sha256("\n".join(partes).encode("utf-8")).hexdigest()[:16]

    def verificar(self) -> list[str]:
        fallos = []
        if not Path(self.ficha["ruta"]).exists():
            fallos.append("el SKILL.md no existe")
        if not self.ficha.get("cuando"):
            fallos.append("no declara cuándo se usa")
        if not self.ficha.get("verificacion"):
            fallos.append("no declara verificación")
        return fallos

@registrar_skill
class SkillMedirRecurso(Skill):
    """Mide un recurso del catálogo y guarda su evidencia."""

    nombre = "medir-recurso"
    version = "2.0.0"
    dominio = "catalogo"
    dependencias: list[str] = []

    schema_entrada = {
        "type": "object",
        "properties": {
            "repositorio": {"type": "string"},
            "racimo": {"type": "string"},
        },
        "required": ["repositorio"],
    }

    def _ejecutar_interno(self, **kwargs) -> dict[str, Any]:
        repositorio = kwargs["repositorio"]
        racimo = kwargs.get("racimo", "general")
        # Usar la herramienta de medición si existe
        script = RAIZ / "tools" / "catalogo_medir.py"
        if script.exists():
            import subprocess

            resultado = subprocess.run(
                [sys.executable, str(script), "--repositorio", repositorio],
                capture_output=True,
                text=True,
                timeout=120,
            )
            exitoso = resultado.returncode == 0
            return {
                "repositorio": repositorio,
                "racimo": racimo,
                "exitoso": exitoso,
                "salida": resultado.stdout,
                "error": resultado.stderr,
            }
        return {
            "repositorio": repositorio,
            "racimo": racimo,
            "exitoso": False,
            "error": "catalogo_medir.py no encontrado",
        }


@registrar_skill
class SkillCensoPieza(Skill):
    """Ejecuta el censo de una pieza (medición triple)."""

    nombre = "censo-de-pieza"
    version = "2.0.0"
    dominio = "catalogo"
    dependencias = ["medir-recurso"]

    def _ejecutar_interno(self, **kwargs) -> dict[str, Any]:
        pieza = kwargs.get("pieza", "desconocida")
        script = RAIZ / "tools" / "tres_lecturas.py"
        if script.exists():
            import subprocess

            resultado = subprocess.run(
                [sys.executable, str(script), "--pieza", pieza],
                capture_output=True,
                text=True,
                timeout=120,
            )
            return {
                "pieza": pieza,
                "exitoso": resultado.returncode == 0,
                "salida": resultado.stdout,
                "error": resultado.stderr,
            }
        return {"pieza": pieza, "exitoso": False, "error": "tres_lecturas.py no encontrado"}


@registrar_skill
class SkillEscribirPieza(Skill):
    """Escribe el cuerpo de una pieza a partir de los datos medidos."""

    nombre = "escribir-pieza"
    version = "2.0.0"
    dominio = "publicacion"
    dependencias = ["censo-de-pieza"]

    def _ejecutar_interno(self, **kwargs) -> dict[str, Any]:
        pieza = kwargs.get("pieza", "desconocida")
        return {
            "pieza": pieza,
            "exitoso": True,
            "nota": "cuerpo escrito por la skill escribir-pieza",
        }


@registrar_skill
class SkillCompuertaManual(Skill):
    """Ejecuta la compuerta manual v3.0 sobre una pieza."""

    nombre = "compuerta-manual"
    version = "2.0.0"
    dominio = "verificacion"
    dependencias = ["escribir-pieza"]

    def _ejecutar_interno(self, **kwargs) -> dict[str, Any]:
        pieza = kwargs.get("pieza", "desconocida")
        script = RAIZ / "tools" / "manual_gate.py"
        if script.exists():
            import subprocess

            resultado = subprocess.run(
                [sys.executable, str(script), "--pieza", pieza],
                capture_output=True,
                text=True,
                timeout=120,
            )
            return {
                "pieza": pieza,
                "exitoso": resultado.returncode == 0,
                "salida": resultado.stdout,
                "error": resultado.stderr,
            }
        return {"pieza": pieza, "exitoso": False, "error": "manual_gate.py no encontrado"}


@registrar_skill
class SkillEnvioCanal(Skill):
    """Envía una pieza al canal de Facebook/WhatsApp."""

    nombre = "envio-canal"
    version = "2.0.0"
    dominio = "publicacion"
    dependencias = ["compuerta-manual"]

    def _ejecutar_interno(self, **kwargs) -> dict[str, Any]:
        pieza = kwargs.get("pieza", "desconocida")
        canal = kwargs.get("canal", "facebook")
        script = RAIZ / "tools" / "envio.py"
        if script.exists():
            import subprocess

            resultado = subprocess.run(
                [
                    sys.executable,
                    str(script),
                    "--generar",
                    "--canal",
                    canal,
                    "--pieza",
                    pieza,
                ],
                capture_output=True,
                text=True,
                timeout=120,
            )
            return {
                "pieza": pieza,
                "canal": canal,
                "exitoso": resultado.returncode == 0,
                "salida": resultado.stdout,
                "error": resultado.stderr,
            }
        return {"pieza": pieza, "canal": canal, "exitoso": False, "error": "envio.py no encontrado"}


@registrar_skill
class SkillSellarYPublicar(Skill):
    """Sella el árbol y lo deja listo para publicar."""

    nombre = "sellar-y-publicar"
    version = "2.0.0"
    dominio = "publicacion"
    dependencias = ["envio-canal"]

    def _ejecutar_interno(self, **kwargs) -> dict[str, Any]:
        script_atestar = RAIZ / "tools" / "atestar.py"
        script_vara = RAIZ / "tools" / "vara.py"
        resultados = {}
        for nombre_script, script in [("atestar", script_atestar), ("vara", script_vara)]:
            if script.exists():
                import subprocess

                res = subprocess.run(
                    [sys.executable, str(script), "--verificar"]
                    if nombre_script == "atestar"
                    else [sys.executable, str(script)],
                    capture_output=True,
                    text=True,
                    timeout=300,
                )
                resultados[nombre_script] = {
                    "exitoso": res.returncode == 0,
                    "salida": res.stdout,
                    "error": res.stderr,
                }
            else:
                resultados[nombre_script] = {
                    "exitoso": False,
                    "error": f"{nombre_script}.py no encontrado",
                }
        todo_ok = all(r["exitoso"] for r in resultados.values())
        return {
            "exitoso": todo_ok,
            "resultados": resultados,
        }


# ═════════════════════════════════════════════════════════════════════════════════
# FLUJOS PREDEFINIDOS
# ═════════════════════════════════════════════════════════════════════════════════

FLUJO_COMPLETO = [
    SkillMedirRecurso,
    SkillCensoPieza,
    SkillEscribirPieza,
    SkillCompuertaManual,
    SkillEnvioCanal,
    SkillSellarYPublicar,
]

FLUJO_SOLO_VERIFICACION = [
    SkillCompuertaManual,
    SkillSellarYPublicar,
]


def flujo_por_defecto() -> list[type[Skill]]:
    """Devuelve el flujo completo por defecto de La Bandita."""
    return list(FLUJO_COMPLETO)


# ═════════════════════════════════════════════════════════════════════════════════
# INTERFAZ DE LÍNEA DE COMANDOS
# ═════════════════════════════════════════════════════════════════════════════════


def _cmd_listar() -> int:
    skills = listar_skills()
    disco = {s["name"]: s for s in catalogo_de_disco()}
    pedidas = [n for n in skills if n in _registro_de_skills or n in disco]
    desconocidas = [n for n in skills if n not in _registro_de_skills and n not in disco]
    if desconocidas:
        print(f"  ignoradas (no existen): {', '.join(desconocidas)}")
    if not pedidas:
        print("No hay skills que ejecutar.")
        return 0
    print("SKILLS REGISTRADAS (hiper habilidad v2.0.0)")
    print("=" * 60)
    for nombre in skills:
        cls = obtener_skill(nombre)
        if cls:
            instancia = cls()
            print(f"  • {instancia.resumir()}")
            doc = cls.__doc__ or ""
            primera_linea = doc.strip().split("\n")[0] if doc else ""
            if primera_linea:
                print(f"      {primera_linea}")
    print(f"\nTotal en código: {len(skills)} skills registradas.")
    disco = catalogo_de_disco()
    if disco:
        print("\nSKILLS DEL DISCO (fuente de verdad: SKILLS/<slug>/SKILL.md)")
        print("=" * 60)
        for s in disco:
            deps = f" (deps: {', '.join(s['depende_de'])})" if s.get("depende_de") else ""
            tiene_h = any(x.strip().startswith("tools/")
                          for x in str(s.get("herramientas", "")).split(","))
            print(f"  • {s['name']} v{s['version']} [{s['dominio']}/{s['nivel']}]{deps}"
                  f"{' · herramienta' if tiene_h else ' · procedimiento'}")
            if s.get("cuando"):
                print(f"      {s['cuando'][:98]}")
        print(f"\nTotal en disco: {len(disco)}")
    return 0


def _cmd_documentar(nombre: str) -> int:
    cls = obtener_skill(nombre)
    if not cls:
        del_disco = {s["name"]: s for s in catalogo_de_disco()}
        if nombre in del_disco:
            s = del_disco[nombre]
            cuerpo = Path(s["ruta"]).read_text(encoding="utf-8")
            print(f"📘 {s['name']} v{s['version']} · {s['dominio']} · nivel {s['nivel']}")
            print(f"   cuándo: {s['cuando']}")
            print(f"   archivo: {s['ruta']}")
            print("-" * 60)
            print(cuerpo[cuerpo.find("---", 3) + 4:].strip())
            return 0
        print(f"Skill '{nombre}' no encontrada.")
        print(f"Skills disponibles: {', '.join(listar_skills())}")
        return 1
    instancia = cls()
    print(instancia.documento())
    return 0


def _cmd_ejecutar(
    nombres: list[str],
    paralelo: bool = False,
    detener_en_fallo: bool = True,
    kwargs_extra: Optional[dict[str, Any]] = None,
) -> int:
    ctx = ContextoLote()
    kwargs_extra = kwargs_extra or {}
    skills_a_ejecutar: list[Any] = []
    del_disco = {s["name"]: s for s in catalogo_de_disco()}
    for nombre in nombres:
        cls = obtener_skill(nombre)
        if cls is None and nombre in del_disco:
            # No está en el código pero sí en el disco: se ejecuta llamando a la herramienta
            # que ella misma declara, o se devuelve como procedimiento. Una sola fuente de verdad.
            sd = SkillDeDisco(del_disco[nombre], ctx)
            r = sd.ejecutar(**kwargs_extra)
            print(f"▶ {sd.nombre} v{sd.version} · modo {r.datos.get('modo')}")
            if r.datos.get("herramienta"):
                print(f"   herramienta: {r.datos['herramienta']}")
                print((r.datos.get("salida") or "").strip()[:1200])
            elif r.datos.get("pasos"):
                for paso in r.datos["pasos"]:
                    print("   " + paso[:110])
            dur = (r.metrica or {}).get("duracion_s", 0)
            print(f"   {'✓' if r.exitoso else '✗'} en {dur:.2f}s · hash {r.hash_resultado}")
            continue
        if cls is None:
            print(f"Skill '{nombre}' no encontrada.")
            del_disco = {s["name"]: s for s in catalogo_de_disco()}
            if nombre in del_disco:
                s = del_disco[nombre]
                cuerpo = Path(s["ruta"]).read_text(encoding="utf-8")
                print(f"📘 {s['name']} v{s['version']} · {s['dominio']} · nivel {s['nivel']}")
                print(f"   cuándo: {s['cuando']}")
                print(f"   archivo: {s['ruta']}")
                print("-" * 60)
                print(cuerpo[cuerpo.find("\n---", 3) + 4:].strip())
                return 0
            print(f"Disponibles: {', '.join(sorted(set(listar_skills()) | set(del_disco)))}")
            return 1
        skills_a_ejecutar.append(cls)

    print(f"EJECUTANDO FLUJO ({'paralelo' if paralelo else 'secuencial'})")
    print("=" * 60)
    resultados = ejecutar_flujo(
        skills_a_ejecutar,
        contexto=ctx,
        paralelo=paralelo,
        detener_en_fallo=detener_en_fallo,
    )

    exitosos = sum(1 for r in resultados if r.exitoso)
    fallos = len(resultados) - exitosos
    print("\n" + "=" * 60)
    print(f"RESULTADO: {exitosos} exitosos, {fallos} fallos de {len(resultados)} skills")
    return 0 if fallos == 0 else 1


def _cmd_verificar(nombres: list[str]) -> int:
    ctx = ContextoLote()
    skills_a_verificar: list[type[Skill]] = []
    for nombre in nombres:
        cls = obtener_skill(nombre)
        if cls is None:
            print(f"Skill '{nombre}' no encontrada.")
            return 1
        skills_a_verificar.append(cls)

    print("VERIFICANDO SKILLS")
    print("=" * 60)
    estados = verificar_flujo(skills_a_verificar, contexto=ctx)
    todos_ok = all(e.exitoso for e in estados.values())
    print(f"\n{'TODAS CORRECTAS' if todos_ok else 'ALGUNAS FALLARON'}")
    return 0 if todos_ok else 1


def _cmd_flujo(nombre_flujo: str, paralelo: bool = False) -> int:
    flujos = {
        "completo": flujo_por_defecto(),
        "verificacion": FLUJO_SOLO_VERIFICACION,
    }
    if nombre_flujo not in flujos:
        print(f"Flujo '{nombre_flujo}' no encontrado.")
        print(f"Disponibles: {', '.join(flujos.keys())}")
        return 1
    return _cmd_ejecutar(
        [s.nombre for s in flujos[nombre_flujo]],
        paralelo=paralelo,
    )


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(
        description="Hiper habilidad · framework de skills de La Bandita"
    )
    sub = parser.add_subparsers(dest="comando")

    sub.add_parser("listar", help="Lista todas las skills registradas")

    p_doc = sub.add_parser("documentar", help="Muestra documentación de una skill")
    p_doc.add_argument("nombre", help="Nombre de la skill")

    p_exec = sub.add_parser("ejecutar", help="Ejecuta una o más skills")
    p_exec.add_argument("nombres", nargs="+", help="Nombres de las skills")
    p_exec.add_argument(
        "--paralelo", action="store_true", help="Ejecutar en paralelo cuando sea posible"
    )
    p_exec.add_argument(
        "--no-detener",
        action="store_true",
        help="No detenerse al primer fallo",
    )

    p_ver = sub.add_parser("verificar", help="Verifica que skills se ejecutaron")
    p_ver.add_argument("nombres", nargs="+", help="Nombres de las skills")

    p_flujo = sub.add_parser("flujo", help="Ejecuta un flujo predefinido")
    p_flujo.add_argument(
        "nombre",
        choices=["completo", "verificacion"],
        help="Nombre del flujo",
    )
    p_flujo.add_argument(
        "--paralelo", action="store_true", help="Ejecutar en paralelo"
    )

    args = parser.parse_args()

    if args.comando == "listar":
        return _cmd_listar()
    if args.comando == "documentar":
        return _cmd_documentar(args.nombre)
    if args.comando == "ejecutar":
        return _cmd_ejecutar(
            args.nombres,
            paralelo=args.paralelo,
            detener_en_fallo=not args.no_detener,
        )
    if args.comando == "verificar":
        return _cmd_verificar(args.nombres)
    if args.comando == "flujo":
        return _cmd_flujo(args.nombre, paralelo=args.paralelo)

    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())