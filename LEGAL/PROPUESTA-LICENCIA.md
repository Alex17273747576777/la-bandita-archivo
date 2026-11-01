# LICENCIA · decisión del dueño, con las consecuencias a la vista

El repositorio **no tiene `LICENSE`**. Ese es el pendiente más caro de todos: sin licencia, nadie
puede reutilizar el archivo legalmente, ningún fondo de infraestructura abierta puede financiarlo y
ninguna empresa puede comprar un informe sin que su abogado abra un expediente aparte.

Esto no lo decidí yo. Una licencia es un acto de propiedad del dueño, no un detalle técnico.
Lo que sí hice: dejar el paquete listo para que la decisión cueste un comando.

## La propuesta de la casa (mi recomendación, no mi decisión)

| Capa | Licencia | Por qué |
|---|---|---|
| **Contenido** (las 259 piezas) | **CC BY-SA 4.0** | permite que el barrio y otros medios reproduzcan con atribución; el «share-alike» impide que alguien lo encierre; conserva el crédito |
| **Código** (`tools/`, `mcp-labandita-registro/`) | **MIT** | máxima adopción; una vara que se puede usar sin fricción es una vara que se usa |
| **Datos** (`registry/`, censos) | **CC BY 4.0** | datos abiertos con atribución obligatoria y cita de la fecha de medición |
| **Marca y nombre** | **Reservados** | la licencia abre el archivo, no la certificación ni el nombre: eso es lo que se vende |

Esta mezcla es la del *open core* honesto: se abre el método y el registro, se reserva el servicio
y la firma. Cualquiera puede verificar; solo la casa certifica.

## Las cuatro opciones que hay sobre la mesa

| Opción | Efecto | Riesgo |
|---|---|---|
| **A · La propuesta de arriba** | abre contenido y código, reserva marca | ninguno legal; exige vigilar el cumplimiento de la atribución |
| **B · Todo MIT** | máxima apertura | permite que un tercero cierre una versión mejorada y compita; diluye la marca |
| **C · Todo CC BY-NC 4.0** | impide uso comercial por terceros | **descalifica para NLnet y para cualquier fondo de software libre**; y es incoherente con vender servicio sobre lo mismo |
| **D · Sin licencia** (statu quo) | nada cambia hoy | sin reutilización legal, sin subvención, sin venta B2B limpia; el activo se deprecia |

## Cómo se aplica, cuando el dueño decida

```bash
bash LEGAL/aplicar-licencia.sh A     # escribe LICENSE, LICENSE-CONTENIDO, LICENSE-DATOS y NOTICE
git add LICENSE LICENSE-CONTENIDO LICENSE-DATOS NOTICE && git commit -m "Licencia: CC BY-SA 4.0 contenido · MIT código · CC BY 4.0 datos"
```

El script **no se ejecutó**: crea archivos de licencia, que son un acto de propiedad. Se ejecuta
cuando el dueño diga la letra.

## Lo que hay que decidir junto con la licencia

1. **Titularidad.** ¿A nombre de quién va el `NOTICE`? (persona física, marca, futura asociación).
2. **Año de inicio.** El archivo arranca en septiembre de 2026; el aviso de copyright debe cubrir
   desde la primera publicación.
3. **Terceros.** Hay capturas, descripciones y metadatos de repositorios ajenos. El `NOTICE` debe
   decir que los datos de terceros conservan su licencia y que las citas son con fines de
   verificación.
4. **La marca.** "La Bandita" registrada o no: la licencia no la cede, y eso debe estar escrito en
   el `NOTICE` antes de publicar la primera licencia.
