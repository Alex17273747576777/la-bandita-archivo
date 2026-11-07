*Tutorial completo: recuperar la biblioteca de Kototoro tras la migración a v2.3.x*

*La Bandita · sábado 7 de noviembre de 2026 · edición dominicano-español · pieza 09 de Facebook*

⏱️ *Lectura total: 38 minutos · pasos verificados contra Kototoro v2.3.12 · migración de biblioteca y extensiones · cómo evitar que vuelva a pasar · cero paquetes alojados · cero enlaces a espejos*

🗺️ *Mapa de esta pieza*

```
├── 📋 Por qué existe este tutorial
├── 🔍 Paso 1 · verificar qué versión tenías y qué tienes ahora
├── 💾 Paso 2 · exportar una copia de seguridad antes de tocar nada
├── 🔄 Paso 3 · instalar v2.3.x sin perder datos
├── 📥 Paso 4 · importar la copia de seguridad en la nueva versión
├── 🔧 Paso 5 · reconfigurar extensiones y fuentes
├── ✅ Paso 6 · comprobar que la biblioteca está completa
├── 🛡️ Paso 7 · configurar backups automáticos para no volver a perder nada
├── ⚠️ Problemas conocidos y cómo solucionarlos
├── 🔗 Enlaces verificados
└── 

───────────────────

📌 *Comentario fijado*

Este comentario está fijado por la Bandita. Aquí encontrarás los avisos más importantes, enlaces de referencia y notas del autor que deben mantenerse visibles al inicio de los comentarios. Si tienes preguntas sobre esta publicación, déjalas abajo y responderemos en orden.


🌅 Cierre · la regla de oro de las copias de seguridad
```

───────────────────

## 📋 Por qué existe este tutorial

Entre junio y noviembre de 2026, Kototoro pasó de la v1.4.x a la v2.3.12. Siete versiones intermedias con cambios en la base de datos, el formato de las copias de seguridad, el motor de extensiones y la gestión de archivos locales. Muchos usuarios que actualizaron directamente se encontraron con bibliotecas vacías, extensiones desaparecidas o progreso de lectura perdido.

Este tutorial no es una traducción del manual oficial. Está escrito desde cero, paso a paso, probado contra la v2.3.12 de Kototoro, y diseñado para que alguien que nunca ha hecho una migración pueda recuperar su biblioteca sin perder nada.

───────────────────

## 🔍 Paso 1 · verificar qué versión tenías y qué tienes ahora

Antes de hacer cualquier cambio, abre Kototoro y ve a Ajustes > Acerca de. Anota:

1. La versión actual instalada (por ejemplo, v1.4.3, v2.3.5, v2.3.10).
2. La versión que quieres instalar (recomendada: v2.3.12, release estable del 7 de noviembre de 2026).

> **Nota sobre nightly builds:** Kototoro también publica compilaciones nocturnas automáticas (nightly-20261101, nightly-20261103, nightly-20261104, nightly-20261105, nightly-20261106) desde la rama de desarrollo. Estas contienen cambios pendientes no aún en una release estable; se recomiendan solo para usuarios avanzados. Para recuperar una biblioteca, usa siempre la versión estable v2.3.12.

Si ya tienes v2.3.12 instalada y tu biblioteca está vacía, salta al Paso 4 (importar copia de seguridad). Si estás en una versión anterior a v2.3.0, lee todo el tutorial antes de actualizar.

───────────────────

## 💾 Paso 2 · exportar una copia de seguridad antes de tocar nada

Nunca actualices sin una copia de seguridad reciente. En Kototoro:

1. Abre la aplicación.
2. Ve a Ajustes > Copias de seguridad.
3. Pulsa "Crear copia de seguridad" o "Exportar biblioteca".
4. Elige una ubicación de almacenamiento local (Descargas, Documentos o una carpeta dedicada).
5. Asigna un nombre que incluya la fecha, por ejemplo: `kototoro-backup-2026-11-07.bak`.
6. Espera a que termine la exportación y verifica que el archivo se creó con un peso razonable (unos pocos megabytes si tienes muchos libros, menos si tienes pocos).

**Importante:** guarda esta copia de seguridad fuera del almacenamiento interno de la aplicación, preferiblemente en una carpeta que no se borre al desinstalar. Copia el archivo a tu ordenador o a la nube si puedes.

Kototoro soporta copias de seguridad interoperables con Mihon y Aniyomi. Eso significa que, si alguna vez necesitas migrar a otra aplicación del ecosistema, tu copia de Kototoro puede importarse allí.

───────────────────

## 🔄 Paso 3 · instalar v2.3.x sin perder datos

Tienes dos opciones según tu situación:

### Opción A · Actualizar sobre la misma instalación (recomendado si ya estás en v2.3.x)
Descarga el APK de v2.3.12 desde los releases oficiales de GitHub e instálalo sobre la versión existente. Android mantendrá los datos de la aplicación. No hace falta desinstalar.

### Opción B · Instalación limpia (si vienes de v1.4.x o la app se comporta mal)
1. Desinstala Kototoro.
2. Instala v2.3.12 desde el APK oficial.
3. **No abras la aplicación todavía.** Ve directo al Paso 4.

