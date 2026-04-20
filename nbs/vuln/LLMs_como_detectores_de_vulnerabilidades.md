---
title: "LLMs como detectores de vulnerabilidades"
subtitle: "Generalización, datos y límites de la automatización"
format:
  html:
    toc: true
    callout-icon: false
    callout-appearance: simple
---

Los modelos de lenguaje se han vuelto atractivos para tareas de seguridad de software. Pueden leer código, explicar fragmentos, comparar versiones, sugerir reparaciones y clasificar funciones como vulnerables o no vulnerables. Esta capacidad parece encajar naturalmente con el análisis de vulnerabilidades. Si un modelo puede razonar sobre código, ¿por qué no usarlo como detector?

El artículo base de esta lectura plantea una tensión central. El problema no es solo si un modelo logra buen desempeño en un conjunto de prueba. El problema es si ese desempeño se mantiene cuando el modelo enfrenta vulnerabilidades fuera de la distribución de entrenamiento (Li et al., 2026).

::: {.callout-note title="Pregunta de partida"}
¿Un LLM que obtiene alta exactitud en un conjunto de datos de vulnerabilidades está aprendiendo patrones reales de seguridad o está aprendiendo las marcas particulares de ese conjunto de datos?
:::

## Lectura base

Esta nota se apoya en el artículo `data/papers/paper_4.pdf`.

| Archivo | Foco del artículo | Aporte para la discusión |
|---|---|---|
| `paper_4.pdf` | LLMs y detección de vulnerabilidades en las Top 25 CWE | Muestra que el desempeño dentro de distribución puede ser engañoso y que la calidad del conjunto de datos condiciona fuertemente la generalización. |

: Lectura usada como base del material.

El trabajo presenta tres piezas principales. **BenchVul** es un benchmark manualmente curado y balanceado para evaluar detección de vulnerabilidades en las MITRE Top 25 CWE. **TitanVul** es un conjunto de datos de entrenamiento construido a partir de siete fuentes públicas, con deduplicación y validación mediante un flujo multiagente con LLMs. **RVG** es un mecanismo para sintetizar ejemplos realistas de vulnerabilidades poco representadas (Li et al., 2026).

## La promesa

La promesa es clara. Un LLM podría analizar grandes volúmenes de código y detectar vulnerabilidades antes de que lleguen a producción. En un flujo de desarrollo seguro, esto permitiría apoyar revisiones de código, priorizar hallazgos, reducir trabajo manual y complementar herramientas como análisis estático o escaneo de dependencias.

El atractivo aumenta porque muchas investigaciones formulan la detección de vulnerabilidades como una tarea de clasificación a nivel de función. Dada una función, el modelo debe decidir si contiene o no una vulnerabilidad. Esta formulación es simple, medible y fácil de integrar con experimentos de aprendizaje automático.

La tensión aparece cuando miramos cómo se evalúan estos modelos.

::: {.column-margin}
**Idea para leer con lupa**

En detección de vulnerabilidades, una exactitud alta puede medir familiaridad con un conjunto de datos, no necesariamente comprensión de una debilidad explotable.
:::

## Tensión 1. Buen resultado no significa buena generalización

El artículo distingue entre evaluación **dentro de distribución** y evaluación **fuera de distribución**. La primera prueba el modelo con datos que provienen del mismo conjunto de datos usado para entrenar. La segunda lo prueba con un benchmark independiente, construido para medir generalización sobre muestras no vistas (Li et al., 2026).

La diferencia importa porque varios conjuntos de datos de vulnerabilidades tienen ruido, duplicación y etiquetas incorrectas. Si el entrenamiento y la prueba vienen del mismo origen, el modelo puede aprender correlaciones superficiales. Puede aprender el estilo del conjunto de datos, los patrones de confirmaciones de cambio o las marcas de ciertas fuentes, sin aprender realmente la vulnerabilidad.

Los resultados del artículo son elocuentes. Un modelo entrenado con BigVul alcanza la mayor exactitud dentro de distribución, con 0.703. Sin embargo, cae a 0.493 en la parte real de BenchVul, que es casi equivalente a adivinar al azar en un conjunto balanceado. En cambio, un modelo entrenado con TitanVul obtiene una exactitud interna más modesta, 0.590, pero alcanza 0.881 en datos reales de BenchVul (Li et al., 2026).

