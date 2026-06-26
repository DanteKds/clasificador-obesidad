# PRD — Tarea Obesity Dataset con CRISP-DM, Rúbrica y Experimentos

## 1. Nombre del proyecto

**Extracción de conocimiento sobre niveles de obesidad usando clustering, clasificación, asociación y experimentos de transformación de datos**

---

## 2. Contexto académico

Este proyecto corresponde a la tarea del **Taller de Aplicaciones — Magíster en Data Science**.

La actividad solicita continuar el trabajo para la casa y ajustar el análisis con base en el feedback docente. La evaluación corresponde al **60%** y exige una nueva presentación, código y resultados actualizados.

El trabajo debe usar buenas prácticas para extraer información y conocimiento desde datos, aplicando:

- Metodología **CRISP-DM**.
- Algoritmos de **agrupamiento**.
- Algoritmos de **clasificación**.
- Algoritmos de **asociación** mediante **FP-Growth**.
- Evaluación de métricas relevantes.
- Nuevos experimentos de transformación y/o ingeniería de características.
- Presentación clara de resultados en una nueva PPT.

---

## 3. Dataset seleccionado

- **Dataset:** Estimation of Obesity Levels Based On Eating Habits and Physical Condition.
- **Fuente:** UCI Machine Learning Repository.
- **Archivo local:** `data\ObesityDataSet_raw_and_data_sinthetic.csv`
- **Registros esperados:** 2.111.
- **Atributos esperados:** 17.
- **Variable objetivo esperada:** `NObeyesdad`.
- **Tipo de problema:** clasificación multiclase.
- **Clases esperadas de la variable objetivo:**
  - Insufficient Weight.
  - Normal Weight.
  - Overweight Level I.
  - Overweight Level II.
  - Obesity Type I.
  - Obesity Type II.
  - Obesity Type III.

---

## 4. Problema a resolver

Se necesita desarrollar un análisis reproducible que permita extraer conocimiento útil sobre niveles de obesidad a partir de variables relacionadas con:

- Características demográficas.
- Condición física.
- Hábitos alimentarios.
- Actividad física.
- Conductas sedentarias.
- Uso de transporte.
- Antecedentes familiares de sobrepeso.

El proyecto debe responder:

1. ¿Qué perfiles de personas pueden identificarse mediante agrupamiento?
2. ¿Qué algoritmo de clasificación predice mejor el nivel de obesidad?
3. ¿Qué reglas de asociación explican patrones relevantes entre hábitos, condición física y obesidad?
4. ¿Cómo cambian los resultados al aplicar reducciones de dimensionalidad?
5. ¿Cómo cambian los resultados al incorporar nuevas variables de ingeniería de características?
6. ¿Qué descubrimientos o métricas son más útiles para presentar en la asesoría?

---

## 5. Objetivo general

Aplicar CRISP-DM y métodos de ciencia de datos para analizar el dataset de obesidad, construyendo modelos de agrupamiento, clasificación y asociación, evaluando nuevos experimentos de transformación de datos e identificando descubrimientos relevantes para una presentación académica.

---

## 6. Objetivos específicos

- Cargar y validar el dataset desde el path local.
- Inspeccionar calidad, estructura y distribución de los datos.
- Aplicar CRISP-DM y explicar qué elementos de la metodología fueron útiles.
- Preparar los datos para clustering, clasificación y asociación.
- Aplicar agrupamiento, justificar el algoritmo usado, justificar el número de clusters e interpretar cada grupo.
- Aplicar algoritmos de clasificación y comparar resultados en datos de testeo.
- Determinar el mejor algoritmo de clasificación según métricas adecuadas.
- Aplicar FP-Growth y explicar reglas con mejores indicadores.
- Seleccionar e interpretar 6 reglas novedosas.
- Realizar 3 experimentos adicionales:
  - 2 experimentos con reducción de dimensionalidad.
  - 1 experimento con 5 atributos nuevos de ingeniería de características.
