# PRD — Tarea Obesity Dataset con CRISP-DM, Clustering Justificado e Iteraciones de Mejora

## 1. Nombre del proyecto

**Extracción de conocimiento sobre niveles de obesidad mediante CRISP-DM, agrupamiento, clasificación, asociación y experimentos iterativos de mejora**

---

## 2. Contexto académico

Este proyecto corresponde a la tarea del **Taller de Aplicaciones — Magíster en Data Science**.

El trabajo debe aplicar buenas prácticas de ciencia de datos para extraer conocimiento desde un dataset del **UCI Machine Learning Repository**. La tarea solicita usar métodos de:

- Agrupamiento.
- Clasificación.
- Asociación.
- CRISP-DM.
- Transformación de datos.
- Reducción de dimensionalidad.
- Ingeniería de características.
- Evaluación e interpretación de resultados.

La entrega debe incluir:

- PPT de la tarea para la casa.
- Nueva PPT ajustada con iteraciones y mejoras.
- Código reproducible.
- Resultados explicables para exposición oral.

---

## 3. Dataset seleccionado

| Elemento | Descripción |
|---|---|
| Dataset | Estimation of Obesity Levels Based On Eating Habits and Physical Condition |
| Fuente | UCI Machine Learning Repository |
| Archivo local | `data\ObesityDataSet_raw_and_data_sinthetic.csv` |
| Registros esperados | 2.111 |
| Atributos esperados | 17 |
| Variable objetivo esperada | `NObeyesdad` |
| Tipo de problema | Clasificación multiclase |
| Uso adicional | Clustering de perfiles de riesgo y reglas de asociación |

---

## 4. Variable objetivo

La variable objetivo esperada es `NObeyesdad`, que representa siete niveles de estado nutricional u obesidad:

| Clase | Interpretación |
|---|---|
| `Insufficient_Weight` | Peso insuficiente |
| `Normal_Weight` | Peso normal |
| `Overweight_Level_I` | Sobrepeso nivel I |
| `Overweight_Level_II` | Sobrepeso nivel II |
| `Obesity_Type_I` | Obesidad tipo I |
| `Obesity_Type_II` | Obesidad tipo II |
| `Obesity_Type_III` | Obesidad tipo III |

---

## 5. Problema a resolver

El equipo debe construir un análisis reproducible que permita extraer conocimiento sobre perfiles de obesidad a partir de variables demográficas, antropométricas, alimentarias, conductuales y de actividad física.

El proyecto debe responder:

1. ¿Qué perfiles de personas pueden identificarse mediante agrupamiento?
2. ¿Qué algoritmo de clustering resulta más adecuado y por qué?
3. ¿Los datos presentan una estructura compatible con clusters globulares?
4. ¿Qué modelo de clasificación predice mejor el nivel de obesidad?
5. ¿Qué reglas de asociación presentan mejores indicadores y cuáles son novedosas?
6. ¿Qué mejoras se observan al aplicar reducción de dimensionalidad, variables ordinales, ingeniería de características, validación cruzada y optimización de hiperparámetros?
7. ¿Qué hallazgos son suficientemente claros para defenderlos en una exposición?

---

## 6. Objetivo general

Desarrollar un análisis de ciencia de datos siguiendo CRISP-DM para identificar perfiles, predecir niveles de obesidad y descubrir reglas de asociación, incorporando iteraciones progresivas de mejora que permitan justificar las decisiones metodológicas y comunicar resultados en una presentación académica.

---

## 7. Objetivos específicos

- Cargar y validar el dataset desde el path local.
- Inspeccionar la estructura, calidad y distribución de los datos.
- Aplicar CRISP-DM como metodología de trabajo.
- Comparar alternativas de clustering antes de seleccionar el modelo final.
- Justificar si K-Means es adecuado o si corresponde usar otro algoritmo.
- Entrenar y comparar modelos de clasificación.
- Aplicar FP-Growth y medir Lift.
- Explicar reglas con mejores indicadores.
- Seleccionar e interpretar 6 reglas novedosas.
- Agregar una nueva iteración de mejora sin eliminar las iteraciones previas.
- Incorporar optimización de hiperparámetros.
- Tratar variables ordinales como ordinales cuando corresponda.
- Crear variables de ingeniería de características.
- Aplicar validación cruzada estratificada.
- Preparar una PPT extendida, clara y alineada con la rúbrica.
- Corregir problemas de visualización de outputs truncados en el notebook.

---

## 8. Metodología CRISP-DM

El proyecto debe organizarse siguiendo CRISP-DM.

