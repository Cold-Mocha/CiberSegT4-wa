---
title: "Preguntas sobre gestión de vulnerabilidades e IA"
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

Esta página funciona como una guía de autoevaluación para la sección de vulnerabilidades. Cada pregunta incluye una respuesta desplegable para que puedas intentar responder primero y luego contrastar tu razonamiento.

Las preguntas se alinean con la lectura `Uso_de_IA_para__gestionar_vulnerabilidades.md`, que combina tres focos: detección de vulnerabilidades con LLMs, adopción industrial de IA en gestión de vulnerabilidades y reparación automática.

## Lo que deberías saber

<details class="qa">
<summary>¿Cuál es la diferencia entre un bug y una vulnerabilidad?</summary>
<div class="respuesta">
<p>Un bug es una falla de software que produce un comportamiento inesperado. Puede afectar disponibilidad, resultados, experiencia de usuario o lógica del sistema, pero no necesariamente permite una acción no autorizada.</p>
<p>Una vulnerabilidad es una debilidad que puede ser aprovechada por un adversario para afectar confidencialidad, integridad o disponibilidad. La diferencia clave está en la explotabilidad y el impacto de seguridad. Un bug puede ser molesto o costoso sin ser explotable. Una vulnerabilidad conecta una falla con una ruta realista de abuso.</p>
<p>Por eso, al analizar un hallazgo, no basta con preguntar si el código tiene un error. También hay que preguntar quién puede alcanzarlo, bajo qué condiciones, qué capacidades requiere el atacante y qué efecto produce si se explota.</p>
</div>
</details>

<details class="qa">
<summary>¿Qué condiciones hacen que una falla sea explotable?</summary>
<div class="respuesta">
<p>Para que una falla sea explotable debe existir una ruta realista entre el adversario y la debilidad. Esto implica que el atacante pueda alcanzar el componente afectado, controlar o influir en los datos relevantes y producir un efecto de seguridad observable.</p>
<p>También importa el contexto. Una misma debilidad puede ser crítica en un servicio expuesto a internet y casi irrelevante en una herramienta interna sin entrada controlable por terceros. La explotabilidad depende de superficie de ataque, permisos, validaciones, configuración, exposición y medidas compensatorias.</p>
<p>Por eso, el análisis defensivo no se limita a la presencia de una falla. Debe evaluar si existe una secuencia plausible de acciones que permita convertir esa falla en daño.</p>
</div>
</details>

<details class="qa">
<summary>¿Cuál es la diferencia entre severidad y riesgo?</summary>
<div class="respuesta">
<p>La severidad describe la gravedad técnica potencial de una vulnerabilidad. Suele apoyarse en métricas como CVSS y considera impacto, facilidad de explotación y condiciones técnicas generales.</p>
<p>El riesgo combina severidad con contexto. Incluye probabilidad de explotación, exposición del sistema, valor del activo afectado, existencia de controles compensatorios, explotación activa y consecuencias para la organización.</p>
<p>Dos vulnerabilidades con la misma severidad pueden tener riesgos distintos. Una puede estar en un servicio público con datos sensibles. Otra puede estar en un entorno aislado, sin ruta de acceso para adversarios. La priorización necesita ambas dimensiones.</p>
</div>
</details>

<details class="qa">
<summary>¿Cuál es la diferencia entre CWE y CVE?</summary>
<div class="respuesta">
<p>CWE clasifica tipos de debilidades. Describe patrones de error que pueden originar vulnerabilidades, como validación insuficiente, control de acceso incorrecto, exposición de información o inyección. CWE ayuda a hablar de la causa o familia del problema.</p>
<p>CVE identifica vulnerabilidades públicas específicas. Un CVE se refiere a un caso concreto en un producto, biblioteca, versión o componente determinado. Ayuda a coordinar comunicación, análisis, remediación y seguimiento entre organizaciones y herramientas.</p>
<p>Una forma práctica de distinguirlos es esta. CWE responde qué tipo de debilidad es. CVE responde qué vulnerabilidad pública específica fue reportada.</p>
</div>
</details>

<details class="qa">
<summary>¿Qué aporta CVSS y qué no debería esperarse de ese puntaje?</summary>
<div class="respuesta">
<p>CVSS aporta una estimación estandarizada de severidad. Resume características como impacto, complejidad de ataque, privilegios requeridos, interacción del usuario y alcance. Esto ayuda a ordenar hallazgos y comunicar urgencia de manera consistente.</p>
<p>CVSS no reemplaza el análisis contextual. Un puntaje alto no siempre implica máximo riesgo en todos los entornos, y un puntaje medio puede ser urgente si afecta un activo crítico o una ruta de ataque muy expuesta.</p>
<p>Por eso, CVSS debe usarse como una señal de priorización, no como decisión automática. La decisión final debe considerar exposición, criticidad del sistema, explotación conocida, disponibilidad de parche y controles compensatorios.</p>
</div>
</details>

<details class="qa">
<summary>¿Qué rol cumple la NVD en la gestión de vulnerabilidades?</summary>
<div class="respuesta">
<p>La National Vulnerability Database reúne y enriquece información sobre vulnerabilidades públicas. Para muchos CVE, entrega metadatos, referencias, puntajes, productos afectados y descripciones útiles para priorización.</p>
<p>Las herramientas de escaneo suelen consultar bases como NVD u otras fuentes de avisos para determinar si una dependencia o producto está asociado a una vulnerabilidad conocida. Esto convierte a NVD en una fuente importante para automatizar análisis.</p>
<p>Sin embargo, la información de NVD no debe leerse de forma aislada. Puede haber retrasos, cambios de puntaje, mapeos imperfectos o diferencias entre bases. Conviene contrastar con avisos del proveedor, repositorios oficiales y evidencia del entorno propio.</p>
</div>
</details>