::: {.callout-warning title="Distinción clave"}
La evaluación dentro de distribución puede premiar sobreajuste. La evaluación fuera de distribución pregunta si el modelo aprendió algo que viaja a otros datos.
:::

## Tensión 2. El conjunto de datos no es un detalle técnico

En aprendizaje automático, a veces se habla del conjunto de datos como si fuera solo el combustible del modelo. En detección de vulnerabilidades, el conjunto de datos es parte del problema científico. Si contiene duplicados, etiquetas incorrectas o ejemplos que no representan vulnerabilidades reales, el modelo aprende sobre una realidad deformada.

El artículo reporta problemas severos en conjuntos de datos públicos. En el análisis inicial, se removieron 22.807 pares redundantes por duplicación completa y 181.183 pares donde el código vulnerable era idéntico al código corregido. En total, el proceso redujo el corpus inicial de 304.726 pares a 100.736 después de dos etapas de deduplicación interna (Li et al., 2026).

También aparece un problema de cobertura. Muchas muestras se concentran en pocas CWE, mientras que debilidades críticas quedan subrepresentadas. En el conjunto consolidado, CWE-20 tiene 5.063 muestras y CWE-798 tiene solo 39. Esa diferencia es relevante porque CWE-798, asociada a credenciales codificadas directamente en el programa, puede tener consecuencias graves aunque aparezca poco en los datos (Li et al., 2026).

::: {.callout-important title="Para discutir"}
Si una vulnerabilidad crítica aparece poco en los datos, ¿el modelo debería ser evaluado por su promedio global o por su desempeño en esa clase rara?
:::

## Tensión 3. Detectar código vulnerable no es lo mismo que distinguir una vulnerabilidad de su corrección

Una de las observaciones más interesantes del artículo es la diferencia entre detectar código "parecido a vulnerable" y distinguir una vulnerabilidad de su corrección. Algunos conjuntos de datos comparan código vulnerable con código benigno general. Esa tarea puede ser más fácil que comparar una función vulnerable con su versión corregida.

El artículo muestra que modelos entrenados en conjuntos de datos como Real-Vul y ReVeal pueden lograr resultados muy altos dentro de distribución, incluso sobre 0.960 en Real-Vul. Sin embargo, cuando se evalúan fuera de distribución con BenchVul, su desempeño cae cerca del azar. La interpretación propuesta es que los modelos aprenden señales de código vulnerable en sentido amplio, pero no necesariamente la diferencia semántica precisa entre la vulnerabilidad y su arreglo (Li et al., 2026).

Esta tensión es importante para el curso. En seguridad, el detalle semántico importa. Un detector útil no solo debe reconocer que un fragmento "se ve peligroso". Debe identificar por qué una condición permite explotación y por qué una modificación elimina o reduce ese riesgo.

## Tensión 4. Los LLMs son parte del detector y parte del laboratorio

El artículo no usa LLMs solo como detectores. También los usa para filtrar, validar y generar datos. TitanVul se construye con un flujo multiagente que revisa pares de vulnerabilidad y corrección. RVG usa agentes con roles como modelador de amenazas, implementador vulnerable, auditor de seguridad y revisor de seguridad para crear ejemplos realistas de vulnerabilidades poco representadas (Li et al., 2026).

Esto abre una tensión metodológica. Los LLMs ayudan a mejorar conjuntos de datos, pero también introducen preguntas sobre confianza. ¿Qué pasa si el mismo tipo de tecnología que se evalúa también participa en la curación de los datos? El artículo mitiga este riesgo con revisión manual. BenchVul alcanza una tasa de corrección de 92%, y TitanVul una validez de 94% según auditoría manual posterior (Li et al., 2026).

::: {.callout-tip title="Lectura sugerida"}
Al evaluar un detector basado en LLMs, pregunta siempre quién construyó el conjunto de datos, cómo se validaron las etiquetas y si hubo revisión humana sobre los ejemplos críticos.
:::