- Evaluar cómo cambian los resultados del modelo de agrupación o clasificación en cada experimento.
- Resumir al menos 3 descubrimientos o métricas destacadas.
- Comparar al menos un descubrimiento o métrica con bibliografía relacionada.
- Preparar una nueva PPT clara, concisa y visualmente ordenada.
- Entregar PPT original, nueva PPT y código en Blackboard.

---

## 7. Entregables

### Entregables obligatorios

1. **PPT tarea para la casa**
   - Presentación previa solicitada por el docente.

2. **Nueva PPT**
   - Debe incorporar ajustes, nuevos experimentos, resultados y conclusiones.

3. **Código**
   - Notebook o script reproducible.
   - Recomendado: `notebooks/obesity_analysis_crisp_dm.ipynb`.

### Entregable opcional

4. **Aplicación Backoffice**
   - Permite usar el clasificador.
   - Voluntario.
   - Puede sumar 1 punto si falta nota.
   - Recomendado: app simple en Streamlit.

---

## 8. Fecha de entrega

**Viernes 12 de junio en Blackboard.**

---

## 9. Alcance del proyecto

### Incluye

- Análisis exploratorio.
- Limpieza y transformación de datos.
- Aplicación explícita de CRISP-DM.
- Agrupamiento.
- Clasificación.
- Asociación con FP-Growth.
- Medición de Lift.
- Interpretación de reglas.
- Experimentos con reducción de dimensionalidad.
- Ingeniería de características con 5 nuevos atributos.
- Comparación de resultados.
- Discusión de hallazgos.
- Nueva presentación académica.
- Código reproducible.

### No incluye

- Despliegue productivo obligatorio.
- Aplicación web obligatoria.
- Deep learning.
- Uso clínico real del clasificador.
- Inferencia causal.
- Automatización avanzada.

---

## 10. Metodología CRISP-DM

El proyecto debe usar CRISP-DM como estructura principal.

### 10.1 Business Understanding / Comprensión del negocio

En este proyecto, el “negocio” corresponde al contexto de asesoría y toma de decisiones basada en datos.

Preguntas guía:

- ¿Qué variables se asocian con mayores niveles de obesidad?
- ¿Qué perfiles de riesgo aparecen en la base?
- ¿Qué modelo clasifica mejor los niveles de obesidad?
- ¿Qué reglas pueden aportar conocimiento interpretable?
- ¿Qué transformación mejora más el resultado?

### 10.2 Data Understanding / Comprensión de los datos

Actividades:

- Cargar dataset.
- Revisar dimensiones.
- Revisar variables.
- Revisar tipos de datos.
- Revisar nulos.
- Revisar duplicados.
- Revisar distribución de `NObeyesdad`.
- Revisar balance de clases.
- Analizar variables numéricas.
- Analizar variables categóricas.

### 10.3 Data Preparation / Preparación de los datos

Actividades:

- Separar variables predictoras y objetivo.
- Codificar variables categóricas.
- Escalar variables numéricas cuando corresponda.
- Preparar dataset para clustering.
- Preparar dataset para clasificación.
- Preparar dataset transaccional para FP-Growth.
- Crear variables nuevas para el experimento de ingeniería de características.

### 10.4 Modeling / Modelamiento

Líneas de modelamiento:

- Clustering.
- Clasificación.
- Asociación.
- Experimentos adicionales.

### 10.5 Evaluation / Evaluación

Evaluar:

- Calidad del clustering.
- Interpretabilidad de los clusters.
- Desempeño de clasificación en test.
- Métricas macro para clasificación multiclase.
- Reglas de asociación con Support, Confidence y Lift.
- Cambios en resultados después de cada experimento.

### 10.6 Deployment / Despliegue o comunicación

En esta tarea, el despliegue principal es académico:

- Nueva PPT.
- Código reproducible.
- Interpretación clara.
- Opcional: Backoffice simple para usar el clasificador.

---

## 11. Requisitos funcionales

### RF-01: Cargar dataset

El sistema debe cargar el archivo:

```python
ruta = "data\\ObesityDataSet_raw_and_data_sinthetic.csv"
```

Debe validar:

- Existencia del archivo.
- Dimensiones.
- Nombres de columnas.
- Tipo de variable objetivo.

---

### RF-02: Inspeccionar datos

El sistema debe mostrar:

- `df.head()`
- `df.info()`
- `df.describe()`
- Cantidad de nulos.
- Cantidad de duplicados.
- Distribución de la variable objetivo.
- Frecuencia de variables categóricas principales.

---

### RF-03: Aplicar CRISP-DM

El notebook debe incluir secciones explícitas:

1. Comprensión del problema.
2. Comprensión de los datos.
3. Preparación de datos.
4. Modelamiento.
5. Evaluación.
6. Comunicación/despliegue académico.

Además, debe indicar:

- Qué elementos de CRISP-DM fueron útiles.
- Qué elementos fueron menos útiles o limitados para esta tarea.
- Cómo CRISP-DM ayudó a ordenar el análisis.

---

### RF-04: Preparar datos para clustering

El sistema debe:

- Excluir la variable objetivo del entrenamiento de clustering principal.
- Mantener la variable objetivo solo para interpretar los clusters.
- Codificar variables categóricas.
- Escalar variables numéricas.
- Construir una matriz procesada.
- Aplicar reducción de dimensionalidad solo si corresponde al experimento.

---

### RF-05: Aplicar agrupamiento

El sistema debe aplicar un algoritmo de clustering.

Algoritmo base recomendado:

- `KMeans`.

Justificación sugerida:

- Es interpretable.
- Permite controlar el número de clusters.
- Funciona bien con datos tabulares procesados.
- Se puede evaluar con inertia y silhouette score.

Debe probar varios valores de `k`, por ejemplo:

```text
k = 2, 3, 4, 5, 6, 7, 8
```

Debe calcular:

- Inertia.
- Silhouette score.
- Tamaño de cada cluster.

---

### RF-06: Justificar número de clusters

La selección de `k` debe justificarse usando:

- Método del codo.
- Silhouette score.
- Tamaño razonable de los grupos.
- Interpretabilidad de los perfiles.

---

### RF-07: Interpretar clusters

El sistema debe crear una tabla por cluster con:

- Cantidad de registros.
- Edad promedio.
- Altura promedio.
- Peso promedio.
- IMC promedio si se crea.
- Nivel de obesidad predominante.
- Género predominante.
- Antecedente familiar predominante.
- Actividad física promedio.
- Conducta sedentaria promedio.
- Perfil interpretativo.

Ejemplo de salida esperada:

| Cluster | Tamaño | Perfil dominante | Nivel de obesidad predominante | Interpretación |
|---|---:|---|---|---|
| 0 | | Jóvenes con bajo peso y menor peso corporal | Insufficient Weight | Perfil de bajo riesgo por peso |
| 1 | | Personas con mayor peso e historial familiar | Obesity Type I/II | Perfil de riesgo metabólico |
| 2 | | Personas activas con peso normal | Normal Weight | Perfil saludable |

---

### RF-08: Preparar datos para clasificación

El sistema debe:

- Definir `X` e `y`.
- Codificar `y` con `LabelEncoder`.
- Separar train/test usando estratificación.
- Usar `random_state=42`.
- Usar pipelines para evitar fuga de datos.

División sugerida:

```python
test_size = 0.25
stratify = y
random_state = 42
```

---

### RF-09: Entrenar modelos de clasificación

Modelos mínimos recomendados:

- Regresión logística multinomial.
- Árbol de decisión.
- Random Forest.

Modelos opcionales:

- KNN.
- SVM.
- Gradient Boosting.
- XGBoost, solo si está disponible y se justifica.

---

### RF-10: Evaluar modelos de clasificación

El sistema debe calcular:

- Accuracy.
- Precision macro.
- Recall macro.
- F1 macro.
- Matriz de confusión.
- Classification report.

Debe indicar:

- Mejor modelo según F1 macro.
- Mejor modelo según accuracy.
- Si hay diferencias relevantes entre métricas.
- Qué clases se predicen peor.
- Qué mejoras futuras podrían aplicarse.

---

### RF-11: Aplicar FP-Growth

El sistema debe:

- Transformar los datos a formato transaccional.
- Convertir variables categóricas en ítems.
- Discretizar variables numéricas.
- Incluir `NObeyesdad` como ítem.
- Aplicar FP-Growth.
- Generar reglas de asociación.

Métricas mínimas:

- Support.
- Confidence.
- Lift.

---

### RF-12: Interpretar reglas de asociación

El sistema debe presentar:

- Reglas con mejores indicadores.
- 6 reglas novedosas.

Cada regla debe incluir:

- Antecedente.
- Consecuente.
- Support.
- Confidence.
- Lift.
- Interpretación.
- Justificación de novedad o utilidad.

---

### RF-13: Realizar experimento 1 de reducción de dimensionalidad

#### PCA

Aplicar `PCA` sobre los datos preprocesados.

Evaluar el impacto sobre:

- Clustering, usando KMeans sobre componentes principales.
- Clasificación, usando modelo base sobre componentes principales.

Métricas a comparar:

- Silhouette score.
- F1 macro.
- Accuracy.
- Número de componentes.
- Varianza explicada acumulada.

---

### RF-14: Realizar experimento 2 de reducción de dimensionalidad

#### TruncatedSVD

Aplicar `TruncatedSVD` sobre la matriz procesada, especialmente útil si hay muchas variables generadas por One-Hot Encoding.

Evaluar el impacto sobre:

- Clustering, usando KMeans sobre componentes SVD.
- Clasificación, usando modelo base sobre componentes SVD.

Métricas a comparar:

- Silhouette score.
- F1 macro.
- Accuracy.
- Número de componentes.
- Varianza explicada aproximada.

---

### RF-15: Realizar experimento 3 con 5 nuevos atributos

Crear 5 variables nuevas recomendadas por IA o bibliografía.

Atributos propuestos:

1. **BMI / IMC**
   - Fórmula: `Weight / Height^2`.
   - Justificación: indicador antropométrico clásico.

2. **BMI_Category**
   - Categoría derivada desde el IMC.
   - Ejemplo: bajo, normal, sobrepeso, obesidad.

3. **Healthy_Habits_Score**
   - Puntaje combinado de hábitos saludables.
   - Puede incluir: consumo de vegetales, agua, actividad física y monitoreo calórico.

4. **Risky_Eating_Score**
   - Puntaje combinado de hábitos alimentarios de riesgo.
   - Puede incluir: consumo de alimentos hipercalóricos, snacks entre comidas y consumo de alcohol.

5. **Sedentary_Risk_Score**
   - Puntaje relacionado con sedentarismo.
   - Puede incluir: uso de tecnología y tipo de transporte.

El sistema debe comparar:

- Modelo base sin ingeniería de características.
- Modelo con 5 atributos nuevos.

Métricas:

- Accuracy.
- F1 macro.
- Recall macro.
- Cambios en matriz de confusión.
- Importancia de variables, si el modelo lo permite.

---

### RF-16: Resumir descubrimientos

La nueva PPT debe incluir al menos 3 descubrimientos interesantes o métricas destacadas.

Ejemplos de descubrimientos esperados:

1. El mejor clasificador alcanzó el mayor F1 macro en test.
2. Un cluster concentró mayor proporción de personas con obesidad y menor actividad física.
3. Algunas reglas de asociación presentaron Lift mayor a 1, sugiriendo asociación positiva entre hábitos y niveles de obesidad.

Cada descubrimiento debe responder:

- Qué se encontró.
- Qué métrica lo respalda.
- Por qué es útil.
- Cómo se relaciona con bibliografía o conocimiento del dominio.

---

### RF-17: Comparar con bibliografía

El sistema debe incluir al menos una referencia relacionada.

Bibliografía mínima sugerida:

- Mendoza Palechor, F., & De la Hoz Manotas, A. (2019). Dataset for estimation of obesity levels based on eating habits and physical condition in individuals from Colombia, Peru and Mexico. *Data in Brief*.
- Fuente adicional recomendada: referencia sobre IMC, actividad física, hábitos alimentarios u obesidad.

La PPT debe incluir al menos una diapositiva o nota breve donde se compare un hallazgo del trabajo con la bibliografía.

---

### RF-18: Backoffice voluntario

Si se implementa, el Backoffice debe permitir:

- Ingresar valores de una persona.
- Usar el mejor clasificador entrenado.
- Predecir nivel de obesidad.
- Mostrar probabilidad por clase si el modelo lo permite.
- Entregar una interpretación simple.

Tecnología sugerida:

- Streamlit.

Archivos sugeridos:

```text
app.py
models/mejor_modelo.pkl
models/label_encoder.pkl
```

---

## 12. Requisitos no funcionales

- El código debe ser reproducible.
- El notebook debe ejecutarse de inicio a fin.
- Las secciones deben estar ordenadas según CRISP-DM.
- Los gráficos deben tener títulos y etiquetas.
- Las tablas deben ser claras.
- Las conclusiones deben estar conectadas con las métricas.
- El análisis debe evitar interpretaciones clínicas no respaldadas.
- Se debe usar `random_state=42` cuando sea posible.
- La presentación debe ser clara, concisa y visualmente atractiva.

---

## 13. Métricas

### 13.1 Clustering

- Inertia.
- Silhouette score.
- Tamaño de clusters.
- Distribución de `NObeyesdad` por cluster.
- Interpretabilidad de perfiles.

### 13.2 Clasificación

- Accuracy.
- Precision macro.
- Recall macro.
- F1 macro.
- Matriz de confusión.
- Classification report.

### 13.3 Asociación

- Support.
- Confidence.
- Lift.
- Número de reglas.
- Novedad de reglas seleccionadas.

### 13.4 Experimentos

- Cambio de F1 macro.
- Cambio de accuracy.
- Cambio de silhouette score.
- Cambio en matriz de confusión.
- Cambio en interpretabilidad.
- Costo/beneficio de cada transformación.

---

## 14. Diseño de experimentos

### Modelo base

- Preprocesamiento estándar.
- Clasificación con modelos comparados.
- Clustering con KMeans.
- FP-Growth con discretización inicial.

### Experimento 1: PCA

Pregunta:

> ¿La reducción con PCA mejora o mantiene el rendimiento del clustering o clasificación?

Resultado esperado:

- Tabla comparativa con métricas antes/después.
- Gráfico de varianza explicada acumulada.
- Interpretación.

### Experimento 2: TruncatedSVD

Pregunta:

> ¿La reducción con TruncatedSVD mejora el desempeño o simplifica el espacio de variables codificadas?

Resultado esperado:

- Tabla comparativa con métricas antes/después.
- Gráfico de varianza explicada acumulada aproximada.
- Interpretación.

### Experimento 3: Ingeniería de características

Pregunta:

> ¿Los 5 nuevos atributos derivados mejoran el rendimiento del modelo o la interpretación de resultados?

Resultado esperado:

- Tabla comparativa modelo base vs modelo con nuevas variables.
- Métricas de clasificación.
- Importancia de variables si se usa Random Forest.
- Interpretación.

---

## 15. Tabla de comparación de modelos

| Modelo | Experimento | Accuracy | Precision macro | Recall macro | F1 macro | Comentario |
|---|---|---:|---:|---:|---:|---|
| Regresión logística | Base | | | | | |
| Árbol de decisión | Base | | | | | |
| Random Forest | Base | | | | | |
| Mejor modelo | PCA | | | | | |
| Mejor modelo | TruncatedSVD | | | | | |
| Mejor modelo | Feature Engineering | | | | | |

---

## 16. Tabla de comparación de clustering

