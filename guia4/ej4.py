import sys

def getMin(lista):
    min = lista[0]
    for n in lista:
        if n < min:
            min = n
    return min

def getMax(lista):
    max = lista[0]
    for n in lista:
        if n > max:
            max = n
    
    return max

def suma(lista):
    suma = 0
    for n in lista:
        suma += n
    return suma

def computeMean(lista):
    total = suma(lista)

    return total / len(lista)


# main

valores = [100, -12, 23, 4, 67, 32, 13]
print('El valor max de la lista es: ' + str(getMax(valores)))
print('El valor min de la lista es: ' + str(getMin(valores)))
print('El valor medio de la lista es: ' + str(computeMean(valores)))