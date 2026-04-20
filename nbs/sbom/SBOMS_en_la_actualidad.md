---
title: "SBOMs en la actualidad"
subtitle: "Tensiones entre promesa, adopción y práctica"
format:
  html:
    toc: true
    callout-icon: false
    callout-appearance: simple
---

Hasta ahora hemos presentado los **Software Bill of Materials** como una respuesta técnica a un problema real. No basta con saber que una aplicación funciona. También necesitamos saber de qué está hecha, qué versiones usa, qué licencias arrastra y qué relaciones existen entre sus componentes.

La idea es poderosa. Un SBOM promete visibilidad, trazabilidad y una base automatizable para responder ante vulnerabilidades. También permite revisar licencias y gestionar riesgos de la cadena de suministro. Los estudios incluidos en `data/papers` muestran una tensión importante. La promesa de los SBOMs está más madura que muchas de sus prácticas reales.

::: {.callout-note title="Pregunta de partida"}
¿Qué tan confiable, completo, útil y accionable es un SBOM cuando sale del laboratorio y entra en proyectos reales, empresas reales y ecosistemas de software reales?
:::

## Lecturas base

Esta nota se apoya en tres trabajos que miran los SBOMs desde ángulos complementarios.

| Archivo | Foco del paper | Aporte para la discusión |
|---|---|---|
| `paper_1.pdf` | Adopción en proyectos open source | Muestra baja adopción, distribución irregular y problemas de completitud en SBOMs reales. |
| `paper_3.pdf` | Prácticas industriales | Muestra que la industria gestiona la cadena de suministro, aunque muchas veces sin SBOMs. |
| `paper_2.pdf` | AIBOMs y sistemas con IA | Extiende la discusión hacia modelos, datasets, entrenamiento y trazabilidad en sistemas con inteligencia artificial. |

: Lecturas usadas como base del material.

## La promesa

Un SBOM convierte una intuición en un artefacto. Si el software se construye ensamblando componentes, entonces necesitamos un inventario de esos componentes. En teoría, esto permite responder preguntas como estas.

- ¿Qué proyectos usan una versión vulnerable de una biblioteca?
- ¿Qué componentes tienen licencias incompatibles con una política interna?
- ¿Qué dependencias transitivas entran al sistema sin que el equipo las haya elegido explícitamente?
- ¿Qué artefactos deben revisarse cuando aparece una nueva vulnerabilidad?

Desde esta perspectiva, el SBOM no es solo un archivo JSON o XML. Es una pieza de infraestructura para tomar decisiones. Si se integra al proceso de desarrollo, puede alimentar análisis de vulnerabilidades, revisión de licencias, auditorías, gestión de proveedores y monitoreo continuo.

La tensión aparece cuando observamos la práctica.

::: {.column-margin}
**Idea para leer con lupa**

Un SBOM no es una fotografía neutral del sistema. Es una observación producida por una herramienta, en un momento específico y con reglas de análisis concretas.
:::

## Tensión 1. Baja adopción, alta expectativa

El estudio sobre proyectos open source muestra que la adopción de SBOMs todavía es baja, aunque crece desde 2021. Los autores identifican 186 repositorios públicos de GitHub que usan herramientas de generación asociadas a SPDX o CycloneDX. En ese conjunto, CycloneDX aparece como el estándar dominante y las herramientas integradas al build o a CI/CD son la vía más común para producir SBOMs (Nocera et al., 2025).

Esto sugiere que el problema ya no es solamente conceptual. Existen estándares, herramientas y presión regulatoria. Aun así, la adopción sigue siendo limitada.

Una posible interpretación es que muchos proyectos no perciben beneficios inmediatos. Otra es que la generación de SBOMs compite con otras tareas de mantenimiento, seguridad y release. También puede ocurrir que el incentivo venga desde fuera mediante clientes, gobiernos, auditorías, plataformas o regulaciones.

::: {.callout-important title="Para discutir"}
Si los SBOMs son tan útiles para la seguridad de la cadena de suministro, ¿por qué tantos proyectos todavía no los producen o no los publican?
:::