| Experimento | Algoritmo | k | Silhouette | Inertia | Interpretabilidad |
|---|---|---:|---:|---:|---|
| Base | KMeans | | | | |
| PCA | KMeans | | | | |
| TruncatedSVD | KMeans | | | | |
| Feature Engineering | KMeans | | | | |

---

## 17. Tabla de reglas de asociación

| Tipo | Antecedente | Consecuente | Support | Confidence | Lift | Interpretación |
|---|---|---|---:|---:|---:|---|
| Mejor indicador | | | | | | |
| Mejor indicador | | | | | | |
| Novedosa 1 | | | | | | |
| Novedosa 2 | | | | | | |
| Novedosa 3 | | | | | | |
| Novedosa 4 | | | | | | |
| Novedosa 5 | | | | | | |
| Novedosa 6 | | | | | | |

---

## 18. Mapeo contra rúbrica

| Criterio de rúbrica | Requisito para apuntar a excelente | Evidencia en entrega |
|---|---|---|
| Completitud de tarea para la casa | Usa agrupamiento, clasificación y asociación; justifica métodos; explica 6 reglas | Notebook + PPT con secciones de clustering, clasificación y FP-Growth |
| Comprensión del modelo y metodología | Demuestra comprensión profunda de algoritmos, métricas y CRISP-DM | Explicaciones en notebook y PPT |
| Análisis y transformación de datos | Analiza, transforma, reduce dimensionalidad e implementa ingeniería de características | EDA + PCA + TruncatedSVD + 5 nuevas variables |
| Presentación de resultados | Resultados claros, concisos y visualmente atractivos | Nueva PPT con gráficos y tablas |
| Interpretación y conclusiones | Interpretación perspicaz y fundamentada | 3 descubrimientos + comparación bibliográfica + conclusiones |

---

## 19. Estructura recomendada del notebook

```text
01_importacion_librerias
02_carga_datos
03_crisp_dm_comprension_problema
04_comprension_datos
05_analisis_exploratorio
06_preparacion_datos
07_clustering_base
08_interpretacion_clusters
09_clasificacion_base
10_evaluacion_modelos
11_fp_growth_reglas_asociacion
12_experimento_pca
13_experimento_truncated_svd
14_experimento_feature_engineering
15_comparacion_experimentos
16_descubrimientos_y_bibliografia
17_conclusiones
18_insumos_ppt
```

---

## 20. Estructura recomendada de la nueva PPT

Máximo sugerido: 15 diapositivas.

| Diapositiva | Contenido |
|---:|---|
| 1 | Título, estudiante, curso, docente y dataset |
| 2 | Objetivo del trabajo y problema |
| 3 | CRISP-DM: elementos útiles para el proyecto |
| 4 | Descripción del dataset y variable objetivo |
| 5 | Preparación y transformación de datos |
| 6 | EDA: hallazgos principales |
| 7 | Clustering: método, k seleccionado y justificación |
| 8 | Clustering: perfiles encontrados |
| 9 | Clasificación: modelos comparados |
| 10 | Clasificación: mejores resultados en test |
| 11 | FP-Growth: reglas con mejores indicadores |
| 12 | 6 reglas novedosas e interpretación |
| 13 | Experimentos: PCA, TruncatedSVD y 5 nuevas variables |
| 14 | 3 descubrimientos o métricas destacadas + bibliografía |
| 15 | Conclusiones y mejoras futuras |

---

## 21. Criterios de aceptación

El proyecto se considera completo si:

- El dataset se carga desde `data\ObesityDataSet_raw_and_data_sinthetic.csv`.
- Se utiliza CRISP-DM de forma explícita.
- Se explica qué elementos de CRISP-DM fueron útiles.
- Se realiza EDA.
- Se transforman datos para mejorar el análisis.
- Se aplica clustering.
- Se justifica el algoritmo de clustering.
- Se justifica el número de clusters.
- Se interpretan los clusters.
- Se aplican algoritmos de clasificación.
- Se comparan modelos con datos de testeo.
- Se identifica el mejor clasificador.
- Se proponen mejoras futuras.
- Se aplica FP-Growth.
- Se reporta Lift.
- Se explican reglas con mejores indicadores.
- Se explican 6 reglas novedosas.
- Se realizan 2 reducciones de dimensionalidad no implementadas previamente.
- Se realiza un experimento con 5 nuevos atributos.
- Se evalúa cómo cambian los resultados en cada experimento.
- Se resumen al menos 3 descubrimientos o métricas destacadas.
- Se compara al menos un hallazgo con bibliografía relacionada.
- Se entrega nueva PPT.
- Se entrega código.
- Opcionalmente, se implementa Backoffice para usar el clasificador.

