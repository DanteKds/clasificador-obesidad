"""Extrae outputs de texto del notebook ejecutado para auditoría."""
import json
import sys

NB = "analisis_obesidad_ejecutado.ipynb"

with open(NB, encoding="utf-8") as f:
    nb = json.load(f)

for i, cell in enumerate(nb["cells"]):
    if cell["cell_type"] != "code":
        continue
    src_head = "".join(cell["source"])[:80].replace("\n", " | ")
    texts = []
    for out in cell.get("outputs", []):
        if out.get("output_type") == "stream":
            texts.append("".join(out.get("text", [])))
        elif out.get("output_type") == "execute_result":
            data = out.get("data", {})
            if "text/plain" in data:
                texts.append("".join(data["text/plain"]))
        elif out.get("output_type") == "error":
            texts.append("ERROR: " + out.get("ename", "") + ": " + out.get("evalue", ""))
    if texts:
        print(f"\n{'='*70}\nCELDA {i} :: {src_head}\n{'='*70}")
        full = "\n".join(texts)
        # limitar celdas muy largas
        if len(full) > 3500:
            full = full[:3000] + f"\n... [TRUNCADO, total {len(full)} chars] ...\n" + full[-400:]
        print(full)
