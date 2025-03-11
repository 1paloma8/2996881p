def verificar_palabra(archivo):
    with open(archivo, 'r', encoding='utf-8') as file:
        contenido = file.read() 
   

    palabras = contenido.split()
    print("bienvenid@ busca tu palabra")
    print("="*60)
    palabra = input("Ingresa una palabra a buscar : ").lower()
     

    cantidad = 0
    for p in palabras:
        if p.lower() == palabra:
            cantidad += 1

    if cantidad > 0:
        print(f"Sí Aparece  dentro del himno {cantidad} veces.")
        print("="*60)
        print("¡¡ejercicio aprobado!!")
    else:
        print(f"no se encuentra dentro del himno intente nuevamente ")
        print("="*60)
        print("¡¡ejercicio  no aprobado!!")

verificar_palabra('himno.txt')