## Tensión 2. Generar no es distribuir

Usar una herramienta de generación no significa necesariamente que exista un SBOM disponible para consumidores del software. En el estudio open source, menos de la mitad de los proyectos analizados tenían SBOMs bajo control de versiones o adjuntos a releases públicas (Nocera et al., 2025).

La cifra es pedagógicamente importante. El paper reporta que los SBOMs estaban disponibles bajo control de versiones, en releases públicas o en ambos mecanismos en un 46% de los proyectos analizados. En los demás casos, los autores no encontraron un SBOM disponible, aunque sí detectaron uso de herramientas de generación (Nocera et al., 2025). Eso separa dos realidades que a veces se mezclan. Una cosa es tener capacidad de producir SBOMs. Otra es poner SBOMs útiles a disposición de otros.

| Acción | Pregunta que responde | Riesgo si falta |
|---|---|---|
| Generar | ¿Puedo construir el inventario? | El proyecto no conoce su composición. |
| Versionar | ¿Puedo saber cómo cambió el inventario? | No hay historia auditable del cambio. |
| Distribuir | ¿Puede usarlo alguien fuera del equipo? | El consumidor queda sin evidencia. |
| Consumir | ¿Puede otra herramienta tomar decisiones con esos datos? | El SBOM queda como documentación pasiva. |

: Cuatro acciones distintas que suelen mezclarse al hablar de SBOMs.

La seguridad aparece cuando estas capas se conectan. Un SBOM aislado, generado una vez y olvidado, se parece más a documentación desactualizada que a una práctica de seguridad.

## Tensión 3. Válido no siempre significa suficiente

No basta con producir un archivo en un formato conocido. Algunos SBOMs no cumplen completamente con la versión del estándar que declaran. Otros cumplen estructuralmente, pero omiten datos relevantes.

El paper sobre proyectos open source muestra problemas concretos. La información de supplier aparece en muy pocos casos. La fase del ciclo de vida no aparece. Las licencias aparecen solo en parte de los SBOMs y los hashes de componentes tampoco son universales. Además, aunque la mayoría de los SBOMs CycloneDX analizados eran válidos, la validez del formato no garantiza que estén todos los datos necesarios para los casos de uso esperados (Nocera et al., 2025).

::: {.callout-warning title="Distinción clave"}
Un SBOM puede ser válido como formato y débil como evidencia. La automatización depende de la calidad, completitud y consistencia de los datos.
:::

Por ejemplo, si un SBOM no identifica bien el componente primario, no distingue relaciones de dependencia, no incluye licencias o no usa identificadores robustos como purl o CPE, su utilidad para análisis posteriores disminuye.

El SBOM no elimina el problema de confianza. Lo mueve hacia la calidad del inventario y hacia la capacidad real de consumirlo.

## Tensión 4. Herramientas múltiples, resultados distintos

El paper con entrevistas a practicantes italianos muestra que la industria sí se preocupa por la cadena de suministro de software, pero no siempre usa SBOMs. Cuando no se usan, aparecen alternativas más manuales o parciales. Entre ellas hay documentación, UML, planillas, archivos de package managers, boletines de seguridad, herramientas SCA, scanners de vulnerabilidades y sistemas internos de monitoreo (Nocera et al., 2024).

El estudio entrevista a 10 practicantes de seis empresas. Solo una de esas empresas usa SBOMs para producir y distribuir inventarios de dependencias. Incluso dentro de esa empresa el conocimiento no es homogéneo. Algunos participantes describen reportes o archivos de dependencias sin reconocerlos necesariamente como SBOMs (Nocera et al., 2024).

Esto es revelador. La necesidad existe incluso cuando la palabra SBOM no está instalada.

En una de las empresas entrevistadas, el uso de SBOMs aparece integrado a CI/CD con herramientas como Syft, Trivy y XRay. Pero incluso ahí hay fricción. Distintas herramientas pueden producir listas diferentes de dependencias, falsos positivos o información contradictoria sobre licencias. La respuesta práctica no es simplemente usar una herramienta. También se requiere validar resultados y, a veces, agregar anotaciones manuales (Nocera et al., 2024).

