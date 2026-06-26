# PRD 04 — Presentación final PPT del trabajo Obesity Dataset

## 1. Nombre del producto

**PPT final — Extracción de conocimiento sobre niveles de obesidad usando CRISP-DM, clustering, clasificación, asociación e iteraciones de mejora**

---

## 2. Propósito del PRD

Este PRD define los requisitos para construir la **presentación final** del trabajo sobre el dataset:

```text
data\ObesityDataSet_raw_and_data_sinthetic.csv
```

La presentación debe comunicar de forma clara, visual y defendible el análisis realizado en la última versión del proyecto. Debe explicar las decisiones metodológicas, las iteraciones realizadas, los resultados principales, los hallazgos relevantes y las conclusiones.

La PPT debe seguir principios de **data storytelling**: no solo mostrar resultados, sino conducir a la audiencia desde el problema hasta la recomendación final.

---

## 3. Contexto académico

El trabajo corresponde a la tarea de análisis de datos del Magíster en Data Science. La evaluación exige entregar:

- PPT de la tarea para la casa.
- Nueva PPT final.
- Código.
- Análisis bajo metodología CRISP-DM.
- Agrupamiento.
- Clasificación.
- Asociación con FP-Growth.
- Tres experimentos adicionales:
  - Dos reducciones de dimensionalidad.
  - Una iteración de ingeniería de características.
- Ajustes metodológicos con mejoras propuestas.
- Discusión de descubrimientos o métricas destacadas.
- Comparación con bibliografía.
- Opcionalmente, aplicación Backoffice.

---

## 4. Objetivo general de la presentación

Construir una presentación final que permita exponer, justificar y defender el trabajo realizado, mostrando cómo el equipo aplicó CRISP-DM, comparó modelos, evaluó iteraciones de mejora y extrajo conocimiento útil desde el dataset de obesidad.

---

## 5. Objetivos específicos

La presentación debe permitir que el evaluador comprenda:

1. Qué problema se abordó.
2. Qué datos se usaron.
3. Cómo se aplicó CRISP-DM.
4. Qué transformaciones se realizaron.
5. Por qué se eligieron ciertos modelos y no otros.
6. Cómo se justificó el clustering.
7. Qué algoritmo de clasificación tuvo mejor desempeño.
8. Qué reglas de asociación fueron relevantes.
9. Qué cambios aportaron las nuevas iteraciones.
10. Qué hallazgos fueron más importantes.
11. Qué limitaciones tiene el trabajo.
12. Qué mejoras futuras se proponen.

---

## 6. Audiencia objetivo

La presentación está dirigida principalmente a:

- Docente evaluador.
- Compañeros del curso.
- Audiencia académica con conocimiento básico o intermedio de ciencia de datos.
- Personas que necesitan entender los resultados sin revisar todo el código.

La presentación debe evitar explicaciones excesivamente técnicas cuando no sean necesarias, pero debe ser suficientemente rigurosa para defender las decisiones tomadas.

---

## 7. Principio narrativo central

La presentación debe contar la siguiente historia:

> El equipo analizó un dataset de hábitos alimentarios, condición física y niveles de obesidad. Usando CRISP-DM, transformó los datos, comparó métodos de clustering, clasificación y asociación, y luego ejecutó nuevas iteraciones para mejorar la robustez del análisis. El resultado final permitió identificar perfiles de riesgo, evaluar modelos predictivos y extraer reglas interpretables apoyadas por métricas.

---

## 8. Mensaje principal esperado

La PPT debe comunicar que:

> La combinación de CRISP-DM, comparación de modelos, reglas de asociación e iteraciones de mejora permitió construir un análisis más sólido, interpretable y defendible que una ejecución única de modelos.

---

## 9. Reglas de storytelling para la PPT

### 9.1 Una idea principal por diapositiva

Cada diapositiva debe tener una sola idea dominante.

Ejemplo incorrecto:

```text
Clustering, clasificación, FP-Growth, métricas y conclusiones
```

Ejemplo correcto:

