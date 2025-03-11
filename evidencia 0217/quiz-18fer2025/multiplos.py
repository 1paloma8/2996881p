def  rango(n1,n2):
    if n1<n2:
        while n1<n2:
            if n1% 7==0:
              print(f"{n1}factor de 7")
            else:
              print(n1)
              n1+=1 
        else:
            print("ciclo ascendente finalizado")    
            print("desde el else em el while")
            
    elif n1>n2:
        while n1> n2:
            print(n1)
        else:
           print(n1)
           n1-=1 
    else:
            print("ciclo descendente finalizado")    
            print("desde el else em el while")
                 
rango(1,15)     
      
      
      