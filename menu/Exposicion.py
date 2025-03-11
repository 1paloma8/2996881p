''' Archivo es un objeto que representa un espacio de memoria en el sistema de archivos de tu computadora. Los archivos pueden contener datos en diferentes formatos, como texto, imágenes, videos,etc..
un ejemplo de este seria :
.''' 
import csv

with open('mi_archivo.txt', 'w') as archivo:
    archivo.write("buenos dias .\n")
    archivo.write("¿como estas?.\n")
    archivo.write("good, aprendiendo archivos .")
    
    
with open('mi_archivo.txt', 'r') as archivo:
   arc = archivo.read(26)
   print(arc)
   

# Abrir el archivo CSV en modo lectura
with open('datos.csv', 'r') as archivo:
    lector = csv.reader(archivo)  # Crear un objeto lector
    for fila in lector:  # Iterar sobre cada fila
        print(fila)  # Cada fila es una lista de valores  

