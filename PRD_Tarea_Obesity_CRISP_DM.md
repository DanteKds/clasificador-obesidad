# PRD — Tarea de Análisis de Datos con Obesity Dataset

## 1. Nombre del proyecto

**Análisis de niveles de obesidad mediante métodos de ciencia de datos usando CRISP-DM**

## 2. Contexto académico

Este proyecto corresponde a la tarea **“Análisis de datos usando métodos de ciencia de datos”** del Taller de Aplicaciones del Magíster en Data Science, Facultad de Ingeniería. El trabajo debe utilizar datos del **UCI Machine Learning Repository** y aplicar métodos de extracción de conocimiento: agrupamiento, clasificación y asociación.

El dataset seleccionado es **Estimation of Obesity Levels Based On Eating Habits and Physical Condition**, que contiene registros de personas de México, Perú y Colombia, con variables asociadas a hábitos alimentarios, condición física y nivel de obesidad.

El proyecto debe trabajarse bajo el enfoque **CRISP-DM** y finalizar en una presentación PowerPoint de máximo 15 diapositivas.

## 3. Dataset seleccionado

- **Nombre:** Estimation of Obesity Levels Based On Eating Habits and Physical Condition
- **Fuente:** UCI Machine Learning Repository
- **Path local:** `data\ObesityDataSet_raw_and_data_sinthetic.csv`
- **Registros esperados:** 2.111
- **Atributos esperados:** 17
- **Problema principal:** clasificación multiclase del nivel de obesidad
- **Variable objetivo esperada:** `NObesity` o `NObeyesdad`, según el nombre real de la columna en el archivo CSV

### Variables esperadas

El dataset incluye variables asociadas a:

- Sexo
- Edad
- Talla
- Peso
- Antecedentes familiares de sobrepeso
- Consumo frecuente de comida hipercalórica
- Consumo de verduras
- Número de comidas principales
- Consumo de alimentos entre comidas
- Tabaquismo
- Consumo de agua
- Monitoreo de calorías
- Actividad física
- Tiempo frente a pantallas o tecnología
- Consumo de alcohol
- Medio de transporte utilizado
- Nivel de obesidad

## 4. Problema a resolver

Se necesita analizar el dataset de obesidad para extraer conocimiento útil mediante tres enfoques de ciencia de datos:

1. **Agrupamiento:** identificar perfiles de personas con características similares.
2. **Clasificación:** predecir el nivel de obesidad y comparar algoritmos según su rendimiento en datos de testeo.
3. **Asociación:** descubrir reglas frecuentes entre hábitos, características y niveles de obesidad mediante FP-Growth, interpretando reglas relevantes y novedosas, incluyendo el indicador Lift.

El resultado final debe ser claro, reproducible y resumido en una presentación de máximo 15 diapositivas.

## 5. Objetivo general

Desarrollar un análisis completo del dataset de obesidad aplicando CRISP-DM, algoritmos de agrupamiento, clasificación y asociación, con interpretación de resultados y generación de una presentación final para exposición académica.

## 6. Objetivos específicos

- Cargar y validar el dataset desde el path local definido.
- Comprender la estructura de los datos y sus variables principales.
- Preparar los datos para análisis, clustering, clasificación y asociación.
- Aplicar un algoritmo de agrupamiento y justificar el número de clusters.
- Interpretar los perfiles identificados en cada cluster.
- Aplicar varios algoritmos de clasificación multiclase.
- Comparar los modelos de clasificación usando métricas en datos de testeo.
- Identificar posibles mejoras futuras al proceso o a los datos.
- Aplicar FP-Growth para descubrir reglas de asociación.
- Seleccionar reglas con buenos indicadores y 6 reglas novedosas.
- Medir e interpretar Lift en las reglas de asociación.
- Organizar los resultados según CRISP-DM.
- Preparar una PPT de máximo 15 diapositivas.

## 7. Alcance

### Incluye

- Carga de datos desde CSV.
- Revisión de estructura, tipos de datos, nulos y duplicados.
- Análisis exploratorio inicial.
- Preprocesamiento de variables categóricas y numéricas.
- Escalamiento de variables numéricas para clustering.
- Codificación de variables categóricas.
- Aplicación de clustering.
- Evaluación de número de clusters.
- Interpretación de clusters.
- Entrenamiento de modelos de clasificación.
- Evaluación con datos de testeo.
- Aplicación de FP-Growth.
- Interpretación de reglas de asociación.
- Generación de insumos para presentación.

