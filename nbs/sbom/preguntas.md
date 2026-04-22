---
title: "Preguntas sobre SBOMs"
format:
  html:
    toc: true
---

<style>
details.qa {
  border: 1px solid #dee2e6;
  border-radius: 6px;
  padding: 0;
  margin: 0.75rem 0;
  background: #fff;
  overflow: hidden;
}

details.qa[open] {
  background: #fbfbfb;
}

details.qa > summary {
  cursor: pointer;
  font-weight: 600;
  line-height: 1.4;
  list-style-position: outside;
  padding: 0.85rem 1rem 0.85rem 2.15rem;
  background: #f1f5f9;
  color: #102a43;
  border-left: 4px solid #2b6cb0;
}

details.qa > summary::marker {
  color: #2b6cb0;
}

details.qa[open] > summary {
  border-bottom: 1px solid #dbe4ee;
}

details.qa .respuesta {
  max-height: 22rem;
  overflow-y: auto;
  margin: 0;
  padding: 0.9rem 1rem 1rem 1.25rem;
  background: #fff;
  border-left: 4px solid #6c757d;
}

details.qa .respuesta::before {
  content: "Respuesta";
  display: inline-block;
  margin-bottom: 0.6rem;
  padding: 0.15rem 0.45rem;
  border-radius: 4px;
  background: #e9ecef;
  color: #495057;
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.02em;
  text-transform: uppercase;
}

details.qa .respuesta p:last-child,
details.qa .respuesta ul:last-child {
  margin-bottom: 0;
}
</style>

Esta página funciona como una guía de autoevaluación. Cada pregunta incluye una respuesta desplegable para que puedas intentar responder primero y luego contrastar tu razonamiento.

## Lo que deberías saber

<details class="qa">
<summary>¿Qué problema de la cadena de suministro de software intenta resolver un SBOM?</summary>
<div class="respuesta">
<p>Un SBOM intenta resolver el problema de la falta de visibilidad sobre los componentes que forman parte de un sistema de software. En el desarrollo moderno, una aplicación rara vez está compuesta solo por código escrito por el equipo. También incorpora bibliotecas de terceros, dependencias transitivas, imágenes de contenedor, herramientas de construcción, componentes propietarios y paquetes de código abierto. Sin un inventario estructurado, es difícil saber qué se está ejecutando realmente y qué riesgos entran al sistema a través de esos componentes.</p>
<p>El SBOM entrega una base para responder preguntas de seguridad, cumplimiento y mantenimiento. Permite identificar componentes vulnerables, revisar licencias, rastrear versiones, analizar relaciones entre dependencias y responder con más rapidez cuando aparece una nueva vulnerabilidad. No elimina el riesgo por sí solo, pero crea una fuente de evidencia que puede alimentar procesos de gestión de riesgo, auditoría y respuesta ante incidentes.</p>
</div>
</details>

<details class="qa">
<summary>¿Cuál es la diferencia entre generar, versionar, distribuir y consumir un SBOM?</summary>
<div class="respuesta">
<p>Generar un SBOM significa producir el inventario de componentes mediante una herramienta o proceso. Por ejemplo, ejecutar Syft, Trivy, CycloneDX o una integración del sistema de construcción para crear un archivo en formato SPDX, CycloneDX u otro formato compatible.</p>
<p>Versionar un SBOM significa conservar su evolución en el tiempo. Esto permite saber cómo cambió la composición del software entre confirmaciones de cambio, construcciones o versiones publicadas. Sin versionamiento, el SBOM puede existir, pero no permite reconstruir la historia de cambios.</p>
<p>Distribuir un SBOM significa ponerlo a disposición de quienes lo necesitan. Puede adjuntarse a una versión publicada, almacenarse junto al artefacto publicado, entregarse a un cliente o mantenerse accesible para equipos internos de seguridad. Si solo se genera localmente y nadie puede acceder a él, su valor queda limitado.</p>
<p>Consumir un SBOM significa usarlo como entrada para otra actividad. Un escáner puede buscar vulnerabilidades, una herramienta de cumplimiento puede revisar licencias o un sistema de monitoreo puede detectar qué proyectos usan una dependencia afectada. El valor operativo aparece cuando el SBOM no solo existe, sino que se usa para tomar decisiones.</p>
</div>
</details>

<details class="qa">
<summary>¿Qué información mínima debería contener un SBOM para ser útil en seguridad?</summary>
<div class="respuesta">
<p>Para que un SBOM sea útil en seguridad debe identificar claramente el componente principal que describe, los componentes incluidos, sus nombres, versiones, identificadores únicos, relaciones de dependencia, autoría del SBOM y fecha de generación. Estos elementos permiten saber qué software se está analizando, qué dependencias contiene y en qué momento fue producido el inventario.</p>
<p>También es muy importante incluir información que facilite el cruce con fuentes externas. Identificadores como purl, CPE o SWID ayudan a conectar componentes con bases de datos de vulnerabilidades. Las huellas criptográficas permiten verificar integridad y distinguir artefactos. Las relaciones entre dependencias ayudan a entender si una vulnerabilidad está en una dependencia directa o en una dependencia transitiva.</p>
<p>Un SBOM útil para seguridad no debería limitarse a listar nombres. Debe permitir que otra herramienta o persona pueda identificar con precisión el componente, ubicarlo dentro del grafo de dependencias y evaluar si existe exposición real ante una vulnerabilidad conocida.</p>
</div>
</details>

