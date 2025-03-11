import random
lista = []

def llenarlista():
    for x in range(20):
        lista.append(random.randint(5, 20))
    return lista

def promedio():
    return sum(lista) / len(lista)

llenarlista()
resultado = promedio()
print("La lista es: ", lista)
print("El promedio es: ", resultado)