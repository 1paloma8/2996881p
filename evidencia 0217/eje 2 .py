# Encontrar todas las ternas pitagóricas con lados menores o iguales a 500
def encontrar_ternas_pitagoricas(max_valor):
    ternas = []
    for a in range(1, max_valor + 1):
         for b in range(a, max_valor + 1): # Comenzamos desde &#39;a&#39; para evitar duplicados
             c = (a**2 + b**2)**0.5
             if c.is_integer() and c <= max_valor:
                ternas.append((a, b, int(c)))
    return ternas

# Definir el valor máximo
max_valor = 500

# Encontrar y mostrar las ternas pitagóricas
ternas = encontrar_ternas_pitagoricas(max_valor)
for terna in ternas:
    print(f"a={terna[0]}, b={terna[1]}, c={terna[2]}")