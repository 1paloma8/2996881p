n = int(input("ingreses un numero :  "))

if n > 0 :
    if n > 99 and n < 1000 :
        c = n % 10
        n = n // 10
        b = n % 10
        a = n // 10
        
        
        print(f" la suma de los digitos es {a +b +c}")
     
    else:
        print(f"el numero {n} no es de tres digitos") 
else :
    print(f"el numero {n} no es positivo")          