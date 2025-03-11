
def  rango (n1,n2):
    if n1<n2:
        while n1<n2:
            print(n1)
            n1+=1 
        else:
            print("ciclo ascendente finalizado")    
            print("desde el else em el while")
            
    elif n1> n2:  
       while n1> n2:
            print(n1)
            n1-=1 
       else:
            print("ciclo descendente finalizado")    
            print("desde el else em el while")
                 
rango(100,50)     



      
        
"""num1=int(input("ingrese el primer numero "))
num2=int(input("ingrese el primer numero "))

print(f"los numeros son :, {num1},{num2}")"""