| Fase CRISP-DM | Aplicación en el proyecto | Evidencia esperada |
|---|---|---|
| Comprensión del problema | Se define que el objetivo es extraer conocimiento sobre obesidad y hábitos asociados | Objetivo, preguntas de análisis y alcance |
| Comprensión de los datos | Se inspeccionan variables, clases, nulos, duplicados y distribución de la variable objetivo | Tablas, gráficos y descripción del dataset |
| Preparación de datos | Se codifican variables, se escalan numéricas, se tratan ordinales y se crean nuevas variables | Pipelines, transformadores y dataset procesado |
| Modelamiento | Se aplican clustering, clasificación, FP-Growth y experimentos | Modelos entrenados y resultados comparados |
| Evaluación | Se comparan métricas, interpretabilidad y utilidad de resultados | Tablas de métricas y conclusiones por modelo |
| Comunicación / despliegue | Se prepara PPT y opcionalmente Backoffice | Presentación, código y posible app |

### 8.1 Elementos de CRISP-DM útiles para esta tarea

| Elemento | Utilidad para el trabajo |
|---|---|
| Separar comprensión del problema y comprensión de datos | Permite evitar aplicar algoritmos sin propósito analítico claro |
| Preparación de datos antes del modelamiento | Reduce errores por variables mal codificadas, escalas incompatibles o fuga de datos |
| Evaluación posterior al modelamiento | Permite comparar resultados y no elegir modelos solo por intuición |
| Ciclo iterativo | Permite incorporar feedback docente y nuevas mejoras sin perder versiones previas |
| Comunicación final | Obliga a convertir resultados técnicos en hallazgos explicables para la PPT |

### 8.2 Limitaciones de CRISP-DM en esta tarea

| Limitación | Interpretación |
|---|---|
| No existe despliegue productivo obligatorio | La fase de despliegue se adapta como comunicación académica y PPT |
| El dataset ya está definido | La fase de recolección de datos es limitada porque no se levantarán nuevos datos |
| La tarea exige varios métodos | El proceso debe dividirse en tres líneas: clustering, clasificación y asociación |

---

## 9. Alcance del proyecto

### 9.1 Incluye

- Carga del dataset.
- Análisis exploratorio.
- Preparación de datos.
- Aplicación explícita de CRISP-DM.
- Comparación de alternativas de clustering.
- Justificación del algoritmo de clustering seleccionado.
- Justificación del número de clusters.
- Interpretación de clusters.
- Entrenamiento y comparación de clasificadores.
- Evaluación con test y validación cruzada.
- Optimización de hiperparámetros.
- Tratamiento de variables ordinales.
- Ingeniería de características.
- FP-Growth.
- Interpretación de reglas con Lift.
- Selección de 6 reglas novedosas.
- PPT extendida para exposición.
- Corrección de outputs truncados.

### 9.2 No incluye

- Despliegue productivo obligatorio.
- Uso clínico real del clasificador.
- Inferencia causal.
- Deep learning obligatorio.
- API productiva.
- Dashboard obligatorio.

---

## 10. Iteraciones del proyecto

El proyecto debe conservar las iteraciones anteriores y agregar una nueva iteración de mejora.

| Iteración | Nombre | Propósito | Estado esperado |
|---:|---|---|---|
| 1 | Base tarea para la casa | Cumplir requisitos mínimos: clustering, clasificación, FP-Growth y CRISP-DM | Se conserva como línea base |
| 2 | Iteración rúbrica 60% | Agregar reducción de dimensionalidad, ingeniería de características inicial y 3 descubrimientos | Se conserva y se compara |
| 3 | Iteración mejorada | Incorporar justificación robusta de clustering, optimización, ordinalidad, nuevas variables y validación cruzada | Se agrega como versión final recomendada |

---

## 11. Requisitos funcionales generales

### RF-01: Cargar dataset

El sistema debe cargar el archivo:

```python
ruta = "data\\ObesityDataSet_raw_and_data_sinthetic.csv"
```

Debe validar:

- Existencia del archivo.
- Dimensiones del dataframe.
- Nombres de columnas.
- Variable objetivo.
- Tipos de datos.

---

### RF-02: Evitar outputs truncados en el notebook

El sistema debe configurar la visualización de pandas para evitar mensajes como:

```text
Output is truncated. View as a scrollable element or open in a text editor. Adjust cell output settings...
```

Debe incluir al inicio del notebook:

```python
import pandas as pd
import numpy as np
from IPython.display import display

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", 200)
pd.set_option("display.max_colwidth", None)
pd.set_option("display.width", 0)
pd.set_option("display.expand_frame_repr", False)
np.set_printoptions(threshold=np.inf)
```