<details class="qa">
<summary>¿Dónde entra MITRE ATT&CK si no es un catálogo de vulnerabilidades?</summary>
<div class="respuesta">
<p>MITRE ATT&CK describe tácticas y técnicas observadas en el comportamiento de adversarios. No clasifica debilidades de software ni identifica vulnerabilidades específicas. Su foco está en cómo actúa un atacante antes, durante o después de una intrusión.</p>
<p>ATT&CK complementa el análisis de vulnerabilidades porque ayuda a conectar una falla técnica con posibles acciones ofensivas. Por ejemplo, una vulnerabilidad puede facilitar ejecución de código, persistencia, robo de credenciales o movimiento lateral.</p>
<p>En un caso de estudio, mapear conductas a ATT&CK ayuda a comunicar el incidente con más precisión. No reemplaza la evidencia técnica, pero mejora la lectura defensiva y la relación con detección y respuesta.</p>
</div>
</details>

<details class="qa">
<summary>¿Qué diferencia hay entre análisis estático y escaneo de dependencias?</summary>
<div class="respuesta">
<p>El análisis estático revisa código fuente o representaciones derivadas del código para encontrar patrones inseguros. Puede detectar problemas como inyección, uso inseguro de datos, flujos peligrosos o errores de validación. CodeQL es un ejemplo de esta aproximación.</p>
<p>El escaneo de dependencias revisa componentes externos usados por el proyecto y los compara contra bases de vulnerabilidades conocidas. Busca responder si alguna biblioteca, paquete o versión incluida tiene vulnerabilidades públicas asociadas. Grype es un ejemplo de esta aproximación.</p>
<p>Ambos enfoques son complementarios. El análisis estático mira el código propio. El escaneo de dependencias mira el ecosistema que el proyecto incorpora. Un programa puede tener código propio seguro y aun así depender de una biblioteca vulnerable.</p>
</div>
</details>

<details class="qa">
<summary>¿Qué es CodeQL y por qué produce resultados en SARIF?</summary>
<div class="respuesta">
<p>CodeQL es una herramienta de análisis estático que modela el código como una base de datos consultable. Permite ejecutar consultas de seguridad y calidad sobre esa representación para detectar patrones problemáticos.</p>
<p>SARIF es un formato estándar para resultados de análisis estático. Permite describir reglas, hallazgos, ubicaciones de archivo, severidad, mensajes y metadatos de herramienta de manera interoperable.</p>
<p>Usar SARIF permite integrar resultados con plataformas, revisiones de código, sistemas de seguimiento y flujos de CI/CD. El valor no está solo en detectar hallazgos, sino en poder procesarlos, compararlos y gestionarlos de forma consistente.</p>
</div>
</details>

<details class="qa">
<summary>¿Qué es Grype y qué tipo de vulnerabilidades detecta?</summary>
<div class="respuesta">
<p>Grype es una herramienta que escanea componentes y dependencias para detectar vulnerabilidades conocidas. Lee manifiestos, paquetes instalados o artefactos como imágenes de contenedor, y compara los componentes encontrados con bases de vulnerabilidades.</p>
<p>Sus hallazgos suelen incluir identificador de vulnerabilidad, paquete afectado, versión actual, severidad, descripción y versión de corrección cuando existe. Esto permite priorizar actualización o mitigación de dependencias vulnerables.</p>
<p>Grype no prueba si una vulnerabilidad es explotable en el contexto específico de la aplicación. Indica que un componente vulnerable está presente o parece estarlo. La decisión defensiva requiere validar exposición, uso real del componente y disponibilidad de remediación.</p>
</div>
</details>

<details class="qa">
<summary>¿Qué significa usar IA para gestionar vulnerabilidades?</summary>
<div class="respuesta">
<p>Significa usar modelos o herramientas basadas en IA para apoyar tareas del ciclo de gestión de vulnerabilidades. Esto puede incluir detección, clasificación, priorización, explicación, generación de tickets, sugerencia de parches, documentación y apoyo a la divulgación.</p>
<p>No significa que la IA deba tomar toda la decisión. En seguridad, una recomendación debe conectarse con evidencia técnica, contexto del sistema, pruebas y responsabilidad organizacional.</p>
<p>La lectura actualizada propone ver la IA como parte de un flujo de trabajo. Su valor depende de cómo se entrena, cómo se evalúa, qué información puede ver, quién revisa sus salidas y qué controles existen antes de aceptar un hallazgo o un parche.</p>
</div>
</details>

<details class="qa">
<summary>¿Por qué detección, evaluación, reparación y divulgación son tareas distintas?</summary>
<div class="respuesta">
<p>Detectar consiste en identificar una posible vulnerabilidad. Evaluar consiste en decidir si el hallazgo aplica, qué severidad tiene y qué riesgo representa en un contexto concreto. Reparar consiste en modificar código, configuración o dependencias para reducir o eliminar el riesgo. Divulgar consiste en comunicar la vulnerabilidad de manera responsable a quienes deben actuar.</p>
<p>Una herramienta puede ser buena en una de estas tareas y débil en otra. Por ejemplo, un LLM puede explicar un hallazgo de forma clara, pero no generar un parche correcto. Un escáner puede detectar una dependencia vulnerable, pero no saber si esa funcionalidad se usa en producción.</p>
<p>Separar las tareas evita una conclusión apresurada. Que una herramienta ayude a detectar no implica que pueda priorizar, reparar o cerrar el ciclo sin validación.</p>
</div>
</details>

