# un modulo es un archivo que contiene definiciones y sentencias  que puede importar mas tarde  y se utiliza cuando se necesario 
# el programador es un usuario y el modulo es un proveedor 
# usuario = emplea un mdulo existente 
# provedor = crea un modulo nuevo
# import es una palabra clave que permite importar modulos script de python
# tipos de modulos :
#     match : funciones matematicas 
#     Sys: manejo  archivos propios del sistema 
#     random: genera un numero a aleatorio 
# script es un archivo de codigo de fuente 
# un modulo es un namespace (cada archivo tiene su propio namespace)
#  los namespaces son una forma de organizar y aislar nombres en Python
# y los usas constantemente incluso sin darte cuenta cuando defines variables, funciones, clases o importas módulos


# Namespace global
x = 10  # 'x' está en el namespace global (x variable)

def mi_funcion():
    # Namespace local
    x = 5  # 'x' está en el namespace local de la función
    print(f"Dentro de la función, x = {x}")

mi_funcion()
print(f"Fuera de la función, x = {x}")


# ejemplo:
    # importamos el modulo random para generar numeros aleatorios
import random
    
# Generar un número aleatorio entre 1 y 10
numero_aleatorio = random.randint(1, 10)

# Mostrar el número generado
print(f"El número aleatorio generado es: {numero_aleatorio}")
