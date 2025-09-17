import pandas as pd
from Config.config_sport import SPORT_FILE_PATH

def extract_data():
    try:
        print("📥 Extrayendo datos de deportes...")
        df = pd.read_csv(SPORT_FILE_PATH)
        print(f"✅ Datos extraídos: {df.shape[0]} filas y {df.shape[1]} columnas")
        return df
    except Exception as e:
        print(f"❌ Error al extraer datos: {e}")
        return None
