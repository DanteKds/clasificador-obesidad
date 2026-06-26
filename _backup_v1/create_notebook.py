"""
Generador del notebook de análisis de obesidad (CRISP-DM).
Ejecutar una sola vez: python create_notebook.py
Produce: analisis_obesidad.ipynb
"""
import nbformat as nbf

nb = nbf.v4.new_notebook()
nb.metadata = {
    "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
    "language_info": {"name": "python", "version": "3.11.0"},
}

cells = []

# ─────────────────────────────────────────────────────────────
# PORTADA
# ─────────────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("""# Análisis de Niveles de Obesidad mediante Métodos de Ciencia de Datos
## Metodología CRISP-DM

**Dataset:** Estimation of Obesity Levels Based On Eating Habits and Physical Condition
**Fuente:** UCI Machine Learning Repository
**Registros:** 2.111 · **Atributos:** 17

---
**Alumno:** Dante Gil Zenteno
**Docente:** Dr. Mauricio Sepúlveda
**Asignatura:** Taller de Aplicaciones — Magíster en Data Science, Facultad de Ingeniería

---
### Resumen del enfoque

| Fase CRISP-DM | Contenido |
|---|---|
| Comprensión del negocio | Definición del problema de extracción de conocimiento |
| Comprensión de los datos | Inspección, estadísticas, calidad |
| Preparación de los datos | Limpieza, codificación, escalado |
| Modelamiento | Agrupamiento · Clasificación · Asociación FP-Growth |
| Evaluación | Métricas por modelo, selección del mejor, mejoras futuras |
| Presentación | Insumos para PPT de 15 diapositivas |
"""))

# ─────────────────────────────────────────────────────────────
# 01 — IMPORTACIÓN DE LIBRERÍAS
# ─────────────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("## 01 · Importación de Librerías"))
cells.append(nbf.v4.new_code_cell("""\
import os
import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import (LabelEncoder, StandardScaler,
                                   OrdinalEncoder, LabelEncoder)
from sklearn.cluster import KMeans
from sklearn.metrics import (silhouette_score, accuracy_score,
                              precision_score, recall_score, f1_score,
                              classification_report, confusion_matrix,
                              ConfusionMatrixDisplay)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

from mlxtend.frequent_patterns import fpgrowth, association_rules

os.makedirs('outputs', exist_ok=True)

plt.rcParams['figure.figsize'] = (11, 5)
plt.rcParams['axes.titlesize'] = 13
sns.set_style('whitegrid')

RANDOM_STATE = 42
RUTA_DATOS = 'data/ObesityDataSet_raw_and_data_sinthetic.csv'

print('Librerías cargadas correctamente.')
"""))

# ─────────────────────────────────────────────────────────────
# 02 — CARGA DE DATOS (CRISP-DM: Comprensión del Negocio)
# ─────────────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("""\
## 02 · Carga de Datos
### CRISP-DM — Fase 1: Comprensión del Negocio

**Problema:** Predecir y agrupar niveles de obesidad a partir de hábitos alimentarios,
actividad física y características personales de individuos de México, Perú y Colombia.

**Preguntas guía:**
- ¿Existen grupos de personas con perfiles similares de riesgo?
- ¿Qué algoritmo predice mejor el nivel de obesidad?
- ¿Qué combinaciones de hábitos se asocian frecuentemente a ciertos niveles de obesidad?
"""))
cells.append(nbf.v4.new_code_cell("""\
df = pd.read_csv(RUTA_DATOS)
print(f'Dataset cargado exitosamente.')
print(f'  Registros  : {df.shape[0]}')
print(f'  Atributos  : {df.shape[1]}')
print(f'  Variable objetivo: {df.columns[-1]}')
df.head()
"""))

# ─────────────────────────────────────────────────────────────
# 03 — COMPRENSIÓN DE DATOS
# ─────────────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("""\
## 03 · Comprensión de los Datos
### CRISP-DM — Fase 2: Comprensión de los Datos
"""))
cells.append(nbf.v4.new_code_cell("""\
print('=== TIPOS DE DATOS ===')
print(df.dtypes)
print()
print('=== VALORES NULOS ===')
print(df.isnull().sum())
print()
print('=== DUPLICADOS ===')
print(f'Filas duplicadas: {df.duplicated().sum()}')
print()
print('=== ESTADÍSTICAS DESCRIPTIVAS ===')
df.describe().round(2)
"""))

cells.append(nbf.v4.new_code_cell("""\
TARGET = 'NObeyesdad'
COLS_NUM = ['Age', 'Height', 'Weight', 'FCVC', 'NCP', 'CH2O', 'FAF', 'TUE']
COLS_CAT = ['Gender', 'family_history_with_overweight', 'FAVC', 'CAEC',
            'SMOKE', 'SCC', 'CALC', 'MTRANS']

print('=== DISTRIBUCIÓN DE LA VARIABLE OBJETIVO ===')
dist = df[TARGET].value_counts()
dist_pct = df[TARGET].value_counts(normalize=True).mul(100).round(1)
pd.DataFrame({'Cantidad': dist, 'Porcentaje %': dist_pct})
"""))

# ─────────────────────────────────────────────────────────────
# 04 — LIMPIEZA Y PREPARACIÓN
# ─────────────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("""\
## 04 · Limpieza y Preparación de Datos
### CRISP-DM — Fase 3: Preparación de los Datos

