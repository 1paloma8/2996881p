# Función para encontrar el número del medio entre tres números
def numero_del_medio(a, b, c):
    lista = [a, b, c]
    lista.sort()  # Ordenamos la lista
    return lista[1]  # El valor del medio será el segundo elemento después de ordenar
# Pedimos los tres números al usuario
a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))
c = int(input("Introduce el tercer número: "))
# Encontramos y mostramos el número del medio
valor_medio = numero_del_medio(a, b, c)
print(f"El valor del medio es {valor_medio}")
