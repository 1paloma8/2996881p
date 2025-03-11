
with open('himno.txt', 'r', encoding='utf-8') as file:
    contenido = file.read() 

vocales = 0
vocales_set = set('aeiou')

for caracter in contenido:
   
    if caracter.lower() in vocales_set: 
       vocales+= 1

print(f"vocales: {vocales}")