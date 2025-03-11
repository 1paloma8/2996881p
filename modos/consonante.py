
with open('himno.txt', 'r', encoding='utf-8') as file:
    contenido = file.read() 

consonantes = 0

consonantes_set = set('bcdfghjklmnpqrstvwxyz')

for caracter in contenido:
   
    if caracter.lower() in consonantes_set: 
        consonantes += 1

print(f"Consonantes: {consonantes}")