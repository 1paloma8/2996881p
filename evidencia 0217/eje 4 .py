import random
def adivina_el_numero():
  """
  Juego para adivinar un número aleatorio, indicando si el intento es mayor o menor.
  """
  numero_secreto = random.randint(1, 100)  # Genera un número aleatorio entre 1 y 100
  intentos = 0 # Inicializa el contador de intentos
  print("¡Bienvenido al juego de adivinar el número!")
  print("He generado un número secreto entre 1 y 100.")
  while True:
    try:
      intento = int(input("Ingresa tu intento: "))  # Pide al usuario un número
      intentos += 1  # Incrementa el contador de intentos
      if intento < numero_secreto:
        print("¡Demasiado bajo!")
      elif intento > numero_secreto:
        print("¡Demasiado alto!")
      else:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        break  # Sale del bucle cuando adivina el número
    except ValueError:
      print("Entrada inválida. Por favor, ingresa un número entero.")
adivina_el_numero()  # Llama a la función para iniciar el juego
