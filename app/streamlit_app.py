# -*- coding: utf-8 -*-
"""
Solemne 2 — Visualización de resultados del clasificador de Obesidad
Taller de Aplicaciones · Magíster en Data Science · USS
Alumno: Dante Gil Zenteno · Docente: Dr. Mauricio Sepúlveda
"""
from pathlib import Path

import joblib
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

BASE = Path(__file__).resolve().parents[1]
MODELS_DIR = BASE / "models"
OUTPUTS_DIR = BASE / "outputs"

st.set_page_config(
    page_title="Clasificador de Obesidad — Solemne 2",
    page_icon="⚕️",
    layout="wide",
)

ETIQUETAS_ES = {
    "Insufficient_Weight": "Peso insuficiente",
    "Normal_Weight": "Peso normal",
    "Overweight_Level_I": "Sobrepeso nivel I",
    "Overweight_Level_II": "Sobrepeso nivel II",
    "Obesity_Type_I": "Obesidad tipo I",
    "Obesity_Type_II": "Obesidad tipo II",
    "Obesity_Type_III": "Obesidad tipo III",
}

INTERPRETACION = {
    "Insufficient_Weight": "IMC bajo el rango saludable. Perfil de bajo peso corporal.",
    "Normal_Weight": "Perfil dentro del rango esperado según los hábitos ingresados.",
    "Overweight_Level_I": "Sobrepeso inicial. Los hábitos ingresados se asemejan a perfiles con exceso de peso leve.",
    "Overweight_Level_II": "Sobrepeso avanzado. Perfil de riesgo de progresión a obesidad.",
    "Obesity_Type_I": "Perfil compatible con obesidad grado I.",
    "Obesity_Type_II": "Perfil compatible con obesidad grado II.",
    "Obesity_Type_III": "Perfil compatible con obesidad grado III (la de mayor severidad en la escala).",
}

COLOR_CLASE = {
    "Peso insuficiente": "#3498db",
    "Peso normal": "#2ecc71",
    "Sobrepeso nivel I": "#f1c40f",
    "Sobrepeso nivel II": "#e67e22",
    "Obesidad tipo I": "#e74c3c",
    "Obesidad tipo II": "#c0392b",
    "Obesidad tipo III": "#7b241c",
}


@st.cache_resource
def cargar_modelos():
    modelo = joblib.load(MODELS_DIR / "mejor_modelo.pkl")
    le = joblib.load(MODELS_DIR / "label_encoder.pkl")
    return modelo, le


@st.cache_data
def cargar_resultados():
    comp = pd.read_csv(OUTPUTS_DIR / "tabla_comparacion_modelos.csv")
    rep = pd.read_csv(OUTPUTS_DIR / "reporte_clasificacion_completo.csv", index_col=0)
    imp = pd.read_csv(OUTPUTS_DIR / "tabla_importancia_atributos_v3.csv")
    return comp, rep, imp


try:
    modelo, le = cargar_modelos()
except FileNotFoundError as e:
    st.error(f"No se encontró el modelo: {e}. Verificá que `models/mejor_modelo.pkl` y `models/label_encoder.pkl` existan.")
    st.stop()

# ─── Header ──────────────────────────────────────────────────────────────────
st.title("⚕️ Clasificador de Niveles de Obesidad")
st.caption(
    "**Solemne 2 — Taller de Aplicaciones · Magíster en Data Science (USS)** · "
    "Modelo entrenado sobre el dataset UCI *Estimation of Obesity Levels* "
    "(Mendoza Palechor & De la Hoz, 2019). "
    "**No constituye diagnóstico clínico.**"
)
st.divider()

# ─── Tabs ─────────────────────────────────────────────────────────────────────
tab_res, tab_viz, tab_pred, tab_info = st.tabs([
    "📊 Resultados del clasificador",
    "📈 Visualizaciones",
    "🔍 Probar el modelo",
    "ℹ️ Metodología",
])