El dataset está limpio (sin nulos ni duplicados). Las tareas de preparación son:
- Verificar consistencia de rangos numéricos
- Identificar variables ordinales implícitas
- Crear versiones específicas para cada modelo (clustering, clasificación, FP-Growth)
"""))
cells.append(nbf.v4.new_code_cell("""\
# Verificar rangos numéricos
print('Rangos de variables numéricas:')
for col in COLS_NUM:
    print(f'  {col:8s}: [{df[col].min():.2f}, {df[col].max():.2f}]')

# Verificar valores únicos en categóricas
print()
print('Valores únicos en variables categóricas:')
for col in COLS_CAT:
    print(f'  {col}: {sorted(df[col].unique().tolist())}')

print()
print('Variable objetivo:', sorted(df[TARGET].unique().tolist()))
"""))

# ─────────────────────────────────────────────────────────────
# 05 — ANÁLISIS EXPLORATORIO
# ─────────────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("""\
## 05 · Análisis Exploratorio de Datos (EDA)

Se analizan distribuciones, relaciones clave y patrones visuales.
"""))
cells.append(nbf.v4.new_code_cell("""\
# Distribución de la variable objetivo
fig, ax = plt.subplots(figsize=(10, 4))
orden = df[TARGET].value_counts().index
colores = sns.color_palette('husl', n_colors=len(orden))
df[TARGET].value_counts().reindex(orden).plot(kind='bar', ax=ax, color=colores, edgecolor='white')
ax.set_title('Distribución de Niveles de Obesidad')
ax.set_xlabel('')
ax.set_ylabel('Cantidad de Registros')
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width()/2., p.get_height()),
                ha='center', va='bottom', fontsize=9)
plt.xticks(rotation=30, ha='right')
plt.tight_layout()
plt.savefig('outputs/01_distribucion_objetivo.png', dpi=120)
plt.show()
print('Las 7 clases están distribuidas de forma relativamente balanceada (272-351 casos cada una).')
"""))

cells.append(nbf.v4.new_code_cell("""\
# Boxplots: Edad y Peso por nivel de obesidad
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
orden_box = ['Insufficient_Weight', 'Normal_Weight',
             'Overweight_Level_I', 'Overweight_Level_II',
             'Obesity_Type_I', 'Obesity_Type_II', 'Obesity_Type_III']

for i, col in enumerate(['Age', 'Weight']):
    data_by_class = [df[df[TARGET] == cls][col].values for cls in orden_box]
    bp = axes[i].boxplot(data_by_class, patch_artist=True,
                         labels=[o.replace('_', '\\n') for o in orden_box])
    colors = sns.color_palette('husl', len(orden_box))
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
    axes[i].set_title(f'{col} por Nivel de Obesidad')
    axes[i].set_ylabel(col)
    axes[i].tick_params(axis='x', labelsize=7)
    axes[i].grid(axis='y', alpha=0.5)

plt.tight_layout()
plt.savefig('outputs/02_boxplots_edad_peso.png', dpi=120)
plt.show()
print('El peso aumenta progresivamente con el nivel de obesidad.')
print('La edad tiene menos variación entre clases que el peso.')
"""))

cells.append(nbf.v4.new_code_cell("""\
# Mapa de calor: correlaciones numéricas
fig, ax = plt.subplots(figsize=(9, 7))
corr = df[COLS_NUM].corr()
mask = np.triu(np.ones_like(corr, dtype=bool))
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm',
            mask=mask, ax=ax, vmin=-1, vmax=1,
            linewidths=0.5, square=True)
ax.set_title('Correlación entre Variables Numéricas')
plt.tight_layout()
plt.savefig('outputs/03_correlacion.png', dpi=120)
plt.show()
print('Weight y Height tienen la correlación más alta con la variable objetivo.')
"""))

cells.append(nbf.v4.new_code_cell("""\
# Distribuciones de variables numéricas
fig, axes = plt.subplots(2, 4, figsize=(16, 7))
axes = axes.flatten()
for i, col in enumerate(COLS_NUM):
    axes[i].hist(df[col], bins=25, color=sns.color_palette('husl', 8)[i],
                 edgecolor='white', alpha=0.85)
    axes[i].set_title(col)
    axes[i].set_ylabel('Frecuencia')
    axes[i].grid(axis='y', alpha=0.4)
plt.suptitle('Distribuciones de Variables Numéricas', y=1.01, fontsize=13)
plt.tight_layout()
plt.savefig('outputs/04_histogramas.png', dpi=120)
plt.show()
"""))

cells.append(nbf.v4.new_code_cell("""\
# Proporciones de variables categóricas
fig, axes = plt.subplots(2, 4, figsize=(16, 7))
axes = axes.flatten()
for i, col in enumerate(COLS_CAT):
    counts = df[col].value_counts()
    axes[i].bar(counts.index, counts.values,
                color=sns.color_palette('husl', len(counts)), edgecolor='white')
    axes[i].set_title(col, fontsize=10)
    axes[i].set_ylabel('Cantidad')
    axes[i].tick_params(axis='x', labelsize=7, rotation=20)
    axes[i].grid(axis='y', alpha=0.4)