<details class="qa">
<summary>¿Qué significa que un modelo generalice fuera de distribución?</summary>
<div class="respuesta">
<p>Significa que el modelo mantiene buen desempeño cuando se evalúa en datos independientes, distintos de los usados para entrenar. En detección de vulnerabilidades, esto es crucial porque el mundo real no replica exactamente el conjunto de datos de entrenamiento.</p>
<p>Un modelo puede obtener alta exactitud dentro del mismo conjunto de datos y aun así fallar en muestras nuevas. Eso puede ocurrir si aprendió correlaciones superficiales, duplicados, estilos de código o marcas propias de la fuente original.</p>
<p>La generalización fuera de distribución es una señal más fuerte. Indica que el modelo aprendió patrones que viajan a otros contextos, aunque tampoco garantiza por sí sola que sea seguro usarlo sin revisión humana.</p>
</div>
</details>

<details class="qa">
<summary>¿Por qué los datos de entrenamiento son críticos en IA para vulnerabilidades?</summary>
<div class="respuesta">
<p>Los datos de entrenamiento determinan qué patrones puede aprender el modelo. Si los datos tienen duplicados, etiquetas incorrectas, clases desbalanceadas o ejemplos que no representan vulnerabilidades reales, el modelo puede aprender señales equivocadas.</p>
<p>En detección de vulnerabilidades, esto es especialmente sensible porque muchas debilidades son raras, contextuales y difíciles de etiquetar. Un modelo entrenado con datos ruidosos puede parecer efectivo en pruebas internas y fallar cuando enfrenta código real.</p>
<p>Por eso, la calidad del conjunto de datos no es un detalle secundario. Es parte central de la validez del detector y de la confianza que se puede tener en sus resultados.</p>
</div>
</details>

<details class="qa">
<summary>¿Qué enseñan BenchVul y TitanVul sobre evaluación de detectores?</summary>
<div class="respuesta">
<p>BenchVul y TitanVul muestran que la evaluación de detectores no puede depender solo de conjuntos públicos ruidosos. BenchVul se construye como benchmark curado para evaluar generalización. TitanVul busca mejorar entrenamiento mediante consolidación, deduplicación y validación de datos.</p>
<p>La tensión principal es que un modelo puede verse fuerte dentro de distribución y débil fuera de ella. En la lectura, un modelo entrenado con BigVul obtiene buen resultado interno, pero cae casi al azar en BenchVul real. Un modelo entrenado con TitanVul logra mejor desempeño fuera de distribución.</p>
<p>La lección es que el benchmark no es un trámite. Define qué significa tener evidencia. Si la evaluación se parece demasiado al entrenamiento, puede medir familiaridad con datos y no comprensión de vulnerabilidades.</p>
</div>
</details>

<details class="qa">
<summary>¿Qué significa que la adopción de IA en gestión de vulnerabilidades sea socio-técnica?</summary>
<div class="respuesta">
<p>Significa que el uso de IA no depende solo del modelo o de la herramienta. También depende de personas, flujos de trabajo, políticas, tickets, revisiones, restricciones de privacidad, cumplimiento, costos e integración con CI/CD.</p>
<p>El estudio industrial de Kholoosi, Le y Babar muestra que la IA se usa en varias etapas del ciclo de gestión, pero normalmente como apoyo y no como autoridad final. La mayoría de los participantes trata sus salidas como recomendaciones que requieren revisión humana.</p>
<p>Esto cambia la pregunta de diseño. No basta con preguntar si la herramienta acierta. Hay que preguntar cómo entra al proceso, quién valida, qué evidencia se registra y qué ocurre cuando la herramienta se equivoca.</p>
</div>
</details>

<details class="qa">
<summary>¿Por qué una experiencia positiva con IA no equivale a confianza total?</summary>
<div class="respuesta">
<p>Una experiencia positiva puede significar que la herramienta ahorra tiempo, mejora cobertura o ayuda a explicar hallazgos. Eso no implica que sus resultados sean correctos en todos los casos ni que puedan aceptarse sin revisión.</p>
<p>En la lectura, los practicantes valoran rapidez y accesibilidad, pero también reportan falsos positivos, falta de contexto, dudas de confianza y problemas de integración. Es posible que una herramienta sea útil y limitada al mismo tiempo.</p>
<p>En seguridad, la confianza debe basarse en evidencia, no solo en satisfacción. Una herramienta puede ser parte del flujo, pero sus salidas deben contrastarse con código, pruebas, contexto y criterios de riesgo.</p>
</div>
</details>

<details class="qa">
<summary>¿Por qué Exact Match no basta para evaluar reparación automática?</summary>
<div class="respuesta">
<p>Exact Match compara si el parche generado es idéntico al parche de referencia. El problema es que una vulnerabilidad puede tener más de una corrección válida. Un parche puede diferir textual o estructuralmente de la referencia y aun así eliminar la vulnerabilidad.</p>
<p>Han et al. muestran que, en L-AVRBench, muchos parches correctos no coinciden exactamente con la referencia. Esto vuelve injusta una evaluación puramente textual, porque castiga soluciones funcionalmente equivalentes.</p>
<p>La reparación de vulnerabilidades exige comprobar más que similitud de texto. Hay que evaluar compilación, comportamiento funcional, seguridad y razonabilidad de la corrección.</p>
</div>
</details>