También debe crear funciones auxiliares para inspección ordenada:

```python
def mostrar_completo(df, filas=200):
    with pd.option_context(
        "display.max_rows", filas,
        "display.max_columns", None,
        "display.max_colwidth", None,
        "display.width", 0,
        "display.expand_frame_repr", False
    ):
        display(df)
```

Para reportes largos, el sistema debe convertir outputs extensos en DataFrames y no imprimir textos largos directamente.

Ejemplo:

```python
from sklearn.metrics import classification_report

reporte = classification_report(y_test, y_pred, output_dict=True)
reporte_df = pd.DataFrame(reporte).T
mostrar_completo(reporte_df)
```

Cuando una tabla sea demasiado extensa, el sistema debe exportarla además como archivo:

```python
reporte_df.to_csv("outputs/reporte_clasificacion_completo.csv", index=True)
```

---

### RF-03: Inspeccionar características de los datos

El sistema debe mostrar de forma no truncada:

- Primeras filas.
- Últimas filas.
- Dimensiones.
- Tipos de datos.
- Valores únicos por columna.
- Cantidad de nulos.
- Cantidad de duplicados.
- Distribución de la variable objetivo.
- Estadísticos descriptivos de variables numéricas.
- Frecuencias de variables categóricas.

Debe incluir una tabla resumen de variables:

| Columna | Tipo | N únicos | Nulos | Ejemplos | Rol esperado |
|---|---|---:|---:|---|---|
| `Age` | Numérica | | | | Predictora |
| `Height` | Numérica | | | | Predictora antropométrica |
| `Weight` | Numérica | | | | Predictora antropométrica |
| `NObeyesdad` | Categórica | 7 | | | Objetivo |

---

## 12. Clustering: decisión metodológica obligatoria

### 12.1 Problema detectado

No se debe asumir automáticamente que K-Means es el mejor algoritmo. El docente solicita justificar la elección del tipo de cluster y del número de clusters.

K-Means funciona mejor cuando los grupos tienen una forma aproximadamente:

- Globular.
- Convexa.
- De tamaño relativamente balanceado.
- Con varianzas similares.
- Separables en términos de distancia euclidiana.

El dataset de obesidad contiene variables mixtas, codificación categórica y posibles relaciones no lineales. Por lo tanto, el equipo debe comparar más de una alternativa antes de seleccionar el modelo final.

---

### 12.2 Preguntas que debe responder la sección de clustering

| Pregunta | Evidencia requerida |
|---|---|
| ¿Los datos tienen forma globular? | Visualización PCA/UMAP 2D, silhouette, distribución de clusters |
| ¿K-Means es adecuado? | Comparación contra otros algoritmos |
| ¿Existe estructura no globular? | Resultados de clustering jerárquico o basado en densidad |
| ¿Cuál algoritmo se elige finalmente? | Tabla comparativa con métricas e interpretación |
| ¿Por qué se elige ese algoritmo? | Justificación técnica y comunicable para la exposición |

---

### 12.3 Algoritmos de clustering a comparar

| Algoritmo | Por qué se prueba | Cuándo sería adecuado | Limitación principal |
|---|---|---|---|
| K-Means | Es una línea base simple, interpretable y común en datos tabulares escalados | Si los clusters son compactos, globulares y separables por distancia | Asume formas aproximadamente esféricas y puede fallar con clusters no convexos |
| Gaussian Mixture Model | Permite clusters elípticos y asignación probabilística | Si los grupos tienen diferente varianza o forma elíptica | Requiere definir número de componentes y puede ser sensible a inicialización |
| Agglomerative Clustering | Permite explorar estructura jerárquica sin asumir centroides | Si los grupos no son claramente globulares o se quiere dendrograma | Puede ser más costoso y depende del linkage elegido |
| DBSCAN | Detecta clusters por densidad y ruido | Si existen grupos de forma irregular y outliers | Puede fallar en alta dimensionalidad o con densidades variables |
| K-Prototypes | Maneja variables mixtas numéricas y categóricas | Si se desea evitar convertir todo a One-Hot Encoding | Requiere librería adicional y ajuste de parámetro gamma |

---

### 12.4 Estrategia de decisión para clustering

El equipo debe seguir esta estrategia:

1. Crear una matriz procesada con variables predictoras.
2. Escalar variables numéricas.
3. Codificar variables categóricas.
4. Proyectar los datos en 2 dimensiones usando PCA o UMAP solo para visualización.
5. Evaluar si los grupos se ven compactos, globulares o solapados.
6. Probar K-Means, Gaussian Mixture y Agglomerative Clustering como mínimo.
7. Probar DBSCAN solo si la visualización sugiere densidades o outliers relevantes.
8. Comparar métricas y perfiles generados.
9. Seleccionar el algoritmo que combine mejor métrica e interpretabilidad.