```text
El mejor clustering no se elige solo por métrica, sino también por interpretabilidad
```

---

### 9.2 Títulos con conclusión

Los títulos deben funcionar como mensajes, no como etiquetas.

Ejemplo básico:

```text
Resultados de clasificación
```

Ejemplo recomendado:

```text
Random Forest obtuvo el mejor equilibrio entre desempeño e interpretabilidad
```

---

### 9.3 Reducir ruido visual

La presentación debe evitar:

- Tablas muy grandes.
- Código dentro de las diapositivas.
- Gráficos sin interpretación.
- Texto excesivo.
- Capturas completas del notebook.
- Colores decorativos sin función.
- Elementos que no aportan al mensaje.

---

### 9.4 Dirigir la atención

Cada gráfico debe destacar visualmente el punto relevante mediante:

- Título interpretativo.
- Anotación breve.
- Etiqueta directa.
- Uso controlado de color.
- Eliminación de elementos innecesarios.

---

### 9.5 Mostrar el “antes y después”

Las iteraciones deben presentarse como una progresión:

1. Modelo base.
2. Revisión crítica.
3. Mejora aplicada.
4. Resultado comparativo.
5. Conclusión de la iteración.

---

### 9.6 Cerrar cada bloque con una decisión

Cada sección debe terminar con una decisión explícita:

- Qué modelo se mantiene.
- Qué transformación aportó valor.
- Qué regla se considera útil.
- Qué hallazgo se prioriza.
- Qué limitación debe mencionarse.

---

## 10. Requisitos de diseño visual

### 10.1 Estilo general

La presentación debe tener un diseño:

- Académico.
- Limpio.
- Moderno.
- Profesional.
- Visualmente sobrio.
- Orientado a datos.

Debe evitar un estilo recargado o con exceso de adornos.

---

### 10.2 Paleta de colores sugerida

Si no existe una plantilla institucional obligatoria, se recomienda usar esta paleta:

| Uso | Color | Hex |
|---|---|---|
| Fondo principal | Azul petróleo muy oscuro | `#0F172A` |
| Fondo secundario | Gris azulado claro | `#F8FAFC` |
| Texto principal oscuro | Gris carbón | `#111827` |
| Texto sobre fondo oscuro | Blanco suave | `#F9FAFB` |
| Color principal | Azul académico | `#2563EB` |
| Color secundario | Morado analítico | `#7C3AED` |
| Acento positivo | Verde | `#16A34A` |
| Acento de alerta | Naranjo | `#F97316` |
| Acento crítico | Rojo | `#DC2626` |
| Líneas y bordes | Gris claro | `#CBD5E1` |

### Regla de uso

- Azul: información principal y métricas centrales.
- Morado: iteraciones, experimentos y comparación metodológica.
- Verde: mejoras o resultados positivos.
- Naranjo: advertencias o limitaciones.
- Rojo: riesgos, errores o resultados inferiores.
- Gris: contexto, etiquetas y elementos secundarios.

---

### 10.3 Tipografía

Se recomienda usar una tipografía estándar disponible en PowerPoint:

| Elemento | Tamaño sugerido |
|---|---:|
| Título de portada | 40–48 pt |
| Título de diapositiva | 28–34 pt |
| Subtítulo | 20–24 pt |
| Texto breve | 18–22 pt |
| Etiquetas de gráficos | 14–18 pt |
| Notas o referencias | 10–12 pt |

No se deben usar cuerpos de texto menores a 14 pt, salvo referencias bibliográficas.

---

### 10.4 Gráficos

Los gráficos deben cumplir:

- Título interpretativo.
- Ejes legibles.
- Leyenda solo si es necesaria.
- Uso limitado de colores.
- Sin exceso de líneas de cuadrícula.
- Sin tablas crudas extensas.
- Con anotación de la conclusión principal.

Gráficos recomendados:

- Distribución de clases.
- Matriz de confusión del mejor modelo.
- Comparación de métricas de clasificación.
- Silhouette score por algoritmo.
- Distribución de clusters.
- Importancia de variables.
- Comparación modelo base vs iteraciones.
- Reglas de asociación ordenadas por Lift.

