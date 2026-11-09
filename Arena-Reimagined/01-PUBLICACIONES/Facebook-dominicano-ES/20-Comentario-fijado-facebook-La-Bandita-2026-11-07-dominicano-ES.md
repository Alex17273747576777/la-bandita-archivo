*Comentario fijado · El teclado que obedece: once teclados clonados y leídos esta mañana · La Bandita · sábado 7 de noviembre de 2026*

Resumen rápido para enlaces y contexto:

**De qué trata esta publicación:** programas medidos uno por uno contra la API de GitHub.
**Datos reales, no estimaciones.** Ningún paquete se aloja aquí.

**Las fichas, con datos reales de hoy:**

**Seis órdenes para comprobar por tu cuenta:**
1. Abre la página de entregas del repositorio y busca archivos .sha256, .sha512, .asc o .sig.
2. En Termux: `pkg install coreutils && sha256sum *.apk`
3. Compara con el autor: `sha256sum -c archivo.sha256`
4. Guarda la firma: `apksigner verify --print-certs archivo.apk` y compara la línea SHA-256 con la versión anterior
5. Pide la huella al autor en sus incidencias (plantilla incluida en la pieza).
6. Verifica atestación: `gh attestation verify archivo.apk --repo dueno/nombre`

**Dónde y cómo se usa:** cada programa se busca en su repositorio de GitHub (enlaces al final de la pieza).
Ningún APK se aloja aquí. La huella se calcula en el teléfono con Termux o en la computadora.

**Por qué importa:** sin huella no puedes saber si el archivo que bajaste es el que publicó el autor.
Con huella, comparas sesenta y cuatro caracteres y lo sabes con certeza.

**Hashtags:** #Teclados #IA #TecladoMovil #LeanType #HeliBoard #FlorisBoard #Prompts #TextoPredictivo #Accesibilidad #LaBandita #Ollama #AnySoftKeyboard

*La Bandita informa a partir de fuentes fechadas. · sábado 7 de noviembre de 2026 · comentario fijado de la publicación*