---

### 12.5 Métricas de clustering

| Métrica | Interpretación | Uso en la decisión |
|---|---|---|
| Silhouette Score | Mide cohesión interna y separación entre clusters | Mayor valor sugiere mejor separación |
| Davies-Bouldin Index | Mide similitud entre clusters | Menor valor sugiere mejor separación |
| Calinski-Harabasz Index | Relación entre dispersión intercluster e intracluster | Mayor valor sugiere clusters más definidos |
| Tamaño de clusters | Evalúa si hay grupos demasiado pequeños o desbalanceados | Evita elegir soluciones artificiales |
| Interpretabilidad | Evalúa si los perfiles tienen sentido para explicar obesidad | Criterio clave para la exposición |

---

### 12.6 Regla de selección del algoritmo de clustering

| Situación observada | Decisión recomendada |
|---|---|
| Los clusters son compactos, separados y aproximadamente globulares | Se justifica seleccionar K-Means |
| Los clusters son elípticos o con varianzas diferentes | Se justifica seleccionar Gaussian Mixture Model |
| Los clusters muestran estructura jerárquica o separación no necesariamente globular | Se justifica seleccionar Agglomerative Clustering |
| Hay outliers o grupos por densidad | Se justifica evaluar DBSCAN |
| Las variables categóricas dominan y se quiere preservar naturaleza mixta | Se justifica evaluar K-Prototypes |

---

### 12.7 Redacción esperada para justificar el modelo elegido

El notebook y la PPT deben incluir una justificación en tercera persona.

Ejemplo si gana K-Means:

> El equipo seleccionó K-Means porque, luego de estandarizar variables numéricas y codificar variables categóricas, el algoritmo presentó una combinación favorable entre Silhouette Score, estabilidad del tamaño de los clusters e interpretabilidad de los perfiles. Aunque K-Means asume grupos aproximadamente globulares, la visualización reducida y la comparación contra modelos alternativos no evidenciaron una mejora suficiente al usar métodos más complejos. Por esta razón, K-Means se mantuvo como modelo final de agrupamiento.

Ejemplo si gana Gaussian Mixture:

> El equipo seleccionó Gaussian Mixture Model porque los perfiles observados no fueron completamente globulares y el modelo permitió representar grupos con dispersión diferente. Además, obtuvo métricas competitivas y generó perfiles interpretables en relación con peso, actividad física, antecedentes familiares y nivel de obesidad predominante.

Ejemplo si gana Agglomerative Clustering:

> El equipo seleccionó Agglomerative Clustering porque la estructura de los datos no mostró clusters claramente globulares y el enfoque jerárquico permitió separar perfiles interpretables sin depender de centroides. Esta decisión fue respaldada por las métricas de separación y por la claridad de los perfiles resultantes.

---

## 13. Clasificación: modelos y justificación

### 13.1 Modelos mínimos a evaluar

| Modelo | Por qué se incluye | Rol en el análisis |
|---|---|---|
| Regresión logística multinomial | Sirve como modelo base interpretable para clasificación multiclase | Línea base explicable |
| Árbol de decisión | Permite reglas simples y visualmente explicables | Modelo interpretable no lineal |
| Random Forest | Captura relaciones no lineales y reduce sobreajuste frente a un árbol único | Modelo robusto principal |
| KNN | Evalúa si la cercanía entre perfiles predice bien la clase | Modelo basado en similitud |
| SVM | Puede rendir bien en espacios de alta dimensión después de codificación | Modelo de frontera de decisión |

### 13.2 Criterio de elección del mejor clasificador

El mejor clasificador no debe elegirse solo por accuracy. El equipo debe usar como métrica principal **F1 macro**, porque el problema es multiclase y se requiere que el rendimiento sea razonable en todas las clases.

| Métrica | Uso |
|---|---|
| Accuracy | Medida general de aciertos |
| Precision macro | Evalúa falsos positivos de forma balanceada entre clases |
| Recall macro | Evalúa falsos negativos de forma balanceada entre clases |
| F1 macro | Métrica principal para comparar rendimiento balanceado |
| Matriz de confusión | Permite identificar clases confundidas |

---

## 14. Nueva iteración de mejora

La nueva iteración debe agregarse sin eliminar las anteriores.

### 14.1 Mejoras incorporadas