# ══════════════════════════════════════════════════════════════════════════════
# TAB 1 — Resultados del clasificador
# ══════════════════════════════════════════════════════════════════════════════
with tab_res:
    try:
        comp, rep, imp = cargar_resultados()
    except FileNotFoundError as e:
        st.warning(f"No se encontraron las tablas en `reports/outputs/`: {e}")
        st.stop()

    acc = float(rep.loc["accuracy", "f1-score"])
    f1m = float(rep.loc["macro avg", "f1-score"])
    prec = float(rep.loc["macro avg", "precision"])
    rec = float(rep.loc["macro avg", "recall"])
    n_clases = sum(1 for c in rep.index if c in ETIQUETAS_ES)

    st.subheader("Métricas del modelo en conjunto de test")

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Accuracy", f"{acc:.1%}", help="Proporción total de predicciones correctas")
    col2.metric("F1-score macro", f"{f1m:.3f}", help="Media armónica de precisión y recall, promediada por clase")
    col3.metric("Precisión macro", f"{prec:.3f}", help="Cuántos de los predichos como X realmente son X")
    col4.metric("Recall macro", f"{rec:.3f}", help="Cuántos de los X reales fueron detectados")
    col5.metric("Niveles clasificados", n_clases)

    st.divider()

    st.markdown("#### Comparación de algoritmos (configuración base)")
    base = comp[comp["Experimento"] == "Base"].sort_values("F1 macro", ascending=False).copy()
    if not base.empty:
        fig_bar = px.bar(
            base, x="Modelo", y="F1 macro",
            color="F1 macro", color_continuous_scale="Teal",
            text="F1 macro", title="F1-score macro por algoritmo (test set)",
            labels={"F1 macro": "F1 macro", "Modelo": "Algoritmo"},
        )
        fig_bar.update_traces(texttemplate="%{text:.3f}", textposition="outside")
        fig_bar.update_layout(showlegend=False, yaxis_range=[0.7, 1.0])
        st.plotly_chart(fig_bar, use_container_width=True)

    with st.expander("Ver tabla completa de experimentos"):
        fmt_cols = {c: "{:.3f}" for c in ["Accuracy", "Precision macro", "Recall macro", "F1 macro"] if c in comp.columns}
        st.dataframe(comp.style.format(fmt_cols), use_container_width=True, hide_index=True)

    st.divider()

    st.markdown("#### Desempeño por nivel de obesidad")
    clases_idx = [c for c in rep.index if c in ETIQUETAS_ES]
    por_clase = rep.loc[clases_idx].copy()
    por_clase.index = [ETIQUETAS_ES[c] for c in clases_idx]
    por_clase = por_clase[["precision", "recall", "f1-score", "support"]]

    fig_clase = px.bar(
        por_clase.reset_index().rename(columns={"index": "Nivel"}),
        x="Nivel", y="f1-score",
        color="f1-score", color_continuous_scale="Greens",
        text="f1-score", title="F1-score por nivel de obesidad",
    )
    fig_clase.update_traces(texttemplate="%{text:.2f}", textposition="outside")
    fig_clase.update_layout(showlegend=False, yaxis_range=[0.8, 1.0], xaxis_tickangle=-20)
    st.plotly_chart(fig_clase, use_container_width=True)

    st.dataframe(
        por_clase.style.format({"precision": "{:.2f}", "recall": "{:.2f}", "f1-score": "{:.2f}", "support": "{:.0f}"}),
        use_container_width=True,
    )

