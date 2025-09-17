import pandas as pd

def transform_data(df):
    try:
        print("🔄 Transformando datos...")

        # Eliminar duplicados
        df = df.drop_duplicates()

        # Eliminar filas con valores nulos
        df = df.dropna()

        # Normalizar nombres de columnas (sin espacios)
        df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

        print(f"✅ Transformación completa: {df.shape[0]} filas y {df.shape[1]} columnas")
        return df
    except Exception as e:
        print(f"❌ Error en la transformación: {e}")
        return None
