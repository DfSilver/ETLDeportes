import pandas as pd
from Config.config_sport import OUTPUT_FILE_PATH, VISUALS_PATH
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(df):
    try:
        print("💾 Cargando datos limpios...")
        df.to_csv(OUTPUT_FILE_PATH, index=False)
        print(f"✅ Datos cargados en: {OUTPUT_FILE_PATH}")

        # Generar visualizaciones
        print("📊 Generando visualizaciones con Seaborn...")

        # Gráfico 1: Distribución de una columna numérica
        if "athleticism" in df.columns:
            plt.figure(figsize=(8,5))
            sns.histplot(df["athleticism"], kde=True, color="blue")
            plt.title("Distribución de Athleticism")
            plt.savefig(f"{VISUALS_PATH}/athleticism_distribution.png")

        # Gráfico 2: Comparación entre dos variables
        if "endurance" in df.columns and "strength" in df.columns:
            plt.figure(figsize=(8,5))
            sns.scatterplot(x="endurance", y="strength", data=df, hue="sport")
            plt.title("Endurance vs Strength por Deporte")
            plt.savefig(f"{VISUALS_PATH}/endurance_vs_strength.png")

        # Gráfico 3: Ranking por alguna métrica
        if "sport" in df.columns and "toughness" in df.columns:
            plt.figure(figsize=(10,6))
            sns.barplot(x="toughness", y="sport", data=df.sort_values("toughness", ascending=False))
            plt.title("Ranking de deportes por Toughness")
            plt.savefig(f"{VISUALS_PATH}/toughness_ranking.png")

        print(f"✅ Visualizaciones guardadas en: {VISUALS_PATH}")

    except Exception as e:
        print(f"❌ Error al cargar datos: {e}")