# ══════════════════════════════════════════════════════════════════════════════
# TAB 2 — Visualizaciones
# ══════════════════════════════════════════════════════════════════════════════
with tab_viz:
    try:
        comp, rep, imp = cargar_resultados()
    except FileNotFoundError:
        st.warning("No se encontraron las tablas de resultados.")
        st.stop()

    col_iz, col_de = st.columns(2)

    with col_iz:
        st.markdown("#### Matriz de confusión")
        img_cm = OUTPUTS_DIR / "09_confusion_matrix.png"
        if img_cm.exists():
            st.image(str(img_cm), use_container_width=True)
            st.caption("Los aciertos están en la diagonal. Los errores se concentran entre niveles contiguos.")
        else:
            st.info("Imagen de matriz de confusión no disponible.")

    with col_de:
        st.markdown("#### Importancia de variables")
        top10 = imp.sort_values("Importancia", ascending=False).head(10)
        fig_imp = px.bar(
            top10, x="Importancia", y="Variable", orientation="h",
            color="Tipo", title="Top 10 variables más importantes",
            color_discrete_map={"Original": "#3498db", "Creada": "#e74c3c"},
        )
        fig_imp.update_layout(yaxis={"categoryorder": "total ascending"})
        st.plotly_chart(fig_imp, use_container_width=True)

    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        img_dist = OUTPUTS_DIR / "01_distribucion_objetivo.png"
        if img_dist.exists():
            st.markdown("#### Distribución de clases")
            st.image(str(img_dist), use_container_width=True)

    with col2:
        img_iter = OUTPUTS_DIR / "18_comparacion_iteraciones.png"
        if img_iter.exists():
            st.markdown("#### Evolución de experimentos")
            st.image(str(img_iter), use_container_width=True)
        else:
            img_comp = OUTPUTS_DIR / "08_comparacion_modelos.png"
            if img_comp.exists():
                st.markdown("#### Comparación de modelos")
                st.image(str(img_comp), use_container_width=True)

    st.divider()
    st.markdown("#### Validación cruzada (k=5)")
    cv_path = OUTPUTS_DIR / "tabla_validacion_cruzada_v3.csv"
    if cv_path.exists():
        cv = pd.read_csv(cv_path)
        fmt = {c: "{:.4f}" for c in cv.columns if cv[c].dtype == "float64"}
        st.dataframe(cv.style.format(fmt), use_container_width=True, hide_index=True)
        st.caption("Validación cruzada estratificada con k=5 folds. Resultados estables entre folds (desv. < 0.01).")

# ══════════════════════════════════════════════════════════════════════════════
# TAB 3 — Probar el modelo
# ══════════════════════════════════════════════════════════════════════════════
with tab_pred:
    st.subheader("Ingresá los datos y probá el modelo")
    st.info("Completá el formulario con las características de una persona y presioná **Predecir** para obtener el nivel de obesidad estimado.")

    with st.form("formulario_prediccion"):
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("**Datos básicos**")
            gender = st.selectbox("Sexo", ["Female", "Male"],
                                  format_func=lambda x: "Femenino" if x == "Female" else "Masculino")
            age = st.number_input("Edad (años)", min_value=14, max_value=90, value=30)
            height = st.number_input("Altura (m)", min_value=1.40, max_value=2.10, value=1.70, step=0.01)
            weight = st.number_input("Peso (kg)", min_value=35.0, max_value=200.0, value=75.0, step=0.5)
            family = st.selectbox("Antecedente familiar de sobrepeso",
                                  ["yes", "no"], format_func=lambda x: "Sí" if x == "yes" else "No")

        with col2:
            st.markdown("**Hábitos alimenticios**")
            favc = st.selectbox("¿Come alimentos hipercalóricos con frecuencia? (FAVC)",
                                ["yes", "no"], format_func=lambda x: "Sí" if x == "yes" else "No")
            fcvc = st.slider("Frecuencia de consumo de verduras (FCVC)", 1.0, 3.0, 2.0, 0.5,
                             help="1=Nunca, 2=A veces, 3=Siempre")
            ncp = st.slider("Número de comidas principales (NCP)", 1.0, 4.0, 3.0, 0.5)
            caec = st.selectbox("Come entre comidas (CAEC)", ["no", "Sometimes", "Frequently", "Always"], index=1)
            ch2o = st.slider("Consumo de agua diario (CH2O, litros aprox.)", 1.0, 3.0, 2.0, 0.5)
            calc = st.selectbox("Consumo de alcohol (CALC)", ["no", "Sometimes", "Frequently", "Always"], index=1)

        with col3:
            st.markdown("**Actividad y estilo de vida**")
            faf = st.slider("Actividad física semanal (FAF)", 0.0, 3.0, 1.0, 0.5,
                            help="0=Nada, 1=1-2 días/sem, 2=2-4 días/sem, 3=4-5 días/sem")
            tue = st.slider("Tiempo en pantallas (TUE)", 0.0, 2.0, 1.0, 0.5,
                            help="0=0-2h, 1=3-5h, 2=más de 5h")
            smoke = st.selectbox("¿Fuma? (SMOKE)", ["no", "yes"],
                                 format_func=lambda x: "Sí" if x == "yes" else "No")
            scc = st.selectbox("¿Monitorea sus calorías? (SCC)", ["no", "yes"],
                               format_func=lambda x: "Sí" if x == "yes" else "No")
            mtrans = st.selectbox("Transporte habitual (MTRANS)",
                                  ["Public_Transportation", "Automobile", "Walking", "Motorbike", "Bike"])

        submitted = st.form_submit_button("🔍 Predecir nivel de obesidad", type="primary", use_container_width=True)

    if submitted:
        try:
            entrada = pd.DataFrame([{
                "Gender": gender, "Age": float(age), "Height": float(height), "Weight": float(weight),
                "family_history_with_overweight": family, "FAVC": favc, "FCVC": fcvc,
                "NCP": ncp, "CAEC": caec, "SMOKE": smoke, "CH2O": ch2o, "SCC": scc,
                "FAF": faf, "TUE": tue, "CALC": calc, "MTRANS": mtrans,
            }])

            pred = modelo.predict(entrada)[0]
            clase = le.inverse_transform([pred])[0]
            clase_es = ETIQUETAS_ES.get(clase, clase)
            imc = float(weight) / float(height) ** 2

            st.success(f"✅ Predicción completada")

            r1, r2, r3 = st.columns(3)
            r1.metric("Nivel de obesidad predicho", clase_es)
            r2.metric("IMC calculado (referencial)", f"{imc:.1f}")
            r3.metric("Clase interna", clase)

            st.info(f"**Interpretación:** {INTERPRETACION.get(clase, '')}")

            if hasattr(modelo, "predict_proba"):
                proba = modelo.predict_proba(entrada)[0]
                df_proba = pd.DataFrame({
                    "Nivel": [ETIQUETAS_ES.get(c, c) for c in le.classes_],
                    "Probabilidad": proba,
                }).sort_values("Probabilidad", ascending=False).reset_index(drop=True)

                fig_proba = px.bar(
                    df_proba, x="Probabilidad", y="Nivel", orientation="h",
                    title="Probabilidad estimada por nivel",
                    color="Probabilidad", color_continuous_scale="RdYlGn",
                    text="Probabilidad",
                )
                fig_proba.update_traces(texttemplate="%{text:.1%}", textposition="outside")
                fig_proba.update_layout(
                    yaxis={"categoryorder": "total ascending"},
                    showlegend=False,
                    xaxis_range=[0, 1.1],
                )
                st.plotly_chart(fig_proba, use_container_width=True)

            st.caption(
                "⚠️ Herramienta académica. El modelo se entrenó con datos parcialmente sintéticos (SMOTE). "
                "**No constituye diagnóstico clínico.**"
            )

        except Exception as e:
            st.error(f"Error al ejecutar la predicción: {e}")