Descarga oficial: https://github.com/Kototoro-app/Kototoro/releases/tag/v2.3.12

───────────────────

## 📥 Paso 4 · importar la copia de seguridad en la nueva versión

1. Abre Kototoro v2.3.12.
2. Ve a Ajustes > Copias de seguridad.
3. Pulsa "Importar copia de seguridad" o "Restaurar biblioteca".
4. Navega hasta el archivo `.bak` que exportaste en el Paso 2.
5. Selecciona el archivo y confirma la importación.
6. Espera a que termine. Kototoro mostrará un progreso mientras restaura capítulos, favoritos y progreso de lectura.

**Qué esperar al finalizar:**
- Tu biblioteca de manga y novelas debería aparecer completa.
- Tu historial de lectura y progreso por capítulo deberían estar intactos.
- Tus extensiones configuradas deberían seguir activas.

Si algo falta, no entres en pánico. Ve al Paso 5 para reconfigurar extensiones, y al Paso 6 para verificar.

───────────────────

## 🔧 Paso 5 · reconfigurar extensiones y fuentes

Tras la importación, algunas extensiones pueden necesitar revisión:

1. Ve a Más > Ajustes > Explorar > Repositorio de extensiones.
2. Verifica que tus fuentes habituales siguen añadidas.
3. Si falta alguna, añádela manualmente con su URL de repositorio.
4. Fuentes recomendadas y activas en noviembre de 2026:
   - **Keiyoushi Extensions** — más de 1500 extensiones de manga.
   - **FelipeGFA** — extensiones con enfoque en español: `https://raw.githubusercontent.com/FelipeFGA/anime-extensoes/repo/index.min.json`
   - **Kohi-den** — cerrado desde mayo de 2026. No añadas este repositorio; sus extensiones no reciben actualizaciones.
5. Para cada extensión, comprueba que se sincroniza y que los capítulos se cargan correctamente.

───────────────────

## ✅ Paso 6 · comprobar que la biblioteca está completa

Haz esta comprobación antes de dar la migración por terminada:

1. Abre tu biblioteca y cuenta cuántos títulos tienes.
2. Abre tres títulos al azul y verifica que el progreso de lectura coincide con lo que recuerdas.
3. Busca un título que sepas que tienes marcado como favorito y confirma que aparece en favoritos.
4. Abre un capítulo y verifica que se carga sin errores.

Si todo cuadra, la migración ha tenido éxito.

───────────────────

## 🛡️ Paso 7 · configurar backups automáticos para no volver a perder nada

Kototoro ofrece sincronización WebDAV y Google Drive. Configura una de ellas para que tu biblioteca se guarde automáticamente:

1. Ve a Ajustes > Sincronización.
2. Elige WebDAV o Google Drive.
3. Introduce tus credenciales y la ruta de destino.
4. Activa la sincronización automática (por ejemplo, cada 24 horas).
5. Verifica que el primer backup se subió correctamente.

Además, cada vez que actualices la aplicación, repite el Paso 2 (exportar copia de seguridad local) antes de instalar la nueva versión. Una copia de seguridad reciente es el único seguro real contra pérdidas de datos.

───────────────────

## ⚠️ Problemas conocidos y cómo solucionarlos

| Problema | Solución |
|----------|----------|
| Biblioteca vacía después de importar | Asegúrate de importar el archivo `.bak` correcto. Si usaste Opción B, importa antes de abrir la app por primera vez. |
| Extensiones que no cargan | Kohi-den está cerrado. Reemplázalo por FelipeGFA o Keiyoushi. |
| Progreso de lectura no coincide | Kototoro v2.3.5 alineó el progreso de capítulos en el historial. Actualiza a v2.3.12 si aún estás en una versión anterior. |
| Copia de seguridad no se crea | Verifica que tienes espacio de almacenamiento y permisos de escritura en la carpeta destino. |
| Error al abrir capítulos | Algunas fuentes pueden necesitar "Abrir en el navegador" y "Borrar cookies" para superar Cloudflare (novedad en v2.3.12). |

───────────────────

## 🔗 Enlaces verificados

- **Kototoro v2.3.12 release**: https://github.com/Kototoro-app/Kototoro/releases/tag/v2.3.12
- **Kototoro repositorio oficial**: https://github.com/Kototoro-app/Kototoro
- **Kototoro nightly builds**: https://github.com/Kototoro-app/Kototoro-Nightly/releases
- **Documentación Kototoro**: https://kototoro-app.github.io/Kototoro/
- **FelipeGFA extensiones**: https://raw.githubusercontent.com/FelipeFGA/anime-extensoes/repo/index.min.json
- **Keiyoushi Extensions**: repositorio de extensiones para manga (más de 1500)

───────────────────

## 🌅 Cierre · la regla de oro

La regla de oro de cualquier migración es simple: **nunca actualices sin una copia de seguridad reciente.** Con Kototoro v2.3.12, el proceso de exportar, actualizar e importar es sencillo, pero solo funciona si tomas la copia de seguridad antes de tocar nada.

Cada paso de este tutorial fue probado contra Kototoro v2.3.12, release del 7 de noviembre de 2026. Si encuentras un comportamiento distinto, verifica que estás usando exactamente esa versión.
