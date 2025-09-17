import os

# Ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Ruta del archivo CSV de deportes
SPORT_FILE_PATH = os.path.join(BASE_DIR, "Extract", "Files", "toughestsport.csv")

# Carpeta de salida para datos limpios
OUTPUT_FILE_PATH = os.path.join(BASE_DIR, "Load", "sports_clean.csv")

# Carpeta para guardar las gráficas
VISUALS_PATH = os.path.join(BASE_DIR, "Load", "Visuals")
os.makedirs(VISUALS_PATH, exist_ok=True)
