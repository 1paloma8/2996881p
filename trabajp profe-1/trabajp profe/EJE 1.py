
def llenarLista(lista, cantidad):
   
    num = 0
    for i in range(cantidad):
        num = int(input("Ingrese un número: "))
        lista.append(num)
    return lista

vector = []
vector = llenarLista(vector, 5)
print(vector)

suma = sum(vector)
print("La suma de los elementos de la lista es:", suma)



