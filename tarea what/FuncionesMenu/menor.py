import random
lista = []

def llenarlista():
    for x in range(20):
        lista.append(random.randint(5, 20))
    return lista

def menorLista(lista):          
    menor = lista[0]
    sum=0
    for x in lista:
        if x < menor:
            menor = x
    return menor

llenarlista()
resultado = menorLista(lista)

print("La lista es: ", lista)
print("El Numero Menor de la Lista es: ", resultado)