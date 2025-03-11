import random
 
lista = []

def llenarlista():
    for x in range(20):
        lista.append(random.randint(5, 20))
    return lista
    

## Suma 

def sumar():
    return sum(lista)

listallena= llenarlista()
suma = sumar()
print("La lista es:", listallena)
print("Cuando sumamos la lista el resultado es: ", suma)

