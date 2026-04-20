---
title: "Uso de IA para gestionar vulnerabilidades"
subtitle: "Detección, adopción industrial y reparación automática"
format:
  html:
    toc: true
    callout-icon: false
    callout-appearance: simple
---

La IA ya no aparece solo como una promesa distante para la seguridad de software. En la práctica, se usa para revisar código, priorizar hallazgos, explicar vulnerabilidades, sugerir parches y apoyar reportes. Esa amplitud puede hacer que el tema parezca resuelto. Si la herramienta detecta, explica y repara, entonces la gestión de vulnerabilidades podría volverse casi automática.

Los tres artículos usados en esta lectura muestran una imagen más incómoda. La IA puede ayudar, pero su valor depende de cómo se entrena, cómo se evalúa, cómo se integra al trabajo real y cómo se valida lo que propone. La pregunta importante no es si la IA puede participar en la gestión de vulnerabilidades. La pregunta es bajo qué condiciones su participación reduce riesgo en vez de producir una confianza prematura.

::: {.callout-note title="Pregunta de partida"}
¿La IA está gestionando vulnerabilidades o está acelerando decisiones que todavía necesitan evidencia humana, técnica y organizacional?
:::

## Lecturas base

Esta nota se apoya en tres artículos ubicados en `data/papers`.

| Archivo | Foco del artículo | Tensión que abre |
|---|---|---|
| `paper_4.pdf` | Detección de vulnerabilidades con LLMs en las Top 25 CWE | Un buen resultado dentro de distribución puede esconder mala generalización. |
| `paper_5.pdf` | Uso industrial de IA en Software Vulnerability Management | La adopción existe, pero confianza, contexto y gobierno siguen siendo problemas abiertos. |
| `paper_6.pdf` | Reparación automática de vulnerabilidades con modelos ajustados | Un parche puede parecer correcto según una métrica y aun así no ser funcional o seguro. |

: Lecturas usadas como base del material.

## La promesa

La gestión de vulnerabilidades combina tareas técnicas y decisiones de proceso. Hay que encontrar fallas, evaluar severidad, priorizar, asignar responsables, corregir, probar, documentar y comunicar. En ese recorrido, la IA parece atractiva porque puede reducir trabajo repetitivo y aumentar cobertura.

El estudio industrial de Kholoosi, Le y Babar (2026) muestra que esta promesa ya está entrando en los flujos reales de trabajo. De 60 practicantes encuestados en 27 países, 85% reporta algún uso de herramientas de IA para gestionar vulnerabilidades. Las herramientas aparecen en detección, evaluación, reparación y divulgación. Sin embargo, el mismo estudio muestra que la IA no reemplaza las prácticas existentes. Las herramientas de análisis estático y la revisión manual siguen siendo más frecuentes que las herramientas de IA.

::: {.column-margin}
**Idea para leer con lupa**

La IA no entra a un vacío. Entra a equipos, políticas, pipelines, tickets, revisiones y restricciones de cumplimiento.
:::

## Tensión 1. Detectar no es generalizar

Li et al. (2026) cuestionan una intuición frecuente. Un detector basado en LLM puede obtener buenos resultados en un conjunto de prueba y aun así fallar cuando enfrenta vulnerabilidades de otra distribución. La diferencia importa porque muchos conjuntos públicos tienen duplicados, etiquetas incorrectas y cobertura desigual entre CWE.

El contraste empírico es fuerte. Un modelo entrenado con BigVul alcanza 0.703 de exactitud dentro de distribución, pero cae a 0.493 en la parte real de BenchVul. En un conjunto balanceado, ese valor está cerca de adivinar. En cambio, un modelo entrenado con TitanVul logra 0.590 dentro de distribución y 0.881 en datos reales de BenchVul (Li et al., 2026).

La lectura no debería quedarse en cuál modelo gana. El punto es más profundo. La evaluación dentro de distribución puede premiar familiaridad con el conjunto de datos. La evaluación fuera de distribución pregunta si el modelo aprendió patrones de vulnerabilidad que viajan a nuevos proyectos, estilos de código y formas de explotación.

::: {.callout-warning title="Distinción clave"}
Una métrica alta puede indicar aprendizaje, pero también puede indicar fuga de datos, duplicación o una tarea de evaluación demasiado parecida al entrenamiento.
:::

## Tensión 2. Adoptar no es confiar