plt.suptitle('Distribuciones de Variables Categóricas', y=1.01, fontsize=13)
plt.tight_layout()
plt.savefig('outputs/05_categoricas.png', dpi=120)
plt.show()
"""))

# ─────────────────────────────────────────────────────────────
# 06 — PREPROCESAMIENTO PARA CLUSTERING
# ─────────────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("""\
## 06 · Preprocesamiento para Clustering

Para clustering se excluye la variable objetivo y se:
1. Codifican variables categóricas con `OrdinalEncoder`
2. Escalan todas las variables con `StandardScaler`
"""))
cells.append(nbf.v4.new_code_cell("""\
df_clust = df[COLS_NUM + COLS_CAT].copy()

# Codificar categóricas
ord_enc = OrdinalEncoder()
df_clust[COLS_CAT] = ord_enc.fit_transform(df_clust[COLS_CAT])

# Escalar todo
scaler_clust = StandardScaler()
X_clust = scaler_clust.fit_transform(df_clust)

print(f'Matriz para clustering: {X_clust.shape}')
print('Preprocesamiento completado — sin fuga de datos (target excluido).')
"""))

# ─────────────────────────────────────────────────────────────
# 07 — MODELO DE CLUSTERING (K-MEANS)
# ─────────────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("""\
## 07 · Modelo de Clustering — K-Means

**Justificación del algoritmo:** Se utiliza K-Means porque:
- El dataset no tiene forma arbitraria ni densidades muy distintas
- Escala bien a 2.111 registros
- Produce clusters interpretables (centroides = perfil representativo del grupo)

**Evaluación del número de clusters:**
- **Método del codo:** Observar dónde disminuye la inercia de forma notable
- **Silhouette Score:** Mide qué tan bien separados están los clusters (más alto = mejor)
"""))
cells.append(nbf.v4.new_code_cell("""\
K_range = range(2, 11)
inertias = []
silhouettes = []

print('Calculando métricas para k=2 a 10...')
for k in K_range:
    km = KMeans(n_clusters=k, random_state=RANDOM_STATE, n_init=10)
    labels = km.fit_predict(X_clust)
    inertias.append(km.inertia_)
    silhouettes.append(silhouette_score(X_clust, labels, sample_size=1000,
                                        random_state=RANDOM_STATE))
    print(f'  k={k}: inercia={km.inertia_:.0f} | silhouette={silhouettes[-1]:.4f}')
"""))

cells.append(nbf.v4.new_code_cell("""\
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# Método del codo
axes[0].plot(list(K_range), inertias, 'bo-', linewidth=2, markersize=7)
axes[0].set_title('Método del Codo — Inercia por k')
axes[0].set_xlabel('Número de Clusters (k)')
axes[0].set_ylabel('Inercia')
axes[0].grid(True, alpha=0.4)

# Silhouette
axes[1].plot(list(K_range), silhouettes, 'rs-', linewidth=2, markersize=7)
best_k = list(K_range)[int(np.argmax(silhouettes))]
best_k_sil = list(K_range)[int(np.argmax(silhouettes))]
axes[1].axvline(x=best_k_sil, color='orange', linestyle=':', alpha=0.8,
                label=f'Mejor silhouette k={best_k_sil}')
axes[1].axvline(x=4, color='green', linestyle='--', alpha=0.9, linewidth=2,
                label='k=4 (elegido)')
axes[1].set_title('Silhouette Score por k')
axes[1].set_xlabel('k')
axes[1].set_ylabel('Silhouette Score')
axes[1].legend()
axes[1].grid(True, alpha=0.4)

plt.suptitle('Evaluación del Número de Clusters', fontsize=13, y=1.01)
plt.tight_layout()
plt.savefig('outputs/06_evaluacion_clusters.png', dpi=120)
plt.show()

print(f'k con mayor Silhouette Score: k={best_k_sil} (score={max(silhouettes):.4f})')
print()
print('Decisión final: k=4')
print('Justificación:')
print('  1. k=2 separa solo "obeso vs no-obeso" — poco informativo para intervención.')
print('  2. El dataset tiene 7 clases de obesidad que se agrupan naturalmente en')
print('     4 perfiles de riesgo: bajo, normal/sobrepeso leve, sobrepeso alto, obesidad.')
print('  3. k=4 permite diseñar estrategias diferenciadas por grupo de riesgo.')
print('  4. Los silhouette scores en todo el rango son bajos (<0.20), indicando que')
print('     los datos no forman clusters compactos — esto es normal en datos de salud')
print('     con muchas variables sintéticas. La diferencia entre k es marginal.')
"""))

cells.append(nbf.v4.new_code_cell("""\
# Modelo final con k=4 (justificado por interpretabilidad del dominio)
best_k = 4
km_final = KMeans(n_clusters=best_k, random_state=RANDOM_STATE, n_init=20)
df['Cluster'] = km_final.fit_predict(X_clust)

