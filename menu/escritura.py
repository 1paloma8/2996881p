
import csv

base = [
    ["nombre", "edad", "ciudad"],
    ["Carlos", 22, "Lima"],
    ["Sofía", 29, "Buenos Aires"],
    ["Luis", 35, "Santiago"]]

with open("nueva_base.csv", mode="w", encoding="utf-8", newline="") as archivo:
    escritor = csv.writer(archivo)  # Creamos el escritor CSV
    escritor.writerows(base)  # Escribimos todas las filas
