# -*- coding: utf-8 -*-
"""
Clasificador de Niveles de Obesidad — App Streamlit
Solemne 2 · Punto 3 — Taller de Aplicaciones · Magíster en Data Science · USS
Alumno: Dante Gil Zenteno · Docente: Dr. Mauricio Sepúlveda

Dos partes que pide la consigna:
  1) Visualización de los RESULTADOS del clasificador (Solemne 1).
  2) Probar el modelo ingresando un dato por pantalla.

Ejecutar:  streamlit run app.py
Requiere:  models/mejor_modelo.pkl, models/label_encoder.pkl
           outputs/  (tablas e imágenes generadas por analisis_obesidad.ipynb)
"""
from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

BASE = Path(__file__).resolve().parent

st.set_page_config(page_title="Clasificador de Obesidad", page_icon="⚕️", layout="wide")

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


@st.cache_resource
def cargar_modelos():
    modelo = joblib.load(BASE / "models" / "mejor_modelo.pkl")
    le = joblib.load(BASE / "models" / "label_encoder.pkl")
    return modelo, le


@st.cache_data
def cargar_resultados():
    """Tablas de evaluación generadas en la Solemne 1 (pueden no existir)."""
    comp = pd.read_csv(BASE / "outputs" / "tabla_comparacion_modelos.csv")
    rep = pd.read_csv(BASE / "outputs" / "reporte_clasificacion_completo.csv", index_col=0)
    return comp, rep


try:
    modelo, le = cargar_modelos()
except FileNotFoundError:
    st.error(
        "No se encontraron `models/mejor_modelo.pkl` / `models/label_encoder.pkl`. "
        "Ejecutá primero el notebook `analisis_obesidad.ipynb` completo."
    )
    st.stop()

st.title("⚕️ Clasificador de Niveles de Obesidad")
st.caption(
    "Taller de Aplicaciones — Magíster en Data Science (USS). "
    "Modelo XGBoost entrenado sobre el dataset UCI *Estimation of Obesity Levels* "
    "(Mendoza Palechor & De la Hoz, 2019). **No constituye diagnóstico clínico.**"
)

tab_pred, tab_res, tab_info = st.tabs(
    ["🔍 Probar el modelo", "📊 Resultados del clasificador", "ℹ️ Acerca de"]
)

