# Tarea Obesity — CRISP-DM

Proyecto de análisis y modelamiento del dataset de obesidad siguiendo CRISP-DM.

## Entorno oficial

El entorno oficial del proyecto es **`venvAPP`**. No uses `.venv`: ese entorno fue reemplazado para evitar confusión.

### Crear el entorno

```powershell
python -m venv venvAPP
venvAPP\Scripts\python.exe -m pip install -r requirements.txt
venvAPP\Scripts\python.exe -m ipykernel install --user --name venvapp-obesity --display-name "Python (venvAPP obesity)"
```

### Usar el notebook

En Jupyter/VS Code seleccioná el kernel:

```text
Python (venvAPP obesity)
```

### Ejecutar scripts

```powershell
venvAPP\Scripts\python.exe create_notebook.py
# La app Streamlit NO se ejecuta con python directo, sino con streamlit run:
venvAPP\Scripts\streamlit.exe run app.py
```

## Archivos principales

- `analisis_obesidad.ipynb`: notebook principal del análisis.
- `requirements.txt`: dependencias directas del proyecto.
- `requirements-lock.txt`: versiones congeladas para reproducibilidad exacta.
- `app.py`: backoffice/app Streamlit.
- `data/`: dataset utilizado.
- `outputs/` y `models/`: resultados locales regenerables.