El estudio industrial muestra una adopción relevante. Entre quienes usan IA para gestión de vulnerabilidades, 69% reporta una experiencia positiva o muy positiva. Los practicantes valoran velocidad, cobertura y accesibilidad (Kholoosi et al., 2026).

Pero esa satisfacción convive con límites claros. Los participantes reportan falsos positivos, falta de contexto, recomendaciones desalineadas con reglas internas y dudas de confianza. También describen restricciones de privacidad, costos de integración, límites de tokens y dependencia de políticas organizacionales. La herramienta puede acelerar una revisión, pero también puede crear trabajo nuevo cuando sus resultados requieren verificación cuidadosa.

El hallazgo más importante para una clase de ciberseguridad es que la adopción es socio-técnica. Según Kholoosi et al. (2026), 80% de los participantes trata la IA como fuente de recomendaciones que requieren revisión humana. Solo 6% reporta decisiones automatizadas con mínima supervisión. Ese dato cambia el encuadre. En seguridad, usar IA de manera madura no significa delegar juicio. Significa diseñar puntos de control.

::: {.callout-important title="Para discutir"}
Si una herramienta de IA reduce tiempo de análisis, pero aumenta la necesidad de revisar explicaciones, parches y contexto, ¿cómo medimos realmente su productividad?
:::

## Tensión 3. Reparar no es producir texto parecido a un parche

La gestión de vulnerabilidades no termina en detectar. Un hallazgo útil debe conducir a una mitigación o corrección que preserve funcionalidad y reduzca riesgo. Han et al. (2026) muestran que evaluar reparación automática es especialmente delicado.

En reparación automática de vulnerabilidades, se han usado métricas como Exact Match, BLEU y CodeBLEU. Estas métricas comparan la salida del modelo con un parche de referencia. El problema es que puede haber múltiples parches válidos para la misma vulnerabilidad. Un parche puede no coincidir textualmente con la referencia y aun así corregir el problema.

El artículo introduce L-AVRBench, un benchmark con 70 funciones C/C++ vulnerables y suites ejecutables para evaluar funcionalidad y seguridad. En sus experimentos se generaron 7.560 parches y 131 fueron clasificados como correctos por el benchmark. De esos 131, solo 4 tuvieron Exact Match igual a 1 (Han et al., 2026). Esto muestra que una métrica textual puede subestimar reparaciones válidas.

La tensión va en ambas direcciones. Una métrica textual puede castigar un parche correcto, pero una prueba funcional también puede ser insuficiente si no cubre todos los caminos de ataque. Por eso Han et al. (2026) complementan las pruebas automáticas con análisis manual y distinguen entre parches razonables, no funcionales, no seguros y no razonables.

## Tensión 4. Los datos pueden inflar la capacidad aparente

Los tres artículos vuelven al mismo punto desde lugares distintos. La calidad de los datos condiciona lo que creemos saber sobre la IA.

Li et al. (2026) reportan problemas severos de duplicación y etiquetado en conjuntos públicos de detección. En su proceso removieron 22.807 pares redundantes por duplicación completa y 181.183 pares donde el código vulnerable era idéntico al código corregido. También muestran una cobertura desigual, por ejemplo 5.063 muestras para CWE-20 frente a solo 39 para CWE-798 en el conjunto consolidado.

Han et al. (2026) muestran un problema similar en reparación. Al eliminar solapamiento entre entrenamiento y prueba mediante una división cronológica, el Exact Match de VulRepair cae de 18.30% a 4.96%, y el de VulMaster de 20.47% a 5.15%. El resultado sugiere que parte del desempeño reportado podía estar midiendo memorización de parches similares, no capacidad de reparar vulnerabilidades nuevas.

::: {.callout-tip title="Lectura sugerida"}
Antes de aceptar una afirmación sobre IA para vulnerabilidades, pregunta cómo se construyó el conjunto de datos, qué duplicados se removieron, si hay fuga entre entrenamiento y prueba, y si la evaluación representa un flujo real.
:::

## Tensión 5. La IA puede ampliar cobertura y también ampliar incertidumbre

Una razón legítima para usar IA es la cobertura. Puede revisar más código, producir primeras explicaciones, ayudar a clasificar hallazgos y sugerir correcciones iniciales. Kholoosi et al. (2026) muestran que los practicantes valoran especialmente la rapidez y la integración en flujos de desarrollo. Algunos reportan uso en CI/CD, pull requests, revisión en IDE y generación de tickets.

