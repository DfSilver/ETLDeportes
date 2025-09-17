# 🚀 Proyecto ETL de Deportes

## 📌 Descripción
Este proyecto implementa un proceso **ETL (Extract, Transform, Load)** sobre un dataset de deportes, clasificándolos en diferentes categorías como **deportes de cancha, acuáticos, de contacto, aéreos, de invierno, de salón y de montaña**.  

El proceso también incluye la generación de gráficos (barras, pastel y columnas) para visualizar la distribución de los deportes.

---

## 🔄 Flujo ETL
1. **Extract**: Lectura del dataset desde archivo CSV.  
2. **Transform**: Limpieza, eliminación de duplicados y nulos, normalización de columnas, categorización de deportes.  
3. **Load**: Exportación de los datos transformados a un nuevo archivo CSV.  

---

## 📊 Diagrama del flujo

mermaid
graph TD
    A[Extract] --> B[Transform]
    B --> C[Load]
    
## 📦 Dependencias
Python 3.9+
Pandas
Matplotlib

## Instalación:

bash
Copiar código
pip install -r requirements.txt
▶️ Pasos de ejecución
bash
Copiar código
python main_etl.py


## 📷 Evidencias

<img width="612" height="526" alt="image" src="https://github.com/user-attachments/assets/7f69523a-fc48-4db9-aaf8-0641695e231f" />
<img width="868" height="522" alt="image" src="https://github.com/user-attachments/assets/ef35e6a3-2826-47d1-bc84-7993179b6018" />
<img width="864" height="514" alt="image" src="https://github.com/user-attachments/assets/fece5fdc-6b36-4eb4-ab51-ef14b2f4abf5" />

