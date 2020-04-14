import sys

def buscar_mesetas(lista):
    result = {}
    i = 0
    for n in lista:
        if str(n) not in result:
            result[str(n)] = 1 # print(str(n) + ' no existe, agrego')
        elif n == lista[i-1] and i-1 >= 0:
            result[str(n)] += 1 # print('sumo 1 a ' + str(n))
        i += 1
    return result             

# main 
sec = [1, 1, 2, 6, 6, 6, 3, 3, 3, 3]

result = [(value, key) for key, value in buscar_mesetas(sec).items()]
print(str(result))
meseta_value, meseta_key = max(result) # se puede hacer funcion meseta_max recorriendo dict

print('la meseta mas grande de la lista es: ' + str(meseta_key) + ' con ' + str(meseta_value) + ' repeticiones')