<details class="qa">
<summary>¿Cuál es la diferencia entre una dependencia directa y una dependencia transitiva?</summary>
<div class="respuesta">
<p>Una dependencia directa es un componente que el proyecto declara o incorpora explícitamente. Por ejemplo, si una aplicación Java declara una biblioteca en su archivo <code>pom.xml</code>, esa biblioteca es una dependencia directa del proyecto.</p>
<p>Una dependencia transitiva es un componente que entra al sistema porque una dependencia directa lo necesita. El equipo puede no haber elegido esa biblioteca de forma explícita, pero termina formando parte del software porque otra dependencia la trae consigo.</p>
<p>La diferencia es importante para seguridad. Muchas vulnerabilidades aparecen en dependencias transitivas que el equipo no mira todos los días. Si el SBOM solo muestra dependencias directas, el inventario queda incompleto. Un análisis serio de la cadena de suministro necesita visibilidad sobre ambos niveles.</p>
</div>
</details>

<details class="qa">
<summary>¿Por qué un archivo de gestor de paquetes, como <code>pom.xml</code>, <code>package-lock.json</code> o <code>requirements.txt</code>, no es necesariamente equivalente a un SBOM?</summary>
<div class="respuesta">
<p>Un archivo de gestor de paquetes describe dependencias desde la perspectiva del ecosistema de desarrollo. Puede indicar qué bibliotecas se requieren, qué versiones se esperan o qué árbol de dependencias resolvió el gestor. Sin embargo, no siempre describe el artefacto final que se construye, distribuye o ejecuta.</p>
<p>Un SBOM busca representar la composición del software como artefacto. Puede incluir información adicional que normalmente no está en los archivos de dependencias, como identificadores normalizados, huellas criptográficas, licencias, proveedor, relaciones entre componentes, metadatos del SBOM y referencias externas.</p>
<p>Además, algunos componentes pueden entrar al sistema fuera del gestor de paquetes. Por ejemplo, binarios copiados manualmente, dependencias del sistema operativo, imágenes base de contenedores, complementos de construcción o componentes generados durante la construcción. Por eso un archivo de gestor de paquetes puede ser una fuente para generar un SBOM, pero no reemplaza necesariamente al SBOM.</p>
</div>
</details>

<details class="qa">
<summary>¿Qué diferencias prácticas existen entre SPDX y CycloneDX?</summary>
<div class="respuesta">
<p>SPDX y CycloneDX son estándares usados para representar SBOMs de forma estructurada y legible por máquinas. Ambos permiten describir componentes, versiones, licencias, identificadores y relaciones. La diferencia práctica está en su origen, énfasis histórico, modelo de datos y ecosistema de herramientas.</p>
<p>SPDX nació con un énfasis fuerte en licencias y cumplimiento. Por eso ha sido muy usado para documentar información legal asociada a componentes de software. Con el tiempo se amplió para cubrir más casos de uso, incluida seguridad de la cadena de suministro.</p>
<p>CycloneDX fue impulsado desde el ecosistema OWASP y ha tenido un foco fuerte en seguridad, análisis de componentes, vulnerabilidades y automatización en flujos de CI/CD. Suele ser común en herramientas de seguridad de aplicaciones y composición de software.</p>
<p>En la práctica, la elección depende del contexto. Algunas organizaciones prefieren SPDX por cumplimiento y estandarización internacional. Otras prefieren CycloneDX por integración con herramientas de seguridad. En proyectos complejos puede ser necesario producir más de un formato para interoperar con distintos consumidores.</p>
</div>
</details>

<details class="qa">
<summary>¿Qué es un identificador de componente y por qué importan purl, CPE o SWID?</summary>
<div class="respuesta">
<p>Un identificador de componente es una forma normalizada de referirse a un paquete, biblioteca o artefacto. Su objetivo es reducir ambigüedad. No basta con decir que un sistema usa una biblioteca llamada <code>requests</code>, <code>log4j</code> o <code>openssl</code>. Es necesario indicar de qué ecosistema proviene, qué versión usa y cómo se puede localizar en fuentes externas.</p>
<p>purl, CPE y SWID son mecanismos de identificación. purl representa paquetes de ecosistemas como Maven, npm, PyPI o RubyGems. CPE es usado ampliamente por bases como NVD para asociar productos con vulnerabilidades. SWID permite identificar software instalado o distribuido mediante etiquetas estructuradas.</p>
<p>Estos identificadores importan porque permiten cruzar el SBOM con bases de vulnerabilidades, repositorios de paquetes, herramientas de cumplimiento y sistemas de monitoreo. Si un componente no tiene identificador robusto, puede ser difícil saber si una vulnerabilidad reportada aplica realmente a ese componente.</p>
</div>
</details>

<details class="qa">
<summary>¿Para qué sirven las huellas criptográficas de componentes dentro de un SBOM?</summary>
<div class="respuesta">
<p>Las huellas criptográficas sirven para verificar la identidad e integridad de un componente. Un nombre y una versión pueden no ser suficientes para distinguir artefactos. Dos archivos pueden declarar la misma versión, pero no tener exactamente el mismo contenido. Una huella criptográfica permite comparar el contenido real del artefacto con un valor calculado de manera reproducible.</p>
<p>En seguridad, esto ayuda a detectar alteraciones no autorizadas, componentes reemplazados, paquetes manipulados o diferencias entre lo declarado y lo distribuido. También facilita cruces con fuentes externas que usan huellas criptográficas para identificar artefactos maliciosos o vulnerables.</p>
<p>Idealmente, un SBOM puede incluir más de un tipo de huella criptográfica, como SHA-256 y SHA-512. Esto mejora la interoperabilidad con herramientas y bases de datos que aceptan distintos algoritmos. Sin huellas criptográficas, el SBOM sigue siendo útil, pero pierde precisión para verificar integridad.</p>
</div>
</details>