<details class="qa">
<summary>¿Qué aporta una evaluación basada en pruebas como L-AVRBench?</summary>
<div class="respuesta">
<p>Una evaluación basada en pruebas permite observar si el parche generado compila, preserva funcionalidad y mitiga la vulnerabilidad. Esto se acerca más al objetivo de reparación que comparar tokens con un parche de referencia.</p>
<p>L-AVRBench incorpora funciones C/C++ vulnerables con pruebas ejecutables. Su valor está en que permite distinguir entre parches que solo se parecen a una solución y parches que efectivamente pasan pruebas funcionales y de seguridad.</p>
<p>Aun así, las pruebas no son garantía absoluta. Un parche puede pasar los casos disponibles y dejar caminos no cubiertos. Por eso la lectura combina evaluación automática con revisión manual de la razonabilidad del parche.</p>
</div>
</details>

<details class="qa">
<summary>¿Por qué un parche que compila no necesariamente es un parche seguro?</summary>
<div class="respuesta">
<p>Compilar solo demuestra que el código cumple las reglas sintácticas y de tipos del lenguaje. No demuestra que el comportamiento esperado se mantenga ni que la vulnerabilidad haya sido eliminada.</p>
<p>Un parche puede compilar y aun así romper funcionalidad, omitir casos límite, introducir una nueva debilidad o cerrar solo una parte del vector de ataque. En seguridad, eso puede generar una falsa sensación de cierre.</p>
<p>Por eso, la aceptación de un parche debe incluir pruebas funcionales, pruebas de seguridad, revisión de contexto y análisis de impacto. La reparación automática necesita más validación que una simple compilación exitosa.</p>
</div>
</details>

<details class="qa">
<summary>¿Cómo se complementan CodeQL, Grype y un LLM en un flujo de gestión?</summary>
<div class="respuesta">
<p>CodeQL ayuda a analizar código propio mediante consultas sobre patrones y flujos. Grype ayuda a identificar vulnerabilidades conocidas en componentes y dependencias. Un LLM puede apoyar lectura, explicación, clasificación inicial, generación de hipótesis y borradores de remediación.</p>
<p>No responden la misma pregunta. CodeQL puede mostrar una ruta de datos peligrosa. Grype puede mostrar que una versión de dependencia tiene un CVE. Un LLM puede ayudar a entender el contexto o sugerir próximos pasos, pero no sustituye la evidencia de las otras herramientas.</p>
<p>Un flujo maduro combina señales. Revisa si los hallazgos son alcanzables, si afectan activos relevantes, si hay parches disponibles y si las acciones propuestas realmente reducen riesgo.</p>
</div>
</details>

## Preguntas para responder

<details class="qa">
<summary>Si CodeQL reporta una posible inyección SQL, ¿qué deberías revisar antes de marcarla como crítica?</summary>
<div class="respuesta">
<p>Primero revisaría si la entrada que llega a la consulta puede ser controlada por un usuario o adversario. Luego revisaría si existe sanitización, parametrización, validación o alguna biblioteca que construya la consulta de forma segura.</p>
<p>También observaría el contexto de ejecución. No es lo mismo una consulta en una ruta pública de una aplicación web que una herramienta administrativa local. Importan permisos, exposición, datos afectados y posibilidad real de explotación.</p>
<p>Finalmente, revisaría si el hallazgo corresponde a una ruta ejecutable y si CodeQL muestra un flujo de datos claro desde la fuente no confiable hasta el uso peligroso. Solo después de validar esas condiciones corresponde priorizarlo como crítico.</p>
</div>
</details>

<details class="qa">
<summary>Si Grype reporta una vulnerabilidad crítica en una dependencia que no se usa en producción, ¿qué harías?</summary>
<div class="respuesta">
<p>No la descartaría automáticamente. Primero confirmaría si realmente no llega al artefacto productivo. Hay dependencias de desarrollo que no se empaquetan ni ejecutan en producción, pero también hay casos donde una dependencia marcada como desarrollo termina incluida en una imagen o entorno final.</p>
<p>Después evaluaría si la vulnerabilidad puede ser explotada durante construcción, pruebas, CI/CD o publicación. Algunas dependencias no afectan producción, pero sí pueden afectar la cadena de suministro si se ejecutan en flujos automatizados con secretos o permisos altos.</p>
<p>Si se confirma que no hay exposición, se puede bajar la prioridad o documentar una excepción. Aun así, conviene actualizar o eliminar la dependencia cuando sea razonable, porque el inventario cambia y una dependencia no usada hoy puede entrar en uso mañana.</p>
</div>
</details>

<details class="qa">
<summary>Si un repositorio no tiene manifiestos de dependencias, ¿significa que no tiene vulnerabilidades en dependencias?</summary>
<div class="respuesta">
<p>No. Significa que la herramienta puede tener menos fuentes para construir el inventario de dependencias. El repositorio podría usar binarios incluidos manualmente, dependencias del sistema operativo, imágenes de contenedor, scripts de instalación o paquetes resueltos fuera de los manifiestos tradicionales.</p>
<p>También puede ocurrir que el proyecto tenga dependencias en archivos no soportados por la herramienta o que el artefacto final incorpore componentes durante la construcción.</p>
<p>La conclusión correcta es que el alcance del escaneo fue limitado. Para afirmar con más confianza que no hay vulnerabilidades en dependencias, habría que analizar el artefacto construido, imágenes, entorno de ejecución o SBOM asociado.</p>
</div>
</details>