---

## 11. Requisitos de contenido

### 11.1 La PPT debe incluir

- Contexto del problema.
- Descripción del dataset.
- Aplicación de CRISP-DM.
- Procesamiento de datos.
- Clustering y justificación del algoritmo elegido.
- Comparación de métodos de clustering.
- Clasificación y comparación de modelos.
- Métricas de test.
- Validación cruzada estratificada.
- Optimización de hiperparámetros.
- Tratamiento ordinal de variables.
- Ingeniería de características.
- Importancia de atributos creados.
- FP-Growth.
- Reglas con mejor Lift.
- 6 reglas novedosas.
- 3 descubrimientos o métricas destacadas.
- Comparación con bibliografía.
- Limitaciones.
- Mejoras futuras.
- Conclusión final.

---

### 11.2 La PPT no debe incluir

- Código completo.
- Capturas largas del notebook.
- Tablas ilegibles.
- Resultados sin interpretación.
- Métricas sin explicar.
- Afirmaciones clínicas no respaldadas.
- Repetición innecesaria de gráficos.

---

## 12. Requisitos funcionales de la PPT

### RF-PPT-01: Portada

Debe incluir:

- Título del trabajo.
- Nombre del estudiante o equipo.
- Asignatura.
- Docente.
- Fecha.
- Dataset utilizado.

La portada no cuenta dentro de las 17 diapositivas explicativas.

---

### RF-PPT-02: Presentar el problema

La presentación debe explicar brevemente:

- Qué se quiere analizar.
- Por qué el dataset es relevante.
- Qué métodos se aplicaron.
- Qué se espera descubrir.

---

### RF-PPT-03: Describir el dataset

Debe incluir:

- Número de registros.
- Número de variables.
- Variable objetivo.
- Tipo de problema.
- Ejemplos de variables relevantes.

---

### RF-PPT-04: Explicar CRISP-DM

Debe explicar qué etapas de CRISP-DM se usaron y por qué fueron útiles.

Debe redactarse en tercera persona.

Ejemplo:

```text
El equipo utilizó CRISP-DM porque permitió ordenar el análisis desde la comprensión del problema hasta la evaluación de modelos y la comunicación de resultados.
```

---

### RF-PPT-05: Mostrar preparación de datos

Debe incluir las principales transformaciones:

- Codificación de variables categóricas.
- Escalamiento de variables numéricas.
- Tratamiento ordinal de `CAEC` y `CALC`.
- Separación train/test.
- Preparación para FP-Growth.
- Creación de variables nuevas.

---

### RF-PPT-06: Justificar clustering

Debe responder explícitamente:

1. ¿Por qué no se asumió directamente que K-Means era el mejor?
2. ¿Los datos parecían tener forma globular?
3. ¿Qué limitaciones tiene K-Means?
4. ¿Qué otros algoritmos se compararon?
5. ¿Qué criterio definió el algoritmo final?

Algoritmos mínimos a comparar:

- K-Means.
- Gaussian Mixture Model.
- Agglomerative Clustering.

Algoritmo opcional:

- DBSCAN, si los resultados permiten interpretarlo.

---

### RF-PPT-07: Mostrar resultados de clustering

Debe incluir:

- Tabla comparativa de algoritmos.
- Métrica de Silhouette.
- Tamaño de clusters.
- Interpretabilidad.
- Perfil de cada cluster.
- Decisión final del modelo de clustering.

---

### RF-PPT-08: Explicar clasificación

Debe incluir:

- Modelos evaluados.
- Métricas usadas.
- Justificación de modelos.
- Mejor modelo.
- Métricas de test.

Modelos mínimos recomendados:

- Regresión logística multinomial.
- Árbol de decisión.
- Random Forest.
- SVM o KNN si se implementa.

---

### RF-PPT-09: Mostrar validación cruzada

Debe explicar:

- Por qué se usó validación cruzada estratificada.
- Qué aporta frente a una única partición train/test.
- Resultado promedio.
- Variabilidad del modelo.

---

### RF-PPT-10: Mostrar optimización de hiperparámetros

Debe explicar:

- Qué modelo se optimizó.
- Qué técnica se usó: `GridSearchCV` o `RandomizedSearchCV`.
- Qué hiperparámetros se buscaron.
- Si la optimización mejoró o no las métricas.

---

### RF-PPT-11: Mostrar tratamiento ordinal

Debe explicar:

- Qué variables fueron tratadas como ordinales.
- Por qué `CAEC` y `CALC` no deben ser tratadas solo como nominales si tienen orden natural.
- Cómo cambió el resultado tras esta decisión.

---

### RF-PPT-12: Mostrar ingeniería de características

Debe presentar los atributos creados.

Variables mínimas:

1. `BMI`
2. `BMI_Category`
3. `Healthy_Habits_Score`
4. `Risky_Eating_Score`
5. `FAF_FAVC_Interaction`

Debe incluir un gráfico de importancia de atributos creados si el modelo lo permite.

---

### RF-PPT-13: Mostrar comparación de iteraciones

Debe incluir una tabla o gráfico comparativo:

| Iteración | Cambio aplicado | Métrica principal | Resultado | Decisión |
|---|---|---:|---|---|
| Base | Preprocesamiento estándar | F1 macro | | |
| Iteración 1 | PCA | F1 macro / Silhouette | | |
| Iteración 2 | TruncatedSVD | F1 macro / Silhouette | | |
| Iteración 3 | Feature Engineering | F1 macro | | |
| Iteración 4 | Ordinal + CV + tuning | F1 macro CV | | |

---

### RF-PPT-14: Presentar FP-Growth

Debe explicar:

- Cómo se transformaron los datos a formato transaccional.
- Qué variables se discretizaron.
- Qué umbrales de soporte se usaron.
- Cómo se generaron las reglas.

---

### RF-PPT-15: Mostrar reglas de asociación

Debe incluir:

- Reglas con mejores indicadores.
- 6 reglas novedosas.
- Support.
- Confidence.
- Lift.
- Interpretación simple.

---

### RF-PPT-16: Presentar descubrimientos

Debe resumir al menos 3 descubrimientos o métricas destacadas.

Cada descubrimiento debe incluir:

- Hallazgo.
- Evidencia métrica.
- Interpretación.
- Utilidad.
- Relación con bibliografía si corresponde.

---

### RF-PPT-17: Comparar con bibliografía

Debe incluir al menos una comparación con bibliografía.

Referencia base recomendada:

```text
Mendoza Palechor, F., & De la Hoz Manotas, A. (2019). Dataset for estimation of obesity levels based on eating habits and physical condition in individuals from Colombia, Peru and Mexico. Data in Brief.
```

También puede incorporarse bibliografía sobre:

- IMC.
- Actividad física.
- Hábitos alimentarios.
- Sedentarismo.
- Clasificación de obesidad.

---

### RF-PPT-18: Presentar limitaciones y mejoras futuras

Debe incluir:

- Limitaciones del dataset.
- Riesgo de sobreajuste.
- Posible dependencia de variables antropométricas.
- Interpretabilidad limitada de algunas transformaciones.
- Mejoras futuras sugeridas.

---

### RF-PPT-19: Cierre

Debe cerrar con una conclusión clara:

```text
El análisis mostró que las mejores decisiones no dependieron de aplicar más modelos, sino de comparar alternativas, justificar supuestos y evaluar cada iteración con métricas consistentes.
```

---

## 13. Estructura recomendada de la presentación

La presentación puede superar las 17 diapositivas explicativas. La portada no cuenta.

