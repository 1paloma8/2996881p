def sumar(x,y):
    return x+y

def restar(x,y):
    return x-y

def multiplicar(x,y):
    return x*y

def dividir(x,y):
    return x/y

sel=1
while sel !=5:
    print("1-sumar")
    print("2-restar")
    print("3-multiplicar")
    print("4-dividir")
    print("5-salir")

    sel=int(input("Seleccione Opción"))

    num1=int(input("Numero 1"))
    num2=int(input("Numero 2"))
    match sel:
        case 1:
            print(sumar(num1,num2))
        case 2:
            print(restar(num1,num2))
        case 3:
            print(multiplicar(num1,num2))
        case 4:
            print(dividir(num1,num2))
        case 5:
            break
        case _:
            print("Opción Equiviocada")