<details class="qa">
<summary>¿Por qué la información de licencias es parte del problema de seguridad y cumplimiento?</summary>
<div class="respuesta">
<p>La información de licencias es parte del cumplimiento porque determina qué se puede hacer legalmente con un componente. Algunas licencias permiten uso comercial sin muchas restricciones. Otras exigen atribución, publicación de código derivado o cumplimiento de condiciones específicas. Si una organización integra componentes sin revisar licencias, puede exponerse a riesgos legales, contractuales y financieros.</p>
<p>También se relaciona con seguridad porque la gestión de dependencias no es solo técnica. Una organización necesita saber qué componentes puede usar, redistribuir, modificar o combinar. Si no entiende sus licencias, puede bloquear versiones publicadas, incumplir contratos o introducir dependencias que luego no puede mantener.</p>
<p>Un SBOM con información de licencias permite automatizar parte de ese análisis. Puede ayudar a detectar licencias incompatibles con políticas internas, revisar componentes de terceros antes de distribución y entregar evidencia a clientes o auditores.</p>
</div>
</details>

<details class="qa">
<summary>¿Qué significa que un SBOM sea válido respecto de una versión de su estándar?</summary>
<div class="respuesta">
<p>Significa que el archivo cumple la estructura, campos obligatorios, tipos de datos y reglas definidas por una versión específica del estándar. Por ejemplo, un SBOM CycloneDX 1.5 debe respetar el esquema de CycloneDX 1.5. Un SBOM SPDX 2.3 debe respetar las reglas de SPDX 2.3.</p>
<p>La validez permite que otras herramientas puedan leer el SBOM sin errores. Si el archivo declara una versión de estándar, pero usa campos incorrectos, URLs inválidas, estructuras no soportadas o atributos faltantes, los consumidores pueden fallar al procesarlo.</p>
<p>Validar el SBOM no garantiza que toda la información sea completa o correcta, pero sí es una condición básica de interoperabilidad. Un SBOM inválido puede romper flujos de CI/CD, bloquear análisis de vulnerabilidades o impedir auditorías automatizadas.</p>
</div>
</details>

<details class="qa">
<summary>¿Por qué un SBOM válido puede seguir siendo insuficiente?</summary>
<div class="respuesta">
<p>Un SBOM válido puede seguir siendo insuficiente porque la validez estructural solo indica que el archivo cumple un esquema. No indica necesariamente que el inventario esté completo, que las versiones sean correctas, que todas las dependencias aparezcan o que los campos más útiles estén poblados.</p>
<p>Por ejemplo, un SBOM puede ser válido y aun así no incluir licencias, huellas criptográficas, proveedor, dependencias transitivas o relaciones claras entre componentes. También puede omitir el componente principal o no representar diferencias entre entornos de despliegue.</p>
<p>La utilidad real depende de la calidad del contenido. Para seguridad, cumplimiento y respuesta ante incidentes, importa que el SBOM permita identificar componentes, conectarlos con fuentes externas y actuar sobre la información. Un SBOM válido pero pobre en datos cumple la forma, pero no necesariamente cumple la función.</p>
</div>
</details>

<details class="qa">
<summary>¿Qué rol puede cumplir CI/CD en la generación, validación y publicación de SBOMs?</summary>
<div class="respuesta">
<p>CI/CD puede convertir la generación de SBOMs en una práctica repetible y no en una tarea manual ocasional. En un flujo de CI/CD se puede generar un SBOM en cada construcción, solicitud de cambios, cambio relevante o versión publicada. Esto permite que el inventario se mantenga alineado con el software que realmente se construye.</p>
<p>También puede validar el SBOM contra su estándar. Si el archivo no cumple el esquema declarado, el flujo de CI/CD puede fallar o marcar una advertencia. Además, puede ejecutar análisis de vulnerabilidades, revisar licencias y comparar cambios de dependencias entre versiones.</p>
<p>En la publicación, CI/CD puede adjuntar el SBOM al artefacto final, subirlo a un repositorio de evidencia, firmarlo, asociarlo con una imagen de contenedor o entregarlo junto a la versión publicada. Esto ayuda a que el SBOM no sea solo un archivo generado, sino parte del ciclo de vida del software.</p>
</div>
</details>

<details class="qa">
<summary>¿Qué tipo de problemas aparecen cuando dos herramientas generan SBOMs distintos para el mismo proyecto?</summary>
<div class="respuesta">
<p>Cuando dos herramientas generan SBOMs distintos aparece un problema de confianza y reconciliación. Las diferencias pueden venir de varias fuentes. Una herramienta puede leer archivos de gestor de paquetes y otra puede analizar el sistema de archivos. Una puede incluir dependencias de desarrollo y otra solo dependencias de producción. Una puede resolver dependencias transitivas de forma distinta o interpretar metadatos de licencias con otro criterio.</p>
<p>También pueden aparecer falsos positivos y falsos negativos. Un falso positivo incluye componentes que no forman parte real del artefacto. Un falso negativo omite componentes que sí están presentes. Ambas situaciones afectan seguridad y cumplimiento.</p>
<p>La respuesta no debería ser elegir ciegamente una herramienta. Conviene definir el alcance del SBOM, documentar el método de generación, comparar salidas, validar casos críticos y usar criterios reproducibles. En algunos contextos, usar varias herramientas puede mejorar cobertura, pero solo si existe un proceso para resolver discrepancias.</p>
</div>
</details>