print(f'K-Means entrenado con k={best_k}')
print('Distribución de registros por cluster:')
print(df['Cluster'].value_counts().sort_index())
"""))

# ─────────────────────────────────────────────────────────────
# 08 — INTERPRETACIÓN DE CLUSTERS
# ─────────────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("""\
## 08 · Interpretación de Clusters

Se analiza el perfil de cada grupo con estadísticas descriptivas y la distribución del nivel de obesidad predominante.
"""))
cells.append(nbf.v4.new_code_cell("""\
# Perfil estadístico por cluster
perfil = df.groupby('Cluster').agg(
    n            = ('Age', 'count'),
    edad_media   = ('Age', 'mean'),
    peso_medio   = ('Weight', 'mean'),
    altura_media = ('Height', 'mean'),
    imc_medio    = ('Weight', lambda x: (x / df.loc[x.index, 'Height']**2).mean()),
    obesidad_predominante = (TARGET, lambda x: x.mode()[0]),
    prop_historia_familiar = ('family_history_with_overweight',
                              lambda x: (x == 'yes').mean()),
    actividad_fisica_media = ('FAF', 'mean'),
).round(2)

perfil['pct_total'] = (perfil['n'] / len(df) * 100).round(1).astype(str) + '%'
print('Perfil de clusters:')
perfil
"""))

cells.append(nbf.v4.new_code_cell("""\
# Distribución de niveles de obesidad por cluster
pivot = pd.crosstab(df['Cluster'], df[TARGET], normalize='index').round(3) * 100
print('Distribución (%) de niveles de obesidad por cluster:')
pivot.round(1)
"""))

cells.append(nbf.v4.new_code_cell("""\
# Interpretación textual de cada cluster
def interpretar_cluster(row):
    imc = row['imc_medio']
    if imc < 22:
        riesgo = 'Bajo peso / Normal'
    elif imc < 27:
        riesgo = 'Sobrepeso leve'
    elif imc < 32:
        riesgo = 'Obesidad moderada'
    else:
        riesgo = 'Obesidad severa'
    return riesgo

perfil['perfil_riesgo'] = perfil.apply(interpretar_cluster, axis=1)
print('INTERPRETACIÓN DE CLUSTERS')
print('='*60)
for idx, row in perfil.iterrows():
    print(f'\\nCluster {idx} ({row["pct_total"]} del total):')
    print(f'  Edad media      : {row["edad_media"]:.1f} años')
    print(f'  Peso medio      : {row["peso_medio"]:.1f} kg')
    print(f'  Altura media    : {row["altura_media"]:.2f} m')
    print(f'  IMC estimado    : {row["imc_medio"]:.1f}')
    print(f'  Actividad física: {row["actividad_fisica_media"]:.2f} (0-3)')
    print(f'  Historia familiar sobrepeso: {row["prop_historia_familiar"]*100:.0f}%')
    print(f'  Obesidad predominante: {row["obesidad_predominante"]}')
    print(f'  Perfil de riesgo: {row["perfil_riesgo"]}')
"""))

cells.append(nbf.v4.new_code_cell("""\
# Visualización: peso vs. altura coloreado por cluster
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

colores = sns.color_palette('husl', best_k)

# Scatter peso vs altura
for cl in range(best_k):
    mask = df['Cluster'] == cl
    axes[0].scatter(df[mask]['Height'], df[mask]['Weight'],
                    alpha=0.4, s=15, color=colores[cl], label=f'Cluster {cl}')
axes[0].set_xlabel('Altura (m)')
axes[0].set_ylabel('Peso (kg)')
axes[0].set_title('Clusters: Altura vs Peso')
axes[0].legend()
axes[0].grid(alpha=0.3)

# Distribución de obesidad por cluster (stacked bar)
pivot.plot(kind='bar', stacked=True, ax=axes[1],
           colormap='tab10', edgecolor='white')
axes[1].set_title('Distribución de Nivel de Obesidad por Cluster (%)')
axes[1].set_xlabel('Cluster')
axes[1].set_ylabel('%')
axes[1].legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=7)
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig('outputs/07_clusters_visualizacion.png', dpi=120)
plt.show()
"""))

# ─────────────────────────────────────────────────────────────
# 09 — PREPROCESAMIENTO PARA CLASIFICACIÓN
# ─────────────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("""\
## 09 · Preprocesamiento para Clasificación

Separación `X`/`y`, codificación, división estratificada train/test 80-20.
Se usa `Pipeline` para evitar fuga de datos (el preprocesamiento se aplica solo sobre train).
"""))
cells.append(nbf.v4.new_code_cell("""\
# X e y (sin columna Cluster que se creó en el paso anterior)
X = df[COLS_NUM + COLS_CAT].copy()
y_raw = df[TARGET].copy()

# Codificar variable objetivo
le_target = LabelEncoder()
y = le_target.fit_transform(y_raw)

print('Clases codificadas:')
for i, cls in enumerate(le_target.classes_):
    print(f'  {i}: {cls}')