| Nº | Diapositiva | Objetivo narrativo |
|---:|---|---|
| 0 | Portada | Identificar trabajo, curso, docente y dataset |
| 1 | Pregunta guía del análisis | Presentar el problema |
| 2 | Dataset y variable objetivo | Mostrar qué datos se analizaron |
| 3 | Metodología CRISP-DM | Explicar cómo se ordenó el trabajo |
| 4 | Preparación de datos | Mostrar decisiones de limpieza y transformación |
| 5 | Distribución de la variable objetivo | Evidenciar el problema multiclase |
| 6 | Estrategia general de modelamiento | Mostrar el mapa de clustering, clasificación y asociación |
| 7 | Clustering: por qué comparar algoritmos | Justificar que K-Means no se asumió como único modelo |
| 8 | Clustering: comparación de algoritmos | Presentar Silhouette, tamaños e interpretabilidad |
| 9 | Clustering: perfiles encontrados | Explicar clusters finales |
| 10 | Clasificación: modelos evaluados | Presentar candidatos y justificación |
| 11 | Clasificación: resultados de test | Mostrar comparación de métricas |
| 12 | Validación cruzada estratificada | Mostrar robustez del modelo |
| 13 | Optimización de hiperparámetros | Mostrar si el tuning mejoró el desempeño |
| 14 | Tratamiento ordinal | Explicar impacto de codificar `CAEC` y `CALC` como ordinales |
| 15 | Ingeniería de características | Presentar atributos creados |
| 16 | Importancia de atributos creados | Mostrar gráfico de importancia |
| 17 | Reducción de dimensionalidad: PCA | Mostrar efecto en resultados |
| 18 | Reducción de dimensionalidad: TruncatedSVD | Mostrar efecto en resultados |
| 19 | Comparación general de iteraciones | Mostrar base vs mejoras |
| 20 | FP-Growth: preparación y reglas | Explicar asociación |
| 21 | Seis reglas novedosas | Presentar reglas relevantes |
| 22 | Tres descubrimientos principales | Sintetizar hallazgos |
| 23 | Comparación con bibliografía | Respaldar interpretación |
| 24 | Limitaciones y mejoras futuras | Mostrar evaluación crítica |
| 25 | Conclusión final | Cerrar la historia |

---

## 14. Orden narrativo recomendado

La presentación debe seguir este flujo:

```text
Problema → Datos → Método → Modelos base → Dudas metodológicas → Comparación → Iteraciones → Hallazgos → Decisión final → Limitaciones
```

Este orden permite mostrar que el equipo no ejecutó modelos de forma mecánica, sino que evaluó supuestos y mejoró progresivamente el análisis.

---

## 15. Criterios de aceptación

La PPT estará completa si cumple:

- Tiene portada.
- Usa 17 o más diapositivas explicativas si es necesario.
- Presenta CRISP-DM de forma explícita.
- Explica qué elementos de CRISP-DM fueron útiles.
- Presenta el dataset y la variable objetivo.
- Resume preparación de datos.
- Justifica el clustering.
- Compara más de un algoritmo de clustering.
- Explica si K-Means era o no adecuado.
- Presenta perfiles de clusters.
- Compara modelos de clasificación.
- Presenta métricas de test.
- Presenta validación cruzada estratificada.
- Presenta optimización de hiperparámetros.
- Presenta tratamiento ordinal.
- Presenta ingeniería de características.
- Muestra importancia de atributos creados.
- Presenta FP-Growth.
- Reporta Lift.
- Explica 6 reglas novedosas.
- Resume al menos 3 descubrimientos.
- Compara al menos un hallazgo con bibliografía.
- Presenta limitaciones.
- Presenta mejoras futuras.
- Usa títulos interpretativos.
- Usa gráficos claros.
- Evita outputs truncados o capturas ilegibles.

---

## 16. Requisitos para outputs del notebook que alimentan la PPT

Para evitar mensajes como:

```text
Output is truncated. View as a scrollable element or open in a text editor.
```

El notebook debe configurar visualización completa o exportar tablas relevantes.

### Configuración recomendada

```python
import pandas as pd

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 0)
pd.set_option("display.max_colwidth", None)
```

### Reglas de uso