<details class="qa">
<summary>¿Qué relación existe entre SBOM, análisis de composición de software, CVE, NVD y VEX?</summary>
<div class="respuesta">
<p>El SBOM es el inventario de componentes. El análisis de composición de software usa información sobre dependencias para detectar vulnerabilidades, licencias y riesgos asociados. Una herramienta de este tipo puede tomar un SBOM como entrada o generar su propio inventario durante el análisis.</p>
<p>CVE es un identificador público para vulnerabilidades conocidas. NVD es una base de datos que agrega información sobre esas vulnerabilidades, productos afectados, severidad y metadatos relacionados. Para saber si una CVE aplica a un sistema, se necesita mapear componentes del SBOM contra fuentes como NVD u otras bases de vulnerabilidades.</p>
<p>VEX complementa al SBOM porque comunica si una vulnerabilidad conocida afecta realmente a un producto en un contexto determinado. Un componente puede estar presente, pero la vulnerabilidad puede no ser explotable por configuración, ruta de ejecución o mitigación aplicada. SBOM dice qué hay. VEX ayuda a explicar si una vulnerabilidad asociada a eso realmente impacta.</p>
</div>
</details>

<details class="qa">
<summary>¿Por qué un SBOM debería actualizarse cuando cambia el código, las dependencias o la versión publicada?</summary>
<div class="respuesta">
<p>Un SBOM describe la composición de un artefacto en un momento determinado. Si cambia el código, las dependencias o la versión publicada, también puede cambiar la composición del software. Por eso un SBOM desactualizado puede entregar una imagen falsa del sistema.</p>
<p>Cuando cambia una dependencia directa, una transitiva, una imagen base o un complemento de construcción, pueden entrar nuevas vulnerabilidades o licencias. Cuando se publica una versión, el consumidor necesita un SBOM que corresponda exactamente a ese artefacto y no a una versión anterior.</p>
<p>Actualizar el SBOM permite mantener trazabilidad. También permite comparar versiones y responder preguntas como qué componente entró, cuál salió, qué versión cambió y qué versión publicada está afectada por una vulnerabilidad nueva.</p>
</div>
</details>

<details class="qa">
<summary>¿Qué diferencia hay entre usar un SBOM como documentación y usarlo como entrada para procesos automatizados?</summary>
<div class="respuesta">
<p>Usar un SBOM como documentación significa tratarlo como una descripción consultable por personas. Puede servir para revisar dependencias, entregar evidencia a un cliente o registrar información de composición. Este uso es valioso, pero limitado si nadie lo actualiza o si no se conecta con otros procesos.</p>
<p>Usarlo como entrada para procesos automatizados significa que herramientas y flujos de CI/CD leen el SBOM para tomar acciones. Por ejemplo, pueden buscar vulnerabilidades, validar licencias, comparar cambios, generar alertas, bloquear versiones publicadas o alimentar sistemas de monitoreo.</p>
<p>La diferencia principal está en la acción. Como documentación, el SBOM informa. Como entrada automatizada, el SBOM permite operar. Para que esto funcione, debe ser legible por máquinas, válido, completo y consistente.</p>
</div>
</details>

## Preguntas para responder

<details class="qa">
<summary>Si una organización genera SBOMs, pero no los adjunta a sus versiones publicadas, ¿quién puede beneficiarse realmente de ellos?</summary>
<div class="respuesta">
<p>Principalmente se beneficia la propia organización que los genera, siempre que los use internamente. Por ejemplo, equipos de seguridad, DevOps, cumplimiento o mantenimiento pueden revisar vulnerabilidades, licencias y cambios de dependencias. También pueden alimentar sistemas internos de monitoreo.</p>
<p>El consumidor externo se beneficia poco o nada si no recibe el SBOM asociado a la versión publicada. Sin acceso al inventario, no puede verificar componentes, evaluar exposición, automatizar revisiones ni integrar esa evidencia en sus propios procesos de gestión de riesgo.</p>
<p>Por eso generar no equivale a distribuir. Para que el SBOM aporte transparencia hacia terceros, debe acompañar al artefacto publicado o estar disponible mediante un mecanismo confiable. De lo contrario, el SBOM puede ser útil como práctica interna, pero no cumple plenamente la promesa de transparencia de la cadena de suministro.</p>
</div>
</details>

<details class="qa">
<summary>Si un SBOM no incluye dependencias transitivas, ¿qué riesgos quedan fuera del análisis?</summary>
<div class="respuesta">
<p>Quedan fuera los riesgos introducidos por componentes que el equipo no declaró directamente, pero que forman parte real del sistema. Muchas vulnerabilidades relevantes aparecen en bibliotecas transitivas. Si el SBOM no las incluye, una herramienta de análisis puede concluir erróneamente que el sistema no está afectado.</p>
<p>También quedan fuera problemas de licencias, mantenimiento y procedencia asociados a esas dependencias. Una dependencia directa puede tener una licencia aceptable, pero arrastrar otra dependencia con restricciones incompatibles. Lo mismo puede ocurrir con paquetes abandonados, versiones obsoletas o componentes sin proveedor claro.</p>
<p>En seguridad de cadena de suministro, la visibilidad parcial produce una falsa sensación de control. Un SBOM sin dependencias transitivas puede servir para una revisión superficial, pero es débil para análisis de exposición real.</p>
</div>
</details>

<details class="qa">
<summary>Si un SBOM no incluye licencias, ¿puede servir para una auditoría de cumplimiento?</summary>
<div class="respuesta">
<p>Puede servir solo de manera limitada. Un SBOM sin licencias puede ayudar a identificar algunos componentes presentes, pero no permite evaluar con claridad si esos componentes cumplen las políticas legales, contractuales o internas de la organización.</p>
<p>Para una auditoría de cumplimiento, la información de licencias es central. El auditor necesita saber qué obligaciones tiene cada componente, si existen licencias incompatibles, si se requiere atribución, si hay restricciones de redistribución o si una dependencia obliga a publicar código derivado.</p>
<p>Si las licencias no están en el SBOM, la organización tendrá que obtener esa información por otra vía. Eso reduce automatización y aumenta riesgo de error. Por lo tanto, el SBOM aún puede ser una pieza de evidencia, pero no es suficiente para una auditoría de cumplimiento completa.</p>
</div>
</details>