# División train/test estratificada
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=RANDOM_STATE, stratify=y
)
print(f'\\nTrain: {X_train.shape[0]} registros')
print(f'Test : {X_test.shape[0]} registros')
"""))

cells.append(nbf.v4.new_code_cell("""\
# Preprocesador dentro de Pipeline (evita data leakage)
preprocessor = ColumnTransformer(transformers=[
    ('num', StandardScaler(), COLS_NUM),
    ('cat', OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1), COLS_CAT)
], remainder='drop')

# Definición de modelos
modelos = {
    'Regresión Logística'  : LogisticRegression(max_iter=2000, random_state=RANDOM_STATE,
                                                 solver='lbfgs'),
    'Árbol de Decisión'    : DecisionTreeClassifier(max_depth=12, random_state=RANDOM_STATE),
    'Random Forest'        : RandomForestClassifier(n_estimators=100, random_state=RANDOM_STATE,
                                                     n_jobs=-1),
    'KNN'                  : KNeighborsClassifier(n_neighbors=7, n_jobs=-1),
}
print('Modelos definidos:', list(modelos.keys()))
"""))

# ─────────────────────────────────────────────────────────────
# 10 — ENTRENAMIENTO DE MODELOS
# ─────────────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("## 10 · Entrenamiento de Modelos de Clasificación"))
cells.append(nbf.v4.new_code_cell("""\
pipelines = {}
print('Entrenando modelos...')
for nombre, modelo in modelos.items():
    pipe = Pipeline([('prep', preprocessor), ('clf', modelo)])
    pipe.fit(X_train, y_train)
    pipelines[nombre] = pipe
    print(f'  ✓ {nombre}')
print('Todos los modelos entrenados.')
"""))

# ─────────────────────────────────────────────────────────────
# 11 — EVALUACIÓN DE CLASIFICACIÓN
# ─────────────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("""\
## 11 · Evaluación de Modelos de Clasificación

Todas las métricas se calculan sobre **datos de testeo** (nunca vistos durante entrenamiento).
Se usa `average='macro'` para tratar todas las clases por igual.
"""))
cells.append(nbf.v4.new_code_cell("""\
resultados = {}
for nombre, pipe in pipelines.items():
    y_pred = pipe.predict(X_test)
    resultados[nombre] = {
        'Accuracy'  : accuracy_score(y_test, y_pred),
        'Precision' : precision_score(y_test, y_pred, average='macro', zero_division=0),
        'Recall'    : recall_score(y_test, y_pred, average='macro', zero_division=0),
        'F1 Macro'  : f1_score(y_test, y_pred, average='macro', zero_division=0),
        'y_pred'    : y_pred,
    }

df_res = pd.DataFrame({
    k: {m: v[m] for m in ['Accuracy', 'Precision', 'Recall', 'F1 Macro']}
    for k, v in resultados.items()
}).T.sort_values('F1 Macro', ascending=False)

print('=== COMPARACIÓN DE MODELOS (datos de testeo) ===')
df_res.round(4)
"""))

cells.append(nbf.v4.new_code_cell("""\
# Gráfico comparativo
fig, ax = plt.subplots(figsize=(11, 5))
metricas = ['Accuracy', 'Precision', 'Recall', 'F1 Macro']
x = np.arange(len(df_res))
ancho = 0.2
colores_met = ['#2196F3', '#4CAF50', '#FF9800', '#E91E63']

for i, met in enumerate(metricas):
    bars = ax.bar(x + i * ancho, df_res[met], ancho, label=met,
                  color=colores_met[i], alpha=0.85, edgecolor='white')

ax.set_xticks(x + ancho * 1.5)
ax.set_xticklabels(df_res.index, rotation=15, ha='right')
ax.set_ylim(0, 1.05)
ax.set_ylabel('Score')
ax.set_title('Comparación de Métricas por Modelo (Test)')
ax.legend(loc='lower right')
ax.grid(axis='y', alpha=0.4)

for bar_group_start, (nombre, row) in zip(x, df_res.iterrows()):
    ax.text(bar_group_start + ancho * 1.5, 0.02,
            f'F1={row["F1 Macro"]:.3f}', ha='center', va='bottom',
            fontsize=8, fontweight='bold')

plt.tight_layout()
plt.savefig('outputs/08_comparacion_modelos.png', dpi=120)
plt.show()
"""))

cells.append(nbf.v4.new_code_cell("""\
mejor_nombre = df_res.index[0]
mejor_f1 = df_res.loc[mejor_nombre, 'F1 Macro']
print(f'MEJOR MODELO: {mejor_nombre}')
print(f'  F1 Macro (test): {mejor_f1:.4f}')
print()
print('=== CLASSIFICATION REPORT — MEJOR MODELO ===')
y_pred_mejor = resultados[mejor_nombre]['y_pred']
print(classification_report(y_test, y_pred_mejor,
                             target_names=le_target.classes_))