::: {.callout-important title="Para discutir"}
Si dos herramientas generan SBOMs distintos para el mismo proyecto, ¿cuál representa la verdad del software?
:::

Una respuesta posible es que ningún SBOM es una verdad absoluta. Es una observación verificable, versionable y auditable. Esa mirada ayuda a discutir los SBOMs sin tratarlos como magia ni descartarlos por sus límites.

## Tensión 5. Cumplimiento, seguridad y trabajo organizacional

Los SBOMs suelen justificarse por seguridad, pero su valor depende de procesos organizacionales. Un SBOM útil requiere decisiones sobre el momento de generación, la herramienta usada, el formato, el estándar, la validación, la publicación y la respuesta ante vulnerabilidades.

El paper de entrevistas muestra que muchas prácticas asociadas a dependencias, licencias y procedencia siguen siendo manuales. Incluso en organizaciones grandes puede haber equipos que conocen SBOMs y otros que no, aunque trabajen en la misma empresa (Nocera et al., 2024).

Esto obliga a mirar los SBOMs como una práctica socio-técnica. No basta con enseñar el comando para generarlos. También hay que discutir incentivos, responsabilidades, transferencia de conocimiento, regulación, confianza entre productores y consumidores, y límites de la automatización.

::: {.callout-tip title="Lectura sugerida"}
Al revisar un SBOM, no preguntes solo si existe. Pregunta cuándo fue generado, con qué herramienta, bajo qué estándar, si fue validado, si acompaña al release y qué proceso lo consume.
:::

## Tensión 6. Cuando el software incluye inteligencia artificial

El paper sobre AIBOMs extiende la discusión hacia sistemas con inteligencia artificial. Un AIBOM busca documentar no solo bibliotecas y paquetes. También incluye modelos, datasets, procesos de entrenamiento, herramientas, infraestructura, métricas, licencias, procedencia, limitaciones y consideraciones éticas (Nocera et al., 2026).

Esto expande el problema. En software tradicional, un SBOM intenta responder de qué componentes está hecho el sistema. En sistemas con IA también importa cómo se entrenó un modelo, con qué datos, bajo qué supuestos, con qué sesgos potenciales, con qué restricciones de uso y cómo puede cambiar su comportamiento.

::: {.callout-warning title="Nueva dificultad"}
Si ya es difícil mantener un SBOM completo para software tradicional, ¿qué implica mantener un inventario confiable para modelos, datos, entrenamiento y comportamiento dinámico?
:::

El paper muestra que los AIBOMs prometen trazabilidad, cumplimiento, gestión de riesgo y transparencia. También enfrentan desafíos importantes. Entre ellos aparecen herramientas inmaduras, datos poco estructurados, interoperabilidad limitada, preocupación por propiedad intelectual, falta de educación y dificultad para capturar aspectos dinámicos de sistemas con IA (Nocera et al., 2026).

El SBOM tradicional no es el final de la conversación. Puede verse como una primera capa dentro de una familia más amplia de Bills of Materials para software, IA, hardware, datos y procesos.

## Referencias

Nocera, S., Di Penta, M., Francese, R., Romano, S., & Scanniello, G. (2024). If it's not SBOM, then what? How Italian practitioners manage the software supply chain. In *2024 IEEE International Conference on Software Maintenance and Evolution (ICSME)* (pp. 730-740). IEEE. https://doi.org/10.1109/ICSME58944.2024.00077

Nocera, S., Di Penta, M., Romano, S., Ahmed, F., & Scanniello, G. (2026). What we know about AIBOMs: Results from a multivocal literature review on artificial intelligence bill of materials. *ACM Transactions on Software Engineering and Methodology*. https://doi.org/10.1145/3786773

Nocera, S., Romano, S., Di Penta, M., Francese, R., & Scanniello, G. (2025). On the adoption of software bill of materials in open-source software projects. *Journal of Systems and Software, 230*, Article 112540. https://doi.org/10.1016/j.jss.2025.112540
