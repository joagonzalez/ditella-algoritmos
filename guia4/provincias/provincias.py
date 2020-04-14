f = open("provincias.csv")

def listar_provincias(data):
    result = []
    for prov in data:
        if prov['poblacion'] >= 2000000:
            result.append(prov['provincia'])
    
    return result

def calcular_poblacion(data):
    result = 0
    for prov in data:
        result += prov['poblacion']

    return result

poblacion_argentina = []
for linea in f:
    aux = {}
    valores = linea.split(',')

    if valores[0] != 'Provincia':
        aux['provincia'] = valores[0]
        aux['poblacion'] = int(valores[3])

        poblacion_argentina.append(aux)

# print(poblacion_argentina)
print('Provincias con mas de 2M habitantes: ' + str(listar_provincias(poblacion_argentina)))
print('Poblacion total: ' + str(calcular_poblacion(poblacion_argentina)))