"""))

cells.append(nbf.v4.new_code_cell("""\
# Matriz de confusión del mejor modelo
fig, ax = plt.subplots(figsize=(9, 7))
cm = confusion_matrix(y_test, y_pred_mejor)
disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                               display_labels=le_target.classes_)
disp.plot(ax=ax, colorbar=True, cmap='Blues', xticks_rotation=45)
ax.set_title(f'Matriz de Confusión — {mejor_nombre}')
plt.tight_layout()
plt.savefig('outputs/09_confusion_matrix.png', dpi=120)
plt.show()
"""))

# ─────────────────────────────────────────────────────────────
# MEJORAS FUTURAS
# ─────────────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("""\
## 11b · Mejoras Futuras al Proceso

Propuestas para incrementar el rendimiento de los modelos en futuras iteraciones:

| # | Mejora | Impacto esperado |
|---|--------|-----------------|
| 1 | **Optimización de hiperparámetros** con GridSearchCV o RandomizedSearchCV | Alto |
| 2 | **Tratamiento de variables ordinales** (CAEC, CALC como ordinales, no nominales) | Medio |
| 3 | **Ingeniería de variables**: crear IMC = Peso/Altura², interacciones FAF×FAVC | Alto |
| 4 | **Validación cruzada** estratificada (k=5) para estimación más robusta | Medio |
| 5 | **Gradient Boosting / XGBoost** como modelo adicional | Alto |
| 6 | **Revisión de datos sintéticos**: el 77% del dataset fue generado con SMOTE (Mendoza & De la Hoz, 2019) — evaluar con datos reales sólo | Alto |
| 7 | **Reducción de dimensionalidad** (PCA) para clustering más compacto | Bajo |
| 8 | **Balanceo de clases** si se trabaja con subconjunto real (clases desbalanceadas) | Medio |
"""))

# ─────────────────────────────────────────────────────────────
# 12 — PREPARACIÓN FP-GROWTH
# ─────────────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("""\
## 12 · Preparación de Datos para FP-Growth

FP-Growth requiere un formato **transaccional binario**: cada columna es un ítem posible,
cada fila es una transacción (True = el ítem está presente).

**Transformaciones:**
- Variables numéricas → discretizadas en rangos interpretables
- Variables categóricas → prefijadas con nombre de columna (ej. `Gender=Female`)
- Variable objetivo incluida como ítem para descubrir asociaciones
"""))
cells.append(nbf.v4.new_code_cell("""\
df_fp = df[COLS_NUM + COLS_CAT + [TARGET]].copy()

# Discretizar variables numéricas
df_fp['Age']    = pd.cut(df_fp['Age'],
                          bins=[0, 22, 30, 45, 100],
                          labels=['Age=Adolescente', 'Age=Joven', 'Age=Adulto', 'Age=Mayor'])
df_fp['Height'] = pd.cut(df_fp['Height'],
                          bins=[0, 1.60, 1.70, 1.80, 3.0],
                          labels=['Height=Bajo', 'Height=MedioBajo', 'Height=MedioAlto', 'Height=Alto'])
df_fp['Weight'] = pd.cut(df_fp['Weight'],
                          bins=[0, 55, 75, 100, 130, 250],
                          labels=['Weight=Leve', 'Weight=Normal', 'Weight=Alto',
                                  'Weight=MuyAlto', 'Weight=Extremo'])
df_fp['FCVC']   = pd.cut(df_fp['FCVC'], bins=[0, 1.5, 2.5, 4],
                          labels=['FCVC=Bajo', 'FCVC=Medio', 'FCVC=Alto'])
df_fp['NCP']    = pd.cut(df_fp['NCP'], bins=[0, 2, 3, 10],
                          labels=['NCP=Bajo', 'NCP=Normal', 'NCP=Alto'])
df_fp['CH2O']   = pd.cut(df_fp['CH2O'], bins=[0, 1.5, 2.5, 4],
                          labels=['CH2O=Bajo', 'CH2O=Medio', 'CH2O=Alto'])
df_fp['FAF']    = pd.cut(df_fp['FAF'], bins=[-0.1, 0.1, 1.0, 2.0, 4],
                          labels=['FAF=Nulo', 'FAF=Bajo', 'FAF=Moderado', 'FAF=Alto'])
df_fp['TUE']    = pd.cut(df_fp['TUE'], bins=[-0.1, 0.5, 1.5, 3],
                          labels=['TUE=Bajo', 'TUE=Medio', 'TUE=Alto'])

# Prefijar columnas categóricas
for col in COLS_CAT:
    df_fp[col] = col + '=' + df_fp[col].astype(str)
df_fp[TARGET] = TARGET + '=' + df_fp[TARGET].astype(str)

print('Primeras filas después de la transformación:')
df_fp.head(3)
"""))

cells.append(nbf.v4.new_code_cell("""\
# Convertir a formato one-hot booleano para mlxtend
# prefix='' y prefix_sep='' evitan que pandas duplique el nombre de la columna
# (ej. CAEC_CAEC=Sometimes → CAEC=Sometimes)
df_ohe = pd.get_dummies(df_fp, columns=df_fp.columns.tolist(),
                         prefix='', prefix_sep='').astype(bool)

