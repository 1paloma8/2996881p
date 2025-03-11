try: 
    print(10/0)
except Exception as fallo:
    print(fallo)
    print("No puede dividir por cero")


lista = []

file = r"archivos\prueba1.txt"  

with open(file, mode='w', encoding="utf-8") as stream:
    stream.write("Este es mi código\n")
    stream.write("Aquí puedes escribir más contenido\n")

print("Archivo escrito con éxito.")

