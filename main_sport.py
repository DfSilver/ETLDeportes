# main_sport.py
from Extract.extractor_sport import extract_data
from Transform.transformer_sport import transform_data
from Load.loader_sport import load_data
from Visualize.graficador import GraficadorSport  # clase del módulo Visualize

def main():
    print("🚀 Iniciando ETL de deportes...")

    # 1) EXTRAER
    df = extract_data()
    if df is None or df.empty:
        print("❌ No se pudieron extraer datos. Fin del proceso.")
        return

    # 2) TRANSFORMAR
    df_clean = transform_data(df)
    if df_clean is None or df_clean.empty:
        print("❌ No se pudieron transformar los datos. Fin del proceso.")
        return

    # 3) CARGAR
    load_data(df_clean)

    # 4) VISUALIZAR (usa la clase GraficadorSport)
    graficador = GraficadorSport(df_clean)
    # show=True mostrará las gráficas (plt.show()), save=True las guardará en disco.
    graficador.graficar_datos(show=True, save=True)

    print("✅ ETL y visualización completados.")

if __name__ == "__main__":
    main()