<details class="qa">
<summary>Si CodeQL y Grype entregan hallazgos distintos en el mismo repositorio, ¿cuál tiene razón?</summary>
<div class="respuesta">
<p>Pueden tener razón ambos, porque observan superficies distintas. CodeQL revisa código propio y patrones de implementación. Grype revisa componentes y vulnerabilidades conocidas en dependencias.</p>
<p>Un hallazgo de CodeQL puede existir aunque no haya dependencias vulnerables. Un hallazgo de Grype puede existir aunque el código propio no tenga patrones inseguros. También pueden relacionarse si el código usa de forma peligrosa una dependencia vulnerable.</p>
<p>La pregunta no debería ser cuál herramienta tiene razón, sino qué riesgo describe cada hallazgo. Hay que validar alcance, evidencia, severidad, exposición y remediación para cada caso.</p>
</div>
</details>

<details class="qa">
<summary>Si aparece un CVE nuevo después de haber ejecutado Grype, ¿el reporte anterior sigue siendo suficiente?</summary>
<div class="respuesta">
<p>No necesariamente. Un reporte de vulnerabilidades es válido para el momento y las bases de datos usadas en esa ejecución. Si aparece un CVE nuevo, un componente que antes parecía limpio puede quedar asociado a una vulnerabilidad.</p>
<p>Por eso el análisis de dependencias debe repetirse de forma periódica o integrarse a CI/CD y monitoreo. La seguridad de dependencias cambia aunque el código del proyecto no cambie.</p>
<p>También es importante conservar inventarios o SBOMs de versiones publicadas. Así, cuando aparece un CVE nuevo, se puede saber qué versiones del producto incluyeron el componente afectado.</p>
</div>
</details>

<details class="qa">
<summary>Si un hallazgo tiene CVSS alto, pero el componente no es alcanzable, ¿debe corregirse igual?</summary>
<div class="respuesta">
<p>Debe evaluarse con cuidado. Un CVSS alto indica severidad técnica potencial, pero el riesgo real depende de si el componente es alcanzable y explotable en el entorno concreto.</p>
<p>Si hay evidencia sólida de que no es alcanzable, puede priorizarse por debajo de otros hallazgos más expuestos. Sin embargo, la decisión debe documentarse, porque cambios futuros de configuración o uso podrían volverlo relevante.</p>
<p>Si existe una actualización segura y de bajo costo, suele ser razonable corregir de todos modos. Si la actualización es riesgosa, se puede justificar una mitigación temporal con controles compensatorios y seguimiento.</p>
</div>
</details>

<details class="qa">
<summary>Si una vulnerabilidad no tiene versión de corrección, ¿qué opciones defensivas quedan?</summary>
<div class="respuesta">
<p>La primera opción es reducir exposición. Puede deshabilitarse la funcionalidad afectada, limitar acceso, aplicar reglas de filtrado, cambiar configuración, aislar el componente o restringir permisos.</p>
<p>También se puede reemplazar la dependencia, aplicar un parche temporal, usar una rama mantenida por la comunidad o compensar con monitoreo y detección de explotación. En algunos casos, corresponde aceptar riesgo de forma formal por un tiempo limitado.</p>
<p>Lo importante es no tratar la ausencia de versión de corrección como ausencia de acción. Puede no haber actualización disponible, pero sí pueden existir mitigaciones mientras se espera una solución definitiva.</p>
</div>
</details>

<details class="qa">
<summary>Si un paquete legítimo fue comprometido y publicado con código malicioso, ¿Grype necesariamente lo detectará?</summary>
<div class="respuesta">
<p>No necesariamente. Grype se basa principalmente en vulnerabilidades conocidas y bases de datos asociadas a componentes y versiones. Si el paquete malicioso aún no tiene aviso, CVE o firma reconocida en las fuentes usadas, puede no aparecer como vulnerable.</p>
<p>Los ataques de cadena de suministro pueden requerir otras señales. Por ejemplo, cambios inesperados entre versiones, comportamiento de instalación sospechoso, ejecución automática, conexiones de red anómalas o alteraciones en el proceso de publicación.</p>
<p>Por eso, el escaneo de vulnerabilidades conocidas debe complementarse con verificación de integridad, revisión de cambios, monitoreo de comportamiento, protección de credenciales y controles de publicación.</p>
</div>
</details>

<details class="qa">
<summary>Si un incidente involucra robo de credenciales, ¿por qué actualizar la dependencia no basta?</summary>
<div class="respuesta">
<p>Actualizar la dependencia puede detener el uso de la versión maliciosa o vulnerable, pero no revierte efectos ya ocurridos. Si el atacante obtuvo credenciales, tokens o secretos, esos materiales pueden seguir siendo válidos aunque el paquete se actualice.</p>
<p>En ese caso corresponde rotar credenciales, revisar registros, buscar persistencia, analizar actividad de red, verificar accesos a servicios externos y evaluar qué datos pudieron quedar expuestos.</p>
<p>La actualización es una acción de contención o remediación técnica, pero la respuesta a incidentes debe considerar el alcance completo del compromiso.</p>
</div>
</details>

