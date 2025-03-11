def invertir_numero():
    """
    Solicita un número de hasta 9 dígitos y lo imprime en orden contrario.
    """
    try:
        numero_str = input("Ingresa un número de hasta 9 dígitos: ")

        if not numero_str.isdigit() or len(numero_str) > 9:
            raise ValueError("Entrada inválida. Ingresa un número de hasta 9 dígitos.")

        numero_invertido = numero_str[::-1]  # Invierte la cadena usando slicing

        print(f"El número invertido es: {numero_invertido}")

    except ValueError as e:
        print(f"Error: {e}")

invertir_numero()  # Llama a la función para ejecutar el programa

