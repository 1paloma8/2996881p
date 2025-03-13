
import csv

# Crear una lista de datos predefinidos
datos = [
    ["Juan", 25, 1.75, True],   # Nombre, Edad, Altura, Es Estudiante
    ["Ana", 30, 1.62, False],
    ["Luis", 22, 1.80, True],
    ["Maria", 28, 1.68, False],
    ["Carlos", 35, 1.90, True],
    ["Laura", 20, 1.55, True],
    ["Pedro", 40, 1.78, False],
    ["Sofia", 18, 1.60, True],
    ["Diego", 27, 1.85, False],
    ["Elena", 32, 1.70, True]
]

base = "escritura_datos.csv"

with open(base, mode="w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    
    escritor.writerow(["Nombre", "Edad", "Altura", "Es Estudiante"])
   
    escritor.writerows(datos)

print(f"Archivo CSV '{base}' creado exitosamente.")