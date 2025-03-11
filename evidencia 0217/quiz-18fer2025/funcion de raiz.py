#funcion que resuelva la formula cuadratica 
import math
def  resolver_cuadra(a,b,c):
    discriminante=b**2 -4*a*c

    if discriminante<0:
        return f"no _soluciones_reales"
    elif discriminante== 0:
        x =-b/(2*a)
        return f"solucion unica: x= {x} "
    else :
        x1=(-b +math.sqrt(discriminante))/ (2*a) 
        x2=(-b -math.sqrt(discriminante))/ (2*a) 
        return f"soluciones :x1 ={x1}, x2={x2}"
print(resolver_cuadra(1,-3,2))
