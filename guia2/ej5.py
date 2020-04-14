"""> python.exe .\ej5.py 10000
Se han encontrado 4 numeros perfectos
[6, 28, 496, 8128]
"""
import sys

def suma(lista):
    result = 0
    for num in lista[1:]:
        result += num
    #print(result)
    #print(lista[1:])
    return result

def perfecto(n):
    divisores = []

    for i in range(n):
        if n % (n-i) == 0:
            divisores.append(n-i)

    print("Los divisores de " + str(n) + " son: " + str(divisores))
    if n == suma(divisores):
        return True
    else:
        return False
    
flag = False

try:
    num = int(sys.argv[1])
    flag = True
except:
    print('Ingrese un numero valido')
    exit

if flag:
    if perfecto(num):
        print("El numero es perfecto")
    else: 
        print("El numero no es perfecto")

count = 0
result = []
for i in range(num):
    if i != 0:
        if perfecto(i):
            print("el numero " + str(i) + " es perfecto!")
            count += 1
            result.append(i)
        else:
            print("el numero " + str(i) + " no es perfecto")
    
print("Se han encontrado " + str(count) + " numeros perfectos")
print(result)