<details class="qa">
<summary>Si una herramienta reporta una dependencia vulnerable y otra no, ¿cómo decidirías cuál resultado investigar primero?</summary>
<div class="respuesta">
<p>Primero revisaría el alcance y método de cada herramienta. Es necesario saber si ambas analizaron el mismo artefacto, si incluyeron dependencias transitivas, si evaluaron dependencias de desarrollo y producción, y si usaron la misma fuente de vulnerabilidades.</p>
<p>Luego investigaría la dependencia reportada como vulnerable. Revisaría nombre, versión, identificadores, ruta de dependencia y CVE asociada. También verificaría si el componente está presente en el artefacto final y si la funcionalidad vulnerable es alcanzable o explotable en el contexto del sistema.</p>
<p>Si la vulnerabilidad tiene alta severidad, explotación conocida o afecta un componente expuesto, debería priorizarse aunque solo una herramienta la reporte. Las discrepancias no se resuelven ignorando la alerta, sino trazando evidencia. La decisión final debe considerar severidad, exposición, confianza en el identificador y contexto de uso.</p>
</div>
</details>

<details class="qa">
<summary>Si un proyecto usa contenedores, ¿debería generar un SBOM del repositorio, de la imagen construida o de ambos?</summary>
<div class="respuesta">
<p>Debería generar ambos cuando el objetivo sea tener visibilidad completa. El SBOM del repositorio ayuda a entender dependencias declaradas en el código fuente, gestores de paquetes y configuración del proyecto. Es útil durante desarrollo y revisión de cambios.</p>
<p>El SBOM de la imagen construida describe lo que realmente se distribuye o ejecuta. Puede incluir paquetes del sistema operativo, librerías instaladas en la imagen base, binarios copiados, dependencias resueltas durante la construcción y componentes que no aparecen explícitamente en el repositorio.</p>
<p>En contenedores, el artefacto final puede diferir bastante del repositorio. Por eso, si se debe priorizar uno para seguridad operacional, el SBOM de la imagen suele ser más cercano al riesgo real en ejecución. El SBOM del repositorio complementa esa mirada con trazabilidad de desarrollo.</p>
</div>
</details>

<details class="qa">
<summary>Si una biblioteca cambia de versión en una dependencia indirecta, ¿cómo debería reflejarse eso en el SBOM?</summary>
<div class="respuesta">
<p>Debe reflejarse como un cambio en el componente transitivo correspondiente. El SBOM actualizado debería mostrar el nuevo nombre y versión del componente, sus identificadores, su relación con las dependencias que lo introducen y, si corresponde, nuevas huellas criptográficas o metadatos asociados.</p>
<p>También debería permitir comparar el cambio contra el SBOM anterior. Esa comparación ayuda a responder qué dependencia directa provocó el cambio, si la nueva versión corrige una vulnerabilidad, si introduce una licencia distinta o si modifica el riesgo de la versión publicada.</p>
<p>Si el SBOM no captura cambios transitivos, la organización pierde visibilidad sobre una parte importante del árbol de dependencias. Por eso conviene generar SBOMs en cada construcción o versión publicada y conservarlos para análisis diferencial.</p>
</div>
</details>

<details class="qa">
<summary>Si un SBOM contiene un componente sin proveedor, sin huella criptográfica y sin identificador robusto, ¿qué tan accionable es ese dato?</summary>
<div class="respuesta">
<p>Es poco accionable. El nombre del componente puede dar una pista, pero sin proveedor, huella criptográfica o identificador robusto es difícil confirmar exactamente a qué artefacto se refiere. También es más difícil cruzarlo con bases de vulnerabilidades, repositorios de paquetes o herramientas de cumplimiento.</p>
<p>El proveedor ayuda a identificar origen y responsabilidad. La huella criptográfica ayuda a verificar integridad y distinguir artefactos concretos. Identificadores como purl o CPE ayudan a conectar el componente con fuentes externas. Sin esos datos, el análisis depende de inferencias manuales.</p>
<p>El dato no es inútil, pero su valor operativo baja. Puede servir como señal para investigar, pero no como evidencia fuerte para automatizar decisiones de seguridad o cumplimiento.</p>
</div>
</details>

<details class="qa">
<summary>Si publicar un SBOM completo revela información sensible, ¿debería mantenerse privado, compartirse parcialmente o publicarse igual?</summary>
<div class="respuesta">
<p>No hay una única respuesta universal. Depende del tipo de software, del contrato con consumidores, del nivel de riesgo, de la regulación aplicable y de la sensibilidad de la información. Publicar un SBOM puede aumentar transparencia, pero también puede revelar tecnología usada, versiones internas o componentes que faciliten reconocimiento por parte de atacantes.</p>
<p>Una opción es mantener el SBOM privado y compartirlo solo con clientes, auditores o reguladores bajo condiciones definidas. Otra es publicar una versión parcial que oculte información sensible, aunque esto reduce utilidad. También puede publicarse completo cuando el beneficio de transparencia supera el riesgo y existe una estrategia de respuesta madura.</p>
<p>Lo importante es que la decisión sea explícita. Una organización debería definir políticas de acceso, clasificación de información, mecanismos de entrega y criterios para determinar qué campos pueden exponerse. Transparencia no significa necesariamente publicación irrestricta.</p>
</div>
</details>

