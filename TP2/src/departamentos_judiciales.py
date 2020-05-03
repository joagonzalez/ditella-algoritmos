import sys
import json
from dependencia_judicial import DependenciaJudicial, abrir_archivo

FOLDER = '../data/'

def bubble_sort(lista):
    """
    Implementacion de algoritmo Bubble Sort O(n^2)
    Se pueden ordenar las listas de dependencias por departamente 
    haciendo uso de la sobrecarga del operador < para los objetos
    de la clase DependenciaJudicial()
    """
    i = 0
    j = 0

    for i in range(len(lista)-1):
        for j in range(len(lista)-1):
            aux = lista[j]

            if lista[j+1] < lista[j]:
                lista[j] = lista[j+1]
                lista[j+1] = aux

    return lista

def formatear(dependencias):
    """
    Funcion que recibe una lista de objetos DependenciaJudicial y genera 
    una lista de diccionarios con key = departamento y value = lista de 
    dependencias y ese departamento. La lista estara ordenada por key
    """
    departamentos = set() # guardamos departamentos en conjunto, ya que no queremos elementos repetidos
    resultado = {}

    for dependencia in dependencias:
        departamentos.add(dependencia.departamento_judicial())

    for departamento in departamentos:
        dependencias_en_departamento = [] # inicializamos lista por cada iteracion de departamento
        for dependencia in dependencias:
            if departamento in dependencia.departamento_judicial():
                 dependencias_en_departamento.append(dependencia)
        resultado[departamento] = dependencias_en_departamento # se guardan todas las dependencias de un departamento en un diccionario key=deparamento

    return resultado

def guardar_dependencias(dependencias, filename):
    """
    Funcion que recibe como parametro una lista de dependencias correctamente
    formateadas y el nombre del archivo en el que se guardaran los resultados 
    """
    pass

# $ python3 departamentos_judiciales.py mapa-judicial.csv departamentos.txt
if __name__ == '__main__':
    try:
        SRC_FILENAME = FOLDER + sys.argv[1]
        DST_FILENAME = FOLDER + sys.argv[2]
    except Exception as e:
        print('Los parametros <SRC FILENAME> <DST LATITUD> no fueron ingresados correctamente. \n' + str(e))

    dependencias = abrir_archivo(SRC_FILENAME)
    dependencias_formateadas = formatear(dependencias)
    #print(dependencias_formateadas['AZUL'])
    for dependencia in dependencias_formateadas['AZUL']:
        print(dependencia)

    bubble_sort(dependencias_formateadas['AZUL']) # ordenamos dependencias de departamento azul
    print('#############################')
    for dependencia in dependencias_formateadas['AZUL']:
        print(dependencia)

    print(sorted(dependencias_formateadas.keys()))
    dependencias_ordenadas = sorted(dependencias_formateadas.keys())

    #print(dependencias_formateadas)
    #guardar_dependencias(dependencias, DST_FILENAME) # guardamos archivo con dependencias ordenadas y formateadas

