import sys

def es_bisiesto(anio):
    result = False

    if ((anio % 400 == 0) or (anio % 4 == 0)) and (anio % 100 != 0):
        result = True
        print("entre!")

    return result

def imprimir_bisiestos(desde, hasta):
    for i in range(int(desde), int(hasta)+1):
        if es_bisiesto(i):
            print("el anio " + str(i) + " es bisiesto")

# main

desde = sys.argv[1]
hasta = sys.argv[2]

imprimir_bisiestos(desde, hasta)