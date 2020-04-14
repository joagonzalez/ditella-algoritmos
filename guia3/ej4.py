import sys

def linea(n):
    for i in range(n):
        print('*', end='')
    print()

def cuadrado(n):
    for i in range(n): # lineas
        for j in range(n): # columnas
            if i == 0 or i == n-1:
                print('*', end='')
            else:
                if j == 0 or j == n-1:
                    print('*', end='')
                else: 
                    print(' ', end='')
        print()


def triangulo(n):
    for i in range(n): # lineas
        count = 0
        for j in range(n): # columnas
            while count <= i:
                if i == n-1: # si es ultima linea
                    print('*', end='')
                else:
                    if count == 0 or count == i:
                        print('*', end='')
                    else:
                        print(' ', end='')
                count += 1
        print()


# main
# python3 ej4.py a 20
# python3 ej4.py b 20
# python3 ej4.py c 20

n = None

try:
    punto = sys.argv[1]
    n = int(sys.argv[2])
except:
    print('ingresar parametros correctos!')

if n is not None:
    if punto == 'a':
        print('imprimo linea: ')
        linea(n)
    elif punto == 'b':
        print('imprimo cuadrado: ')
        cuadrado(n)
    elif punto == 'c':
        print('imprimo triangulo: ')
        triangulo(n)

