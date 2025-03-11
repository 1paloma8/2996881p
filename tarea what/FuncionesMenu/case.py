import random
 
lista = []

def llenarlista():
    for x in range(20):
        lista.append(random.randint(5, 20))
    return lista
    

## Suma 
def sumar():
    return sum(lista)

## Promedio
def promedio():
    return sum(lista) / len(lista)

##  Menor
def menorLista(lista):          
    menor = lista[0]
    sum=0
    for x in lista:
        if x < menor:
            menor = x
    return menor

## Mayor
print("--"*30)
def mayorLista(lista):          
    mayor = lista[0]
    sum=0
    for x in lista:
        if x > mayor:
            mayor = x
    return mayor


## Asc 



## Menú
sel = 1
while sel != 5:  # El bucle se sigue ejecutando hasta que sel sea 5
    # Mostrar el menú de opciones
    print("1-Sumar")
    print("2-Promedio")
    print("3-Mayor")
    print("4-Menor")
    print("5-Salir")

    # Obtener la opción del usuario
    sel = int(input("Seleccione Opcion: "))

    if sel != 5:  # Solo pedimos los números si no se seleccionó "salir"
        num1 = int(input("Numero 1: "))
        num2 = int(input("Numero 2: "))

        # Ejecutar la operación correspondiente utilizando match-case
        match sel:
            case 1:
                print(f"Resultado de la suma: {sumar(num1, num2)}")
            case 2:
                print(f"Promedio: {promedio(num1, num2)}")
            case 3:
                print(f"Mayor: {mayorLista(num1, num2)}")
            case 4:
                print(f"Menor: {menorLista(num1, num2)}")
            case _:
                print("Opcion equivocada")

print("¡Programa terminado!")