<details class="qa">
<summary>Si un LLM detecta una vulnerabilidad y explica su razonamiento, ¿deberías confiar en la explicación?</summary>
<div class="respuesta">
<p>No deberías confiar solo por la fluidez de la explicación. Los LLMs pueden producir explicaciones plausibles pero incorrectas. En seguridad, una justificación convincente debe contrastarse con el código, el flujo de datos, la configuración y el modelo de amenazas.</p>
<p>La explicación puede ser útil como hipótesis inicial. Puede orientar qué revisar, qué entrada es relevante o qué control parece faltar. Pero debe verificarse con evidencia técnica.</p>
<p>Una práctica razonable es tratar al LLM como asistente de análisis, no como autoridad. Sus hallazgos deben pasar por revisión humana, pruebas o contraste con herramientas especializadas.</p>
</div>
</details>

<details class="qa">
<summary>Si un modelo tiene alta exactitud dentro de distribución y baja fuera de distribución, ¿qué indica?</summary>
<div class="respuesta">
<p>Indica que probablemente no generaliza bien. Puede haber aprendido patrones propios del conjunto de entrenamiento, duplicados, estilo de los ejemplos o artefactos de etiquetado, en vez de patrones reales de vulnerabilidad.</p>
<p>En detección de vulnerabilidades, esto es grave porque el código real suele diferir de los datos de entrenamiento. Un modelo que falla fuera de distribución puede dar una falsa sensación de seguridad.</p>
<p>La evaluación útil debe incluir benchmarks independientes, cobertura por tipos de CWE y análisis de desempeño en clases raras. La exactitud interna no basta para afirmar que el detector será confiable.</p>
</div>
</details>

<details class="qa">
<summary>Si un conjunto de datos tiene muchos duplicados, ¿cómo puede afectar a un detector basado en aprendizaje automático?</summary>
<div class="respuesta">
<p>Los duplicados pueden inflar métricas. Si ejemplos muy similares aparecen en entrenamiento y prueba, el modelo puede memorizar patrones en vez de aprender características generales de vulnerabilidad.</p>
<p>También pueden distorsionar la distribución de clases. Algunas CWE o estilos de código pueden aparecer artificialmente sobrerrepresentados, haciendo que el modelo parezca fuerte en patrones frecuentes y débil en otros.</p>
<p>Por eso la deduplicación es parte esencial de una evaluación seria. Sin ella, la métrica puede reflejar repetición de datos más que capacidad de detección.</p>
</div>
</details>

<details class="qa">
<summary>Si una CWE crítica aparece poco en los datos, ¿cómo debería cambiar la evaluación?</summary>
<div class="respuesta">
<p>La evaluación no debería depender solo del promedio global. Un modelo puede tener buen desempeño promedio porque acierta clases frecuentes y aun así fallar en debilidades raras pero críticas.</p>
<p>Conviene reportar desempeño por CWE, especialmente en clases poco representadas. También puede ser necesario balancear benchmarks, generar datos adicionales validados o usar evaluación específica para clases de alto impacto.</p>
<p>La decisión defensiva debe considerar riesgo, no solo frecuencia. Una debilidad poco común puede ser muy grave si permite exposición de credenciales, ejecución remota o bypass de autenticación.</p>
</div>
</details>

<details class="qa">
<summary>Si una herramienta de IA reduce tiempo de análisis pero aumenta revisión manual, ¿cómo medirías su productividad?</summary>
<div class="respuesta">
<p>No mediría solo tiempo de respuesta de la herramienta. Mediría el ciclo completo, incluyendo revisión humana, validación técnica, corrección de falsos positivos, pruebas, documentación y cierre del ticket.</p>
<p>También miraría calidad de los resultados. Una herramienta rápida pero ruidosa puede desplazar trabajo hacia revisión. Una herramienta más lenta pero precisa puede ahorrar tiempo total si reduce retrabajo.</p>
<p>En gestión de vulnerabilidades, productividad real significa reducir riesgo con evidencia. Por eso conviene medir tiempo hasta remediación validada, tasa de falsos positivos, cobertura útil, aceptación de parches y costo de verificación.</p>
</div>
</details>

<details class="qa">
<summary>Si el 69% de los practicantes reporta satisfacción con IA, ¿qué conclusión sería apresurada?</summary>
<div class="respuesta">
<p>Sería apresurado concluir que la IA puede gestionar vulnerabilidades de forma autónoma. La satisfacción indica utilidad percibida, pero no elimina problemas de confianza, contexto, falsos positivos o validación.</p>
<p>En el estudio industrial, la adopción positiva convive con supervisión humana y gobierno organizacional. Muchos practicantes usan IA como apoyo para acelerar o ampliar tareas, no como sustituto de revisión experta.</p>
<p>La conclusión prudente es que la IA ya tiene valor práctico, pero ese valor depende de controles. La satisfacción debe leerse junto con cómo se valida la salida y quién asume responsabilidad por la decisión final.</p>
</div>
</details>

<details class="qa">
<summary>Si un equipo quiere dejar que la IA cierre automáticamente tickets de vulnerabilidad, ¿qué objeciones plantearías?</summary>
<div class="respuesta">
<p>La primera objeción es que cerrar un ticket requiere evidencia. Hay que demostrar que el hallazgo aplicaba, que la corrección fue implementada, que las pruebas pasan y que el riesgo fue reducido o aceptado formalmente.</p>
<p>La segunda objeción es la responsabilidad. Si la IA cierra un ticket por error, el equipo debe saber quién revisó, qué evidencia se usó y cómo se detectará una regresión o explotación posterior.</p>
<p>Una alternativa más segura es que la IA proponga cierre con evidencia adjunta. El cierre final debería pasar por revisión humana o por reglas automatizadas bien definidas, trazables y limitadas a casos de bajo riesgo.</p>
</div>
</details>

