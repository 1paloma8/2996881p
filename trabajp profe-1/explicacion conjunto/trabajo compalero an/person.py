import random

def generar_lista_aleatoria(n):
    return [random.randint(1, 100) for _ in range(n)]

def llenarlista(lista, x):
    pares = [num for num in lista if num % 2 == 0]  
    impares = [num for num in lista if num % 2 != 0]  #residuo 2 diferente o igual a 0"
    multiplos_x = [num for num in lista if num % x == 0] 
    return pares, impares, multiplos_x


n = int(input("¿Cuántos números quieres en la lista? "))
x = int(input("¿Qué número quieres usar para los múltiplos? "))

lista = generar_lista_aleatoria(n)
print(f"alea lista: {lista}")

# Clasificar los números
pares, impares, multiplos_x = llenarlista(lista, x)

# Mostrar los resultados
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Múltiplos de {x}: {multiplos_x}")

# Convertir listas a conjuntos para operaciones de conjuntos
set_pares = set(pares)
set_multiplos_x = set(multiplos_x)

# Realizar operaciones de conjuntos
print(f"Unión: {set_pares | set_multiplos_x}")
print(f"Intersección: {set_pares & set_multiplos_x}")
print(f"Diferencia (pares - múltiplos de x): {set_pares - set_multiplos_x}")
print(f"Diferencia simétrica: {set_pares ^ set_multiplos_x}")