<details class="qa">
<summary>Si una regulación exige SBOMs, ¿cómo evitarías que se transformen en documentos generados solo para cumplir?</summary>
<div class="respuesta">
<p>Para evitar que se vuelvan documentos formales sin valor, el SBOM debe integrarse a procesos reales. Debe generarse automáticamente en el flujo de CI/CD, validarse contra el estándar, adjuntarse a la versión publicada y usarse en análisis de vulnerabilidades, licencias y cambios de dependencias.</p>
<p>También se requieren criterios de calidad. La organización debería definir campos mínimos, revisar cobertura de dependencias, exigir identificadores robustos, registrar herramienta y fecha de generación, y controlar que el SBOM corresponda al artefacto distribuido.</p>
<p>Finalmente, debe haber responsabilidad organizacional. Alguien debe revisar alertas, resolver excepciones y mantener políticas. Si el SBOM no alimenta decisiones, se convierte en evidencia burocrática. Si alimenta decisiones de seguridad y cumplimiento, se vuelve una práctica operativa.</p>
</div>
</details>

<details class="qa">
<summary>Si un equipo ya usa análisis de composición de software en CI/CD, ¿qué aporta adicionalmente un SBOM?</summary>
<div class="respuesta">
<p>El análisis de composición de software detecta riesgos en un momento determinado, pero el SBOM deja una evidencia estructurada de la composición del artefacto. Esa evidencia puede archivarse, compartirse y reutilizarse fuera de la herramienta que hizo el análisis.</p>
<p>Un SBOM permite separar inventario y análisis. Hoy se puede usar para vulnerabilidades. Mañana se puede usar para licencias, auditoría, respuesta ante incidentes o revisión por un cliente. También permite comparar versiones publicadas y mantener trazabilidad histórica.</p>
<p>Además, el SBOM facilita interoperabilidad. Distintas herramientas pueden consumir el mismo inventario en vez de repetir descubrimiento desde cero. Esto es útil cuando el consumidor del software no tiene acceso al código fuente, pero sí necesita evaluar componentes.</p>
</div>
</details>

<details class="qa">
<summary>Si un equipo mantiene una planilla manual de dependencias, ¿qué errores son más probables frente a un SBOM automatizado?</summary>
<div class="respuesta">
<p>Una planilla manual tiende a desactualizarse. Es fácil olvidar una dependencia nueva, no registrar una actualización, omitir dependencias transitivas o copiar mal una versión. También es común que la planilla describa lo que el equipo cree que usa, no lo que el artefacto realmente contiene.</p>
<p>También hay mayor riesgo de inconsistencia. Distintas personas pueden escribir nombres de componentes de forma distinta, usar criterios diferentes para licencias o no registrar identificadores técnicos. Esto dificulta automatizar cruces con bases de vulnerabilidades.</p>
<p>Un SBOM automatizado no es perfecto, pero reduce trabajo manual y mejora reproducibilidad. La mejor práctica puede combinar generación automática con revisión humana de casos críticos, especialmente licencias, componentes internos o discrepancias entre herramientas.</p>
</div>
</details>

<details class="qa">
<summary>Si un SBOM falla la validación del estándar, ¿debería bloquear la versión publicada?</summary>
<div class="respuesta">
<p>Depende de la política de riesgo de la organización y del tipo de producto. En software crítico, regulado o entregado a clientes que exigen SBOMs, fallar la validación debería bloquear la versión publicada o, al menos, requerir una excepción formal aprobada. Un SBOM inválido puede impedir que herramientas consumidoras lo procesen.</p>
<p>En etapas tempranas de adopción, la organización puede empezar con advertencias y luego endurecer la política. Sin embargo, si se permite publicar SBOMs inválidos de manera habitual, se pierde confianza en el proceso.</p>
<p>Una política razonable distingue entre errores estructurales y problemas de completitud. Los errores que rompen el formato deberían tratarse como bloqueantes. Los campos faltantes pueden tener niveles de severidad según el caso de uso. Lo importante es que la decisión sea explícita y auditable.</p>
</div>
</details>

<details class="qa">
<summary>Si el SBOM se genera en cada solicitud de cambios, ¿también debería guardarse cada resultado?</summary>
<div class="respuesta">
<p>No necesariamente debe guardarse cada resultado como artefacto permanente. Generar el SBOM en cada solicitud de cambios sirve para detectar cambios, vulnerabilidades o problemas de validación antes de integrar código. En ese contexto, puede bastar con conservar evidencia temporal asociada al flujo de revisión.</p>
<p>Sí conviene guardar SBOMs asociados a eventos importantes, como integraciones a ramas principales, construcciones candidatas, versiones publicadas, imágenes publicadas o entregas a clientes. Esos SBOMs permiten trazabilidad histórica y respuesta ante incidentes.</p>
<p>Una buena política puede generar SBOMs frecuentemente, comparar sus cambios y conservar solo los vinculados a artefactos relevantes. Así se evita saturar almacenamiento y navegación, pero no se pierde evidencia importante.</p>
</div>
</details>

<details class="qa">
<summary>Si un consumidor recibe un SBOM, ¿qué verificaciones mínimas debería hacer antes de confiar en él?</summary>
<div class="respuesta">
<p>Primero debería verificar que el SBOM corresponde al artefacto recibido. Debe revisar nombre del producto, versión, fecha de generación, herramienta usada y, si existe, firma o mecanismo de integridad. También debería confirmar que el formato es válido respecto del estándar declarado.</p>
<p>Luego debería revisar cobertura mínima. El SBOM debería incluir componente principal, dependencias directas y transitivas, versiones, identificadores robustos, licencias cuando sean relevantes y relaciones entre componentes. Si hay huellas criptográficas, puede usarlas para verificar integridad.</p>
<p>Finalmente, debería consumir el SBOM con herramientas propias. Eso permite buscar vulnerabilidades, revisar licencias y evaluar si existen componentes prohibidos por políticas internas. La confianza no debería basarse solo en recibir el archivo, sino en validar su consistencia y utilidad.</p>
</div>
</details>