## Tensión 5. Los modelos conversacionales fuertes tampoco resuelven todo

Podría pensarse que modelos generales muy potentes, usados con instrucciones cuidadosamente diseñadas, bastan para detectar vulnerabilidades. El artículo evalúa GPT-4.1 y Claude-3.7-Sonnet con estrategias directas, razonamiento paso a paso y aprendizaje con pocos ejemplos. Sus resultados son modestos, con muchas exactitudes entre 0.5 y 0.7 (Li et al., 2026).

Esto no significa que esos modelos sean inútiles. Significa que la detección precisa de vulnerabilidades sigue siendo difícil, incluso para modelos avanzados. La tarea exige más que leer código. Requiere entender contexto, flujo de datos, precondiciones de explotación, relación entre versión vulnerable y versión corregida, y diferencias finas entre bug común y debilidad explotable.

La lección no es que los LLMs no sirvan. La lección es que usarlos como detectores exige una evaluación más seria que probar algunos ejemplos y confiar en la explicación generada.

## Tensión 6. La síntesis de vulnerabilidades puede ayudar, pero no reemplaza la realidad

RVG busca generar ejemplos realistas para CWEs poco representadas. Al aumentar TitanVul con datos sintéticos, el desempeño mejora. En la parte real de BenchVul, la exactitud sube de 0.881 a 0.932. En la parte sintética, sube de 0.785 a 0.888. El efecto es especialmente fuerte en CWE-798, donde la exactitud aumenta de 0.587 a 0.863 (Li et al., 2026).

Esto muestra que la generación sintética puede ser útil cuando hay escasez de datos. También muestra un límite. Los datos sintéticos deben validarse, compararse con muestras reales y usarse con cuidado. Si se generan ejemplos demasiado limpios o demasiado parecidos entre sí, el modelo puede aprender un patrón artificial.

::: {.callout-warning title="Nueva dificultad"}
La generación sintética puede cerrar vacíos de cobertura, pero también puede crear una nueva forma de sesgo si los ejemplos no representan fallas reales de desarrollo.
:::

## Implicancias para el curso

Este artículo cambia la forma de leer herramientas basadas en LLMs. No basta con preguntar si detectan vulnerabilidades. Hay que preguntar dónde fueron entrenadas, con qué datos fueron evaluadas, qué clases de CWE cubren, qué tan ruidosas son sus etiquetas y si el resultado se mantiene fuera del conjunto de datos original.

| Pregunta | Por qué importa |
|---|---|
| ¿El modelo fue evaluado fuera de distribución? | Permite estimar si generaliza a datos nuevos. |
| ¿El conjunto de datos tiene duplicados o etiquetas ruidosas? | Puede inflar métricas y esconder fallas reales. |
| ¿Hay balance entre CWE frecuentes y raras? | Un promedio global puede ocultar debilidades críticas. |
| ¿Los negativos son correcciones reales o código benigno general? | Cambia la dificultad y el tipo de patrón aprendido. |
| ¿Hubo validación humana? | Ayuda a distinguir datos plausibles de datos correctos. |

: Preguntas mínimas para leer resultados sobre LLMs detectores de vulnerabilidades.

También permite ubicar los LLMs junto a las herramientas del módulo. CodeQL expresa consultas y reglas explícitas sobre patrones de código. Grype detecta vulnerabilidades conocidas en componentes y dependencias. Un LLM puede complementar esas herramientas, pero no debería reemplazar el razonamiento de seguridad, la validación del contexto ni la revisión de evidencia.

## Referencias

Li, Y., Bui, N. T., Zhang, T., Yang, C., Zhou, X., Weyssow, M., Jiang, J., Chen, J., Huang, H., Nguyen, H. H., Ho, C. Y., Tan, J., Li, R., Yin, Y., Ang, H. W., Liauw, F., Ouh, E. L., Shar, L. K., & Lo, D. (2026). *Out of distribution, out of luck: How well can LLMs trained on vulnerability datasets detect Top 25 CWE weaknesses?* arXiv. https://doi.org/10.48550/arXiv.2507.21817
