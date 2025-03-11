def contar_cifras():
    """
    Pide un número entre 0 y 9999 y dice cuántas cifras tiene.
    Si el número excede los límites, muestra un mensaje y termina.
    """
    try:
        numero = float(input("Ingresa un número entre 0 y 9999: "))
        if numero < 0 or numero > 9999:
            print("El número está fuera del rango permitido.")
            return  # Termina la función si el número está fuera de rango
        cantidad_cifras = len(str(numero).replace(".", ""))  # Cuenta las cifras sin el punto decimal
        print(f"El número {numero} tiene {cantidad_cifras} cifras.")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número válido.")
contar_cifras()  # Llama a la función para ejecutar el programa