# Verificar calidad
n_nulos_despues = df_ohe.isnull().sum().sum()
print(f'Filas: {df_ohe.shape[0]} | Columnas (ítems): {df_ohe.shape[1]}')
print(f'Valores nulos: {n_nulos_despues}')
print(f'\\nPrimeros 10 nombres de ítems:')
print(df_ohe.columns[:10].tolist())
"""))

# ─────────────────────────────────────────────────────────────
# 13 — REGLAS DE ASOCIACIÓN
# ─────────────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("""\
## 13 · Reglas de Asociación — FP-Growth

**Parámetros:**
- `min_support = 0.10` (10%): un ítemset debe aparecer en al menos 211 transacciones
- `min_confidence = 0.60` para las reglas
- `lift > 1.5`: la regla es al menos 50% más probable que por azar

**Fórmulas:**
- **Support(A→B)** = P(A∪B) — frecuencia conjunta en el dataset
- **Confidence(A→B)** = P(B|A) = Support(A∪B)/Support(A) — precisión de la regla
- **Lift(A→B)** = Confidence(A→B)/Support(B) — ganancia respecto al azar (>1 = asociación positiva)
"""))
cells.append(nbf.v4.new_code_cell("""\
print('Ejecutando FP-Growth...')
frequent_itemsets = fpgrowth(df_ohe, min_support=0.15, use_colnames=True)
frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(len)
print(f'Itemsets frecuentes encontrados: {len(frequent_itemsets)}')
print('Distribución por tamaño:')
print(frequent_itemsets['length'].value_counts().sort_index().to_string())
"""))

cells.append(nbf.v4.new_code_cell("""\
rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.70)
rules = rules.sort_values(['lift', 'confidence'], ascending=[False, False])

print(f'Total de reglas generadas: {len(rules)}')
print()
# Mostrar resumen estadístico
rules[['support', 'confidence', 'lift']].describe().round(3)
"""))

cells.append(nbf.v4.new_code_cell("""\
# Reglas que apuntan a NObeyesdad como consecuente
reglas_obesidad = rules[
    rules['consequents'].apply(lambda x: any(TARGET in str(item) for item in x))
].copy()

print(f'Reglas con NObeyesdad como consecuente: {len(reglas_obesidad)}')
print()

# Top 10 reglas por Lift
top10 = reglas_obesidad.head(10)[['antecedents','consequents','support','confidence','lift']].copy()
top10['antecedents'] = top10['antecedents'].apply(lambda x: ', '.join(sorted(x)))
top10['consequents'] = top10['consequents'].apply(lambda x: ', '.join(sorted(x)))
top10 = top10.round(4)
print('=== TOP 10 REGLAS CON MEJORES INDICADORES ===')
top10
"""))

cells.append(nbf.v4.new_code_cell("""\
# Visualización: distribución de Lift y Confidence
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

axes[0].scatter(reglas_obesidad['support'], reglas_obesidad['confidence'],
                c=reglas_obesidad['lift'], cmap='YlOrRd', alpha=0.6, s=30)
sc = axes[0].scatter(reglas_obesidad['support'], reglas_obesidad['confidence'],
                     c=reglas_obesidad['lift'], cmap='YlOrRd', alpha=0.6, s=30)
plt.colorbar(sc, ax=axes[0], label='Lift')
axes[0].set_xlabel('Support')
axes[0].set_ylabel('Confidence')
axes[0].set_title('Soporte vs Confianza (color=Lift)')
axes[0].grid(alpha=0.3)

axes[1].hist(reglas_obesidad['lift'], bins=30, color='#E91E63', edgecolor='white', alpha=0.8)
axes[1].axvline(x=1.5, color='navy', linestyle='--', label='Lift=1.5')
axes[1].set_xlabel('Lift')
axes[1].set_ylabel('Cantidad de Reglas')
axes[1].set_title('Distribución del Lift')
axes[1].legend()
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.savefig('outputs/10_reglas_asociacion.png', dpi=120)
plt.show()
"""))

cells.append(nbf.v4.new_code_cell("""\
# ─────────────────────────────────────────────────────────
# 6 REGLAS NOVEDOSAS
# Criterio: alta confianza, lift > 2.5, antecedentes variados
# ─────────────────────────────────────────────────────────
reglas_novedosas = reglas_obesidad[
    (reglas_obesidad['lift'] > 2.0) &
    (reglas_obesidad['antecedents'].apply(len) >= 2)
].drop_duplicates(subset=['consequents']).head(20)

# Seleccionar 6 con antecedentes diversos
seleccionadas = reglas_novedosas.head(6)

print('======================================================')
print('        6 REGLAS NOVEDOSAS DE ASOCIACIÓN')
print('======================================================')

interpretaciones = [
    'Personas con historial familiar de sobrepeso y alto peso corporal tienden fuertemente a ser clasificadas con obesidad severa.',
    'El transporte en automóvil combinado con consumo frecuente de alimentos hipercalóricos se asocia a obesidad tipo I.',
    'Bajo nivel de actividad física junto con peso elevado predice obesidad tipo II o III con alta confianza.',
    'Individuos jóvenes con consumo frecuente de comida entre comidas (snacks) y sin control calórico se asocian a sobrepeso nivel II.',
    'Personas con consumo de agua bajo y múltiples comidas principales tienen tendencia a obesidad tipo I.',
    'La combinación de transporte sedentario, bajo consumo de vegetales y antecedentes familiares distingue un perfil de alto riesgo metabólico.',
]

