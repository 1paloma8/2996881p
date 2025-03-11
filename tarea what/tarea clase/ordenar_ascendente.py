import random

# Función para llenar una lista con números aleatorios entre 1 y 100
def llenarListaRandom(cantidad):
    lista = []  # Se crea una lista vacía
    for _ in range(cantidad):  # Se repite el proceso la cantidad de veces indicada
        num = random.randint(1, 100)  # Se genera un número aleatorio entre 1 y 100
        lista.append(num)  # Se agrega el número a la lista
    return lista  # Se devuelve la lista llena

# Función para ordenar una lista usando el método de ordenamiento burbuja
def ordenamientoBurbuja(lista):
    swapped = True  # Variable que indica si hubo intercambios
    while swapped:
        swapped = False  # Se inicia como False para verificar si hay intercambios
        for i in range(len(lista) - 1):  # Se recorre la lista hasta el penúltimo elemento
            if lista[i] > lista[i + 1]:  # Se comparan elementos adyacentes
                lista[i], lista[i + 1] = lista[i + 1], lista[i]  # Se intercambian si están en el orden incorrecto
                swapped = True  # Se marca como True para continuar iterando
    return lista  # Se devuelve la lista ordenada

# Bloque principal del programa
cantidad_numeros = 20  # Definir cuántos números queremos en la lista
lista_numeros = llenarListaRandom(cantidad_numeros)  # Llenar la lista con números aleatorios
print("Lista generada:", lista_numeros)  # Imprimir la lista original

lista_ordenada = ordenamientoBurbuja(lista_numeros)  # Ordenar la lista con el método burbuja
print("Lista ordenada:", lista_ordenada)  # Imprimir la lista ordenada