import random

def llenarListaRandom(cantidad):
    """
    Esta función genera una lista de números aleatorios entre 1 y 100.
    La cantidad de números generados está determinada por el parámetro 'cantidad'.
    """
    lista = []
    for _ in range(cantidad):
        num = random.randint(1, 100)
        lista.append(num)
    return lista

def buscarNumero(lista, numero):
    """
    Esta función busca un número en la lista y devuelve:
    - Si el número está en la lista.
    - En qué posiciones se encuentra.
    - Cuántas veces aparece en la lista.
    """
    posiciones = [i for i, valor in enumerate(lista) if valor == numero]
    cantidad = len(posiciones)
    
    if cantidad > 0:
        print(f"El número {numero} se encuentra en la lista.")
        print(f"Posiciones: {posiciones}")
        print(f"Cantidad de veces que aparece: {cantidad}")
    else:
        print(f"El número {numero} no está en la lista.")

# Ejecución del programa
cantidad_numeros = 20  # Definir la cantidad de elementos en la lista
lista_numeros = llenarListaRandom(cantidad_numeros)
print("Lista generada:", lista_numeros)

numero_a_buscar = int(input("Ingrese el número a buscar: "))
buscarNumero(lista_numeros, numero_a_buscar)