---

## 22. Riesgos y mitigaciones

| Riesgo | Impacto | Mitigación |
|---|---:|---|
| Las reglas FP-Growth son demasiado obvias | Medio | Filtrar por Lift y buscar combinaciones no triviales |
| Demasiadas reglas generadas | Medio | Ajustar soporte mínimo y ordenar por Lift/confianza |
| PCA empeora interpretabilidad | Medio | Presentarlo como comparación, no como reemplazo obligatorio |
| TruncatedSVD no mejora métricas | Bajo | Reportar resultado honestamente y discutir costo/beneficio |
| Nuevas variables no mejoran modelo | Medio | Evaluar importancia e interpretar por qué no aportaron |
| Modelo clasifica bien solo por variables muy directas como peso/altura | Medio | Discutir posible dependencia del IMC y revisar importancia de variables |
| PPT queda sobrecargada | Alto | Usar tablas resumen y mover detalles al código |
| Backoffice consume tiempo | Medio | Dejarlo como opcional solo si la nota lo requiere |

---

## 23. Mejoras futuras sugeridas

- Aplicar validación cruzada estratificada.
- Optimizar hiperparámetros con GridSearchCV.
- Probar modelos adicionales.
- Revisar sensibilidad de FP-Growth a distintos soportes mínimos.
- Evaluar balance de clases.
- Analizar importancia de variables.
- Comparar resultados con y sin variables antropométricas directas.
- Mejorar ingeniería de características.
- Construir Backoffice voluntario en Streamlit.

---

## 24. Prompt recomendado para trabajar en tu sistema

```md
Actúa como asistente de desarrollo para una tarea académica de Magíster en Data Science.

Usa este PRD como fuente principal y construye un notebook reproducible usando el archivo:

data\ObesityDataSet_raw_and_data_sinthetic.csv

El proyecto debe seguir CRISP-DM y cumplir la rúbrica de evaluación. Debe incluir análisis exploratorio, agrupamiento, clasificación, asociación con FP-Growth, métricas, Lift, interpretación de 6 reglas novedosas y conclusiones.

Además, debe realizar 3 experimentos:
1. Reducción de dimensionalidad con PCA.
2. Reducción de dimensionalidad con TruncatedSVD.
3. Ingeniería de características con 5 nuevos atributos: BMI, BMI_Category, Healthy_Habits_Score, Risky_Eating_Score y Sedentary_Risk_Score.

Para cada experimento, compara cómo cambian los resultados del clustering o clasificación. Presenta tablas comparativas, gráficos claros y conclusiones útiles para una nueva PPT de máximo 15 diapositivas.

Prioriza código simple, ordenado, reproducible, con secciones claras y explicaciones interpretables.
```

---

## 25. Definition of Done

El proyecto estará listo cuando existan:

- Notebook ejecutable.
- PPT anterior.
- Nueva PPT.
- Código entregable.
- CRISP-DM explicado.
- Clustering aplicado e interpretado.
- Clasificación comparada con métricas de test.
- Mejor modelo identificado.
- FP-Growth aplicado.
- Lift reportado.
- 6 reglas novedosas interpretadas.
- 2 experimentos de reducción de dimensionalidad.
- 1 experimento con 5 nuevas variables.
- Al menos 3 descubrimientos o métricas destacadas.
- Comparación con bibliografía.
- Conclusiones claras.
- Backoffice opcional si se busca el punto extra.