| Prioridad | Mejora | Impacto esperado | Justificación |
|---:|---|---|---|
| 1 | Optimización de hiperparámetros con GridSearchCV o RandomizedSearchCV | Alto | Permite mejorar el rendimiento del modelo evitando depender de parámetros por defecto |
| 2 | Tratamiento de variables ordinales, especialmente `CAEC` y `CALC` | Medio | Preserva el orden natural de categorías como frecuencia de consumo, evitando tratarlas como nominales independientes |
| 3 | Ingeniería de variables: IMC e interacción `FAF × FAVC` | Alto | Agrega variables con sentido de dominio y puede mejorar la capacidad predictiva |
| 4 | Validación cruzada estratificada con k=5 | Medio | Entrega una estimación más robusta del rendimiento y reduce dependencia de una sola partición train/test |

---

### 14.2 Iteración 3A: Tratamiento ordinal

El sistema debe tratar como ordinales las variables que representan frecuencia o intensidad.

Variables candidatas:

| Variable | Significado esperado | Tratamiento propuesto |
|---|---|---|
| `CAEC` | Consumo de alimentos entre comidas | Codificación ordinal |
| `CALC` | Consumo de alcohol | Codificación ordinal |
| `FCVC` | Frecuencia de consumo de verduras | Mantener numérica u ordinal según inspección |
| `NCP` | Número de comidas principales | Mantener numérica u ordinal según inspección |
| `FAF` | Frecuencia de actividad física | Mantener numérica u ordinal según inspección |
| `TUE` | Tiempo usando tecnología | Mantener numérica u ordinal según inspección |

Ejemplo de codificación para `CAEC`:

```python
orden_caec = ["no", "Sometimes", "Frequently", "Always"]
```

Ejemplo de codificación para `CALC`:

```python
orden_calc = ["no", "Sometimes", "Frequently", "Always"]
```

El equipo debe validar los valores reales antes de aplicar el mapeo.

---

### 14.3 Iteración 3B: Ingeniería de características ampliada

El sistema debe crear al menos las siguientes variables:

| Variable nueva | Fórmula o construcción | Justificación |
|---|---|---|
| `BMI` | `Weight / Height**2` | Indicador antropométrico clásico relacionado con peso y talla |
| `BMI_Category` | Categorías derivadas de IMC | Permite interpretar rangos de estado nutricional |
| `FAF_FAVC_Interaction` | `FAF * FAVC_binaria` | Evalúa interacción entre actividad física y consumo de alimentos hipercalóricos |
| `Healthy_Habits_Score` | Combinación de vegetales, agua, actividad física y monitoreo calórico | Resume hábitos potencialmente protectores |
| `Risky_Eating_Score` | Combinación de FAVC, CAEC, CALC y baja ingesta saludable | Resume hábitos alimentarios de riesgo |
| `Sedentary_Risk_Score` | Combinación de TUE, baja FAF y transporte sedentario | Resume exposición a sedentarismo |

Aunque se solicitan 5 atributos nuevos, el equipo puede crear 6 si mejora la interpretación. La PPT debe destacar como mínimo 5.

---

### 14.4 Gráfico obligatorio de importancia de atributos creados

La nueva PPT debe incluir un gráfico de importancia de variables cuando se use un modelo que lo permita, por ejemplo Random Forest.

El gráfico debe responder:

- Si las variables creadas aportan información.
- Si `BMI` domina la predicción.
- Si las interacciones y scores agregan valor.
- Si la mejora del modelo se debe a variables nuevas o a variables originales.

Tabla esperada:

| Variable | Importancia | Tipo |
|---|---:|---|
| `BMI` | | Creada |
| `FAF_FAVC_Interaction` | | Creada |
| `Healthy_Habits_Score` | | Creada |
| `Risky_Eating_Score` | | Creada |
| `Sedentary_Risk_Score` | | Creada |

---

### 14.5 Iteración 3C: Validación cruzada estratificada

El sistema debe aplicar validación cruzada estratificada con `k=5`.

Requisito técnico:

```python
from sklearn.model_selection import StratifiedKFold, cross_validate

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
```

Métricas de validación cruzada:

- Accuracy.
- Precision macro.
- Recall macro.
- F1 macro.

Resultado esperado:

| Modelo | Accuracy CV media | F1 macro CV media | F1 macro CV desviación | Interpretación |
|---|---:|---:|---:|---|
| Regresión logística | | | | |
| Árbol de decisión | | | | |
| Random Forest | | | | |
| SVM | | | | |

---

### 14.6 Iteración 3D: Optimización de hiperparámetros