### No incluye

- Desarrollo de una aplicación web.
- API o despliegue productivo.
- Deep learning.
- Modelos no interpretables sin justificación.
- Automatización fuera del notebook.
- Inferencia causal.
- Uso clínico real de predicciones.

## 8. Metodología CRISP-DM

### 8.1 Comprensión del negocio / problema

Definir el problema como una tarea académica de extracción de conocimiento sobre perfiles de obesidad usando hábitos alimentarios y condición física.

Preguntas guía:

- ¿Qué patrones existen entre hábitos y niveles de obesidad?
- ¿Es posible agrupar perfiles de riesgo?
- ¿Qué algoritmo predice mejor el nivel de obesidad?
- ¿Qué reglas de asociación permiten describir relaciones relevantes o novedosas?

### 8.2 Comprensión de los datos

Actividades requeridas:

- Cargar el CSV.
- Revisar dimensiones.
- Revisar nombres de columnas.
- Revisar tipos de variables.
- Revisar valores nulos.
- Revisar duplicados.
- Revisar distribución de la variable objetivo.
- Identificar variables numéricas y categóricas.

### 8.3 Preparación de los datos

Actividades requeridas:

- Estandarizar nombres de columnas si es necesario.
- Identificar la variable objetivo real: `NObesity` o `NObeyesdad`.
- Separar variables predictoras y variable objetivo.
- Codificar variables categóricas.
- Escalar variables numéricas cuando corresponda.
- Crear una versión de datos para clustering.
- Crear una versión de datos para clasificación.
- Crear una versión binarizada o discretizada para FP-Growth.

### 8.4 Modelamiento

Debe incluir tres líneas de modelamiento:

1. **Clustering**
   - Algoritmo sugerido base: K-Means.
   - Alternativas: Agglomerative Clustering o DBSCAN si se justifica.
   - Evaluación sugerida: método del codo, silhouette score e interpretación de perfiles.

2. **Clasificación**
   - Algoritmos sugeridos:
     - Regresión logística multinomial.
     - Árbol de decisión.
     - Random Forest.
     - K-Nearest Neighbors.
     - Support Vector Machine, si el tiempo lo permite.
   - Evaluación:
     - Accuracy.
     - Precision macro.
     - Recall macro.
     - F1 macro.
     - Matriz de confusión.

3. **Asociación**
   - Algoritmo requerido: FP-Growth.
   - Métricas mínimas:
     - Support.
     - Confidence.
     - Lift.
   - Resultado requerido:
     - Reglas con mejores indicadores.
     - 6 reglas novedosas interpretadas.

### 8.5 Evaluación

Evaluar si los resultados responden a la tarea:

- ¿El clustering fue justificado?
- ¿Los clusters fueron interpretados?
- ¿Se compararon clasificadores en test?
- ¿Se indicó el mejor algoritmo?
- ¿Se propusieron mejoras futuras?
- ¿Se aplicó FP-Growth?
- ¿Se reportó Lift?
- ¿Se explicaron reglas relevantes y novedosas?

### 8.6 Presentación / despliegue académico

El resultado se debe sintetizar en una PPT de máximo 15 páginas para subir a Blackboard y presentar en clase.

## 9. Requisitos funcionales

### RF-01: Cargar dataset

El sistema debe cargar el archivo:

```python
ruta = "data\\ObesityDataSet_raw_and_data_sinthetic.csv"
```

Debe validar que el archivo exista y que el dataframe se cargue correctamente.

### RF-02: Inspeccionar datos

El sistema debe mostrar:

- Primeras filas.
- Dimensiones.
- Tipos de datos.
- Nulos.
- Duplicados.
- Distribución de la variable objetivo.

### RF-03: Preparar datos para clustering

El sistema debe:

- Excluir la variable objetivo del clustering principal.
- Codificar variables categóricas.
- Escalar variables numéricas.
- Generar matriz procesada.

### RF-04: Aplicar clustering

El sistema debe:

- Probar diferentes valores de `k`.
- Calcular silhouette score.
- Apoyar la decisión con método del codo.
- Seleccionar un número de clusters.
- Agregar la etiqueta de cluster al dataframe.

### RF-05: Interpretar clusters

El sistema debe entregar una tabla descriptiva por cluster con:

- Edad promedio.
- Peso promedio.
- Altura promedio.
- Nivel de obesidad predominante.
- Hábitos predominantes.
- Perfil interpretativo del grupo.

### RF-06: Preparar datos para clasificación

El sistema debe:

- Separar `X` e `y`.
- Codificar la variable objetivo.
- Dividir train/test respetando estratificación por clase.
- Aplicar preprocesamiento dentro de pipeline para evitar fuga de datos.

### RF-07: Entrenar clasificadores

El sistema debe entrenar y comparar al menos tres modelos:

- Regresión logística multinomial.
- Árbol de decisión.
- Random Forest.

Opcionales:

- KNN.
- SVM.
- Gradient Boosting.

### RF-08: Evaluar clasificación

El sistema debe calcular:

- Accuracy.
- Precision macro.
- Recall macro.
- F1 macro.
- Matriz de confusión.
- Classification report.

Debe indicar cuál algoritmo tiene mejores predicciones en test.

### RF-09: Proponer mejoras futuras

El sistema debe generar una sección con mejoras posibles:

- Optimización de hiperparámetros.
- Balanceo de clases si corresponde.
- Validación cruzada.
- Ingeniería de variables.
- Revisión de variables ordinales.
- Reducción de dimensionalidad.
- Evaluación con datos externos.

### RF-10: Preparar datos para FP-Growth

El sistema debe convertir los datos a formato transaccional:

- Variables categóricas como ítems.
- Variables numéricas discretizadas en rangos interpretables.
- Variable objetivo incluida como ítem para descubrir asociaciones con niveles de obesidad.

Ejemplos de ítems:

- `Gender=Female`
- `Age=Young`
- `Weight=High`
- `FAVC=yes`
- `FAF=Low`
- `NObesity=Obesity_Type_I`

### RF-11: Aplicar FP-Growth

El sistema debe:

- Generar itemsets frecuentes.
- Crear reglas de asociación.
- Filtrar reglas por soporte, confianza y Lift.
- Ordenar reglas por Lift y confianza.

### RF-12: Interpretar reglas de asociación

El sistema debe seleccionar:

- Reglas con mejores indicadores.
- 6 reglas novedosas.

Para cada regla debe explicar:

- Antecedente.
- Consecuente.
- Support.
- Confidence.
- Lift.
- Interpretación en lenguaje simple.
- Por qué la regla es útil o novedosa.

### RF-13: Generar insumos para PPT

El sistema debe producir:

- Tabla resumen del dataset.
- Gráficos exploratorios.
- Resultado de clustering.
- Comparación de clasificadores.
- Reglas de asociación seleccionadas.
- Conclusiones finales.

## 10. Requisitos no funcionales

- El notebook debe ser claro y reproducible.
- El código debe estar dividido por secciones.
- Se deben usar comentarios breves y útiles.
- Las tablas deben ser interpretables.
- Los gráficos deben tener títulos y etiquetas.
- El análisis debe priorizar explicación académica sobre complejidad técnica.
- El flujo debe ser compatible con ejecución local o en notebook.
- El path del dataset debe mantenerse como `data\ObesityDataSet_raw_and_data_sinthetic.csv`.

## 11. Métricas de evaluación del proyecto

### Clustering

- Silhouette score.
- Inertia / método del codo.
- Interpretabilidad de clusters.
- Distribución de niveles de obesidad por cluster.

### Clasificación

- Accuracy.
- Precision macro.
- Recall macro.
- F1 macro.
- Matriz de confusión.

### Asociación

- Support.
- Confidence.
- Lift.
- Novedad interpretativa de las reglas.

## 12. Criterios de aceptación

El proyecto será considerado completo si cumple con:

- Se usa el dataset seleccionado.
- Se indica claramente el path local del dataset.
- Se aplica CRISP-DM.
- Se realiza análisis exploratorio.
- Se aplica clustering.
- Se justifica el tipo de clustering.
- Se justifica el número de clusters.
- Se interpretan los clusters.
- Se aplican algoritmos de clasificación.
- Se determina el mejor algoritmo con datos de testeo.
- Se proponen mejoras futuras.
- Se aplica FP-Growth.
- Se reporta Lift.
- Se explican reglas con mejores indicadores.
- Se explican 6 reglas novedosas.
- Se prepara contenido compatible con PPT de máximo 15 páginas.

## 13. Estructura recomendada del notebook

```text
01_importacion_librerias
02_carga_datos
03_comprension_datos_crisp_dm
04_limpieza_y_preparacion
05_analisis_exploratorio
06_preprocesamiento_clustering
07_modelo_clustering
08_interpretacion_clusters
09_preprocesamiento_clasificacion
10_modelos_clasificacion
11_evaluacion_clasificacion
12_preparacion_fp_growth
13_reglas_asociacion
14_conclusiones
15_insumos_presentacion
```

## 14. Estructura recomendada de la PPT, máximo 15 diapositivas

1. Título, integrantes, asignatura y dataset.
2. Contexto del problema y objetivo.
3. Metodología CRISP-DM.
4. Descripción del dataset.
5. Preparación y procesamiento de datos.
6. Análisis exploratorio principal.
7. Clustering: método y justificación.
8. Clustering: interpretación de grupos.
9. Clasificación: modelos comparados.
10. Clasificación: resultados en test.
11. Mejor modelo y mejoras futuras.
12. FP-Growth: preparación de datos.
13. Reglas de asociación con mejores indicadores.
14. Seis reglas novedosas e interpretación.
15. Conclusiones finales.

## 15. Riesgos y mitigaciones

| Riesgo | Impacto | Mitigación |
|---|---:|---|
| Nombre real de la variable objetivo distinto a `NObesity` | Medio | Detectar si existe `NObesity` o `NObeyesdad` |
| Variables numéricas son continuas y FP-Growth requiere ítems | Alto | Discretizar en rangos interpretables |
| Clusters difíciles de interpretar | Alto | Resumir variables clave por cluster y cruzar con obesidad |
| Clases desbalanceadas | Medio | Usar métricas macro y estratificación |
| Demasiadas reglas de asociación | Medio | Filtrar por Lift, confianza y soporte mínimo |
| PPT supera 15 diapositivas | Medio | Usar anexos fuera de la presentación si es necesario |

## 16. Decisiones técnicas iniciales

- Usar `pandas` y `numpy` para manejo de datos.
- Usar `matplotlib` y opcionalmente `seaborn` para visualización.
- Usar `scikit-learn` para preprocesamiento, clustering y clasificación.
- Usar `mlxtend` para FP-Growth y reglas de asociación.
- Usar pipelines para clasificación.
- Usar `train_test_split` con estratificación para la variable objetivo.
- Usar `random_state=42` para reproducibilidad.

## 17. Prompt recomendado para el sistema de desarrollo

```md
Actúa como asistente de desarrollo para una tarea académica de Magíster en Data Science. Usa este PRD como fuente principal.

Debes construir un notebook reproducible usando el dataset ubicado en:

data\ObesityDataSet_raw_and_data_sinthetic.csv

El trabajo debe seguir CRISP-DM y aplicar tres métodos: clustering, clasificación y asociación con FP-Growth. Debes justificar el algoritmo de clustering, justificar el número de clusters, interpretar cada grupo, entrenar varios clasificadores, determinar cuál predice mejor en datos de testeo, proponer mejoras futuras, aplicar FP-Growth, medir Lift, explicar reglas con mejores indicadores y seleccionar 6 reglas novedosas.

Prioriza código claro, secciones ordenadas, tablas interpretables y conclusiones útiles para una PPT de máximo 15 diapositivas.
```

## 18. Definition of Done

El trabajo está terminado cuando existe:

- Notebook ejecutable de inicio a fin.
- Análisis CRISP-DM explícito.
- Clustering aplicado e interpretado.
- Modelos de clasificación comparados.
- Mejor clasificador seleccionado con métricas de test.
- FP-Growth aplicado.
- Reglas de asociación interpretadas con Lift.
- 6 reglas novedosas explicadas.
- Resumen listo para transformar en PPT de máximo 15 diapositivas.