# ══════════════════════════════════════════════════════════════════════════════
# TAB 4 — Metodología
# ══════════════════════════════════════════════════════════════════════════════
with tab_info:
    st.subheader("Metodología y contexto")
    st.markdown("""
### Dataset
- **Nombre:** *Estimation of Obesity Levels Based On Eating Habits and Physical Condition*
- **Fuente:** UCI Machine Learning Repository
- **Registros:** 2.111 (México, Perú y Colombia)
- **Atributos:** 17 (edad, altura, peso, hábitos alimenticios, actividad física, etc.)
- **Variable objetivo:** `NObeyesdad` — 7 niveles de obesidad

### Flujo CRISP-DM
1. **Comprensión del negocio:** identificar predictores de obesidad
2. **Comprensión de los datos:** 17 variables mixtas, distribución desbalanceada
3. **Preparación:** encoding ordinales, feature engineering (IMC, BMI_Category, scores de hábitos)
4. **Modelado:** comparación de 6 algoritmos — XGBoost, SVM, RF, DT, LR, KNN
5. **Evaluación:** validación cruzada k=5, optimización con RandomizedSearchCV
6. **Despliegue:** esta aplicación Streamlit

### Modelo en producción
- **Algoritmo:** XGBoost dentro de un `Pipeline` sklearn
- **Accuracy (test):** ~96.5%
- **F1-score macro (test):** 0.9637
- **Mejor experimento (Random Forest optimizado):** F1 macro 0.9904
- **Feature más importante:** IMC (calculado como Weight/Height²)

### Referencia
Mendoza Palechor, F. & De la Hoz Manotas, A. (2019).
*Obesity Level Estimation Software based on Decision Trees.* Data in Brief.
""")

    st.warning(
        "⚠️ **Advertencia académica:** El modelo se entrenó con datos parcialmente sintéticos (77% generados con SMOTE). "
        "Cualquier decisión de salud requiere evaluación profesional."
    )
