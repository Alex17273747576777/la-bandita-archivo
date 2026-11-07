#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""FRAMEWORK DE SKILLS · habilidades ejecutables con estado persistente entre skills.

Cada skill es una clase con `ejecutar()`, `verificar()`, `entradas`, `salidas` y un
contexto de ejecución que guarda estado entre skills (medido → censado → escrito →
gateado → enviado → sellado). El estado se guarda en `.estado-lote.json` para permitir
interrumpir y reanudar sin repetir pasos.

Qué hace:
  * Define la clase base `Skill` que todas las habilidades deben heredar.
  * Proporciona `ContextoLote` para guardar y restaurar estado entre skills.
  * Orquesta el flujo: medir-recurso → censo-de-pieza → escribir-pieza →
    compuerta-manual → envio-canal → sellar-y-publicar.
  * Guarda el estado tras cada skill para poder reanudar tras una interrupción.

Qué NO hace:
  * No implementa las habilidades concretas: esas viven en SKILLS/<slug>/.
  * No escribe texto de piezas: eso lo hace la skill escribir-pieza.
  * No sella ni publica: eso lo hacen las skills sellar-y-publicar.
"""
from __future__ import annotations

import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

RAIZ: Path = Path(__file__).resolve().parents[1]
ESTADO_LOTE: Path = RAIZ / "docs" / ".estado-lote.json"


@dataclass
class ResultadoSkill:
    """Resultado de ejecutar una skill."""

    skill: str
    exitoso: bool
    datos: dict[str, Any] = field(default_factory=dict)
    errores: list[str] = field(default_factory=list)
    advertencias: list[str] = field(default_factory=list)


class ContextoLote:
    """Estado persistente de un lote de trabajo entre skills."""

    def __init__(self, ruta: Path = ESTADO_LOTE):
        self.ruta = ruta
        self._datos: dict[str, Any] = self._cargar()

    def _cargar(self) -> dict[str, Any]:
        if self.ruta.exists():
            try:
                return json.loads(self.ruta.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                pass
        return {"skills": {}, "lote": None, "fecha": None}

    def guardar(self) -> None:
        self.ruta.parent.mkdir(parents=True, exist_ok=True)
        self.ruta.write_text(
            json.dumps(self._datos, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
        )

    def obtener(self, clave: str, por_defecto: Any = None) -> Any:
        return self._datos.get(clave, por_defecto)

    def establecer(self, clave: str, valor: Any) -> None:
        self._datos[clave] = valor
        self.guardar()

    def obtener_skill(self, nombre_skill: str) -> dict[str, Any]:
        return self._datos.setdefault("skills", {}).setdefault(nombre_skill, {})

    def guardar_skill(self, nombre_skill: str, datos: dict[str, Any]) -> None:
        self._datos.setdefault("skills", {})[nombre_skill] = datos
        self.guardar()


class Skill:
    """Clase base para todas las habilidades de La Bandita."""

    nombre: str = "skill-base"
    version: str = "1.0.0"
    dominio: str = "general"

    def __init__(self, contexto: ContextoLote | None = None):
        self.contexto = contexto or ContextoLote()

    def ejecutar(self, **kwargs) -> ResultadoSkill:
        """Ejecuta la skill. Debe ser implementada por cada subclase."""
        raise NotImplementedError(f"{self.nombre} no implementa ejecutar()")

    def verificar(self) -> ResultadoSkill:
        """Verifica que la skill se ejecutó correctamente. Por defecto, revisa que haya datos."""
        datos = self.contexto.obtener_skill(self.nombre)
        if not datos:
            return ResultadoSkill(
                skill=self.nombre,
                exitoso=False,
                errores=[f"no hay datos de ejecución para {self.nombre}"],
            )
        return ResultadoSkill(skill=self.nombre, exitoso=True, datos=datos)

    def resumir(self) -> str:
        return f"{self.nombre} v{self.version} ({self.dominio})"


def ejecutar_flujo(skills: list[type[Skill]], contexto: ContextoLote | None = None) -> list[ResultadoSkill]:
    """Ejecuta una lista de skills en orden, guardando estado entre cada una."""
    ctx = contexto or ContextoLote()
    resultados: list[ResultadoSkill] = []

    for cls_skill in skills:
        skill = cls_skill(contexto=ctx)
        print(f"▶ {skill.resumir()}")
        resultado = skill.ejecutar()
        resultados.append(resultado)

        if resultado.exitoso:
            ctx.guardar_skill(skill.nombre, resultado.datos)
            print(f"  ✓ {skill.nombre} completado")
        else:
            print(f"  ✗ {skill.nombre} falló: {', '.join(resultado.errores)}")
            break

    return resultados


if __name__ == "__main__":
    print("FRAMEWORK DE SKILLS · importa Skill y ContextoLote desde tools.skill_framework")
    print("Ejemplo: from tools.skill_framework import Skill, ContextoLote, ejecutar_flujo")