<details class="qa">
<summary>Si una vulnerabilidad aparece meses después de la versión publicada, ¿qué información del SBOM permitiría responder más rápido?</summary>
<div class="respuesta">
<p>La respuesta será más rápida si el SBOM conserva nombre y versión de los componentes, identificadores como purl o CPE, relaciones de dependencia, fecha de generación y vínculo con la versión publicada exacta. Con esa información, la organización puede buscar qué artefactos contienen el componente vulnerable.</p>
<p>También ayudan las huellas criptográficas y el historial de SBOMs. Las huellas criptográficas permiten distinguir artefactos concretos. El historial permite saber cuándo entró una dependencia, qué versiones publicadas la incluyeron y cuándo fue corregida o reemplazada.</p>
<p>Si el SBOM está integrado con sistemas de monitoreo o VEX, la organización puede ir más allá de saber que el componente existe. Puede evaluar si la vulnerabilidad es explotable en ese producto, priorizar remediación y comunicar impacto con mayor precisión.</p>
</div>
</details>

<details class="qa">
<summary>Si un proyecto de código abierto no tiene incentivos regulatorios ni comerciales, ¿por qué debería producir SBOMs?</summary>
<div class="respuesta">
<p>Puede producir SBOMs para mejorar transparencia, facilitar adopción y apoyar a sus usuarios. Aunque el proyecto no esté obligado, otros sistemas pueden depender de él. Si esos consumidores tienen exigencias de seguridad o cumplimiento, un SBOM facilita la integración del proyecto en contextos más exigentes.</p>
<p>También ayuda al propio mantenimiento. Un SBOM permite detectar dependencias obsoletas, vulnerables o con licencias problemáticas. Puede mejorar la respuesta ante incidentes y hacer más visible el impacto de cambios en dependencias.</p>
<p>Por último, los SBOMs pueden convertirse en una señal de madurez del proyecto. No garantizan seguridad por sí mismos, pero muestran que el proyecto se preocupa por trazabilidad y gestión de la cadena de suministro.</p>
</div>
</details>

<details class="qa">
<summary>Si una organización usa varias herramientas para generar SBOMs, ¿cómo debería reconciliar diferencias entre sus salidas?</summary>
<div class="respuesta">
<p>Primero debería definir cuál es el alcance esperado del SBOM. No es lo mismo inventariar código fuente, artefacto construido, imagen de contenedor o entorno desplegado. Muchas diferencias entre herramientas aparecen porque analizan cosas distintas.</p>
<p>Después debería comparar resultados con criterios explícitos. Componentes presentes en una salida y ausentes en otra deben revisarse según su origen, ruta de dependencia, presencia en el artefacto final, tipo de dependencia y severidad de riesgo. Las discrepancias de licencias deben resolverse revisando fuentes oficiales del componente.</p>
<p>Finalmente, la organización debería documentar una fuente de verdad operacional. Puede elegir una herramienta principal, complementar con otra para ciertos ecosistemas y mantener reglas de reconciliación. Usar varias herramientas sin proceso aumenta ruido. Usarlas con un proceso claro puede mejorar cobertura.</p>
</div>
</details>

<details class="qa">
<summary>Si un SBOM representa solo paquetes, ¿qué aspectos del sistema quedan invisibles?</summary>
<div class="respuesta">
<p>Quedan invisibles componentes que no se expresan como paquetes tradicionales. Por ejemplo, archivos copiados manualmente, binarios descargados durante la construcción, guiones de automatización, servicios externos, configuraciones, secretos mal gestionados, interfaces de programación de aplicaciones de terceros, datos usados por el sistema o componentes del sistema operativo.</p>
<p>También pueden quedar fuera aspectos de procedencia y comportamiento. Un SBOM de paquetes no necesariamente muestra quién produjo un componente, cómo fue construido, con qué flujo de CI/CD, si fue firmado, si pasó pruebas de seguridad o si existe una atestación sobre su origen.</p>
<p>Esto no significa que un SBOM de paquetes no sirva. Sirve para una parte importante del riesgo, pero no debe confundirse con una descripción completa del sistema. En escenarios complejos se necesitan otros artefactos complementarios, como atestaciones, VEX, inventarios de infraestructura o AIBOMs.</p>
</div>
</details>

<details class="qa">
<summary>Si el software incluye un modelo de IA, ¿qué debería aparecer en un AIBOM que no aparece en un SBOM tradicional?</summary>
<div class="respuesta">
<p>Un AIBOM debería incluir información sobre modelos, conjuntos de datos, entrenamiento, evaluación y uso. Además de bibliotecas de software, debería documentar arquitectura del modelo, versión, origen, proveedor, licencia, métricas relevantes, limitaciones conocidas, datos de entrenamiento, datos de prueba y transformaciones aplicadas.</p>
<p>También debería registrar procedencia. Esto incluye de dónde vienen los modelos y conjuntos de datos, quién los produjo, bajo qué condiciones se pueden usar, si fueron modificados, afinados o cuantizados, y qué relación tienen con otros modelos o datos.</p>
<p>En sistemas con IA, la composición no se limita a paquetes. El comportamiento depende de datos, entrenamiento y configuración. Por eso un AIBOM busca capturar elementos que un SBOM tradicional no representa bien.</p>
</div>
</details>

