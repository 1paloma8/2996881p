import csv

# Abrimos el archivo en modo lectura
with open("datos.csv", mode="r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)  # Creamos el lector CSV
    for fila in lector:
        print(fila)  # Imprimimos cada fila
