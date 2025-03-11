
with open('himno.txt', 'r', encoding='utf-8') as file:
    contenido = file.read()  


mayusculas = 0
minusculas = 0


for caracter in contenido:
    if caracter.isupper():  # Si el carácter es mayúscula
        mayusculas += 1
    elif caracter.islower():  # Si el carácter es minúscula
        minusculas += 1


print(f"Mayúsculas: {mayusculas}")
print(f"Minúsculas: {minusculas}")





