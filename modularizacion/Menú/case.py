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
print("Bienvenid@ a Nuestro Menú Estadístico. La carta del día es: ")
sel = 1
while sel != 5:  
    print("1-Sumar")
    print("2-Promedio")
    print("3-Mayor")
    print("4-Menor")
    print("5-Salir")

    sel = int(input("Seleccione la Opción de Preferencia: "))
    print("--"*30)
    if sel != 5: 
        llenarlista()
        match sel:
            case 1:
                print("La lista es: ", lista)
                print("--"*30)
                print(f"Resultado de la suma: {sumar()}")
                print("--"*30)
            case 2:
                print("La lista es: ", lista)
                print("--"*30)
                print(f"Promedio: {promedio()}")
                print("--"*30)
            case 3:
                print("La lista es: ", lista)
                print("--"*30)
                print(f"Mayor: {mayorLista(lista)}")
                print("--"*30)
            case 4:
                print("La lista es: ", lista)
                print("--"*30)
                print(f"Menor: {menorLista(lista)}")
                print("--"*30)
            case _:
                print("Opción equivocada")

print("¡Lamentamos que no te Haya Gustado el Menú!")