El sistema debe aplicar `GridSearchCV` o `RandomizedSearchCV` al mejor o mejores modelos de clasificación.

Modelo recomendado para optimización principal:

- Random Forest.

Modelos alternativos para optimización secundaria:

- SVM.
- Regresión logística.

Justificación:

| Modelo | Por qué optimizarlo |
|---|---|
| Random Forest | Tiene múltiples hiperparámetros que afectan sesgo, varianza y capacidad predictiva |
| SVM | El rendimiento depende de `C`, `kernel` y `gamma` |
| Regresión logística | Permite ajustar regularización y solver |

Ejemplo de grilla para Random Forest:

```python
param_grid_rf = {
    "modelo__n_estimators": [100, 200, 300],
    "modelo__max_depth": [None, 5, 10, 20],
    "modelo__min_samples_split": [2, 5, 10],
    "modelo__min_samples_leaf": [1, 2, 4],
    "modelo__class_weight": [None, "balanced"]
}
```

La métrica de optimización debe ser:

```python
scoring = "f1_macro"
```

---

## 15. Experimentos acumulados

### 15.1 Tabla maestra de experimentos

| Experimento | Descripción | Se conserva de iteración anterior | Métrica principal | Resultado esperado |
|---|---|---|---|---|
| Base | Preprocesamiento estándar + modelos iniciales | Sí | F1 macro / Silhouette | Línea base |
| PCA | Reducción de dimensionalidad con PCA | Sí | F1 macro / Silhouette | Comparación dimensional |
| TruncatedSVD | Reducción para matriz codificada | Sí | F1 macro / Silhouette | Comparación dimensional alternativa |
| Feature Engineering inicial | Variables creadas iniciales | Sí | F1 macro | Evaluar aporte de nuevas variables |
| Ordinal Encoding | Tratamiento ordinal de CAEC y CALC | Nuevo | F1 macro | Evaluar si mejora la representación |
| Feature Engineering ampliada | BMI + interacción FAF × FAVC + scores | Nuevo | F1 macro / importancia de variables | Evaluar aporte de dominio |
| CV estratificada | Validación robusta k=5 | Nuevo | F1 macro CV media | Reducir dependencia de split único |
| Optimización | GridSearchCV o RandomizedSearchCV | Nuevo | F1 macro CV | Mejorar modelo final |

---

## 16. FP-Growth y reglas de asociación

### 16.1 Preparación transaccional

El sistema debe discretizar variables numéricas y convertir categorías en ítems.

Ejemplos de ítems:

```text
Gender=Female
Age_Group=Young
BMI_Category=Obesity
FAVC=yes
CAEC=Sometimes
FAF=Low
NObeyesdad=Obesity_Type_I
```

### 16.2 Reglas requeridas

El sistema debe presentar:

- Reglas con mejores indicadores.
- 6 reglas novedosas.
- Lift en todas las reglas seleccionadas.

### 16.3 Tabla requerida para la PPT

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

## 17. Presentación nueva: estructura recomendada

La nueva PPT puede tener **17 diapositivas o más**, ya que la portada no cuenta como diapositiva explicativa. La prioridad debe ser explicar bien el trabajo y las iteraciones.

### 17.1 Estructura sugerida

| N° | Diapositiva | Contenido |
|---:|---|---|
| 0 | Portada | Título, curso, docente, estudiante, dataset |
| 1 | Objetivo del trabajo | Problema, objetivo general y métodos usados |
| 2 | Dataset | Fuente, registros, variables y variable objetivo |
| 3 | CRISP-DM | Fases usadas y utilidad concreta en la tarea |
| 4 | Comprensión de datos | Distribución de clases, tipos de variables y calidad de datos |
| 5 | Preparación de datos | Codificación, escalamiento, ordinalidad y partición train/test |
| 6 | Estrategia de clustering | Por qué no se asume K-Means automáticamente |
| 7 | Comparación de clustering | K-Means vs GMM vs Agglomerative vs DBSCAN si aplica |
| 8 | Clustering final | Algoritmo elegido, número de clusters y justificación |
| 9 | Interpretación de clusters | Perfiles encontrados y relación con niveles de obesidad |
| 10 | Clasificación base | Modelos comparados y métrica principal |
| 11 | Resultados de clasificación | Tabla de accuracy, recall, precision y F1 macro |
| 12 | Validación cruzada | Resultados con Stratified K-Fold k=5 |
| 13 | Optimización | Resultado antes/después de GridSearchCV o RandomizedSearchCV |
| 14 | Ingeniería de características | Variables creadas: BMI, interacción y scores |
| 15 | Importancia de atributos | Gráfico de importancia destacando variables creadas |
| 16 | FP-Growth | Reglas con mejores indicadores y Lift |
| 17 | 6 reglas novedosas | Interpretación breve de las reglas seleccionadas |
| 18 | Experimentos de reducción | PCA y TruncatedSVD: impacto en resultados |
| 19 | Descubrimientos principales | Al menos 3 hallazgos o métricas destacadas |
| 20 | Bibliografía y contraste | Comparación con al menos una fuente relacionada |
| 21 | Conclusiones y mejoras futuras | Decisión final, limitaciones y próximos pasos |
| 22 | Backoffice opcional | Solo si se implementa la app voluntaria |

