numero =[]
def separar (x):
    while x > 0 :
        print (x % 10)
        numero.append (x % 10)
        x =x // 10
    print(numero[:])  
    
     
n= int(input("ingrese un numero : "))   
separar(n)