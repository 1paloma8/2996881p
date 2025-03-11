import random

def tabla_edades(num_alumnos):
    """Genera una lista de edades aleatorias únicas entre 10 y 15."""
    edades = []
    for i in range(num_alumnos):
        edades.append(random.randint(10, 15))
    return edades

num_alumnos = 50
edades = tabla_edades(num_alumnos)

# ------------------------------------------------------------------------------
# Cálculo de frecuencias
# ------------------------------------------------------------------------------

frecuencias = {}
for edad in edades:
    if edad in frecuencias:
        frecuencias[edad] += 1
    else:
        frecuencias[edad] = 1

# ------------------------------------------------------------------------------
# Cálculo del total de frecuencias
# ------------------------------------------------------------------------------

total_frecuencias = 0
for edad in frecuencias:
    total_frecuencias += frecuencias[edad]

# ------------------------------------------------------------------------------
# Cálculo de frecuencias relativas
# ------------------------------------------------------------------------------

frecuencias_relativas = {}
for edad in frecuencias:
    frecuencias_relativas[edad] = frecuencias[edad] / total_frecuencias

# ------------------------------------------------------------------------------
# Cálculo del total de frecuencias relativa
# ------------------------------------------------------------------------------

total_frecuencias_relativas = 0
for edad in frecuencias:
    total_frecuencias_relativas += frecuencias_relativas[edad]

# ------------------------------------------------------------------------------
# Cálculo de porcentajes
# ------------------------------------------------------------------------------

porcentajes = {}
for edad in frecuencias:
    porcentajes[edad] = frecuencias_relativas[edad] * 100

# ------------------------------------------------------------------------------
# Cálculo del total de porcentaje
# ------------------------------------------------------------------------------

total_porcentajes = 0
for edad in frecuencias:
    total_porcentajes += porcentajes[edad]

# ------------------------------------------------------------------------------
# Cálculo de frecuencias acumuladas
# ------------------------------------------------------------------------------

frecuencias_acumuladas = {}
acumulado = 0
edades_ordenadas = sorted(frecuencias)
for edad in edades_ordenadas:
    acumulado += frecuencias[edad]
    frecuencias_acumuladas[edad] = acumulado

# ------------------------------------------------------------------------------
# Cálculo del total de frecuencia acumulada
# ------------------------------------------------------------------------------
total_frecuencias_acumuladas = 50

for edad in frecuencias:
    total_frecuencias_acumuladas 

# ------------------------------------------------------------------------------
# Impresión de la tabla de resultados
# ------------------------------------------------------------------------------

print("Edad | Frecuencia | Frecuencia Relativa | Porcentaje | Frecuencia Acumulada")
print("-------------------------------------------------------------------------------")

edades_ordenadas = sorted(frecuencias)
for edad in edades_ordenadas:
    print(f"{edad} | {frecuencias[edad]} | {frecuencias_relativas[edad]} | {porcentajes[edad]} % | {frecuencias_acumuladas[edad]}")

print("-------------------------------------------------------------------------------")
print(f"Total frecuencias: {total_frecuencias}")
print(f"Total frecuencias relativas: {total_frecuencias_relativas}")  
print(f"Total porcentajes: {total_porcentajes} %")  
print(f"Total frecuencias acumuladas: {total_frecuencias_acumuladas}")  