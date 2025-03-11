import random 
l1=[random.randint(1,10) for i in range(random.randint(5,15))]
l2=[random.randint(5,20) for i in range(random.randint(5,15))]
c1=set(l1)
c2=set(l2)
print(c1)
print(c2)


print(f"union{c1|c2}")
print(f"interseccion{c1&c2}")
print(f"diferencia{c1-c2}")
print(f"simetrica{c1^c2}")

cc1={1,2,3,4,5,6,7,8,9,10,11}
cc2={2,4,6,8}
print(100 in cc1)
print(cc2 <= cc1)
print(cc1 >= cc2)