# ──────────────────────────────────────────────────────────────────────────────
# PESTAÑA 1 — Probar el modelo (input por pantalla)
# ──────────────────────────────────────────────────────────────────────────────
with tab_pred:
    col_izq, col_der = st.columns([1.2, 1])

    with col_izq:
        st.subheader("Datos de la persona")

        c1, c2, c3 = st.columns(3)
        with c1:
            gender = st.selectbox("Sexo", ["Female", "Male"],
                                  format_func=lambda x: "Femenino" if x == "Female" else "Masculino")
            age = st.number_input("Edad (años)", 14, 90, 30)
            height = st.number_input("Altura (m)", 1.40, 2.10, 1.70, step=0.01)
            weight = st.number_input("Peso (kg)", 35.0, 200.0, 75.0, step=0.5)
        with c2:
            family = st.selectbox("Antecedente familiar de sobrepeso", ["yes", "no"],
                                  format_func=lambda x: "Sí" if x == "yes" else "No")
            favc = st.selectbox("¿Consume alimentos hipercalóricos con frecuencia? (FAVC)", ["yes", "no"],
                                format_func=lambda x: "Sí" if x == "yes" else "No")
            fcvc = st.slider("Frecuencia de consumo de verduras (FCVC)", 1.0, 3.0, 2.0, 0.5)
            ncp = st.slider("Número de comidas principales (NCP)", 1.0, 4.0, 3.0, 0.5)
            caec = st.selectbox("Come entre comidas (CAEC)", ["no", "Sometimes", "Frequently", "Always"],
                                index=1)
        with c3:
            smoke = st.selectbox("¿Fuma? (SMOKE)", ["no", "yes"],
                                 format_func=lambda x: "Sí" if x == "yes" else "No")
            ch2o = st.slider("Consumo de agua diario (CH2O, litros aprox.)", 1.0, 3.0, 2.0, 0.5)
            scc = st.selectbox("¿Monitorea sus calorías? (SCC)", ["no", "yes"],
                               format_func=lambda x: "Sí" if x == "yes" else "No")
            faf = st.slider("Actividad física semanal (FAF, 0=nada · 3=alta)", 0.0, 3.0, 1.0, 0.5)
            tue = st.slider("Tiempo en pantallas (TUE, 0=bajo · 2=alto)", 0.0, 2.0, 1.0, 0.5)
            calc = st.selectbox("Consumo de alcohol (CALC)", ["no", "Sometimes", "Frequently", "Always"],
                                index=1)
            mtrans = st.selectbox("Transporte habitual (MTRANS)",
                                  ["Public_Transportation", "Automobile", "Walking", "Motorbike", "Bike"])

        predecir = st.button("🔍 Predecir nivel de obesidad", type="primary", width="stretch")

    with col_der:
        st.subheader("Resultado")

        if predecir:
            entrada = pd.DataFrame([{
                "Gender": gender, "Age": age, "Height": height, "Weight": weight,
                "family_history_with_overweight": family, "FAVC": favc, "FCVC": fcvc,
                "NCP": ncp, "CAEC": caec, "SMOKE": smoke, "CH2O": ch2o, "SCC": scc,
                "FAF": faf, "TUE": tue, "CALC": calc, "MTRANS": mtrans,
            }])

            pred = modelo.predict(entrada)[0]
            clase = le.inverse_transform([pred])[0]
            imc = weight / height ** 2

            st.metric("Nivel de obesidad predicho", ETIQUETAS_ES.get(clase, clase))
            st.metric("IMC calculado (referencial)", f"{imc:.1f}")
            st.info(INTERPRETACION.get(clase, ""))

            if hasattr(modelo, "predict_proba"):
                proba = modelo.predict_proba(entrada)[0]
                df_proba = pd.DataFrame({
                    "Clase": [ETIQUETAS_ES.get(c, c) for c in le.classes_],
                    "Probabilidad": proba,
                }).sort_values("Probabilidad", ascending=False).reset_index(drop=True)
                st.write("**Probabilidad por clase:**")
                st.dataframe(
                    df_proba.style.format({"Probabilidad": "{:.1%}"}),
                    width="stretch", hide_index=True,
                )
                st.bar_chart(df_proba.set_index("Clase")["Probabilidad"])

            st.caption(
                "⚠️ Salida de un modelo académico entrenado con datos parcialmente sintéticos "
                "(77% SMOTE). Cualquier decisión de salud requiere evaluación profesional."
            )
        else:
            st.write("Completá los datos y presioná **Predecir**.")

