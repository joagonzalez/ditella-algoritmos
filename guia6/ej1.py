import sys
import random
from burbuja import booble_order

def crear_mazo(n):
    mazo = []

    for i in range(n):
        mazo.append(random.randint(1,n))
    
    return mazo

def esta_ordenado(mazo):
    result = True

    for i in range(0,len(mazo)-1):
        if mazo[i] > mazo[i+1]:
            print('comparo ' + str(mazo[i]) + '>' + str(mazo[i+1]))
            result = False
        
        if not result: break
    
    return result


if __name__ == '__main__':
    mazo = crear_mazo(50)
    print(mazo)
    print(esta_ordenado(mazo))
    mazo = booble_order(mazo)
    print(mazo)
    print(esta_ordenado(mazo))

    # por cada cofre en lista de cofres                        O(N)
        # esta_ordenado(mazo)                                  O(len(mazo)=M)
        # si esta ordenado salir                               O(1)
        # si no esta ordenado continuar con el siguiente cofre O(1)

    # O(N*M)