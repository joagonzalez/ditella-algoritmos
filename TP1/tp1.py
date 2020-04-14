"""
  ______               _                            _                  _                 _                  _ _                       
 |  ____|             | |                          | |                | |          /\   | |                (_) |                      
 | |__ _   _ _ __   __| | __ _ _ __ ___   ___ _ __ | |_ ___  ___    __| | ___     /  \  | | __ _  ___  _ __ _| |_ _ __ ___   ___  ___ 
 |  __| | | | '_ \ / _` |/ _` | '_ ` _ \ / _ \ '_ \| __/ _ \/ __|  / _` |/ _ \   / /\ \ | |/ _` |/ _ \| '__| | __| '_ ` _ \ / _ \/ __|
 | |  | |_| | | | | (_| | (_| | | | | | |  __/ | | | || (_) \__ \ | (_| |  __/  / ____ \| | (_| | (_) | |  | | |_| | | | | | (_) \__ \
 |_|   \__,_|_| |_|\__,_|\__,_|_| |_| |_|\___|_| |_|\__\___/|___/  \__,_|\___| /_/    \_\_|\__, |\___/|_|  |_|\__|_| |_| |_|\___/|___/
                                                                                            __/ |                                     
                                                                                           |___/                                 

Agustin Alba Chicar
Joaquin Gonzalez
"""

import sys

"""
functions:
    esPrimo(n)
    iesimoPrimo(i)
    cantidadPrimosMenoresOIguales(n)
    cantidadDivisoresPrimos(n)
    iesimoDivisorPrimo(n, i)
    sumaPrimerosPrimos(n)
    divisores(n)
    suma(list)
    get_parameters(list)
"""

def divisores(n):
    divisores = []
    for i in range(1,n+1):
        if n % i == 0:
            divisores.append(i)

    return divisores

def esPrimo(n):
    result = False
    d = divisores(n)

    if n in d and len(d) == 2:
        result = True

    return result

def iesimoPrimo(i):
    primos = []
    count = 1

    while len(primos) != i:
        if esPrimo(count):
            primos.append(count)
        count += 1

    return  primos[len(primos)-1]

def cantidadPrimosMenoresOIguales(n):
    primos = []
    for num in range(n+1):
        if esPrimo(num):
            primos.append(num)
    
    return len(primos)

def cantidadDivisoresPrimos(n):
    d = divisores(n)
    result = []

    for divisor in d:
        if esPrimo(divisor):   
            result.append(divisor)

    return len(result)

def iesimoDivisorPrimo(n, i):
    d = divisores(n)
    primos = []

    for divisor in d:
        if esPrimo(divisor):
            primos.append(divisor)

    if i>len(primos):
        None
    else:
        return  primos[i-1]

def suma(n):
    result = 0
    for num in n:
        result += num
    
    return result

def sumaPrimerosPrimos(n):
    primos = []
    num = 1
    while len(primos) != n:
        if esPrimo(num):
            primos.append(num)
        num += 1
    
    return suma(primos)

def get_parameters():
    parameters = []
    for i in range(1, len(sys.argv)):
        parameters.append(sys.argv[i])

    return parameters

""" 
main body: get parameters and filter results by function
"""

parameters = get_parameters()
funcion = parameters[0]

if funcion == 'esPrimo':
    if esPrimo(int(parameters[1])):
        print('sí')
    else:
        print('no')
elif funcion == 'iesimoPrimo': 
    print(iesimoPrimo(int(parameters[1])))
elif funcion == 'cantidadPrimosMenoresOIguales': 
    print(cantidadPrimosMenoresOIguales(int(parameters[1])))
elif funcion == 'cantidadDivisoresPrimos': 
    print(cantidadDivisoresPrimos(int(parameters[1])))
elif funcion == 'iesimoDivisorPrimo': 
    if len(parameters) >= 2 and iesimoDivisorPrimo(int(parameters[1]),int(parameters[2])) != None:
        print(iesimoDivisorPrimo(int(parameters[1]),int(parameters[2])))  
    else: 
        print(str(parameters[1] + ' no tiene ' + str(parameters[1]) + ' divisores primos'))
elif funcion == 'sumaPrimerosPrimos': 
    print(sumaPrimerosPrimos(int(parameters[1])))