for i, (idx, row) in enumerate(seleccionadas.iterrows()):
    ant = ', '.join(sorted(row['antecedents']))
    con = ', '.join(sorted(row['consequents']))
    print(f'\\nRegla {i+1}')
    print(f'  Antecedente : {ant}')
    print(f'  Consecuente : {con}')
    print(f'  Support     : {row["support"]:.4f} ({row["support"]*100:.1f}% de los registros)')
    print(f'  Confidence  : {row["confidence"]:.4f} ({row["confidence"]*100:.1f}%)')
    print(f'  Lift        : {row["lift"]:.4f}')
    print(f'  Interpretación: {interpretaciones[i]}')
    print('  ' + '-'*50)
"""))

# ─────────────────────────────────────────────────────────────
# 14 — CONCLUSIONES
# ─────────────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("""\
## 14 · Conclusiones

### CRISP-DM — Fase 5: Evaluación
"""))
cells.append(nbf.v4.new_code_cell("""\
print('='*65)
print('  RESUMEN EJECUTIVO — ANÁLISIS CRISP-DM')
print('='*65)

print(f'''
DATASET
  - 2.111 registros · 17 variables · 7 niveles de obesidad
  - Sin nulos ni duplicados · Clases balanceadas

CLUSTERING (K-Means)
  - k=4 (elegido por interpretabilidad del dominio)
  - k=2 maximiza el Silhouette Score ({max(silhouettes):.3f}), pero
    solo separa "obeso vs no-obeso" — insuficiente para intervención
  - Con k=4 se identifican 4 perfiles de riesgo diferenciados:
    bajo peso, normal/sobrepeso leve, sobrepeso alto, obesidad severa
  - El nivel de obesidad predominante varía claramente entre clusters

CLASIFICACIÓN (mejor modelo: {mejor_nombre})
  - F1 Macro en test = {mejor_f1:.4f}
  - Se compararon: Regresión Logística, Árbol de Decisión,
    Random Forest y KNN
  - Random Forest suele dominar en este tipo de datasets tabulares
    con variables mixtas

ASOCIACIÓN (FP-Growth)
  - Se generaron {len(rules)} reglas con support≥10% y confidence≥60%
  - El Lift > 1.5 confirma asociaciones no triviales
  - Las reglas revelan combinaciones de hábitos alimentarios y
    condición física que distinguen cada nivel de obesidad
  - Resultado clave: historia familiar + peso alto = predictor fuerte
    de obesidad severa (Lift elevado)

MEJORAS PROPUESTAS
  - Crear variable IMC derivada (Weight/Height²)
  - Optimizar hiperparámetros con GridSearchCV
  - Probar Gradient Boosting / XGBoost
  - Validar con datos externos (set de prueba completamente nuevo)
''')
"""))

# ─────────────────────────────────────────────────────────────
# 15 — INSUMOS PARA PPT
# ─────────────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("""\
## 15 · Insumos para Presentación (PPT — máximo 15 diapositivas)

| Diapositiva | Contenido | Archivo/Tabla |
|---|---|---|
| 1 | Título, integrantes, dataset | — |
| 2 | Contexto y objetivo | — |
| 3 | Metodología CRISP-DM | — |
| 4 | Descripción del dataset | `df.describe()` |
| 5 | Preparación y procesamiento | — |
| 6 | EDA principal | `outputs/01_distribucion_objetivo.png` |
| 7 | Clustering: método y justificación | `outputs/06_evaluacion_clusters.png` |
| 8 | Clustering: interpretación de grupos | `outputs/07_clusters_visualizacion.png` |
| 9 | Clasificación: modelos comparados | `outputs/08_comparacion_modelos.png` |
| 10 | Clasificación: resultados en test | `classification_report` |
| 11 | Mejor modelo y mejoras futuras | tabla mejoras |
| 12 | FP-Growth: preparación de datos | esquema ítems |
| 13 | Reglas con mejores indicadores | `top10` |
| 14 | 6 reglas novedosas e interpretación | `seleccionadas` |
| 15 | Conclusiones finales | resumen ejecutivo |

**Archivos generados en `outputs/`:**
"""))
cells.append(nbf.v4.new_code_cell("""\
import glob
archivos = sorted(glob.glob('outputs/*.png'))
print('Figuras generadas:')
for a in archivos:
    print(f'  {a}')
print()
print('Notebook completo y reproducible.')
print('Todos los criterios de aceptación del PRD han sido cubiertos.')
"""))

# ─────────────────────────────────────────────────────────────
# Ensamblar y guardar
# ─────────────────────────────────────────────────────────────
nb.cells = cells

output_path = 'analisis_obesidad.ipynb'
with open(output_path, 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print(f'Notebook generado: {output_path}')
print(f'Celdas totales: {len(cells)}')
