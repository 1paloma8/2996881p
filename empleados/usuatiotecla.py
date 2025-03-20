import json

datos = {
    "usuario": input("Por favor, digite algo: ")}


# Abre el archivo en modo escritura y guarda los datos en formato JSON
with open("C:\\Users\\FORMACION.SIBAPRSESFSD058\\Documents\\prada\\empleados\\employees.json", 'w') as archivo:
    json.dump(datos, archivo)
print("="*90)
print("Los datos están guardados satifactoriamente.")