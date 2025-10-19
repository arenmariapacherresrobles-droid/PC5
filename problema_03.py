import os
import zipfile
import pandas as pd
import requests
# Ruta del archivo ZIP (ya está en la misma carpeta)
zip_path = "./0333.zip"

# Carpeta donde se extraerán los datos
extract_folder = "./data_youtube"

# Si no existe la carpeta, la creamos
if not os.path.exists(extract_folder):
    os.makedirs(extract_folder)

# Descomprimir el ZIP
with zipfile.ZipFile(zip_path, "r") as zip_ref:
    zip_ref.extractall(extract_folder)

print(" Archivo descomprimido correctamente en:", extract_folder)



# Listar archivos extraídos
archivos = os.listdir(extract_folder)
print(" Archivos encontrados:", archivos)

# Leer el primer archivo (por ejemplo)
archivo = os.path.join(extract_folder, archivos[0])

# Leer usando tabulaciones como separador
df = pd.read_csv(archivo, sep="\t", header=None, encoding="latin1")

print(" Datos leídos correctamente:")
print(df.head())

# ASIGNAR NOMBRES DE COLUMNAS

df.columns = [
    "VideoID", "uploader", "age", "category",
    "length", "views", "rate", "ratings", "comments"
]

print(" Columnas asignadas:")
print(df.columns)


# SELECCIONAR LAS COLUMNAS PEDIDAS

df_filtrado = df[["VideoID", "age", "category", "views", "rate"]]
print("Columnas seleccionadas:")
print(df_filtrado.head())

# APLICAR UN FILTRADO BÁSICO

# Ejemplo: quedarnos solo con algunas categorías
categorias_deseadas = ["Music", "Sports", "Comedy"]
df_final = df_filtrado[df_filtrado["category"].isin(categorias_deseadas)]

print(" Filtrado por categorías:")
print(df_final.head())


# GUARDAR EL RESULTADO

df_final.to_csv("youtube_filtrado.csv", index=False)
print("Archivo final guardado como 'youtube_filtrado.csv'")