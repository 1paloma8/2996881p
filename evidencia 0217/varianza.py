def calcular_varianza(a,b):
    media=(a+b)/2
    varianza =(a - media)**2 + (b- media)/2
    return varianza 
a=5
b=6
"""num1= float(input("ingrese el primer numero"))
num2= float(input("ingrese del segundo numero"))"""
varianza=calcular_varianza(a,b)

print (f"la media de {a} y {b} es {varianza}")