---

## 18. Gráficos mínimos esperados

| Gráfico | Propósito | Ubicación sugerida |
|---|---|---|
| Distribución de `NObeyesdad` | Mostrar balance de clases | EDA |
| Heatmap o matriz de correlación numérica | Explorar relaciones entre variables continuas | EDA |
| PCA 2D coloreado por clase | Visualizar estructura general de datos | Clustering |
| PCA 2D coloreado por cluster | Evaluar separación visual de clusters | Clustering |
| Método del codo | Justificar número de clusters en K-Means | Clustering |
| Silhouette por k y algoritmo | Comparar clustering | Clustering |
| Matriz de confusión | Mostrar errores del mejor clasificador | Clasificación |
| Barras de métricas por modelo | Comparar clasificadores | Clasificación |
| Importancia de variables | Evaluar variables creadas | Ingeniería de características |
| Top reglas por Lift | Resumir FP-Growth | Asociación |

---

## 19. Mapeo contra rúbrica

| Criterio de rúbrica | Requisito para excelente | Evidencia en el proyecto |
|---|---|---|
| Completitud de tarea para la casa | Se usa agrupamiento, clasificación y asociación; se justifican métodos; se explican 6 reglas | Notebook, tablas de modelos, reglas FP-Growth y PPT |
| Comprensión del modelo y metodología | Se demuestra comprensión de algoritmos, métricas y CRISP-DM | Secciones de justificación y comparación |
| Análisis y transformación de datos | Se analizan y transforman datos; se aplican reducciones de dimensionalidad e ingeniería de características | EDA, PCA, TruncatedSVD, ordinal encoding y variables nuevas |
| Presentación de resultados | Resultados claros, concisos y visualmente atractivos | PPT extendida con gráficos y tablas |
| Interpretación y conclusiones | Interpretación fundamentada, patrones significativos y conclusiones | Hallazgos, bibliografía, discusión y mejoras futuras |

---

## 20. Criterios de aceptación

El proyecto se considera completo si:

- El dataset se carga desde `data\ObesityDataSet_raw_and_data_sinthetic.csv`.
- El notebook no oculta outputs importantes por truncamiento.
- Se usa CRISP-DM explícitamente.
- Se explica qué elementos de CRISP-DM fueron útiles.
- Se realiza EDA completo.
- Se justifica la elección del algoritmo de clustering.
- Se evalúa si K-Means es adecuado o no.
- Se comparan al menos 3 algoritmos de clustering.
- Se justifica el número de clusters.
- Se interpretan los clusters.
- Se entrenan varios modelos de clasificación.
- Se usa F1 macro como métrica principal.
- Se aplica validación cruzada estratificada k=5.
- Se aplica optimización de hiperparámetros.
- Se tratan variables ordinales como ordinales cuando corresponde.
- Se crean variables de ingeniería de características.
- Se incluye gráfico de importancia de atributos creados.
- Se aplica FP-Growth.
- Se mide Lift.
- Se explican reglas con mejores indicadores.
- Se explican 6 reglas novedosas.
- Se realizan experimentos de PCA y TruncatedSVD.
- Se resumen al menos 3 descubrimientos o métricas destacadas.
- Se compara al menos un hallazgo con bibliografía relacionada.
- Se entrega nueva PPT.
- Se entrega código reproducible.

---

## 21. Riesgos y mitigaciones