# ──────────────────────────────────────────────────────────────────────────────
# PESTAÑA 2 — Resultados del clasificador (evaluación de la Solemne 1)
# ──────────────────────────────────────────────────────────────────────────────
with tab_res:
    try:
        comp, rep = cargar_resultados()
    except FileNotFoundError:
        st.warning("No se encontraron las tablas en `outputs/`. Ejecutá el notebook para generarlas.")
        st.stop()

    acc = float(rep.loc["accuracy", "f1-score"])
    f1m = float(rep.loc["macro avg", "f1-score"])
    n_clases = sum(1 for c in rep.index if c in ETIQUETAS_ES)

    st.subheader("Desempeño del modelo en producción (XGBoost)")
    m1, m2, m3 = st.columns(3)
    m1.metric("Accuracy (test)", f"{acc:.1%}")
    m2.metric("F1-score macro", f"{f1m:.3f}")
    m3.metric("Niveles que clasifica", n_clases)

    st.divider()

    # --- Comparación de algoritmos ---
    st.markdown("#### XGBoost lideró la comparación de algoritmos")
    base = (comp[comp["Experimento"] == "Base"]
            .sort_values("F1 macro", ascending=False))
    st.bar_chart(base.set_index("Modelo")["F1 macro"], height=280)
    st.caption("F1-score macro por algoritmo (configuración base, sobre el conjunto de test).")

    with st.expander("Ver tabla completa de experimentos (incluye PCA, SVD y Feature Engineering)"):
        st.dataframe(
            comp.style.format({
                "Accuracy": "{:.1%}", "Precision macro": "{:.1%}",
                "Recall macro": "{:.1%}", "F1 macro": "{:.1%}",
            }),
            width="stretch", hide_index=True,
        )
        st.caption(
            "El feature engineering (+5 atributos derivados, incluido el IMC) llevó a XGBoost "
            "hasta 98.3% de accuracy: mejora explorada como trabajo futuro."
        )

    st.divider()

    # --- Matriz de confusión + desempeño por clase ---
    c_izq, c_der = st.columns(2)

    with c_izq:
        st.markdown("#### Matriz de confusión")
        img_cm = BASE / "outputs" / "09_confusion_matrix.png"
        if img_cm.exists():
            st.image(str(img_cm), width="stretch")
        st.caption(
            "Los aciertos están en la diagonal. Los pocos errores se concentran entre "
            "niveles contiguos (p. ej. Peso normal ↔ Sobrepeso I), lo esperable en una escala ordinal."
        )

    with c_der:
        st.markdown("#### Desempeño por nivel")
        clases_idx = [c for c in rep.index if c in ETIQUETAS_ES]
        por_clase = rep.loc[clases_idx].copy()
        por_clase.index = [ETIQUETAS_ES[c] for c in clases_idx]
        st.dataframe(
            por_clase.style.format({
                "precision": "{:.2f}", "recall": "{:.2f}",
                "f1-score": "{:.2f}", "support": "{:.0f}",
            }),
            width="stretch",
        )
        st.caption("Precisión, recall y F1 por nivel. *Support* = casos de ese nivel en el test.")

    st.divider()

    # --- Importancia de variables ---
    st.markdown("#### ¿Qué variables pesan más en la predicción?")
    imp_path = BASE / "outputs" / "tabla_importancia_atributos_v3.csv"
    if imp_path.exists():
        imp = (pd.read_csv(imp_path)
               .sort_values("Importancia", ascending=False)
               .head(10))
        st.bar_chart(imp.set_index("Variable")["Importancia"], height=300)
        st.caption(
            "Importancia de variables (análisis con atributos derivados). El **IMC** (Weight/Height²) "
            "y el **peso** dominan la decisión, algo coherente con el dominio clínico."
        )
    else:
        st.info("Tabla de importancia no disponible en `outputs/`.")

# ──────────────────────────────────────────────────────────────────────────────
# PESTAÑA 3 — Acerca de
# ──────────────────────────────────────────────────────────────────────────────
with tab_info:
    st.subheader("Sobre este trabajo")
    st.markdown(
        """
- **Dataset:** *Estimation of Obesity Levels Based On Eating Habits and Physical Condition*
  (UCI, 2.111 registros de México, Perú y Colombia, 17 atributos).
- **Problema:** clasificación **multiclase** en 7 niveles, de *Peso insuficiente* a *Obesidad tipo III*.
- **Modelo en producción:** **XGBoost** dentro de un `Pipeline` (preprocesamiento + clasificador),
  ~96.5 % de *accuracy* en test. El preprocesamiento se aplica solo, por eso la pestaña de predicción
  recibe los datos crudos tal como los ingresás.
- **Flujo CRISP-DM:** comprensión del negocio → datos → preparación → modelado → evaluación → despliegue (esta app).
- **Referencia:** Mendoza Palechor, F. & De la Hoz Manotas, A. (2019). *Data in Brief*.
        """
    )
    st.warning(
        "⚠️ Herramienta **académica**. El modelo se entrenó con datos parcialmente sintéticos (SMOTE) "
        "y **no constituye diagnóstico clínico**. Cualquier decisión de salud requiere evaluación profesional."
    )
