import random

## Suma 
def sumar(a, b, c):
    return a + b + c

## Promedio
def promedio(a, b, c):
    return (a + b + c) / 3

##  Menor
def menor(a, b, c):          
    menor = a
    if b < menor:
        menor = b
    if c < menor:
        menor = c
    return menor

## Mayor
def mayor(a, b, c):          
    mayor = a
    if b > mayor:
        mayor = b
    if c > mayor:
        mayor = c
    return mayor

## Asc 
def asc(a, b, c):
    numeros = [a, b, c]

    for i in range(len(numeros)):    
        for j in range(0, len(numeros) - i - 1):
            if numeros[j] > numeros[j + 1]:
                numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
    return numeros[0], numeros[1], numeros[2]