import sys
from random import randint

def crear_lista(cant_elem, rango):
    lista = []

    for i in range(cant_elem):
        lista.append(randint(0, rango))

    return lista

def encontrar_lista_desordenada(x, lista):  # O(len(lista))
    result = []                          # O(1)

    for i in lista:                      # O(len(lista))
        if int(x) >= i:                  # O(1)
            result.append(i)             # O(1)

    return result                        # O(1)

def encontrar_lista_ordenada(x, lista):
    # implementar busqueda binaria 
    pass

def bubble_sort(lista):                  # O(len(lista)^2)
    i = 0                                # O(1)
    j = 0                                # O(1)

    for i in range(len(lista)-1):        # O(len(lista))
        for j in range(len(lista)-1):    # O(len(lista))
            aux = lista[j]               # O(1)

            if lista[j+1] < lista[j]:    # O(1)
                lista[j] = lista[j+1]    # O(1)
                lista[j+1] = aux         # O(1)

    return lista                         # O(1)

if __name__ == '__main__':
    l = crear_lista(20, 50)
    print(l)

    print(encontrar_lista_desordenada(sys.argv[1], l))    