<details class="qa">
<summary>Si un LLM propone un parche que pasa las pruebas unitarias, ¿qué revisarías antes de aceptarlo?</summary>
<div class="respuesta">
<p>Revisaría si las pruebas cubren la condición de seguridad que originó el hallazgo. Pasar pruebas unitarias generales no demuestra que la vulnerabilidad haya sido corregida.</p>
<p>También revisaría si el parche preserva comportamiento esperado, no introduce efectos secundarios, no elimina validaciones importantes y no crea una nueva debilidad. Si el cambio afecta autenticación, autorización, criptografía o manejo de entradas, la revisión debe ser especialmente estricta.</p>
<p>Finalmente, pediría evidencia de seguridad. Puede ser una prueba de regresión específica, un caso que antes explotaba y ahora falla, una consulta CodeQL que deja de reportar el flujo o una verificación manual del modelo de amenazas.</p>
</div>
</details>

<details class="qa">
<summary>Si un parche generado por IA no coincide con el parche de referencia, ¿debe rechazarse?</summary>
<div class="respuesta">
<p>No necesariamente. En reparación de vulnerabilidades puede haber varias soluciones válidas. Un parche puede diferir del arreglo original y aun así eliminar la condición vulnerable.</p>
<p>La comparación textual con una referencia sirve como señal, pero no como criterio absoluto. Exact Match puede castigar soluciones correctas que usan otra estructura, otra constante o una validación equivalente.</p>
<p>La decisión debería basarse en pruebas funcionales, pruebas de seguridad y revisión de razonabilidad. Si el parche conserva comportamiento, elimina el vector de ataque y se integra bien al proyecto, puede ser aceptable aunque no sea idéntico al parche histórico.</p>
</div>
</details>

<details class="qa">
<summary>Si un parche generado por IA elimina la vulnerabilidad pero rompe funcionalidad, ¿cómo lo clasificarías?</summary>
<div class="respuesta">
<p>Lo clasificaría como una corrección incompleta o no aceptable. Reducir el riesgo de seguridad no basta si el cambio rompe comportamiento esencial del sistema.</p>
<p>En la lógica de evaluación de reparación automática, este tipo de salida puede ser no funcionalmente correcta. Puede bloquear el vector vulnerable, pero a costa de cambiar lo que el programa debía hacer.</p>
<p>Una reparación útil debe equilibrar seguridad y funcionalidad. Si no se puede lograr de inmediato, el equipo debe decidir entre mitigación temporal, rediseño, parche manual o aceptación de riesgo documentada.</p>
</div>
</details>

<details class="qa">
<summary>Si un parche pasa pruebas funcionales y de seguridad, ¿por qué aún podría necesitar revisión humana?</summary>
<div class="respuesta">
<p>Porque las pruebas no cubren todo el espacio posible de entradas, configuraciones y usos. Un parche puede pasar los casos disponibles y aun así dejar un camino no cubierto o introducir una debilidad en otro contexto.</p>
<p>La revisión humana puede detectar problemas de diseño, inconsistencias con el estilo del proyecto, efectos sobre mantenibilidad, requisitos regulatorios o supuestos no representados en las pruebas.</p>
<p>En seguridad, las pruebas son evidencia fuerte, pero no son toda la evidencia. La revisión humana ayuda a interpretar el cambio dentro del sistema completo.</p>
</div>
</details>

<details class="qa">
<summary>Si un equipo usa un LLM externo para analizar vulnerabilidades, ¿qué riesgos de gobierno aparecen?</summary>
<div class="respuesta">
<p>Aparecen riesgos de confidencialidad, privacidad, cumplimiento y trazabilidad. El equipo puede enviar código propietario, secretos, fragmentos de arquitectura, datos de clientes o información sobre vulnerabilidades no divulgadas a un servicio externo.</p>
<p>También aparece el problema de auditoría. Hay que saber qué se envió, qué respondió el modelo, quién revisó la salida y si esa salida influyó en una decisión de seguridad.</p>
<p>Una política madura debería definir qué datos pueden compartirse, qué modelos están permitidos, cómo se registran las decisiones y cuándo se requiere una herramienta local o aprobada por la organización.</p>
</div>
</details>

<details class="qa">
<summary>Si diseñaras puntos de validación para IA en un pipeline de vulnerabilidades, ¿dónde los pondrías?</summary>
<div class="respuesta">
<p>Pondría un primer punto después de la detección, para confirmar que el hallazgo aplica y no es solo ruido. Pondría otro antes de priorizar, para incorporar exposición, severidad, activos afectados y contexto de negocio.</p>
<p>Pondría un punto fuerte antes de aceptar un parche, con revisión de código, pruebas funcionales y pruebas de seguridad. También pondría una verificación después del merge o despliegue, para confirmar que el hallazgo ya no aparece y que no hubo regresión.</p>
<p>Además, registraría evidencia en el ticket. La IA puede acelerar análisis, pero el flujo debe conservar trazabilidad sobre qué se aceptó, por qué y con qué evidencia.</p>
</div>
</details>

<details class="qa">
<summary>Si sintetizas ejemplos de vulnerabilidades para entrenar un modelo, ¿qué riesgos aparecen?</summary>
<div class="respuesta">
<p>El primer riesgo es crear ejemplos artificiales demasiado limpios, repetitivos o alejados del código real. El modelo podría aprender patrones de generación y no patrones reales de vulnerabilidad.</p>
<p>El segundo riesgo es etiquetar mal. Un ejemplo sintético puede parecer vulnerable, pero no ser explotable, o puede no corresponder exactamente a la CWE que se quiere representar.</p>
<p>La síntesis puede ser útil para clases poco representadas, pero requiere validación. Idealmente debe combinarse con revisión humana, comparación con datos reales y evaluación fuera de distribución.</p>
</div>
</details>

