import sys
import random

lista = []

def fill_list(max_value):
    for i in range(max_value):
        lista.append(random.randint(1,max_value))

    print(lista)

def booble_order(list):
    i = 0
    j = 0

    for i in range(len(list)-1):
        for j in range(len(list)-1):
            aux = list[j]

            if list[j+1] < list[j]:
                list[j] = list[j+1]
                list[j+1] = aux

    return list

if __name__ == '__main__':
    fill_list(10)
    print(booble_order(lista))    



