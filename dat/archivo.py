import json

file_path = 'data.txt'  # Ruta al archivo
output_file = 'archivo.py'  # Nombre del nuevo archivo
names = []  # Lista para almacenar los nombres

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()  # Eliminar espacios en blanco
        
        if line:  # Verificar que la línea no esté vacía
            try:
                data = json.loads(line)  # Convertir la línea en JSON
                if 'name' in data:
                    names.append(data['name'])  # Agregar el nombre a la lista
            except json.JSONDecodeError:
                print(f"Error al leer la línea: {line}")

# Guardar los nombres en un nuevo archivo
with open(output_file, 'w', encoding='utf-8') as file:
    for name in names:
        file.write(name + "\n")

print(f"Los nombres han sido guardados en {output_file}")
