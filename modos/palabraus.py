def verificar_palabra(archivo):
    with open(archivo, 'r', encoding='utf-8') as file:
        contenido = file.read()

    palabras = contenido.split()

    palabra = input("Ingresa una palabra: ")

    cantidad = palabras.count(palabra)

    if cantidad > 0:
        print(f"Sí está. Aparece {cantidad} veces.")
    else:
        print(f"No está. Tiene {len(palabra)} letras.")

verificar_palabra('himno.txt')