Sin embargo, ampliar cobertura no elimina incertidumbre. Un detector puede fallar en vulnerabilidades fuera de distribución. Un asistente puede producir una explicación convincente sin entender restricciones del sistema. Un reparador puede generar un parche que compila, pero rompe comportamiento esperado o deja un vector de ataque abierto.

Esta es la tensión que el estudiante debe llevar al trabajo práctico. Herramientas como CodeQL, Grype o un LLM no responden la misma pregunta. CodeQL expresa consultas sobre propiedades del código. Grype contrasta componentes con bases de vulnerabilidades conocidas. Un LLM puede apoyar lectura, clasificación y generación de hipótesis. La gestión madura combina evidencia de varias fuentes y decide qué evidencia pesa más en cada caso.

## Tensión 6. Automatizar exige diseñar responsabilidad

Los artículos no proponen abandonar la IA. Proponen usarla con criterios más exigentes. Li et al. (2026) construyen BenchVul y TitanVul para mejorar evaluación y entrenamiento. Kholoosi et al. (2026) recomiendan explicabilidad, conciencia de contexto, integración con flujos de trabajo y prácticas de validación. Han et al. (2026) recomiendan evitar fuga de datos, evaluar con particiones cronológicas y usar pruebas que midan funcionalidad y seguridad.

La responsabilidad aparece en varios niveles. En el nivel técnico, hay que revisar datos, métricas, pruebas y contexto. En el nivel organizacional, hay que definir quién acepta hallazgos, quién aprueba parches, qué información puede enviarse a una herramienta externa y qué evidencia se exige antes de cerrar un ticket. En el nivel pedagógico, hay que enseñar a leer resultados de IA como afirmaciones que requieren auditoría.

::: {.callout-note title="Pregunta para el módulo"}
Si incorporas IA en un flujo de gestión de vulnerabilidades, ¿dónde pondrías los puntos obligatorios de validación y qué evidencia pedirías en cada uno?
:::

## Implicancias para leer herramientas de IA

| Aspecto | Pregunta crítica | Riesgo si se ignora |
|---|---|---|
| Detección | ¿Se evaluó fuera de distribución? | Confundir familiaridad con generalización. |
| Datos | ¿Hay duplicados, ruido o clases CWE subrepresentadas? | Inflar métricas y ocultar fallas en debilidades raras. |
| Adopción | ¿La herramienta entra como recomendación o como decisión automática? | Delegar juicio sin control organizacional. |
| Contexto | ¿El modelo ve reglas del proyecto, arquitectura y requisitos de cumplimiento? | Recibir recomendaciones plausibles pero inaplicables. |
| Reparación | ¿El parche se evalúa con pruebas funcionales y de seguridad? | Aceptar una corrección textual que no reduce riesgo real. |
| Gobierno | ¿Hay trazabilidad sobre entradas, salidas y aprobaciones? | Perder responsabilidad sobre decisiones de seguridad. |

: Preguntas mínimas para discutir IA en gestión de vulnerabilidades.

## Referencias

Han, W., Kwak, Y., Yu, M., Kim, K., Lee, Y., Moon, H., & Paek, Y. (2026). *Rethinking the capability of fine-tuned language models for automated vulnerability repair*. En *2026 IEEE/ACM 48th International Conference on Software Engineering (ICSE '26)*. ACM. https://doi.org/10.1145/3744916.3773167

Kholoosi, M. M., Le, T. H. M., & Babar, M. A. (2026). *Software vulnerability management in the era of artificial intelligence: An industry perspective*. En *Proceedings of 2026 IEEE/ACM International Conference on Software Engineering (ICSE '26)*. ACM. https://doi.org/10.48550/arXiv.2512.18261

Li, Y., Bui, N. T., Zhang, T., Yang, C., Zhou, X., Weyssow, M., Jiang, J., Chen, J., Huang, H., Nguyen, H. H., Ho, C. Y., Tan, J., Li, R., Yin, Y., Ang, H. W., Liauw, F., Ouh, E. L., Shar, L. K., & Lo, D. (2026). *Out of distribution, out of luck: How well can LLMs trained on vulnerability datasets detect Top 25 CWE weaknesses?* arXiv. https://doi.org/10.48550/arXiv.2507.21817
