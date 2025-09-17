from Extract.extractor_sport import extract_data
from Transform.transformer_sport import transform_data
from Load.loader_sport import load_data

def main():
    print("🚀 Iniciando ETL de Deportes...")

    # 1. Extraer
    df = extract_data()
    if df is None:
        print("❌ No se pudieron extraer datos. Fin del proceso.")
        return

    # 2. Transformar
    df_clean = transform_data(df)
    if df_clean is None:
        print("❌ No se pudieron transformar los datos. Fin del proceso.")
        return

    # 3. Cargar y graficar
    load_data(df_clean)

    print("🎉 Proceso ETL de deportes completado con éxito.")

if __name__ == "__main__":
    main()