<details class="qa">
<summary>Si un modelo de IA fue entrenado con un conjunto de datos externo, ¿qué información de procedencia, licencia y limitaciones debería registrarse?</summary>
<div class="respuesta">
<p>Debería registrarse el origen del conjunto de datos, su versión, proveedor, fecha de acceso, método de obtención y cualquier transformación aplicada antes del entrenamiento. También es importante indicar si el conjunto de datos es público, privado, sintético, derivado de otro conjunto de datos o combinado con varias fuentes.</p>
<p>La licencia debe documentarse con suficiente detalle para evaluar si el uso en entrenamiento, distribución o uso comercial está permitido. Algunos conjuntos de datos tienen restricciones de redistribución, atribución, investigación, uso comercial o tratamiento de datos personales.</p>
<p>Las limitaciones también son críticas. Deben registrarse sesgos conocidos, cobertura insuficiente, problemas de calidad, datos sensibles, restricciones geográficas, idioma, dominio, fecha de recolección y supuestos de uso. Sin esta información, es difícil evaluar responsabilidad, cumplimiento y riesgo del modelo entrenado.</p>
</div>
</details>

<details class="qa">
<summary>Si un modelo cambia su comportamiento con nuevos datos, ¿cómo cambia la idea de inventario?</summary>
<div class="respuesta">
<p>La idea de inventario deja de ser una fotografía estática. En software tradicional, un artefacto puede mantenerse relativamente estable después de la versión publicada. En sistemas con IA, el comportamiento puede cambiar por reentrenamiento, aprendizaje continuo, ajuste de parámetros, cambios de datos o modificaciones en la configuración de inferencia.</p>
<p>Por eso el inventario debe capturar versiones y relaciones a lo largo del ciclo de vida. No basta con decir qué modelo se usó. También hay que saber con qué datos fue entrenado, cuándo cambió, qué versión se desplegó, qué métricas tenía y qué decisiones se tomaron en cada actualización.</p>
<p>Esto vuelve más importante la trazabilidad temporal. Un AIBOM debería ayudar a reconstruir qué combinación de modelo, datos, código y configuración produjo cierto comportamiento en cierto momento.</p>
</div>
</details>

<details class="qa">
<summary>Si un AIBOM incluye detalles sobre conjuntos de datos, modelos e infraestructura, ¿qué riesgos de propiedad intelectual o privacidad aparecen?</summary>
<div class="respuesta">
<p>Aparece el riesgo de revelar información sensible sobre cómo fue construido el sistema. Detalles sobre conjuntos de datos, arquitectura, proveedores, modelos base o procesos de entrenamiento pueden exponer ventajas competitivas, secretos comerciales o decisiones estratégicas.</p>
<p>También puede haber riesgos de privacidad. Si un AIBOM describe conjuntos de datos con información personal, fuentes sensibles o procesos de recolección, podría revelar detalles que permitan inferir información sobre individuos, clientes o poblaciones. Incluso metadatos aparentemente inofensivos pueden ser sensibles en ciertos contextos.</p>
<p>Por eso la transparencia debe equilibrarse con control de acceso. Un AIBOM puede mantenerse interno, compartirse con auditores o entregarse de manera parcial a clientes. La clave es definir qué información se necesita para responsabilidad y cumplimiento sin exponer más de lo necesario.</p>
</div>
</details>

<details class="qa">
<summary>Si los SBOMs son una tecnología de transparencia, ¿transparencia para quién?</summary>
<div class="respuesta">
<p>La transparencia puede tener destinatarios distintos. Para desarrolladores, un SBOM entrega visibilidad sobre dependencias y cambios. Para equipos de seguridad, permite detectar vulnerabilidades y priorizar remediación. Para equipos legales o de cumplimiento, permite revisar licencias y obligaciones.</p>
<p>Para consumidores, clientes y auditores, el SBOM entrega evidencia sobre la composición del producto recibido. Para reguladores, puede servir como base de control y responsabilidad. Para proveedores, puede demostrar prácticas de gestión de cadena de suministro.</p>
<p>También existe una tensión. La misma información que ayuda a defensores puede ayudar a atacantes a identificar componentes vulnerables. Por eso la pregunta correcta no es solo si debe haber transparencia, sino qué nivel de transparencia, para qué actores, bajo qué condiciones y con qué mecanismos de protección.</p>
</div>
</details>

<details class="qa">
<summary>Si tuvieras que diseñar una política mínima de SBOMs para una empresa, ¿qué exigirías en generación, validación, almacenamiento y publicación?</summary>
<div class="respuesta">
<p>En generación, exigiría producir SBOMs automáticamente en el flujo de CI/CD para cada versión publicada y para cada imagen o artefacto distribuible. También exigiría registrar herramienta, versión de herramienta, fecha, estándar usado y alcance del análisis.</p>
<p>En validación, exigiría comprobar que el SBOM cumple el estándar declarado. También revisaría campos mínimos como componente principal, dependencias directas y transitivas, versiones, identificadores robustos, relaciones, licencias cuando aplique y huellas criptográficas cuando sea posible.</p>
<p>En almacenamiento, exigiría conservar los SBOMs asociados a versiones publicadas, construcciones candidatas y artefactos entregados a clientes. Deben quedar vinculados al artefacto exacto que describen y protegidos contra modificaciones no autorizadas.</p>
<p>En publicación, exigiría una regla clara. Para software interno, el SBOM puede quedar en sistemas corporativos. Para clientes o reguladores, debe existir un mecanismo de entrega confiable. Para software público, se debe decidir si se publica completo, parcialmente o bajo solicitud. La política debe incluir excepciones, responsables y criterios de bloqueo ante fallas de validación.</p>
</div>
</details>
