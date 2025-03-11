import random

def generar_edades(n):
    """
    Genera una lista de edades aleatorias entre 1 y 60.
    para n: Número de alumnos
    return: Lista de edades
    """
    edades = [random.randint(1, 60) for _ in range(n)]
    return edades

def calcular_frecuencia(edades, n):
    """
    Calcula la tabla de frecuencias.
    para edades: Lista de edades de los alumnos
    para n: Número de alumnos
    return: Listas con datos de la tabla de frecuencia
    """
    edades_unicas = sorted(set(edades))  # Lista ordenada con edades únicas
    f = [edades.count(edad) for edad in edades_unicas]  # Frecuencia absoluta
    fr = [freq / n for freq in f]  # Frecuencia relativa
    porcentaje = [rel * 100 for rel in fr]  # Porcentaje
    F = [sum(f[:i+1]) for i in range(len(f))]  # Frecuencia acumulada correctamente calculada
    
    return edades_unicas, f, fr, porcentaje, F

def mostrar_tabla(edades_unicas, f, fr, porcentaje, F):
    """
    Muestra la tabla de frecuencias.
    """
    print("+------+----+-------+-------+----+")
    print("| Edad |  f |   fr  |   %   |  F |")
    print("+------+----+-------+-------+----+")
    for i in range(len(edades_unicas)):
        print(f"| {edades_unicas[i]:4} | {f[i]:2} | {fr[i]:.3f} | {porcentaje[i]:6.2f} | {F[i]:2} |")
    print("+------+----+-------+-------+----+")
    print(f"| TOTAL | {sum(f):2} | 1.000 | 100.00 | -- |")
    print("+------+----+-------+-------+----+")

# Programa principal
n = int(input("Ingrese el número de alumnos: "))
edades = generar_edades(n)
edades_unicas, f, fr, porcentaje, F = calcular_frecuencia(edades, n)
mostrar_tabla(edades_unicas, f, fr, porcentaje, F)