<details class="qa">
<summary>Si tuvieras que priorizar hallazgos de CodeQL, Grype y un LLM en una misma semana, ¿qué criterios usarías?</summary>
<div class="respuesta">
<p>Usaría severidad técnica, exposición, explotabilidad, criticidad del activo, disponibilidad de corrección y evidencia de explotación activa. También consideraría si el hallazgo afecta datos sensibles, autenticación, autorización o ejecución remota.</p>
<p>Para CodeQL, revisaría si el flujo vulnerable es alcanzable por entradas no confiables y si falta un control real. Para Grype, revisaría si la dependencia afectada está en el artefacto productivo, si se usa la funcionalidad vulnerable y si existe versión de corrección. Para un LLM, pediría evidencia verificable y no solo una explicación plausible.</p>
<p>La prioridad final debería equilibrar impacto y factibilidad. A veces una actualización de dependencia crítica es rápida. Otras veces un hallazgo de código propio requiere rediseño. La gestión debe ser explícita y trazable.</p>
</div>
</details>

<details class="qa">
<summary>Si una herramienta entrega muchos falsos positivos, ¿deberías dejar de usarla?</summary>
<div class="respuesta">
<p>No necesariamente. Primero conviene ajustar configuración, reglas, exclusiones y alcance. Algunas herramientas son muy útiles, pero necesitan calibración para el lenguaje, arquitectura y riesgos del proyecto.</p>
<p>También se puede usar la herramienta en etapas específicas. Por ejemplo, bloquear solo hallazgos de alta confianza y dejar otros como advertencias revisables. Esto evita fatiga sin perder visibilidad.</p>
<p>Dejar de usarla puede ser razonable si el costo de revisión supera consistentemente el valor de los hallazgos. Pero esa decisión debería basarse en evidencia y no solo en frustración inicial.</p>
</div>
</details>

<details class="qa">
<summary>Si una vulnerabilidad aparece en una dependencia transitiva, ¿quién debería corregirla?</summary>
<div class="respuesta">
<p>La corrección puede requerir varias capas. El equipo consumidor puede actualizar la dependencia directa que trae la transitiva, forzar una versión segura si el ecosistema lo permite o reemplazar la biblioteca afectada.</p>
<p>El mantenedor de la dependencia directa también puede necesitar actualizar sus propias dependencias. En proyectos de código abierto, puede ser necesario abrir un reporte de problema, enviar una solicitud de cambios o esperar una versión nueva.</p>
<p>Desde la perspectiva del producto, la responsabilidad operativa recae en quien distribuye o ejecuta el software. Aunque la falla venga de una dependencia transitiva, el equipo debe gestionar el riesgo mientras llega una corrección desde el proyecto mantenedor.</p>
</div>
</details>

<details class="qa">
<summary>Si un CVE no tiene CWE asociado, ¿pierde utilidad para el análisis?</summary>
<div class="respuesta">
<p>No pierde toda utilidad. El CVE sigue identificando una vulnerabilidad pública específica y puede incluir descripción, referencias, versiones afectadas y severidad.</p>
<p>Sin CWE, se pierde una capa de clasificación causal. Es más difícil agrupar el problema con familias de debilidades similares, extraer lecciones de desarrollo seguro o analizar tendencias por tipo de error.</p>
<p>En ese caso conviene revisar la descripción técnica y referencias para inferir la naturaleza de la debilidad, pero evitando etiquetar con demasiada seguridad si la evidencia no alcanza.</p>
</div>
</details>

<details class="qa">
<summary>Si diseñaras una política mínima de gestión de vulnerabilidades con IA, ¿qué exigirías?</summary>
<div class="respuesta">
<p>Exigiría escaneo periódico de código propio y dependencias, registro de hallazgos, criterios de severidad, responsables claros y tiempos esperados de remediación según criticidad.</p>
<p>Para la IA, exigiría reglas adicionales. Toda salida debe tratarse como recomendación hasta que exista validación. Los parches generados deben pasar revisión de código, pruebas funcionales y pruebas de seguridad. Las decisiones deben quedar trazadas en tickets o registros equivalentes.</p>
<p>También definiría límites de uso. No todo código o información sensible puede enviarse a herramientas externas. Toda excepción debe documentarse con razón, evidencia, fecha de revisión y responsable.</p>
</div>
</details>

<details class="qa">
<summary>Si tuvieras que cerrar una vulnerabilidad asistida por IA, ¿qué evidencia mínima pedirías?</summary>
<div class="respuesta">
<p>Pediría identificación del hallazgo, explicación de por qué aplica, evidencia de alcance, decisión de severidad o riesgo, cambio aplicado y responsable de revisión.</p>
<p>También pediría pruebas. Si era código propio, una prueba de regresión o una consulta que demuestre que el flujo vulnerable ya no existe. Si era dependencia, evidencia de actualización o mitigación y confirmación de que el artefacto final ya no contiene la versión afectada.</p>
<p>Finalmente, pediría trazabilidad sobre la IA. Si el modelo sugirió diagnóstico o parche, debe quedar claro qué parte fue aceptada, qué fue modificada y quién asumió la decisión final.</p>
</div>
</details>
