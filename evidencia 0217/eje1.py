# Función para calcular el opuesto de un número
def opuesto(numero):
    return -numero
# Contador para llevar el número de entradas
contador = 0
print("Introduce números (termina con cero):")
while True:
    # Pedimos un número al usuario
    numero = int(input("Número: "))
    # Si el número es cero, terminamos el bucle
    if numero == 0:
        break
    # Calculamos y mostramos el opuesto
    opuesto_numero = opuesto(numero)
    print(f"{numero} opuesto es {opuesto_numero}")
    # Incrementamos el contador
    contador += 1
# Mostramos el número total de entradas
print(f"Se ingresaron {contador} números.")
                                                                                                                                                                      