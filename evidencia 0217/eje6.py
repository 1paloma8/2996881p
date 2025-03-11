def comparar_numeros():
  """
  Compara tres números y determina si son todos iguales, dos son iguales o todos son distintos.
  """
  try:
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    num3 = int(input("Ingresa el tercer número: "))

    if num1 == num2 == num3:
      print("Los tres números son iguales.")
    elif num1 == num2 or num1 == num3 or num2 == num3:
      print("Hay dos números iguales.")
    else:
      print("Los tres números son distintos.")
  except ValueError:
    print("Entrada inválida. Por favor, ingresa números enteros.")

comparar_numeros()  # Llama a la función para ejecutar el programa