- Para exploración completa, se puede usar `display(df)`.
- Para PPT, se deben usar tablas resumidas.
- Si una tabla es muy extensa, debe exportarse a CSV o Excel.
- La PPT debe mostrar solo las filas relevantes.
- Las reglas FP-Growth deben filtrarse antes de presentarse.

---

## 17. Tablas mínimas que deben generarse para la PPT

### 17.1 Tabla de modelos de clasificación

| Modelo | Accuracy test | Precision macro | Recall macro | F1 macro | Decisión |
|---|---:|---:|---:|---:|---|
| Regresión logística | | | | | |
| Árbol de decisión | | | | | |
| Random Forest | | | | | |
| SVM/KNN | | | | | |

---

### 17.2 Tabla de clustering

| Algoritmo | Supuesto principal | Silhouette | Tamaño de clusters | Interpretabilidad | Decisión |
|---|---|---:|---|---|---|
| K-Means | Clusters aproximadamente globulares | | | | |
| Gaussian Mixture | Clusters elípticos/probabilísticos | | | | |
| Agglomerative | Estructura jerárquica | | | | |
| DBSCAN | Densidad y ruido | | | | |

---

### 17.3 Tabla de iteraciones

| Iteración | Mejora aplicada | Resultado esperado | Métrica usada | Conclusión |
|---|---|---|---|---|
| Base | Preprocesamiento inicial | Punto de comparación | F1 macro / Silhouette | |
| PCA | Reducción dimensional | Simplificar espacio | F1 macro / Silhouette | |
| TruncatedSVD | Reducción en matriz codificada | Evaluar espacio one-hot | F1 macro / Silhouette | |
| Feature Engineering | Nuevas variables | Mejorar señal predictiva | F1 macro | |
| Ordinal + CV + tuning | Robustez metodológica | Mejor estimación | F1 macro CV | |

---

### 17.4 Tabla de reglas de asociación

| Regla | Antecedente | Consecuente | Support | Confidence | Lift | Interpretación |
|---|---|---|---:|---:|---:|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |

---

## 18. Gráficos mínimos recomendados

La PPT debe incluir al menos:

1. Distribución de `NObeyesdad`.
2. Comparación de métricas de clasificación.
3. Matriz de confusión del mejor modelo.
4. Silhouette score por algoritmo de clustering.
5. Distribución de clusters.
6. Importancia de atributos creados.
7. Comparación de iteraciones.
8. Reglas de asociación por Lift.

---

## 19. Plantilla de redacción para la exposición

La redacción debe mantenerse en tercera persona.

### Ejemplo para clustering

```text
El equipo no asumió que K-Means fuera automáticamente el mejor algoritmo, porque este método funciona mejor cuando los grupos tienen forma aproximadamente globular y tamaños relativamente similares. Por esta razón, se comparó con métodos alternativos como Gaussian Mixture y Agglomerative Clustering. La elección final se basó en la combinación de Silhouette, distribución de grupos e interpretabilidad.
```

### Ejemplo para clasificación

```text
El equipo comparó varios algoritmos de clasificación porque el problema corresponde a una clasificación multiclase. La selección del mejor modelo no se basó solo en accuracy, sino también en F1 macro, ya que esta métrica permite evaluar mejor el desempeño promedio entre clases.
```

### Ejemplo para ingeniería de características

```text
El equipo incorporó variables derivadas como IMC, categoría de IMC y puntajes de hábitos para evaluar si una representación más informativa de los datos podía mejorar el desempeño del clasificador. La importancia de variables permitió revisar si estas nuevas características aportaron señal útil al modelo.
```

---

## 20. Definition of Done

La PPT final estará lista cuando:

- Tenga una historia clara.
- Use diseño consistente.
- Explique decisiones y no solo resultados.
- Justifique clustering.
- Muestre iteraciones.
- Presente métricas relevantes.
- Incluya reglas de asociación interpretadas.
- Muestre importancia de atributos creados.
- Presente 3 descubrimientos.
- Incluya bibliografía.
- Sea defendible oralmente ante el docente.
