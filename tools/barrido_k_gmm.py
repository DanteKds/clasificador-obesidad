"""
Barrido del número de componentes (k) para Gaussian Mixture Model.

Objetivo: elegir el k de GMM con el criterio CORRECTO para mixturas gaussianas
(BIC como principal, AIC y Silhouette de apoyo), reproduciendo EXACTAMENTE el
mismo preprocesamiento de clustering que usa el notebook v3 (create_notebook_v3.py):

    df_clust = df[COLS_NUM + COLS_CAT]
    OrdinalEncoder sobre COLS_CAT
    StandardScaler sobre todo  ->  X_clust   (target NObeyesdad excluido)

No modifica el notebook. Solo produce evidencia para decidir el k antes de
actualizar el documento.
"""
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score

# ── Constantes idénticas al notebook ──────────────────────────────────────────
RANDOM_STATE = 42
RUTA_DATOS = "data/ObesityDataSet_raw_and_data_sinthetic.csv"
TARGET = "NObeyesdad"
COLS_NUM = ["Age", "Height", "Weight", "FCVC", "NCP", "CH2O", "FAF", "TUE"]
COLS_CAT = ["Gender", "family_history_with_overweight", "FAVC", "CAEC",
            "SMOKE", "SCC", "CALC", "MTRANS"]
K_RANGE = range(2, 11)

# ── Preprocesamiento idéntico al notebook (06 · Preprocesamiento para Clustering)
df = pd.read_csv(RUTA_DATOS)
df_clust = df[COLS_NUM + COLS_CAT].copy()
df_clust[COLS_CAT] = OrdinalEncoder().fit_transform(df_clust[COLS_CAT])
X_clust = StandardScaler().fit_transform(df_clust)
print(f"Matriz para clustering: {X_clust.shape}  (target excluido)")
print()

# ── Barrido principal: GMM covariance_type='full' (coherente con la decisión) ──
filas = []
print("=== BARRIDO k=2..10 — GMM covariance_type='full' ===")
print(f"{'k':>2} | {'BIC':>12} | {'AIC':>12} | {'Silhouette':>10} | {'tam_min_%':>9}")
print("-" * 60)
for k in K_RANGE:
    gmm = GaussianMixture(n_components=k, covariance_type="full",
                          random_state=RANDOM_STATE, n_init=5)
    labels = gmm.fit_predict(X_clust)
    bic = gmm.bic(X_clust)
    aic = gmm.aic(X_clust)
    sil = silhouette_score(X_clust, labels, sample_size=1500,
                           random_state=RANDOM_STATE)
    tam_min = pd.Series(labels).value_counts(normalize=True).min() * 100
    filas.append({"k": k, "BIC": bic, "AIC": aic, "Silhouette": sil,
                  "tam_min_%": round(tam_min, 1)})
    print(f"{k:>2} | {bic:>12.1f} | {aic:>12.1f} | {sil:>10.4f} | {tam_min:>8.1f}%")

tabla = pd.DataFrame(filas)
k_bic = int(tabla.loc[tabla["BIC"].idxmin(), "k"])
k_aic = int(tabla.loc[tabla["AIC"].idxmin(), "k"])
k_sil = int(tabla.loc[tabla["Silhouette"].idxmax(), "k"])

print()
print(f"k que MINIMIZA BIC (criterio principal GMM): k={k_bic}")
print(f"k que minimiza AIC                          : k={k_aic}")
print(f"k que maximiza Silhouette                   : k={k_sil}")
print()

# ── Complemento: BIC por (k x covariance_type) — approach canónico sklearn ─────
print("=== COMPLEMENTO: BIC por tipo de covarianza (menor = mejor) ===")
print(f"{'k':>2} | {'spherical':>11} | {'diag':>11} | {'tied':>11} | {'full':>11}")
print("-" * 60)
mejor_global = {"bic": np.inf, "k": None, "cov": None}
for k in K_RANGE:
    fila = {}
    for cov in ["spherical", "diag", "tied", "full"]:
        g = GaussianMixture(n_components=k, covariance_type=cov,
                            random_state=RANDOM_STATE, n_init=5).fit(X_clust)
        b = g.bic(X_clust)
        fila[cov] = b
        if b < mejor_global["bic"]:
            mejor_global = {"bic": b, "k": k, "cov": cov}
    print(f"{k:>2} | {fila['spherical']:>11.0f} | {fila['diag']:>11.0f} | "
          f"{fila['tied']:>11.0f} | {fila['full']:>11.0f}")
print()
print(f"Mínimo BIC global: k={mejor_global['k']}, "
      f"covariance_type='{mejor_global['cov']}' (BIC={mejor_global['bic']:.0f})")
print()

# ── Gráfico BIC/AIC/Silhouette vs k ───────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(13, 5))
axes[0].plot(tabla["k"], tabla["BIC"], "o-", color="#2563EB", lw=2, label="BIC")
axes[0].plot(tabla["k"], tabla["AIC"], "s--", color="#7C3AED", lw=2, label="AIC")
axes[0].axvline(k_bic, color="#16A34A", ls="--", lw=2, label=f"min BIC (k={k_bic})")
axes[0].set_title("Selección de k para GMM — BIC / AIC (menor = mejor)")
axes[0].set_xlabel("k (n componentes)"); axes[0].set_ylabel("Criterio de información")
axes[0].legend(); axes[0].grid(alpha=0.3)
axes[0].spines["top"].set_visible(False); axes[0].spines["right"].set_visible(False)

axes[1].plot(tabla["k"], tabla["Silhouette"], "s-", color="#6B7280", lw=2)
axes[1].axvline(k_sil, color="#16A34A", ls="--", lw=2, label=f"max Silhouette (k={k_sil})")
axes[1].set_title("Silhouette por k (apoyo)")
axes[1].set_xlabel("k"); axes[1].set_ylabel("Silhouette")
axes[1].legend(); axes[1].grid(alpha=0.3)
axes[1].spines["top"].set_visible(False); axes[1].spines["right"].set_visible(False)
plt.suptitle("GMM — Selección del número de componentes", y=1.02, fontsize=13)
plt.tight_layout()
plt.savefig("outputs/06b_seleccion_k_gmm.png", dpi=150, bbox_inches="tight")
tabla.to_csv("outputs/barrido_k_gmm.csv", index=False)
print("Guardado: outputs/06b_seleccion_k_gmm.png + outputs/barrido_k_gmm.csv")
