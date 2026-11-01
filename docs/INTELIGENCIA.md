# QUÉ INTELIGENCIA USAR · decisión, no menú

Pedido: elegir la mejor inteligencia disponible para este caso. Este es el caso: **una persona sola,
enferma, con 112 piezas escritas y 6.826 fichas medidas, publicando por WhatsApp, sin dinero y sin
equipo**. La mejor inteligencia no es la que escribe más bonito: es la que **no inventa y no la
obliga a supervisar**.

## La regla que manda sobre el modelo

Ningún modelo, por bueno que sea, sabe qué estrellas tenía un repositorio ayer. Eso no se resuelve
eligiendo mejor cerebro: se resuelve **conectándolo al registro**. Por eso el orden es:

1. **Primero el registro** (`mcp-labandita-registro`, ya publicado): el modelo consulta datos fechados.
2. **Después el modelo**, para redactar, ordenar y explicar.
3. **Al final la vara**, que es la única que puede decir «esto está bien» — y es código, no opinión.

Un modelo sin registro es una fuente de anécdotas. Un registro sin modelo es un JSON que nadie lee.
La pareja es el producto.

## Recomendación concreta

### Para escribir y verificar (el trabajo de todos los días)

**Un agente con conexión MCP al registro**, usando el modelo más fuerte que tengas disponible en el
cliente que ya usas. En este entorno eso significa Arena con Claude/GPT/Gemini según el turno; en tu
máquina, el cliente que prefieras. Lo importante no es la marca: es que **la herramienta esté
conectada**, porque sin registro el modelo adivina.

**Configuración lista para copiar** (Claude Desktop, Cursor, VS Code o cualquier cliente MCP):

```json
{
  "mcpServers": {
    "labandita-registro": {
      "command": "python3",
      "args": ["/ruta/a/la-bandita-archivo/mcp-labandita-registro/servidor.py"]
    }
  }
}
```

Y la instrucción que hay que darle al agente, palabra por palabra:

> Consulta `labandita-registro` antes de afirmar cualquier dato de un repositorio. Si la herramienta
> responde `estado_frescura: rancio`, dilo con la edad exacta; si responde `no está en el registro`,
> no lo inventes: declara la ausencia. No cites estrellas, licencias ni fechas que no vengan de una
> ficha.

### Para cuando no hay internet o no quieres gastar cuota

**Local, en tu propia máquina**: Ollama + un modelo abierto mediano (familia Qwen o Gemma, la versión
que tu equipo aguante). Sirve para redactar y reescribir; **no** para datos, porque no tiene el
registro. Y es coherente con el proyecto: la casa ya tiene la pieza 61 sobre Ollama.

### Para medir (lo que no se le pide a un modelo)

Nada de esto lo hace una IA conversacional: **se hace con código**. `tools/pulso.py` mide, `tools/vara.py`
juzga, `tools/atestar.py` sella. Un modelo puede proponer un recurso; solo el pulso puede afirmar que
existe, que licencia tiene y cuándo se movió.

## Comparación honesta (lo que sé y lo que no)

| Opción | Fortaleza real | Límite que hay que asumir |
|---|---|---|
| Modelo fuerte conectado al registro | redacción en dominicano y Juicio editorial | cuesta; hay que revisar la salida igual |
| Modelo abierto local (Ollama) | privado, gratis, sin red | más flojo en matiz; sin datos frescos |
| Solo código (sin modelo) | verdad verificable | no escribe una guía legible para el barrio |
| Solo modelo (sin registro) | rápido y elocuente | **inventa datos con seguridad. Descartado.** |

## Lo que no voy a recomendarte

- **No** uses un modelo para decidir qué recomendar. Esa es la firma que hace que el archivo valga.
- **No** dejes que un agente publique solo, sin vara. El proyecto ya pagó ese error una vez.
- **No** cambies de modelo cada semana buscando el «mejor»: cambia la herramienta conectada y la
  disciplina, que es lo que de verdad mueve la calidad.

## La decisión, en una línea

**Agente con MCP al registro para escribir; Ollama local para lo privado; código para medir; el dueño
para firmar.** El modelo es el lápiz, no la mano.
