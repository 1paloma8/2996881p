import random
def llenar_listarandom(lista,cantidad):
    lista=[]
    for i in  range (cantidad):
        num=random.randint(1,100)
        lista.append(num)
   
    return lista

vec =[]
tam= int(input("cuantos numeros ingreso a la lista"))
vec=llenar_listarandom(vec,tam)
print(vec)


