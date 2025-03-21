# Importar el módulo csv para trabajar con archivos CSV
import csv

# Crear una lista de diccionarios con los datos
datos = [
    {"Nombre": "Juan", "Edad": 25, "Altura": 1.75, "Es Estudiante": True},
    {"Nombre": "Ana", "Edad": 30, "Altura": 1.62, "Es Estudiante": False},
    {"Nombre": "Luis", "Edad": 22, "Altura": 1.80, "Es Estudiante": True},
    {"Nombre": "Maria", "Edad": 28, "Altura": 1.68, "Es Estudiante": False},
    {"Nombre": "Carlos", "Edad": 35, "Altura": 1.90, "Es Estudiante": True},
    {"Nombre": "Laura", "Edad": 20, "Altura": 1.55, "Es Estudiante": True},
    {"Nombre": "Pedro", "Edad": 40, "Altura": 1.78, "Es Estudiante": False},
    {"Nombre": "Sofia", "Edad": 18, "Altura": 1.60, "Es Estudiante": True},
    {"Nombre": "Diego", "Edad": 27, "Altura": 1.85, "Es Estudiante": False},
    {"Nombre": "Elena", "Edad": 32, "Altura": 1.70, "Es Estudiante": True}
]


nombre_archivo = "datos_diccionario.csv"


with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo:
    
    columnas = datos[0].keys()
   
    escritor = csv.DictWriter(archivo, fieldnames=columnas)
    
    escritor.writeheader()
 
    escritor.writerows(datos)

print(f"Archivo CSV '{nombre_archivo}' creado exitosamente.")