| Riesgo | Impacto | Mitigación |
|---|---:|---|
| K-Means no sea adecuado por geometría no globular | Alto | Comparar con GMM, Agglomerative y DBSCAN antes de seleccionar |
| La alta dimensionalidad por One-Hot afecte clustering | Alto | Evaluar PCA, TruncatedSVD y métricas de separación |
| Las variables ordinales se codifiquen como nominales | Medio | Aplicar ordinal encoding validando orden real de categorías |
| El modelo tenga buen accuracy pero mal rendimiento en clases minoritarias | Alto | Usar F1 macro, recall macro y matriz de confusión |
| El output del notebook se trunque | Medio | Configurar pandas display y exportar tablas completas |
| La ingeniería de características genere fuga de datos | Alto | Crear variables solo desde predictoras y dentro del flujo correcto |
| `BMI` domine demasiado la predicción | Medio | Reportar importancia de variables y discutir dependencia antropométrica |
| FP-Growth genere reglas obvias | Medio | Filtrar por Lift y seleccionar reglas novedosas además de las mejores métricas |
| La PPT quede demasiado cargada | Medio | Usar tablas resumen, gráficos clave y anexar detalles al código |

---

## 22. Decisiones técnicas esperadas

| Decisión | Criterio |
|---|---|
| Métrica principal de clasificación | F1 macro, por tratarse de clasificación multiclase |
| División de datos | Train/test estratificado y validación cruzada estratificada |
| Clustering final | Se elige después de comparar algoritmos y revisar interpretabilidad |
| Número de clusters | Se justifica por métricas y utilidad interpretativa |
| Variables ordinales | Se codifican respetando orden cuando representen frecuencia |
| Variables nuevas | Se crean con justificación de dominio e impacto en métricas |
| Modelo final | Se selecciona por rendimiento, estabilidad e interpretabilidad |

---

## 23. Estructura recomendada del notebook

```text
01_configuracion_visualizacion_outputs
02_importacion_librerias
03_carga_dataset
04_crisp_dm_comprension_problema
05_comprension_datos_eda
06_preparacion_datos_base
07_clustering_comparacion_algoritmos
08_clustering_modelo_final_interpretacion
09_clasificacion_base
10_validacion_cruzada_estratificada
11_optimizacion_hiperparametros
12_tratamiento_ordinal
13_ingenieria_caracteristicas
14_importancia_atributos_creados
15_pca_reduccion_dimensionalidad
16_truncated_svd_reduccion_dimensionalidad
17_fp_growth_reglas_asociacion
18_comparacion_iteraciones
19_descubrimientos_bibliografia
20_conclusiones_ppt
```

---

## 24. Prompt recomendado para el sistema de desarrollo

```md
Actúa como asistente de desarrollo para una tarea académica de Magíster en Data Science.

Usa este PRD como fuente principal. Debes construir un notebook reproducible usando el archivo:

data\ObesityDataSet_raw_and_data_sinthetic.csv

El proyecto debe seguir CRISP-DM y cumplir la rúbrica. Debe aplicar clustering, clasificación y FP-Growth. No debe asumir que K-Means es automáticamente el mejor clustering. Debe comparar K-Means, Gaussian Mixture, Agglomerative Clustering y DBSCAN si corresponde. Debe justificar si los datos tienen estructura globular o no, y elegir el algoritmo final según métricas e interpretabilidad.

Debe conservar las iteraciones anteriores y agregar una nueva iteración con:
1. Optimización de hiperparámetros con GridSearchCV o RandomizedSearchCV.
2. Tratamiento ordinal de variables como CAEC y CALC.
3. Ingeniería de características con BMI, interacción FAF × FAVC y scores de hábitos.
4. Validación cruzada estratificada k=5.

El código debe evitar outputs truncados. Configura pandas para mostrar todas las columnas relevantes, convierte reportes largos en DataFrames y exporta tablas completas a CSV cuando sea necesario.

La nueva PPT puede tener 17 diapositivas o más, sin contar portada. Debe incluir la justificación de modelos elegidos, comparación de clustering, resultados de clasificación, validación cruzada, optimización, FP-Growth, 6 reglas novedosas, 3 descubrimientos, bibliografía y gráfico de importancia de atributos creados.

Toda explicación debe redactarse en tercera persona para facilitar su uso en exposición.
```

---

## 25. Definition of Done

El proyecto estará listo cuando existan:

- Notebook ejecutable de inicio a fin.
- Configuración para evitar outputs truncados.
- CRISP-DM explicado.
- EDA completo.
- Clustering comparado y justificado.
- Modelo de clustering final seleccionado con evidencia.
- Clasificadores comparados.
- Validación cruzada estratificada.
- Optimización de hiperparámetros.
- Tratamiento ordinal.
- Ingeniería de características.
- Gráfico de importancia de atributos creados.
- FP-Growth con Lift.
- 6 reglas novedosas interpretadas.
- Comparación de iteraciones.
- 3 descubrimientos o métricas destacadas.
- Contraste con bibliografía.
- Nueva PPT extendida.
- Código entregable.
- Backoffice opcional si se busca puntaje adicional.
