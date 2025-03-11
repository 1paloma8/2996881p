import random

def llenarListaRandom(cantidad):
    """
    Función que genera una lista de números aleatorios entre 1 y 100.
    Se asegura de que cada número aparezca menos de 100 veces.
    """
    lista = []  # Creamos una lista vacía
    for _ in range(cantidad):  # Iteramos la cantidad de veces que queremos llenar la lista
        num = random.randint(1, 100)  # Generamos un número aleatorio entre 1 y 100
        lista.append(num)  # Agregamos el número a la lista
    return lista  # Retornamos la lista llena

def ordenarBurbuja(lista):
    """
    Función que ordena una lista de forma descendente usando el algoritmo de burbuja.
    """
    swapped = True  # Variable que indica si hubo intercambios en la iteración
    while swapped:  # Mientras haya intercambios, seguimos ordenando
        swapped = False  # Reiniciamos la variable en False
        for i in range(len(lista) - 1):  # Recorremos la lista hasta el penúltimo elemento
            if lista[i] < lista[i + 1]:  # Comparamos elementos adyacentes
                lista[i], lista[i + 1] = lista[i + 1], lista[i]  # Intercambiamos si están en el orden incorrecto
                swapped = True  # Indicamos que hubo un intercambio
    return lista  # Retornamos la lista ordenada

# Ejecutamos las funciones
cantidad_numeros = 20  # Definimos cuántos números tendrá la lista
lista_numeros = llenarListaRandom(cantidad_numeros)  # Llenamos la lista con números aleatorios
print("Lista original:", lista_numeros)  # Mostramos la lista antes de ordenar

lista_ordenada = ordenarBurbuja(lista_numeros)  # Ordenamos la lista en orden descendente
print("Lista ordenada:", lista_ordenada)  # Mostramos la lista ordenada

