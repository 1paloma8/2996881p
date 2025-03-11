import random

# Función para llenar la lista con números aleatorios entre 1 y 100
def llenarListaRandom(cantidad):
    lista = []  # Se inicializa una lista vacía
    for _ in range(cantidad):  # Se repite el proceso la cantidad de veces indicada
        num = random.randint(1, 100)  # Se genera un número aleatorio entre 1 y 100
        lista.append(num)  # Se agrega el número a la lista
    return lista  # Se retorna la lista llena

# Función para calcular la moda sin usar Counter
def calcularModa(lista):
    frecuencia = {}  # Diccionario para contar la cantidad de veces que aparece cada número
    
    # Se recorre la lista y se cuenta la frecuencia de cada número
    for num in lista:
        if num in frecuencia:
            frecuencia[num] += 1  # Si ya existe en el diccionario, aumenta la cuenta
        else:
            frecuencia[num] = 1  # Si no existe, lo inicializa en 1

    # Encontrar el número con mayor frecuencia
    max_frecuencia = max(frecuencia.values())  # Encuentra la mayor frecuencia
    modas = [num for num, freq in frecuencia.items() if freq == max_frecuencia]  # Encuentra los números con esa frecuencia
    
    return modas, max_frecuencia  # Retorna la moda y su frecuencia

# Programa principal
cantidad_numeros = 50  # Se define cuántos números tendrá la lista
lista_aleatoria = llenarListaRandom(cantidad_numeros)  # Se genera la lista aleatoria
moda, frecuencia = calcularModa(lista_aleatoria)  # Se calcula la moda

# Se muestra el resultado
print("Lista de números aleatorios generada:")
print(lista_aleatoria)
print(f"\nModa(s): {moda} con una frecuencia de {frecuencia}")