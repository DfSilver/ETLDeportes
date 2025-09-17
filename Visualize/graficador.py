# Visualize/graficador.py
import os
import seaborn as sns
import matplotlib.pyplot as plt
from Config.config_sport import VISUALS_PATH  # ruta de salida para gráficos

class GraficadorSport:
    """
    Clase para generar 3 visualizaciones distintas con Seaborn:
      1. Histograma de una métrica
      2. Scatterplot comparando dos métricas
      3. Boxplot para comparar una métrica entre deportes
    """

    def __init__(self, df):
        self.df = df
        os.makedirs(VISUALS_PATH, exist_ok=True)

    def graficar_datos(self, show=True, save=True):
        print("📊 Generando gráficas con Seaborn...")

        # --- Gráfico 1: Histograma de una métrica numérica ---
        num_col_1 = None
        for c in ["athleticism", "toughness", "endurance", "strength"]:
            if c in self.df.columns:
                num_col_1 = c
                break

        if num_col_1:
            plt.figure(figsize=(8, 5))
            sns.histplot(self.df[num_col_1].dropna(), kde=True, color="skyblue")
            plt.title(f"Distribución de {num_col_1}")
            plt.tight_layout()
            if save:
                fp = os.path.join(VISUALS_PATH, f"{num_col_1}_distribution.png")
                plt.savefig(fp)
                print(f"  - Guardado: {fp}")
            if show:
                plt.show()
            plt.clf()

        # --- Gráfico 2: Scatterplot entre dos métricas ---
        x_col, y_col = None, None
        cand_x = ["endurance", "athleticism", "speed"]
        cand_y = ["strength", "toughness", "power"]
        for cx in cand_x:
            for cy in cand_y:
                if cx in self.df.columns and cy in self.df.columns:
                    x_col, y_col = cx, cy
                    break
            if x_col:
                break

        if x_col and y_col:
            plt.figure(figsize=(8, 6))
            hue_col = "sport" if "sport" in self.df.columns else None
            sns.scatterplot(x=self.df[x_col], y=self.df[y_col], hue=self.df[hue_col] if hue_col else None, palette="tab10")
            plt.title(f"{x_col.capitalize()} vs {y_col.capitalize()}")
            plt.tight_layout()
            if save:
                fp = os.path.join(VISUALS_PATH, f"{x_col}_vs_{y_col}.png")
                plt.savefig(fp)
                print(f"  - Guardado: {fp}")
            if show:
                plt.show()
            plt.clf()

        # --- Gráfico 3: Boxplot para comparar deportes ---
        box_col = None
        for c in ["toughness", "athleticism", "strength"]:
            if c in self.df.columns and "sport" in self.df.columns:
                box_col = c
                break

        if box_col:
            plt.figure(figsize=(12, 6))
            sns.boxplot(x="sport", y=box_col, data=self.df, palette="Set2")
            plt.title(f"Distribución de {box_col} por deporte")
            plt.xticks(rotation=45)
            plt.tight_layout()
            if save:
                fp = os.path.join(VISUALS_PATH, f"{box_col}_boxplot.png")
                plt.savefig(fp)
                print(f"  - Guardado: {fp}")
            if show:
                plt.show()
            plt.clf()

        print(f"✅ Visualizaciones completadas. Carpeta: {VISUALS_PATH}")
