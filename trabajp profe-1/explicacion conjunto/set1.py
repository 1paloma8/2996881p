
import random

conjunto={1}
# print(type(conjunto))
conjunto2=set([1,2,4])
lista=[random.randint(1,10) for i in range(20)]
# lista=(random.randint(1,10) for i in range(10)()
print(type(lista))
print(lista)
conjunto3= set (lista)
print(type(conjunto3))
print(conjunto3)

conjunto.update(lista)
print(f"conjunto update, {conjunto}")
print(f"{conjunto}")



