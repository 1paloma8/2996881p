import random
lista = []

def llenarlista():
    for x in range(20):
        lista.append(random.randint(5, 20))
    return lista

def mayorLista(lista):          
    mayor = lista[0]
    sum=0
    for x in lista:
        if x > mayor:
            mayor = x
    return mayor

llenarlista()
resultado = mayorLista(lista)

print("La lista es: ", lista)
print("El Numero Mayor de la Lista es: ", resultado)